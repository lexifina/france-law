"""French law as one git history: every version of every article in DILA's LEGI base, one commit per amending text per
day it took effect, streamed into git fast-import.

    python -X utf8 scripts/france-law/scan.py <LEGI full tar.gz> --db legi.sqlite        (first: read the full dump)
    python -X utf8 scripts/france-law/scan_daily.py scan <daily dir> --out daily-db         (the daily updates, in parallel)
    python -X utf8 scripts/france-law/scan_daily.py merge daily-db --db legi.sqlite
    python -X utf8 scripts/france-law/build.py --db legi.sqlite --repo ../france-law --docs-date YYYY-MM-DD \
        --archives <folder holding the full dump and daily/>

Layout: constitution/<text>/<article>.md, codes/<code>/<article>.md and textes/<nature>/<year>/<text>/<article>.md, one
file per article, with index.md in each text folder (written by the documentation commit).

A commit's author is the text that made the article versions it writes: the LEGI link, on the new article version, to
the text that created, modified, moved, codified or corrected it, signed on or before the day the version took effect
(the latest such signature wins). An article's first version with no such link, in a text that is not a code, is
credited to its own text. Versions LEGI gives no maker for are authored by the publisher, labelled. A version that ends
with no successor is removed on its end day in a commit credited to the successor's maker when there is one, otherwise
in a labelled "Fin de vigueur" commit.

Dates: noon in Paris on the day the version took effect (DATE_DEBUT). Dates before 1970 are clamped to 1970-01-01 UTC,
a second apart in order, with the real date in the In-force trailer (the on-date tool reads the trailer).
"""
import argparse
import datetime as dt
import hashlib
import json
import platform
import re
import sqlite3
import subprocess
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMMITTER = 'Lexifina <france-law@lexifina.com>'
PUBLISHER = 'Légifrance (DILA), version consolidée'
PUBLISHER_EMAIL = 'consolidation@legifrance.invalid'
ENDED = 'Fin de vigueur'
ENDED_EMAIL = 'fin-de-vigueur@legifrance.invalid'
FAR = '2999-01-01'
LEGIFRANCE = 'https://www.legifrance.gouv.fr'
CONSTITUTION = 'LEGITEXT000006071194'
# Links on an article version that name the text which made it. LEGI writes each relation from either end: a verb with
# sens="cible" (MODIFIE: the linked text modified this article) means the same as a noun with sens="source"
# (MODIFICATION). legi.py's TYPELIEN_MAP pairs them. A verb with sens="source" is the other way round: this article
# acting on the linked one.
MAKES = {('CREE', 'cible'), ('MODIFIE', 'cible'), ('TRANSFERE', 'cible'), ('DEPLACE', 'cible'), ('CODIFIE', 'cible'),
         ('RATIFIE', 'cible'), ('CREATION', 'source'), ('MODIFICATION', 'source'), ('TRANSFERT', 'source'),
         ('DEPLACEMENT', 'source'), ('CODIFICATION', 'source'), ('RATIFICATION', 'source'), ('RECTIFICATION', 'source')}
# Links that name the text which ended a version (repealed, annulled, lapsed), in both spellings.
ENDS = {('ABROGE', 'cible'), ('ANNULE', 'cible'), ('PERIME', 'cible'), ('DISJOINT', 'cible'), ('ABROGATION', 'source'),
        ('ANNULATION', 'source'), ('PEREMPTION', 'source'), ('DISJONCTION', 'source')}
SPACE = re.compile(r'\s+')


def last_sunday(year: int, month: int) -> dt.date:
    d = dt.date(year, month + 1, 1) - dt.timedelta(days=1) if month < 12 else dt.date(year, 12, 31)
    return d - dt.timedelta(days=(d.weekday() + 1) % 7)


def paris_offset(day: dt.date) -> int:
    """Hours ahead of UTC at noon in Paris: +1, and +2 in summer time (from 1976; to September until 1995, October since)."""
    if day.year < 1976:
        return 1
    end = last_sunday(day.year, 10 if day.year >= 1996 else 9)
    return 2 if last_sunday(day.year, 3) <= day < end else 1


def stamp(day: str, clamp: int) -> str:
    d = dt.date.fromisoformat(day)
    off = paris_offset(d)
    t = int(dt.datetime(d.year, d.month, d.day, 12 - off, tzinfo=dt.timezone.utc).timestamp())
    if t < 0:
        # git cannot store dates before 1970: clamped, a second apart in order, and kept before 1970-01-01 noon Paris.
        return f'{min(clamp, 39599)} +0000'
    return f'{t} +0{off}00'


def ascii_slug(s: str) -> str:
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    s = re.sub(r'[^A-Za-z0-9]+', '-', s).strip('-').lower()
    return s or 'x'


def article_slug(num: str, aid: str) -> str:
    """'L. 123-4' -> L123-4; 'Annexe I' -> Annexe-I; no number -> the LEGI id."""
    if not num:
        return aid
    s = unicodedata.normalize('NFKD', num).encode('ascii', 'ignore').decode()
    s = re.sub(r'\b([LRDA])\s*\.?\s*\*?\s*(?=\d)', r'\1', s)
    s = re.sub(r'[^A-Za-z0-9\-]+', '-', s).strip('-')
    return s[:80] or aid


def text_folder(t: dict) -> str:
    if t['id'] == CONSTITUTION:
        return 'constitution/constitution-1958'
    if t['nature'] == 'CONSTITUTION':
        return f"constitution/{ascii_slug(t['titre'])[:80]}"
    if t['nature'] == 'CODE':
        return f"codes/{ascii_slug(t['titre'])[:80]}"
    nature = ascii_slug(t['nature'] or 'texte')
    year = (t['date_texte'] or '0000')[:4]
    if t['num']:
        name = f"{nature}-{ascii_slug(t['num'])}"
    else:
        name = f"{nature}-{t['date_texte'] or ''}-{t['id'][-6:]}"
    return f'textes/{nature}/{year}/{name[:90]}'


def clean_title(s: str) -> str:
    s = SPACE.sub(' ', s or '').strip()
    s = re.sub(r'\s+-\s+art\..*$', '', s)
    s = re.sub(r',?\s+v\. init\.?$', '', s)
    s = re.sub(r'\s+art\..*$', '', s) if re.match(r'^\S+ \d', s) else s
    s = re.sub(r'\s+JORF .*$', '', s)
    return s.replace('<', '(').replace('>', ')').strip()


def makers_of(liens: list, debut: str, kinds: set = MAKES) -> tuple | None:
    """The text that made this article version (or, with kinds=ENDS and its end day, ended it): (cid, nature, num,
    signed), the link of that kind signed latest on or before the day. None if LEGI names none."""
    best = None
    for typelien, sens, cid, nature, numtexte, signed, _id, _num, _title in liens:
        if (typelien, sens) not in kinds or not cid or not cid.startswith(('JORFTEXT', 'LEGITEXT')):
            continue
        if signed and signed > debut:
            continue
        key = (signed or '', cid)
        if best is None or key > best[0]:
            best = (key, (cid, nature or '', numtexte or '', signed or ''))
    return best[1] if best else None


def render(num: str, aid: str, body: str, nota: str) -> bytes:
    """An article file: heading, the text, and LEGI's NOTA when there is one."""
    out = f'# Article {num or aid}\n\n{body}\n' if body else f'# Article {num or aid}\n'
    if nota:
        out += f'\nNOTA :\n\n{nota}\n'
    return out.encode('utf-8')


def blob_id(data: bytes) -> str:
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


def load(db: sqlite3.Connection, until: str, only: str | None = None) -> dict:
    """Everything the build and the check need, deterministically: texts and their folders, each article version with
    its path and maker, and the makers' names."""
    texts: dict[str, dict] = {}
    for tid, nature, cid, num, date_texte, date_publi, nor in db.execute(
            'select id, nature, cid, num, date_texte, date_publi, nor from struct order by id'):
        texts[tid] = {'id': tid, 'nature': nature or '', 'cid': cid or '', 'num': num or '', 'date_texte': date_texte or '',
                      'date_publi': date_publi or '', 'nor': nor or '', 'titre': '', 'titrefull': ''}
    for tid, titre, titrefull in db.execute('select id, titre, titrefull from version order by id'):
        if tid in texts:
            texts[tid]['titre'] = SPACE.sub(' ', titre or titrefull or '').strip()
            texts[tid]['titrefull'] = SPACE.sub(' ', titrefull or titre or '').strip()
    folders: dict[str, str] = {}
    used: dict[str, str] = {}
    for tid in sorted(texts):
        f = text_folder(texts[tid])
        if f in used:
            f = f'{f}-{tid[-6:]}'
        used[f] = tid
        folders[tid] = f
    rx = re.compile(only) if only else None

    titles: dict[str, list[str]] = {}       # maker cid -> the titles LEGI's links give it
    rows = []
    for aid, tid, num, debut, fin, liens, versions in db.execute(
            "select id, legitext, num, debut, fin, liens, versions from article where legitext != '' order by id"):
        if tid not in folders or not debut or debut >= FAR or debut > until or (fin and fin <= debut):
            continue
        if rx and not rx.search(folders[tid]):
            continue
        liens = json.loads(liens)
        vs = json.loads(versions) or [[aid, debut, fin, '', num]]
        chain = min(v[0] for v in vs if v[0])
        m = makers_of(liens, debut)
        if m:
            for typelien, sens, cid, _n, _nb, _s, _i, _a, title in liens:
                if cid == m[0] and (typelien, sens) in MAKES and title:
                    titles.setdefault(cid, []).append(clean_title(title))
        elif texts[tid]['nature'] != 'CODE' and debut == min(v[1] for v in vs if v[1]):
            t = texts[tid]
            m = (t['cid'] or tid, t['nature'], t['num'], t['date_texte'])
            titles.setdefault(m[0], []).append(clean_title(t['titre']))
        successor = sorted(v[0] for v in vs if v[1] == fin and v[0] != aid) if fin and fin < FAR else []
        end = makers_of(liens, fin, ENDS) if fin and fin < FAR else None
        if end:
            for typelien, sens, cid, _n, _nb, _s, _i, _a, title in liens:
                if cid == end[0] and (typelien, sens) in ENDS and title:
                    titles.setdefault(cid, []).append(clean_title(title))
        rows.append({'aid': aid, 'tid': tid, 'num': num or '', 'debut': debut, 'fin': fin or FAR, 'chain': chain,
                     'slug': article_slug(num or '', aid), 'maker': m, 'ender': end,
                     'successor': successor[0] if successor else ''})

    # Paths: one file per article number in its text. Two article chains with the same number in one text, in force at
    # the same time (an annex's article 1 beside the decree's), would overwrite each other: the later one gets its
    # chain id in its name.
    spans: dict[tuple, dict[str, list]] = {}
    for r in rows:
        s = spans.setdefault((r['tid'], r['slug']), {}).setdefault(r['chain'], [r['debut'], r['fin']])
        s[0], s[1] = min(s[0], r['debut']), max(s[1], r['fin'])
    path_of_chain: dict[tuple, str] = {}
    for (tid, slug), chains in sorted(spans.items()):
        placed: list[tuple] = []
        for chain, (a, b) in sorted(chains.items(), key=lambda kv: (kv[1][0], kv[0])):
            clash = any(a < pb and pa < b for pa, pb in placed)
            path_of_chain[(tid, chain)] = f'{folders[tid]}/{slug}.md' if not clash else f'{folders[tid]}/{slug}-{chain[-8:]}.md'
            if not clash:
                placed.append((a, b))
    for r in rows:
        r['path'] = path_of_chain[(r['tid'], r['chain'])]

    names: dict[str, str] = {}
    for cid, ts in titles.items():
        good = sorted({t for t in ts if t}, key=lambda t: (-ts.count(t), len(t), t))
        names[cid] = good[0][:200] if good else ''
    return {'texts': texts, 'folders': folders, 'rows': rows, 'names': names}


NATURES = {'LOI': 'Loi', 'LOI_ORGANIQUE': 'Loi organique', 'LOI_CONSTIT': 'Loi constitutionnelle', 'DECRET': 'Décret',
           'DECRET_LOI': 'Décret-loi', 'ARRETE': 'Arrêté', 'ORDONNANCE': 'Ordonnance', 'DECISION': 'Décision',
           'DELIBERATION': 'Délibération', 'CIRCULAIRE': 'Circulaire', 'CONSTITUTION': 'Constitution', 'CODE': 'Code'}
MONTHS = ('janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre',
          'décembre')


def french_date(day: str) -> str:
    y, m, d = day.split('-')
    return f'{"1er" if d == "01" else int(d)} {MONTHS[int(m) - 1]} {y}'


def law_name(m: tuple | None, names: dict) -> tuple[str, str]:
    """'Loi n° 2003-1312 du 30 décembre 2003', from LEGI's structured fields; the link title when they are missing."""
    if not m:
        return PUBLISHER, PUBLISHER_EMAIL
    cid, nature, num, signed = m
    label = NATURES.get(nature) or (nature.replace('_', ' ').capitalize() if nature else '')
    if label and re.fullmatch(r'\d{4}-\d{2}-\d{2}', signed or '') and signed < FAR:
        name = f'{label} n° {num} du {french_date(signed)}' if num else f'{label} du {french_date(signed)}'
    else:
        name = names.get(cid) or label or cid
    return name, f'{cid.lower()}@legifrance.invalid'


def texts_by_cid(plan: dict) -> dict[str, tuple]:
    """Each credited text's (cid, nature, num, signed), from the article versions that name it (by article id order)."""
    out: dict[str, tuple] = {}
    for r in sorted(plan['rows'], key=lambda r: r['aid']):
        for m in (r['maker'], r['ender']):
            if m:
                out[m[0]] = m
    return out


def events_of(plan: dict) -> list:
    """(day, group, kind, path, article id): a group is a maker cid, '' for no maker, '~' for end-of-force removals
    no text is credited with. Within a group removals sort before writes."""
    by_id = {r['aid']: r for r in plan['rows']}
    events = []
    for r in plan['rows']:
        m = r['maker']
        events.append((r['debut'], m[0] if m else '', 'M', r['path'], r['aid']))
        if r['fin'] < FAR and r['fin'] <= plan['until']:
            nxt = by_id.get(r['successor'])
            if nxt and nxt['debut'] == r['fin']:
                # Replaced by its successor, in place or renumbered: removed in the successor's commit (removals sort
                # before writes within a commit, so in place the file is simply rewritten).
                group = nxt['maker'][0] if nxt['maker'] else ''
            elif r['ender']:
                group = r['ender'][0]          # repealed, annulled or lapsed by a text LEGI names
            else:
                group = '~'
            events.append((r['fin'], group, 'D', r['path'], r['aid']))
    events.sort()
    return events


def replay(events: list):
    """The commits, in order: (day, group, {path: article id to write, or None to remove}), and finally the files in
    force at the end. Each path keeps the versions in force there, latest written last: a version ending while an
    earlier one (a LEGI overlap) is still in force puts that one back rather than removing the file."""
    in_force: dict[str, list[str]] = {}
    i = 0
    while i < len(events):
        day, group = events[i][0], events[i][1]
        j = i
        while j < len(events) and events[j][0] == day and events[j][1] == group:
            j += 1
        ops: dict[str, str | None] = {}
        for _, _, kind, path, aid in events[i:j]:
            stack = in_force.setdefault(path, [])
            if kind == 'D':
                if aid not in stack:
                    continue
                shown = stack[-1] == aid
                stack.remove(aid)
                if shown:
                    ops[path] = stack[-1] if stack else None
                if not stack:
                    del in_force[path]
            else:
                if aid in stack:
                    stack.remove(aid)
                stack.append(aid)
                ops[path] = aid
        i = j
        if ops:
            yield day, group, ops
    yield None, None, {p: st[-1] for p, st in in_force.items()}


def write(plan: dict, db: sqlite3.Connection, repo: Path, docs: dict, docs_date: str, events: list) -> dict:
    names = plan['names']
    makers = texts_by_cid(plan)
    subprocess.run(['git', 'init', '-q', '-b', 'main', str(repo)], check=True)
    fi = subprocess.Popen(['git', '-C', str(repo), 'fast-import', '--quiet', '--done'], stdin=subprocess.PIPE, bufsize=1 << 20)
    w = fi.stdin.write
    mark = clamp = 0
    body_of = db.cursor()
    tags: dict[str, int] = {}
    last_day = ''
    live: dict[str, str] = {}
    for day, group, ops in replay(events):
        if day is None:
            live = ops
            break
        mark += 1
        if group == '~':
            name, email = ENDED, ENDED_EMAIL
        else:
            name, email = law_name(makers.get(group), names)
        touched = sorted({p.rsplit('/', 1)[0] for p in ops})
        subject = name if len(name) <= 72 else name[:69] + '...'
        n_set = sum(1 for v in ops.values() if v is not None)
        n_del = len(ops) - n_set
        parts = []
        if n_set:
            parts.append(f'{n_set} article{"s" if n_set > 1 else ""} written')
        if n_del:
            parts.append(f'{n_del} article{"s" if n_del > 1 else ""} no longer in force')
        body = [', '.join(parts) + ' in ' + ', '.join(touched[:12]) + (f' and {len(touched) - 12} more' if len(touched) > 12 else '')]
        if group == '':
            body.append('LEGI names no text that made these versions; the commit is labelled as the publisher\'s.')
        elif group == '~':
            body.append('These versions end on this day and LEGI gives no successor; no text is credited.')
        trailers = [f'In-force: {day}']
        if group not in ('', '~'):
            m = makers[group]
            if m[3]:
                trailers.append(f'Signed: {m[3]}')
            trailers.append(f'Text: {LEGIFRANCE}/{"jorf" if group.startswith("JORF") else "loda"}/id/{group}')
        msg = f'{subject}\n\n' + '\n'.join(body) + '\n\n' + '\n'.join(trailers) + '\n'
        if day < '1970-01-01':
            clamp += 1
        when = stamp(day, clamp)
        w(f'commit refs/heads/main\nmark :{mark}\nauthor {name} <{email}> {when}\ncommitter {COMMITTER} {when}\n'.encode())
        b = msg.encode('utf-8')
        w(f'data {len(b)}\n'.encode() + b + b'\n')
        if mark > 1:
            w(f'from :{mark - 1}\n'.encode())
        for path in sorted(ops):
            aid = ops[path]
            if aid is None:
                w(f'D {path}\n'.encode())
                continue
            num, text, nota = body_of.execute('select num, body, nota from article where id = ?', (aid,)).fetchone()
            content = render(num, aid, text, nota)
            w(f'M 100644 inline {path}\ndata {len(content)}\n'.encode() + content + b'\n')
        if any(p.startswith('constitution/constitution-1958/') for p in ops):
            tags[f'constitution/{day}'] = mark       # the day's last commit
        last_day = day
        if mark % 20000 == 0:
            print(f'{day}: {mark} commits', flush=True)

    # The documentation commit: docs, tools and each text's index.md, dated the docs day, by Lexifina.
    mark += 1
    d = dt.date.fromisoformat(docs_date)
    when = f'{int(dt.datetime(d.year, d.month, d.day, 12 - paris_offset(d), tzinfo=dt.timezone.utc).timestamp())} +0{paris_offset(d)}00'
    msg = ('Documentation, index of texts and tools\n\nREADME.md, REPRODUCE.md, LICENSE, corpus.json, an index.md in each '
           'text folder, and tools/. No article file is changed.\n').encode('utf-8')
    w(f'commit refs/heads/main\nmark :{mark}\nauthor {COMMITTER} {when}\ncommitter {COMMITTER} {when}\n'.encode())
    w(f'data {len(msg)}\n'.encode() + msg + b'\n')
    if mark > 1:
        w(f'from :{mark - 1}\n'.encode())
    for path in sorted(docs):
        content = docs[path]
        w(f'M 100644 inline {path}\ndata {len(content)}\n'.encode() + content + b'\n')
    for tag, m in sorted(tags.items()):
        w(f'reset refs/tags/{tag}\nfrom :{m}\n\n'.encode())
    if last_day:
        w(f'reset refs/tags/legi/{plan["until"]}\nfrom :{mark - 1}\n\n'.encode())
    w(b'done\n')
    fi.stdin.close()
    if fi.wait():
        raise SystemExit('git fast-import failed')
    return {'commits': mark, 'law_commits': mark - 1, 'events': len(events), 'tags': len(tags) + (1 if last_day else 0),
            'last_day': last_day, 'live_files': len(live)}


# ---------------------------------------------------------------- documentation

def index_md(t: dict, folder: str, live: list[tuple[str, str]]) -> bytes:
    link = f'{LEGIFRANCE}/{"codes/texte_lc" if t["nature"] == "CODE" else "loda/id"}/{t["id"]}'
    lines = [f'# {t["titrefull"] or t["titre"] or t["id"]}', '']
    meta = [('Nature', t['nature'].title()), ('Numéro', t['num']), ('Date du texte', t['date_texte']),
            ('Publication au JORF', t['date_publi']), ('NOR', t['nor']), ('Identifiant LEGI', t['id']),
            ('Identifiant JORF', t['cid'] if t['cid'] != t['id'] else ''), ('Sur Légifrance', link)]
    for k, v in meta:
        if v and v != '2999-01-01':
            lines.append(f'- {k} : {v}')
    lines += ['', f'{len(live)} article{"s" if len(live) != 1 else ""} en vigueur dans ce dossier à la date du dernier '
              'commit de loi. Chaque fichier est un article ; `git log --follow` montre les textes qui l\'ont écrit.', '']
    return ('\n'.join(lines) + '\n').encode('utf-8')


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def fill(template: str, values: dict) -> str:
    for k, v in values.items():
        template = template.replace('{{' + k + '}}', str(v))
    left = re.findall(r'\{\{[A-Z_]+\}\}', template)
    if left:
        raise SystemExit(f'unfilled placeholders: {sorted(set(left))}')
    return template


def documents(plan: dict, stats: dict, args, live_paths: dict[str, list[tuple[str, str]]]) -> dict[str, bytes]:
    docs: dict[str, bytes] = {}
    tpl = HERE / 'repo'
    rows = plan['rows']
    history_from = min((r['debut'] for r in rows), default='')
    makers = texts_by_cid(plan)
    archives = []
    if args.archives:
        a = Path(args.archives)
        for p in sorted(a.glob('Freemium_legi_global_*.tar.gz')) + sorted((a / 'daily').glob('LEGI_*.tar.gz')):
            archives.append({'file': p.name, 'bytes': p.stat().st_size, 'sha256': sha256(p)})
    docs['data/archives.json'] = (json.dumps(archives, indent=1, ensure_ascii=False) + '\n').encode('utf-8')
    verification = {}
    vf = HERE / 'verification.json'
    if vf.exists():
        verification = json.loads(vf.read_text(encoding='utf-8'))
    n_codes = sum(1 for f in live_paths if f.startswith('codes/'))
    n_textes = sum(1 for f in live_paths if f.startswith('textes/'))
    values = {
        'DOCS_DATE': args.docs_date, 'UNTIL': plan['until'], 'HISTORY_FROM': history_from,
        'LAW_COMMITS': f'{stats["law_commits"]:,}', 'TAGS': f'{stats["tags"]:,}', 'MAKERS': f'{len(makers):,}',
        'VERSIONS': f'{len(rows):,}', 'TEXTS': f'{len(plan["folders"]):,}', 'LIVE_FILES': f'{stats["live_files"]:,}',
        'CODES': f'{n_codes:,}', 'TEXTES': f'{n_textes:,}', 'ARCHIVES': f'{len(archives):,}',
        'FULL_DUMP': archives[0]['file'] if archives else '(none given)',
        'LAST_DAILY': archives[-1]['file'] if len(archives) > 1 else '(none)',
        'CHECK': verification.get('check', {}).get('summary', 'not run for this build'),
        'SMOKE': verification.get('smoke', {}).get('summary', 'not run for this build'),
        'REBUILD': verification.get('rebuild', {}).get('summary', 'not run for this build'),
        'BUILD_BLOB': subprocess.run(['git', 'hash-object', str(HERE / 'build.py')], capture_output=True, text=True).stdout.strip(),
        'PYTHON': platform.python_version(),
        'GIT': subprocess.run(['git', '--version'], capture_output=True, text=True).stdout.strip(),
    }
    for name in ('README.md', 'REPRODUCE.md', 'LICENSE'):
        docs[name] = fill((tpl / name).read_text(encoding='utf-8'), values).encode('utf-8')
    corpus = json.loads((tpl / 'corpus.json').read_text(encoding='utf-8'))
    corpus.update({'history_from': history_from, 'record_to': stats['last_day'], 'built': args.docs_date,
                   'acts': {'texts': len(plan['folders']), 'with_articles_in_force': len(live_paths)}})
    docs['corpus.json'] = (json.dumps(corpus, indent=2, ensure_ascii=False) + '\n').encode('utf-8')
    for p in sorted((tpl / 'tools').glob('*.py')):
        docs[f'tools/{p.name}'] = p.read_bytes()
    for name in ('build.py', 'scan.py', 'scan_daily.py', 'check_repo.py', 'test_repo.py'):
        if (HERE / name).exists():
            docs[f'tools/{name}'] = (HERE / name).read_bytes()
    by_folder = {f: t for t, f in plan['folders'].items()}
    for folder in sorted(live_paths):
        docs[f'{folder}/index.md'] = index_md(plan['texts'][by_folder[folder]], folder, live_paths[folder])
    return docs


def live_at_end(events: list) -> dict[str, list[tuple[str, str]]]:
    """Each text folder's article files in force on the last day, from the same events the history is written from."""
    live: dict[str, str] = {}
    for day, _g, ops in replay(events):
        if day is None:
            live = ops
    out: dict[str, list[tuple[str, str]]] = {}
    for path in sorted(live):
        out.setdefault(path.rsplit('/', 1)[0], []).append((path, live[path]))
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--db', required=True)
    ap.add_argument('--repo', required=True)
    ap.add_argument('--docs-date', required=True, help='the documentation commit day: the day the data was retrieved')
    ap.add_argument('--until', help='leave out versions that take effect after this day (default: the docs date)')
    ap.add_argument('--only', help='a regex: build only text folders that match (testing)')
    ap.add_argument('--archives', help='the folder holding the full dump and daily/ (listed with sha256 in data/archives.json)')
    ap.add_argument('--checkout', action='store_true', help='check out a working tree (default: a bare repository)')
    args = ap.parse_args()
    repo = Path(args.repo)
    if repo.exists() and any(repo.iterdir()):
        raise SystemExit(f'{repo} is not empty')
    db = sqlite3.connect(args.db)
    plan = load(db, args.until or args.docs_date, args.only)
    plan['until'] = args.until or args.docs_date
    print(f'{len(plan["folders"])} texts, {len(plan["rows"])} article versions', flush=True)
    events = events_of(plan)
    live = live_at_end(events)
    # The documents carry the commit count, so the commits are counted before they are written.
    stats = {'law_commits': 0, 'tags': 0, 'last_day': '', 'live_files': sum(len(v) for v in live.values())}
    const_days: dict[str, bool] = {}
    for day, _group, ops in replay(events):
        if day is None:
            break
        stats['law_commits'] += 1
        stats['last_day'] = day
        if any(p.startswith('constitution/constitution-1958/') for p in ops):
            const_days[day] = True
    stats['tags'] = len(const_days) + 1
    docs = documents(plan, stats, args, live)
    out = write(plan, db, repo, docs, args.docs_date, events)
    if out['law_commits'] != stats['law_commits'] or out['tags'] != stats['tags']:
        print(f'note: documented {stats["law_commits"]} commits / {stats["tags"]} tags, wrote {out["law_commits"]} / {out["tags"]}',
              flush=True)
    if args.checkout:
        subprocess.run(['git', '-C', str(repo), 'checkout', '-q', 'main', '--', '.'], check=True)
    else:
        subprocess.run(['git', '-C', str(repo), 'config', 'core.bare', 'true'], check=True)
    print(json.dumps(out))


if __name__ == '__main__':
    main()

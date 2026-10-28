"""Read DILA's LEGI dump (every version of every consolidated French text and article) into one SQLite file.

    python -X utf8 scripts/france-law/scan.py <legi tar.gz> [more tar.gz: daily updates, oldest first] --db legi.sqlite

The tar is streamed and never unpacked (millions of small files are slow to write on Windows); its members are parsed
by every core in parallel. A later archive's version of a file replaces the earlier one, so a full dump followed by the
daily updates gives the current state. Files listed in an update's liste_suppression_legi.dat are deleted.
"""
import argparse
import multiprocessing as mp
import re
import sqlite3
import sys
import tarfile
import xml.etree.ElementTree as ET

ID = re.compile(r'(LEGITEXT|JORFTEXT)\d{12}')


def text_of(el: ET.Element | None) -> str:
    """CONTENU as plain text with paragraphs: <br/> and block elements become line breaks, tables become rows."""
    if el is None:
        return ''
    out: list[str] = []

    def walk(e: ET.Element) -> None:
        tag = e.tag.lower()
        if tag in ('p', 'div', 'tr', 'li', 'h1', 'h2', 'h3', 'h4', 'blockquote'):
            out.append('\n')
        if e.text:
            out.append(e.text)
        for c in e:
            if c.tag.lower() == 'br':
                out.append('\n')
            else:
                walk(c)
            if c.tail:
                out.append(c.tail)
        if tag in ('td', 'th'):
            out.append(' | ')
        if tag in ('p', 'div', 'tr', 'li', 'h1', 'h2', 'h3', 'h4', 'blockquote'):
            out.append('\n')

    walk(el)
    lines = [re.sub(r'[ \t ]+', ' ', l).strip() for l in ''.join(out).split('\n')]
    paras, blank = [], False
    for l in lines:
        if l:
            paras.append(l)
    return '\n\n'.join(paras)


def g(root: ET.Element, path: str) -> str:
    e = root.find(path)
    return (e.text or '').strip() if e is not None else ''


def parse(item: tuple[str, bytes]):
    """One member of the dump -> a row for the database, or None."""
    name, data = item
    m = ID.search(name)
    container = m.group(0) if m else ''
    try:
        root = ET.fromstring(data)
    except ET.ParseError as e:
        return ('error', name, str(e))
    if root.tag == 'ARTICLE':
        ctx = root.find('CONTEXTE/TEXTE')
        legitext = ''
        if ctx is not None:
            for t in ctx.findall('TITRE_TXT'):
                if (t.get('id_txt') or '').startswith('LEGITEXT'):
                    legitext = t.get('id_txt')
        liens = []
        for l in root.findall('LIENS/LIEN'):
            liens.append([l.get('typelien'), l.get('sens'), l.get('cidtexte'), l.get('naturetexte'), l.get('numtexte'),
                          l.get('datesignatexte'), l.get('id'), l.get('num'), (l.text or '').strip()])
        versions = [[v.get('id'), v.get('debut'), v.get('fin'), v.get('etat'), v.get('num')] for v in root.findall('VERSIONS/VERSION/LIEN_ART')]
        return ('article', g(root, 'META/META_COMMUN/ID'), container, legitext,
                g(root, 'META/META_SPEC/META_ARTICLE/NUM'), g(root, 'META/META_SPEC/META_ARTICLE/ETAT'),
                g(root, 'META/META_SPEC/META_ARTICLE/DATE_DEBUT'), g(root, 'META/META_SPEC/META_ARTICLE/DATE_FIN'),
                g(root, 'META/META_SPEC/META_ARTICLE/TYPE'), text_of(root.find('BLOC_TEXTUEL/CONTENU')),
                text_of(root.find('NOTA/CONTENU')), liens, versions)
    if root.tag == 'TEXTELR':      # a text's structure: its top-level sections and articles, with dates
        links = [[e.tag, e.get('id'), e.get('debut'), e.get('fin'), e.get('etat'), e.get('num') or (e.text or '').strip(), e.get('niv')]
                 for e in root.find('STRUCT') or []]
        return ('struct', g(root, 'META/META_COMMUN/ID'), container, g(root, 'META/META_COMMUN/NATURE'),
                g(root, 'META/META_SPEC/META_TEXTE_CHRONICLE/CID'), g(root, 'META/META_SPEC/META_TEXTE_CHRONICLE/NUM'),
                g(root, 'META/META_SPEC/META_TEXTE_CHRONICLE/DATE_TEXTE'), g(root, 'META/META_SPEC/META_TEXTE_CHRONICLE/DATE_PUBLI'),
                g(root, 'META/META_SPEC/META_TEXTE_CHRONICLE/NOR'), links)
    if root.tag == 'TEXTE_VERSION':
        mv = 'META/META_SPEC/META_TEXTE_VERSION/'
        return ('version', g(root, 'META/META_COMMUN/ID'), container, g(root, mv + 'TITRE'), g(root, mv + 'TITREFULL'),
                g(root, mv + 'ETAT'), g(root, mv + 'DATE_DEBUT'), g(root, mv + 'DATE_FIN'),
                text_of(root.find('VISAS/CONTENU')), text_of(root.find('SIGNATAIRES/CONTENU')))
    if root.tag == 'SECTION_TA':
        links = [[e.tag, e.get('id'), e.get('debut'), e.get('fin'), e.get('etat'), e.get('num') or (e.text or '').strip(), e.get('niv')]
                 for e in root.find('STRUCTURE_TA') or []]
        return ('section', g(root, 'ID'), container, g(root, 'TITRE_TA'), links)
    return None


def members(paths: list[str], deleted: list[str]):
    for p in paths:
        with tarfile.open(p, 'r|gz') as tar:
            for ti in tar:
                if ti.isfile() and ti.name.endswith('.xml'):
                    yield ti.name, tar.extractfile(ti).read()
                elif ti.isfile() and ti.name.endswith('liste_suppression_legi.dat'):
                    deleted.extend(tar.extractfile(ti).read().decode('utf-8').split())


SCHEMA = """
create table if not exists article (id text, container text, legitext text, num text, etat text, debut text,
  fin text, type text, body text, nota text, liens text, versions text);
create table if not exists struct (id text, container text, nature text, cid text, num text, date_texte text,
  date_publi text, nor text, links text);
create table if not exists version (id text, container text, titre text, titrefull text, etat text, debut text,
  fin text, visas text, signataires text);
create table if not exists section (id text, container text, titre text, links text);
create table if not exists error (name text, message text);
"""


def main() -> None:
    import json
    ap = argparse.ArgumentParser()
    ap.add_argument('archives', nargs='+')
    ap.add_argument('--db', required=True)
    ap.add_argument('--workers', type=int, default=max(1, mp.cpu_count() - 2))
    args = ap.parse_args()
    db = sqlite3.connect(args.db)
    # Rows are appended in dump order (a later archive's file after an earlier one's) and indexed at the end; a text
    # primary key made every insert a random B-tree write.
    db.executescript('pragma journal_mode=off; pragma synchronous=off; pragma cache_size=-1000000;' + SCHEMA)
    deleted: list[str] = []
    n = 0
    with mp.Pool(args.workers) as pool:
        for row in pool.imap_unordered(parse, members(args.archives, deleted), chunksize=256):
            if row is None:
                continue
            kind, *vals = row
            vals = [json.dumps(v, ensure_ascii=False) if isinstance(v, list) else v for v in vals]
            db.execute(f'insert into {kind} {"(name, message)" if kind == "error" else ""} values ({",".join("?" * len(vals))})', vals)
            n += 1
            if n % 100000 == 0:
                db.commit()
                print(f'{n} files', flush=True)
    print('indexing', flush=True)
    for t in ('article', 'struct', 'version', 'section'):
        # Keep only the last row read for each id (a daily update replaces the file), then index.
        db.execute(f'delete from {t} where rowid not in (select max(rowid) from {t} group by id)')
        db.execute(f'create unique index if not exists {t}_id on {t}(id)')
    db.execute('create index if not exists article_text on article(legitext)')
    for d in deleted:   # paths like legi/global/.../LEGIARTI000006850355 (no extension)
        m = re.search(r'(LEGI(ARTI|TEXT|SCTA)\d{12})$', d.strip())
        if m:
            for t in ('article', 'struct', 'version', 'section'):
                db.execute(f'delete from {t} where id = ?', (m.group(1),))
    db.commit()
    for t in ('article', 'struct', 'version', 'section', 'error'):
        print(t, db.execute(f'select count(*) from {t}').fetchone()[0])


if __name__ == '__main__':
    main()

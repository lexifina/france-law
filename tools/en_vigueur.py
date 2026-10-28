"""Prints an article, or a whole text, as it stood on a given day, from this repository's history.

    python tools/en_vigueur.py 2000-01-01 constitution-1958 89      # article 89 of the Constitution on 1 January 2000
    python tools/en_vigueur.py 2010-06-01 code-civil 1382           # article 1382 of the Code civil on 1 June 2010
    python tools/en_vigueur.py 2020-01-01 code-civil                # the whole Code civil on 1 January 2020
    python tools/en_vigueur.py 2020-01-01 codes/code-du-travail/L1234-1.md
    python tools/en_vigueur.py 2020-01-01 textes --list             # every file under textes/, with its blob id

A text is named by its folder (constitution/<name>, codes/<name>, textes/<nature>/<year>/<name>) or just its last part
when that is unambiguous. An article is its number as written ("L. 1234-1", "1382", "R*121-1"), or a file name.

Each law commit carries the day its change took effect in an `In-force:` trailer (git cannot store dates before 1970,
so the trailer, not the commit date, is the source of truth). The text in force on a day is the last commit whose
In-force day is on or before it. A folder holding more than 2,000 files is listed (path and blob id) rather than
printed; add --text to print it anyway. Standard library only; works in a bare clone.
"""
import datetime as dt
import re
import subprocess
import sys
import unicodedata

LIST_ABOVE = 2000


def git(*args: str) -> str:
    return subprocess.run(['git', *args], capture_output=True, text=True, encoding='utf-8', check=True).stdout


def article_slug(num: str) -> str:
    """The file name the build gives an article number: 'L. 123-4' -> L123-4."""
    s = unicodedata.normalize('NFKD', num).encode('ascii', 'ignore').decode()
    s = re.sub(r'\b([LRDA])\s*\.?\s*\*?\s*(?=\d)', r'\1', s)
    return re.sub(r'[^A-Za-z0-9\-]+', '-', s).strip('-')[:80]


def commit_on(day: str) -> str:
    """The last law commit in force on `day`. Commits after 1970 are dated noon in Paris on their In-force day, so git
    can find the candidate by date; the trailer confirms it. Earlier days are read from the clamped commits' trailers."""
    if day >= '1970-01-02':
        h = git('rev-list', '-1', f'--before={day}T23:59:59+02:00', 'main').strip()
        while h:
            body = git('log', '-1', '--format=%(trailers:key=In-force,valueonly,separator=)', h).strip()
            if body and body <= day:
                return h
            h = git('rev-list', '-1', f'{h}~1').strip() if git('rev-list', '--count', h).strip() != '1' else ''
        return ''
    out = git('log', '--before=1970-01-02T00:00:00Z', '--format=%H%x09%(trailers:key=In-force,valueonly,separator=)', 'main')
    for line in out.splitlines():
        h, _, d = line.partition('\t')
        if d.strip() and d.strip() <= day:
            return h
    return ''


def folder_of(commit: str, name: str) -> str:
    name = name.strip('/')
    if name.endswith('.md') or re.match(r'^(constitution|codes|textes)(/|$)', name):
        return name
    for top in ('constitution', 'codes'):
        if git('ls-tree', '--name-only', commit, f'{top}/{name}').strip():
            return f'{top}/{name}'
    hits = [l for l in git('ls-tree', '-r', '-d', '--name-only', commit, 'textes/').splitlines() if l.endswith('/' + name)]
    if len(hits) == 1:
        return hits[0]
    sys.exit(f'{name}: {"ambiguous: " + ", ".join(hits[:5]) if hits else "no such text"}')


def order(path: str) -> tuple:
    name = path.rsplit('/', 1)[1][:-3]
    return tuple((0, int(p), '') if p.isdigit() else (1, 0, p) for p in re.split(r'(\d+)', name) if p)


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if len(args) < 2:
        sys.exit(__doc__)
    day = args[0]
    dt.date.fromisoformat(day)
    commit = commit_on(day)
    if not commit:
        sys.exit(f'Nothing in the record is in force on {day}.')
    target = folder_of(commit, args[1])
    if len(args) > 2:
        target = f'{target}/{article_slug(args[2]) if not args[2].endswith(".md") else args[2]}'
        if not target.endswith('.md'):
            target += '.md'
    if target.endswith('.md'):
        try:
            sys.stdout.write(git('show', f'{commit}:{target}'))
        except subprocess.CalledProcessError:
            sys.exit(f'{target} was not in force on {day}.')
        return
    rows = [l.split('\t') for l in git('ls-tree', '-r', commit, target + '/').splitlines()]
    files = sorted(((meta.split()[2], path) for meta, path in rows if path.endswith('.md') and not path.endswith('/index.md')),
                   key=lambda r: (r[1].rsplit('/', 1)[0], order(r[1])))
    if not files:
        sys.exit(f'{target} has no article in force on {day}.')
    if '--list' in sys.argv or (len(files) > LIST_ABOVE and '--text' not in sys.argv):
        for blob, path in files:
            print(f'{path}\t{blob}')
        return
    batch = subprocess.run(['git', 'cat-file', '--batch'], input=''.join(f'{b}\n' for b, _ in files).encode(),
                           capture_output=True, check=True).stdout
    pos, texts = 0, []
    while pos < len(batch):
        nl = batch.index(b'\n', pos)
        size = int(batch[pos:nl].split()[2])
        texts.append(batch[nl + 1:nl + 1 + size].decode('utf-8'))
        pos = nl + 1 + size + 1
    sys.stdout.write('\n'.join(texts))


if __name__ == '__main__':
    main()

"""Prints the law of France as it stood on a given day, read from this repository's history.

    python tools/en_vigueur_au.py 2016-09-30 code-civil 1382     # art. 1382 the day before the 2016 reform
    python tools/en_vigueur_au.py 2016-10-01 code-civil 1240     # the same rule, renumbered art. 1240
    python tools/en_vigueur_au.py 2008-07-24 constitution 89     # art. 89 before the 2008 revision
    python tools/en_vigueur_au.py 2000-01-01 constitution        # the whole Constitution on 1 January 2000
    python tools/en_vigueur_au.py --law 2024-03-10 constitution 34  # also name the law behind that wording

A thin wrapper around tools/on.py: the version is chosen by each commit's `In-force:` trailer, never by its commit
date, and branches named wip* are ignored. An article number as Légifrance writes it (`515-11`, `R610-1`) is turned
into its file name (`art-0515-011`, `r-610-001`); `preambule` is the Preamble. Standard library only.
"""
import re
import runpy
import subprocess
import sys
from pathlib import Path


def article(act: str, unit: str) -> str:
    m = re.fullmatch(r'([LRDA])?\*?(\d+(?:-\d+)*)(?:-?([A-Za-z]+))?', unit.strip())
    if not m:
        return unit
    pre, nums, suf = m.groups()
    parts = nums.split('-')
    files = set()
    for ref in ('main', 'futur'):
        out = subprocess.run(['git', 'ls-tree', '-r', '--name-only', ref, f'{act}/'], capture_output=True,
                             text=True, encoding='utf-8')
        files.update(out.stdout.split())
    for width in (3, 4):
        key = ('art-' if not pre else pre.lower() + '-') + '-'.join([parts[0].zfill(width)] + [p.zfill(3) for p in parts[1:]])
        key += '-' + suf.lower() if suf else ''
        if f'{act}/{key}.md' in files:
            return key
    return unit


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    args = [a for a in sys.argv[1:] if a != '--law']
    if len(args) == 3:
        i = len(sys.argv) - 1 - sys.argv[::-1].index(args[2])
        sys.argv[i] = article(args[1], args[2])
    sys.argv[0] = str(Path(__file__).with_name('on.py'))
    runpy.run_path(sys.argv[0], run_name='__main__')

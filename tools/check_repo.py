"""Checks the built French law repository against the LEGI database it was built from.

    python -X utf8 scripts/france-law/check_repo.py --db legi.sqlite --repo ../france-law [--dates 1990-01-01,...] [--record]

For each date, the articles LEGI has in force that day (DATE_DEBUT <= day < DATE_FIN) are rendered exactly as the
build renders them and hashed as git blobs; the tree of the commit tools/en_vigueur.py picks for that day must hold
exactly those files with exactly those blob ids. Comparing ids compares every byte without reading the blobs back.
Default dates: the first of January every five years from 1960, the day before and the day of the last In-force day,
and the record's last day. Mismatches are listed by kind with examples; with --record the summary is written to
verification.json next to this script (REPRODUCE.md reports it).
"""
import argparse
import datetime as dt
import importlib.util
import json
import os
import sqlite3
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build  # noqa: E402

LAW_DIRS = ('constitution/', 'codes/', 'textes/')


def tool():
    spec = importlib.util.spec_from_file_location('en_vigueur', HERE / 'repo' / 'tools' / 'en_vigueur.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def compare(a: Path, b: Path, record: bool) -> None:
    def refs(repo: Path) -> tuple[str, str, str]:
        git = lambda *x: subprocess.run(['git', '-C', str(repo), *x], capture_output=True, text=True, check=True).stdout
        return git('rev-parse', 'main~1').strip(), git('rev-parse', 'main').strip(), git('show-ref', '--tags')
    (law_a, main_a, tags_a), (law_b, main_b, tags_b) = refs(a), refs(b)
    n_commits = subprocess.run(['git', '-C', str(a), 'rev-list', '--count', 'main~1'], capture_output=True, text=True).stdout.strip()
    same = law_a == law_b and main_a == main_b and tags_a == tags_b
    summary = (f'a second build from the same database into an empty folder gave the same history: last law commit '
               f'{law_a}, main {main_a}, all {n_commits} law commits and {len(tags_a.splitlines())} tags identical'
               if same else f'REBUILD DIFFERS: law commit {law_a} vs {law_b}, main {main_a} vs {main_b}, '
               f'tags {"same" if tags_a == tags_b else "differ"}')
    print(summary)
    if record:
        p = HERE / 'verification.json'
        rec = json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}
        rec['rebuild'] = {'summary': summary, 'same': same, 'law_commit': law_a, 'main': main_a}
        p.write_text(json.dumps(rec, indent=1, sort_keys=True, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    raise SystemExit(0 if same else 1)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--db', required=True)
    ap.add_argument('--repo', required=True)
    ap.add_argument('--until', help='as given to build.py (default: the In-force day of the last law commit)')
    ap.add_argument('--only', help='as given to build.py')
    ap.add_argument('--dates', help='comma-separated days to check')
    ap.add_argument('--record', action='store_true')
    ap.add_argument('--compare', metavar='OTHER_REPO', help='only compare main and every tag with a second build of the '
                    'same data (determinism); with --record, written as the rebuild result')
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    if args.compare:
        compare(Path(args.repo), Path(args.compare), args.record)
        return
    repo = Path(args.repo).resolve()
    db = sqlite3.connect(Path(args.db).resolve())
    os.chdir(repo)
    ev = tool()
    last = ev.git('log', '-1', '--format=%(trailers:key=In-force,valueonly,separator=)', 'main~1').strip()
    until = args.until or json.loads(ev.git('show', 'main:corpus.json'))['built']
    plan = build.load(db, until, args.only)
    if args.dates:
        dates = args.dates.split(',')
    else:
        days = ev.git('log', '-400', '--format=%(trailers:key=In-force,valueonly,separator=)', 'main~1').split()
        earlier = [d for d in days if d < last]
        dates = [f'{y}-01-01' for y in range(1960, int(last[:4]) + 1, 5)] + [last] + earlier[:1]
        # and every day the Constitution changed, each with the day before it
        for tag in ev.git('tag', '-l', 'constitution/*').split():
            day = tag.split('/', 1)[1]
            prev = (dt.date.fromisoformat(day) - dt.timedelta(days=1)).isoformat()
            dates += [day, prev]
    dates = sorted(set(dates))
    blob_of: dict[str, str] = {}
    cur = db.cursor()

    def blob(aid: str) -> str:
        if aid not in blob_of:
            num, body, nota = cur.execute('select num, body, nota from article where id = ?', (aid,)).fetchone()
            blob_of[aid] = build.blob_id(build.render(num, aid, body, nota))
        return blob_of[aid]

    results, total_files, total_bad = [], 0, 0
    examples: dict[str, list] = {}
    for day in dates:
        commit = ev.commit_on(day)
        expected: dict[str, list[str]] = {}
        for r in plan['rows']:
            if r['debut'] <= day < r['fin']:
                expected.setdefault(r['path'], []).append(r['aid'])
        have = {}
        if commit:
            for line in ev.git('ls-tree', '-r', commit).splitlines():
                meta, path = line.split('\t', 1)
                if path.startswith(LAW_DIRS) and not path.endswith('/index.md'):
                    have[path] = meta.split()[2]
        bad = {'missing': 0, 'extra': 0, 'differs': 0, 'two_versions_in_force': 0}
        for path in sorted(set(expected) | set(have)):
            want = expected.get(path)
            if want and len(want) > 1:
                bad['two_versions_in_force'] += 1
                if have.get(path) in [blob(a) for a in want]:
                    continue
                kind = 'two_versions_in_force'
            elif want is None:
                bad['extra'] += 1
                kind = 'extra'
            elif path not in have:
                bad['missing'] += 1
                kind = 'missing'
            elif have[path] != blob(want[0]):
                bad['differs'] += 1
                kind = 'differs'
            else:
                continue
            ex = examples.setdefault(kind, [])
            if len(ex) < 8:
                ex.append({'day': day, 'path': path, 'legi': want or []})
        # Two LEGI versions of one article both in force is LEGI's overlap, not a build error, when git holds one of them.
        errors = bad['missing'] + bad['extra'] + bad['differs']
        total_files += len(expected)
        total_bad += errors
        results.append({'day': day, 'commit': commit[:12], 'files': len(expected), **bad})
        print(f'{day} {commit[:10]}: {len(expected)} files, missing {bad["missing"]}, extra {bad["extra"]}, '
              f'differs {bad["differs"]}, LEGI overlaps {bad["two_versions_in_force"]}', flush=True)
    summary = (f'{len(dates)} dates checked ({total_files} article files), {total_bad} mismatches '
               f'(missing, extra or different); LEGI overlaps: {sum(r["two_versions_in_force"] for r in results)}')
    print(summary)
    for kind, ex in sorted(examples.items()):
        print(kind, json.dumps(ex[:3], ensure_ascii=False))
    if args.record:
        p = HERE / 'verification.json'
        rec = json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}
        rec['check'] = {'summary': summary, 'dates': results, 'examples': examples}
        p.write_text(json.dumps(rec, indent=1, sort_keys=True, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    raise SystemExit(1 if total_bad else 0)


if __name__ == '__main__':
    main()

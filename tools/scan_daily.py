"""Read DILA's daily LEGI updates in parallel, one archive per process, each into its own SQLite file; then merge them,
oldest first, into the database scan.py made from the full dump.

    python -X utf8 scripts/france-law/scan_daily.py scan <daily dir> --out <dir> [--workers 8]
    python -X utf8 scripts/france-law/scan_daily.py merge <dir> --db legi.sqlite

The full dump is read by one process (a gzip stream cannot be split), so the updates are read while it runs. A merge
applies each archive in date order: its files replace the earlier versions (by id), then its liste_suppression_legi.dat
deletions are applied, so a file deleted and later re-added ends up present.
"""
import argparse
import json
import multiprocessing as mp
import re
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from scan import SCHEMA, members, parse  # noqa: E402

TABLES = ('article', 'struct', 'version', 'section')


def scan_one(job: tuple[str, str]) -> str:
    archive, out = job
    done = Path(out + '.done')
    if done.exists():
        return archive
    tmp = Path(out + '.tmp')
    tmp.unlink(missing_ok=True)
    db = sqlite3.connect(tmp)
    db.executescript('pragma journal_mode=off; pragma synchronous=off;' + SCHEMA + 'create table deleted (id text);')
    deleted: list[str] = []
    for item in members([archive], deleted):
        row = parse(item)
        if row is None:
            continue
        kind, *vals = row
        vals = [json.dumps(v, ensure_ascii=False) if isinstance(v, list) else v for v in vals]
        db.execute(f'insert into {kind} {"(name, message)" if kind == "error" else ""} values ({",".join("?" * len(vals))})', vals)
    for d in deleted:
        m = re.search(r'(LEGI(ARTI|TEXT|SCTA)\d{12})$', d.strip())
        if m:
            db.execute('insert into deleted values (?)', (m.group(1),))
    db.commit()
    db.close()
    tmp.replace(out)
    done.touch()
    return archive


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)
    s = sub.add_parser('scan')
    s.add_argument('daily')
    s.add_argument('--out', required=True)
    s.add_argument('--workers', type=int, default=8)
    m = sub.add_parser('merge')
    m.add_argument('dir')
    m.add_argument('--db', required=True)
    args = ap.parse_args()
    if args.cmd == 'scan':
        Path(args.out).mkdir(parents=True, exist_ok=True)
        archives = sorted(Path(args.daily).glob('LEGI_*.tar.gz'))   # names are LEGI_YYYYMMDD-HHMMSS: sorted = date order
        jobs = [(str(a), str(Path(args.out) / (a.name[:-7] + '.sqlite'))) for a in archives]
        with mp.Pool(args.workers) as pool:
            for i, a in enumerate(pool.imap_unordered(scan_one, jobs), 1):
                print(f'{i}/{len(jobs)} {Path(a).name}', flush=True)
        return
    db = sqlite3.connect(args.db)
    db.executescript('pragma journal_mode=off; pragma synchronous=off; pragma cache_size=-1000000;')
    parts = sorted(Path(args.dir).glob('LEGI_*.sqlite'))
    for i, p in enumerate(parts, 1):
        if not Path(str(p) + '.done').exists():
            sys.exit(f'{p.name} is not finished; run scan first')
        db.execute('attach ? as d', (str(p),))
        for t in TABLES:
            # The full dump's ids are unique (scan.py indexed them), so a replace swaps in the newer version.
            db.execute(f'insert or replace into {t} select * from d.{t} where rowid in (select max(rowid) from d.{t} group by id)')
        for t in TABLES:
            db.execute(f'delete from {t} where id in (select id from d.deleted)')
        db.execute('insert into error select * from d.error')
        db.commit()
        db.execute('detach d')
        if i % 50 == 0 or i == len(parts):
            print(f'merged {i}/{len(parts)}', flush=True)
    for t in TABLES + ('error',):
        print(t, db.execute(f'select count(*) from {t}').fetchone()[0])


if __name__ == '__main__':
    main()

"""Rebuild visualisations/le-droit-francais-en-20-graphiques.html from this repository.

    python visualisations/src/make.py [--repo PATH] [--ref REF] [--skip-extract]

Steps (all read-only on the repository; scratch output goes to visualisations/src/.build/):
  1. git log of REF, streamed: one line per commit with its author (the text that made the change), its subject and
     the trailers the charts use (In-force, Signed, Text, Redates, Corrects)          -> .build/log.tsv
  2. git log --name-status of REF, streamed: one line per article file a commit writes or ends
                                                                                         -> .build/names.tsv
  3. the tree of REF: every file in force on the last day of the record                -> .build/tree.tsv
  4. the blobs the charts read, listed from the tree of REF:
     - every index.md (one per code, per Constitution and per text with articles in force: title, nature, number,
       dates, NOR)                                                                    -> .build/index.jsonl
     - the articles of the Constitution of 1958                                       -> .build/constitution.jsonl
     - corpus.json and the tables in data/ (archives.json, credits.csv, the corrections) -> .build/repo/
     - the current text of the 60 code articles with the most versions               -> .build/top-articles.jsonl
  5. prep.py turns those into .build/data.json; build.py fills page.tpl.html with it.
In a partial (blobless) clone the missing blobs are fetched in batches; nothing is held in memory at once: the
history is streamed line by line. About 120,000 small index.md blobs are read (some 50 MB of .git), and no article
text except the Constitution's and those 60 articles'.
"""
import argparse, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument('--repo', default=os.path.abspath(os.path.join(HERE, '..', '..')))
ap.add_argument('--ref', default=None, help='default: origin/main if present, else HEAD')
ap.add_argument('--out', default=os.path.join(HERE, '..', 'le-droit-francais-en-20-graphiques.html'))
ap.add_argument('--skip-extract', action='store_true', help='reuse .build/ from a previous run (prep and build only)')
a = ap.parse_args()
B = os.path.join(HERE, '.build')
os.makedirs(B, exist_ok=True)
NOLAZY = dict(os.environ, GIT_NO_LAZY_FETCH='1')
GIT = ['git', '-C', a.repo, '-c', 'core.quotepath=off']


def git(*args, **kw):
    return subprocess.run([*GIT, *args], check=True, capture_output=True, env=NOLAZY, **kw).stdout


ref = a.ref
if not ref:
    ref = 'origin/main' if subprocess.run(['git', '-C', a.repo, 'rev-parse', '--verify', '-q', 'origin/main'], capture_output=True).returncode == 0 else 'HEAD'
sha = git('rev-parse', ref).decode().strip()
print('ref', ref, sha)


def fetch_missing(oids, batch=20000):
    """batched fetches for the blobs a partial clone does not have yet"""
    oids = sorted(set(oids))
    chk = subprocess.run([*GIT, 'cat-file', '--batch-check'], input=''.join(o + '\n' for o in oids).encode(),
                         capture_output=True, env=NOLAZY).stdout.decode().split('\n')
    missing = [l.split()[0] for l in chk if l.endswith(' missing')]
    for i in range(0, len(missing), batch):
        part = missing[i:i + batch]
        print('fetching', len(part), 'blobs', f'({i + len(part)} of {len(missing)})', flush=True)
        subprocess.run([*GIT, '-c', 'fetch.negotiationAlgorithm=noop', 'fetch', 'origin', '--no-tags', '--no-write-fetch-head',
                        '--recurse-submodules=no', '--filter=blob:none', '--stdin'], input=''.join(m + '\n' for m in part).encode(), check=False)


def read_blobs(items):
    """yield (path, bytes) for (oid, path) pairs, one blob at a time"""
    p = subprocess.Popen([*GIT, 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=NOLAZY)
    for oid, path in items:
        p.stdin.write((oid + '\n').encode()); p.stdin.flush()
        head = p.stdout.readline().split()
        if len(head) < 3:
            sys.exit('cannot read ' + path)
        data = p.stdout.read(int(head[2])); p.stdout.read(1)
        yield path, data
    p.stdin.close(); p.wait()


TRAILERS = ['In-force', 'Signed', 'Text', 'Redates', 'Corrects']
if not a.skip_extract:
    # 1. the history, streamed: one line per commit (a trailer that occurs more than once is joined with " ; ")
    fmt = '%x1e%H%x1f%an%x1f%ae%x1f%aI%x1f%s%x1f%(trailers:unfold,separator=%x1d)'
    lg = subprocess.Popen([*GIT, 'log', ref, '--format=' + fmt], stdout=subprocess.PIPE, env=NOLAZY)
    n, buf = 0, b''
    with open(os.path.join(B, 'log.tsv'), 'w', encoding='utf-8', newline='\n') as out:
        out.write('\t'.join(['i', 'sha', 'author', 'email', 'date', 'subject'] + TRAILERS) + '\n')

        def emit(rec):
            global n
            rec = rec.decode('utf-8', 'replace').strip('\n')
            if not rec:
                return
            parts = rec.split('\x1f')
            tr = {}
            for t in (parts[5] if len(parts) > 5 else '').split('\x1d'):
                k, _, v = t.partition(': ')
                k = k.strip()
                if k:
                    tr.setdefault(k, []).append(v.strip())
            row = [str(n)] + parts[:5] + [' ; '.join(tr.get(k, [])) for k in TRAILERS]
            out.write('\t'.join(x.replace('\t', ' ').replace('\n', ' ') for x in row) + '\n')
            n += 1
        for chunk in iter(lambda: lg.stdout.read(1 << 16), b''):
            buf += chunk
            *recs, buf = buf.split(b'\x1e')
            for r in recs:
                emit(r)
        emit(buf)
    lg.wait()
    print('commits', n, flush=True)

    # 2. the files of each commit, streamed; the commit is its line number in log.tsv (0 = newest)
    lg = subprocess.Popen([*GIT, 'log', ref, '--format=@@C %h', '--name-status', '--no-renames'], stdout=subprocess.PIPE, env=NOLAZY)
    nf, ci = 0, -1
    with open(os.path.join(B, 'names.tsv'), 'w', encoding='utf-8', newline='\n') as out:
        for raw in lg.stdout:
            l = raw.decode('utf-8', 'replace').rstrip('\n')
            if l.startswith('@@C '):
                ci += 1
                continue
            if l and ci >= 0:
                st, _, f = l.partition('\t')
                out.write(f'{ci}\t{st[:1]}\t{f}\n')
                nf += 1
    lg.wait()
    print('file changes', nf, flush=True)

    # 3. the tree on the last day of the record
    nt, idx, const, tables = 0, [], [], []
    with open(os.path.join(B, 'tree.tsv'), 'w', encoding='utf-8', newline='\n') as out:
        lt = subprocess.Popen([*GIT, 'ls-tree', '-r', '-z', ref], stdout=subprocess.PIPE, env=NOLAZY)
        buf = b''
        for chunk in iter(lambda: lt.stdout.read(1 << 16), b''):
            buf += chunk
            *ents, buf = buf.split(b'\0')
            for e in ents:
                meta, path = e.split(b'\t', 1)
                _, typ, oid = meta.split()
                p = path.decode('utf-8')
                out.write(p + '\n')
                nt += 1
                if p.endswith('/index.md'):
                    idx.append((oid.decode(), p))
                elif p.startswith('constitution/constitution-1958/'):
                    const.append((oid.decode(), p))
                elif p in ('corpus.json', 'data/archives.json', 'data/credits.csv', 'data/metadata-corrections-signed-2999.json'):
                    tables.append((oid.decode(), p))
        lt.wait()
    print('files in the tree', nt, 'index.md', len(idx), 'constitution', len(const), 'tables', len(tables), flush=True)

    # 4. the blobs the charts read
    fetch_missing([o for o, _ in idx + const + tables])
    R = os.path.join(B, 'repo')
    for path, data in read_blobs(tables):
        dst = os.path.join(R, *path.split('/'))
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, 'wb') as fh:
            fh.write(data)

    def jsonl(name, items):
        with open(os.path.join(B, name), 'w', encoding='utf-8', newline='\n') as out:
            for path, data in read_blobs(items):
                out.write(json.dumps({'p': path, 't': data.decode('utf-8', 'replace')}, ensure_ascii=False) + '\n')
    jsonl('index.jsonl', idx)
    jsonl('constitution.jsonl', const)

    # 4b. the current text of the 60 code articles with the most versions (law commits only), for chart 14
    lex = set()
    with open(os.path.join(B, 'log.tsv'), encoding='utf-8') as fh:
        fh.readline()
        for line in fh:
            r = line.split('\t', 3)
            if r[2] == 'Lexifina':
                lex.add(int(r[0]))
    cnt = {}
    with open(os.path.join(B, 'names.tsv'), encoding='utf-8') as fh:
        for line in fh:
            ci, st, f = line.rstrip('\n').split('\t', 2)
            if st != 'D' and f.startswith('codes/') and not f.endswith('/index.md') and int(ci) not in lex:
                cnt[f] = cnt.get(f, 0) + 1
    top = sorted(cnt, key=lambda f: -cnt[f])[:60]
    del cnt
    ents = []
    for e in git('ls-tree', '-z', ref, '--', *top).split(b'\0'):
        if e:
            meta, path = e.split(b'\t', 1)
            ents.append((meta.split()[2].decode(), path.decode('utf-8')))
    fetch_missing([o for o, _ in ents])
    jsonl('top-articles.jsonl', ents)
    print('top articles', len(ents), flush=True)

# 5. prep + build
env = dict(os.environ, HEAD_SHA=sha)
subprocess.run([sys.executable, '-X', 'utf8', os.path.join(HERE, 'prep.py'), B], check=True, env=env)
subprocess.run([sys.executable, '-X', 'utf8', os.path.join(HERE, 'build.py'), os.path.join(B, 'data.json'), os.path.abspath(a.out)], check=True)

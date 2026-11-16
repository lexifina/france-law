"""Compute every number for the 20 charts into <build>/data.json.

    python prep.py <build-dir>

Reads, from <build> (written by make.py): log.tsv (one line per commit: its author, which is the text that made the
change, and its trailers), names.tsv (the article files each commit writes or ends), tree.tsv (every file in force on
the last day of the record), index.jsonl (the index.md of every code, Constitution and text with articles in force:
title, nature, number, dates, NOR), top-articles.jsonl (the current text of the code articles with the most versions)
and repo/ (corpus.json). Every rule that reads a category out of a name or a title is in this file.

A version is one article file written (status A or M) by a law commit; an article ends when a commit deletes its file
(status D). Dates are the commits' In-force and Signed trailers, with the corrections that later documentation commits
name in their Redates trailers. Documentation commits by Lexifina are not counted.
"""
import collections, json, os, re, statistics, sys
from datetime import date

B = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '.build')
OUT, PROFILE = {}, {}
D = lambda s: date.fromisoformat(s[:10])
RECORD_END = '2026-10-28'
LAST_FULL = 2025


def jl(name):
    with open(os.path.join(B, name), encoding='utf-8') as fh:
        for line in fh:
            yield json.loads(line)


def wmedian(pairs):
    """median of (value, weight) pairs"""
    pairs = sorted(pairs)
    tot = sum(w for _, w in pairs)
    if not tot:
        return None
    acc = 0
    for v, w in pairs:
        acc += w
        if acc * 2 >= tot:
            return v


def q(v, p):
    v = sorted(v)
    return v[min(len(v) - 1, max(0, int(round(p * (len(v) - 1)))))] if v else None


MOIS = {'janvier': 1, 'février': 2, 'fevrier': 2, 'mars': 3, 'avril': 4, 'mai': 5, 'juin': 6, 'juillet': 7, 'août': 8, 'aout': 8,
        'septembre': 9, 'octobre': 10, 'novembre': 11, 'décembre': 12, 'decembre': 12}

# ------------------------------------------------------------------ the history
# the kind of text that made each commit, read from its author's name (LEGI's nature, number and date of signature)
NATURES = [('Loi constitutionnelle', 'lc'), ('Loi organique', 'lo'), ('Loi', 'loi'), ('Ordonnance', 'ord'), ('Décret-loi', 'dec'), ('Décret', 'dec'),
           ('Arrêté', 'arr'), ('Décision', 'jug'), ('Légifrance (DILA)', 'dila'), ('Fin de vigueur', 'fin'), ('Lexifina', 'lex')]


def nature(author):
    for p, k in NATURES:
        if author.startswith(p):
            return k
    return 'aut'   # délibérations, avis, accords, circulaires, conventions, déclarations, rapports, the Constitutions themselves


SHA, AUTH, NAT, INF, SIG = [], [], [], [], []
redate_inf, redate_sig = {}, {}
with open(os.path.join(B, 'log.tsv'), encoding='utf-8') as fh:
    head = fh.readline().rstrip('\n').split('\t')
    for line in fh:
        r = dict(zip(head, line.rstrip('\n').split('\t')))
        SHA.append(r['sha'])
        AUTH.append(re.sub(r'\s+', ' ', re.sub(r'n°\s*', 'n° ', r['author'])).strip())
        NAT.append(nature(r['author']))
        INF.append(r['In-force'][:10])
        SIG.append(r['Signed'][:10])
        for rd in (r['Redates'].split(' ; ') if r['Redates'] else []):
            p = rd.split()
            if len(p) == 2 and re.match(r'^\d{4}-\d{2}-\d{2}$', p[1]):
                redate_inf[p[0]] = p[1]
            elif len(p) == 3 and p[1] == 'enacted':
                redate_sig[p[0]] = p[2] if re.match(r'^\d{4}-\d{2}-\d{2}$', p[2]) else ''
N = len(SHA)
SI = {s: i for i, s in enumerate(SHA)}
n_inf = n_sig = 0
for s, d in redate_inf.items():
    if s in SI and INF[SI[s]] != d:
        INF[SI[s]] = d; n_inf += 1
for s, d in redate_sig.items():
    if s in SI:
        SIG[SI[s]] = d; n_sig += 1
for i in range(N):   # LEGI's sentinel for an unknown signing date
    if SIG[i].startswith('2999'):
        SIG[i] = ''
LEX = [k == 'lex' for k in NAT]
print('commits', N, 'law commits', N - sum(LEX), 'in-force days corrected', n_inf, 'signing dates corrected', n_sig)
PROFILE.update(commits=N, law_commits=N - sum(LEX), head=os.environ.get('HEAD_SHA', ''), redated=n_inf)
assert all(re.match(r'^\d{4}-\d{2}-\d{2}$', INF[i]) for i in range(N) if not LEX[i]), 'a law commit without In-force'
bad_years = sorted({INF[i][:4] for i in range(N) if not LEX[i] and not ('1500' <= INF[i][:4] <= '2026')})
print('in-force years outside 1500-2026:', bad_years)

# laws: number -> (author name) and titles from index.md
INDEX = {}           # folder -> dict(title, nature, number, signed, published, nor, n)
for o in jl('index.jsonl'):
    t, p = o['t'], o['p']
    f = dict(re.findall(r'^- ([^:\n]+?) : (.*)$', t, re.M))
    m = re.search(r'^(\d+) articles? en vigueur', t, re.M)
    INDEX[p.rsplit('/', 1)[0]] = {'title': t.split('\n', 1)[0].lstrip('# ').strip(), 'nature': f.get('Nature', ''), 'number': f.get('Numéro', ''),
                                  'signed': f.get('Date du texte', ''), 'published': f.get('Publication au JORF', ''), 'nor': f.get('NOR', ''),
                                  'n': int(m.group(1)) if m else 0}
LAW_TITLE = {}       # 'loi:2016-1088' -> title (lois, lois organiques, ordonnances in force)
for folder, x in INDEX.items():
    if x['number'] and x['nature'] in ('Loi', 'Loi_Organique', 'Ordonnance', 'Loi_Constit'):
        LAW_TITLE[('ord:' if x['nature'] == 'Ordonnance' else 'loi:') + x['number']] = x['title']
NUM = re.compile(r'^(Loi(?: organique| constitutionnelle)?|Ordonnance) n°\s*(\d{2,4}-\d+)')


def law_key(author):
    m = NUM.match(author)
    if not m:
        return None
    return ('ord:' if m.group(1) == 'Ordonnance' else 'loi:') + m.group(2)


# ------------------------------------------------------------------ the files
def kind(f):
    """where an article file sits: the Constitution, a code, or a text of a nature"""
    if f.startswith('codes/'):
        return 'code'
    if f.startswith('constitution/'):
        return 'const'
    n = f.split('/')[1]
    return {'loi': 'loi', 'loi-organique': 'loi', 'loi-constit': 'loi', 'ordonnance': 'ord', 'decret': 'dec', 'decret-loi': 'dec', 'arrete': 'arr'}.get(n, 'aut')


def is_article(f):
    return f.endswith('.md') and not f.endswith('/index.md') and f.startswith(('codes/', 'constitution/', 'textes/'))


def folder(f):
    p = f.split('/')
    return '/'.join(p[:2]) if p[0] in ('codes', 'constitution') else '/'.join(p[:4])


HEAD = set()
TREE_N = collections.Counter()
TREE_FOLDER = collections.Counter()
with open(os.path.join(B, 'tree.tsv'), encoding='utf-8') as fh:
    for line in fh:
        f = line.rstrip('\n')
        if is_article(f):
            HEAD.add(f)
            TREE_N[kind(f)] += 1
            TREE_FOLDER[folder(f)] += 1
print('articles in force', len(HEAD), dict(TREE_N))
PROFILE['articles'] = len(HEAD)

# ------------------------------------------------------------------ one pass over the files of every commit (newest first)
YEARS = range(1500, 2027)
stock_d = collections.defaultdict(collections.Counter)       # kind -> in-force year -> +A -D
added = collections.defaultdict(collections.Counter)         # kind -> year -> articles added
ended = collections.defaultdict(collections.Counter)         # kind -> year -> articles ended
code_d = collections.defaultdict(collections.Counter)        # code -> year -> +A -D
code_v = collections.defaultdict(collections.Counter)        # code -> year -> versions
code_vn = collections.defaultdict(collections.Counter)       # code -> author nature -> versions since 2000
ver_year = collections.defaultdict(collections.Counter)      # year -> author nature -> versions
cal = collections.Counter()                                  # (month, day) -> versions 2000-2025
jan1 = collections.Counter()                                 # year -> versions that took effect on 1 January
wd_inf = collections.Counter()                               # weekday -> versions 2000-2025
cv = [0] * N                                                 # versions per commit
codeday = collections.defaultdict(collections.Counter)       # (code, day) -> author nature -> articles added
codeday_auth = collections.defaultdict(collections.Counter)  # (code, day) -> author -> articles added
pathv = collections.Counter()                                # code article -> versions
pathfirst = {}                                               # code article -> its oldest version day
law_codes = collections.defaultdict(collections.Counter)     # law -> code -> versions
law_own = collections.Counter()                              # law -> versions of its own articles
law_end = collections.Counter()                              # law -> code articles it ended
law_days = collections.defaultdict(collections.Counter)      # law -> in-force day -> versions (codes and its own text)
fin_cgi = collections.defaultdict(collections.Counter)       # 'cgi'/'css' -> (year, author kind)
age = collections.defaultdict(collections.Counter)           # kind -> year of the current wording -> articles
cc_rows = []                                                 # the Code civil's articles: (number, day, author)
oldest = []                                                  # the oldest wordings still in force
juge = collections.defaultdict(lambda: collections.Counter())  # decision -> (status, target) counts
const_ev = collections.defaultdict(lambda: collections.defaultdict(list))  # (day, author) -> status -> articles
folders_hist = collections.defaultdict(set)                  # kind -> text folders in the history
remaining = set(HEAD)
nfc = 0
with open(os.path.join(B, 'names.tsv'), encoding='utf-8') as fh:
    for line in fh:
        ci, st, f = line.rstrip('\n').split('\t', 2)
        i = int(ci)
        if LEX[i] or not is_article(f):
            continue
        nfc += 1
        k, a, inf, nat = kind(f), AUTH[i], INF[i], NAT[i]
        y = int(inf[:4])
        fo = folder(f)
        if fo not in folders_hist[k]:
            folders_hist[k].add(fo)
        if st == 'A':
            stock_d[k][y] += 1; added[k][y] += 1
        elif st == 'D':
            stock_d[k][y] -= 1; ended[k][y] += 1
        code = f.split('/')[1] if k == 'code' else None
        if code:
            code_d[code][y] += 1 if st == 'A' else -1 if st == 'D' else 0
        lk = law_key(a)
        if st == 'D':
            if lk and code:
                law_end[lk] += 1
            if nat == 'jug':
                juge[a][('D', f.split('/')[1] if code else k)] += 1
            if f.startswith('constitution/constitution-1958/'):
                const_ev[(inf, a)]['D'].append(f.rsplit('/', 1)[1][:-3])
            continue
        # a version (A or M)
        cv[i] += 1
        if lk:
            law_days[lk][inf] += 1
        ver_year[y][nat] += 1
        if inf[5:] == '01-01':
            jan1[y] += 1
        if 2000 <= y <= LAST_FULL:
            dd = D(inf)
            cal[(dd.month, dd.day)] += 1
            wd_inf[dd.weekday()] += 1
        if code:
            code_v[code][y] += 1
            if y >= 2000:
                code_vn[code][nat] += 1
            pathv[f] += 1
            pathfirst[f] = inf
            if st == 'A':
                codeday[(code, inf)][nat] += 1
                codeday_auth[(code, inf)][a] += 1
            if lk:
                law_codes[lk][code] += 1
            if code in ('code-general-des-impots-cgi', 'code-de-la-securite-sociale') and y >= 2000:
                fin_cgi['cgi' if 'impots' in code else 'css'][(y, lk or nat)] += 1
        elif lk:
            law_own[lk] += 1
        if nat == 'jug':
            juge[a][(st, code if code else k)] += 1
        if f.startswith('constitution/constitution-1958/'):
            const_ev[(inf, a)][st].append(f.rsplit('/', 1)[1][:-3])
        if f in remaining:   # the newest version of an article in force: its current wording
            remaining.discard(f)
            age[k][y] += 1
            if y < 1800:
                oldest.append((inf, f, a))
            if f.startswith('codes/code-civil/'):
                cc_rows.append((f.split('/')[2][:-3], inf, a))
print('article file changes', nfc, 'articles in force without a version found', len(remaining))
PROFILE['versions'] = sum(cv)
PROFILE['ended'] = sum(sum(v.values()) for v in ended.values())
PROFILE['texts_hist'] = sum(len(v) for v in folders_hist.values())
first_inf = min(INF[i] for i in range(N) if not LEX[i])
PROFILE['first_in_force'] = first_inf
PROFILE['record_end'] = RECORD_END
PROFILE['built'] = json.load(open(os.path.join(B, 'repo', 'corpus.json'), encoding='utf-8')).get('built', RECORD_END)
PROFILE['texts_in_force'] = len([x for x in INDEX.values() if x['nature'] not in ('Code', 'Constitution')])
PROFILE['codes'] = len([x for x in INDEX.values() if x['nature'] == 'Code'])
print('versions', PROFILE['versions'], 'texts in the history', PROFILE['texts_hist'])

KINDS = ['const', 'code', 'loi', 'ord', 'dec', 'arr', 'aut']

# ------------------------------------------------------------------ c01: what is in force
c01 = {'rows': []}
for k in KINDS:
    fol = [fo for fo in TREE_FOLDER if kind(fo + '/x.md') == k]
    big = max(fol, key=lambda fo: TREE_FOLDER[fo])
    c01['rows'].append({'k': k, 'texts': len(fol), 'arts': TREE_N[k], 'hist': len(folders_hist[k]),
                        'med': statistics.median([TREE_FOLDER[fo] for fo in fol]),
                        'big': [big, INDEX.get(big, {}).get('title', big), TREE_FOLDER[big]]})
# the natures inside "other texts", and the biggest texts outside the codes
oth = collections.Counter()
for fo in TREE_FOLDER:
    if kind(fo + '/x.md') == 'aut':
        oth[fo.split('/')[1]] += 1
c01['other_natures'] = oth.most_common()
c01['biggest'] = [[fo, INDEX.get(fo, {}).get('title', fo), n] for fo, n in sorted(((fo, n) for fo, n in TREE_FOLDER.items() if not fo.startswith(('codes/', 'constitution/'))), key=lambda x: -x[1])[:12]]
c01['cc'] = TREE_FOLDER['codes/code-civil']
c01['n'] = len(HEAD)
OUT['c01'] = c01

# ------------------------------------------------------------------ c02: the stock on 1 January of each year, and what came and went
def cum(d, years):
    s, out, ys = 0, [], sorted(d)
    j = 0
    for Y in years:
        while j < len(ys) and ys[j] < Y:
            s += d[ys[j]]; j += 1
        out.append(s)
    return out


SY = list(range(1980, 2027))
c02 = {'years': SY, 'stock': {k: cum(stock_d[k], SY) for k in KINDS}, 'end': {k: sum(stock_d[k].values()) for k in KINDS},
       'added': {k: [added[k][y] for y in SY] for k in KINDS}, 'ended': {k: [ended[k][y] for y in SY] for k in KINDS}}
assert sum(c02['end'].values()) == len(HEAD), (sum(c02['end'].values()), len(HEAD))
OUT['c02'] = c02

# ------------------------------------------------------------------ c03: the 77 codes and their parts
def part(fn):
    s = fn[:-3]
    if re.match(r'^LO\*?\d', s): return 'LO'
    if re.match(r'^L\*?\d', s): return 'L'
    if re.match(r'^R\*?\d', s): return 'R'
    if re.match(r'^D\*?\d', s): return 'D'
    if re.match(r'^A\*?\d', s): return 'A'
    if re.match(r'^\d', s): return 'N'
    return 'X'


parts = collections.defaultdict(collections.Counter)
for f in HEAD:
    if f.startswith('codes/'):
        parts[f.split('/')[1]][part(f.split('/')[2])] += 1
c03 = []
for code, c in parts.items():
    c03.append({'k': code, 'name': INDEX.get('codes/' + code, {}).get('title', code), **{p: c[p] for p in ['L', 'LO', 'R', 'D', 'A', 'N', 'X']}, 'n': sum(c.values())})
c03.sort(key=lambda r: -r['n'])
OUT['c03'] = c03

# ------------------------------------------------------------------ c04: how old the wording in force is
c04 = {'kinds': {}}
for k in KINDS:
    c04['kinds'][k] = sorted(age[k].items())
allyears = collections.Counter()
for k in KINDS:
    allyears.update(age[k])
tot = sum(allyears.values())
acc, med = 0, None
for yy in sorted(allyears):
    acc += allyears[yy]
    if med is None and acc * 2 >= tot:
        med = yy
c04['median'] = med
c04['n'] = tot
old = collections.defaultdict(lambda: [None, 0])
for inf, f, a in oldest:
    o = old[folder(f)]
    o[0] = min(o[0] or inf, inf); o[1] += 1
c04['oldest'] = [[fo, INDEX.get(fo, {}).get('title', fo), d0, n] for fo, (d0, n) in sorted(old.items(), key=lambda x: x[1][0])]
OUT['c04'] = c04
print('c04 median year of the current wording', med)

# ------------------------------------------------------------------ c05: the Code civil, article by article
def artkey(s):
    """'1240' < '1240-1' < '1241'; an article with letters sorts after its number"""
    out = []
    for p in re.split(r'[-\s]', s):
        m = re.match(r'^(\d+)(.*)$', p)
        out.append((int(m.group(1)), m.group(2)) if m else (10 ** 6, p))
    return out


cc_rows.sort(key=lambda r: artkey(r[0]))
cc_auth = collections.Counter(a for _, _, a in cc_rows)
OUT['c05'] = {'rows': [[n, inf, a] for n, inf, a in cc_rows], 'first': min(r[1] for r in cc_rows),
              'authors': [[a, n, LAW_TITLE.get(law_key(a) or '', '')] for a, n in cc_auth.most_common(12)]}

# ------------------------------------------------------------------ c06: who writes the versions
VY = list(range(1990, 2027))
NATS6 = ['loi', 'lo', 'lc', 'ord', 'dec', 'arr', 'jug', 'aut', 'dila']
c06 = {'years': VY, 'by': {n: [ver_year[y][n] for y in VY] for n in NATS6}}
top_codes = sorted(code_vn, key=lambda c: -sum(code_vn[c].values()))[:20]
c06['codes'] = [{'k': c, 'name': INDEX.get('codes/' + c, {}).get('title', c), **{n: code_vn[c][n] for n in NATS6}} for c in top_codes]
OUT['c06'] = c06

# ------------------------------------------------------------------ c07: the calendar
pub_wd = collections.Counter()
for x in INDEX.values():
    if x['published'] and x['published'][:4] >= '2000':
        try:
            pub_wd[D(x['published']).weekday()] += 1
        except ValueError:
            pass
OUT['c07'] = {'cal': [[m, d, n] for (m, d), n in sorted(cal.items())], 'wd_inf': [wd_inf[i] for i in range(7)], 'wd_pub': [pub_wd[i] for i in range(7)],
              'years': [2000, LAST_FULL], 'jan1': [[y, jan1[y], sum(ver_year[y].values())] for y in range(1990, 2027)]}

# ------------------------------------------------------------------ c08: from signature to entry into force
BK = [(-10 ** 6, -1, 'before'), (0, 1, 'd1'), (2, 7, 'd7'), (8, 30, 'd30'), (31, 182, 'm6'), (183, 365, 'y1'), (366, 10 ** 6, 'later')]
c08 = {}
pairs = collections.defaultdict(list)
for i in range(N):
    if LEX[i] or not cv[i] or not SIG[i] or NAT[i] not in ('loi', 'lo', 'ord', 'dec', 'arr'):
        continue
    if not ('1990' <= SIG[i][:4] <= '2026'):
        continue
    d = (D(INF[i]) - D(SIG[i])).days
    pairs[NAT[i]].append((d, cv[i]))
for n, pr in pairs.items():
    r = {'n': sum(w for _, w in pr), 'commits': len(pr), 'med': wmedian(pr)}
    for lo, hi, key in BK:
        r[key] = sum(w for d, w in pr if lo <= d <= hi)
    r['max'] = max(d for d, _ in pr)
    c08[n] = r
# the laws whose changes took effect latest after they were signed
late = []
for i in range(N):
    if not LEX[i] and cv[i] and SIG[i] and NAT[i] in ('loi', 'lo') and SIG[i][:4] >= '1990':
        late.append(((D(INF[i]) - D(SIG[i])).days, AUTH[i], INF[i], cv[i]))
c08['_late'] = [[d, a, inf, n] for d, a, inf, n in sorted(late, reverse=True)[:12]]
OUT['c08'] = c08

# ------------------------------------------------------------------ c09: from signature to the Journal officiel
c09 = {}
for nat_ in ('Loi', 'Ordonnance', 'Decret', 'Arrete'):
    by = collections.defaultdict(list)
    for x in INDEX.values():
        if x['nature'] != nat_ or not x['signed'] or not x['published']:
            continue
        try:
            s, p = D(x['signed']), D(x['published'])
        except ValueError:
            continue
        if 1990 <= s.year <= 2026 and 0 <= (p - s).days <= 3650:
            by[s.year].append((p - s).days)
    c09[nat_] = [[y, len(v), statistics.median(v), q(v, .25), q(v, .75), round(100 * sum(1 for d in v if d > 30) / len(v), 1)] for y, v in sorted(by.items())]
OUT['c09'] = c09

# ------------------------------------------------------------------ c10: the laws that wrote the most versions in the codes
CODIF = re.compile(r"partie législative|partie réglementaire", re.I)
laws = [lk for lk in law_codes if lk.startswith('loi:')]
laws.sort(key=lambda lk: -sum(law_codes[lk].values()))
c10, skipped = [], []
for lk in laws:
    t = LAW_TITLE.get(lk, '')
    if CODIF.search(t):
        skipped.append(lk); continue
    c10.append({'k': lk, 'title': t, 'codes': dict(law_codes[lk].most_common()), 'own': law_own[lk], 'ended': law_end[lk]})
    if len(c10) == 15:
        break
OUT['c10'] = {'rows': c10, 'skipped': skipped, 'laws': len(laws)}

# ------------------------------------------------------------------ c11: how the codes grew
GROW = ['code-de-la-sante-publique', 'code-du-travail', 'code-des-transports', 'code-de-l-environnement', 'code-de-commerce', 'code-de-la-securite-sociale',
        'code-civil', 'code-general-des-impots-cgi']
c11 = []
for code in GROW:
    ys = list(range(1950, 2027))
    st = cum(code_d[code], [y + 1 for y in ys])   # at the end of each year
    first = min(y for y in code_d[code])
    jumps = sorted(((day, sum(c.values())) for (cd, day), c in codeday.items() if cd == code), key=lambda x: -x[1])[:3]
    c11.append({'k': code, 'name': INDEX.get('codes/' + code, {}).get('title', code), 'years': ys, 'n': st, 'first': first, 'jumps': jumps,
                'now': TREE_FOLDER['codes/' + code]})
OUT['c11'] = c11

# ------------------------------------------------------------------ c12: the codes written in a day
c12 = []
for (code, day), c in codeday.items():
    n = sum(c.values())
    if n >= 1000 and day >= '1985':
        auth = codeday_auth[(code, day)].most_common()
        c12.append({'k': code, 'name': INDEX.get('codes/' + code, {}).get('title', code), 'day': day, 'n': n, 'by': dict(c), 'auth': auth[:4],
                    'now': TREE_FOLDER.get('codes/' + code, 0)})
c12.sort(key=lambda r: r['day'])
OUT['c12'] = c12

# ------------------------------------------------------------------ c13: the codes year by year
HY = list(range(1990, 2027))
top13 = sorted(code_v, key=lambda c: -sum(code_v[c][y] for y in HY))[:25]
OUT['c13'] = {'years': HY, 'rows': [{'k': c, 'name': INDEX.get('codes/' + c, {}).get('title', c), 'v': [code_v[c][y] for y in HY], 'first': min(code_v[c]),
                                     'now': TREE_FOLDER.get('codes/' + c, 0)} for c in top13]}

# ------------------------------------------------------------------ c14: the articles with the most versions
tops = {}
for o in jl('top-articles.jsonl'):
    tops[o['p']] = o['t']
OVERSEAS = re.compile(r"applicables?\b.{0,400}?(Nouvelle-Calédonie|Polynésie française|Wallis)", re.S)
REDAC = re.compile(r"dans (sa|leur) rédaction", re.I)
c14 = []
for f, n in pathv.most_common(40):
    if f not in HEAD:
        continue
    t = tops.get(f, '')
    body = t.split('\n', 2)[-1] if t else ''
    cls = 'om' if OVERSEAS.search(body[:1500]) and REDAC.search(body) else 'cgi' if f.startswith('codes/code-general-des-impots-cgi/') else 'other'
    c14.append({'p': f, 'code': f.split('/')[1], 'name': INDEX.get('codes/' + f.split('/')[1], {}).get('title', ''), 'n': n, 'first': pathfirst.get(f),
                'cls': cls, 'head': re.sub(r'\s+', ' ', body[:220]).strip()})
    if len(c14) == 20:
        break
OUT['c14'] = c14

# ------------------------------------------------------------------ c15: the finance laws and the two codes they rewrite most
def fin_kind(key):
    if isinstance(key, str) and key.startswith('loi:'):
        t = LAW_TITLE.get(key, '').lower()
        if 'financement de la sécurité sociale' in t or 'financement rectificative de la sécurité sociale' in t:
            return 'lfss'
        if re.search(r'de finances rectificative|de fin de gestion', t):
            return 'lfr'
        if re.search(r'\bde finances pour\b|\bloi de finances\b', t):
            return 'lf'
        return 'loi' if t else 'loi'
    if isinstance(key, str) and key.startswith('ord:'):
        return 'ord'
    return {'dec': 'dec', 'arr': 'arr', 'ord': 'ord', 'loi': 'loi', 'lo': 'loi', 'lc': 'loi'}.get(key, 'other')


c15 = {}
for code, cnt in fin_cgi.items():
    by = collections.defaultdict(collections.Counter)
    for (y, key), n in cnt.items():
        by[y][fin_kind(key)] += n
    c15[code] = [[y, dict(by[y])] for y in range(2000, 2027)]
# the finance laws themselves: each initial finance law and the versions it wrote in the CGI
lfs = []
for lk, cc in law_codes.items():
    t = LAW_TITLE.get(lk, '')
    m = re.match(r'^(?:LOI|Loi) n°\s*[\d-]+ du \d{1,2}(?:er)? \S+ \d{4} de finances pour (\d{4})', t, re.I)
    if m and lk.startswith('loi:'):
        signed = re.search(r' du (\d{1,2})(?:er)? (\S+) (\d{4})', t)
        sd = date(int(signed.group(3)), MOIS[signed.group(2)], int(signed.group(1))).isoformat() if signed and signed.group(2) in MOIS else ''
        td = law_days[lk].most_common(1)[0] if law_days[lk] else ['', 0]
        lfs.append([lk, int(m.group(1)), cc.get('code-general-des-impots-cgi', 0), sum(cc.values()), len(cc), sd, td[0], td[1]])
c15['lf'] = sorted(lfs, key=lambda r: r[1])
OUT['c15'] = c15

# ------------------------------------------------------------------ c16: lois and ordonnances, year by year
texts_y = collections.defaultdict(lambda: collections.defaultdict(set))
first_day = {}
for i in range(N):
    if LEX[i] or NAT[i] not in ('loi', 'lo', 'ord') or not SIG[i]:
        continue
    texts_y[int(SIG[i][:4])][NAT[i]].add(AUTH[i])
    first_day[AUTH[i]] = SIG[i]
c16 = {'years': list(range(1958, 2027))}
for n in ('loi', 'lo', 'ord'):
    c16[n] = [len(texts_y[y][n]) for y in c16['years']]
ord_days = collections.Counter(d for a, d in first_day.items() if a.startswith('Ordonnance'))
c16['ord_days'] = ord_days.most_common(6)
OUT['c16'] = c16

# ------------------------------------------------------------------ c17: the first words of the laws' titles
TITLE = re.compile(r"^(?:LOI|Loi)\b(?:\s+organique)?(?:\s+n°\s*[\d-]+)?(?:\s+organique)?\s+du\s+\d{1,2}(?:er)?\s+\S+\s+\d{4},?\s+(.*)$")
OPEN = [('fin', r"^(de finances|de financement|de règlement|relative aux résultats de la gestion|portant règlement définitif|d'approbation des comptes|de fin de gestion|spéciale prévue)"),
        ('traite', r"^autorisant\b"), ('visant', r"^(visant|tendant)\b"), ('relative', r"^(relative?s?|relatifs?)\b"), ('portant', r"^portant\b"),
        ('ratif', r"^(ratifiant|portant ratification)\b"), ('pour', r"^pour\b")]


def opening(t):
    m = TITLE.match(t)
    if not m:
        return None
    rest = m.group(1).strip().lower()
    for k, pat in OPEN:
        if re.search(pat, rest):
            return k
    return 'other'


c17 = collections.defaultdict(collections.Counter)
c17_ex = collections.defaultdict(list)
unread = 0
for fo, x in INDEX.items():
    if x['nature'] != 'Loi' or not x['signed']:
        continue
    k = opening(x['title'])
    if k is None:
        unread += 1; continue
    y = int(x['signed'][:4])
    c17[y][k] += 1
    if k == 'visant' and y >= 2024:
        c17_ex[y].append(x['title'])
OUT['c17'] = {'years': [[y, dict(c17[y])] for y in range(1958, 2027)], 'unread': unread, 'ex': {y: v[:6] for y, v in c17_ex.items()}}

# ------------------------------------------------------------------ c18: the décrets d'application
APP = re.compile(r"\b(?:pris|prise)\s+pour\s+l'application\b|\bportant application\b|\bpour l'application\b|\bd'application de\b|\brelatif à l'application\b|\bconditions d'application\b|\bmodalités d'application\b", re.I)
LAWREF = re.compile(r"\bloi(?: organique)?\s+n°\s*(\d{2,4}-\d+)\s+du\s+(\d{1,2})(?:er)?\s+([a-zéû]+)\s+(\d{4})", re.I)
first_dec = {}
ndec = collections.Counter()
for fo, x in INDEX.items():
    if x['nature'] != 'Decret' or not x['signed'] or not APP.search(x['title']):
        continue
    m = LAWREF.search(x['title'])
    if not m or m.group(3).lower() not in MOIS:
        continue
    try:
        ld = date(int(m.group(4)), MOIS[m.group(3).lower()], int(m.group(2)))
    except ValueError:
        continue
    key = m.group(1)
    ndec[key] += 1
    dd = D(x['signed'])
    if key not in first_dec or dd < first_dec[key][1]:
        first_dec[key] = (ld, dd, x['title'])
c18 = {'laws': sorted([[k, ld.isoformat(), dd.isoformat(), (dd - ld).days] for k, (ld, dd, t) in first_dec.items() if 2000 <= ld.year <= 2024 and dd >= ld],
                      key=lambda r: r[1]),
       'most': [[k, n, LAW_TITLE.get('loi:' + k, '')] for k, n in ndec.most_common(10)], 'decrees': sum(ndec.values())}
OUT['c18'] = c18

# ------------------------------------------------------------------ c19: the Constitution of 1958
c19 = []
for (inf, a), sts in sorted(const_ev.items()):
    c19.append({'day': inf, 'by': a, 'A': sorted(sts.get('A', []), key=artkey), 'M': sorted(sts.get('M', []), key=artkey), 'D': sorted(sts.get('D', []), key=artkey)})
OUT['c19'] = c19

# ------------------------------------------------------------------ c20: the judge in the text
c20 = []
for a, cnt in juge.items():
    m = re.match(r'^Décision n°\s*(\S+)(?:\s+(QPC|DC|L|LP|FNR))?', a)
    # the Conseil constitutionnel numbers its decisions <year>-<number> (QPC, DC ...), the Conseil d'État with five or six digits
    court = ('cc' if re.search(r'\b(QPC|DC)\b', a) or re.match(r'^Décision n°\s*(19|20)\d{2}-\d+(/\d+)*(\s|$)', a)
             else 'ce' if re.match(r'^Décision n°\s*\d{5,6}\b', a) else 'other')
    dm = re.search(r' du (\d{1,2})(?:er)? ([a-zéû]+) (\d{4})', a)
    day = None
    if dm and dm.group(2) in MOIS:
        day = date(int(dm.group(3)), MOIS[dm.group(2)], int(dm.group(1))).isoformat()
    c20.append({'a': a, 'court': court, 'day': day, 'M': sum(v for (s, t), v in cnt.items() if s == 'M'), 'D': sum(v for (s, t), v in cnt.items() if s == 'D'),
                'A': sum(v for (s, t), v in cnt.items() if s == 'A'), 'targets': collections.Counter({t: v for (s, t), v in cnt.items()}).most_common()})
c20.sort(key=lambda r: (r['day'] or '', r['a']))
OUT['c20'] = c20

# ------------------------------------------------------------------ the data profile
PROFILE['in_force_by_kind'] = dict(TREE_N)
PROFILE['index'] = len(INDEX)
PROFILE['laws_titled'] = len(LAW_TITLE)
json.dump({'charts': OUT, 'profile': PROFILE}, open(os.path.join(B, 'data.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('data.json', os.path.getsize(os.path.join(B, 'data.json')))

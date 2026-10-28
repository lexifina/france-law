"""Functional smoke test of the built French law repository: the things a reader does with it work. Standard library
only; works on a bare repository.

    python -X utf8 scripts/france-law/test_repo.py --repo ../france-law [--record]
    python -X utf8 tools/test_repo.py                   # from inside a checkout of the repository

It asserts that:
1. `git blame` on an article the Constitution's last change touched names a text as author of its lines;
2. tools/en_vigueur.py gives the text before and after that change, and each equals the file at and before the tag;
3. `git log --follow` on changed articles lists texts in the order they took effect;
4. every tag resolves to a commit, and every commit but the documentation commit has an `In-force:` trailer;
5. no commit is authored by Lexifina except the documentation commit (the last one), and no author name is a file name
   or a path (a builder bug once put `index.md` in the author field); every author email ends in `.invalid`;
6. every git or tool command in the README's table runs and prints something.
With --record the result is written to verification.json next to this script (for REPRODUCE.md).
"""
import argparse
import datetime as dt
import json
import re
import shlex
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PUBLISHERS = ('Légifrance (DILA), version consolidée', 'Fin de vigueur')
CONSTITUTION = 'constitution/constitution-1958/'


def default_repo() -> Path:
    if (HERE.parent / '.git').exists():
        return HERE.parent
    return HERE.parents[2] / 'france-law'


def bad_author(name: str) -> bool:
    """A file name or path in the author field: 'index.md', 'codes/code-civil/1240.md'. Text numbers may hold a slash
    ('Décision n° 2011-183/184 QPC'), so a slash alone is not a path; a slash with no space is."""
    return (not name.strip() or name == 'Lexifina' or bool(re.search(r'\.(md|json|csv|txt|py)$', name, re.I))
            or bool(re.fullmatch(r'\S*[/\\]\S*', name)) or '<' in name or '>' in name)


class Smoke:
    def __init__(self, repo: Path):
        self.repo = repo
        self.results: list[tuple[str, bool, str]] = []
        on_disk = repo / 'tools' / 'en_vigueur.py'
        self.tool_path = on_disk if on_disk.exists() else HERE / 'repo' / 'tools' / 'en_vigueur.py'
        self.target: tuple[str, str, str] | None = None

    def git(self, *args: str) -> str:
        out = subprocess.run(['git', *args], cwd=self.repo, capture_output=True, text=True, encoding='utf-8')
        if out.returncode:
            raise AssertionError(f'git {" ".join(args)}: {out.stderr.strip()}')
        return out.stdout

    def tool(self, *args: str) -> str:
        out = subprocess.run([sys.executable, '-X', 'utf8', str(self.tool_path), *args], cwd=self.repo, capture_output=True,
                             text=True, encoding='utf-8')
        if out.returncode:
            raise AssertionError(f'en_vigueur {" ".join(args)}: {out.stderr.strip()}')
        return out.stdout

    def check(self, name: str, fn):
        try:
            detail = fn() or ''
            self.results.append((name, True, detail))
            print(f'PASS {name}: {detail}')
        except AssertionError as exc:
            self.results.append((name, False, str(exc)))
            print(f'FAIL {name}: {exc}')

    def pick(self):
        """The latest Constitution tag whose commit changed an article that existed before it: (tag, path, day)."""
        if self.target:
            return self.target
        tags = sorted(self.git('tag', '-l', 'constitution/*').split(), reverse=True)
        assert tags, 'no constitution/* tags'
        for tag in tags:
            for path in self.git('show', '--format=', '--name-only', '--diff-filter=M', tag).split():
                if path.startswith(CONSTITUTION):
                    self.target = (tag, path, tag.split('/', 1)[1])
                    return self.target
        raise AssertionError('no Constitution change modifies an existing article')

    # 1
    def blame(self):
        tag, path, _ = self.pick()
        out = self.git('blame', '--line-porcelain', 'main', '--', path)
        authors = sorted({l[7:] for l in out.splitlines() if l.startswith('author ')})
        assert authors, 'no blame output'
        laws = [a for a in authors if a not in PUBLISHERS]
        assert laws, f'{path}: only {authors}'
        assert not [a for a in authors if bad_author(a)], f'{path}: bad authors {authors}'
        return f'{path} lines by {"; ".join(authors)}'

    # 2
    def on_date(self):
        tag, path, day = self.pick()
        before = (dt.date.fromisoformat(day) - dt.timedelta(days=1)).isoformat()
        art = path.rsplit('/', 1)[1][:-3]
        a, b = self.tool(before, 'constitution-1958', art), self.tool(day, 'constitution-1958', art)
        assert a and b and a != b, f'{path}: no change between {before} and {day}'
        assert b == self.git('show', f'{tag}:{path}'), f'{path} on {day} is not the file at {tag}'
        prev_day = self.git('log', '-1', '--format=%(trailers:key=In-force,valueonly,separator=)', f'{tag}~1').strip()
        if prev_day < day:
            assert a == self.git('show', f'{tag}~1:{path}'), f'{path} on {before} is not the file before {tag}'
        whole = self.tool(day, 'constitution-1958')
        assert '# Article 1\n' in whole, 'the whole Constitution lacks article 1'
        return f'{path} {before} != {day}; whole Constitution on {day}: {whole.count("# Article ")} articles'

    # 3
    def follow(self):
        tag, path, _ = self.pick()
        checked = []
        for p in sorted({path, CONSTITUTION + '1.md'}):
            out = self.git('log', '--follow', '--format=%an%x09%(trailers:key=In-force,valueonly,separator=)', 'main', '--', p)
            rows = [l.split('\t') for l in out.splitlines() if l]
            assert len(rows) >= 2, f'{p}: {len(rows)} commits'
            days = [d.strip() for _, d in rows]
            assert days == sorted(days, reverse=True), f'{p}: not in date order {days}'
            assert not [a for a, _ in rows if bad_author(a)], f'{p}: bad authors'
            checked.append(f'{p} {len(rows)} commits')
        return '; '.join(checked)

    # 4
    def tags_and_trailers(self):
        tags = self.git('tag').split()
        assert tags, 'no tags'
        for t in tags:
            self.git('rev-parse', '--verify', '-q', f'{t}^{{commit}}')
        rows = self.git('log', '--format=%H%x09%(trailers:key=In-force,valueonly,separator=)', 'main').splitlines()
        assert not rows[0].split('\t')[1].strip(), 'documentation commit should carry no In-force'
        missing = [r[:10] for r in rows[1:] if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', r.split('\t')[1].strip())]
        assert not missing, f'{len(missing)} commits without a valid In-force, e.g. {missing[:3]}'
        days = [r.split('\t')[1].strip() for r in rows[1:]]
        assert days == sorted(days, reverse=True), 'In-force days are not in order along main'
        return f'{len(tags)} tags resolve; {len(rows) - 1} law commits carry In-force, in date order'

    # 5
    def authors(self):
        rows = self.git('log', '--format=%H%x09%an%x09%ae%x09%cn', 'main').splitlines()
        by_lex = [r for r in rows if r.split('\t')[1] == 'Lexifina']
        assert len(by_lex) == 1 and by_lex[0] == rows[0], f'{len(by_lex)} commits by Lexifina'
        assert all(r.split('\t')[3] == 'Lexifina' for r in rows), 'a committer other than Lexifina'
        names = sorted({r.split('\t')[1] for r in rows[1:]})
        bad = [n for n in names if bad_author(n)]
        assert not bad, f'author names that are not texts: {bad[:5]}'
        emails = [r.split('\t')[2] for r in rows[1:] if not r.split('\t')[2].endswith('.invalid')]
        assert not emails, f'author emails not ending .invalid: {emails[:3]}'
        return f'only the documentation commit {rows[0][:10]} is by Lexifina; {len(names)} distinct authors, none a file name'

    # 6
    def readme(self):
        text = self.git('show', 'main:README.md')
        table = text[text.index('## The questions'):text.index('## The dates')]
        cmds = [c for c in re.findall(r'`([^`]+)`', table) if c.startswith(('git ', 'python '))]
        assert len(cmds) >= 8, f'only {len(cmds)} commands found'
        for c in cmds:
            args = shlex.split(c)
            if args[0] == 'python':
                args[0:2] = [sys.executable, '-X', 'utf8', str(self.tool_path)]
            out = subprocess.run(args, cwd=self.repo, capture_output=True, text=True, encoding='utf-8')
            assert out.returncode == 0, f'{c}: exit {out.returncode} {out.stderr.strip()[:200]}'
            assert out.stdout.strip(), f'{c}: printed nothing'
        return f'{len(cmds)} README commands ran and printed output'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default=None)
    ap.add_argument('--record', action='store_true')
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    s = Smoke(Path(args.repo).resolve() if args.repo else default_repo())
    s.check('blame names a text', s.blame)
    s.check('text before and after an amendment', s.on_date)
    s.check('log --follow in date order', s.follow)
    s.check('tags resolve, In-force on every law commit', s.tags_and_trailers)
    s.check('only the documentation commit is by Lexifina; authors are texts', s.authors)
    s.check('README commands run', s.readme)
    ok = all(r[1] for r in s.results)
    summary = f'{sum(r[1] for r in s.results)} of {len(s.results)} passed'
    print(summary)
    if args.record:
        p = HERE / 'verification.json'
        rec = json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}
        rec['smoke'] = {'summary': summary, 'passed': sum(r[1] for r in s.results), 'total': len(s.results),
                        'results': [{'test': n, 'ok': o, 'detail': d} for n, o, d in s.results]}
        p.write_text(json.dumps(rec, indent=1, sort_keys=True, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    raise SystemExit(0 if ok else 1)


if __name__ == '__main__':
    main()

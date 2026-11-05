"""Prevent metadata correction labels from bypassing the smoke gate."""
import unittest
from pathlib import Path

from test_repo import Smoke


class MetadataSmoke(unittest.TestCase):
    def smoke(self, extra='', changed=None):
        target, parent, sha = '1' * 40, '2' * 40, '3' * 40
        block = '\n'.join(['Kind: correction', 'Correction-scope: metadata only',
                           'Corrected: 2026-11-05', 'Reason: Unknown signing date',
                           'Supersedes: Signing metadata', 'In-force-basis: Source dates unchanged',
                           f'Corrects: {target}', f'Redates: {target} enacted no-date',
                           'Files: data/dates.json']) + '\n' + extra
        row = '\x1f'.join([sha, 'Lexifina', 'france-law@lexifina.com', 'Lexifina',
                           'france-law@lexifina.com', block]) + '\x1e'
        s = Smoke(Path('.'))
        def git(*args):
            if args[0] == 'log':
                return row
            if args[0] == 'rev-list':
                return f'{sha} {parent}\n'
            if args[0] == 'merge-base':
                return ''
            if args[0] == 'diff-tree':
                return '\n'.join(changed or ['data/dates.json']) + '\n'
            raise AssertionError(f'unexpected command: {args}')
        s.git = git
        return s, sha

    def test_valid_metadata_only_correction(self):
        s, sha = self.smoke()
        self.assertEqual(s.metadata_corrections(), {sha})

    def test_label_does_not_exempt_law_changes(self):
        s, _ = self.smoke(changed=['constitution/constitution-1958/1.md'])
        with self.assertRaisesRegex(AssertionError, 'changes law'):
            s.metadata_corrections()

    def test_fictitious_in_force_is_rejected(self):
        s, _ = self.smoke(extra='In-force: 2026-11-05\n')
        with self.assertRaisesRegex(AssertionError, 'must not assert In-force'):
            s.metadata_corrections()

    def test_invalid_or_incomplete_correction_is_rejected(self):
        for extra in ('Corrected: 2026-02-30\n', 'Kind: documentation\n',
                      'Redates: ' + '4' * 40 + ' enacted 2026-02-30\n',
                      'Files: tools/undeclared.py\n'):
            with self.subTest(extra=extra):
                s, _ = self.smoke(extra=extra)
                with self.assertRaises(AssertionError):
                    s.metadata_corrections()


if __name__ == '__main__':
    unittest.main()

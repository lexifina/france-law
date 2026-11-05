"""Regression tests for LEGI's unknown signing-date sentinel and title dates."""
import unittest

import build


class SigningDates(unittest.TestCase):
    def test_calendar_dates_and_unknown_values(self):
        for value in ('', '2999-01-01', '3000-01-01', '2024-02-30', '0000-01-01', '2024-1-1'):
            with self.subTest(value=value):
                self.assertEqual(build.signing_date(value), '')
        self.assertEqual(build.signing_date('2024-02-29'), '2024-02-29')

    def test_date_of_leading_act_not_referenced_act(self):
        title = ('Décret n° 2024-1218 du 28 décembre 2024 abrogeant le décret '
                 'n° 2024-1163 du 4 décembre 2024')
        self.assertEqual(build.signing_date(build.FAR, title), '2024-12-28')
        self.assertEqual(build.signing_date('', 'ARRÊTÉ DU 1ER MAI 2024'), '2024-05-01')
        self.assertEqual(build.signing_date('', 'Loi du 31 février 2024'), '')
        self.assertEqual(build.signing_date('', 'Loi du 1er mai 2999'), '')
        self.assertEqual(build.signing_date('', 'Avis relatif au décret du 4 décembre 2024'), '')
        self.assertEqual(build.signing_date('', "Avenant n° 1 à l'accord du 20 octobre 2023"), '')

    def test_known_structured_date_has_priority(self):
        self.assertEqual(build.signing_date('2024-01-01', 'Décret du 2 janvier 2024'), '2024-01-01')

    def test_own_full_title_fallback_and_conflicting_records(self):
        m = ('JORFTEXT1', 'DECRET', '2024-1218', build.FAR)
        text = {'id': 'LEGITEXT1', 'cid': m[0], 'date_texte': build.FAR,
                'titre': 'Décret n°2024-1218', 'titrefull': 'Décret n° 2024-1218 du 28 décembre 2024'}
        plan = {'texts': {'LEGITEXT1': text}, 'names': {}}
        self.assertEqual(build.maker_signing_date(m, plan), '2024-12-28')
        conflict = {**text, 'id': 'LEGITEXT2', 'date_texte': '2024-12-27'}
        plan = {'texts': {'LEGITEXT1': text, 'LEGITEXT2': conflict}, 'names': {}}
        self.assertEqual(build.maker_signing_date(m, plan), '')

    def test_link_title_fallback_without_own_record(self):
        m = ('JORFTEXT1', 'LOI', '', '')
        plan = {'texts': {}, 'names': {m[0]: 'Loi du 1er février 2024'}}
        self.assertEqual(build.maker_signing_date(m, plan), '2024-02-01')


if __name__ == '__main__':
    unittest.main()

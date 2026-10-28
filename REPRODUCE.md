# How this repository was made (France)

This file is written by the build on 2026-10-28, the day the source data was retrieved. Everything below is enough to rebuild this repository hash for hash.

## Sources

| Source | Address | Retrieved | Requests | Licence |
| --- | --- | --- | ---: | --- |
| DILA, base LEGI (Légifrance open data) | <https://echanges.dila.gouv.fr/OPENDATA/LEGI/> | 2026-10-28 | 483 | Licence Ouverte / Open Licence 2.0 (Etalab), https://www.etalab.gouv.fr/licence-ouverte-open-licence |

Every response is cached by the sha256 of its URL, and the table above lists every source with its retrieval date. Lexifina keeps its fetch scripts privately; `tools/parse.py` reads only the cache and writes `corpus.json`, so the same cache always gives the same corpus.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution du 4 octobre 1958 | 24 | 1958-10-05 to 2024-03-10 |
| `code-civil` | Code civil | 222 | 1994-01-01 to 2029-01-01 |
| `code-penal` | Code pénal | 329 | 1994-03-01 to 2029-01-01 |

The build made 584 commits:

| Commits | Kind |
| ---: | --- |
| 3 | first version of an act |
| 550 | one law on its in-force day |
| 31 | changes no amendment note explains, credited to the publisher |

Other counts:
- 3 commits on the branch `futur`: laws not yet in force on 2026-10-28.
- 4 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 490 laws in the record.
- 1060 tags.

## Dates

Each commit is dated at noon (Europe/Paris) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Code civil, art. 1er, alinéa 1er: "Les lois et, lorsqu'ils sont publiés au Journal officiel de la République française, les actes administratifs entrent en vigueur à la date qu'ils fixent ou, à défaut, le lendemain de leur publication. Toutefois, l'entrée en vigueur de celles de leurs dispositions dont l'exécution nécessite des mesures d'application est reportée à la date d'entrée en vigueur de ces mesures." LEGI already applies this rule, or the text's own entry-into-force clause, in each article version's DATE_DEBUT, which is used as the in-force day. https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006419280

## Commands, in order

```sh
# fill the cache from the sources listed above (network; Lexifina's fetch scripts are kept privately)
python -X utf8 tools/parse.py                  # cache -> corpus.json (no network)
python -X utf8 tools/build.py <folder> --repo <empty folder> --docs-date 2026-10-28
python -X utf8 tools/check_repo.py <repo> --corpus <folder>/corpus.json --write
python -X utf8 tools/build.py <folder> --repo <another empty folder> --docs-date 2026-10-28 --compare <repo>
```

In the main Lexifina repository these files live as follows:
- `fetch.py`, `parse.py` and `repo/`: in `scripts/france-law/`.
- `build.py`, `check_repo.py` (`check.py` there) and `on.py`: in `scripts/gitlaw_common/`, with the corpus format in `SCHEMA.md`.

## Exact inputs

- `corpus.json` sha256 `7f11195a02b852ef08bbbfe763adf5e9c5c219079719401d5482035ccb84905b` (7584309 bytes)
- Script blob hashes (`git hash-object`):

| Script | Blob |
| --- | --- |
| build.py | `2bfc4ac9df193a7be844556d7f69cdb9d93ec3f2` |
| check.py | `cd346c7ff9996d450240e3bab52bcae03b2bc865` |
| on.py | `644a6c0857fbcc72562032b58d57aa113fee0641` |
| fetch.py | `b686c30b29fe370cf0b0a79950eaff74e6e28e3d` |
| parse.py | `509d827dba3c4c4f02b3856680b67ef676da73ce` |

- Tools:
  - Python 3.14.0
  - git version 2.52.0.windows.1
  - curl 8.21.0 (Windows) libcurl/8.21.0 Schannel zlib/1.3.2 WinIDN WinLDAP

## Checks

575 versions of 3 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 581 history commits and 1060 tags (history tip `37b03c4e28f81648462c68841ee2d28a917bd0db`).

These results are from the check run on the build before this one, from the same corpus.

## Decisions made by hand

- Source: the LEGI database of DILA (Légifrance), one XML file per article version with its in-force dates (DATE_DEBUT, DATE_FIN), its state (ETAT) and links to the texts that created, modified, abrogated or transferred it. Each version of an act here is the set of LEGI article versions in force on its day; its sha256 is that of the sorted manifest "<article version id> TAB <sha256 of the file>" of those files, and its source_url is Légifrance's reader for the act on that day.
- In-force dates: each change takes effect on the LEGI DATE_DEBUT of the new article version (or the DATE_FIN of the last one, for a removal). LEGI sets these from the amending text's own entry-into-force clause or, failing one, from Code civil art. 1er (the day after publication in the Journal officiel).
- Article versions whose DATE_DEBUT is on or after their DATE_FIN were never in force (ETAT MODIFIE_MORT_NE and the like) and are skipped.
- Credits come only from LEGI's own amendment links. A new wording is credited to the texts its article version links to as creating, modifying, transferring or moving it (CREATION/CREE, MODIFICATION/MODIFIE, TRANSFERT/TRANSFERE, DEPLACEMENT/DEPLACE, either direction of the link), signed on or before the day it took effect, leaving out every link the article's previous version already carried when it took effect (LEGI repeats an article's older links on its later versions); of those, only the latest signing date counts.
- A removal is credited to the removed version's own abrogation or transfer links (ABROGATION/ABROGE, TRANSFERT/TRANSFERE, DEPLACEMENT/DEPLACE) signed on or before the day it ended, leaving out inherited links and transfer links from the provision that created that version (they record the move in, not out); latest signing date only. An explicit abrogation link from the creating provision counts: loi n° 2016-1087 art. 4 inserted Code civil arts. 1386-19 to 1386-25 from 2016-08-10 and abrogated them from 2016-10-01.
- Anything those rules leave unexplained is committed as unexplained, by the publisher; no credit is guessed. Example of why inherited links are left out: Code civil art. 515-11 took a new wording on 2020-01-01; its links name loi n° 2019-1480 (signed 2019-12-28, already on the version of 2019-12-30) and ordonnance n° 2019-964 art. 35; only the ordonnance is credited, as LEGI's own note on that version says.
- An article version whose ETAT is abrogated, that follows the previous version without a gap and repeats its words, that no new link created, and whose abrogation link was signed on or before its own first day, is the record LEGI keeps after an abrogation, still holding the old words (for example Code civil art. 9 from 1927-08-14 to 1970-07-19, abrogated by the loi du 10 août 1927): the article is absent from that day, the removal credited to that abrogation link.
- Where an article's version ends as modified (not abrogated or transferred) and its next version starts later, LEGI does not give the text in force in between: the article reads "[La source ne donne pas le texte en vigueur à cette date.]" for that period, unexplained, rather than keeping the old words or dropping the article.
- Two versions of one article overlapping in time: the later one wins from its first day. Two versions of one article starting the same day: the one with the later LEGI id is kept.
- Text: <p>, <div> and <br/> end a line; other markup is dropped; non-breaking spaces become spaces, soft hyphens are dropped, curly quotes become straight quotes, every dash and minus sign becomes "-", and runs of spaces collapse. NOTA (editorial notes) are not part of the text.
- Unit keys: art-<number> with the first number padded to the act's widest (at least 3 digits) and each further number to 3 (Code civil art. 515-11 is art-0515-011); a letter prefix (R, D, L) is the key prefix instead of "art" (Code pénal art. R610-1 is r-610-001); the preamble is preambule.
- Laws: each amending text is keyed by its nature and number (loi-2016-1547, ordonnance-2016-131, loi-constitutionnelle-2008-724, decision-2012-240-qpc), labelled from its own LEGI record (nature, number, signing date) and titled with its TITREFULL from the same dumps (extract.py --titles). Kinds: lois, lois organiques, lois constitutionnelles and ordonnances are laws; décrets, décrets-lois and arrêtés are decrees; Conseil constitutionnel decisions are court; the Constitution itself, loi n° 62-1292 (1962) and loi constitutionnelle n° 2000-964 (2000) were adopted by referendum. A text whose LEGI nature is LOI but whose own title (or link text) reads "loi constitutionnelle" is labelled a loi constitutionnelle (loi n° 2003-276, n° 2024-200).
- The Constitution starts on 1958-10-05, the day it was published and took effect, as enacted: every LEGI version in force that day carries no amendment link, so the first commit is the Constitution itself.
- constitution: 148 changed provisions after the first version, 146 credited to a text, 2 unexplained (committed by the publisher).
- The Code civil starts on 1994-01-01, not 1804. LEGI holds the Code civil from 1804-03-21, but its older history is incomplete: for every year before 1994, articles that provably existed then (an amendment link on a later version is dated before that year) have no LEGI version covering it (19 at 1993-01-01, 20 at 1985-01-01, 51 at 1975-01-01, 336 at 1900-01-01; for example art. 59 and art. 459, whose first LEGI versions are of 1993 and 1988). From 1994-01-01 every such case is a law signed earlier that took effect later, or a gap in one article that is marked below. The text in force on 1994-01-01 is committed as the oldest version available, credited to no law.
- code-civil: 3656 changed provisions after the first version, 3597 credited to a text, 59 unexplained (committed by the publisher).
- code-civil: 2 abrogated-state versions (absent from their first day): 9 1927-08-14, 10 1927-08-14.
- code-civil: 29 gaps with no text (placeholder): 16-11 2005-07-01..2007-07-01, 9-1 1993-09-02..1994-07-30, 21-15 1999-12-29..1999-12-30, 22-1 1999-12-29..1999-12-30, 27 1999-12-29..1999-12-30, 27-1 1999-12-29..1999-12-30, 27-2 1999-12-29..1999-12-30, 28-1 1999-12-29..1999-12-30, 30-1 1999-12-29..1999-12-30, 31 1995-02-09..1995-05-09, 31-2 1995-02-09..1995-05-09, 31-3 1995-02-09..1995-05-09, 334-2 1995-02-09..1995-05-09, 348-3 1995-02-09..1995-05-09, 369 1949-04-21..1966-11-01, 374 1995-02-09..1995-05-09, 470 1995-02-09..1995-05-09, 473 1995-02-09..1995-05-09, 491-3 1995-02-09..1995-05-09, 500 1995-02-09..1995-05-09, 512 1995-02-09..1995-05-09, 1427 1986-01-07..1986-07-01, 1471 1986-01-07..1986-07-01, 1832 1985-07-12..1985-07-13, 2134 1998-04-07..1998-07-01, 2148 1998-04-07..1998-07-01, 2152 1998-04-07..1998-07-01, 2201 1998-04-07..1998-07-01, 2508 2012-01-01..2012-10-01.
- code-civil: 22 overlapping versions (the later one wins): 210 1804-03-21..1994-03-01 / 1994-02-01, 211 1804-03-21..1994-03-01 / 1994-02-01, 220-1 1966-02-01..1994-03-01 / 1994-02-01, 247 1987-07-24..1994-03-01 / 1994-02-01, 252-2 1976-01-01..1994-03-01 / 1994-02-01, 264-1 1986-07-01..1994-03-01 / 1994-02-01, 334-2 1972-08-01..1994-03-01 / 1994-02-01, 334-3 1972-08-01..1994-03-01 / 1994-02-01, 334-5 1972-08-01..1994-03-01 / 1994-02-01, 334-5 1994-02-01..2005-01-01 / 2003-09-01, 371-4 1971-01-01..1994-03-01 / 1994-02-01, 373-4 1987-07-24..1994-03-01 / 1994-02-01, 375-3 1989-07-14..1994-03-01 / 1994-02-01, 376-1 1987-07-24..1994-03-01 / 1994-02-01, 377 1974-07-07..1994-03-01 / 1994-02-01, 377-1 1974-07-07..1994-03-01 / 1994-02-01, 377-2 1971-01-01..1994-03-01 / 1994-02-01, 539 1804-02-04..2004-08-17 / 1804-03-21, 650 1804-02-10..2006-07-01 / 1804-03-21, 2101 1989-07-14..1990-01-04 / 1990-01-02, 2104 1989-07-14..1990-01-04 / 1990-01-02, 2270-1 1986-01-01..1998-06-18 / 1998-06-16.
- The Code pénal starts on 1994-03-01, the day the new Code pénal took effect (loi n° 92-1336 du 16 décembre 1992, art. 373). LEGI also dates 30 article versions from 1992-07-23: the wording of the laws of 22 July 1992 that loi n° 92-1336 amended before the code as a whole took effect (for example art. 131-6, amended by its art. 341). They are left out. The text in force on 1994-03-01 is committed as the oldest version available, naming the five laws that made it.
- code-penal: 2926 changed provisions after the first version, 2906 credited to a text, 20 unexplained (committed by the publisher).
- code-penal: 6 gaps with no text (placeholder): 121-2 2004-03-10..2005-12-31, 131-8 2005-01-01..2005-10-01, 131-22 2004-03-10..2005-12-13, 132-70-1 1998-05-12..2014-10-01, 434-29 1997-12-20..1997-12-31, 716-1 2001-07-13..2002-01-01.
- code-penal: 4 overlapping versions (the later one wins): 711-1 2019-10-04..2019-12-30 / 2019-12-28, 711-1 2022-02-02..2022-09-01 / 2022-05-01, 713-2 1996-05-01..2001-07-07 / 1999-03-21, R131-35 1994-03-01..2004-09-29 / 2004-09-27.
- code-penal: 1 two versions start the same day (latest file id kept): 713-2 1996-05-01.

## What AI did and did not do

The fetch, parse and check scripts were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above, through code that anyone can rerun.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none: no model wrote, chose or checked any legal text or credit. parse.py was written with Claude Code (Claude Opus 5.5, claude-opus-5-5); it runs no model.

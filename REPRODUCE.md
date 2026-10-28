# How this history was made, and how to make it again

This file records how the repository was built: the sources, the commands, the software, the decisions, and what an
AI model did and did not do. The build writes it, so it describes the build that made this commit.

## Short version

```sh
git clone --bare https://github.com/lexifina/france-law && cd france-law.git
mkdir ../legi && cd ../legi
# download the archives listed in data/archives.json from https://echanges.dila.gouv.fr/OPENDATA/LEGI/
# (the full dump into legi/, the daily updates into legi/daily/), and check their sha256
git -C ../france-law.git show main:tools/scan.py > scan.py      # likewise scan_daily.py, build.py, check_repo.py
python -X utf8 scan.py legi/Freemium_legi_global_20250713-140000.tar.gz --db legi.sqlite
python -X utf8 scan_daily.py scan legi/daily --out daily-db
python -X utf8 scan_daily.py merge daily-db --db legi.sqlite
python -X utf8 build.py --db legi.sqlite --repo ../rebuilt --docs-date 2026-10-28 --archives legi
git -C ../rebuilt rev-parse main~1       # the same hash as this repository's last law commit
```

`build.py` and the scanners need Python 3.12 or later (standard library only) and git. `build.py` needs
`repo/` (README.md, REPRODUCE.md, LICENSE, corpus.json and tools/en_vigueur.py) beside it, as in Lexifina's
`scripts/france-law/`. With the same archives and the same `--docs-date` it gives the same commits with the same hashes.

## Sources

All legal text and all information about versions, dates and amending texts come from **LEGI**, the database of
consolidated French law that the Direction de l'information légale et administrative (DILA) publishes as open data at
https://echanges.dila.gouv.fr/OPENDATA/LEGI/, the same data as Légifrance. Nothing was typed in, summarised or rewritten.
The build read 479 archives: the full dump `Freemium_legi_global_20250713-140000.tar.gz` and the daily updates after it, up to `LEGI_20261027-211214.tar.gz`.
Each is listed with its size and sha256 in `data/archives.json`. They were downloaded one at a time, with curl, from
DILA's open-data server. The licence is the Licence Ouverte 2.0 (see LICENSE); the server has no robots.txt rules for it.

| What LEGI gives | Where it goes |
| --- | --- |
| Each article version (ARTICLE): its number, text, NOTA, start and end days (DATE_DEBUT, DATE_FIN), its text, the list of all versions of the article, and links to the texts that acted on it | one file per article; the commit that writes a version; its author |
| Each text's structure and version (TEXTELR, TEXTE_VERSION): nature, number, dates, NOR, title | the text's folder name and `index.md`; the authors' names for first versions |

## The build, step by step

1. `scan.py` streamed the full dump (never unpacked) into SQLite, parsing members on every core; `scan_daily.py`
   read each daily update into its own SQLite file in parallel and merged them oldest first, so a later file replaces
   an earlier one and each update's `liste_suppression_legi.dat` removes what it lists.
2. `build.py --docs-date 2026-10-28` wrote this repository with git fast-import: 187,161 law commits from
   1,556,213 article versions in 153,011 texts, 25 tags, then this documentation commit. `tools/build.py`
   here is the same file (git blob `3d6e239b07d9a0f9c88874f9dfa38ef988047418`).
3. `check_repo.py`: not run for this build.
4. `test_repo.py` (functional smoke test): not run for this build.
5. Rebuild: not run for this build.

It ran with Python 3.12.10 and git version 2.46.0.windows.1 on Windows 11.

## How the text and the commits are derived

Everything below is done by `tools/build.py`, deterministically.

- **Text.** An article version's CONTENU becomes plain text: paragraphs (`<p>`, `<br/>`, block elements) become
  paragraphs separated by a blank line, runs of spaces become one space, and table cells are separated by ` | `. The
  file is `# Article <number>`, the text, and `NOTA :` with LEGI's note when there is one.
- **Commits.** Each article version is written on its DATE_DEBUT. Versions are grouped by day and by the text that
  made them; each group is one commit. A version whose DATE_FIN comes with no successor at the same place is removed
  that day: in the successor's text's commit when the successor starts that day; otherwise in the commit of the text
  LEGI names as having ended it (ABROGE, ANNULE, PERIME or DISJOINT with sens="cible", or ABROGATION, ANNULATION,
  PEREMPTION or DISJONCTION with sens="source", signed latest on or before the end day); otherwise in a labelled
  `Fin de vigueur` commit. Removals sort after writes within a day, so a version replaced that day is never removed.
  Versions starting after `--docs-date`, and versions LEGI marks as never in force (DATE_FIN on or before
  DATE_DEBUT), are left out.
- **Author.** The LEGI link on the new version, of a kind that makes a version (CREE, MODIFIE, TRANSFERE, DEPLACE,
  CODIFIE or RATIFIE with sens="cible", or CREATION, MODIFICATION, TRANSFERT, DEPLACEMENT, CODIFICATION, RATIFICATION
  or RECTIFICATION with sens="source"; legi.py's TYPELIEN_MAP pairs the two spellings), to the text signed latest on or
  before the version's first day. Its name is built from the link's nature, number and date of signature (`Décret n° 2016-1511 du 8 novembre
  2016`); when those are missing, the most frequent title LEGI's links give it. An
  article's first version with no such link, in a text that is not a code, is credited to its own text. Otherwise the
  author is `Légifrance (DILA), version consolidée`.
- **Dates.** Noon in Paris, UTC+1 or UTC+2 in summer time (from 1976; the last Sunday of March to the last Sunday of
  September until 1995, of October since). Before 1970: 1970-01-01 UTC, a second apart.
- **Tags.** `constitution/<day>` on the last commit of each day the Constitution of 1958 changed, and
  `legi/2026-10-28` on the last law commit.

## Decisions made by hand

- The direction of LEGI's links was checked against legi.py (`tar2sqlite.py`, TYPELIEN_MAP and the reversal of
  sens="cible") and against examples in the data: the four versions of article 2 bis of LEGITEXT000006062318 credit
  décrets 2001-784, 2008-680, 2016-1511 and 2020-561, each signed a few days before the version took effect.
- First versions without a link are credited to their own text, except in codes, whose first versions come from many
  texts.
- Section headings are not reproduced; files are flat in each text's folder.

## What an AI model did

The builder, scanners, tools and this documentation were written by Claude (Anthropic) working as a coding agent for
Lexifina. No model reads, writes or changes legal text: the build is a deterministic program
over DILA's data, and no model runs during it.

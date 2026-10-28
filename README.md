# French law, change by change

Every consolidated text in LEGI, the database behind Légifrance, as one git repository: the Constitution of 1958, the
codes, and the laws, ordinances, decrees and orders that LEGI consolidates, one file per article. Each commit is a text
taking effect: it writes the article versions that text made, is credited to that text, and is dated the day the
versions took effect, at noon in Paris. The text is LEGI's, published by the DILA under the Licence Ouverte 2.0.

187,161 law commits, from 0881-10-09 to the data of 2026-10-28; 1,556,213 article versions in 153,011 texts,
made or ended by 156,293 texts. On the last day, 692,985 article files are in force, in 77 codes and 118,773 other
texts.

*En français : [plus bas](#en-français).*

The repository holds 692,985 article files, so a bare clone (`git clone --bare`) is quicker to get; every git
command below works in one. In a bare clone, take the tool out first: `git show main:tools/en_vigueur.py >
en_vigueur.py`, and run it from inside the clone as `python ../en_vigueur.py …`.

## The questions, as git commands

| Question | Command |
| --- | --- |
| What did article 1 of the Constitution say on 1 January 2000? | `python tools/en_vigueur.py 2000-01-01 constitution-1958 1` |
| Article 1382 of the Code civil on 1 June 2010 | `python tools/en_vigueur.py 2010-06-01 code-civil 1382` |
| Which text wrote each paragraph of article 1 of the Constitution? | `git blame main -- constitution/constitution-1958/1.md` |
| Every change to article 1, with the text and the day | `git log --follow --format="%(trailers:key=In-force,valueonly,separator=) %an" main -- constitution/constitution-1958/1.md` |
| Every day the Constitution changed | `git tag -l "constitution/*"` |
| The last ten changes to the Code civil | `git log -10 --format="%(trailers:key=In-force,valueonly,separator=) %an" main -- codes/code-civil` |
| Everything one text changed: the loi constitutionnelle of 23 July 2008 | `git log --author="2008-724" --format="%(trailers:key=In-force,valueonly,separator=) %s" main` |
| Versions LEGI gives no amending text for | `git log -5 --author="Légifrance" --format="%(trailers:key=In-force,valueonly,separator=) %b" main` |
| Articles that ended with no successor | `git log -5 --author="Fin de vigueur" --format="%(trailers:key=In-force,valueonly,separator=) %b" main` |
| What a text is, with its numbers and its Légifrance link | `git show main:codes/code-civil/index.md` |

## The dates, and which one we use

A French text has the day it was signed (`Signed:`), the day it was published in the Journal officiel, and, for each
article version it makes, the day that version took effect. **Commits are dated the day the article versions took
effect** (LEGI's DATE_DEBUT), at noon in Paris (CET, or CEST in summer time): that is the day that decides which text
applies. The trailer `In-force:` carries that day in every law commit. Git cannot store dates before 1970, so earlier
commits are dated 1970-01-01 UTC, a second apart in order, and their real day is only in `In-force:` and the tags;
`tools/en_vigueur.py` reads the trailer.

## What "author" means

The author of a commit is the text that made the change, named from LEGI's fields as its nature, number and date of
signature, for example `Loi constitutionnelle n° 2008-724 du 23 juillet 2008`, with an address made of its Journal
officiel identifier and ending `@legifrance.invalid` (it cannot exist), so `git blame` names the text. The committer is always `Lexifina`.

LEGI links each article version to the texts that created, modified, moved, codified or corrected it. The build credits
the linked text with the latest signature on or before the day the version took effect. An article's first version
with no such link, in a text that is not a code, is credited to its own text (a law's articles are made by that law).
Two labelled authors are not texts:

- `Légifrance (DILA), version consolidée`: LEGI names no text that made these versions. Many are codes' first
  versions, or old consolidations.
- `Fin de vigueur`: article versions that end on that day (repealed, expired or annulled) with no successor and no
  text LEGI names as having repealed, annulled or ended them. When LEGI names one (an ABROGE or ABROGATION link), the
  removal is credited to that text instead.

Neither is ever credited to a law.

## Files

- `constitution/constitution-1958/` is the Constitution of 4 October 1958; other constitutional texts in LEGI are
  beside it.
- `codes/<code>/`, for example `codes/code-civil/`, holds each code in force or repealed.
- `textes/<nature>/<year>/<nature>-<number>/` holds every other consolidated text, for example
  `textes/loi/1978/loi-78-17/` (the data-protection law of 6 January 1978).

Each article is one file named after its number: `L. 1234-1` is `L1234-1.md`. An article with no number is named after
its LEGI identifier. If two articles of one text carry the same number at the same time (an annex's article 1 beside
the decree's), the later one's file name ends with part of its LEGI identifier. A file is `# Article <number>`, then
the article's paragraphs, then LEGI's `NOTA` when there is one. When an article stops being in force it is removed.
Each text folder has an `index.md` with its title, nature, number, dates, identifiers and Légifrance link. Section
headings (livres, titres, chapitres) are not reproduced.

## How it is checked

`tools/check_repo.py` takes a series of days and compares, file for file and byte for byte, the tree in force that day
with the article versions LEGI has in force that day. `tools/test_repo.py` checks that the commands above work. The
results are in [`REPRODUCE.md`](REPRODUCE.md).

## What it does not show

- Texts LEGI does not consolidate, and versions older than LEGI's: LEGI records each text from the version it was
  first consolidated in. Its history of the oldest codes is fullest from the 1990s.
- Section headings and the order of the parts of a code.
- Which part of a text an amending text changed, beyond the article: the amending text is credited with the whole new
  version of the article.

The consolidated text is for information. The authentic text is the one published in the Journal officiel.

## How it is built

`tools/scan.py` and `tools/scan_daily.py` read DILA's LEGI archives (the full dump and the daily updates, listed with
their sha256 in [`data/archives.json`](data/archives.json)) into SQLite; `tools/build.py` writes this repository from
scratch from that database. Every step, the software, the decisions and what an AI model did are in
[`REPRODUCE.md`](REPRODUCE.md). [`corpus.json`](corpus.json) describes the corpus for tools that read many of these
repositories.

## En français

Tout le droit consolidé de la base LEGI (Légifrance) sous forme de dépôt git : un fichier par article, un commit par
texte modificateur et par jour d'entrée en vigueur, daté de ce jour à midi (heure de Paris) et dont l'auteur est le
texte modificateur. `python tools/en_vigueur.py AAAA-MM-JJ code-civil 1382` affiche un article à une date donnée ;
`git blame` indique le texte qui a écrit chaque paragraphe. Données : DILA, base LEGI, Licence Ouverte 2.0 (voir
[`LICENSE`](LICENSE)).

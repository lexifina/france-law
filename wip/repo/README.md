# France: law history in git

The law of France as a git history: one file per article, one commit per text on the day it took effect, and the text that made each change (loi, loi constitutionnelle, ordonnance, décret, décision du Conseil constitutionnel) as the commit's author. `git blame` names the text behind every paragraph; `git log` lists every change to an article; reading a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `fr/`.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution du 4 octobre 1958 | 24 | As enacted (in force 5 October 1958) to today: all 25 constitutional revisions, 1960 to 2024 |
| `code-civil/` | Code civil | 222, of which 3 on `futur` | From 1 January 1994 to today (see "What it does not show" for why not 1804); changes already published for 31 December 2026, 6 January 2027 and 1 January 2029 are on the branch `futur` |
| `code-penal/` | Code pénal | 329, of which 1 on `futur` | From 1 March 1994, the day the new Code pénal took effect, to today, legislative (L) and regulatory (R, D) parts; ordonnance n° 2025-1091, in force 1 January 2029, is on `futur` |

Every version is the set of article versions that DILA's LEGI database (the data behind Légifrance) marks as in force on that day. The per-act `README.md` in each folder lists every article, how often it changed and when.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did art. 1382 of the Code civil say on 30 September 2016? | `python tools/en_vigueur_au.py 2016-09-30 code-civil 1382` |
| The same, with raw git (bash) | `git show $(git rev-list -1 --before="2016-09-30T23:59:59Z" main -- code-civil/art-1382.md):code-civil/art-1382.md` |
| The same, in PowerShell | `$r = git rev-list -1 --before="2016-09-30T23:59:59Z" main -- code-civil/art-1382.md; git show "$($r):code-civil/art-1382.md"` |
| Which text wrote each paragraph of art. 89 of the Constitution? | `git blame constitution/art-089.md` |
| Every change to art. 222-33 of the Code pénal, word by word | `git log -p --word-diff code-penal/art-222-033.md` |
| Every text in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |
| Everything one text changed | `git show law/ordonnance-2016-131` (tags `law/<key>` mark each text's commit) |
| The whole Constitution on a date | `python tools/en_vigueur_au.py 2000-01-01 constitution` |
| An act as in force on one of its version days | `git show constitution/2008-07-25` (tags `<act>/<in-force day>`) |
| Texts published but not yet in force | `git log main..futur` |

File names: `art-` plus the article number, the first number padded to the act's width and each further number to three digits (art. 515-11 of the Code civil is `code-civil/art-0515-011.md`, art. 222-33 of the Code pénal `code-penal/art-222-033.md`); regulatory articles start with their letter (`code-penal/r-610-001.md` is art. R610-1); the Preamble is `constitution/preambule.md`. The tool accepts the number as Légifrance writes it.

After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, Europe/Paris, on the day the change took effect** (the in-force date). The signing and Journal officiel publication dates are trailers (`Enacted:`, `Published:`); the in-force day is in `In-force:`, which the tools read.
- **The in-force day is LEGI's.** Every LEGI article version has a start day (DATE_DEBUT). DILA sets it from the amending text's own entry-into-force clause or, failing one, from the default rule of Code civil art. 1er: laws "entrent en vigueur à la date qu'ils fixent ou, à défaut, le lendemain de leur publication". Those days are used as given.
- **Staged entry into force** shows as separate commits by the same text on different days: loi constitutionnelle n° 2008-724 has commits on 25 July 2008, 1 March 2009 and 1 December 2009.
- `--before="YYYY-MM-DD"` alone uses your clock's time of day, so a change that took effect that day may be missed before noon. Use `T23:59:59Z` as above, or the tool.
- Git cannot store dates before 1970. The commits of 1958, 1960, 1962 and 1963 (Constitution) are dated 1 January 1970, a second apart, in order; their real day is in `In-force:`.

## How it is checked

- Every version of every act is read back from git on the day it took effect and on the day before (`tools/check_repo.py`); both must match `corpus.json`. Results are in `REPRODUCE.md`.
- Health checks: no merge commits on `main`, commit dates never go backwards, nothing dated in the future, and every commit's trailers parse with git.
- **Against the official text today:** `tools/verify.py` compares each act as in force on 28 October 2026, article by article, with the LEGI article versions in force that day, with every version LEGI marks VIGUEUR (the current text Légifrance shows), and with the act's own table of contents in LEGI (an independent list of current article versions). All three acts match exactly: 109 provisions of the Constitution, 2,899 articles of the Code civil, 1,301 of the Code pénal.
- **The crediting rule is tested** (`tools/test_parse.py`) on 17 changes to the Constitution, whose 25 revisions were checked by hand against the list published in the Journal officiel, and on Code civil cases where LEGI's links mislead.
- The repository is rebuilt from the same data a second time and must give identical hashes.

## What "author" means

The author of a commit is the text that made the change, with an e-mail address that cannot exist (`ordonnance-2016-131@dila.invalid`), so `git blame` and `git log --author` name texts. The committer is always Lexifina.

- **Credits come only from LEGI.** Each article version carries links to the texts that created, modified, transferred or abrogated it. A new wording is credited to the texts linked as creating, modifying or transferring it, signed on or before the day it took effect, **leaving out every link the article's previous version already carried**, since LEGI repeats an article's older links on its later versions; of what is left, only the latest signing date counts. A removed article is credited to its own abrogation or transfer link.
- **Unexplained changes** are committed by the publisher, DILA, and labelled "unexplained": 2 in the Constitution (art. 28 on 31 December 1963 and art. 7 on 19 June 1976: LEGI's versions name no text, though the changes are the lois constitutionnelles n° 63-1327 and n° 76-527), 59 in the Code civil and 20 in the Code pénal. Most of these are gaps (below); the rest are versions whose links name no new text. None is guessed.
- **Gaps.** Where LEGI ends an article's version as modified but starts the next one later (29 cases in the Code civil, 6 in the Code pénal, from 1 day to 16 years), it does not give the text in between. The article then reads "[La source ne donne pas le texte en vigueur à cette date.]" for that period rather than keeping old words or vanishing.
- Décisions of the Conseil constitutionnel that abrogate articles (QPC) are commits of kind "court"; the Constitution itself, loi n° 62-1292 and loi constitutionnelle n° 2000-964 were adopted by referendum.
- Blame credits whole lines (one paragraph per line). In an article written by several texts, use `git log -p --word-diff` to see exactly which words each changed.

## What it does not show

- **The Code civil before 1994.** LEGI has Code civil versions back to 21 March 1804, but its older history is incomplete. For every start date before 1994, articles that provably existed then (an amendment link on a later version is dated earlier) have no LEGI version covering it: 19 on 1 January 1993, 20 in 1985, 51 in 1975 and 336 in 1900. For example, art. 59 and art. 459 have no LEGI version before 1993 and 1988. A history from 1804 would show a code with hundreds of articles missing, so this one starts on 1 January 1994, the first year with no such gap. That first commit is "oldest version available", credited to no text.
- **The old Code pénal of 1810.** The Code pénal here is the new code in force since 1 March 1994. Thirty article versions dated 1992 (the 1992 laws' wording, amended before the code took effect) are left out.
- **Editorial notes (NOTA)** on Légifrance, such as deferred-application notes, are not part of the text. Read them on Légifrance.
- **Transitional provisions in the amending texts** (which cases a change applies to) are not encoded.
- Words unchanged does not mean law unchanged: a decision of the Conseil constitutionnel that only interprets (réserve d'interprétation) leaves no trace here.

## How it is built

`scripts/france-law/` in the Lexifina repository: `fetch.py` downloads the full LEGI dump and every daily update; `extract.py` replays them in order into a cache; `parse.py` writes `corpus.json` and `corpus.d/*.json`; the shared builder turns them into this repository. Every command, tool version, script hash and data hash is in `REPRODUCE.md`; the scripts are in `tools/`. No AI model wrote, chose or checked any legal text or credit; the scripts were written with Claude Code (Claude Opus 5.5).

## Sources

- **DILA, base LEGI** (Légifrance open data), https://echanges.dila.gouv.fr/OPENDATA/LEGI/: the full dump `Freemium_legi_global_20250713-140000.tar.gz` and all 479 daily updates after it, the last `LEGI_20261028-212713.tar.gz`, retrieved on 28 October 2026. All 480 archives passed `gzip -t`; their sha256 are in the cache log.
- Also from the register: [Légifrance](https://www.legifrance.gouv.fr) (article-level versions with in-force ranges; the PISTE API needs registration), [the LEGI dataset on data.gouv.fr](https://www.data.gouv.fr/datasets/legi-codes-lois-et-reglements-consolides), [Archéo Lex](https://github.com/Legilibre/Archeo-Lex) (rebuilds git histories of French codes from LEGI, dormant since 2019) and [La Fabrique de la Loi](https://www.lafabriquedelaloi.fr) (how bills changed in Parliament). Volunteer projects were used for reconciliation only; no text was copied from any.

## Licence

Source : DILA, Légifrance, base LEGI, reused under the Licence Ouverte / Open Licence 2.0 (Etalab). Lexifina's own contributions are CC0. See `LICENSE`.

## En français

Ce dépôt retrace le droit français dans git : un fichier par article, un commit par texte au jour de son entrée en vigueur, et pour auteur le texte qui a fait la modification (loi, loi constitutionnelle, ordonnance, décret, décision du Conseil constitutionnel). Il contient la Constitution du 4 octobre 1958 depuis son entrée en vigueur, le Code civil depuis le 1er janvier 1994 et le Code pénal depuis le 1er mars 1994, d'après la base LEGI de la DILA (téléchargée le 28 octobre 2026).

- **Dates :** chaque commit est daté du jour d'entrée en vigueur (DATE_DEBUT de LEGI), à midi, heure de Paris. Les modifications publiées mais pas encore en vigueur sont sur la branche `futur`.
- **Auteurs :** uniquement les textes que nomment les liens de LEGI sur la version de l'article, sans les liens hérités de la version précédente. Une modification qu'aucun lien n'explique est attribuée à l'éditeur (DILA) et signalée « unexplained ».
- **Lacunes :** quand LEGI ne donne pas le texte d'un article pour une période, l'article indique « [La source ne donne pas le texte en vigueur à cette date.] ». L'historique du Code civil commence en 1994 parce que LEGI n'a pas toutes les versions antérieures.
- **Vérification :** au 28 octobre 2026, le texte de chaque code correspond, article par article, aux versions en vigueur de LEGI.
- Exemple : `python tools/en_vigueur_au.py 2016-09-30 code-civil 1382`.

Source : DILA, Légifrance, base LEGI, sous Licence Ouverte 2.0 (Etalab).

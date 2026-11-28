<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Watching the sources: what is watched for France

[Français](WATCHING.md)

How global-law watches every country's sources: [global-law WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md). This page is the same for France only: every official source this repository takes text from, what is read on it, how often and when it was last read. Every read and what came of it: [monitoring/](monitoring/README.en.md).

| Source | What is read | Folders | How often | Last read | State |
| --- | --- | --- | --- | --- | --- |
| [LEGI, DILA's open data of consolidated law (the data behind Légifrance)](https://echanges.dila.gouv.fr/OPENDATA/LEGI/) | the list of LEGI archives and each new daily increment (every article, structure and version file DILA added or changed that day, and the files it withdrew), applied to a full copy of LEGI kept from DILA's full dump; every article file held here compared with it each day | `constitution/`, `codes/`, `textes/` | daily | 2026-11-28 16:00 UTC | watched |
| [This repository's other sources (Journal officiel, KALI, ACCO, CNIL, circulaires, Parliament, local authorities)](https://echanges.dila.gouv.fr/OPENDATA/) | — | `journal-officiel/`, `conventions-collectives/`, `accords-entreprise/`, `parlement/`, `circulaires/`, `autorites/`, `collectivites/`, `doctrine/`, `historique/` | — | — | not watched yet: outside corpus.json's scope (LEGI); their updates are not read by the check trail yet |

Sources are read within their robots.txt and terms, with pauses between requests.

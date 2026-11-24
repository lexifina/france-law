<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Monitoring: what is read and what came of it

[Français](README.md)

How global-law monitors every country: [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). This page is the same for France only: every time an official source is read, when, and what came of it (acts added, changed and removed). The machine-readable form is [data/checks/](../data/checks/) (JSON Lines, schema `lexifina-check/1`), in `git log` as `Kind: check` commits, and month by month in [checks/](checks/).

**Last check:** 2026-11-24 05:07 UTC, LEGI, DILA's open data of consolidated law (the data behind Légifrance): 5 addresses read; 51 added, 175 changed, 7 removed; changes found; 133 not published, 0 of them with no reason.

## Sources

| Source | Folders | How often | Last successful check | Last result | State |
| --- | --- | --- | --- | --- | --- |
| [LEGI, DILA's open data of consolidated law (the data behind Légifrance)](https://echanges.dila.gouv.fr/OPENDATA/LEGI/) | `constitution/`, `codes/`, `textes/` | daily | 2026-11-24 05:07 UTC | changes found | watched |
| [This repository's other sources (Journal officiel, KALI, ACCO, CNIL, circulaires, Parliament, local authorities)](https://echanges.dila.gouv.fr/OPENDATA/) | `journal-officiel/`, `conventions-collectives/`, `accords-entreprise/`, `parlement/`, `circulaires/`, `autorites/`, `collectivites/`, `doctrine/`, `historique/` | — | — | — | not watched yet: outside corpus.json's scope (LEGI); their updates are not read by the check trail yet |

## The last 30 days

| Started (UTC) | Source | Read | Added | Changed | Removed | Not published (no reason) | Result | Commits |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| [2026-11-24 05:01](checks/2026-11.md#fr-legi-20261124t050102z) | legi | 5 | 51 | 175 | 7 | 133 (0) | changes found | [65](https://github.com/lexifina/france-law/compare/ebfeabbc39db...d64fce15d982) |
| [2026-11-23 15:00](checks/2026-11.md#fr-legi-20261123t150001z) | legi | 8 | 82 | 584 | 12 | 131 (0) | changes found | [124](https://github.com/lexifina/france-law/compare/d5d80b17e4c3...031498b1aeb0) |

## Check it yourself

```
python tools/checktrail.py                      # the latest check of every source
python tools/checktrail.py --day 2026-11-23     # every check of a day
python tools/checktrail.py --act <id>           # when an act was seen and published
git log --grep='^Kind: check' --format='%ci %s'  # the checks in the history
```

Only the official publication has legal force; the texts here are copies for reading and searching.

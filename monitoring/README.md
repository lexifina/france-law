<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Surveillance : ce qui est lu et ce qui en résulte

[English](README.en.md)

Comment global-law surveille chaque pays : [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). Cette page fait de même pour France seulement : chaque lecture d’une source officielle, sa date et ce qui en est ressorti (actes ajoutés, modifiés et retirés). La forme lisible par machine est dans [data/checks/](../data/checks/) (JSON Lines, schéma `lexifina-check/1`), dans `git log` sous forme de commits `Kind: check`, et mois par mois dans [checks/](checks/).

**Dernière vérification :** 2026-11-26 15:26 UTC, LEGI, données ouvertes de la DILA sur le droit consolidé (les données de Légifrance) : 1 adresses lues ; 0 ajoutés, 0 modifiés, 0 retirés ; la vérification a échoué ; 188 non publiés, dont 0 sans motif.

## Sources

| Source | Dossiers | Fréquence | Dernière vérification réussie | Dernier résultat | État |
| --- | --- | --- | --- | --- | --- |
| [LEGI, données ouvertes de la DILA sur le droit consolidé (les données de Légifrance)](https://echanges.dila.gouv.fr/OPENDATA/LEGI/) | `constitution/`, `codes/`, `textes/` | chaque jour | 2026-11-25 05:08 UTC | la vérification a échoué | surveillée |
| [Les autres sources de ce dépôt (Journal officiel, KALI, ACCO, CNIL, circulaires, Parlement, collectivités)](https://echanges.dila.gouv.fr/OPENDATA/) | `journal-officiel/`, `conventions-collectives/`, `accords-entreprise/`, `parlement/`, `circulaires/`, `autorites/`, `collectivites/`, `doctrine/`, `historique/` | — | — | — | pas encore surveillée: hors du périmètre de corpus.json (LEGI) ; leurs mises à jour ne sont pas encore lues par le journal des vérifications |

## Les 30 derniers jours

| Début (UTC) | Source | Lues | Ajoutés | Modifiés | Retirés | Non publiés (sans motif) | Résultat | Commits |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| [2026-11-26 15:06](checks/2026-11.md#fr-legi-20261126t150646z) | legi | 1 | 0 | 0 | 0 | 188 (0) | la vérification a échoué | — |
| [2026-11-26 14:00](checks/2026-11.md#fr-legi-20261126t140034z) | legi | 1 | 0 | 0 | 0 | 188 (0) | la vérification a échoué | — |
| [2026-11-26 13:00](checks/2026-11.md#fr-legi-20261126t130036z) | legi | 1 | 0 | 0 | 0 | 188 (0) | la vérification a échoué | — |
| [2026-11-26 12:00](checks/2026-11.md#fr-legi-20261126t120036z) | legi | 1 | 0 | 0 | 0 | 188 (0) | la vérification a échoué | — |
| [2026-11-26 11:00](checks/2026-11.md#fr-legi-20261126t110035z) | legi | 1 | 0 | 0 | 0 | 188 (0) | la vérification a échoué | — |
| [2026-11-26 10:00](checks/2026-11.md#fr-legi-20261126t100035z) | legi | 1 | 0 | 0 | 0 | 188 (0) | la vérification a échoué | — |
| [2026-11-26 09:16](checks/2026-11.md#fr-legi-20261126t091643z) | legi | 1 | 0 | 0 | 0 | 188 (0) | la vérification a échoué | — |
| [2026-11-26 05:00](checks/2026-11.md#fr-legi-20261126t050035z) | legi | 2 | 24 | 255 | 2 | 188 (0) | la vérification a échoué | — |
| [2026-11-25 05:00](checks/2026-11.md#fr-legi-20261125t050033z) | legi | 5 | 19 | 299 | 5 | 133 (0) | changements constatés | [27](https://github.com/lexifina/france-law/compare/569bbdfc939b...dcac01217cf9) |
| [2026-11-24 05:01](checks/2026-11.md#fr-legi-20261124t050102z) | legi | 5 | 51 | 175 | 7 | 133 (0) | changements constatés | [65](https://github.com/lexifina/france-law/compare/ebfeabbc39db...d64fce15d982) |
| [2026-11-23 15:00](checks/2026-11.md#fr-legi-20261123t150001z) | legi | 8 | 82 | 584 | 12 | 131 (0) | changements constatés | [124](https://github.com/lexifina/france-law/compare/d5d80b17e4c3...031498b1aeb0) |

## Vérifiez vous-même

```
python tools/checktrail.py                      # la dernière vérification de chaque source
python tools/checktrail.py --day 2026-11-23     # toutes les vérifications d’un jour
python tools/checktrail.py --act <id>           # quand un acte a été vu et publié
git log --grep='^Kind: check' --format='%ci %s'  # les vérifications dans l’historique
```

Seule la publication officielle fait foi ; les textes de ce dépôt sont des copies destinées à la lecture et à la recherche.

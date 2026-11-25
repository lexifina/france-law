<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Surveillance des sources : ce qui est surveillé pour France

[English](WATCHING.en.md)

Comment global-law surveille les sources de chaque pays : [global-law WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md). Cette page fait de même pour France seulement : chaque source officielle dont ce dépôt tire des textes, ce qui y est lu, à quelle fréquence et quand elle a été lue pour la dernière fois. Chaque lecture et son résultat : [monitoring/](monitoring/README.md).

| Source | Ce qui est lu | Dossiers | Fréquence | Dernière lecture | État |
| --- | --- | --- | --- | --- | --- |
| [LEGI, données ouvertes de la DILA sur le droit consolidé (les données de Légifrance)](https://echanges.dila.gouv.fr/OPENDATA/LEGI/) | la liste des archives LEGI et chaque nouvel incrément quotidien (tous les fichiers d’article, de structure et de version que la DILA a ajoutés ou modifiés ce jour-là, et ceux qu’elle a retirés), appliqués à une copie complète de LEGI tenue depuis l’export intégral de la DILA ; chaque fichier d’article de ce dépôt comparé chaque jour | `constitution/`, `codes/`, `textes/` | chaque jour | 2026-11-25 05:00 UTC | surveillée |
| [Les autres sources de ce dépôt (Journal officiel, KALI, ACCO, CNIL, circulaires, Parlement, collectivités)](https://echanges.dila.gouv.fr/OPENDATA/) | — | `journal-officiel/`, `conventions-collectives/`, `accords-entreprise/`, `parlement/`, `circulaires/`, `autorites/`, `collectivites/`, `doctrine/`, `historique/` | — | — | pas encore surveillée: hors du périmètre de corpus.json (LEGI) ; leurs mises à jour ne sont pas encore lues par le journal des vérifications |

Les sources sont lues dans le respect de leur robots.txt et de leurs conditions, avec des pauses entre les requêtes.

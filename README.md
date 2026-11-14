# France : l’histoire du droit dans git

**Français** · **[Or read it in English](README.en.md)**

<picture>
<source media="(prefers-color-scheme: dark)" srcset="data/fr/effort-dark.svg">
<img alt="Le droit français dans ce dépôt : ce qu’il contient, les modifications par année d’entrée en vigueur, l’exhaustivité au regard des sources officielles et l’exactitude de son contenu" src="data/fr/effort-light.svg" width="880">
</picture>

Le droit français sous forme d’historique git : un fichier par article, un commit pour les modifications de chaque texte au jour de leur entrée en vigueur, et pour auteur de chaque commit le texte qui a fait la modification. `git blame` nomme le texte à l’origine de chaque alinéa ; `git log` énumère chaque modification d’un article ; le choix d’une date donne le texte en vigueur ce jour-là.

Fait partie de [lexifina/global-law](https://github.com/lexifina/global-law), un historique git unique pour le droit de chaque pays : ce dépôt contient le droit national français, que global-law lit dans `france/national/acts/`.

**Ce qu’il contient aujourd’hui :** tous les textes que consolide LEGI, la base de données sur laquelle repose Légifrance, tels qu’au 2026-10-28. En vigueur ce jour-là : la Constitution de 1958 (avec les articles des Constitutions de 1946 et de 1848 que LEGI garde en vigueur), 77 codes et 118 773 autres textes (69 738 arrêtés, 44 755 décrets, 2 815 lois, 1 320 ordonnances et 145 autres), soit 692 977 articles ; dans l’historique, 1 556 213 versions d’articles de 153 011 textes, en 187 161 commits. Le dossier de chaque texte contient un `index.md` avec son titre, ses numéros, ses dates et son lien Légifrance.

La Constitution se trouve dans `constitution/constitution-1958/`, chaque code dans `codes/<code>/` (`codes/code-du-travail/` est le Code du travail) et tout autre texte dans `textes/<nature>/<année>/<nature>-<numéro>/` (`textes/loi/1978/loi-78-17/` est la loi Informatique et Libertés du 6 janvier 1978). Chaque article est un fichier nommé d’après son numéro : l’article L. 3141-1 est `L3141-1.md`. Avec environ 810 000 fichiers, un clone nu (`git clone --bare`) s’obtient plus vite, et les commandes git ci-dessous y fonctionnent.

Le texte est en français, tel que LEGI le publie. Une traduction anglaise ne fait pas partie de ce registre.

## Les questions, en commandes git

| Question | Commande |
| --- | --- |
| Toutes les modifications de l’article L. 3141-1 du Code du travail (congés payés) | `git log -p --word-diff -- codes/code-du-travail/L3141-1.md` |
| Quel texte a écrit chaque ligne de l’article L. 3141-1 ? | `git blame codes/code-du-travail/L3141-1.md` |
| Toutes les modifications du Code du travail, avec le jour de leur entrée en vigueur et le texte qui les a faites | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- codes/code-du-travail` |
| L’article L. 3141-1 tel qu’en vigueur le 1er janvier 2010 | `python tools/en_vigueur.py 2010-01-01 code-du-travail L3141-1` |

**En dehors de git**, nous mettons aussi ce registre à disposition du public, gratuitement :

- **[Interrogez Claude sur le droit français](https://global-law.lexifina.com/v1/try_claude?country=france)** : ouvre Claude avec une première question prête.
- **[Interrogez ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=france)** : la même question dans ChatGPT.
- **[Appelez l’API dans votre navigateur](https://global-law.lexifina.com/v1/search_law?query=cong%C3%A9s+pay%C3%A9s&jurisdictions=france)** : une recherche de « congés payés » dans le droit français, renvoyée en JSON. La documentation est [ici](https://lexifina.com/api/global-law).

Les deux assistants lisent le registre par le connecteur gratuit Global law (MCP, `https://global-law.lexifina.com/mcp`) ; la première fois, la conversation vous donne le lien qui l’ajoute. Posez vos questions en français ou en anglais.

**Hébergez-le vous-même, simplement.** Il suffit de git et de Python, et les outils tournent sur votre machine :

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add france/national/acts
python3 tools/law.py show 2026-01-01 france/national/acts/codes/code-du-travail/L3141-1.md
```

Ouvert dans Claude Code, Cursor, VS Code ou Codex, le clone démarre aussi un serveur MCP local doté des mêmes outils ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Chaque commit de droit est daté à midi, heure de Paris (Europe/Paris), du jour d’entrée en vigueur de ses versions d’articles, et porte ce jour dans son trailer `In-force:` ; le jour de signature du texte figure dans `Signed:`.

- Le jour est celui que LEGI donne pour début de chaque version d’article (DATE_DEBUT) ; les versions que LEGI marque comme jamais entrées en vigueur sont écartées.
- Une version d’article qui prend fin sans successeur est supprimée à son dernier jour, dans le commit du texte que LEGI désigne comme y ayant mis fin, ou à défaut dans un commit `Fin de vigueur`.
- Git ne peut pas enregistrer de dates antérieures à 1970 : les 6 097 commits antérieurs sont donc datés à partir du 1970-01-01 UTC, à une seconde d’intervalle, le jour réel figurant dans `In-force:`. Interrogez une date avec `tools/en_vigueur.py`, et non avec `git log --before`.
- Lorsque le jour donné par LEGI est erroné (une année mal saisie, un jour antérieur à la signature du texte), des commits ultérieurs nomment la version et le bon jour ; les commits publiés ne sont pas réécrits.

Chaque modification est attribuée au texte qui l’a faite, tel que le nomment les liens de LEGI (`Loi n° 2016-1088 du 8 août 2016`) : le texte lié signé en dernier à la date d’entrée en vigueur de la version ou avant. Lorsque LEGI n’en nomme aucun, elle est attribuée à `Légifrance (DILA), version consolidée` (5 410 commits) ; [`data/credits.csv`](data/credits.csv) nomme le bon texte pour les versions que LEGI classe sous un autre.

## Comment il est vérifié

- `tools/check_repo.py` prend une série de jours et compare, fichier par fichier et octet par octet, l’arborescence en vigueur chaque jour avec les versions d’articles que LEGI donne en vigueur ce jour-là.
- `tools/test_repo.py` vérifie que blame, l’outil de dates et `git log --follow` fonctionnent, que chaque commit de droit porte `In-force:` et que chaque commit de droit est attribué à un texte, jamais à Lexifina.
- [`REPRODUCE.md`](REPRODUCE.md) décrit chaque étape de la construction, avec le sha256 des archives dans [`data/archives.json`](data/archives.json) ; selon ce fichier, les mêmes archives donnent les mêmes commits avec les mêmes hashes, et pour la construction du 2026-10-28 ni ces vérifications ni une reconstruction n’ont été lancées.

## Ce qu’il ne montre pas

- **Les textes que LEGI ne consolide pas, et les versions antérieures à celles de LEGI.** LEGI enregistre chaque texte à partir de la version dans laquelle il l’a consolidé pour la première fois ; son historique des codes les plus anciens est le plus complet à partir des années 1990.
- **Les intitulés de divisions** (livres, titres, chapitres) et l’ordre des parties d’un code.
- **Les mots qu’un texte modificateur a changés** au sein d’un article : il est crédité de toute la nouvelle version.
- **Les modifications postérieures au 2026-10-28** : les mises à jour quotidiennes de LEGI ont été lues jusqu’à ce jour.
- **La jurisprudence.** Elle se trouve dans six dépôts distincts, que global-law lit à côté de celui-ci ([france/](https://github.com/lexifina/global-law/tree/main/france)).

## Sources

| Source | Nature | Versions antérieures | Remarques |
| --- | --- | --- | --- |
| [LEGI](https://echanges.dila.gouv.fr/OPENDATA/LEGI/) (DILA), les données de [Légifrance](https://www.legifrance.gouv.fr) | Droit national consolidé : la Constitution, les codes, lois, ordonnances, décrets et arrêtés | oui, chaque version d’article que LEGI enregistre | L’export complet et ses mises à jour quotidiennes ; le texte authentique est celui publié au Journal officiel |

## Licence

Voir [`LICENSE`](LICENSE). Le texte juridique et son historique sont ceux de LEGI, réutilisés sous la Licence Ouverte 2.0 (Etalab), qui demande de mentionner la source (la DILA) et la date de sa dernière mise à jour ; les outils et la documentation sont sous licence MIT.

Aucun modèle d’IA n’a écrit ni modifié de texte juridique ; le programme de construction, les outils et la documentation ont été écrits par un modèle d’IA (voir [`REPRODUCE.md`](REPRODUCE.md)).

Ceci est une traduction de la version anglaise ([README.en.md](README.en.md)) ; en cas de divergence, la version anglaise fait foi.

## En savoir plus

Dans le dépôt [lexifina/global-law](https://github.com/lexifina/global-law) (pages en anglais) :

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): toutes les fonctionnalités et ce que chaque corpus doit prendre en charge (`git blame`, `law.py`, outils MCP)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions et réponses · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposer une modification · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): serveur MCP · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): comment il a été construit · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): à quel point chaque corpus est à jour · [Surveillance](https://github.com/lexifina/global-law/tree/main/monitoring): si les mises à jour fonctionnent · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): comment chaque source officielle est surveillée pour repérer les modifications
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): la rapidité des outils, mesurée
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): graphiques et liens à travers le droit du monde entier
- [Vulnérabilités](https://github.com/lexifina/global-law/tree/main/vulnerabilities): erreurs dans les textes tels qu’ils ont été publiés

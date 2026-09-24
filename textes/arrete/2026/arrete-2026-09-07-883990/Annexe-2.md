# Article Annexe 2

ANNEXE 2

RÉFÉRENTIEL D'INTEROPÉRABILITÉ DES SERVICES NUMÉRIQUES POUR L'ÉDUCATION

Table des matières

1. Préambule

1.1. Contexte

1.2. Objectifs du document

1.3. Cycle de vie du document et gouvernance

2. Principes d'interopérabilité

2.1. Définition

2.2. Niveaux d'interopérabilité

2.3. Nomenclatures et vocabulaires

2.4. Principes et outils pour les échanges de données

3. Périmètre et principes du référentiel d'interopérabilité des services numériques pour l'éducation

3.1. Périmètre de l'interopérabilité

3.2. Typologie des données d'éducation

3.3. Bénéfice de l'interopérabilité pour les usagers

3.4. Critères de sélection des standards

4. Cartographie des données et besoins de standardisation

5. Principes d'urbanisation communs

5.1. Nomenclatures des objets d'éducation

5.2. Echanges de données par API

5.3. Echanges de fichiers pour les systèmes de stockage

5.4. Normes et standards

6. Présentation des exigences et standards retenus par domaine fonctionnel

6.1. Identification et authentification des utilisateurs dans un contexte interopérable

6.2. Organisation pédagogique pour la vie scolaire

6.3. Portails de services numériques et ressources pour l'enseignement et les pratiques pédagogiques

6.4. Examens, certifications et concours

6.5. Pilotage des missions éducatives

7. Synthèse des standards retenus

8. Cas d'usage

8.1. Accéder à une ressource pédagogique

8.2. Faciliter l'intégration des ressources dans un LMS pour une utilisation sans couture dans un parcours pédagogique

8.3. Assurer la portabilité des contenus d'un parcours pédagogique lors d'un changement de LMS

Table des figures

Figure 1 : Définitions et niveaux d'interopérabilité

Figure 2 : Conception de l'organisation des données

Figure 3 : Grille de description standard des données

Figure 4 : Quatre volets d'amélioration

Figure 5 : Grille de positionnement des besoins de standardisation des données

Figure 6 : Positionnement des nomenclatures

Figure 7 : Synthèse des standards retenus

1. Préambule

1.1. Contexte

Le présent document constitue le référentiel d'interopérabilité des services numériques pour l'éducation. Il s'inscrit dans le corpus des référentiels de la doctrine technique du numérique pour l'éducation.

Il recense les règles, exigences et recommandations d'interopérabilité pour l'ensemble des acteurs qui opèrent les services numériques pour l'éducation.

Ce document s'appuie sur des documents de référence français et européens : le référentiel général d'interopérabilité (4) et l'EIF (European Interoperability Framework) (5). Il s'inspire des meilleures pratiques en matière de standardisation, d'architecture technique et d'urbanisation de système d'information. Il ne souscrit à aucune méthode ni aucun outil propriétaire.

Ce document s'adresse spécifiquement aux acteurs qui réalisent, exploitent, intègrent les services numériques pour l'éducation pour le compte de porteurs de projet et responsables de traitement (collectivités territoriales, académies, ministère en charge de l'éducation, EPLE). Il vise à ce que chaque acteur puisse apporter des services à valeur ajoutée avec les mêmes règles, et à ce que chaque utilisateur bénéficie de ces services dans le cadre de confiance fixé par le ministère dans la doctrine technique du numérique pour l'éducation.

1.2. Objectifs du document

L'objectif du document est de définir des exigences en matière d'interopérabilité pour les services numériques pour l'éducation.

Il doit ainsi permettre de faciliter les choix pour les concepteurs et acheteurs de services numériques pour l'éducation, et de renforcer la cohérence de l'écosystème du numérique pour l'éducation aux échelles nationale et européenne.

Le document définit donc les standards et protocoles du périmètre défini dans la doctrine technique. Les différentes versions du document pourront également présenter des trajectoires et cibles à atteindre à un horizon temporel déterminé.

1.3. Cycle de vie du document et gouvernance

Le ministère, ses services déconcentrés et opérateurs, les collectivités territoriales et les fournisseurs de services numériques pour l'éducation ont participé à l'élaboration de ce référentiel. Les enseignants et personnels de direction des établissements scolaires ont également été parties prenantes des travaux pour identifier les besoins des usagers en matière d'amélioration de leurs parcours usagers dans l'écosystème des services et ressources numériques pour l'éducation à leur disposition.

Le présent document constitue la troisième version du référentiel d'interopérabilité des services numériques pour l'éducation.

Ce document a vocation à évoluer fréquemment pour s'adapter aux évolutions technologiques et juridiques à venir. Un réexamen annuel, avec l'ensemble des acteurs concernés incluant les représentants des personnels et des usagers, permet d'apprécier l'opportunité d'une actualisation du document. Ce dernier est ensuite soumis à l'avis du Conseil supérieur de l'éducation (CSE).

2. Principes d'interopérabilité

L'interopérabilité, au-delà du seul périmètre technique, impacte les systèmes informatiques, les processus, les procédures, les organisations tout au long de leur cycle de vie.

L'interopérabilité est assurée au travers de normes et formats respectés par tout élément ou système qui souhaite intégrer un domaine interopérable. Si l'interopérabilité dans les domaines de l'informatique et des télécommunications peut également être un outil de positionnement commercial, permettant à des consortiums de collaborer pour offrir des services plus complets qui s'enrichissent les uns avec les autres, c'est aussi un outil au service de l'humain pour lui permettre d'accéder à des parcours usagers plus fluides et proches des besoins.

2.1. Définition

L'interopérabilité s'entend comme la capacité de deux ou plusieurs systèmes à échanger des données et à utiliser les informations de chacun, sans nécessiter d'efforts importants de la part des utilisateurs ou des développeurs pour les intégrer et en faire usage.

Pour ce faire, ces systèmes doivent préalablement s'accorder sur la manière dont ils vont communiquer et utiliser les données et les informations qui peuvent être échangées. Cela consiste à s'entendre sur les protocoles d'échanges à utiliser et sur le format, la signification, la pertinence ou valeur ajoutée des données échangées.

La gestion des identités et des accès selon des règles partagées permet de fournir des parcours usagers sans réauthentification et respectueux des données personnelles, résolvant en cela un premier besoin d'interopérabilité entre les systèmes. Des notions et processus métiers partagés permettent quant à eux de poser les bases d'exigences d'interopérabilité pour les acteurs intervenant dans le même périmètre métier. L'adoption de normes ou de standards identiques au sein d'un écosystème favorise une autonomie technologique entre

ses différents systèmes. En respectant une interface standardisée, un système peut être remplacé par un autre de manière quasi transparente.

L'approche d'interopérabilité entre systèmes :

- permet une communication et une collaboration simplifiées et facilitées entre différentes applications, plateformes ou systèmes d'information ;

- stimule l'innovation et la créativité de nouvelles fonctionnalités pour les usagers, tout en facilitant l'évolutivité des systèmes conformes aux interfaces associées ;

- favorise la complémentarité et une mise en concurrence équitable des systèmes au sein de l'écosystème ;

- prévient la prolifération de connecteurs spécifiques et contribue à maîtriser les coûts pour l'ensemble des acteurs.

L'interopérabilité est ainsi primordiale afin de tirer parti des avantages offerts par diverses technologies pour créer des environnements informatiques plus flexibles, fluides et efficaces pour l'utilisateur final.

2.2. Niveaux d'interopérabilité

Comme cela a été identifié par l'EIF (European Interoperability Framework) (6) et rappelé dans le RGI (Référentiel Général d'Interopérabilité), plusieurs niveaux d'interopérabilité sont à prendre en considération dès que l'on souhaite faire communiquer deux systèmes entre eux.

Vous pouvez consulter l'intégralité du texte avec ses images à partir de l'extrait du Journal officiel électronique authentifié accessible en bas de page

Figure 1 : Définitions et niveaux d'interopérabilité

1. Le niveau politique apporte une stratégie convergente et des visions partagées entre les parties prenantes, favorisant ainsi la mise en œuvre des solutions d'échange.

2. Le niveau juridique garantit que les informations échangées seront bien en accord avec le cadre légal et réglementaire et les accords contractuels établis. Il doit ainsi notamment prendre en considération les recommandations de la CNIL et de l‘ANSSI.

3. Le niveau organisationnel définit les moyens et les procédures mis en œuvre pour permettre les échanges et l'interopérabilité entre les systèmes.

4. Le niveau sémantique permet une compréhension partagée des différents éléments de l'échange entre les tiers concernés. Elle pourra ainsi reposer sur un ensemble de nomenclatures partagées entre les acteurs.

5. Le niveau syntaxique précise le format des données échangées.

6. Le niveau technique définit enfin les caractéristiques techniques de l'échange comme les protocoles et moyens de transport.

2.3. Nomenclatures et vocabulaires

L'interopérabilité entre services ou systèmes d'information hétérogènes et dans les systèmes d'échange nécessite de poser et maintenir un contenu informationnel compréhensible par les différents partenaires.

Les spécifications sémantiques d'interopérabilité imposent de définir un langage commun permettant aux applications des systèmes d'information participants d'interpréter de façon homogène la nature et les valeurs des données transmises et de les réutiliser sans erreur ou perte d'information.

Dans le champ de l'éducation, différentes nomenclatures permettent de répondre à ce besoin.

Les nomenclatures de la BCN (Base Centrale des Nomenclatures) constituent le langage commun du système d'information du ministère chargé de l'éducation nationale. Elles sont mises à jour régulièrement et historisées au moyen de dates d'ouverture et de fermeture. Elles sont en consultation sur le site de la Base centrale des nomenclatures (7).

En dehors de son profil d'application, ScoLOMFR (8) fournit des vocabulaires communs aux acteurs sur les principaux aspects de l'activité et de l'enseignement scolaire. Il est à la disposition de l'ensemble de la communauté scolaire.

2.4. Principes et outils pour les échanges de données

Pour que les échanges de données entre acteurs s'opèrent dans de bonnes conditions afin d'assurer une interopérabilité effective, des principes doivent être partagés et respectés.

Un outillage pour la mise en œuvre de ces principes est alors possible, sur la base d'API, dont la gestion massive pour l'intégration des services peut être facilitée via l'utilisation d'un API manager.

2.4.1. Un ensemble cohérent, du dictionnaire de données aux protocoles recommandés

La proposition représentée ci-dessous s'inspire des travaux de Brandt Redd (9) qui sont exposés sur EdMatrix (10) sous licence Creative Commons 4.0. La conception des données requiert une organisation en quatre couches. Elles ne sont pas nécessairement présentes dans toutes les normes mais chacune d'entre elles doit être prise en compte pour s'intégrer dans un système fonctionnel.

Vous pouvez consulter l'intégralité du texte avec ses images à partir de l'extrait du Journal officiel électronique authentifié accessible en bas de page

Figure 2 : Conception de l'organisation des données

Dictionnaire de données : Il s'agit d'une liste de données, chacune ayant un titre, une définition et parfois un format. Par exemple, Titre : « Date de naissance » ; Définition :« Jour de naissance d'un individu »; Format : « année-mois-jour ».

Modèle logique de données : Un modèle logique de données définit la structure des données, en décrivant les relations entre les données, regroupées en ensembles cohérents (objets ou entités). Par exemple, une entité « Élève » peut inclure les propriétés « nom », « date de naissance », « sexe », « adresse », etc. Le type d'entité « Étudiant » aurait une relation de plusieurs à plusieurs avec l'entité « Classe ».

Format de données : Il s'agit du codage des informations représentatives d'un objet sous la forme d'une suite d'informations plus petites (« atomiques ») pour permettre la transmission d'informations structurées ou leur stockage. Les deux formats XML et JSON, par exemple, sont en concurrence pour les formats de codage textuel mais des formats personnalisés peuvent exister et s'appliquer à un même modèle de données.

Protocole : Il dicte les règles de communication entre deux systèmes afin d'assurer que les données échangées soient envoyées et reçues sans perte d'octets, sans erreur, sans duplication et dans l'ordre dans lequel elles ont été envoyées.

2.4.2. Mise en œuvre des échanges par API

Si un protocole est un ensemble de règles qui régissent la manière dont les données sont transmises sur un réseau, une API est une interface qui permet à deux applications différentes de communiquer entre elles. La mise en œuvre des échanges de données par API permet d'assurer la fluidité des échanges entre applications, services et ressources et d'intégrer efficacement des services numériques à partir d'une ou plusieurs plateformes dans un parcours de navigation optimisé pour l'élève, l'enseignant ou tout autre acteur de la communauté éducative. La collaboration et le partage des ressources s'en trouvera facilité.

Les API doivent être accompagnées d'une documentation complète et claire par le fournisseur ainsi que d'un support technique efficace afin de faciliter leur adoption et leur utilisation par les développeurs.

Elles sont conçues pour être flexibles et évolutives afin de répondre aux besoins actuels et être en capacité de s'adapter aux besoins futurs.

3. Périmètre et principes du référentiel d'interopérabilité des services numériques pour l'éducation

3.1. Périmètre de l'interopérabilité

Le référentiel d'interopérabilité des services numériques pour l'éducation traite des questions d'interopérabilité pour l'ensemble des services numériques pour l'éducation fournis par les acteurs publics ou privés.

3.2. Typologie des données d'éducation

Afin de pouvoir décrire des règles communes pour l'interopérabilité des services numériques, le schéma ci-dessous propose une grille de description standard des données, s'appuyant sur la typologie des données d'éducation, présentée au chapitre 5 de la doctrine technique.

Ces propositions et représentations s'inspirent des travaux de Brandt Redd qui sont exposés sur EdMatrix sous licence Creative Commons 4.0.

Vous pouvez consulter l'intégralité du texte avec ses images à partir de l'extrait du Journal officiel électronique authentifié accessible en bas de page

Figure 3 : Grille de description standard des données

Les données standard d'éducation peuvent être réparties en 2 grandes catégories et 8 types :

Données liées aux parties prenantes (« données des acteurs ») :

- données décrivant l'organisation scolaire ;

- données liées à l'identité ;

- données décrivant les interactions entre les acteurs (données évènementielles), dont font partie les « traces d'apprentissage » ;

- données descriptives des attestations de réussite.

Données liées aux contenus (« données des ressources ou services ») :

- métadonnées pour référencer et partager de façon certifiée les acquis des personnes ;

- métadonnées pour décrire, référencer et partager les définitions de compétences ;

- métadonnées de définition des contenus ;

- métadonnées pour le conditionnement et l'intégration des contenus.

3.3. Bénéfice de l'interopérabilité pour les usagers

Le référentiel vise à contribuer à la mise en place d'une offre de services finale cohérente, centrée sur les besoins de l'usager.

Les travaux menés avec les utilisateurs des services numériques pour l'éducation (11) dans le cadre des travaux 2023-2024 du programme Doctrine technique du numérique ont permis de dégager quatre volets d'amélioration liés à l'interopérabilité entre services.

Vous pouvez consulter l'intégralité du texte avec ses images à partir de l'extrait du Journal officiel électronique authentifié accessible en bas de page

Figure 4 : Quatre volets d'amélioration

3.3.1. Authentification unique

Une authentification unique des utilisateurs est nécessaire pour :

- assurer une simplicité d'accès aux services numériques et favoriser la fluidité du parcours usagers entre plusieurs services (principe du « dites-le-nous une fois ») ;

- contribuer à la sécurité du service et du parcours usager ;

- contribuer à la défendabilité du service.

Les solutions (standards et services socles du périmètre de l'éducation décrit dans le chapitre 4 de la doctrine technique) utilisées pour l'authentification et la propagation des données d'identité ont un impact sur les autres volets.

3.3.2. Portabilité des données des acteurs

La portabilité des données doit être définie dès l'initialisation du contrat, elle est nécessaire pour :

- assurer la continuité du parcours usager entre années et cycles scolaires ;

- assurer la continuité du parcours usager entre établissements ou académies ;

- assurer la continuité du parcours usager lors de changement de fournisseurs de services ;

- garantir l'authenticité, l'intégrité, la disponibilité de la donnée, et assurer la non répudiation ;

- garantir l'export de la donnée dans un format lisible.

3.3.3. Circulation des données entre services numériques

La circulation des données, de façon maîtrisée, entre services numériques pour l'éducation est nécessaire pour :

- assurer le service public du numérique éducatif pour les activités pédagogiques et les missions éducatives et les démarches administratives (principe du « dites-le-nous une fois ») ;

- créer de nouvelles fonctionnalités au bénéfice des usagers et de l'écosystème ;

- renforcer les possibilités créées par le numérique de personnalisation des parcours, de suivi des apprentissages et de remédiation par l'enrichissement des outils ;

- assurer le suivi de l'élève, quelle que soit l'activité qu'il a réalisée et quel que soit l'éditeur qui met à disposition le service numérique correspondant ;

- Garantir la conservation, maintenir l'intégrité, l'authenticité et la non répudiation des données produites par l'usager pour son propre usage.

3.3.4. Intégration de contenus éditoriaux

L'intégration de contenus éditoriaux entre services et ressources numériques est nécessaire pour :

- produire des parcours usagers fluides ;

- favoriser la complémentarité entre services.

3.4. Critères de sélection des standards

A l'instar des critères d'adoption retenus pour le RGI (12), les standards sélectionnés dans le présent document répondent aux critères suivants :

- ouvert ;

- pertinent ;

- mature ;

- indépendant ;

- facile à déployer ;

- soutenu par l'industrie.

Par ailleurs, à chaque standard est associé un statut pour faciliter la prise en compte par les fournisseurs de services, assurer une période de transition et de mise en conformité progressive. Le statut « émergent » permet également de prendre en compte les innovations technologiques.

Statut |

Explication du statut |

Cible |

Il s'agit d'un standard qui doit être respecté et appliqué par tous. |

En usage |

Il s'agit d'un standard actuellement en usage au sein des systèmes d'information d'éducation. |

Émergent |

Il s'agit d'un standard en émergence ou dont la maturité, la mise en œuvre et le soutien par la recherche et/ou l'industrie ne sont pas totalement acquis. |

En fin de vie |

Il s'agit d'un standard en fin de vie, dont le soutien se termine car d'autres standards de remplacement émergent. Son application est à prendre avec précaution ; il est donc considéré « en sursis ».

Si son retrait n'a pas encore été demandé dans tous les systèmes existants, il ne doit cependant pas être utilisé pour les nouveaux projets. |

4. Cartographie des données et besoins de standardisation

Pour que les échanges de données entre acteurs permettent d'assurer une interopérabilité effective, des principes doivent être partagés et respectés. Sur la base de la typologie des données présentée au chapitre 2 du présent document, la matrice ci-dessous fournit une grille de positionnement des besoins de standardisation des données.

Elle fait apparaître la nécessité de dictionnaires de données partagés, de règles de structuration des données et de leur échange selon des principes communs, afin de pouvoir les échanger de façon optimisée et dans l'intérêt final de l'usager.

Le chapitre 6 décrit les standards retenus dans la doctrine technique du numérique pour l'éducation, puis en fournit une synthèse selon cette même matrice.

Vous pouvez consulter l'intégralité du texte avec ses images à partir de l'extrait du Journal officiel électronique authentifié accessible en bas de page

Figure 5 : Grille de positionnement des besoins de standardisation des données

5. Principes d'urbanisation communs

Pour une approche urbanisée des échanges, nécessaire pour décloisonner le secteur des services numériques pour l'éducation, des vocabulaires communs sont nécessaires et des interactions via des API permettront d'assurer la fluidité des échanges de données et l'intégration entre services.

5.1. Nomenclatures des objets d'éducation

Des nomenclatures nationales permettent de proposer un vocabulaire de base, en français, permettant aux acteurs de partager la même compréhension du concept manipulé, indépendamment du système d'où il provient. Ces vocabulaires partagés sont essentiels pour améliorer l'interopérabilité sémantique des services interconnectés.

Vous pouvez consulter l'intégralité du texte avec ses images à partir de l'extrait du Journal officiel électronique authentifié accessible en bas de page

Figure 6 : Positionnement des nomenclatures

N°1 |

Exigence

Les services numériques pour l'éducation dans les 1er et 2d degrés décrivent les personnes et structures pédagogiques de manière identique sur la base des nomenclatures de la BCN (Base Centrale des Nomenclatures). |

5.2. Echanges de données par API

N°2 |

Exigences

Les services numériques pour l'éducation sont API-sés en exposant des APIs sécurisées pour d'autres services ou applications consommatrices. Ils permettent également de consommer des APIs fournies par des services ou applications tierces. Les services permettent également l'accès à d'autres services en utilisant des APIs. |

N°3 |

OMOGEN est le point d'entrée et de sortie unique pour les échanges de données publiques via les API avec les SI en académie, avec les partenaires externes et au national. |

5.3. Echanges de fichiers pour les systèmes de stockage

N°4 |

Exigence

Les systèmes de stockage de fichiers permettent le partage et l'échange de fichiers au format Objet en utilisant le protocole REST ou S3 |

5.4. Normes et standards

Le tableau ci-dessous présente les normes et standards utilisables ainsi que leur statut pour l'échange et la circulation des données.

Champs |

Organisme |

Standards |

Observation |

Statut |

Protocole |

IETF |

HTTPS |

HyperText Transfer Protocol Secure : combinaison du HTTP avec une couche de chiffrement TLS. |

Cible |

Protocole |

|

REST |

Representational state transfer.

Style d'architecture logicielle définissant un ensemble de contraintes à utiliser pour créer des services web |

Cible |

Format |

IETF |

JSON |

JavaScript Object Notation.

Format de données textuel dérivé de la notation des objets du langage JavaScript. |

Cible |

Format |

W3C |

XML |

Extensible Markup Language.

L'objectif initial de XML est de faciliter l'échange automatisé de contenus complexes entre systèmes d'informations hétérogènes |

En usage |

6. Présentation des exigences et standards retenus par domaine fonctionnel

Ce chapitre permet de présenter l'ensemble des exigences pour les services numériques pour l'éducation par domaine fonctionnel et type de données.

6.1. Identification et authentification des utilisateurs dans un contexte interopérable

L'authentification des utilisateurs est opérée par un service numérique « d'identification/authentification » qui fonctionne à partir de la réception et de la vérification d'un couple « identifiant / authentifiant ». Il permet également la gestion du cycle de vie des identités et des authentifiants.

L'identification permet de connaître l'identité d'un utilisateur, alors que l'authentification permet de vérifier l'identité.

Il existe plusieurs facteurs d'authentification : utiliser une information que seul le prétendant connaît (mot de passe), possède (carte à puce), est (données biométriques), peut produire (un geste).

Les protocoles d'authentification décrivent les interactions entre un prouveur et un vérifieur et les messages permettant de prouver l'identité d'un utilisateur. On distingue deux familles de protocoles d'authentification : l'authentification simple (un seul facteur d'authentification en jeu) et l'authentification forte (deux facteurs ou plus). Par ailleurs, on parle d'authentification unique lorsqu'un utilisateur n'a besoin de procéder qu'à une seule authentification pour accéder à plusieurs applications informatiques.

N°5 |

Exigence

Les services numériques pour l'éducation implémentent les fonctions de propagation d'identité SSO (single sign-on). Le système permet l'accès à un service externe puis de revenir sur le premier service, par échange de données d'identité. |

6.1.1. Fournisseurs d'identité du périmètre des services numériques pour l'éducation (services socles)

La doctrine technique du numérique pour l'éducation décrit, dans son chapitre 4, les services d'identification/authentification ÉduConnect pour les élèves et leurs représentants légaux, et le guichet Agents pour les agents de l'éducation nationale.

Ils permettent à ces utilisateurs de fédérer leur identité entre les différents portails de services raccordés.

6.1.2. Interface avec les services socles fournisseurs d'identité

N°6 |

Exigence

Les services numériques pour l'éducation utilisent les services socles pour l'authentification/identification des usagers du périmètre éducatif. |

6.1.2.1. Contrats d'interface ÉduConnect

Les contrats d'interface ÉduConnect sont disponibles sur demande, lors des travaux d'accrochage.

L'interconnexion des services numériques pour l'éducation avec le guichet ÉduConnect, sous réserve qu'ils soient sous la responsabilité de traitement du ministère de l'éducation nationale (ministère, académies, chefs d'établissement, IA-DASEN) et déclarés dans les registres de traitement des entités concernées s'effectue par la mise en place d'une fédération d'identité.

6.1.2.2. Contrats d'interface du guichet Agents

A venir |

6.1.3. Normes et standards

N°7 |

Exigence

Pour la fédération d'identités permettant l'authentification SSO, les services numériques pour l'éducation s'appuient sur des protocoles standards et éprouvés tels que décrits dans le tableau ci-dessous.

Les appels aux APIs utilisent une authentification basée sur des protocoles d'autorisation et d'authentification tels que OAuth2 ou OIDC. |

Le tableau ci-dessous présente les normes et standards utilisables ainsi que leur statut pour l'identification et l'authentification des utilisateurs.

Champs |

Organisme |

Standard |

Observation |

Statut |

Protocole |

OIDF |

Open ID Connect (OIDC) |

Couche d'identification basée sur OAuth 2.0, dispositif d'autorisation. |

Cible |

Protocole |

Internet engineering task force (IETF) |

OAuth2 |

Protocole d'autorisation. Inclus dans OIDC |

Cible |

Protocole |

Organization for the Advancement of Structured Information Standards (OASIS) |

SAML 2.0 |

Utilisé par le GAR.

Permet l'échange de données d'authentification et d'identification entre domaines de sécurité. |

En usage |

Protocole |

APEREO |

CAS |

Central Authentification Service (système d'authentification unique).

Support OIDC, OAuth2 et SAML |

Fin de vie |

6.2. Organisation pédagogique pour la vie scolaire

Les fonctions correspondant aux processus et activités métiers s'appuyant sur l'organisation pédagogique visent à matérialiser et mettre à jour l'organisation scolaire optimisée dans l'espace et le temps pour assurer les activités pédagogiques et missions éducatives, c'est-à-dire l'emploi du temps. Les données d'organisation scolaire sont nécessaires pour les fonctions de suivi de l'assiduité des élèves (absences, évaluations…) telles que définies au code de l'éducation, mais également pour les espaces numériques de travail, les systèmes d'information d'évaluation ou de certification.

N°8 |

Exigence

Les services numériques pour l'éducation outillant le système d'information pédagogique de l'établissement implémentent les fonctions d'échanges de données d'organisation scolaire avec les autres services numériques habilités. |

6.2.1. Périmètre des services numériques pour l'éducation

Les fournisseurs de solutions d'emploi du temps et/ou de vie scolaire outillent les processus et activités s'appuyant sur l'organisation pédagogique définie par le chef d'établissement.

La doctrine technique du numérique pour l'éducation décrit, dans son chapitre 4, le service pour la circulation des données d'organisation pédagogique (Scope).

6.2.2. Interface entre les fournisseurs de données et fournisseurs de service du périmètre

6.2.2.1. Echanges par API normalisées

N°9 |

Exigence

Les différents fournisseurs de données ou de services outillant les établissements et écoles pour leurs processus et activités pédagogiques permettent des communications basées sur des API normalisées et apportant des mesures de sécurité prouvant l'authentification des sujets, l'intégrité et la confidentialité des échanges. |

6.2.2.2. Contrats d'interface Scope

N°10 |

Exigence

Les services numériques éducatifs utilisent le service socle Scope pour la circulation des données d'organisation pédagogique du périmètre éducatif. |

A. Emplois du temps (« Scope entrée »)

Le contrat d'interface unique pour la remontée des données d'organisation pédagogique, entre le MEN pour le service SCOPE et chaque acteur fournissant un service d'élaboration et de gestion d'emploi du temps, est disponible aux acteurs habilités dans l'espace Pléiade (13)

« ESPACE ÉDITEURS INTERFACE ÉDUCATION NATIONALE » / rubrique « emploi du temps ».

B. Contrat d'interface Scope - Services habilités (« Scope sortie »)

Les contrats d'interface entre le service Scope du MENJ et chaque acteur habilité à récupérer des données issues des emplois du temps opérationnels seront disponibles à titre expérimental sous la seule forme d'API dans un premier temps. L'API Scope proposera plusieurs services (souscription sur demande à osmose.coord-gen@ac-dijon.fr), répondant chacun à des cas d'usage préalablement concertés avec les représentants des personnels de direction d'EPLE.

6.2.3. Normes et standards

N°11 |

Exigence

Pour la circulation des données d'organisation pédagogique, les services numériques pour l'éducation s'appuient sur des standards et éprouvés tels que EML (pour les messages de type courrier électronique), iCal (pour les invitations Agenda), vCard (pour les informations de contacts des utilisateurs) ou encore OneRoster (pour les listes de cours et les données associées). |

Le tableau ci-dessous présente les normes et standards utilisables, ainsi que leur statut, sur le périmètre de l'organisation pédagogique pour la vie scolaire.

Champs |

Organisme |

Standards |

Observation |

Statut |

Protocole / format |

1EdTech |

OneRoster |

Profil français à venir, dans le cadre des travaux avec 1Edtech.

Éléments d'échange de toutes les données de vie scolaire |

Cible |

Format |

IETF |

EML |

Format de fichier pour les messages électroniques |

Cible |

Format |

Internet Mail Consortium |

vCard |

Format de carnet d'adresses |

Cible |

Format |

IETF |

iCal |

Internet Calendaring and Scheduling Core Object Specification pour l'échange et le déploiement des événements de calendrier et de planification. |

Cible |

6.3. Portails de services numériques et ressources et services numériques pour l'enseignement et les pratiques pédagogiques

Les pratiques pédagogiques des enseignants s'appuient sur les programmations pédagogiques annuelles et périodiques (progressions) outillées par des services numériques de type « cahier de textes » pour sérier et organiser les activités associées ainsi que par des ressources numériques éducatives fournissant du contenu et des outils au bénéfice de l'enseignement et de l'apprentissage.

N°12 |

Exigence

Les services numériques pour l'éducation fournissant des fonctions de ressources et services numériques pour l'enseignement et les pratiques pédagogiques organisent leurs contenus selon une description sémantique normalisée et permettent l'intégration de granules pour réutiliser facilement des contenus ou des modules d'évaluation, pour rendre compte des expériences d'apprentissage ou encore pour assurer le suivi en continu de l'activité des élèves. |

6.3.1. Fournisseurs de ressources et services numériques pour l'enseignement et les pratiques pédagogiques

Les fonctions d'enseignement et pratiques pédagogiques sont outillées par de nombreux ressources ou services numériques, dont le choix est opéré par les enseignants au titre de leur liberté pédagogique, exercée dans le cadre de leur établissement/école eux-mêmes bénéficiaires des projets territoriaux de ressources et services numériques.

En raison de la diversité des projets territoriaux et des fournisseurs de services concernés, il est indispensable de partager des principes permettant de trouver, accéder, éditer et intégrer les outils et ressources pédagogiques de manière transparente entre les services ou portails de services, tout en garantissant la protection des données à caractère personnel des élèves et des personnels d'éducation.

Le document principal de la doctrine technique du numérique pour l'éducation décrit le cadre du SDET pour les ENT, de CARMO pour les projets d'équipements individuels, de CARINE pour les services d'infrastructures ainsi que le service GAR pour la gestion des accès aux ressources.

6.3.2. Exigences pour les fournisseurs de données et fournisseurs de service du périmètre

6.3.2.1. Alimentation des portails de services numériques territoriaux

N°12 bis |

Exigence

Les portails de services numériques portés par des projets territoriaux alimentent leur base des données à partir du système d'information du ministère sur la base des processus d'alimentation définis et encadrés par l'annuaire fédérateur. |

Actuellement, l'annuaire fédérateur fournit des exports pour les projets d'ENT et d'équipements mobiles.

6.3.2.2. Intégration de contenus pour les parcours pédagogiques

N°13 |

Exigence

Les services numériques pour l'éducation doivent permettre aux utilisateurs :

- de construire un parcours pédagogique avec des ressources pédagogiques ;

- d'utiliser des granules pédagogiques dans un parcours pédagogique sans sortir de celui-ci ;

- de suivre l'activité de l'élève tout au long d'un parcours. |

6.3.2.3. Portabilité et réversibilité

N°14 |

Exigence

Les services numériques pour l'éducation doivent permettre aux utilisateurs :

- de créer des parcours pérennes et réutilisables, donc indépendants des différents acteurs ;

- d'exporter et d'importer des granules ou des parcours pédagogiques. |

6.3.2.4. Echanges de données à caractère personnel - contrat d'interface GAR

N°15 |

Exigence

Les services numériques pour l'éducation utilisent les services socles pour la gestion des accès aux ressources (GAR). |

Le GAR permet d'assurer une autorité d'autorisation, en mettant en relation les données des utilisateurs avec les données des ressources

Les contrats d'interface permettant le raccordement au GAR sont fournis par le RTFS (référentiel technique, fonctionnel et de sécurité) du GAR. Celui-ci s'adresse aux partenaires, fournisseurs de ressources d'une part et projets ENT d'autre part. Il est organisé en trois opuscules et un paquetage :

- opus « Présentation générale » ;

- opus « Référentiel juridique et administratif » ;

- opus « Référentiel technique » ;

- paquetage de documents d'accompagnement et exemples.

Le RTFS comporte une version pour les fournisseurs d'identité, notamment les projets ENT et leurs exploitants, et une version pour les fournisseurs de ressources.

Le RTFS intègre le contrat d'interface des exploitants ENT ou des fournisseurs de ressources.

Il est disponible sur demande à l'adresse dne-gar@education.gouv.fr ou sur le site du GAR, dès la demande d'accrochage.

6.3.3. Normes et standards

N°16 |

Exigence

Pour répondre aux exigences d'intégration de contenus, de portabilité et de réversibilité, les services numériques pour l'éducation s'appuient sur des protocoles standards et éprouvés tels que xAPI ou LTI. |

Normes et standards utilisables pour l'enseignement avec leur statut

Champs |

Organisme |

Standard |

Observations |

Statut |

Suivre l'activité de l'élève tout au long d'un parcours (traces d'apprentissage) |

Données évènementielles / Protocole |

ADIL/IEEE |

xAPI |

Tin Can/xAPI est un standard paramétrable qui peut être utilisé dans tous les contextes (services numériques, plateformes pédagogiques, ressources numériques, évaluations formatives et sommatives, interactions pair à pair) pour collecter des données évènementielles permettant de rendre compte du parcours d'un élève en le suivant pas à pas, et des usages d'une plateforme, d'un service ou d'une ressource. |

Cible |

Données évènementielles / Protocole |

1EdTech |

Caliper Analytics |

Le standard Caliper offre un cadre normalisé et largement adopté pour la collecte et l'analyse des données événementielles liées à l'apprentissage, favorisant ainsi une meilleure compréhension de l'activité des élèves tout au long de leur parcours éducatif. |

Cible |

Exporter et importer des granules ou des parcours pédagogiques |

Métadonnées de définitions des contenus / Modèle logique de données et sérialisation |

1EdTech |

Common Cartridge |

Une norme de packaging des contenus pour échanger des contenus et des parcours pédagogiques. |

Cible |

Données pour le conditionnement et l'intégration des contenus / Modèle logique de données et sérialisation |

ADL/IEEE |

Scorm |

Format pour développer et publier des ressources d'apprentissage numériques réutilisables dans des systèmes de gestion de l'apprentissage et d'autres environnements d'apprentissage. |

En fin de vie |

Utiliser des granules pédagogiques dans un parcours pédagogique |

Données pour le conditionnement et l'intégration des contenus / Modèle logique de données et sérialisation |

Groupe H5P |

H5P |

H5P est un plugin pour les systèmes de publication existants qui permet aux utilisateurs de créer du contenu interactif comme des vidéos interactives, des présentations, des jeux, des quiz et bien d'autres. |

Cible |

Données pour le conditionnement et l'intégration des contenus |

1EdTech |

QTI |

Format d'échange de questions et de structures de test, d'informations sur la notation |

Cible |

Données pour le conditionnement et l'intégration des contenus / Protocole |

1EdTech |

LTI |

Protocole permettant à un système de gestion de l'apprentissage d'intégrer des outils d'apprentissage personnalisés ou des expériences proposées par un autre système. |

Cible |

Décrire des ressources pédagogiques |

Métadonnées de définitions des contenus / Dictionnaires de données, modèle logique de données et sérialisation |

IEEE / AFNOR |

ScoLOMFR |

Description des ressources. |

Cible |

6.4. Examens, certifications et concours

Le tableau ci-dessous présente les normes et standards utilisables ainsi que leur statut pour les examens, certifications et concours.

Champs |

Organisme |

Standard |

Observation |

Statut |

Modèle de données |

Commission Européenne |

European Learning Model (ELM) |

Modèle de données multilingue pour l'interopérabilité des possibilités d'apprentissage, des qualifications, de l'accréditation et des titres de compétences en Europe. |

Cible |

Modèle de données |

1EdTech |

Open Badge |

Méthode pour regrouper des informations sur une reconnaissance ou une réalisation unique, telle qu'une microcertification, une aptitude, une compétence ou un diplôme. |

Cible |

6.5. Pilotage des missions éducatives

6.5.1. Fournisseurs de données et de services pour l'évaluation des services numériques pour l'éducation

Le pilotage des missions éducatives relève de différents niveaux de décision, de l'établissement ou de l'école, jusqu'aux services du ministère chargé de l'éducation nationale, en passant par les académies et collectivités territoriales.

Des dispositifs d'évaluation permettent d'outiller les besoins de pilotage de chacun de ces niveaux de décision, afin d'apporter une aide au pilotage de la politique publique d'éducation et des projets de services numériques pour l'éducation en particulier.

6.5.2. Exigences pour les fournisseurs de ressources et services numériques pour l'éducation

6.5.2.1. Utilisation d'indicateurs de fréquentation normés

Le nombre de visites est l'indicateur standard des outils de mesure d'audience. Il représente la consultation de pages d'un site. L'utilisation de services numériques pour l'éducation nécessitant la plupart du temps une authentification, chaque visite est effectuée par un utilisateur.

N°17 |

Exigence

Pour répondre aux besoins de pilotage des projets et politiques numériques, les services numériques pour l'éducation sont capables de fournir a minima deux indicateurs principaux : la visite et l'utilisateur. |

Si un utilisateur reste inactif plus de trente minutes avant de reprendre son activité, il génère deux visites. Si sa période d'inactivité est inférieure à trente minutes, il ne génère qu'une visite.

Si deux utilisateurs se connectent depuis le même ordinateur (ou autre appareil) ; ils génèrent chacun une visite et sont considérés comme différents.

Vous pouvez consulter l'intégralité du texte avec ses images à partir de l'extrait du Journal officiel électronique authentifié accessible en bas de page

6.5.2.2. Intégration dans le DNMA - dispositif de mesure d'audience

Le DNMA est défini comme service socle au chapitre 4 de la doctrine technique du numérique pour l'éducation.

Les services de type ENT qui s'inscrivent dans le DNMA bénéficient du cadre normalisé retenu pour ce dispositif. La définition des indicateurs produits par ce dispositif est celle retenue par l'ACPM (alliance pour les chiffres de la presse et des médias) et l'outil de recueil des indicateurs est certifié par cette association professionnelle française.

Le DNMA repose sur une solution de « marquage » externe conforme à un cahier des charges partagé qui définit le contenu et la structure des marqueurs. Le cahier des charges est composé :

- du référentiel fonctionnel et technique d'intégration (RFTI) :

- description des indicateurs utilisés ;

- liste de référence des indicateurs « service » et « outil » ;

- informations techniques et fonctionnelles nécessaires à la mise en œuvre du marqueur DNMA ;

- description des exigences pour être conforme au DNMA ;

- description des options d'implémentations complémentaires ;

- du plan de marquage :

- il s'agit de la table de correspondance entre les pages et fonctionnalités de la plateforme ENT et le référentiel des services du dispositif qui permet d'interpréter les statistiques du dispositif ;

- le plan de marquage est propre à chaque plateforme ENT ;

- le respect du plan de marquage est une exigence de conformité au DNMA.

6.5.3. Normes et standards pour la mesure de la fréquentation

N°18 |

Exigence

Pour répondre aux besoins de pilotage et fournir des indicateurs de fréquentation normés, les ressources et services numériques pour l'éducation s'appuient sur des indicateurs inscrits dans le DNMA. |

7. Synthèse des standards retenus

Vous pouvez consulter l'intégralité du texte avec ses images à partir de l'extrait du Journal officiel électronique authentifié accessible en bas de page

Figure 7 : Synthèse des standards retenus

Champs |

Organisme |

Standards |

Observation |

Statut |

Protocole |

IETF |

HTTPS |

HyperText Transfer Protocol Secure : combinaison du HTTP avec une couche de chiffrement TLS. |

Cible |

Protocole |

|

REST |

Representational state transfert.

Style d' architecture logicielle définissant un ensemble de contraintes à utiliser pour créer des services web. |

Cible |

Format |

IETF |

JSON |

JavaScript Object Notation.

Format de données textuel dérivé de la notation des objets du langage JavaScript. |

Cible |

Format |

W3C |

XML |

Extensible Markup Language.

L'objectif initial de XML est de faciliter l'échange automatisé de contenus complexes entre systèmes d'informations hétérogènes. |

En usage |

Protocole |

OIDF |

Open ID Connect (OIDC) |

Couche d'identification basée sur OAuth 2.0, dispositif d'autorisation. |

Cible |

Protocole |

Internet engineering task force (IETF) |

OAuth2 |

Protocole d'autorisation. Inclus dans OIDC. |

Cible |

Protocole |

Organization for the Advancement of Structured Information Standards (OASIS) |

SAML 2.0 |

Utilisé par le GAR.

Permet l'échange de données d'authentification et d'autorisation entre domaines de sécurité. |

En usage |

Protocole |

APEREO |

CAS |

Central Authentification Service (Système d'authentification unique). Support OIDC, OAuth2 et SAML |

Fin de vie |

Protocole / format |

1EdTech |

OneRoster |

Profil français à venir, dans le cadre des travaux avec 1Edtech. Éléments d'échange de toutes les données de vie scolaire. |

Cible |

Format |

IETF |

EML |

Format de fichier pour les messages électroniques. |

Cible |

Format |

Internet Mail Consortium |

vCard |

Format de carnet d'adresses. |

Cible |

Format |

IETF |

iCal |

Internet Calendaring and Scheduling Core Object Specification pour l'échange et le déploiement des événements de calendrier et de planification. |

Cible |

Données évènementielles / Protocole |

ADIL/IEEE |

xAPI |

Un protocole pour rapporter et suivre les traces laissées par les activités. |

Cible |

Données évènementielles / Protocole |

1EdTech |

Caliper Analytics |

Le standard Caliper offre un cadre normalisé et largement adopté pour la collecte et l'analyse des données événementielles liées à l'apprentissage, favorisant ainsi une meilleure compréhension de l'activité des élèves tout au long de leur parcours éducatif. |

Cible |

Métadonnées de définitions des contenus

/ Modèle logique de données et sérialisation |

1EdTech |

Common Cartridge |

Une norme de packaging des contenus pour échanger des contenus et des parcours pédagogiques. |

Cible |

Données pour le conditionnement et l'intégration des contenus / Modèle logique de données et sérialisation |

ADL/IEEE |

Scorm |

Format pour développer et publier des ressources d'apprentissage numériques réutilisables à utiliser dans des systèmes de gestion de l'apprentissage et d'autres environnements d'apprentissage. |

En fin de vie |

Données pour le conditionnement et l'intégration des contenus / Modèle logique de données et sérialisation |

Groupe H5P |

H5P |

H5P est un plugin pour les systèmes de publication existants qui permet aux utilisateurs de créer du contenu interactif comme des vidéos interactives, des présentations, des jeux, des quiz et bien plus encore. |

Cible |

Données pour le conditionnement et l'intégration des contenus |

1EdTech |

QTI |

Format d'échange de questions et de structures de test, d'informations sur la notation |

Cible |

Données pour le conditionnement et l'intégration des contenus / Protocole |

1EdTech |

LTI |

Protocole permettant à un système de gestion de l'apprentissage d'intégrer des outils d'apprentissage personnalisés ou des expériences proposées par un autre système. |

Cible |

Métadonnées de définitions des contenus

/ Dictionnaires de données, modèle logique de données et sérialisation |

IEEE |

ScoLOMFR |

Description des ressources. |

Cible |

Modèle de données |

Commission Européenne |

European Learning Model (ELM) |

Modèle de données multilingues pour l'interopérabilité des possibilités d'apprentissage, des qualifications, de l'accréditation et des titres de compétences en Europe. |

Cible |

Modèle de données |

1EdTech |

Open Badge |

méthode pour regrouper des informations sur une reconnaissance ou une réalisation unique, telle qu'une microcertification, une aptitude, une compétence ou un diplôme. |

Cible |

8. Cas d'usage

8.1. Accéder à une ressource pédagogique

Description

Un élève souhaite accéder à une ressource numérique depuis son parcours pédagogique.

Exemple de scénario d'accès via le GAR

L'élève se connecte sur le service numérique de son établissement (ENT/OVS/LMS) via ÉduConnect.

A partir de son parcours pédagogique, l'élève accède à une ressource numérique (via un lien profond).

Une session d'apprentissage s'ouvre sur le fournisseur de ressources depuis le navigateur de l'élève.

Hypothèses

Les responsabilités liées à l'accès et l'utilisation des ressources sont encadrées par le contrat GAR / RGPD.

Le fournisseur de ressources est accessible via une URL du GAR

L'authentification unique (SSO) réalisée par l'élève via ÉduConnect permet au GAR d'identifier l'élève.

La ressource permet un accès granulaire.

Pas d'utilisation d'outil propriétaire pour la visualisation de contenu.

Normes et standards concernés par ce cas d'usage

Source |

Destination |

Protocole de transport |

Norme d'échange |

Contrat d'interface |

Description |

ENT/OVS/LMS |

ÉduConnect |

HTTPS-REST |

OIDC |

ÉduConnect |

Identité de l'élève fournie par ÉduConnect après authentification |

GAR |

ENT/OVS/LMS |

HTTPS |

LTI |

GAR |

L'accès à la ressource est réalisé via une URL GAR. Celui-ci relaie l'accès au fournisseur de ressources après un contrôle d'autorisation |

ENT/OVS/LMS |

Fournisseur de ressources |

HTTPS |

LTI |

A définir |

Ouverture d'une session LTI entre le navigateur de l'élève et le serveur du fournisseur de ressources |

ENT/OVS/LMS |

ENT/OVS/LMS |

REST |

xAPI |

A définir |

Enregistrer les traces d'apprentissage |

8.2. Faciliter l'intégration des ressources dans un LMS pour une utilisation sans couture dans un parcours pédagogique

Description

Un enseignant souhaite créer un parcours pédagogique basé sur des ressources numériques fournies par plusieurs éditeurs tiers.

Exemple de scénario d'accès via le GAR

L'enseignant se connecte sur le service numérique de son établissement (ENT/OVS/LMS).

Il construit son parcours pédagogique en utilisant une liste de ressources accessibles, remontée par le GAR dans le médiacentre proposé par le service numérique.

Hypothèses

Le GAR est le fournisseur de métadonnées sur les ressources.

Le GAR reconnait l'identité de l'enseignant connecté sur son outil numérique.

La liste de ressources remontée par le GAR est à la fois accessible par l'enseignant et par les élèves auxquels est destiné le parcours pédagogique.

L'ENT est le fournisseur de l'identifiant de l'utilisateur pour le GAR.

Flux techniques et normes

Source |

Destination |

Protocole |

Norme ou standard |

Contrat d'interface |

Description |

Guichet Agents |

ENT/OVS/L MS |

REST |

OpenID Connect |

Guichet Agents |

Authentification et identification de l'enseignant |

GAR |

ENT/OVS/L MS |

REST |

ScoLOMFR |

GAR |

Fourniture de la liste de ressources accessibles à l'enseignant |

8.3. Assurer la portabilité des contenus d'un parcours pédagogique lors d'un changement de LMS

Description :

Un enseignant / un personnel de direction souhaite, dans le cadre d'un changement d'établissement, faire le transfert et la reprise de ses données depuis la solution numérique de l'établissement de départ jusqu'à la solution numérique de l'établissement d'arrivée.

Exemple de scénario exécuté sur l'ENT de l'établissement de départ

L'enseignant/PERDIR se connecte sur l'ENT de son établissement de départ puis saisit une demande de changement d'établissement et de transfert de son dossier vers un établissement d'arrivée. Il sélectionne ensuite une liste des contenus à transférer.

L'ENT de départ envoie une demande à l'ENT d'arrivée avec la liste des contenus (cahier de texte, messagerie, parcours Moodle, ressources pédagogiques, etc.) et leurs formats sources.

L'ENT d'arrivée analyse la demande et répond avec la liste des contenus et formats compatibles.

Exemple de scénario exécuté sur l'ENT de l'établissement d'arrivée

L'enseignant/PERDIR se connecte sur l'ENT de son établissement d'arrivée.

L'ENT télécharge et intègre automatiquement les données dont le format est compatible avec la solution ENT de l'établissement d'arrivée.

L'enseignant/PERDIR réalise le téléchargement manuel des contenus dont le format n'est pas compatible avec l'ENT de l'établissement d'arrivée. L'opération est exécutée via l'IHM de l'ENT de l'établissement d'arrivée.

Hypothèses :

Les ENT de départ et d'arrivée sont capables de reconnaitre l'identité de l'enseignant/PERDIR demandant le transfert.

Source |

Destination |

Protocole

de transport |

Norme d'échange |

Contrat d'interface |

Description |

Guichet Agents |

ENT1 (départ) / ENT2 (arrivée) |

REST |

OpenId Connect |

Guichet Agents : +lien |

Fourniture de l'identité de l'enseignant |

ENT1

(départ) |

ENT2 (arrivée) |

REST |

JSON |

Contrat d'interface unique pour les ENT :

+lien |

Liste des contenus avec leur formats locaux |

ENT2

(arrivée) |

ENT1 (départ) |

REST |

JSON |

Contrat d'interface unique pour les ENT :

+lien |

Liste des contenus avec les formats compatibles |

ENT1

(départ) |

ENT2 (arrivée) |

REST / S3 |

Binaire, ScoLOMFR,

Schema.org |

Contrat d'interface unique pour les ENT :

+lien |

Téléchargement des contenus binaires, ou formatés comme les liste d'indexes SCOLORMFR/Schema.org |

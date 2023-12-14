# Délibération n° 2023-150 du 14 décembre 2023 portant avis sur un projet d'arrêté modifiant l'arrêté du 21 février 2014 portant création par la direction générale des finances publiques d'un traitement automatisé de lutte contre la fraude dénommé « ciblage de la fraude et valorisation des requêtes »

- Nature : Deliberation
- Type : Avis
- Numéro : 2023-150
- Date : 2023-12-14
- Publication : 2024-12-14
- NOR : CNIX2430698X
- État : VIGUEUR
- Légifrance : https://www.legifrance.gouv.fr/cnil/id/CNILTEXT000050773162

Date de l'avis : 14 décembre 2023.

|

N° de la délibération : n° 2023-150. |

N° de demande d'avis : DA 1726052.V9.

Organisme(s) à l'origine de la saisine : ministère de l'économie, des finances et de la souveraineté industrielle et numérique. |

Textes concernés : projet d'arrêté modifiant l'arrêté du 21 février 2014 portant création par la direction générale des finances publiques d'un traitement automatisé de lutte contre la fraude dénommé ciblage de la fraude et valorisation des requêtes . |

Thématiques : recouvrement de l'impôt, lutte contre la fraude, collecte de données sur les plateformes et les réseaux sociaux. |

Fondement de la saisine : article 31, I, 2°, de la loi du 6 janvier 1978 modifiée. |

L'essentiel :

La CNIL a été saisie par le ministère de l'économie, des finances et de la souveraineté industrielle et numérique pour avis d'un projet d'arrêté visant, en particulier, à préciser les finalités du traitement ciblage de la fraude et valorisation des requêtes (CFVR), à modifier les destinataires des données et, enfin, à prévoir l'alimentation par les résultats du traitement de plusieurs outils métiers de la Direction générale des finances publiques (DGFiP).

La CNIL considère que les modifications envisagées sont légitimes. A la lumière des récentes jurisprudences française et européenne s'agissant du régime juridique applicable aux traitements de l'administration fiscale, elle estime que le traitement CFVR relève du RGPD.

Elle rappelle la nécessité de respecter les principes de protection des données par conception et par défaut dans le développement des outils métiers à destination des agents de son administration. En particulier, les destinataires des résultats du traitement devront être limités à ceux qui ont besoin d'en connaître, eu égard à leurs missions respectives.

Il revient au ministère de faire preuve d'une grande prudence dans la conception et l'utilisation de ce type de traitements algorithmiques, compte tenu des risques qu'ils présentent et des biais dont ils peuvent souffrir. La CNIL recommande en particulier la mise en place de formations spécifiques permettant aux agents en charge de la programmation et des contrôles de maîtriser les principes des algorithmes utilisés.

La Commission nationale de l'informatique et des libertés,

Vu le règlement (UE) 2016/679 du Parlement européen et du Conseil du 27 avril 2016 relatif à la protection des personnes physiques à l'égard du traitement des données à caractère personnel et à la libre circulation de ces données, et abrogeant la directive 95/46/CE (règlement général sur la protection des données ou RGPD) ;

Vu la loi n° 78-17 du 6 janvier 1978 modifiée relative à l'informatique, aux fichiers et aux libertés ( loi informatique et libertés ), notamment ses articles 4, 31, 47 et 52 ;

Après avoir entendu le rapport de M. Philippe-Pierre CABOURDIN, commissaire, et les observations de M. Damien MILIC, commissaire du Gouvernement,

Adopte la délibération suivante :

I. - La saisine

A. - Le contexte

La lutte contre la fraude fiscale est un objectif de valeur constitutionnelle qui légitime certaines actions du Gouvernement et de l'administration en faveur d'une détection efficiente des manquements et des infractions prévus au code des impôts. Ces actions s'inscrivent dans la feuille de route gouvernementale de lutte contre toutes les fraudes aux finances publiques, présentée en juin 2023.

Dans le but d'améliorer la programmation des contrôles fiscaux, le ministère de l'économie, des finances et de la souveraineté industrielle et numérique met en œuvre depuis 2014 le dispositif de ciblage de la fraude et de valorisation des requêtes (CFVR) faisant appel à des techniques de fouille de données ( datamining ). Ce traitement, qui n'a pas pour but de remplacer l'analyse des agents, vise un meilleur ciblage du contrôle des particuliers et des professionnels qui pourraient se trouver en situation de manquement ou de fraude. Pour ce faire, le traitement CFVR fait appel, d'une part, à l'agrégation de plusieurs bases de données internes à la direction générale des finances publiques (DGFiP), comme les fichiers des comptes bancaires (traitement FICOBA ) et des contrats de capitalisation et d'assurance-vie (traitement FICOVIE ), et externes, telles que certaines données des unions de recouvrement des cotisations de sécurité sociale et d'allocations familiales (URSSAF), et, d'autre part, à des modèles statistiques probabilistes reposant sur la recherche d'atypies ou d'incohérences, sur l'expérience acquise par la DGFiP ainsi que sur l'analyse de réseaux afin de faire apparaître de possibles liens entre des personnes physiques ou morales. Le bureau en charge de la programmation des contrôles et de l'analyse des données au sein de la DGFiP (SJCF-1D) mène ces travaux visant à mieux caractériser une personne ou une entreprise potentiellement frauduleuse.

Initialement mis en œuvre en 2014 à titre expérimental, dans le cadre de la recherche de fraudes commises par les contribuables professionnels, le traitement CFVR a été pérennisé en 2015 pour ces contribuables et étendu concomitamment, à titre d'expérimentation, aux personnes physiques impliquées dans le fonctionnement des entités professionnelles. Cette extension a elle-même été pérennisée en 2016, puis ce traitement a été élargi une nouvelle fois en 2017 aux particuliers à titre expérimental jusqu'en août 2019. Parallèlement, les finalités de ce traitement ont été étendues afin de permettre la détection anticipée des entreprises en difficulté ainsi que l'envoi automatique de demandes de compléments d'informations aux contribuables. Enfin, à titre expérimental, la loi a autorisé l'administration fiscale, à des fins de recherche d'infractions limitativement énumérées, à collecter et à exploiter les contenus librement accessibles et manifestement rendus publics par les utilisateurs sur les plateformes et les réseaux sociaux (article 154 de la loi n° 2019-1479 du 28 décembre 2019 de finances pour 2020). Chacune de ces modifications a fait l'objet d'un avis de la CNIL.

B. - L'objet de la saisine

La CNIL a été saisie pour avis, sur le fondement du 2° du I de l'article 31 de la loi n° 78-17 du 6 janvier 1978 modifiée, par le ministère de l'économie, des finances et de la souveraineté industrielle et numérique, d'un projet d'arrêté modifiant l'arrêté du 21 février 2014 portant création par la direction générale des finances publiques d'un traitement automatisé de lutte contre la fraude dénommé ciblage de la fraude et valorisation des requêtes .

Le projet d'arrêté :

- précise les finalités du traitement et modifie le régime juridique qui lui est applicable ;

- complète la liste des données à caractère personnel traitées ;

- reformule la présentation des destinataires des données à caractère personnel et précise les applications métiers qui seront alimentées par les résultats du traitement ;

- modifie les bases légales sur lesquelles reposent les droits des personnes concernées en cohérence avec le régime juridique choisi ;

- écarte l'objectif de mise en œuvre d'un dispositif de journalisation pour ce traitement, dont la date butoir était le 6 mai 2023.

Dans la mesure où le traitement CFVR est susceptible d'engendrer un risque élevé pour les droits et les libertés des personnes physiques, le ministère a réalisé une analyse d'impact relative à la protection des données à caractère personnel (AIPD) qui a été adressée à la CNIL avec la demande d'avis.

II. - L'avis de la CNIL

A titre liminaire :

- la CNIL rappelle l'engagement du ministère, tel que formalisé par la délibération du 12 septembre 2019 portant sur ce même traitement, de lui communiquer régulièrement des bilans sur les conditions d'utilisation et d'exploitation [du] traitement [CFVR] et sur les coûts afférents (CNIL, SP, 12 septembre 2019, traitement CFVR , n° 2019-115, publié). Il était précisé qu'une telle transmission pouvait être annuelle. Bien que le ministère se soit engagé au cours de l'instruction à adresser ce bilan au plus tard au deuxième trimestre 2023, la CNIL constate l'absence de transmission des rapports de fonctionnement réguliers de ce traitement, et ce, d'autant plus que celui-ci est d'une complexité et d'une ampleur significatives ;

- dans la délibération n° 2018-346 du 8 novembre 2018, le ministère s'était engagé à édicter un acte réglementaire dédié au traitement relatif à la détection anticipée des entreprises en difficulté (CNIL, SP, 8 novembre 2018, traitement CFVR , n° 2018-346). La CNIL constate, là encore, l'absence d'un tel acte. Compte tenu de la multiplicité des finalités du traitement CFVR, ce texte apparait nécessaire afin, d'une part, de rendre intelligibles les objectifs des traitements respectifs de CFVR et, d'autre part, de distinguer clairement les régimes juridiques applicables.

A. - Sur les finalités du traitement et le régime juridique applicable

L'article 1er du projet d'arrêté modifie les finalités du traitement qui viserait dorénavant à modéliser et [à] visualiser les anomalies fiscales afin de programmer des opérations de recherche, de constatation ou de poursuite de manquements fiscaux et d'amélioration du respect des obligations fiscales des usagers. . Cette finalité ne fait plus référence aux actions de prévention, de recherche, de constatation ou de poursuites d'infractions pénales , telles que l'article 2 de l'arrêté du 21 février 2014 le prévoit dans sa version actuelle.

Le ministère précise que cette modification n'est pas un changement de nature du traitement CFVR mais permet de mieux rendre compte de ses finalités. Cette clarification, ainsi que sa lecture des jurisprudences française et européenne, conduisent le ministère à substituer le régime du RGPD au titre III de la loi du 6 janvier 1978 modifiée, qui transpose la directive 2016/680 du 27 avril 2016 (dite Police-Justice ), jusqu'alors applicable à ce traitement.

Plusieurs jurisprudences européennes précisent le régime juridique applicable aux traitements mis en œuvre par l'administration fiscale au titre de ses missions :

- la Cour de justice de l'Union européenne (CJUE) indique que les exceptions au champ d'application du RGPD, telles que prévues au 2 de l'article 2 de ce dernier, doivent recevoir une interprétation stricte (CJUE, grande chambre, 16 juillet 2020, Facebook Ireland et Schrems, C-311/18, EU:C:2020:559, point 84) ;

- dans sa décision Puškár du 27 septembre 2017, la CJUE a estimé que lorsque des données sont collectées et utilisées aux fins de la perception de l'impôt et de la lutte contre la fraude fiscale , ces traitements relèvent de la directive 95/46/CE du 24 octobre 1995, texte de référence en termes de protection des données à caractère personnel jusqu'à l'entrée en vigueur du RGPD. Elle juge également que même s'il n'apparaît pas exclu que lesdites données puissent être utilisées dans le cadre de poursuites pénales qui pourraient être exercées, en cas d'infraction dans le domaine fiscal, contre certaines personnes dont les noms figurent sur la liste litigieuse, les données en cause au principal n'apparaissent pas avoir été collectées dans l'objectif spécifique de l'exercice de telles poursuites pénales ou dans le cadre des activités de l'Etat relatives à des domaines du droit pénal (CJUE, deuxième chambre, 27 septembre 2017, Puškár, C-73/16, EU:C:2017:725, points 40-44) ;

- la CJUE a confirmé cette jurisprudence, après l'entrée en vigueur du RGPD, dans sa décision Valsts ieņēmumu dienests du 24 février 2022. Elle a ajouté que la notion d' autorité compétente , telle que précisée aux considérants 10 et 11 de la nouvelle directive Police-Justice, doit être comprise en lien avec la protection des données à caractère personnel dans le domaine de la coopération judiciaire en matière pénale et de la coopération policière, compte tenu des aménagements qui peuvent s'avérer nécessaires, à cet égard, en raison de la nature spécifique de ces domaines (CJUE, cinquième chambre, 24 février 2022, Valsts ieņēmumu dienests, C-175/20 ; EU:C:2022:124, point 43).

Au niveau national, la Cour de cassation a, le 1er juin 2023, appliqué la jurisprudence européenne en indiquant qu'un traitement de données mis en œuvre par l'administration fiscale aux fins d'obtenir l'autorisation de procéder à des opérations de visite et saisies sur le fondement de l'article L. 16 B du livre des procédures fiscales, qui a pour finalité d'obtenir le droit de procéder à une mesure d'enquête pouvant donner lieu à la constatation d'une infraction ou d'un manquement à la législation fiscale, dans le but de percevoir l'impôt et de lutter contre la fraude fiscale, entre dans le champ d'application matériel du RGPD. (Cour de cassation, chambre commerciale, financière et économique, 1er juin 2023, pourvoi n° F 21-18.558, point 10).

Selon les éléments fournis par le ministère, le traitement CFVR n'a qu'à titre accessoire pour objet de détecter des manquements fiscaux susceptibles de donner lieu à une transmission au parquet en vue d'une poursuite pénale. Selon le ministère, moins de 700 infractions liées à la fraude fiscale seraient constatées par le juge chaque année, soit moins de 1 % des contrôles réalisés. La finalité principale du traitement est la constatation des manquements fiscaux dans le cadre de la lutte contre la fraude fiscale opérée par l'administration. En outre, le ministère souligne que l'extension régulière du champ du traitement CFVR, dans une période de facilitation de la correction des erreurs commises par les contribuables de bonne foi ouverte par la loi du 10 août 2018 pour un Etat au service d'une société de confiance (dite loi ESSOC ), le conduit également à considérer que la régularisation de la situation fiscale des redevables est une finalité importante du traitement.

Au regard de la jurisprudence européenne mentionnée ci-dessus, d'une part, l'administration fiscale ne semble pas constituer en l'espèce une autorité compétente , au sens de la directive Police-Justice, lorsqu'elle agit au titre de ses missions de contrôle fiscal ; d'autre part, les finalités de régularisation ou de lutte contre la fraude fiscale relèvent d'après la CJUE du RGPD, sans qu'y fasse obstacle le fait que, dans certains cas, il y ait transmission au parquet.

Au vu de ces éléments, et plus particulièrement de l'évolution de la jurisprudence en la matière, la CNIL estime que le traitement CFVR est soumis au RGPD. Elle souligne qu'il en résulte que les droits des personnes ne doivent pas faire l'objet des restrictions prévues par la directive Police-justice et ne peuvent être aménagé que lorsque cela pourrait nuire à l'objectif de lutte contre la fraude fiscale, en application des dispositions permettant des dérogations ou dans le cadre restreint de l'article 23 du RGPD. La CNIL sera attentive au respect des droits des personnes s'agissant notamment du recours à ces dérogations.

Dès lors que le traitement peut donner lieu à la saisine du parquet, et que cette transmission ne s'effectue pas dans des conditions de droit commun mais en fonction d'un choix propre de l'administration fiscale en application de l'article L. 228 du livre des procédures fiscales, la CNIL recommande, à titre de mesure de transparence, que cette finalité accessoire demeure mentionnée dans l'arrêté et invite le ministère à reformuler les finalités du traitement rédigées à l'article 1er du projet d'arrêté.

Enfin, la CNIL relève que, dans la mesure où le traitement CFVR comporte un objet pénal au sens du 2° du I de l'article 31 de la loi du 6 janvier 1978 modifiée, elle continuera d'être saisie par le ministère des futures modifications de ce traitement. La CNIL considère également que la transmission, à l'occasion de ces saisines, de l'AIPD afférente à ce traitement est une bonne pratique à laquelle elle est favorable.

B. - Sur les catégories d'accédants et de destinataires

L'article 3 du projet d'arrêté précise que seuls les agents territorialement compétents chargés de la gestion, de la programmation et du contrôle des dossiers des professionnels et des particuliers seront rendus destinataires des données personnelles strictement utiles à leur mission .

En premier lieu, la CNIL remarque que l'AIPD fournie par le ministère procède à une distinction stricte du régime d'accès suivant, d'une part, la phase de développement des modèles algorithmiques et, d'autre part, la phase d'exploitation des résultats du traitement. Afin de garantir une plus grande lisibilité des principes régissant l'accès aux données du traitement CFVR, la CNIL considère que cette distinction, qu'elle accueille favorablement depuis le début de la mise en œuvre du traitement, pourrait expressément apparaître dans le projet d'arrêté.

En second lieu, elle remarque que, en y incluant la gestion des dossiers des particuliers, le ministère élargit significativement le nombre de services accédant aux dossiers ayant été ciblés par le traitement CFVR. Le ministère précise, dans la documentation fournie, qu'il s'agit notamment de prévoir l'accès des agents en charge du recouvrement et de ceux en charge du contentieux à certains éléments de ces dossiers. Le ministère indique également que les agents en charge du recouvrement et du contentieux n'auront pas accès à aux fiches produites par le service SJCF-1D, accompagnant les dossiers ciblés par le traitement CFVR.

Elle constate que les finalités du traitement, selon la nouvelle formulation du projet de texte, sont la modélisation et la visualisation des anomalies fiscales afin de programmer des opérations de recherche, de constatation ou de poursuite de manquements fiscaux et l'amélioration du respect des obligations fiscales des usagers. . Compte tenu de ces finalités, la CNIL estime que seuls les agents en charge de la programmation et du contrôle devraient pouvoir avoir accès aux fiches afférentes au traitement CFVR produites par le service SJCF-1D. En conséquence, elle demande au ministère de modifier le projet d'arrêté afin de détailler les services pouvant avoir accès : aux différentes bases de données dans le cadre du développement des traitements algorithmiques de CFVR ; aux fiches produites par le service SJCF-1D ; ou seulement à certains éléments des dossiers ciblés par ce traitement, voire au dossier dans son ensemble.

C. - Sur les mises en relation

L'article 3 du projet d'arrêté prévoit également, dans le cadre du projet pilotage et analyse du contrôle (PILAT) visant à moderniser et à simplifier le travail des agents de l'administration fiscale par le développement de nouveaux outils métiers, l'alimentation de deux nouvelles applications grâce aux résultats du traitement CFVR :

- l'application GALAXIE , ayant déjà fait l'objet d'un avis de la CNIL (CNIL, SP, 17 février 2022, traitement GALAXIE , n° 2022-025, publié), permettant de connaître les liens d'associés, d'actionnaires et de dirigeants entre, d'une part, des personnes physiques ou morales et, d'autre part, des sociétés (v. arrêté du 11 mars 2022 portant autorisation par la direction générale des finances publiques du traitement de données à caractère personnel dénommé GALAXIE). Le ministère précise que les liens identifiés entre des personnes morales ou physiques, par l'application CFVR, seront transmis à l'application GALAXIE afin d'être consultables par les agents chargés des opérations de validation et de contrôle ;

- l'application PILOT CF ayant pour objet le suivi de l'ensemble du processus de contrôle fiscal, le pilotage des services et le suivi d'activité pour les agents concernés et, enfin, le suivi statistique du contrôle. Le ministère précise que le bureau SJCF-1D intégrera, trimestriellement ou mensuellement, des listes de dossiers de contribuables professionnels et particuliers présentant des risques fiscaux détectés par le traitement CFVR.

Le ministère précise que la nouvelle application métier VUE 360 sera également alimentée par les résultats du traitement CFVR. Cette dernière application permet aux agents chargés du contrôle, afin d'appréhender les situations fiscales dans leur globalité, d'accéder à une vue d'ensemble des bases de données de la DGFiP dans lesquelles l'entreprise ou la personne physique en cause est présente. Le ministère précise que des limitations, quant aux données visualisables et aux agents ayant accès à ces données, seront étudiées lors du développement de cet outil. Dans la mesure où cette application a, en l'état, pour seule fonctionnalité la visualisation des informations contenues dans les bases de données y étant adossées, sans stockage ni modification de ces informations, la CNIL constate qu'aucun traitement distinct n'est mis en œuvre.

En premier lieu, le traitement CFVR contient un grand nombre de données à caractère personnel. Dans le cadre de la refonte des applications métiers du ministère, la CNIL rappelle l'importance de la protection de la vie privée dès la conception et par défaut qui devra guider le développement de ces nouveaux outils. Elle accueille favorablement les mécanismes d'habilitation stricts mis en œuvre dans l'application PILOT CF , permettant de dissocier les envois des listes de programmation en fonction des missions des agents, et appelle le ministère à mettre en place des méthodes équivalentes pour les autres applications métiers.

En deuxième lieu, concernant les formalités relatives aux outils métiers développés par le ministère, la CNIL prend acte de ce qu'une AIPD est en cours de rédaction concernant l'application PILOT CF . En application du 2° du I de l'article 31 de la loi du 6 janvier 1978 modifiée, il revient également au ministère de prendre l'arrêté d'autorisation de ce traitement de données à caractère personnel après avis motivé et publié de la CNIL.

En dernier lieu, le ministère précise que les dossiers des personnes physiques ou morales présentant des risques fiscaux identifiés par le traitement CFVR seront, eu égard aux enjeux et aux seuils préalablement fixés, intégrés dans l'outil PILOT CF par le bureau SJCF-1D. La CNIL appelle à une grande prudence dans la conception et l'utilisation de ce type d'algorithmes, eu égard aux risques qu'ils comportent et aux biais qu'ils peuvent présenter (v. CNIL, SP, 16 novembre 2023, traitement dispositif ressources mensuelles , n° 2023-120). L'exemple du traitement algorithmique déployé aux Pays-Bas pour détecter des situations de fraude à certaines prestations sociales a montré que la confiance accordée par une administration à un traitement algorithmique de détection de la fraude, sans précautions et contrôles humains suffisants, pouvait avoir des conséquences graves pour les personnes. Ces risques, notamment de discriminations, sont régulièrement rappelés par le Défenseur des droits (v. notamment le rapport Algorithmes : prévenir l'automatisation des discriminations , 31 mai 2020). Elle rappelle, qu'en application des articles 22 du RGPD et 47 de la loi du 6 janvier 1978 modifiée, aucune décision produisant des effets juridiques à l'égard d'une personne ou l'affectant de manière significative ne peut être prise sur le seul fondement d'un traitement automatisé de données à caractère personnel, y compris le profilage.

La CNIL estime que le déploiement de tels algorithmes devrait s'accompagner :

- d'une part, de formations spécifiques permettant aux agents en charge de la programmation et des contrôles de maîtriser les principes des algorithmes utilisés ;

- d'autre part, d'une documentation couvrant également le risque de biais algorithmiques prohibés pouvant entraîner des discriminations. Pour ce faire, il revient au ministère de mettre en place un ensemble de mesures et de tests afin d'avoir un suivi continu des performances et des évolutions des algorithmes à des fins d'analyse proactive permettant de mettre à jour l'émergence de tels biais.

En outre, la CNIL estime que les dossiers considérés comme à risque par le traitement CFVR, mais par la suite écartés par les services de la programmation et des contrôles :

- ne devraient plus apparaitre, pour les mêmes raisons, dans les applications de ciblage de la fraude. Il revient à l'administration d'améliorer en continue les performances des traitements algorithmes de détection de la fraude afin de réduire le risque de faux positifs ;

- ne doivent pas comporter une mention selon laquelle ces dossiers ont déjà fait l'objet, par le passé, d'un ciblage par les algorithmes du traitement CFVR. D'une manière générale, le fait de déjà avoir été ciblé à tort par les algorithmes ne devrait pas constituer un indice augmentant la probabilité d'être une nouvelle fois considéré comme un dossier à risque par le traitement CFVR.

D. - Sur les droits des personnes concernées

L'article 4 du projet d'arrêté prévoit de modifier le fondement légal sur lesquels reposent les droits des personnes concernées, et ce, afin de prendre en compte le changement de régime juridique souhaité par le ministère.

En premier lieu, la CNIL remarque que, dans la mesure où le ministère n'est pas une juridiction financière, il ne peut se fonder sur le dernier alinéa de l'article 52 de la loi du 6 janvier 1978 modifiée pour restreindre les droits d'accès et de rectification. Elle prend acte de l'intention du ministère de corriger la base légale sur laquelle il se fonde pour restreindre les droits d'accès et de rectification.

En second lieu, la CNIL constate que l'arrêté ne contient aucune dérogation ou aménagement au droit à l'information. Si le ministère met en œuvre une politique d'information sur son site web, elle rappelle, qu'en application des articles 12 et suivants du RGPD, ces informations doivent être aisément accessibles pour toute personne, rédigées de manière intelligible, pédagogique et spécifique au traitement concerné. En conséquence, et compte tenu des enjeux importants du traitement CFVR en termes de protection des données à caractère personnel, la CNIL estime que la politique d'information du ministère pour ce traitement devra être complétée et être plus facilement accessible au grand public.

S'agissant de la finalité spécifique de la lutte contre la fraude, la CNIL rappelle qu'elle admet que l'information de la personne dont les données sont traitées puisse, dans certains cas, nuire aux finalités de détection et de redressement des cas de fraude. Elle estime cependant nécessaire de conjuguer l'information des personnes et l'efficacité de la lutte contre la fraude. A cette fin, elle recommande que la politique d'information soit mise en œuvre, a minima, en deux temps distincts :

- dans un premier temps, une information générale de l'ensemble des personnes concernées sur la possibilité d'utilisation de leurs données à des fins de lutte contre la fraude ;

- dans un second temps, une information spécifique des personnes effectivement contrôlées dès lors que cette information n'est plus susceptible de nuire à l'efficacité du contrôle, c'est-à-dire au plus tard lorsqu'en application des droits de la défense, il est procédé à un échange contradictoire avec la personne soupçonnée de fraude.

Elle invite donc le ministère à compléter le projet d'arrêté en ce sens.

E. - Sur la sécurité et la tenue d'un journal des opérations

En premier lieu, la CNIL prend acte de la mise en place d'une journalisation. Elle rappelle que le traitement de ces données a pour seule finalité la détection et la prévention d'opérations illégitimes sur les données du traitement. Si la mise en place de ces journaux et leur conservation sur trois années peuvent constituer des garanties fortes contre le détournement de finalités pour les personnes concernées par le traitement, la mise en œuvre d'un mécanisme proactif de contrôle automatique des données de journalisation, incluant la génération automatique d'alertes, est indispensable pour atteindre ce but.

En second lieu, la CNIL prend note que les modalités d'alimentation des applications GALAXIE et PILOT-CF sont satisfaisantes, les données étant mises à disposition sous forme de fichiers chiffrés avec des algorithmes et des procédures de gestion de clés, conformes à l'annexe B1 du référentiel général de sécurité (RGS), étant mises en œuvre.

La présidente,

M.-L. Denis

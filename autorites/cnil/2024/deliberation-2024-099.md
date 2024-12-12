# Délibération n° 2024-099 du 12 décembre 2024 portant avis sur un projet d'arrêté modifiant l'arrêté du 10 août 2016 autorisant la création d'un traitement automatisé de données à caractère personnel dénommé « DOCVERIF »

- Nature : Deliberation
- Type : Avis
- Numéro : 2024-099
- Date : 2024-12-12
- Publication : 2025-01-09
- NOR : CNIX2435158X
- État : VIGUEUR
- Légifrance : https://www.legifrance.gouv.fr/cnil/id/CNILTEXT000050959650

N° de demande d'avis : 24015335 |

Thématiques : lutte contre la fraude documentaire, identité numérique. |

Organisme(s) à l'origine de la saisine : ministère de l'intérieur |

Fondement de la saisine : article 31 de la loi informatique et libertés |

L'essentiel :

La CNIL a été saisie d'un projet d'arrêté modifiant le traitement DOCVERIF, lequel vise à renforcer l'efficacité de la lutte contre la fraude documentaire et l'usurpation d'identité en facilitant le contrôle de la validité des titres d'identité. Ce traitement a été récemment modifié pour permettre, à titre expérimental, la communication de données d'état civil à certains utilisateurs lorsque le titre est valide.

Le projet d'arrêté pérennise ce dispositif. Il ressort du compte rendu de l'expérimentation que le nombre de faux titres détectés sur un échantillon de faux titres avérés a augmenté. La CNIL invite cependant le ministère à continuer de mesurer l'efficacité du dispositif et à essayer de documenter l'existence d'éventuels faux positifs.

En outre, elle recommande d'étudier, dans quelques années, la possibilité de recourir à d'autres moyens, moins sensibles, permettant de repérer les titres falsifiés, s'agissant notamment de la nouvelle carte nationale d'identité électronique (CNIe).

Le projet d'arrêté étend le périmètre des utilisateurs de DOCVERIF aux établissements de paiement, de monnaie électronique, ainsi qu'aux sociétés d'assurance. A cet égard, la CNIL rappelle que la consultation des données de DOCVERIF doit être justifiée par un besoin opérationnel déterminé et proportionnée au regard des objectifs poursuivis.

La Commission nationale de l'informatique et des libertés,

Vu la loi n° 78-17 du 6 janvier 1978 modifiée relative à l'informatique, aux fichiers et aux libertés ( loi informatique et libertés ), et notamment son titre III ;

Après avoir entendu le rapport de Mme Sophie Lambremon, commissaire, et les observations de M. Damien Milic, commissaire du Gouvernement,

Adopte la délibération suivante :

I. - La saisine

A. - Le contexte

Autorisé par l'arrêté du 10 août 2016, DOCVERIF est un traitement qui vise à renforcer l'efficacité de la lutte contre la fraude documentaire et l'usurpation d'identité en facilitant le contrôle de la validité des titres d'identité émis par les autorités françaises (cartes nationales d'identité ou CNI , passeports et titres de séjour comportant un composant électronique).

Il peut être interrogé par les services de la police ou encore de la gendarmerie nationales (utilisateurs du cercle 1 ), ainsi que par les administrations publiques, les organismes chargés d'une mission de service public ou encore les établissements de crédit (utilisateurs du cercle 2 ). Le traitement permet à ces utilisateurs d'accéder à des données relatives au statut d'un document ( valide , invalide ou inconnu ).

Afin de renforcer la lutte contre la fraude, il a connu plusieurs évolutions pour étendre les périmètres des utilisateurs et des catégories de données qui peuvent être communiquées. A cet égard, l'arrêté du 28 avril 2022 a élargi, à titre expérimental, les catégories de données auxquelles les utilisateurs du cercle 1 peuvent avoir accès. Dans le cadre de cette expérimentation, il leur est ainsi permis d'accéder, jusqu'au 31 décembre 2024 et pour les CNI et passeports seulement, aux nom et premier prénom mentionnés sur le document, y compris lorsque le titre est valide (v. CNIL, SP, 7 avril 2022, avis sur projet d'arrêté, n° 2022-041, publié).

Pour assurer l'accès à ces informations, DOCVERIF est alimenté par une interconnexion avec deux autres traitements :

- pour les données relatives aux CNI et passeports, le traitement titres électroniques sécurisés (TES) ;

- pour les données relatives aux titres de séjour, l'application de gestion des dossiers des ressortissants étrangers en France (AGDREF).

B. - L'objet de la saisine

La CNIL a été saisie, par le ministère de l'intérieur, d'un projet d'arrêté modificatif du traitement DOCVERIF.

Ce projet prévoit deux évolutions :

- la pérennisation, pour les utilisateurs du cercle 1 , de la communication systématique, lorsque le titre vérifié est une CNI ou un passeport, des nom et premier prénom figurant sur le document et ce, y compris lorsque le titre est valide ;

- une extension du périmètre des utilisateurs du cercle 2 , par l'ajout des établissements de paiement, des établissements de monnaie électronique, ainsi que des sociétés d'assurance.

II. - L'avis de la CNIL

A. - Sur la pérennisation de l'expérimentation

L'expérimentation menée permet au cercle 1 , pour les CNI et passeports seulement, d'accéder aux nom et premier prénom mentionnés sur le document, y compris lorsque le titre est valide.

L'objectif de cette mesure est de lutter contre les fraudes liées à la présentation d'un titre comportant un numéro valide mais des éléments d'état civil falsifiés. Il peut s'agir, par exemple, de manipulations sur un titre volé ou trouvé. En effet, en l'absence de déclaration de perte ou de vol par son propriétaire légitime, un utilisateur de DOCVERIF est dans l'incapacité de détecter ce type de fraude s'il n'a pas d'information sur l'état civil. Le dispositif expérimenté vise à pallier ce manque.

Le dispositif porte faiblement atteinte à la vie privée puisque les seules données révélées sont le premier prénom et le nom de la personne porteuse du titre que, en principe, l'agent qui vérifie la validité du titre connaît déjà. Cependant, le système DOCVERIF conduit à collecter et rendre de nombreuses personnes destinataires de données issues de fichiers particulièrement sensibles (TES et AGDREF) : les liaisons informatiques ainsi réalisées nécessitent une forte sécurisation. En outre, le dispositif, pour fonctionner dans de bonnes conditions de sécurité, conduit à dupliquer les données des bases sources. Au regard de ces enjeux de sécurité et de minimisation, il convenait donc d'évaluer la nécessité du dispositif avant d'envisager sa pérennisation.

S'agissant de la durée d'expérimentation, il ressort des précisions apportées que la fonctionnalité liée au contrôle du nom et prénom a été mise en œuvre en avril 2023, et plus largement relayée auprès des forces de sécurité intérieures à travers des actions de communication à l'été 2023.

S'agissant des éléments justifiant la pérennisation du dispositif, une étude des résultats statistiques obtenus fait apparaître une amélioration du nombre de détection de faux documents par DOCVERIF, grâce à l'apport du nom et premier prénom.

En premier lieu, le bilan fait ressortir que le dispositif a permis d'améliorer le taux de détection de documents frauduleux sur un échantillon de documents déjà avérés comme falsifiés (s'agissant par exemple des échantillonnages réalisés par la direction générale de la gendarmerie nationale, le taux de titres frauduleux détectés passe de 80 à 96 %). Le dispositif permet donc de détecter les documents disposant d'un numéro de titre valide mais de données d'identité falsifiées.

La CNIL souligne cependant qu'une expérimentation menée dans des conditions différentes aurait pu permettre de documenter, notamment, l'existence ou non de faux positifs (c'est-à-dire de titres authentiques et valides mais détectés comme frauduleux), lesquels peuvent avoir des conséquences pour les personnes concernées. Elle recommande ainsi que la pérennisation du dispositif s'accompagne de nouvelles mesures pour quantifier son efficacité et, en particulier, documenter d'éventuels cas de faux positifs.

S'il s'avère qu'il y en a, il conviendra de déterminer les mesures pour permettre de les éviter et garantir aux personnes de pouvoir faire reconnaître au plus vite leur identité. A cet égard, la CNIL prend acte de l'engagement du ministère d'approfondir le suivi déjà effectué avec les forces de sécurité intérieures.

En second lieu, la lutte contre la fraude documentaire fait l'objet d'un ensemble de mesures destinées à contrer les différentes stratégies des fraudeurs. La CNIL rappelle qu'il convient de recourir aux moyens présentant les risques les plus faibles possibles pour atteindre la finalité poursuivie de lutte contre la fraude. S'agissant de la proportionnalité du dispositif, elle avait ainsi considéré que l'objectif devait être, qu'à terme, la vérification des titres d'identité puisse être réalisée en s'assurant directement que le titre n'est pas physiquement falsifié (v. CNIL, SP, 7 avril 2022, n° 2022-041, précité).

Interrogé sur la possibilité de faire reposer sur le cachet électronique visible (CEV) la vérification de conformité des nom et premier prénom présents sur la nouvelle carte nationale d'identité électronique (CNIe), le ministère a indiqué que le nombre de titres actuellement en circulation disposant du CEV était évalué à 21 millions, contre 39 millions de CNI sur lesquelles cet élément ne figure pas. Le ministère a par ailleurs précisé, qu'au plus tard à l'échéance de 2036, les CNI ne disposant pas du CEV ne seront plus valides.

Les CEV, qui comportent les nom et premier prénom figurant sur le titre d'identité - entre autres informations, respectent le format 2D-DOC, un format ouvert et facilement lisible par des applications dites de lecture de QR code . Les CEV comportent aussi une signature électronique de l'émetteur du titre pour permettre de vérifier leur authenticité. La vérification de la signature du CEV, et donc in fine de l'authenticité des données figurant sur le titre d'identité, serait par conséquent possible sans avoir recours à DOCVERIF par les utilisateurs actuels du service. Les requêtes à DOCVERIF demeureraient en revanche nécessaires en ce qui concerne le statut (invalide, perdu ou volé) du titre.

Il deviendrait alors possible, concernant les informations figurant dans la base de données de DOCVERIF, de procéder à une minimisation de celles-ci en ne conservant que celles nécessaires à la détermination du statut - invalide, perdu ou volé. A l'heure actuelle, le CEV ne figure que sur les CNIe et non sur les anciennes cartes d'identité, les passeports et les titres de séjour. Une telle minimisation ne pourrait donc se faire que pour les CNIe. La CNIL encourage le ministère à préparer, sur le long terme, une minimisation des données relatives aux CNIe figurant dans la base de données DOCVERIF.

De surcroît, si un CEV venait à être ajouté, à l'avenir, sur les autres types de titres (passeports et titres de séjour), l'authenticité des informations pourrait alors aussi être vérifiée au moyen de cette méthode, plus respectueuse de la vie privée des personnes et comportant de moindres risques de sécurité en comparaison de requêtes auprès de serveurs distants.

Dès lors, la CNIL invite le ministère à procéder, dans quelques années, à une nouvelle réflexion sur la conception d'un dispositif qui permette de minimiser les données de la base DOCVERIF.

B. - Sur le périmètre des nouveaux utilisateurs du cercle 2

En premier lieu, la mention du caractère valide ou non du document ainsi que, uniquement pour les CNI et les passeports, le résultat de la comparaison des nom et prénom saisis (par exemple nom et premier prénom conformes ) sont accessibles aux utilisateurs du cercle 2 . Il s'agit, actuellement :

- des administrations publiques ;

- des agents de police municipale et des gardes champêtres ;

- des organismes chargés d'une mission de service public ;

- des établissements de crédit et des sociétés de financement mentionnées à l'article L. 511-1 du code monétaire et financier ;

- des fournisseurs de moyen d'identification électronique ;

- des agents mentionnés au I de l'article 3 du décret n° 2022-676 du 26 avril 2022 relatif au service de garantie de l'identité numérique (SGIN).

L'analyse d'impact relative à la protection des données (AIPD) transmise révèle que de nouveaux utilisateurs ont été ajoutés au titre des administrations publiques et des organismes chargés d'une mission de service public . La CNIL considère que, pour assurer l'information et garantir l'effectivité des droits des personnes, la liste des utilisateurs devrait être détaillée, a minima sur le site web du ministère.

En deuxième lieu, le projet d'arrêté élargit le périmètre du cercle 2 à trois nouvelles catégories d'utilisateurs :

- les établissements de paiement ;

- les établissements de monnaie électronique ;

- les sociétés d'assurance.

Le ministère justifie ces ajouts par le fait que ces acteurs sont soumis, en application du code monétaire et financier, aux obligations relatives à la lutte contre le blanchiment des capitaux et le financement du terrorisme. Le contrôle de validité des titres au moyen du traitement DOCVERIF devrait donc permettre d'améliorer l'efficacité du dispositif de vérification d'identité des clients avant l'établissement de la relation d'affaires (v. art. L. 561-2 du code monétaire et financier).

S'agissant précisément des sociétés d'assurance, l'utilisation de DOCVERIF devrait permettre, par ailleurs, de lutter contre la fraude à l'assurance en permettant de détecter la fraude documentaire. Il ressort des précisions apportées par le ministère, pour justifier cet accès conféré aux sociétés d'assurance, que :

- le volume des cas de fraude à l'assurance est significatif et les préjudices financiers qui en découlent peuvent être importants pour les assurés vertueux ;

- certaines fraudes à l'assurance concernent de faux sinistres déclarés sous de multiples identités.

La CNIL considère que l'utilisation de DOCVERIF doit être strictement limitée aux objectifs poursuivis en matière de détection de fraude documentaire, dans la perspective de la lutte contre le blanchiment des capitaux et le financement du terrorisme. Elle invite le ministère à encadrer cette consultation par l'ajout, dans la convention conclue entre les utilisateurs et le responsable de traitement, de garanties spécifiques liées aux modalités d'accès afin de restreindre sa consultation aux seuls services compétents au sein des sociétés d'assurance.

En outre, la CNIL réitère sa recommandation de compléter les conventions afin d'inciter les organismes à informer les personnes concernées du fait qu'ils sont susceptibles de réaliser une interrogation de DOCVERIF (v. CNIL, SP, 7 avril 2022, n° 2022-041, précité).

C. - Sur le principe de protection des données par conception et par défaut

a. Sur les informations statistiques utilisées à des fins d'amélioration du service

Des statistiques d'utilisation globale du service (taux d'erreur, faux négatifs, comparaison avec la volumétrie globale des requêtes, etc.) permettrait une meilleure appréciation de la pertinence d'utilisation de ce service par les utilisateurs, notamment du cercle 2 . La CNIL invite le ministère à mettre en place des dispositifs permettant d'agréger de tels indicateurs et respectant la vie privée des personnes.

b. Sur l'accès à la fonctionnalité de vérification de la conformité du nom et du prénom par les utilisateurs du cercle 2

Concernant les utilisateurs du cercle 2 , ceux-ci saisissent, par exemple, les nom et prénom inscrits sur le titre présenté (CNIe ou passeport) et DOCVERIF répond à la requête de concordance par la négative ou l'affirmative sans avoir besoin d'effectuer la comparaison avec les nom et prénom eux-mêmes (qui ne sont pas conservés dans la base de données du cercle 2 ) mais en s'appuyant sur un haché de ceux-ci. La CNIL considère que les données enregistrées dans la base de données des informations du cercle 2 sont donc minimisées, les noms et prénoms des personnes n'apparaissant pas en clair dans la base de données du cercle 2 et la vérification de conformité reposant sur la comparaison de hachés obtenus à partir du numéro du titre, du type de titre, du nom et du premier prénom figurant sur le titre après saisie complémentaire de la date de délivrance inscrite sur le titre.

La CNIL considère également que le risque de mauvaise saisie des nom et premier prénom des personnes concernées, pouvant entraîner une réponse signalant la non-conformité du document, a été pris en compte. En effet, les informations de l'état civil sont traitées sous une forme dite normalisée, c'est-à-dire une forme simplifiée pour éviter les erreurs (par exemple, les accents peuvent être automatiquement enlevés des lettres qui en comportent ou bien toutes les lettres transformées en minuscules). La comparaison des hachés issus de ces informations a donc moins de chances de signaler comme différentes ces informations alors que l'écart ne proviendrait que d'une différence de forme (par exemple l'accentuation ou la casse).

En revanche, l'AIPD indique que la vérification de conformité du nom et du premier prénom des personnes concernées est une fonctionnalité optionnelle. Or il ressort des précisions apportées par le ministère que cette fonctionnalité est en réalité disponible par défaut et qu'il revient aux utilisateurs du cercle 2 de l'activer ou non en fonction de leur besoin, du contexte d'usage et des capacités de leur propre système d'information. La CNIL encourage le ministère à revoir l'AIPD pour lever cette ambigüité.

D. - Sur les transferts

La CNIL relève que lors de la précédente saisine ayant donné lieu à la délibération n° 2022-041 (précitée), il a été constaté que la convention type d'utilisation de DOCVERIF ne comportait pas d'interdiction de tout transfert de données hors de l'Union européenne. Elle demandait notamment que la convention type soit modifiée pour que soit mentionnée explicitement l'interdiction des transferts de données vers des Etats n'appartenant pas à l'Union Européenne.

Dans l'avis du délégué ministériel à la protection des données personnelles, il est indiqué que les sous-traitants ultérieurs sont susceptibles de procéder à des transferts de données hors de l'Union Européenne, ou de recourir eux-mêmes à des sous-traitants soumis à un droit extraterritorial clair . Par ailleurs, ce même avis indique que le délégué ministériel à la protection des données personnelles n'a pas reçu ladite convention dans les documents fournis pour son analyse.

La CNIL rappelle que les transferts de données vers des Etats n'appartenant pas à l'Union européenne ne pourront être opérés que sous réserve du respect des conditions énoncées à l'article 112 de la loi informatique et libertés . Le cas échéant, il conviendra notamment que des garanties appropriées en matière de protection des données à caractère personnel soient fournies par un instrument juridiquement contraignant. En l'absence de décision d'adéquation adoptée par la Commission européenne ou de garanties équivalentes, et par dérogation à l'article 112 précité, de tels transferts ne pourront être réalisés que sous réserve de respecter les conditions énoncées à l'article 113 de la loi informatique et libertés .

La CNIL réitère sa demande au ministère de faire figurer dans la convention type une interdiction explicite des transferts de données et que cette convention soit soumise pour analyse au délégué ministériel à la protection des données personnelles. Ceci est particulièrement important dans le cadre d'un traitement régalien comportant les données d'identité de la quasi-totalité de la population française et des résidents titulaires d'un droit au séjour.

E. - Sur la sécurité

a. Sur le renouvellement des clefs de chiffrement

La CNIL relève que, lors de la précédente saisine, le plan d'action pour améliorer le service DOCVERIF évoquait l'exploration de la possibilité de procéder au renouvellement des clefs de chiffrement utilisées dans l'infrastructure.

Le plan d'action disponible dans la présente AIPD indique un abandon de cette amélioration. Le ministère a précisé que les coûts que représenterait une implémentation de mise à jour des clefs de chiffrement dans l'infrastructure de DOCVERIF, associés aux risques de dysfonctionnement que cela pourrait occasionner lors d'une telle opération, ont été jugés, en lien avec les responsables de la sécurité des systèmes d'information de France Titres, trop élevés au regard des bénéfices attendus. La CNIL invite le ministère à documenter cette décision dans l'AIPD pour sa bonne traçabilité.

La CNIL comprend les enjeux financiers d'une telle mise à jour, mais encourage le ministère à s'aligner sur le Référentiel Général de Sécurité version 2.0 maintenu par l'ANSSI, et en particulier ses annexes B1 et B2. En effet, le référentiel couvre la problématique de la durée de vie maximale de clefs de chiffrement (crypto-période) et, de fait, la mise en place d'un système de renouvellement des clefs de chiffrement est encouragée, particulièrement dans un contexte où les durées de vie des clefs s'amenuisent avec le temps.

b. Sur le contrôle des accès logiques

Le ministère indique que le système d'authentification au service DOCVERIF pour les utilisateurs ne disposant pas de carte agent est mis en œuvre par les utilisateurs dont ils dépendent, en particulier pour le cercle 2 .

Si ce choix est compréhensible, la CNIL encourage le ministère, en tant que responsable du traitement, à systématiser l'accompagnement dans l'intégration du service DOCVERIF aux systèmes d'information des utilisateurs en étant particulièrement vigilant sur le fait qu'une authentification multifacteur pour accéder au service doit être encouragée, ainsi qu'une gestion stricte des habilitations au sein de l'organisme utilisateur couplée à une traçabilité individuelle des accès conforme aux recommandations de la CNIL sur ce sujet (délibération n° 2021-122 du 14 octobre 2021 portant adoption d'une recommandation relative à la journalisation).

c. Sur le chiffrement des flux réseau

La CNIL prend acte de l'engagement du ministère d'intégrer dans son plan d'action un passage à la version TLS 1.3, a minima au niveau des interfaces à destination des utilisateurs du cercle 2 accessibles depuis un réseau externe à celui géré par le ministère - la version 1.2 étant sujette à des vulnérabilités. Dans l'attente de cette mise en œuvre, la CNIL attire l'attention du ministère sur l'importance d'assurer le respect des conditions précisées dans les recommandations de sécurité relatives à TLS (version 1.2 du 26 mars 2020) de l'ANSSI pour permettre de considérer l'usage de TLS 1.2 comme sûr ou de mettre en place des contre-mesures adéquates en les documentant dans l'AIPD.

d. Sur le résultat des audits techniques

La CNIL observe que des audits ont été effectués dans le cadre de l'homologation du dispositif, qui est requise tous les trois ans ou lors d'une évolution majeure par la politique de sécurité des systèmes d'information du ministère. Le ministère souligne que la correction des principaux écarts a été effectuée mais il n'a pour l'heure pas communiqué la liste des évolutions effectuées.

La mise en œuvre des corrections nécessaires pour pallier tout écart au moins important est considérée comme indispensable par la CNIL.

F. - Sur l'analyse d'impact relative à la protection des données

La CNIL observe que l'AIPD et notamment la section 3, qui propose une synthèse des sections précédentes (1 et 2), présente des incohérences au niveau des évaluations (code couleur) comme de leurs descriptions détaillées telles que décrites dans les sections 1 et 2 du document.

Par ailleurs, la CNIL observe des évolutions dans le tableau de description et évaluation des mesures contribuant à traiter les risques liés à la sécurité des données n'ayant pas été documentées ou justifiées, en particulier les items chiffrement et cloisonnement des données passés du statut de améliorable à acceptable .

Enfin, les durées de conservation des données de titres devraient être corrigées pour les titres de séjour Brexit dont la durée de conservation est indiquée comme étant de 1 à 5 ans ou permanente (la CNIL n'ayant pas connaissance de tels titres ayant une durée de validité permanente).

La CNIL demande au ministère de mettre à jour l'AIPD en conséquence.

La présidente,

M.-L. Denis

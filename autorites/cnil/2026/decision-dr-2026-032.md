# Décision DR-2026-032 du 25 février 2026 autorisant le CENTRE HOSPITALIER UNIVERSITAIRE D’ANGERS à mettre en œuvre un traitement de données ayant pour finalité une étude portant sur le développement de modèles d’aide à la détection de deux maladies rares, intitulée « PAI ». (Demande d’autorisation n° 925250)

- Nature : Decision
- Type : Autorisation de recherche
- Numéro : DR-2026-032
- Date : 2026-02-25
- Publication : 2026-03-14
- État : VIGUEUR
- Légifrance : https://www.legifrance.gouv.fr/cnil/id/CNILTEXT000053668617

Décision DR-

2026

-032 du 25 février 2026 autorisant le

centre hospitalier universitaire d’Angers

à mettre en œuvre un traitement de données ayant pour finalité une étude portant sur le développement de modèles d’aide à la détection de deux maladies rares, intitulée "PAI". (Demande d’autorisation n° 925250)

La Commission nationale de l’informatique et des libertés,

Vu le règlement (UE) 2016/679 du Parlement européen et du Conseil du 27 avril 2016, relatif à la protection des personnes physiques à l'égard du traitement des données à caractère personnel et à la libre circulation de ces données ;

Vu la loi n° 78-17 du 6 janvier 1978 relative à l'informatique, aux fichiers et aux libertés ;

Vu le décret n° 2019-536 du 29 mai 2019 pris pour l'application de la loi n° 78-17 du 6 janvier 1978 relative à l'informatique, aux fichiers et aux libertés ;

Vu la décision du 2 juin 2025 portant délégation de signature du secrétaire général de la Commission nationale de l’informatique et des libertés ;

Saisie d’une demande d’autorisation relative à un traitement de données à caractère personnel à des fins de recherche, d'étude ou d'évaluation dans le domaine de la santé ;

Considérant que ce traitement, dont la finalité présente un caractère d’intérêt public, relève des dispositions de la section 3 du chapitre III du titre II de la loi du 6 janvier 1978 modifiée ;

Considérant que le traitement présente les caractéristiques et répond aux conditions suivantes :

Avis du comité

|

Avis favorable du Comité éthique et scientifique pour les recherches, les études et les évaluations dans le domaine de la santé du 2 octobre 2025.

|

Observations liminaires sur le déploiement de la plateforme "Ouest Data Hub" et la responsabilité de traitement

|

Chaque établissement du Groupement de coopération sanitaire des Hôpitaux universitaires du Grand Ouest (GCS HUGO) a développé un entrepôt de données de santé (EDS) à partir d’une plateforme technique identique : le système eHOP ("entrepôt-Hôpital").

Le GCS HUGO s’est doté d’une plateforme technique pour le traitement des données massives en santé, dénommée plateforme "Ouest Data Hub" (ODH). Il est responsable de l’intégration des données sur la plateforme technique, de la pseudonymisation des données de la base projet (deuxième pseudonymisation), de la création de la base projet, de la gestion des comptes utilisateurs projet, de l’attribution des droits sur la base projet, du suivi des traces d’activité des gestionnaires HUGO et des utilisateurs sur l’espace projet.

Dans le cadre du déploiement de la plateforme ODH, le CHU de Nantes :

est responsable de l’hébergement des données et de l’exploitation technique de la plateforme ;

met à disposition un espace projet dédié, des outils de gestion des comptes et de gestion des traces d’activité sur la plateforme ;

est responsable de la gestion des comptes gestionnaires.

|

Points de non-conformité à la méthodologie de référence concernée

|

Le dossier de demande mentionne que le traitement envisagé est conforme aux dispositions de la méthodologie de référence MR-004, à l'exception de :

la nature des données traitées (traitement du NIR à des fins d’appariement entre plusieurs entrepôts de données de santé, date de naissance pour la recherche du statut vital) ;

des destinataires des données directement identifiantes (recherche du statut vital) ;

des modalités d’information de certaines personnes concernées.

En dehors de ces points, qui font l’objet d’un examen spécifique dans la présente décision, ce traitement devra respecter le cadre prévu par ce référentiel.

|

Finalité et principe de minimisation (méthodologie de la recherche)

|

L’étude porte sur le développement de modèles d’aide à la détection précoce de deux maladies rares (angiodème bradykinique héréditaire et pseudoxanthome élastique).

Pour atteindre cet objectif, cette étude portera sur les données des patients, âgées de 5 à 65 ans, pris en charge :

entre 2010 et 2023 ;

par les centres hospitaliers universitaires (CHU) d’Angers, de Brest, de Nantes, de Rennes et de Tours ;

au sein des services des urgences, de dermatologie, de médecine vasculaire, d’ophtalmologie, de réanimation, d’urologie, de pédiatrie et de médecine interne.

Seuls les patients dont le dossier médical comporte au moins cinq documents seront concernés afin de trouver un équilibre entre l’exploitabilité des données et la diversité dans la volumétrie des dossiers médicaux. Une analyse sera réalisée sur ces documents afin de rechercher des patients potentiellement atteints par une des maladies rares étudiées. Cette analyse consistera dans la détection de mots-clés caractéristiques des symptômes de ces maladies et de signes d'errance médicale qui caractérisent le diagnostic des maladies rares (en particulier, admission dans au moins quatre des services précités).

Le nombre total de personnes concernées par cette étude s’explique par la nécessité de disposer d’un nombre suffisant de patients témoins afin d’entraîner les modèles à détecter des signaux faibles dans une population. Des techniques de sous-échantillonnage de la classe sur-représentée et des techniques d'augmentation de la classe sous-représentée de patients atteints d'une maladie rare sont prévues. L’impact de la réduction progressive du nombre de patients négatifs sera documenté pour évaluer la possibilité de minimiser autant que possible le recours à des données à caractère personnel pour l’entraînement des modèles.

Ces critères d’inclusion permettent une minimisation des données traitées dans le cadre de cette étude conforme au c) du 1 de l’article 5 du RGPD.

Dans un premier temps, le développement des modèles sera réalisé à partir des données de l’entrepôt "EHOP Angers".

Dans un second temps, ces modèles seront validés à partir des données issues des entrepôts "EHOP Rennes", "EHOP Tours", "EHOP Nantes", "EHOP Brest".

|

Réutilisation des données de bases existantes

|

Seront réutilisées les données issues de :

l’entrepôt "EHOP Angers" mis en œuvre par le CHU d’Angers (demande d’autorisation n°2215237) ;

l’entrepôt "EHOP Nantes" mis en œuvre par le CHU de Nantes (demande d’autorisation n°2129203) ;

l’entrepôt "EHOP Brest" mis en œuvre par le CHU de Brest (demande d’autorisation n°2217775) ;

l’entrepôt "EHOP Tours" mis en œuvre par le CHU de Tours (demande d’autorisation n°2212853) ;

l’entrepôt "EHOP Rennes" mis en œuvre par le CHU de Rennes (demande d’autorisation n°2212496).

|

Destinataires des données directement identifiantes

|

Le statut vital des participants à l’étude sera recherché partir de leurs données nominatives (nom, prénom), leur date de naissance, leur sexe et leur commune de naissance grâce aux données publiques de mortalité disponibles sur le site web de l’Institut national de la statistique et des études économiques (fichier des personnes décédées). Cet appariement sera réalisé par le personnel habilité de chaque responsable des entrepôts de données réutilisés.

|

Circuit d’appariement

|

Pour les participants à l’étude ayant été pris en charge dans plusieurs CHU, les données issues des entrepôts feront l’objet d’un rapprochement par l’utilisation du numéro d’inscription au répertoire national d’identification des personnes physiques (NIR), du sexe et de la date de naissance complète des participants.

Afin d’assurer la pseudonymisation et le chaînage des données du projet, un traitement du NIR est réalisé localement dans chaque établissement, par application d’une fonction de hachage à clé secrète à l’aide d’un logiciel "boîte noire" disposant des secrets spécifiques au projet. Il est traité au sein de la DSI de chaque établissement par une personne en charge de la gestion de l’application administrative du système d’information de l’établissement, soumise au secret professionnel, dans un environnement sécurisé. Cette personne est habilitée à y accéder, dans le cadre de ses missions ; elle sera la seule à accéder à cette donnée pour le projet et ses actions seront tracées.

Les données identifiantes et le NIR sont manipulés dans des fichiers temporaires qui ne portent pas le nom de l’étude, sont stockés dans un espace d’accès restreint et sont effacés dès qu’ils ne sont plus utiles. Le NIR n’est pas exporté et le pseudonyme issu de son traitement fait l’objet d’une deuxième pseudonymisation lors de sa réception sur la plateforme ODH.

|

Information et droits des personnes

|

S’agissant des personnes prises en charge après la constitution des entrepôts de données de santé :

Les personnes concernées ont reçu un premier niveau d’information individuelle les renvoyant vers un dispositif spécifique d’information (portail de transparence) auquel elles peuvent se reporter préalablement à la mise en œuvre de chaque nouveau traitement de données procédant à la réutilisation des données des entrepôts concernés. Une note d’information relative à la présente étude sera diffusée sur le portail de transparence de chaque entrepôt accessible via le site web de leur responsable de traitement.

S’agissant des personnes prises en charge avant la constitution des entrepôts de données de santé :

En application de l'article 69 de la loi "informatique et libertés" et du b) du 5 de l’article 14 du RGPD, l'obligation d'information individuelle de la personne concernée peut faire l'objet d'exceptions, notamment dans l'hypothèse où la fourniture d'une telle information exigerait des efforts disproportionnés. En pareils cas, le responsable de traitement prend des mesures appropriées pour protéger les droits et libertés, ainsi que les intérêts légitimes de la personne concernée, y compris en rendant les informations publiquement disponibles.

En l'espèce, il sera fait exception au principe d'information individuelle des personnes et des mesures appropriées seront mises en œuvre, notamment par la diffusion d’une information relative à l’étude sur le site web :

du responsable de traitement ;

des CHU de Nantes, de Brest, de Tours et de Rennes ;

de la plateforme ODH.

Ces notes d’information devront être complétées avant le commencement de l’étude afin de comporter l’ensemble des mentions prévues par le RGPD.

|

Mesures de sécurité

|

Une analyse d’impact relative à la protection des données spécifique au projet "PAI" a été réalisée et fournie à l’appui du dossier. Celle-ci intègre également les éléments liés à la solution technique de la plateforme "ODH".

Les utilisateurs se connecteront à la plateforme ODH à l’aide d’un certificat et d’un mot de passe ; l’authentification multifacteurs pour l’accès aux espaces projet a été mise en place. Les traces seront centralisées dans un système mis à disposition par l’hébergeur. Un mécanisme proactif de contrôle automatique des données de journalisation contribuant à la sécurité du traitement par la génération automatique d’alertes a été mis en place.

Les exports de données depuis l’espace projet ne pourront être constitués que de données anonymes. À cet égard, le responsable de traitement doit réaliser une analyse permettant de démontrer que ses processus d’anonymisation respectent les trois critères définis par l’avis n°05/2014 sur les techniques d’anonymisation adoptés par le groupe de l’Article 29 (G29) le 10 avril 2014. À défaut de remplir parfaitement ces trois critères, le responsable de traitement doit démontrer, via une évaluation approfondie, que le risque d’identification d'une personne à l'aide de moyens raisonnablement susceptibles d'être utilisés, par lui-même ou par toute autre personne, est négligeable.

Les mesures de sécurité décrites dans le dossier de demande ont pour objectif de répondre aux exigences prévues par le f) du 1 de l’article 5 et l’article 32 du RGPD. Cette obligation nécessite la mise à jour de l’AIPD et de ses mesures de sécurité au regard de la réévaluation régulière des risques.

|

Durées de conservation en base active et en archivage

|

Les données administratives d’identification (nom, prénom, date et commune de naissance) ne seront pas conservées après la recherche du statut vital.

Les NIR et la date de naissance complète des participants ne seront pas conservés après l’appariement.

|

Transparence du traitement

|

Ce traitement devra être enregistré dans le répertoire public mis à disposition par la Plateforme des données de santé.

|

AUTORISE le

centre hospitalier universitaire d’Angers à mettre en œuvre le traitement décrit ci-dessus.

Le Directeur de l’accompagnement juridique

Thomas DAUTIEU

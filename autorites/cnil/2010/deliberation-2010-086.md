# Délibération n°2010-086 du 25 mars 2010 autorisant la mise en œuvre par la Caisse nationale des allocations familiales (CNAF) d’un traitement de données à caractère personnel ayant pour finalité l’amélioration du ciblage des comptes allocataires à contrôler par les Caisses d’allocations familiales (CAF)

- Nature : Deliberation
- Type : Autre autorisation
- Numéro : 2010-086
- Date : 2010-03-25
- Publication : 2019-11-13
- État : VIGUEUR
- Légifrance : https://www.legifrance.gouv.fr/cnil/id/CNILTEXT000022205702

La Commission nationale de l’informatique et des libertés,

Vu la Convention n° 108 du Conseil de l’Europe pour la protection des personnes à l’égard du traitement automatisé des données à caractère personnel ;

Vu la directive 95/46/CE du Parlement européen et du Conseil du 24 octobre 1995 relative à la protection des personnes physiques à l’égard du traitement de données à caractère personnel et à la libre circulation de ces données ;

Vu le Code de la sécurité sociale et, notamment, ses articles L. 114-9 à L. 114-21 ;

Vu la loi n° 78-17 du 6 janvier 1978 relative à l'informatique, aux fichiers et aux libertés, modifiée en 2004 et notamment les articles 8-IV et 25-I-3°;

Vu le décret n° 2005-1309 du 20 octobre 2005 pris pour l’application de la loi n° 78-17 du 6 janvier 1978 relative à l’informatique, aux fichiers et aux libertés, modifié par le décret n°2007-451 du 25 mars 2007 ;

Après avoir entendu, M. Philippe GOSSELIN, commissaire en son rapport et Mme Elisabeth ROLIN, commissaire du Gouvernement, en ses observations.

Formule les observations suivantes :

La Commission nationale de l’informatique des libertés a été saisie par la Caisse nationale des allocations familiales (CNAF) d’un traitement de données à caractère personnel ayant pour finalité l’amélioration du ciblage des comptes allocataires à contrôler par les Caisses d’allocations familiales (CAF).

Ce traitement relève du régime de l’autorisation prévu à l’article 25-I-3° de la loi du 6 janvier 1978 modifiée, applicable aux traitements portant sur des données relatives aux infractions, condamnations ou mesures de sûreté.

Sur les finalités poursuivies par le traitement

Ce traitement (« datamining ») s’inscrit dans le cadre de la lutte contre la fraude. Il a pour objectif d’améliorer le ciblage des dossiers allocataires à contrôler sans modifier la procédure de contrôle vis-à-vis de l’usager. A cet effet, il crée un outil permettant de détecter dans les dossiers des allocataires les corrélations existantes entre les dossiers à risque (comportements types des fraudeurs). Le logiciel de « datamining » croise les données pour découvrir des liens entre les dossiers de fraude.

La mise en place de cet outil comporte plusieurs étapes :

la première étape consiste à réaliser un modèle statistique de détection des fraudes en utilisant la base de données anonymisées gérée par la CNAF « Allnat ». L’outil de « datamining » analyse ces données et détermine les profils de dossiers présentant des risques de fraude ;

la seconde étape a pour objet de déployer dans l’ensemble des Caisses d’allocations familiales (CAF) cet outil pour réaliser des requêtes ;

la troisième étape consiste à appliquer le modèle aux bases de données locales de chaque CAF pour cibler les dossiers à contrôler en fonction d’un score de risque. L’attribution de ce score à chaque dossier varie en fonction de son degré de similitude avec le modèle. Les dossiers présentant les plus forts risques de fraude sont proposés, en priorité, pour un contrôle selon la procédure habituelle.

A l’issue des contrôles effectués par les agents habilités de la caisse concernée, un code particulier dénommé « suspicion de fraude »est inséré dans les dossiers des allocataires pour lesquels une fraude est suspectée.

Si la fraude est retenue, un code fraude est inséré dans l’application de gestion des prestations familiales et de l’action sociale (CRISTAL). Les fraudes sont classées en quatre catégories : les actes d’omission et de fausse déclaration (code 641), les fraudes à l’isolement (code 642) qui sont propres aux prestations pour parents isolés, les faux et usage de faux (code 643) et les escroqueries (code 644).

Conformément à l’article 10 de la loi du 6 janvier 1978, le résultat ne peut avoir, en toute hypothèse, qu’un caractère indicatif. Le dossier est en effet soumis à une commission administrative « fraude » qui propose soit de ne pas retenir la fraude, soit de la retenir avec diverses options : la fraude pourra être retenue sans pénalité mais avec envoi d’une lettre d’avertissement, ou avec signalement au parquet, ou avec application des pénalités, ou suspension de l’aide au logement, enfin le cas échéant, avec dépôt de plainte.

Si la fraude n’est pas retenue par le directeur, il y a effacement sans délai du code suspicion dans la base précitée CRISTAL.

Les cas de fraudes font ensuite l’objet d’une anonymisation avant de figurer dans la base de données statistiques « Allnat » servant à la création des modèles de « datamining ».

Sur les catégories de données traitées

Les données traitées pour élaborer l’outil de « datamining » concernent les données administratives relatives aux dossiers des allocataires : la situation de famille (âge, statut du NIR : certifié ou non, présence d’un conjoint, code nationalité : française, union européenne ou hors union européenne), nature éventuelle de la tutelle, données relatives à la gestion du dossier, aux enfants ou personnes à charge, à l’activité professionnelle, aux ressources, aux prestations versées, au logement, aux contacts avec l’allocataire, aux contrôles des dossiers, aux indus, aux rappels et à la fraude (sanctions, types de fraude, préjudice). Ces données ne sont pas identifiantes.

Les catégories de données relatives aux fraudes sont issues de CORALI et celles relatives aux indus proviennent de CRISTAL et sont utilisées pour la modélisation des profils des fraudeurs.

Un code fraude (fausse déclaration, faux et usage de faux, escroquerie) sera affecté à chaque dossier qualifié comme tel. Ce code sera supprimé, sans délai, si la fraude n’est pas retenue

Les données statistiques figurant dans la base de données « Allnat »sont réactualisées chaque mois en fonction de la vie du dossier allocataire.

Chaque année, l’outil « datamining » mettra à jour les profils en utilisant les données de la base Allnat des seuls douze derniers mois.

Sur les catégories de destinataires

Le directeur de la CNAF habilite, selon leurs compétences, les agents chargés de créer les profils types et d’élaborer les modèles ainsi que les requêtes à partir de la base de données nationale anonymisée de la CNAF.

Les habilitations données aux agents pour l’accès aux bases de données CRISTAL et CORALI demeurent inchangées.

Sur l’information des personnes concernées

La CNAF diffuse une information générale sur la création du processus de « datamining » sur son site.

L’allocataire faisant l’objet d’un contrôle est informé, dans les mêmes conditions que pour les autres contrôles de lutte contre la fraude de la procédure encours, des voies de recours et des droits qui lui sont ouverts au titre de la loi du 6 janvier 1978.

Sur les mesures de sécurité mises en œuvre

Tous les accès à la base sont tracés avec notamment l’enregistrement des types d’accès (consultation, création, modification).

Les accès aux bases de données anonymisées se font sur un réseau intranet sécurisé.

Les données sont susceptibles d’être stockées chez un prestataire, dès lors la Commission recommande de mettre en place un chiffrement de la base afin que les administrateurs ne puissent accéder à celle-ci en clair.

Dans ces conditions, la Commission autorise la Caisse nationale des allocations familiales à mettre en œuvre le traitement de données à caractère personnel présenté.

Le Président

Alex TURK

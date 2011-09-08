# Délibération n° 2011 -246 du 8 septembre 2011 autorisant la mise en œuvre par la société CELTIPharm d’un traitement de données à caractère personnel ayant pour finalité la réalisation d’études épidémiologiques à partir de données issues des feuilles de soins électroniques anonymisées à bref délai

- Nature : Deliberation
- Type : Autre autorisation
- Numéro : 2011-246
- Date : 2011-09-08
- Publication : 2019-11-13
- État : VIGUEUR
- Légifrance : https://www.legifrance.gouv.fr/cnil/id/CNILTEXT000024667731

La Commission nationale de l'informatique et des libertés,

Vu la Convention n° 108 du Conseil de l'Europe pour la protection des personnes à l'égard du traitement automatisé des données à caractère personnel ;

Vu la directive 95/46/CE du Parlement européen et du Conseil du 24 octobre 1995 relative à la protection des personnes physiques à l'égard du traitement de données à caractère personnel et à la libre circulation de ces données ;

Vu le code de la santé publique et notamment ses articles L. 6316-1, L. 1110-4 et L. 1111-8 ;

Vu la loi n° 78-17 du 6 janvier 1978 relative à l'informatique, aux fichiers et aux libertés, modifiée en 2004, et notamment ses articles 8-III et 25-I, 1°;

Vu le décret n° 2005-1309 du 20 octobre 2005 pris pour l'application de la loi n° 78-17 du 6 janvier 1978 relative à l'informatique, aux fichiers et aux libertés, modifié en 2007 ;

Sur le rapport de M. Jean MASSOT, commissaire, et les observations de Mme Elisabeth ROLIN, commissaire du gouvernement ;

Autorise, dans les conditions définies dans le dossier et ses compléments, la société CELTIPharm à mettre en œuvre un traitement ayant pour finalité la réalisation d'études épidémiologiques à partir de données issues des feuilles de soins électroniques anonymisées à bref délai, dont les caractéristiques sont résumées dans le tableau ci-dessous.

Responsable du traitement

|

La société CELTIPharm (56)

|

Finalités

|

- Réalisation d'études épidémiologiques à partir de données issues des feuilles de soins électroniques anonymisées.

- Les finalités principales du traitement sont :

Mise en place d'indicateurs sanitaires avancés

Suivi longitudinal de la consommation médicamenteuse en temps réel des médicaments prescrits ou non

Mesure l'efficacité des recommandations sanitaires auprès des professionnels de santé et de leurs patients

Détection les variations atypiques de délivrance des médicaments ainsi que les tendances

Amélioration de la connaissance des usages post autorisation de mise sur le marché (AMM) des médicaments.

Les analyses seront effectuées à partir d'un panel d'officines représentatives de l'ensemble des officines françaises dont les résultats sont extrapolés à l'ensemble du territoire. Les données recueillies permettent de modéliser les comportements pour anticiper une évolution probable de l'état de santé de la population.

|

Données traitées

|

- Données relatives à la pharmacie émettrice de la FSE : numéro ADELI de la pharmacie et raison sociale

- Données sur le patient : identifiant anonyme unique, mois et année de naissance

- Données concernant le prescripteur : identifiant anonyme unique du prescripteur, spécialité, condition d'exercice, origine de la prescription de l'acte, date de la prescription de l'acte

- Données relatives à l'assurance maladie obligatoire : numéro de la caisse gestionnaire, régime, centre gestionnaire, nature de l'assurance

- Données relatives à l'assurance maladie complémentaire : type de contrat souscrit

- Données relatives à l'acte de soin délivré, aux montants remboursables, aux produits délivrés et prescrits : code d'identification du médicament (CIP) ou du produit (liste des produits et prestations) prescrit et délivré, quantités, tarif unitaire du produit, montant total facturé.

Le NIR, jour de naissance, rang de naissance, numéro de complémentaire santé figurant sur la feuille de soins électronique mais sont utilisés pour créer un identifiant anonyme et supprimés à bref délai

Un identifiant anonyme du prescripteur est calculé à partir de son numéro de prescripteur (ADEL-RPPS).

|

Destinataires

|

- CELTIPharm

|

Information et droit d'accès

|

Des affichettes de présentation du traitement seront apposées dans les pharmacies participant au dispositif.

Un numéro de téléphone vert et une adresse électronique seront mis à la disposition du public pour obtenir de l'information.

Le droit d'accès s'exercera directement auprès de l'officine.

|

Caractéristiques particulières du traitement

|

- Anonymisation : le dispositif mettra en œuvre à plusieurs reprises une fonction d'anonymisation irréversible à clé secrète de type FOIN basée sur une fonction de hachage de la famille SHA-2 (256 bits), référencée ci-après sous le nom de FOIN2.

Les données d'identification du patient feront l'objet d'une double anonymisation FOIN2 : une première anonymisation sera réalisée par les organismes concentrateurs techniques (OCT) et une deuxième par la société CELTIPharm. La clé détenue par l'OCT n'est jamais portée à la connaissance de la société CELTIPharm.

Le même procédé ne peut pas être utilisé pour anonymiser l'identifiant des professionnels de santé puisqu'il n'est pas déchiffré par l'OCT. La société CELTIPharm utilisera des clés de déchiffrement remis par le GIE SESAM Vitale insérés dans une boite noire (HSM) pour déchiffrer cet identifiant. La société CELTIPharm n'a pas accès aux secrets contenus dans cette boite noire. Une fois le déchiffrement de l'identifiant du professionnels de santé réalisé, il lui sera substitué, à bref délai, un nouvel identifiant calculé avec FOIN2.

Les secrets cryptographiques détenus par la société CELTIPharm seront sur supports individuels sécurisés et protégés selon le principe de partage des connaissances, avec un quorum minimum de 3 personnes nécessaires à l'activation d'un secret.

- Sécurité : Les échanges réseaux réalisés dans le cadre de ce traitement seront chiffrés. Le système d'information fait l'objet de mesures de protection logique et physique. Une traçabilité des accès au système d'information par les utilisateurs sera réalisée. La société CELTIPharm mettra en œuvre une politique de sécurité formalisée qui sera mise à jour annuellement. Des audits de sécurité seront effectués de manière régulière.

|

Le Président

Alex TÜRK

# Délibération n° 2013-370 du 28 novembre 2013 autorisant la société CARRE CASTAN CONSULTANTS à mettre en œuvre un traitement automatisé de données à caractère personnel ayant pour finalité la réalisation de veilles et d’études épidémiologiques et médico-économiques à partir des données issues des logiciels de pharmacie.

- Nature : Deliberation
- Type : Autre autorisation
- Numéro : 2013-370
- Date : 2013-11-28
- Publication : 2014-01-15
- État : VIGUEUR
- Légifrance : https://www.legifrance.gouv.fr/cnil/id/CNILTEXT000028464652

(Demande d’autorisation n° 1577460)

La Commission nationale de l'informatique et des libertés,

Saisie par la société CARRE CASTAN CONSULTANTS d’une demande d’autorisation concernant un traitement automatisé de données à caractère personnel ayant pour finalité la réalisation de veilles et d’études épidémiologiques et médico-économiques à partir des données issues des logiciels de pharmacie;

Vu la Convention n° 108 du Conseil de l’Europe pour la protection des personnes à l’égard du traitement automatisé des données à caractère personnel ;

Vu la directive 95/46/CE du Parlement européen et du Conseil du 24 octobre 1995 relative à la protection des personnes physiques à l’égard du traitement des données à caractère personnel et à la libre circulation de ces données ;

Vu la loi n° 78-17 du 6 janvier 1978 modifiée relative à l’informatique, aux fichiers et aux libertés, notamment ses articles 8-III et 25-I-1° ;

Vu le décret n° 2005-1309 du 20 octobre 2005 modifié pris pour l’application de la loi n° 78-17 du 6 janvier 1978 relative à l’informatique, aux fichiers et aux libertés ;

Après avoir entendu M. Jean MASSOT commissaire, en son rapport, et M. Jean-Alexandre SILVY, commissaire du Gouvernement, en ses observations,

Formule les observations suivantes :

La Commission nationale de l’informatique et des libertés a été saisie par la société CARRE CASTAN CONSULTANTS d’une demande d’autorisation relative à un traitement automatisé de données à caractère personnel visant à permettre la réalisation de veilles et d’études épidémiologiques et médico-économiques à partir des données issues des logiciels de pharmacie .

Sur le fondement juridique et la finalité du traitement :

La Commission estime que la demande formulée par la société CARRE CASTAN CONSULTANTS relève de la procédure d’autorisation prévue à l’article 8-III de la loi du 6 janvier 1978 modifiée, dans la mesure où le traitement des données de santé fait l’objet d’un procédé d’anonymisation à bref délai.

La finalité du traitement consiste à permettre la réalisation de veilles et d’études épidémiologiques et médico-économiques à partir des données issues des logiciels de pharmacie

Le traitement a vocation à permettre de :

réaliser des analyses et des projections dans le temps en France concernant les critères de bon usage ou de mésusage de médicaments,

mesurer l’efficacité des recommandations sanitaires officielles auprès des professionnels de santé et de leurs patients,

et à partir des consommations médicamenteuses, d’identifier et de prévenir certains états pathologiques.

Au regard de ces éléments, la Commission considère que la finalité assignée au traitement est déterminée, explicite et légitime, conformément aux dispositions de l’article 6-2° de la loi du 6 janvier 1978 modifiée.

Sur le dispositif envisagé et le procédé d’anonymisation à bref délai :

Le dispositif envisagé consiste :

d’une part, dans l’extraction de données collectées et traitées dans le logiciel de gestion d’officine du pharmacien, spécialement équipé d’une fonctionnalité d’extraction ;

et d’autre part, dans la transmission de celles-ci vers une plateforme, fournie par CARRE CASTAN CONSULTANTS, installée chez un hébergeur de données de santé agréé.

Un procédé d’anonymisation irréversible à bref délai est alors mis en place et se décompose en plusieurs étapes.

Les données d’identification seront pseudonymisées dès leur enregistrement sur la plateforme installée chez le premier hébergeur de données de santé agréé. Un identifiant calculé, dérivé du numéro de sécurité sociale ou NIR, se substituera aux données d’identification.

Les données ainsi pseudonymisées seront transmises chez un second hébergeur de données de santé agrée, qui calculera un nouvel identifiant anonyme au sens de la loi du 6 janvier 1978 modifiée, à partir du premier.

Les données associées à ce second identifiant seront enfin transmises à la société

CARRE CASTAN CONSULTANTS.

Le processus de génération des identifiants est basé sur des boitiers cryptographiques, sur lesquels seront stockées les clés secrètes permettant la génération des identifiants dans le cadre des deux pseudonymisations précitées.

Ces clés ne seront pas accessibles par CARRE CASTAN CONSULTANTS ou par les hébergeurs de données de santé agréés.

Les clés des boitiers sont distinctes, et sont générées lors d’une opération de génération des clés, faisant intervenir trois personnes morales distinctes.

En cas de compromission avérée des clés, celles-ci seront modifiées. Une table de correspondance entre les identifiants générés avec les anciennes clés et les identifiants générés avec les nouvelles clés sera créée afin de conserver l’historique des données. A la fin de la reprise de l’historique des données, les tables de correspondances sont détruites.

La Commission estime que les clés devront être modifiées tous les cinq ans, que les clés aient été endommagées ou non.

S’agissant de l’algorithme utilisé pour générer les clés, les audits annuels prévus par l’hébergeur vérifieront sa robustesse. En cas de compromission de l’algorithme, celui-ci sera modifié, et afin de conserver l’historique des données, une table de correspondance des identifiants générés avec l’ancien algorithme et ceux générés avec le nouvel algorithme sera créé. A la fin de la reprise de l’historique des données, les tables de correspondances sont détruites.

Le dispositif d’anonymisation irréversible à bref délai prévu permet donc de prévenir la ré-identification des personnes dont les données sont dans les logiciels de gestions des pharmacies partenaires, par la société CARRE CASTAN CONSULTANTS ou les hébergeurs de données de santé agréés.

Les personnels chargés de mener les études au sein de la société CARRE CASTAN CONSULTANTS ne disposent pas d’un accès direct à la base de données brutes.

Ceux-ci accèdent à des extractions de données, constituées spécifiquement pour leurs besoins par la société CARRE CASTAN CONSULTANTS. Les données constituant ces extractions sont agrégées, avec un agrégat minimum de cinquante patients.

La Commission considère dès lors que le traitement des données de santé fait l’objet d’un procédé d’anonymisation à bref délai, reconnu conforme aux dispositions de la loi du 6 janvier 1978 modifiée par la Commission, et relève par conséquent des dispositions des articles 8-III et 25-I-1° de la dite loi.

Sur la nature des données traitées :

Les données suivantes seront collectées :

concernant les données relatives à la pharmacie, le numéro ADELI de la pharmacie et sa raison sociale ;

concernant le patient, un identifiant anonyme unique, l’âge, et le sexe ;

concernant le prescripteur, un identifiant anonyme unique du prescripteur, spécialité, condition d'exercice, origine de la prescription de l’acte, date de la prescription de l'acte ;

concernant l’acte de soin délivré, les montants remboursables, les produits délivrés et prescrits, le code d’identification du médicament (CIP) ou du produit (liste des produits et prestations) prescrit et délivré, les quantités, le tarif unitaire du produit, et le montant total facturé.

Le numéro de sécurité sociale du patient, le jour et le rang de naissance, le numéro de complémentaire santé figurent sur la feuille de résultats d’analyses de biologie médicale mais ne sont utilisés que pour créer un identifiant anonyme et supprimés à bref délai.

La Commission considère que les données traitées sont adéquates, pertinentes et non excessives au regard de la finalité poursuivie.

Sur la durée de conservation des données :

Les données, ayant fait l’objet du procédé d’anonymisation irréversible selon les modalités précédemment décrites, sont conservées le temps nécessaire à la réalisation des études et des veilles médico-économiques visées par le présent traitement.

Sur les destinataires des données :

Seuls ont accès au traitement les personnels habilités de la société CARRE CASTAN CONSULTANTS en fonction de leur mission.

La Commission prend acte du fait qu’aucun tiers ne sera rendu destinataire des données traitées.

Sur l'information des personnes :

Des affiches de présentation du traitement seront apposées dans les pharmacies dans lesquels les professionnels de santé participant au dispositif exercent.

Conformément aux dispositions de l’article 32-IV de la loi du 6 janvier 1978 modifiée, relatives aux traitements portant sur des données faisant l’objet à bref délai d’un procédé d’anonymisation au sens de l’article 8-III de la même loi, la note d’information se limite à préciser l’identité du responsable de traitement ainsi que la finalité du traitement de données projeté.

Un numéro de téléphone vert et une adresse électronique seront mis à la disposition du public pour obtenir toute information complémentaire concernant le traitement.

La Commission considère dès lors que ces modalités d’informations sont satisfaisantes.

Sur les droits d'accès, de rectification et d'opposition des personnes :

Les données personnelles ayant fait l’objet d’un procédé d’anonymisation à bref délai au sens de l’article 8-III de la loi du 6 janvier 1978 modifiée, la Commission prend acte qu’aucun des droits prévus aux articles 38 à 40 de la même loi ne pourra s’exercer.

Elle rappelle néanmoins que les personnes peuvent exercer leur droit d’opposition au traitement automatisé de leurs données à caractère personnel dans les logiciels de gestion des pharmacies partenaires.

Sur la sécurité des données et la traçabilité des actions :

La base de données brute, contenant les données est chiffrée par l’algorithme de chiffrement AES 256. L’accès à la clé de chiffrement est protégé par un certificat électronique.

Les transferts de données sont réalisés sur des réseaux virtuels privés sécurisés par le protocole IPSEC.

Les accès à la base de données sont autorisés uniquement aux utilisateurs disposant d’un profil d’administrateur système. Ces utilisateurs doivent s’authentifier par l’usage d’un mot de passe composé d’un minimum de douze caractères, disposant de trois types de caractères distincts parmi les minuscules, majuscules, chiffres ou caractères spéciaux. Il doit être renouvelé tous les quarante-deux jours au maximum.

Le contrôle d’accès est opéré par l’utilisation d’un identifiant et d’un mot de passe. Les mots de passe sont composés d’un minimum de huit caractères, doivent disposer de trois types de caractères distincts parmi les minuscules, majuscules, chiffres ou caractères spéciaux. Ils sont renouvelés tous les quarante-deux jours au maximum.

Les accès et les requêtes effectuées sur les données sont tracés. Ces traces sont auditées au minimum une fois par an.

Sous réserve des précédentes observations, les mesures de sécurité décrites par le responsable de traitement sont conformes à l’exigence de sécurité prévue par l’article 34 de la loi du 6 janvier 1978 modifiée.

La Commission rappelle toutefois que cette obligation nécessite la mise à jour des mesures de sécurité au regard de la réévaluation régulière des risques.

Dans ces conditions, la Commission autorise la société CARRE CASTAN CONSULTANTS à mettre en œuvre un traitement de données à caractère personnel ayant pour finalité la réalisation de veilles et d’études épidémiologiques et médico-économiques à partir des feuilles de résultats d’analyses des laboratoires d’analyses médicales.

La Présidente

Isabelle FALQUE-PIERROTIN

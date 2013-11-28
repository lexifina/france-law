# Délibération n° 2013-369 du 28 novembre 2013 autorisant la société Celtiph@rm à mettre en œuvre un traitement automatisé de données à caractère personnel ayant pour finalité la réalisation d’études et de veilles médico-économiques à partir des feuilles de soins électroniques émises par les professionnels de santé.

- Nature : Deliberation
- Type : Autre autorisation
- Numéro : 2013-369
- Date : 2013-11-28
- Publication : 2014-01-15
- État : VIGUEUR
- Légifrance : https://www.legifrance.gouv.fr/cnil/id/CNILTEXT000028464651

(Demande d’autorisation n° 1594771)

La Commission nationale de l'informatique et des libertés,

Saisie par la société Celtiph@rm d’une demande d’autorisation concernant un traitement automatisé de données à caractère personnel ayant pour finalité la réalisation d’études et de veilles médico-économiques à partir des feuilles de soins électroniques émises par les professionnels de santé ;

Vu la Convention n° 108 du Conseil de l’Europe pour la protection des personnes à l’égard du traitement automatisé des données à caractère personnel ;

Vu la directive 95/46/CE du Parlement européen et du Conseil du 24 octobre 1995 relative à la protection des personnes physiques à l’égard du traitement des données à caractère personnel et à la libre circulation de ces données ;

Vu la loi n° 78-17 du 6 janvier 1978 modifiée relative à l’informatique, aux fichiers et aux libertés, notamment ses articles 8-III et 25-I-1° ;

Vu le décret n° 2005-1309 du 20 octobre 2005 modifié pris pour l’application de la loi n° 78-17 du 6 janvier 1978 relative à l’informatique, aux fichiers et aux libertés ;

Après avoir entendu M. Jean MASSOT, commissaire, en son rapport, et M. Jean-Alexandre SILVY, commissaire du Gouvernement, en ses observations,

Formule les observations suivantes :

La Commission nationale de l’informatique et des libertés a été saisie par la société Celtiph@rm d’une demande d’autorisation relative à un traitement automatisé de données à caractère personnel visant à permettre la réalisation d’études et de veilles médico-économiques à partir des feuilles de soins électroniques (FSE) émises par les professionnels de santé.

Sur le fondement juridique et la finalité du traitement :

La Commission estime que la demande formulée par la société Celtiph@rm relève de la procédure d’autorisation prévue à l’article 8-III de la loi du 6 janvier 1978 modifiée, dans la mesure où le traitement des données de santé fait l’objet d’un procédé d’anonymisation à bref délai.

La finalité du traitement consiste à permettre la réalisation d’études et de veilles médico-économiques à partir de FSE émises par les professionnels de santé.

Le traitement a vocation à permettre au responsable de traitement de disposer de données permettant :

de mener des analyses des consommations de soins par territoire et par bassin de population,

de réaliser un suivi spatio-temporel de la consommation de soins par territoire,

d’en mesurer les variations économiques,

d’établir des indicateurs avancés sanitaires,

et d’identifier l’adéquation entre l’offre de soin et la population.

Au regard de ces éléments, la Commission considère que la finalité assignée au traitement est déterminée, explicite et légitime, conformément aux dispositions de l’article 6-2° de la loi du 6 janvier 1978 modifiée.

Sur le dispositif envisagé et le procédé d’anonymisation à bref délai :

Un contrat tripartite, dont le modèle est versé au dossier de demande d’autorisation, conclu entre la société Celtiph@rm, l’organisme concentrateur technique (OCT) et chaque professionnel de santé, organise les relations entre les différentes parties et définit les droits et obligations de chacun.

Le professionnel de santé, volontaire, s’engage notamment :

à autoriser l’OCT à effectuer le routage des FSE nécessaires à la réalisation du présent traitement de données vers Celtiph@rm ;

à procéder aux formalités idoines auprès de la Commission ;

à informer ses patients, par voie d’affichage.

L’OCT, jouant le rôle de « tiers de confiance », s’engage quant à lui :

à effectuer le routage des FSE, en partie chiffrées, vers Celtiph@rm, et ce sur la base de l’identifiant national du professionnel de santé ;

à suivre les recommandations de la Commission, notamment en termes de mesures de sécurité à mettre en place.

La société Celtiph@rm s’engage :

à fournir des études aux instances représentatives des professionnels de santé participant au dispositif ;

à fournir aux professionnels de santé la documentation nécessaire et notamment la note d’information destinée aux patients ;

et à mettre en place une ligne d’information gratuite accessible aux patients par téléphone, télécopie et courriel.

Le dispositif envisagé consiste en la transmission par le professionnel de santé de FSE vers un OCT, ayant contractualisé avec le responsable de traitement et le professionnel.

L’OCT, utilisant une plateforme fournie par la société Celtiph@rm en son sein, copie le flux des FSE en provenance des professionnels de santé partenaires.

Les données chiffrées au sein des FSE ne seront pas traitées par la société Celtiph@rm qui ne dispose pas des clés de déchiffrement.

Un procédé d’anonymisation irréversible à bref délai est alors mis en place et se décompose en plusieurs étapes.

Une première pseudonymisation des données d’identification contenues dans les FSE sera réalisée par l’OCT, les données d’identification du patient étant alors remplacées par un identifiant calculé, dérivé du numéro de sécurité sociale ou NIR.

Les FSE ainsi pseudonymisées seront transmises, via un accès sécurisé sur un serveur dédié chez un hébergeur de données de santé agréé, qui calculera un nouvel identifiant anonyme au sens de la loi, à partir du premier.

Les données associées à ce second identifiant seront enfin transmises à la société Celtiph@rm.

Le processus de génération des identifiants est basé sur des boitiers cryptographiques, sur lesquels seront stockées les clés secrètes permettant la génération des identifiants dans le cadre des deux pseudonymisations précitées.

Ces clés ne seront pas accessibles par Celtiph@rm, par l’OCT ou par l’hébergeur de données de santé agréé.

Les clés des boitiers sont distinctes et sont générées lors d’une opération de génération des clés, faisant intervenir trois personnes morales distinctes.

En cas de compromission avérée des clés, celles-ci seront modifiées. Une table de correspondance entre les identifiants générés avec les anciennes clés et les identifiants générés avec les nouvelles clés sera alors créée afin de conserver l’historique des données. A la fin de la reprise de l’historique des données, les tables de correspondances seront détruites.

La Commission estime que les clés devront être modifiées tous les cinq ans, que les clés aient été endommagées ou non.

S’agissant de l’algorithme utilisé pour générer les clés, les audits annuels prévus par l’hébergeur examineront sa robustesse. En cas de compromission de l’algorithme, celui-ci sera modifié et, afin de conserver l’historique des données, une table de correspondance des identifiants générés avec l’ancien algorithme et ceux générés avec le nouvel algorithme sera créé. A la fin de la reprise de l’historique des données, les tables de correspondances doivent être détruites.

Le dispositif d’anonymisation irréversible à bref délai prévu permet donc de prévenir la ré-identification des personnes dont les données sont dans les FSE, par la société Celtiph@rm, l’OCT ou l’hébergeur de données de santé.

Les personnels chargés de mener les études au sein de la société Celtiph@rm, ne disposent pas d’un accès direct à la base de données brutes.

Ceux-ci accèdent à des extractions de données, constituées spécifiquement pour leurs besoins par la société Celtiph@arm. Les données constituant ces extractions sont agrégées, avec un agrégat minimum de cinquante patients.

La Commission considère dès lors que le traitement des données de santé fait l’objet d’un procédé d’anonymisation à bref délai, reconnu conforme aux dispositions de la loi du 6 janvier 1978 modifiée par la Commission, et relève par conséquent des dispositions des articles 8-III et 25-I-1° de la dite loi.

Sur la nature des données traitées :

A titre liminaire, la Commission rappelle que seules les données figurant en clair dans les FSE seront collectées et traitées par la société Celtiph@rm, après anonymisation de celles-ci.

Les données suivantes seront collectées :

concernant le prescripteur, un identifiant anonyme unique du prescripteur dérivé du numéro d’inscription au RPPS, spécialité, condition d'exercice, origine de la prescription de l’acte, date de la prescription de l'acte ;

concernant les données relatives au professionnel de santé émetteur de la FSE, le numéro d’inscription au répertoire partagé des professionnels de santé (RPPS) et sa raison sociale ;

concernant le patient, un identifiant anonyme unique et dérivé du NIR, les mois et année de naissance, le sexe et le code postal de résidence ;

concernant l’assurance maladie obligatoire, le numéro de la caisse gestionnaire, le régime, le centre gestionnaire, et la nature de l’assurance ;

concernant l’assurance maladie complémentaire, le type de contrat souscrit ;

concernant l’acte de soin délivré, les montants remboursables, les produits délivrés et prescrits, le code d’identification du médicament (CIP) ou du produit (liste des produits et prestations) prescrit et délivré, les quantités, le tarif unitaire du produit, et le montant total facturé.

Le numéro de sécurité sociale du patient, ou son jour et rang de naissance si le bénéficiaire des soins n’est pas l’assuré et si son NIR n’est pas connu, ainsi que le numéro de complémentaire santé figurent sur la FSE mais ne sont utilisés que pour créer un nouvel identifiant et sont supprimés à bref délai par l’OCT.

La Commission considère que les données traitées sont adéquates, pertinentes et non excessives au regard de la finalité poursuivie.

Sur la durée de conservation des données :

La Commission prend tout d’abord acte qu’aucune donnée ne sera conservée et archivée chez les OCT participant au dispositif projeté.

Les données, ayant fait l’objet du procédé d’anonymisation irréversible selon les modalités précédemment décrites, sont conservées le temps nécessaire à la réalisation des études et des veilles médico-économiques visées par le présent traitement

Sur les destinataires des données :

Seuls ont accès au traitement les personnels habilités de la société Celtiph@rm en fonction de leur mission.

La Commission prend acte du fait qu’aucun tiers ne sera rendu destinataire des données traitées.

Sur l'information des personnes :

Des affiches de présentation du traitement seront apposées dans les cabinets médicaux dans lesquels les professionnels de santé participant au dispositif exercent.

Conformément aux dispositions de l’article 32-IV de la loi du 6 janvier 1978 modifiée, relatives aux traitements portant sur des données faisant l’objet à bref délai d’un procédé d’anonymisation au sens de l’article 8-III de la même loi, la note d’information se limite à préciser l’identité du responsable de traitement ainsi que la finalité du traitement de données projeté.

Un numéro de téléphone vert et une adresse électronique seront mis à la disposition du public pour obtenir toute information complémentaire concernant le traitement.

La Commission considère dès lors que ces modalités d’informations sont satisfaisantes.

Sur les droits d'accès, de rectification et d'opposition des personnes :

Les données personnelles ayant fait l’objet d’un procédé d’anonymisation à bref délai au sens de l’article 8-III de la loi du 6 janvier 1978 modifiée, la Commission prend acte qu’aucun des droits prévus aux articles 38 à 40 de la même loi ne pourra s’exercer.

Elle rappelle néanmoins que les personnes peuvent exercer leur droit d’opposition à la transmission des données vers l’OCT.

Sur la sécurité des données et la traçabilité des actions :

La base de données brute est chiffrée par l’algorithme de chiffrement AES-256. L’accès à la clé de chiffrement est protégé par un certificat électronique.

Les transferts de données sont réalisés sur des réseaux virtuels privés sécurisés par le protocole IPSEC.

Les accès à la base de données sont autorisés uniquement pour les utilisateurs disposant d’un profil d’administrateur système.

Ces administrateurs doivent s’authentifier par l’usage d’un mot de passe composé d’un minimum de douze caractères, composé de trois types de caractères distincts parmi les minuscules, majuscules, chiffres ou caractères spéciaux.

Le contrôle d’accès est opéré par l’utilisation d’un identifiant et d’un mot de passe. Les mots de passe sont composés d’un minimum de huit caractères, de trois types de caractères distincts parmi les minuscules, majuscules, chiffres ou caractères spéciaux. Ils sont renouvelés tous les quarante-deux jours au maximum.

Les accès et les requêtes effectuées sur les données sont tracés. Ces traces sont auditées au minimum une fois par an.

Les mesures de sécurité décrites par le responsable de traitement sont conformes à l’exigence de sécurité prévue par l’article 34 de la loi du 6 janvier 1978 modifiée.

La Commission rappelle toutefois que cette obligation nécessite la mise à jour des mesures de sécurité au regard de la réévaluation régulière des risques.

Dans ces conditions, la Commission autorise société Celtiph@rm à mettre en œuvre un traitement de données à caractère personnel ayant pour finalité la réalisation d’études et de veilles médico-économiques à partir des feuilles de soins électroniques émises par les professionnels de santé.

La Présidente

Isabelle FALQUE-PIERROTIN

# Délibération n° 2015-387 du 5 novembre 2015 autorisant PRICEMINISTER à mettre en œuvre un traitement automatisé de données à caractère personnel ayant pour finalité la lutte contre la fraude et les impayés lors des achats réalisés sur la plateforme PRICEMINISTER.

- Nature : Deliberation
- Type : Autre autorisation
- Numéro : 2015-387
- Date : 2015-11-05
- Publication : 2016-02-04
- État : VIGUEUR
- Légifrance : https://www.legifrance.gouv.fr/cnil/id/CNILTEXT000031969934

(Demande d’autorisation n° 1815753)

La Commission nationale de l'informatique et des libertés,

Saisie par PRICEMINISTER d’une demande d’autorisation concernant un traitement automatisé de données à caractère personnel ayant pour finalité la lutte contre la fraude et les impayés lors des achats réalisés sur la plateforme PRICEMINISTER ;

Vu la convention n° 108 du Conseil de l’Europe pour la protection des personnes à l’égard du traitement automatisé des données à caractère personnel ;

Vu la directive 95/46/CE du Parlement européen et du Conseil du 24 octobre 1995 relative à la protection des personnes physiques à l’égard du traitement des données à caractère personnel et à la libre circulation de ces données ;

Vu la loi n° 78-17 du 6 janvier 1978 modifiée relative à l’informatique, aux fichiers et aux libertés, notamment son article 25.I.4° ;

Vu le décret n° 2005-1309 du 20 octobre 2005 modifié pris pour l’application de la loi n° 78-17 du 6 janvier 1978 relative à l’informatique, aux fichiers et aux libertés ;

Vu le dossier et ses compléments ;

Sur la proposition de M. François PELLEGRINI, commissaire, et après avoir entendu les observations de M. Jean-Alexandre SILVY, commissaire du Gouvernement,

Formule les observations suivantes :

Responsable du traitement

|

PRICEMINISTER, société de vente à distance sur catalogue via la plateforme www.priceminister.com

|

Sur la finalité

|

La société PRICEMINISTER a développé une plateforme internet www.priceminister.com qui permet la mise en relation de vendeurs annonceurs et d'acheteurs de produits neufs ou d’occasion.

Afin de lutter contre les tentatives de fraude relatives aux commandes passées sur la plateforme et aux impayés qui en découlent, la société souhaite mettre en place un traitement pour évaluer les risques présentés par ce type de transactions.

Ce traitement a pour objet d’identifier respectivement les commandes et les paiements effectués à distance auprès de la société PRICEMINSITER et présentant un risque de fraude susceptible de générer un impayé.

La Commission considère que ce traitement peut avoir pour effet d’exclure des personnes du bénéfice d’un contrat en l’absence de toute disposition légale ou réglementaire le prévoyant sans avoir la possibilité de recourir à ce mode de paiement à distance. Il relève donc du 4° du I de l’article 25 de la loi du 6 janvier 1978 modifiée et doit, à ce titre, faire l’objet d’une autorisation de la Commission.

Le traitement considéré est l’outil de mesure de risque (« scoring ») développé par la société PRICEMINISTER. Cet outil permet de traiter deux situations présentant des risques de fraude :

-d’une part, à évaluer le niveau de risque des commandes pour lesquelles l’acheteur a déjà pré-enregistré les données de sa carte bancaire (achats express) et

-d’autre part, à détecter des paniers suspects, dits « paniers en observation », qui sont temporairement bloqués dans l’attente d’une vérification complémentaire.

Plus précisément, le traitement permet le calcul d’un score par panier d’achat en fonction d’un ensemble de critères régulièrement évalués et actualisés afin d’adapter constamment leur pertinence par rapport aux fraudes les plus systématiques rencontrées par le personnel spécialisé du service des fraudes du back-office de PRICEMINISTER. Ces critères sont communs aux deux fonctionnalités du traitement.

Si le score du panier est supérieur à un certain seuil, une demande de communication du cryptogramme visuel de la carte de paiement est envoyée à l’acheteur par le prestataire de paiement et la commande concernée est mise en attente, le temps que l’acheteur fournisse cette information.

Si l’acheteur est dans l’incapacité de communiquer au prestataire le cryptogramme visuel, la transaction par carte bancaire ne peut être finalisée. Il peut néanmoins toujours régler sa commande via un autre moyen de paiement.

Les commandes mises en observation suite à leur détection via des mots clés préenregistrés, doivent être validées manuellement par un opérateur du service fraudes du back-office dans un délai pouvant aller de 48h à 72h maximum.

Les critères de score sont définis par des mots clés adaptés selon les types de fraudes constatées par le service de lutte contre la fraude.

Avant de valider un panier mis en observation, l’opérateur du service des fraudes vérifie la cohérence des données relatives au compte de l’acheteur concerné.

Ce n’est qu’en cas de doute persistant sur la commande qu’une vérification supplémentaire est effectuée et peut prendre l’une des formes suivantes :

- une vérification par le système 3D Secure ;

- ou, dans l’hypothèse ou la carte bancaire n’est pas éligible à la vérification par le système 3D Secure (carte bancaire étrangère, carte type Electron ou American Express), une demande de justificatifs complémentaires est adressée à l’acheteur concerné.

Enfin, et si la vérification par le système 3DS ou l’analyse humaine des justificatifs n’est pas concluante, la commande n’est pas finalisée.

La Commission considère que dès lors qu’une présomption de fraude est confirmée à la suite de l’analyse complémentaire effectuée par PRICEMINISTER, la personne doit être informée individuellement, par écrit, des raisons de l’annulation de sa commande ou de toute décision lui portant grief en lui donnant la possibilité de présenter ses observations.

Elle prend acte que, conformément aux dispositions de l’article 10 de la loi du 6 janvier 1978 modifiée, les résultats du traitement feront l’objet d’une instruction par le service chargé de la prévention de la fraude au cas par cas, et non automatisée.

La Commission relève que seules les données pertinentes relatives à l’acheteur sont utilisées par l’outil de score pour la création de mots clés permettant de détecter les futures tentatives de fraudes.

Par ailleurs, les comptes faisant l’objet d’un impayé sont suivis dans le cadre d’une procédure de recouvrement visant à obtenir le remboursement de la dette de l’acheteur concerné.

La Commission considère que cette finalité est déterminée, explicite et légitime.

|

Sur les données traitées

|

Les catégories de données traitées sont les suivantes :

identification : nom, prénom, adresses postale, de livraison et de messagerie électronique, numéros de téléphone ;

données de connexion : identifiants de connexion au compte (hash du mot de passe), horodatage de la commande, adresse IP et localisation de la machine ;

informations relatives à la commande : montant de la commande, nombre et montant cumulé des achats, ancienneté de la dernière commande, type de produit(s) commandé(s), historique du compte, mode de livraison ;

informations d’ordre économique et financier : informations relatives à la carte bancaire (hash du PAN), mode de paiement, utilisation d’un coupon de parrainage ou d’un bon de réduction, statut du paiement, partenaire de paiement, type de terminal utilisé pour passer la commande (ordinateur ou mobile).

les mots clés identifiants qui n’ont pas été associés à des commandes litigieuses sont effacés au bout de 6 mois ;

en cas de fraudes avérées et d’oppositions, les mots clés identifiants qui n’ont pas été associés à des commandes litigieuses sont effacés au bout de 3 ans, sauf si la situation est régularisée, auquel cas le mot clé est supprimé ;

le commentaire relatif au mot clé identifiant est supprimé des zones de commentaires libres du compte de l’acheteur concerné dans le back-office en application des délais précédents ;

les copies des pièces justificatives sont conservées pendant une durée maximale de six mois ;

enfin en cas de litige les données sont conservées le temps de la procédure puis archivées.

identification : nom, prénom, adresses postale, de livraison et de messagerie électronique, numéros de téléphone ;

données de connexion : identifiants de connexion au compte (hash du mot de passe), horodatage de la commande, adresse IP et localisation de la machine ;

informations relatives à la commande : montant de la commande, nombre et montant cumulé des achats, ancienneté de la dernière commande, type de produit(s) commandé(s), historique du compte, mode de livraison ;

informations d’ordre économique et financier : informations relatives à la carte bancaire (hash du PAN), mode de paiement, utilisation d’un coupon de parrainage ou d’un bon de réduction, statut du paiement, partenaire de paiement, type de terminal utilisé pour passer la commande (ordinateur ou mobile).

les mots clés identifiants qui n’ont pas été associés à des commandes litigieuses sont effacés au bout de 6 mois ;

en cas de fraudes avérées et d’oppositions, les mots clés identifiants qui n’ont pas été associés à des commandes litigieuses sont effacés au bout de 3 ans, sauf si la situation est régularisée, auquel cas le mot clé est supprimé ;

le commentaire relatif au mot clé identifiant est supprimé des zones de commentaires libres du compte de l’acheteur concerné dans le back-office en application des délais précédents ;

les copies des pièces justificatives sont conservées pendant une durée maximale de six mois ;

enfin en cas de litige les données sont conservées le temps de la procédure puis archivées.

identification : nom, prénom, adresses postale, de livraison et de messagerie électronique, numéros de téléphone ;

données de connexion : identifiants de connexion au compte (hash du mot de passe), horodatage de la commande, adresse IP et localisation de la machine ;

informations relatives à la commande : montant de la commande, nombre et montant cumulé des achats, ancienneté de la dernière commande, type de produit(s) commandé(s), historique du compte, mode de livraison ;

informations d’ordre économique et financier : informations relatives à la carte bancaire (hash du PAN), mode de paiement, utilisation d’un coupon de parrainage ou d’un bon de réduction, statut du paiement, partenaire de paiement, type de terminal utilisé pour passer la commande (ordinateur ou mobile).

les mots clés identifiants qui n’ont pas été associés à des commandes litigieuses sont effacés au bout de 6 mois ;

en cas de fraudes avérées et d’oppositions, les mots clés identifiants qui n’ont pas été associés à des commandes litigieuses sont effacés au bout de 3 ans, sauf si la situation est régularisée, auquel cas le mot clé est supprimé ;

le commentaire relatif au mot clé identifiant est supprimé des zones de commentaires libres du compte de l’acheteur concerné dans le back-office en application des délais précédents ;

les copies des pièces justificatives sont conservées pendant une durée maximale de six mois ;

enfin en cas de litige les données sont conservées le temps de la procédure puis archivées.

La Commission considère que les données traitées sont adéquates, pertinentes et non excessives au regard de la finalité poursuivie.

Le traitement vise à évaluer l’authenticité et la cohérence de l’ensemble des éléments identitaires utilisés pour passer la commande. Ces critères peuvent varier ponctuellement et sont adaptés en fonction des fraudes constatées sur la plateforme.

Une copie de la pièce d’identité et un justificatif de domicile de la personne ayant passé commande peuvent également être collectés dans des conditions permettant de garantir la transmission et la conservation de ces documents de manière sécurisée.

Les durées de conservation suivantes sont mises en œuvre :

identification : nom, prénom, adresses postale, de livraison et de messagerie électronique, numéros de téléphone ;

données de connexion : identifiants de connexion au compte (hash du mot de passe), horodatage de la commande, adresse IP et localisation de la machine ;

informations relatives à la commande : montant de la commande, nombre et montant cumulé des achats, ancienneté de la dernière commande, type de produit(s) commandé(s), historique du compte, mode de livraison ;

informations d’ordre économique et financier : informations relatives à la carte bancaire (hash du PAN), mode de paiement, utilisation d’un coupon de parrainage ou d’un bon de réduction, statut du paiement, partenaire de paiement, type de terminal utilisé pour passer la commande (ordinateur ou mobile).

les mots clés identifiants qui n’ont pas été associés à des commandes litigieuses sont effacés au bout de 6 mois ;

en cas de fraudes avérées et d’oppositions, les mots clés identifiants qui n’ont pas été associés à des commandes litigieuses sont effacés au bout de 3 ans, sauf si la situation est régularisée, auquel cas le mot clé est supprimé ;

le commentaire relatif au mot clé identifiant est supprimé des zones de commentaires libres du compte de l’acheteur concerné dans le back-office en application des délais précédents ;

les copies des pièces justificatives sont conservées pendant une durée maximale de six mois ;

enfin en cas de litige les données sont conservées le temps de la procédure puis archivées.

identification : nom, prénom, adresses postale, de livraison et de messagerie électronique, numéros de téléphone ;

données de connexion : identifiants de connexion au compte (hash du mot de passe), horodatage de la commande, adresse IP et localisation de la machine ;

informations relatives à la commande : montant de la commande, nombre et montant cumulé des achats, ancienneté de la dernière commande, type de produit(s) commandé(s), historique du compte, mode de livraison ;

informations d’ordre économique et financier : informations relatives à la carte bancaire (hash du PAN), mode de paiement, utilisation d’un coupon de parrainage ou d’un bon de réduction, statut du paiement, partenaire de paiement, type de terminal utilisé pour passer la commande (ordinateur ou mobile).

les mots clés identifiants qui n’ont pas été associés à des commandes litigieuses sont effacés au bout de 6 mois ;

en cas de fraudes avérées et d’oppositions, les mots clés identifiants qui n’ont pas été associés à des commandes litigieuses sont effacés au bout de 3 ans, sauf si la situation est régularisée, auquel cas le mot clé est supprimé ;

le commentaire relatif au mot clé identifiant est supprimé des zones de commentaires libres du compte de l’acheteur concerné dans le back-office en application des délais précédents ;

les copies des pièces justificatives sont conservées pendant une durée maximale de six mois ;

enfin en cas de litige les données sont conservées le temps de la procédure puis archivées.

identification : nom, prénom, adresses postale, de livraison et de messagerie électronique, numéros de téléphone ;

données de connexion : identifiants de connexion au compte (hash du mot de passe), horodatage de la commande, adresse IP et localisation de la machine ;

informations relatives à la commande : montant de la commande, nombre et montant cumulé des achats, ancienneté de la dernière commande, type de produit(s) commandé(s), historique du compte, mode de livraison ;

informations d’ordre économique et financier : informations relatives à la carte bancaire (hash du PAN), mode de paiement, utilisation d’un coupon de parrainage ou d’un bon de réduction, statut du paiement, partenaire de paiement, type de terminal utilisé pour passer la commande (ordinateur ou mobile).

les mots clés identifiants qui n’ont pas été associés à des commandes litigieuses sont effacés au bout de 6 mois ;

en cas de fraudes avérées et d’oppositions, les mots clés identifiants qui n’ont pas été associés à des commandes litigieuses sont effacés au bout de 3 ans, sauf si la situation est régularisée, auquel cas le mot clé est supprimé ;

le commentaire relatif au mot clé identifiant est supprimé des zones de commentaires libres du compte de l’acheteur concerné dans le back-office en application des délais précédents ;

les copies des pièces justificatives sont conservées pendant une durée maximale de six mois ;

enfin en cas de litige les données sont conservées le temps de la procédure puis archivées.

identification : nom, prénom, adresses postale, de livraison et de messagerie électronique, numéros de téléphone ;

données de connexion : identifiants de connexion au compte (hash du mot de passe), horodatage de la commande, adresse IP et localisation de la machine ;

informations relatives à la commande : montant de la commande, nombre et montant cumulé des achats, ancienneté de la dernière commande, type de produit(s) commandé(s), historique du compte, mode de livraison ;

informations d’ordre économique et financier : informations relatives à la carte bancaire (hash du PAN), mode de paiement, utilisation d’un coupon de parrainage ou d’un bon de réduction, statut du paiement, partenaire de paiement, type de terminal utilisé pour passer la commande (ordinateur ou mobile).

les mots clés identifiants qui n’ont pas été associés à des commandes litigieuses sont effacés au bout de 6 mois ;

en cas de fraudes avérées et d’oppositions, les mots clés identifiants qui n’ont pas été associés à des commandes litigieuses sont effacés au bout de 3 ans, sauf si la situation est régularisée, auquel cas le mot clé est supprimé ;

le commentaire relatif au mot clé identifiant est supprimé des zones de commentaires libres du compte de l’acheteur concerné dans le back-office en application des délais précédents ;

les copies des pièces justificatives sont conservées pendant une durée maximale de six mois ;

enfin en cas de litige les données sont conservées le temps de la procédure puis archivées.

identification : nom, prénom, adresses postale, de livraison et de messagerie électronique, numéros de téléphone ;

données de connexion : identifiants de connexion au compte (hash du mot de passe), horodatage de la commande, adresse IP et localisation de la machine ;

informations relatives à la commande : montant de la commande, nombre et montant cumulé des achats, ancienneté de la dernière commande, type de produit(s) commandé(s), historique du compte, mode de livraison ;

informations d’ordre économique et financier : informations relatives à la carte bancaire (hash du PAN), mode de paiement, utilisation d’un coupon de parrainage ou d’un bon de réduction, statut du paiement, partenaire de paiement, type de terminal utilisé pour passer la commande (ordinateur ou mobile).

les mots clés identifiants qui n’ont pas été associés à des commandes litigieuses sont effacés au bout de 6 mois ;

en cas de fraudes avérées et d’oppositions, les mots clés identifiants qui n’ont pas été associés à des commandes litigieuses sont effacés au bout de 3 ans, sauf si la situation est régularisée, auquel cas le mot clé est supprimé ;

le commentaire relatif au mot clé identifiant est supprimé des zones de commentaires libres du compte de l’acheteur concerné dans le back-office en application des délais précédents ;

les copies des pièces justificatives sont conservées pendant une durée maximale de six mois ;

enfin en cas de litige les données sont conservées le temps de la procédure puis archivées.

Les informations relatives à la personne sont inscrites en liste grise tandis que les données relatives au moyen de paiement sont inscrites en liste noire. Les informations sont conservées sur ces listes pour une durée 3 ans.

|

Sur les destinataires

|

L’accès au traitement est restreint aux seuls collaborateurs habilités du service chargé de la prévention de la fraude.

Ces destinataires n’appellent pas d’observations de la part de la Commission.

|

Sur l’information et le droit d’accès

|

La personne concernée est informée que les données relatives aux commandes sont analysées dans le cadre de la politique de prévention des risques de fraude accessible sur le site internet de PRICEMINISTER et que les vérifications opérées à cette fin sont susceptibles d’entrainer une inscription de la personne ou d’un moyen de paiement en liste grise ce qui a pour effets de déclencher de nouvelles vérifications lors de prochaines commandes.

La Commission considère que dès lorsqu’une présomption de fraude est confirmée à la suite de l’analyse complémentaire effectuée par PRICEMINISTER, la personne doit être informée individuellement, par écrit, des raisons de l’annulation de sa commande ou de toute décision lui portant grief en lui donnant la possibilité de présenter ses observations. Les clients ont la possibilité de présenter leurs observations en cliquant sur un bouton intitulé « répondre à ce message » qui figure dans les courriels adressés par PRICEMINISTER.

Les droits d’accès et de rectification s’exercent auprès du Service back-office et juridique à l’adresse suivante : 42, rue Réaumur – 75002 Paris ou à l’adresse électronique suivante : cil@priceminister.com.

La Commission considère que l’information est suffisante au regard de l’article 32 de la loi du 6 janvier 1978 modifiée.

|

Sur les mesures de sécurité

|

L'accès aux locaux est restreint au moyen de portes verrouillées contrôlées par un moyen d'authentification personnel. Des alarmes sont installées et leur fonctionnement est testé régulièrement.

Les postes de travail disposent d'un pare-feu et d'un logiciel antivirus. Les logiciels et systèmes d’exploitation sont régulièrement mis à jour. La confidentialité des données personnelles hébergées sur des systèmes informatiques mobiles est garantie au moyen de mesures de chiffrement adéquates.

Le responsable de traitement a rédigé une charte informatique sensibilisant les utilisateurs. Des profils d'habilitation sont prévus afin de gérer les accès aux données. Les permissions d'accès sont supprimés pour tout utilisateur n'étant plus habilité.

Chaque utilisateur dispose d'un identifiant qui lui est propre. Le responsable de traitement a mis en place une politique de mot de passe conforme à la recommandation de la Commission.

Une journalisation des opérations de consultation, création, modification et suppression du traitement est réalisée. Les journaux sont conservés et font l’objet d’une analyse régulière. Les utilisateurs sont informés que leurs actions font l'objet d'une journalisation.

Les données sont transmises aux tiers sous forme de fichiers chiffrés au moyen d'un algorithme considéré comme sûr et utilisant des clés de taille suffisantes. La transmission du secret se fait via un canal de communication distinct des données.

Les mots de passe des utilisateurs et des personnes concernées sont conservés hachés.

Des sauvegardes quotidiennes sont réalisées. Elles sont stockées dans un endroit garantissant leur sécurité et leur disponibilité

Les interventions de maintenance font l'objet d'une traçabilité. L'accord de l'utilisateur est recueilli avant toute intervention sur son poste informatique. Les supports de stockages usagés ou en panne font l'objet d'une procédure de destruction ou d'effacement.

Les mesures de sécurité décrites par le responsable de traitement sont conformes à l’exigence de sécurité prévue par l’article 34 de la loi du 6 janvier 1978 modifiée.

La Commission rappelle toutefois que cette obligation nécessite la mise à jour des mesures de sécurité au regard de la réévaluation régulière des risques.

|

Sur les autres caractéristiques du traitement

|

Les utilisations d’une carte par son porteur légitime qui sont rendues irrégulières du seul fait d’un défaut de provision ne font pas partie des risques de fraude qui donnent lieu à la production d’alerte.

Le traitement contient des zones de commentaires libres qui précisent qu’il existe une suspicion de comportement frauduleux émanant de l’acheteur.

La Commission relève que ces commentaires sont objectifs, adéquats, pertinents et non excessifs. En outre, les commentaires sont effacés si après vérification la suspicion s’avère infondée.

|

Autorise, conformément à la présente délibération, PRICEMINISTER à mettre en œuvre le traitement susmentionné.

La Présidente

I. FALQUE-PIERROTIN

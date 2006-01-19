# Délibération portant autorisation d'un traitement mis en oeuvre à titre expérimental par le GIE Groupama TPG et ayant pour finalité l'accès sous forme anonymisée, à l'information sur les défauts visuels des assurés figurant sur les demandes de prises en charge.

- Nature : Deliberation
- Type : Autre autorisation
- Numéro : 2006-010
- Date : 2006-01-19
- Publication : 2019-11-13
- État : VIGUEUR
- Légifrance : https://www.legifrance.gouv.fr/cnil/id/CNILTEXT000017651753

La Commission nationale de l'informatique et des libertés,

Saisie d'une demande d'autorisation par le GIE Groupama (tiers payant généralisé) concernant la mise en place d'une expérimentation ayant pour finalité l'accès, sous forme anonymisée, à l'information sur les défauts visuels des assurés figurant sur les demandes de prises en charge.

Vu la Convention n° 108 du Conseil de l'Europe pour la protection des personnes à l'égard du traitement automatisé des données à caractère personnel ;

Vu la directive 95/46/CE du Parlement européen et du Conseil du 24 octobre 1995 relative à la protection des personnes physiques à l'égard du traitement de données à caractère personnel et la libre circulation de ces données ;

Vu la loi n° 78-17 du 6 janvier 1978 relative à l'informatique, aux fichiers et aux libertés modifiée par la loi n° 2004-801 du 6 août 2004 relative à la protection des personnes physiques à l'égard des traitements de données à caractère personnel, et notamment ses articles 8 et 25 ;

Vu le décret n° 2005-1309 du 20 octobre 2005 pris pour l'application de la loi n° 78-17 du 6 janvier 1978 modifiée ;

Vu le code de la sécurité sociale et ses articles L. 161-29 et R. 115-1 et suivants ;

Après avoir entendu M. Jean-Pierre de Longevialle, commissaire, en son rapport, et Mme Pascale Compagnie commissaire du Gouvernement, en ses observations ;

Formule les observations suivantes :

Le GIE Groupama a saisi la Commission nationale de l'informatique et des libertés d'une demande d'autorisation relative à un traitement automatisé de données à caractère personnel ayant pour finalité l'accès à titre expérimental, sous forme anonymisée, à l'information sur les défauts visuels des assurés figurant sur les demandes de prises en charges en vue d'améliorer leur remboursement.

Des expérimentations comparables ayant également pour objet d'améliorer la prise en charge de l'assurance maladie complémentaire et utilisant un procédé d'anonymisation à bref délai des données à caractère personnel figurant sur les feuilles de soins électroniques ont déjà été autorisées par la Commission.

La branche assurance maladie complémentaire du GIE Groupama qui assure la prise en charge d'une partie des dépenses de soins et de biens médicaux en complément du régime obligatoire reçoit des professionnels de santé des données relatives à l'identité du patient dont le numéro de sécurité sociale, la lettre-clé de l'acte pratiqué ou de la prestation servie ainsi que des demandes de prise en charge papiers.

En matière d'optique, les régimes obligatoires ne remboursent qu'une petite partie des équipements. Les contrats complémentaires santé classiques remboursent les assurés en fonction de forfaits exprimés soit en pourcentage de la prise en charge du régime obligatoire, soit sur la base d'un montant fixe prévu dans le contrat. Ces contrats ne tiennent donc pas compte du défaut visuel de l'assuré. Dès lors, si le défaut de vision est facile à corriger, le coût des équipements est en dessous du forfait mais la prestation optique est fréquemment facturée au niveau du forfait. Lorsque le défaut visuel est important, le forfait est souvent largement dépassé et le reste à charge est substantiel pour l'assuré.

Pour mieux adapter la prise en charge aux besoins de ses assurés, le GIE Groupama propose de moduler les remboursements des verres en fonction de la complexité du défaut visuel du patient et par conséquent en fonction de l'équipement optique nécessaire.

Dans ce cadre, le GIE Groupama souhaiterait que l'opticien conseil puisse accéder, de façon anonymisée, à l'information sur le défaut visuel traité et aux caractéristiques de l'équipement proposé afin de vérifier leur adéquation.

Les assurés qui ne souhaiteront pas s'équiper chez les opticiens partenaires conserveront la possibilité de le faire chez l'opticien de leur choix et seront alors remboursés à hauteur du forfait classique.

Ce dispositif permettra aux assurés d'obtenir une prise en charge plus adaptée à leurs besoins et en particulier de diminuer le reste à charge lorsque leur défaut visuel est très important. Parallèlement, le GIE Groupama sera mieux à même de maîtriser les coûts et de suivre de façon globale l'évolution des dépenses en optique afin de faire évoluer les garanties en conséquence.

Bien qu'il n'existe pas, pour les organismes d'assurance maladie complémentaires, de disposition analogue à l'article L. 161-29 du code de la sécurité sociale qui autorise les professionnels de santé, les organismes et établissements de santé à transmettre le numéro de code des actes effectués, prestations réalisées et pathologies diagnostiquées aux organismes d'assurance maladie obligatoire, la Commission a déjà estimé pouvoir se fonder sur l'article 8-III de la loi du 6 janvier 1978 modifiée pour se prononcer sur les traitements expérimentaux analogues. Aux termes de cette disposition, il est en effet prévu que si les données de santé à caractère personnel sont appelées à faire l'objet à bref délai d'un procédé d'anonymisation préalablement reconnu conforme aux dispositions de la loi précitée par la CNIL, celle-ci peut autoriser, compte tenu de leur finalité, certaines catégories de traitements.

Sur l'architecture du dispositif

Le dispositif expérimental concernera des opticiens partenaires volontaires qui émettront, en accédant à un extranet, les demandes de prises en charge électroniques. Ces flux bénéficieront d'un chiffrement fort.

A réception de ces données chiffrées sur la plate forme d'échange gérée par un prestataire, la demande sera décryptée puis les données relatives à l'identification de l'assuré et au défaut visuel seront immédiatement chiffrées avec deux clés différentes. Une fois ce chiffrement réalisé, la demande de prise en charge sera transmise au système dédié à la gestion des remboursements (prestations optiques) dénommé "middle office". Ce dispositif est hébergé chez un second prestataire de service.

Le "middle office" traitera les demandes de prise en charge. Il déchiffrera les données relatives au défaut visuel, contrôlera le respect des grilles tarifaires et enverra une requête au "back office" du GIE Groupama TPG pour le calcul du reste à charge.

Cette requête comportera l'identité de l'assurée chiffrée, le tarif pratiqué par l'opticien ainsi que le code de la prestation tel qu'il figure sur les décomptes de sécurité sociale qui sont actuellement transmis aux organismes d'assurance maladie complémentaires. Le système informatique du GIE Groupama TPG "back office" déchiffrera les données identifiantes et calculera le reste à charge par rapport aux garanties souscrites.

Le "middle office" réceptionnera la réponse du GIE et communiquera à l'opticien partenaire concerné le montant de la prise en charge et le reste à charge par le biais de la plate forme d'échange (extranet).

Une base "statistique" sera constituée afin d'effectuer des simulations et proposer de nouvelles garanties. Elle ne comportera que des données anonymisées.

Sur les mesures de sécurité mises en oeuvre

Les flux de données entre les opticiens et la plate forme d'échange bénéficieront d'un chiffrement SSL et les clés de chiffrement utilisées pour l'identification de l'assuré et les données relatives au défaut visuel seront différentes. Aucune entité du GIE Groupama ne disposera à la fois des clés permettant d'accéder aux données d'identification des assurés et aux informations médicales.

Toutes les opérations de chiffrement et de déchiffrement seront tracées.

Sur le procédé d'anonymisation

Les précisions apportées sur l'algorithme d'anonymisation, sa longueur et les modalités de stockage de la clé apparaissent satisfaisantes à la Commission dans le cadre d'une expérimentation, et les dispositifs techniques proposés conformes à l'état de l'art.

Le GIE Groupama devra démontrer à l'issue de l'expérimentation que les procédés d'anonymisation ont fait l'objet d'une expertise indépendante et communiquer les résultats de celle-ci à la Commission.

Sur la base de données réclamations

Le GIE Groupama prévoit un processus qui lui permettra, en cas de réclamation de la part d'un assuré ou d'un opticien, de retrouver la demande de remboursement correspondante.

Cette base située au niveau du "middle-office" sera isolée des autres bases et uniquement consultable par l'opticien conseil Groupama à la demande expresse des assurés ou des professionnels de santé concernés pour une seule facture à la fois. Elle ne sera interrogée que dans l'hypothèse où un premier niveau de traitement de la réclamation, ne nécessitant pas de remonter au défaut visuel, sera insuffisant.

Le procédé consistera à créer de nouveau la clé d'anonymisation à partir d'éléments fournis par l'assuré ou l'opticien pour retrouver, dans la base informatique, les informations correspondant à la demande de remboursement électronique concernée par la réclamation. Une traçabilité des accès sera mise en place.

Si la procédure ainsi mise en place semble satisfaisante, il apparaît toutefois nécessaire de vérifier son effectivité. A cet égard, la Commission considère comme indispensable la procédure d'expertise indépendante qui permettra en particulier de démontrer la pertinence de cette base et son utilité avant toute généralisation.

La Commission demande qu'un bilan détaillé de l'utilisation de la base lui soit remis à l'issue de l'expérimentation.

Sur les mesures d'information des personnes concernées Outre l'information sur le dispositif diffusée par le GIE Groupama dans les conditions générales du contrat d'assurance santé et la note d'infonnation qui sera envoyée aux assurés avant le lancement de l'expérimentation, il convient de proposer aux partenaires des affichettes d'information qu'ils pourront apposer dans leur centre d'optique.

Les assurés seront informés qu'ils peuvent refuser la transmission de leurs données anonymisées et envoyer leur demande de prise en charge par courrier postal.

Autorise dans ces conditions le GIE Groupama à mettre en oeuvre à titre expérimental pour une durée d'un an, un traitement ayant pour finalité l'accès sous forme anonymisée à l'information sur les défauts visuels du patient figurant sur les demandes de prises en charge sur le fondement de l'article 8-III relatif à l'anonymisation à bref délai.

Le président, Alex TURK.

# Délibération n°2010-033 du 11 février 2010 autorisant la mise en œuvre par le Centre Oscar Lambret de Lille d’un traitement de données à caractère personnel reposant sur la reconnaissance de l'empreinte digitale avec base centralisée et ayant pour finalité le contrôle de l'identité des patients pris en charge en radiothérapie.

- Nature : Deliberation
- Type : Autre autorisation
- Numéro : 2010-033
- Date : 2010-02-11
- Publication : 2019-11-13
- État : VIGUEUR
- Légifrance : https://www.legifrance.gouv.fr/cnil/id/CNILTEXT000022039257

(demande d’autorisation n°1340737)

La Commission nationale de l’informatique et des libertés,

Vu la Convention n° 108 du Conseil de l’Europe pour la protection des personnes à l’égard du traitement automatisé des données à caractère personnel ;

Vu la directive 95/46/CE du Parlement européen et du Conseil du 24 octobre 1995 relative à la protection des personnes physiques à l’égard du traitement de données à caractère personnel et à la libre circulation de ces données ;

Vu la loi n° 78-17 du 6 janvier 1978 relative à l'informatique, aux fichiers et aux libertés, modifiée en 2004, notamment ses articles 6-3° et 25-I-8°;

Vu le décret n° 2005-1309 du 20 octobre 2005 pris pour l’application de la loi n° 78-17 du 6 janvier 1978 relative à l’informatique, aux fichiers et aux libertés, modifié en 2007 ;

Vu la demande d’autorisation déposée le 16 janvier 2009 par le Centre Oscar Lambret, Centre régional de lutte contre le cancer du Nord-Pas-de-Calais;

Après avoir entendu le Professeur Eric Lartigau, Chef du Département Universitaire de Radiothérapie du Centre Oscar Lambret le 28 janvier 2010 devant la Commission réunie en séance plénière;

Sur le rapport de M. Jean MASSOT, commissaire et les observations de Mme Elisabeth ROLIN, commissaire du Gouvernement ;

En application de l’article 25-I-8° et de la loi du 6 janvier 1978 modifiée en 2004, la Commission est saisie par le Centre Oscar Lambret d’une demande d’autorisation relative à la mise en œuvre, à titre expérimental, d’un traitement de données à caractère personnel reposant sur la reconnaissance de l’empreinte digitale et le recours à une base centralisée et ayant pour finalité de renforcer la sécurité des personnes prises en charge en radiothérapie, en prévenant les erreurs d’identification de ces personnes.

Formule les observations suivantes :

Le Département Universitaire de Radiothérapie du Centre Oscar Lambret de Lille, Centre régional de lutte contre le cancer du Nord-Pas-de-Calais, prend en charge 300 patients par jour.

L’identification des patients est un enjeu important dans le cadre des traitements en radiothérapie compte tenu de leurs spécificités : il s’agit, en effet, d’une prise en charge thérapeutique nécessitant plusieurs séances hebdomadaires étalées sur plusieurs semaines (en moyenne 20 séances par patient pendant une durée variant de 4 à 7 semaines, à raison de 5 séances par semaine), effectuée avec des équipements de très haute technologie entièrement pilotés par le système informatique, en présence de personnels mobiles qui travaillent en flux tendu. En outre, une multitude d’acteurs du système de soins (personnel d’accueil, radiothérapeute, manipulateurs…) interviennent dans le cadre de cette prise en charge.

Ce flux croissant de personnes implique des garanties d’identification toujours plus drastiques, afin de se prémunir contre les erreurs et les risques qui pourraient découler d’une mauvaise identification d’un patient.

A cette fin, le Centre Oscar Lambret souhaite mettre en place un procédé biométrique fondé sur la reconnaissance d’empreinte digitale, assorti de la constitution d’une base de données biométriques. Le traitement projeté doit permettre de certifier, avant le lancement du traitement, la concordance entre le patient présent dans la salle de traitement et celui identifié par le système informatique et, ainsi, de renforcer la sécurité des patients pris en charge en radiothérapie, en prévenant les risques d’erreur.

Le dispositif biométrique serait mis en place à titre expérimental pendant un an, afin d’en tester l’efficacité, la faisabilité, ainsi que l’acceptabilité par les patients.

La mise en œuvre du dispositif reposera sur sept lecteurs biométriques, situés à l’accueil de l’hôpital et dans les six salles de traitement par radiothérapie. Ces lecteurs seront reliés à un serveur à partir duquel il sera possible de piloter le fonctionnement du dispositif et notamment le processus d’enrôlement et de suppression des données.

Tout patient qui entrera dans l’établissement pour une prise en charge en radiothérapie se verra proposer de participer au dispositif expérimental.

L’enrôlement sera effectué par le personnel d’accueil de l’hôpital, spécialement formé, après information et recueil du consentement du patient. Un gabarit chiffré des empreintes digitales (3 captures de 2 doigts) des patients volontaires sera stocké dans une base de données cryptée (de type SQL Server ou Oracle chiffrée en AES 256) et associé aux données d’identification du patient et à une photographie de ce dernier, prise à ce stade.

Une carte individuelle sera également produite et délivrée au patient sur laquelle seront inscrits son gabarit biométrique, son identité et sa photo. Elle ne sera utilisée que dans l’hypothèse où un nouveau traitement s’avèrerait nécessaire, afin de réintroduire les données biométriques du patient dans la base directement par lecture de sa carte, sans avoir à effectuer un nouvel enrôlement du patient.

L’identité du patient sera contrôlée lors de chaque séance de radiothérapie, à son arrivée dans le service et préalablement au lancement du traitement. Le patient apposera son doigt sur le lecteur biométrique du boîtier, une comparaison s’effectuera alors entre cette empreinte digitale et le gabarit enregistré dans la base de données. La fiche d’identité du patient accompagnée de sa photo s’affichera alors sur l’écran de contrôle. Le manipulateur pourra ainsi vérifier la concordance entre le patient et les données stockées dans le système informatique avant de démarrer le traitement.

La conservation par le Centre Oscar Lambret du gabarit biométrique sera limitée à la durée de la prise en charge thérapeutique du patient. A l’issue de celle-ci, les données d’empreintes seront effacées de la base de données détenues par le Centre. Cet effacement sera effectué lors de la clôture du dossier par le service chargé de la facturation.

Le patient restera alors seul possesseur des données biométriques enregistrées dans la carte individuelle.

Le dispositif sera subordonné au consentement éclairé et préalable du patient ou des personnes habilitées par la loi à le représenter qui se verront remettre à cet effet, par le service d’accueil de l’hôpital, une note d’information, ainsi qu’un «formulaire de recueil du consentement de participation à l’évaluation de la biométrie dans le département de radiothérapie du centre Oscar Lambret ».

Dans la mesure où le dispositif repose sur le volontariat, un mode alternatif sera disponible en parallèle. Les personnes qui ne consentiront pas à l’utilisation de la biométrie se verront attribuer une carte non biométrique sur laquelle figureront leur photo et les références de leur dossier médical.

Appréciation du traitement au regard de la loi du 6 janvier 1978 modifiée en 2004

En application de l’article 6-3° de la loi du 6 janvier 1978 modifiée en août 2004, il appartient à la Commission de déterminer si le traitement projeté porte sur des données à caractère personnel adéquates, pertinentes et non excessives au regard des finalités pour lesquelles elles sont collectées et de leurs traitements ultérieurs.

A cet égard, elle observe que le Centre Oscar Lambret a fait le choix d’un dispositif reposant sur la reconnaissance de l’empreinte digitale, assortie de la constitution d’une base centralisée, dispositif que la Commission n’admet que dans les cas où un fort impératif de sécurité le justifie.

Sur ce point, la Commission constate que l’identification certaine de la personne soignée est un enjeu majeur de la sécurité sanitaire et que l’ « identitovigilance » occupe une place particulière en matière de radiothérapie, compte tenu du nombre de patients traités, de l’automatisation du traitement et des conséquences d’une erreur dans ce domaine. Il est impératif d’éviter que les patients soient exposés à un risque d’irradiation inappropriée, susceptible d’avoir des conséquences graves, voire irréversibles pour leur santé.

La Commission relève, en outre, que le dispositif retenu répond à des contraintes liées à la maladie ou au traitement des patients. En effet, le Centre Oscar Lambret précise s’être orienté vers un dispositif biométrique fondé sur l’empreinte digitale plutôt que le réseau veineux, technique biométrique sans trace, dans la mesure où il a été constaté sur le plan scientifique que la pathologie ou les effets secondaires du traitement de chimiothérapie, souvent associé à la radiothérapie, étaient de nature à « modifier significativement dans le temps le réseau veineux superficiel » des sujets malades, ce qui n’a pas été démontré pour l’empreinte digitale. De même, il est apparu qu’une solution reposant exclusivement sur l’enregistrement du gabarit biométrique sur un support individuel détenu par le patient n’apporterait pas un niveau de sécurité équivalent à celui recherché dans la mesure où certains patients, en raison de leur maladie ou leur âge, étaient susceptibles de perdre ou d’oublier leur carte ou tout autre support externe. Enfin, il a été indiqué que tout système non biométrique porté sur le patient (bracelet, tatouage…) avait été jugé inacceptable, compte tenu de son caractère visible, donc stigmatisant.

Dans ces conditions particulières, la Commission considère que le recours à la reconnaissance de l’empreinte digitale avec stockage dans une base centralisée répond à une finalité légitime et peut apparaître adapté et proportionné au regard de cette finalité pour l’expérimentation projetée.

La Commission relève que si un contrôle d’identité du patient est effectué par le système, à l’aide de l’empreinte digitale, la décision de lancer le traitement est prise par le manipulateur après un contrôle effectué à l’aide de la fiche d’identification du patient. La Commission en prend acte avec satisfaction dans la mesure où la technique doit venir à l’appui de l’organisation du service et de la vigilance du personnel, non s’y substituer. Elle prend acte de la volonté affirmée de conserver aux professionnels de santé un rôle premier pour garantir la sécurité des patients.

La Commission relève également que la durée de conservation des données biométriques sera limitée à celle du traitement des patients.

Les droits d’accès et de rectification s’exerceront directement auprès du Département Universitaire de Radiothérapie du Centre Oscar Lambret.

Les catégories de données à caractère personnel enregistrées seront le gabarit de l’empreinte digitale, des données d’identification (le nom, le prénom, le sexe, la date de naissance, adresse, téléphone, numéro de sécurité sociale (à des fins de facturation), la photographie numérique.

Les destinataires des informations seront, dans la limite de leurs attributions et pour la poursuite de la finalité précitée, les personnels habilités du service de radiothérapie.

En conséquence, la Commission demande :

que lui soit communiqué, au terme de l’expérimentation, le bilan portant sur la faisabilité et l’acceptabilité du projet qui sera établi à l’issue de l’expérimentation. Il comportera notamment une évaluation de la fiabilité de la reconnaissance biométrique des personnes malades par empreintes digitales.

-qu’afin de garantir la sécurité des patients, le système soit paramétré pour limiter le taux de fausses acceptations ;

Dans ces conditions, la Commission autorise le Centre Oscar Lambret à mettre en œuvre, à titre expérimental, le traitement de données à caractère personnel présenté pendant une durée de un an à compter de la présente délibération.

Le Président

Alex TURK

# CAD - Informatisation du plan cadastral - Politique conventionnelle menée par la DGFiP - Phase technique

- Identifiant : BOI-CAD-INFO-10-20-20191105
- Publié le : 2019-11-05
- Type : Commentaire
- Série : CAD, INFO
- Bureau : DGFIP
- Page officielle : https://bofip.impots.gouv.fr/bofip/5178-PGP.html/identifiant=BOI-CAD-INFO-10-20-20191105
- Directeur de publication : Jérôme Fournel, directeur général des finances publiques
- Références : Contenu:5101-PGP, Contenu:5193-PGP, Contenu:5195-PGP, Contenu:5294-PGP

## Texte

CAD - Informatisation du plan cadastral - Politique conventionnelle menée par la DGFiP - Phase technique

1

La signature d’une convention entraîne la mise en œuvre de certains travaux, pour certains
réalisés par les services de la direction générale des Finances publiques (DGFiP), pour d'autres réalisés par les partenaires.

## I. Les interlocuteurs de la DGFiP au cours de la phase technique

10

La phase technique peut, en fonction de l'avancement et de la qualité des travaux, donner lieu à
de nombreux échanges entre la DGFiP, ses partenaires, et sur certains points techniques, entre la DGFiP et le prestataire chargé des travaux de vectorisation.

### A. Les relations entre la DGFiP et ses partenaires associés

20

L'interlocuteur privilégié de la DGFiP dans le cadre conventionnel reste le coordinateur des
partenaires associés avec lesquels elle est engagée contractuellement.

Celui-ci doit être informé de toutes les difficultés importantes qui pourraient survenir dans la
réalisation des travaux des prestataires (calendrier de livraison non respecté, géoréférencement externalisé non validé, anomalies récurrentes et/ou multiples, etc.).

En cas de difficultés persistantes (qualité des données non conformes, retard important dans les
travaux ou absence totale de travaux), la résiliation de la convention pourra être mise en œuvre conformément aux dispositions prévues.

### B. Les relations entre la DGFiP et les prestataires des partenaires associés

30

La DGFiP assure, si besoin est, un soutien technique auprès des prestataires chargés des travaux
de vectorisation (respect des recommandations de numérisation élaborées par la DGFiP, respect des standards d'échange, analyse des cas particuliers présents sur le plan cadastral induisant des
difficultés lors de la vectorisation, explications techniques sur les corrections à réaliser, etc.).

En outre, le traitement des raccords de feuilles infra-communaux, s'il est réalisé par le
prestataire dans le cadre de la convention, est effectué en concertation avec le correspondant technique de la DGFiP.

## II. Les données échangées par la DGFiP et les partenaires associés

### A. Les données transmises par la DGFiP

40

La DGFiP communique aux partenaires associés aux fins de vectorisation les copies des fichiers
des plans scannés, ainsi que les fichiers des localisants parcellaires. Avant transmission, les plans pourront utilement être mis à jour des croquis en instance de manière à minimiser les travaux
ultérieurs de report dans l'application PCI-Vecteur.

S'agissant du géoréférencement, plusieurs cas sont à distinguer.

#### 1. La DGFiP fournit aux partenaires associés les fichiers de géoréférencement

50

Les données transmises varient en fonction du mode de réalisation des plans.

##### a. Tous les plans de la commune ont été réalisés par voie de réfection, remaniement, renouvellement ou suite à un
aménagement foncier rural

60

Les fichiers générés par l'application PCI-Image sont les fichiers à fournir au prestataire
chargé des travaux de vectorisation du plan.

Le fichier de géoréférencement d'une feuille de plan est un fichier texte contenant les
coordonnées des quatre coins du fichier "tagged image file format" (fichier TIFF) de la feuille exprimées dans le système "pixel", et dans le système de projection de référence nationale ainsi que les
paramètres arrondis de la transformation mathématique de géoréférencement.

Au préalable, ces feuilles de plan qui disposent d'un carroyage auront été référencées dans
PCI-Image, dans le système de projection national.

##### b. Tous les plans de la commune ont été rénovés par voie de mise à jour ou renouvelés en coordonnées indépendantes

70

Ces feuilles de plan ne disposent pas d'un carroyage exploitable. Aucun géoréférencement
exploitable ne peut être extrait de PCI-Image.

Les fichiers de géoréférencement à délivrer aux partenaires associés sont ceux obtenus :

- soit auprès de l'institut national de l'information géographique et forestière (IGN). La
convention d'échanges conclue le 25 mars 2010 entre la DGFiP et l’IGN prévoit en effet la fourniture à la DGFiP des fichiers de géoréférencement des feuilles du plan cadastral non connues en
coordonnées. Ces fichiers pourront être rediffusés aux partenaires associés, après leur vérification par les services ;

- soit auprès d'un prestataire externe ;

- soit par la réalisation d'un géoréférencement en régie
(BOI-CAD-TOPO-50).

En tout état de cause, il est important de traiter la commune de manière homogène en optant
pour l'ensemble de ses feuilles de plan pour une des solutions ci-dessus.

##### c. Les plans de la commune répondent pour partie aux deux cas précédents

80

Pour les feuilles qui ont été réalisées par voie de réfection, remaniement, renouvellement ou
aménagement foncier rural, les fichiers de géoréférencement à délivrer aux partenaires associés sont ceux obtenus en utilisant le carroyage présent sur chaque feuille de plan.

Ainsi pour ces planches cadastrales, dans la mesure où le carroyage présent est de bonne
qualité, il est formellement proscrit de géoréférencer à nouveau ces plans (en régie ou à l'entreprise) ou d'utiliser les fichiers de géoréférencement de l'IGN.

Pour les feuilles de plan restantes qui ont été rénovées par voie de mise à jour ou
renouvelées en coordonnées indépendantes, les fichiers de géoréférencement à transmettre au prestataire chargé de la vectorisation du plan sont ceux obtenus :

- soit auprès de l'IGN ;

- soit auprès d'un prestataire externe ;

- soit par la réalisation d'un géoréférencement en régie
(BOI-CAD-TOPO-50).

Remarque : Pour garantir une certaine homogénéité, il convient de traiter cette
partie restante de la commune en optant pour une seule des trois solutions possibles. Les discordances qui pourraient être mises en évidence entre les sections possédant un carroyage et les autres
feuilles de plan seront traitées selon les prescriptions relatives au traitement des raccords entre feuilles de plan.

#### 2. Les partenaires associés prennent en charge les travaux de géoréférencement

90

Ces travaux ne concernent que les plans rénovés par voie de mise à jour ou renouvelés en
coordonnées indépendantes.

La DGFiP remettra aux partenaires associés les images des feuilles cadastrales à
géoréférencer.

Ces images ont les caractéristiques suivantes :

- une image par feuille ;

- fichiers binaires noirs et blancs (scannage natif en 256 niveaux de gris ramené
automatiquement à 16 niveaux de gris, puis transformation des images en fichiers binaires en noir et blanc obtenus par partage automatique sur la gamme des 16 niveaux de gris) ;

- résolution de 300 dpi ;

- format de l’image scannée pouvant varier en fonction de la caméra utilisée lors du scannage
de la feuille (parmi 4 caméras). Le format est proche de 12 350 pixels x 8 860 pixels ;

- compression en CCITT Groupe 4 monolithique BPS, extension "tif" ;

- fichiers des localisants parcellaires ;

- fichiers de géoréférencement issus de PCI-Image s'il existe sur la commune des feuilles
rénovées par voie de réfection, remaniement, renouvellement suite à un aménagement foncier rural ;

- points connus dans le système légal.

### B. Les données transmises par les partenaires aux conventions

#### 1. À l'issue des travaux de géoréférencement

100

Les partenaires associés remettent à la DGFiP un dossier composé des pièces suivantes :

- le cédérom initialement transmis par le service du cadastre ;

- un cédérom contenant les fichiers d’images des feuilles cadastrales annotées des points
d’appui (symbole et numéro) permettant la vectorisation et le géoréférencement de la feuille. Il est précisé qu'à aucun moment l'image du plan cadastral ne doit être ré-échantillonnée ;

- un fichier "NXY" au format texte reprenant l’ensemble des points déterminés sur la commune
avec leurs coordonnées, pour la métropole, en Lambert 93 ou Conique Conforme 9 zones selon le système de projection retenu. Ce fichier comprend une première ligne de texte contenant le nom de la
commune puis la liste des points (un point par ligne) sous la forme N séparateur X séparateur Y ;

- un tirage sur papier au format A0 de chaque feuille annotée ;

- un dossier technique décrivant la méthodologie employée pour le géoréférencement et les
caractéristiques de la base de données géographiques utilisée pour l’opération.

#### 2. A l'issue des travaux de vectorisation

110

Les partenaires associés remettent à la DGFiP les fichiers vectorisés dans le système de
référence en vigueur selon le standard d’échange des objets du plan cadastral informatisé fondé sur le format fixé par la convention.

Pour permettre la vérification de la qualité des travaux, ils remettent également à la DGFiP
le tableau des points de calage avec leurs résidus, un fichier NXY comprenant uniquement les coordonnées des points de calage dans le système de référence en vigueur, un fichier de type image (au
format TIFF de préférence) issu du plan cadastral scanné remis par le service du cadastre et comprenant l’indication des points de calage utilisés, le fichier NXY de l’ensemble des points vectorisés.

## III. Le contrôle de la qualité des données

### A. La vérification du géoréférencement

120

Les partenaires associés ayant une obligation de résultat, la qualité des fichiers transmis
seront contrôlés par la DGFiP conformément aux prescriptions relatives à la vérification des travaux topographiques (BOI-CAD-TOPO-60 au IV-D-2
§ 275 et suivants).

S'agissant plus particulièrement des fichiers de géoréférencement obtenus auprès de l'IGN et
compte tenu des spécificités du prestataire, de sa méthodologie de géoréférencement connue de la DGFiP, les travaux de vérification pourront être allégés sans jamais réaliser moins d'un point de
contrôle par commune.

Il convient d'adapter cet allègement en fonction d'une part, de la qualité du plan cadastral à
géoréférencer et d'autre part de la nature du terrain (zones montagneuses ou à forte dénivelées, zones frontalières ou côtières) et donc de la qualité des orthophotographies.

### B. La vérification de l'exhaustivité et de la précision

130

Les vérifications de la précision et de l’exhaustivité des données vectorisées permettent de
s’assurer de la conformité du plan vectorisé au plan minute de conservation. Ils donnent lieu à la rédaction d’un rapport de vérification et à l’attribution d’un label. Les modalités techniques de
cette vérification sont les suivantes.

#### 1. Objet de la vérification

140

Cette vérification consiste à apprécier et à certifier la qualité des données fournies par les
partenaires associés. La vérification consiste à contrôler la conformité des données vectorisées par rapport au plan issu de PCI-Image et fourni au prestataire par le service.

Le contrôle doit porter sur deux aspects :

- le contrôle de l’exhaustivité du contenu ;

- le contrôle de la précision topométrique.

La procédure de vérification décrite au III-B-2 § 150 à 250 est à mettre en
œuvre pour toute feuille de plan vectorisée, quel que soit son mode de rénovation.

#### 2. Modalités de la vérification

##### a. Le contrôle du contenu

150

Le contrôle du contenu consiste à s'assurer que les données vectorisées sont conformes aux
indications présentes sur le plan cadastral.

Pour permettre ce contrôle, les partenaires associés devront produire un fichier vectoriel au
format prévu dans la convention (format d'échange
EDIGéO ou
DXF-PCI).

160

Le contrôle pourra être effectué selon les modalités suivantes :

- un contrôle systématique, permettant de s'assurer que les informations du plan cadastral ont
été reprises dans le respect des recommandations de la DGFiP pour la vectorisation du plan cadastral, sera effectué sur 50 % des feuilles vectorisées. Ces feuilles devront être choisies en tenant
compte de la densité foncière de chaque feuille, étant précisé que les opérations de vérification concerneront en priorité les plans cadastraux présentant le maximum d'informations. En particulier, le
vérificateur s’attachera à relever les anomalies suivantes :

- l’absence de certains éléments essentiels figurant sur le PMC (limites de propriété,
bâtiments, numéros de parcelles et de voirie, toponymie, etc.),

- les parcelles ou les bâtiments mal fermés,

- les erreurs d’attribution des numéros de parcelles ou de voirie,

- la mauvaise lisibilité ou le défaut de positionnement des signes conventionnels et des
écritures.

Cette liste n’est cependant pas exhaustive. Il appartient au vérificateur d’apprécier si la
nature et l’importance des discordances constatées sont susceptibles de nuire à la qualité des informations cadastrales tant du point de vue de la consultation que de la mise à jour. C’est le cas
notamment des conventions de dessin ;

- les autres feuilles vectorisées seront contrôlées selon l'alternative suivante :

- la première tranche de vérification, décrite ci-dessus, a permis de s'assurer de la qualité
de la vectorisation. Dans ce cas, le contrôle des autres feuilles sera allégé, et ne portera que sur les éléments essentiels du plan (limites de parcelles, bâtiments, toponymie),

- la première tranche de vérification a révélé un grand nombre d'anomalies. Dans ce cas, le
service pourra arrêter la vérification et informer les partenaires associés du rejet de la vectorisation de la commune concernée.

170

Enfin, dans le cadre du contrôle du contenu, le vérificateur examinera avec soin le plan
vectorisé pour relever certaines anomalies géométriques. La comparaison du plan d’origine et de sa représentation après numérisation permettra en particulier d’apprécier les défauts d’orthogonalité,
de parallélisme et d’alignement.

##### b. Le contrôle de la précision topométrique

180

Le contrôle de la précision consiste à apprécier d’une part la qualité du calage et d’autre
part la qualité des points vectorisés.

Le contrôle pourra être effectué par sondage selon les modalités suivantes :

- lorsque le partenaire a une seule commune à vectoriser, le nombre de feuilles vérifiées doit
être au moins égal à 25% ;

- lorsque le partenaire a plusieurs communes à vectoriser, une dégressivité du nombre de
feuilles à vérifier pourra être appliquée. Pour la commune la plus importante en nombre de planches cadastrales, 25% des feuilles au moins seront vérifiées. Pour les communes suivantes, le
vérificateur se contentera de contrôler 10% des feuilles de chacune d’elles.

Le vérificateur veillera à constituer un échantillon représentatif des différents types de
plan rencontrés sur une commune, notamment en termes de mode de confection, de densité du bâti et de morcellement du parcellaire.

###### 1° Le contrôle du calage

190

Dans le processus de vectorisation, les points enregistrés sont affectés d'un premier jeu de
coordonnées. Celles-ci sont ensuite transformées dans le système RGF 93, projection Lambert 93 ou conique conforme de la zone correspondant au département (ou dans le système et la projection
concernant le DOM) au moyen de points connus dans les deux systèmes de coordonnées, appelés points de calage. (pour plus d'information sur les systèmes de référence de coordonnées,
BOI-CAD-TOPO-10 au II § 30 à 140). Ce changement doit s’opérer au moyen d’une transformation (Helmert en principe) qui n'entraîne aucune
modification du plan cadastral, hormis une réorientation et une mise à l'échelle de la zone transformée.

Pour les besoins du contrôle, le partenaire devra fournir l’identification des points de
calage utilisés pour la vectorisation sous la forme d’un fichier d’images issu du plan cadastral scanné et comprenant l’indication des points de calage utilisés.

Conjointement, le partenaire doit fournir un document donnant, pour chaque point de calage,
l’écart en abscisse, l’écart en ordonnée, le résidu en position correspondant et l’erreur moyenne quadratique des résidus.

Le cas des points de calage éliminés du calcul des paramètres de la transformation, parce que
présentant un résidu hors tolérance, doit être examiné avec les responsables de la vectorisation.

Enfin, le partenaire doit fournir un fichier NXY comprenant uniquement les coordonnées Lambert
93 ou CC 9 zones des points de calage.

Le vérificateur contrôle le calage sur les mêmes points que ceux choisis par le partenaire.

200

Dans le cas d’une vectorisation réalisée à partir du plan scanné et d’un fichier de
géoréférencement fourni par le service (issu de PCI-image ou du logiciel de géoréférencement), ce même fichier de géoréférencement pourra être utilisé directement par le logiciel de vérification, ce
qui permettra d’alléger, voire de supprimer le contrôle du calage. Dans ce cas, le partenaire n’aura plus à fournir l’ensemble des éléments cités au III-B-2-b-1° § 190.

###### a° Cas des feuilles carroyées

210

En cas de vérification de feuilles carroyées, les points de calage peuvent être choisis
parmi les croisées de carroyage. Dans ce cas, ils devront être répartis harmonieusement sur l'ensemble de la planche cadastrale et leur nombre ne devra pas être inférieur à dix. Cette dernière
condition doit permettre, après une première transformation, d’éliminer les points hors tolérance, ainsi que ceux qui, tout en étant dans la tolérance, présentent un résidu manifestement supérieur à
la moyenne des autres écarts. Dans tous les cas, cinq points de calage, répartis de façon homogène, constituent un minimum à respecter.

Les écarts en position, appelés résidus, résultant de la comparaison entre les coordonnées
des points de calage et leurs coordonnées transformées, sont soumis à la tolérance T = 0,04 x E, où E représente le facteur d'échelle du plan et où T est exprimée en centimètres.

En cas de dépassement de la tolérance imputable à la mauvaise qualité du carroyage, la
méthode relative aux feuilles non carroyées peut être appliquée.

###### b° Cas des feuilles non carroyées

220

Il conviendra dans ce cas :

- de s'assurer que les points retenus pour la transformation (au nombre minimal de cinq)
présentent une répartition homogène sur la feuille ;

- de veiller à ce qu’ils aient été choisis de façon à minimiser les résidus de l'adaptation,
en n'éliminant cependant que les points manifestement aberrants ;

- de comparer pour chaque point de calage les résidus obtenus par la DGFiP lors du contrôle
avec ceux constatés par l'entrepreneur. L'écart entre ces résidus ne doit résulter que d'une erreur de pointé acceptable.

La tolérance applicable à cet écart est fixée à 0,015 x E (en centimètres).

###### c° Cas particuliers

230

Pour les feuilles comportant des exclus de remembrement, il convient d’utiliser comme points
de calage des points issus du remembrement se trouvant en périphérie de la zone exclue et d’appliquer une transformation conforme.

Les agrandissements en marge sont, eux, intégrés en utilisant comme points de calage des
points situés en périphérie de la zone origine. L’ajustement est réalisé à l’aide d’une transformation conforme.

###### 2° Le contrôle des points vectorisés

240

La vérification s’appuie sur un pointé de contrôle des points vectorisés. Pour chaque
feuille vectorisée, les partenaires associés sont tenus de fournir un fichier texte au format NXY comprenant, pour chaque feuille vectorisée, l’ensemble des points caractéristiques (nœuds selon la
terminologie EDIGéO), et indiquant pour chacun d’eux son numéro et ses coordonnées dans la base.

Les fichiers texte seront sous la forme NNNNN XXXXXXX.XX YYYYYYY.YY, avec :

- NNNNN : numéro du point ;

- XXXXXXX.XX : coordonnée en abscisse ;

- YYYYYYY.YY : coordonnée en ordonnée.

Le nombre de points servant à la vérification de la vectorisation sera fonction de la
densité et du morcellement de chaque feuille :

- dans le cas de feuilles à forte densité ou à coefficient de morcellement élevé, la
vérification s’appuiera sur un pointé de contrôle à raison de 100 points environ par feuille ;

- dans les autres cas, le vérificateur appréciera le nombre de points à contrôler dans une
fourchette de 50 à 100 points.

Pour chaque point de contrôle, les coordonnées des points issus du pointé du vérificateur
sont comparées aux coordonnées des points du fichier transmis par les partenaires associés, et le résidu en position est calculé. La proportion d’écarts hors tolérance ne doit pas dépasser 4 % par
feuille.

Si cette condition est satisfaite, la moyenne quadratique des écarts individuels inférieurs
ou égaux à la tolérance est calculée et comparée à la tolérance adaptée

##### c. Rapport de vérification et attribution du label

250

Si tous les contrôles effectués s’avèrent concluants, un label de conformité au plan
cadastral est attribué au document vérifié.

Dans le cas contraire, l’agent chargé du visa doit tenter d’analyser les facteurs qui ont pu
provoquer les discordances constatées. Il convient en effet, en concertation avec les responsables de la vectorisation, de rechercher la solution à mettre en œuvre afin de remédier aux défauts
constatés si ceux-ci proviennent, par exemple:

- d’une déformation de son support (PMC ou fichier d’images) ;

- d’une identification erronée des points de calage sur le plan cadastral.

En revanche, s’il s’avère que les écarts relevés sont imputables aux seules carences du
processus de vectorisation établi par le prestataire, le label de conformité sera refusé.

Les constatations faites en cours de vérification sont relatées dans un rapport dont la
conclusion doit faire état, soit de l’attribution sans condition, soit de l’attribution sous réserve de rectification des anomalies ponctuelles, soit du refus du label de conformité au plan cadastral.

Les tableaux de vérification du calage des feuilles carroyées joints au
BOI-ANNX-000395 présentent les formules à appliquer et les tolérances associés.

### C. La vérification de la structuration

260

La vérification de la conformité des données numériques livrées par les partenaires au
standard d’échange prévu par la convention, réalisée par le service de la documentation nationale du cadastre (SDNC), permet de s’assurer que les données fournies pourront être intégrées sans
difficulté dans l’application PCI-Vecteur.

Ce contrôle est obligatoirement opéré pour vérifier la qualité des fichiers de la première
commune fournie par les partenaires à chaque nouvelle convention signée, et peut être utilement mis en œuvre pour toute autre commune, si le service le juge opportun, notamment en cas de changement de
prestataires ou de problèmes récurrents sur la qualité des données.

Pour les autres communes, la conformité des données numériques livrées au standard d'échange
est vérifiée par les services du cadastre au cours de la montée en charge des données dans PCI-Vecteur.

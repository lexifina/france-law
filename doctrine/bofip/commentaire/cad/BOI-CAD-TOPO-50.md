# CAD – Travaux topographiques du cadastre - Le géoréférencement du plan cadastral

- Identifiant : BOI-CAD-TOPO-50-20120912
- Publié le : 2012-09-12
- Type : Commentaire
- Série : CAD, TOPO
- Bureau : DGFIP
- Page officielle : https://bofip.impots.gouv.fr/bofip/5193-PGP.html/identifiant=BOI-CAD-TOPO-50-20120912
- Directeur de publication : Bruno Bézard, directeur général des finances publiques
- Références : Contenu:5101-PGP, Contenu:5195-PGP, Contenu:5215-PGP, Contenu:5282-PGP

## Texte

CAD – Travaux topographiques du cadastre - Le géoréférencement du plan cadastral

## I. Généralités

1

Le plan cadastral est entièrement dématérialisé pour être consultable sur le site internet
www.cadastre.gouv.fr. Cette dématérialisation a été réalisée sous deux formes : la forme image ou la forme vecteur.

10

Le plan cadastral « vecteur » est obtenu soit par réfection du plan dans le cadre de travaux de
remaniement, soit par vectorisation du plan image en régie ou dans le cadre d'une convention (cf. BOI-CAD-INFO-10 relatif à l'informatisation du plan cadastral).

20

Le passage du plan image au plan vecteur doit permettre à l'utilisateur final de connaître les
coordonnées de tout point du plan dans le système de projection légal. Pour réaliser cet objectif, les services du cadastre doivent disposer de fichiers de géoréférencement ou bien « équiper » les
feuilles à vectoriser de points connus en coordonnées. Ces travaux sont appelés travaux de géoréférencement du plan cadastral.

## II. Le géoréférencement réalisé en régie

### A. Plans rénovés par voie de renouvellement, par réfection, remaniés, remembrés ou aménagés, dans un système ancien de
coordonnées

Lors de leur confection, ces plans ont été rattachés au système de projection légal de l'époque
et, possèdent donc un système de repérage de coordonnées appelé carroyage. Par exemple, en métropole ce carroyage peut être défini dans l'ancien système de coordonnées appelé Lambert zones. C'est ce
carroyage qui fournit les points de calage nécessaires au géoréférencement de la feuille de plan.

30

Le géoréférencement de ce type de feuille de plan consiste à reprojeter le carroyage présent sur
la feuille dans le système de projection légal souhaité.

40

Ainsi, après s'être assuré de la bonne qualité du carroyage, le géoréférencement de chaque
feuille de plan est obtenu après les deux opérations suivantes :

- la production du fichier de géoréférencement (dans le système ancien de coordonnées) de la
feuille à l'aide d'une fonctionnalité de l'application PCI image ;

- la reprojection du fichier de géoréférencement qui précède dans le système de projection
légal. Cette reprojection est réalisée à l'aide d'un logiciel d'initiative locale validé par l'administration.

Les fichiers de géoréférencement reprojetés sont les fichiers à utiliser lors des travaux de
vectorisation du plan.

50

Le fichier de géoréférencement d'une feuille de plan, appelé aussi « fichier de
géoréférencement de type PCI image », est un fichier texte contenant les coordonnées des quatre coins du fichier Tiff de la feuille dans le système « pixel » et dans le système de projection légal,
ainsi que les paramètres arrondis de la transformation mathématique de géoréférencement.

### B. Plans rénovés par voie de mise à jour ou de renouvellement en coordonnées indépendantes

#### 1. Principe

Les feuilles de plan rénovées par voie de mise à jour ou renouvelées dans un système de
coordonnées indépendant (ou dans un système autre qu'un ancien système légal de référence) ne possèdent pas de carroyage exploitable.

60

Le géoréférencement de ces feuilles de plan consiste à les équiper d'un certain nombre de
points de calage connus en coordonnées pour produire un fichier de géoréférencement pour chacune des feuilles. Ces points de calage pourraient être déterminés de manière indépendante pour chaque
feuille de plan, ce qui entrainerait des travaux topographiques très importants et produirait un géoréférencement « absolu » de qualité au détriment du géoréférencement « relatif » des feuilles entre
elles.

70

En régie, la DGFiP privilégie le géoréférencement relatif des feuilles entre elles au moyen
d'un calcul mathématique en bloc par les moindres carrés. Cette méthode facilite la résorption des discordances de raccord entre feuilles.

80

Les feuilles de plan à géoréférencer doivent former un bloc homogène (feuilles de la même
commune, de même qualité et d'échelle voisine).

Des points d'appui connus en coordonnées (dans le système de coordonnées cible) en périphérie
et à l'intérieur du bloc permettent de géoréférencer le bloc et des points de liaison entre feuilles permettent d'assembler les feuilles du bloc.

90

Ces points d'appui sont déterminés soit par des travaux topographiques (détermination des
coordonnées de ces points à l'aide d'un lever) soit par des travaux de bureau en utilisant des orthophotographies dont la précision est satisfaisante ou à partir des coordonnées de carroyage (dont on
aura préalablement contrôlé la qualité) présents sur des feuilles en périphérie ou à l'intérieur du bloc.

#### 2. Mise en œuvre

Le géoréférencement d’un bloc de feuilles de plans se déroule en trois grandes étapes.

100

Dans un premier temps, au bureau, un bloc cohérent est défini en assemblant les feuilles à
géoréférencer et éventuellement des feuilles déjà géoréférencées à l'aide d'un logiciel validé par l'administration. L'assemblage des feuilles est réalisé en repérant des points communs entre deux ou
plusieurs feuilles, appelés points de liaison.

110

Dans un second temps, un certain nombre de points d’appui répartis au mieux en tenant compte
de la qualité des liaisons entre feuilles sont choisis. Selon le tissu, l'utilisation d'une carte au 1/25 000 ainsi que la consultation d'orthophotographies permettra de confirmer ou non la
subsistance de lieux du plan cadastral pressentis comme points d'appuis potentiels sur le terrain.

Les points d’appui sont déterminés par des travaux topographiques sur le terrain (Cf.
BOI-CADTOPO-10 relatif au canevas)ou à partir d'orthophotographies. Les croisées de carroyage de feuilles voisines du bloc possédant un carroyage peuvent aussi être
retenues comme points d'appui.

La classe de précision planimétrique totale attendue pour les points d'appui de
géoréférencement est de [60 cm] (Cf. BOI-CAD-TOPO-60 relatif à la vérification des travaux topographiques).

120

Les orthophotographies utilisées le cas échéant doivent permettre de déterminer des points
d'appui dont la classe de précision planimétrique totale est égale à [60 cm]. C'est pourquoi, il convient de n'utiliser que des orthophotographies de haute résolution dont la précision topographique
est connue et pour lesquelles :

résolution pixel de l'image + classe de précision planimétrique ≤ 60 cm

130

Enfin, à l'aide du logiciel approprié, différentes simulations de calcul en bloc sont
réalisées. Le calcul retenu sera celui dans lequel les résidus sur les points de liaison seront les plus faibles tout en conservant une répartition homogène de points d'appui.

Une fois le calcul validé, les fichiers de géoréférencement sont générés pour chacune des
feuilles.

#### 3. Fichiers de géoréférencement de l'IGN

Dans le cadre de la mise à jour du référentiel à grande échelle (RGE) et plus particulièrement
de la mise à jour de la composante parcellaire de ce référentiel appelée « base de données parcellaire », l'Institut national de l'information géographique et forestière (IGN) et la DGFIP ont signé
une convention d'échange de données.

140

Dans ce cadre, la DGFIP peut disposer des fichiers de géoréférencement des feuilles du plan
cadastral non connues en coordonnées produits par l'IGN.

Les directions départementales des finances publiques commandent ces fichiers auprès de
l'administration centrale (bureau du cadastre).

Ces fichiers doivent impérativement faire l'objet d'un contrôle conformément aux prescriptions
de la Cf. BOI-CAD-TOPO-60 relatif à la vérification des travaux topographiques

Remarque :

Dans la mesure où le service du cadastre transmet ces fichiers de géoréférencement à un
prestataire chargé de la vectorisation du plan cadastral, il convient de s'assurer que ce dernier n'utilisera que les coordonnées des points d'appui indiqués dans chaque fichier (les 4 angles du
fichier Tiff de la feuille de plan) et non les paramètres de la transformation figurant en dessous, qui sont arrondis et transmis uniquement pour information.

## III. Géoréférencement confié à l'entreprise

150

Pour faire face aux calendriers des opérations de vectorisation et à l'accroissement des
demandes de nouvelles conventions, la DGFiP peut proposer aux partenaires des conventions de prendre à leur charge les travaux de géoréférencement, moyennant une obligation de résultats en termes de
précision.

Conformément à l'esprit de
l'arrêté du 16 septembre 2003 relatif aux classe
de précision des levers topographiques, aucune méthodologie ne doit être imposée au prestataire chargé des travaux qui a seulement une obligation de résultats. Néanmoins, il devra se conformer aux
prescriptions figurant dans le Cahier des Clauses Techniques Particulières joint au BOI-ANNX-000394.

### A. Dossier remis au prestataire

Le service du cadastre dont dépend la commune à traiter remettra sur cédérom les images des
feuilles cadastrales à géoréférencer.

Ces images ont les caractéristiques suivantes :

- une image par feuille ;

- résolution de 300 dpi ;

- format de l’image scannée pouvant varier en fonction de la caméra utilisée lors du scannage
de la feuille (parmi 4 caméras). Le format est proche de 12 350 pixels x 8 860 pixels ;

- compression en CCITT Groupe 4 monolithique BPS, extension « .TIFF ».

### B. Travaux réalisés par le prestataire

160

A partir d’une base de données géographiques (points GPS, orthophotographies, etc.) le
prestataire géoréférence les images des feuilles cadastrales. Cette base de données géographiques servant d’appui au géoréférencement doit être homogène en précision sur l’ensemble de la commune.

170

Le système de coordonnées de la base de données utilisée pour géoréférencer les feuilles
cadastrales doit être conforme au système national de référence de coordonnées géographiques, planimétriques et altimétriques cité dans le
décret n°2000-1276 du 26 décembre 2000 relatif aux
conditions d’exécution et de publication des levés de plans entrepris par les services publics et modifié par le
décret n°2006-272 du 3 mars 2006.

180

Ce géoréférencement consiste à fournir et à annoter, pour chaque feuille initialement remise
par le service du cadastre, un minimum de 8 points répartis de façon homogène sur le périmètre de la feuille et de 2 points à l’intérieur de celle-ci.

190

Les points choisis doivent être significatifs et sans ambiguïté. Ils ne doivent prêter à
aucune confusion et doivent, bien sûr, être reproduits de façon identique sur chaque feuille où ils se trouvent (par exemple : sommets de bâtiments, sommets de limites parcellaires, etc.).Ils doivent
être identifiables sur le terrain dans toute la mesure du possible, et en tout état de cause clairement pour 50 % d’entre eux. Cette contrainte résulte de la méthode retenue pour la vérification à
savoir un nouveau calcul par procédés satellitaires des coordonnées d’un échantillon représentatif de points.

### C. Dossier remis par le prestataire

200

Le prestataire chargé des travaux remettra au service du cadastre un dossier
composé des pièces suivantes :

- le cédérom initialement transmis par le service du cadastre ;

- un cédérom contenant les fichiers d’images des feuilles cadastrales annotées des points
d’appui (symbole et numéro) permettant la numérisation et le géoréférencement de la feuille. Il est précisé qu'à aucun moment l'image du plan cadastral ne doit être ré-échantillonnée ;

- un fichier « NXY » au format texte reprenant l’ensemble des points déterminés sur la commune
avec leurs coordonnées, pour la métropole, en Lambert 93 ou Conique Conforme 9 zones selon le système de projection retenu. Ce fichier comprend une première ligne de texte contenant le nom de la
commune puis la liste des points (un point par ligne) sous la forme NséparateurXséparateurY ;

- un tirage sur papier au format A0 de chaque feuille annotée ;

- un dossier technique décrivant la méthodologie employée pour le géoréférencement et les
caractéristiques de la base de données géographiques éventuellement utilisée pour l’opération.

Le service du cadastre contrôlera les travaux réalisés conformément aux prescriptions en la
matière du BOI-CAD-TOPO-60 relatif à la vérification des travaux topographiques

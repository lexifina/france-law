# ANNEXE - CAD - Cahier des Clauses Techniques Particulières relatives à l'externalisation du géoréférencement du plan cadastral

- Identifiant : BOI-ANNX-000394-20130617
- Publié le : 2013-06-17
- Type : Autres annexes
- Série : CAD, CAD
- Bureau : DGFIP
- Page officielle : https://bofip.impots.gouv.fr/bofip/5282-PGP.html/identifiant=BOI-ANNX-000394-20130617
- Directeur de publication : Bruno Bézard, directeur général des finances publiques

## Texte

ANNEXE - CAD - Cahier des Clauses Techniques Particulières relatives à l'externalisation du géoréférencement du plan cadastral

## I. Généralités

La numérisation d’une feuille de plan nécessite la connaissance d’un nombre suffisant de points
connus en coordonnées pour la métropole, dans le système de projection de référence (Lambert 93 ou Coniques conformes 9 zones), correctement répartis sur la périphérie ainsi qu’à l’intérieur de la
feuille.

Pour les plans réalisés par réfection, remaniement, renouvellement ou aménagement foncier, ce
problème est résolu dans la très grande majorité des cas, car chaque feuille possède des croisées de carroyage ou des points dont on connaît les coordonnées. Si le carroyage est connu dans l’ancien
système de coordonnées Lambert zones alors, il sera nécessaire de procéder à des transformations pour pouvoir fournir aux partenaires chargé de la vectorisation du plan, les coordonnées des points de
calage dans le système de projection souhaité. Pour effectuer ces transformations, le logiciel "Circé", téléchargeable gratuitement sur le site internet de l'Institut géographique national qui permet
de transformer des coordonnées Lambert zones en coordonnées Lambert 93 ou Coniques conformes 9 zones (CC 9 zones), sera utilisé.

Les plans rénovés par voie de mise à jour ne répondent en revanche pas à cette exigence, et il
convient de rattacher les feuilles de plan non carroyées au système de coordonnées retenu : Lambert 93 ou CC 9 zones.

Pour une bonne numérisation, il faut que les feuilles de plan cadastral à équiper de points le
soient à partir d’une base de données homogène connue dans la projection retenue (Lambert 93 ou CC 9 zones) et définie à partir du système national de référence géodésique RGF93.

## II. Dossier remis au prestataire

Le service du cadastre dont dépend la commune à traiter remettra sur cédérom les images des
planches cadastrales à géoréférencer.

Ces images ont les caractéristiques suivantes :

- une image par feuille ;

- scannage natif en 256 niveaux de gris ramené automatiquement à 16 niveaux de gris, puis
transformation des images en fichiers binaires en noir et blanc obtenus par partage automatique sur la gamme des 16 niveaux de gris ;

- résolution de 300 dpi ;

- format de l’image scannée pouvant varier en fonction de la caméra utilisée lors du scannage
de la feuille (parmi 4 caméras). Le format est proche de 12 350 pixels x 8 860 pixels ;

- compression en CCITT Groupe 4 monolithique BPS, extension ".TIFF" ;

- taille moyenne de 250 Ko.

## III. Travaux réalisés par le prestataire

A partir d’une base de données géographiques (points GNSS, orthophotographies, etc.) le
prestataire géoréférencera les images des feuilles cadastrales.

Cette base de données géographiques servant d’appui au géoréférencement doit être homogène en
précision sur l’ensemble de la commune.

Le système de coordonnées de la base de données utilisée pour géoréférencer les feuilles
cadastrales doit être conforme au système national de référence de coordonnées géographiques, planimétriques et altimétriques cité à
l’article
1er du décret n° 2000-1276 du 26 décembre 2000 modifié par le
décret n° 2006-272 du 3 mars
2006.

Ce géoréférencement consistera à fournir et à annoter, pour chaque feuille initialement remise
par le service du cadastre, un minimum de 8 points répartis de façon homogène sur le périmètre de la feuille et de 2 points à l’intérieur de celle-ci.

Les points choisis doivent être significatifs et sans ambiguïté. Ils ne doivent prêter à
aucune confusion et doivent, bien sûr, être reproduits de façon identique sur chaque feuille où ils se trouvent (par exemple : sommets de bâtiments, sommets de limites parcellaires, etc.).

Ils doivent être identifiables sur le terrain dans toute la mesure du possible, et en tout
état de cause clairement pour 50 % d’entre eux. Cette contrainte résulte de la méthode retenue pour la vérification, à savoir un nouveau calcul par procédés satellitaires des coordonnées d’un
échantillon représentatif de points.

En outre, les classes de précision, et par suite les tolérances associées, étant fonction de
l’échelle du plan, et compte tenu de l’hétérogénéité possible des plans cadastraux sur une même commune (coexistence d’échelles et de modes de confection différents), les points identifiables, et par
suite vérifiables, devront être convenablement répartis dans chaque zone infra-communale homogène (lots de feuilles à la même échelle).

Les points seront numérotés de 1 à 9999 par commune et seront déterminés dans le système de
coordonnées retenu (Lambert 93 ou CC 9 zones) à partir du système national de référence géodésique RGF93.

Ces points sont matérialisés sur l’image du plan minute de conservation (ou sur son
impression). Le repérage est facilité par un cercle dessiné autour du point accompagné de son numéro d’identification.

Cas particulier : calage des feuilles comportant des agrandissements en marge.

Les agrandissements en marge sont intégrés lors de la numérisation du plan en utilisant comme
points d’appui, des points graphiques nets situés à la fois en périphérie de la zone d’origine et de la zone agrandie. Il n’y a pas lieu de considérer que ces agrandissements présentent une précision
supérieure au reste de la feuille : la classe de précision est celle de la feuille principale. L’adaptation est réalisée à l’aide d’une transformation conforme.

Les situations résiduelles seront ensuite examinées en liaison avec le service territorial en
charge du plan cadastral.

## IV. Dossier remis par le prestataire

Le prestataire chargé des travaux remettra au service du cadastre un dossier composé des
pièces suivantes :

- le cédérom initialement transmis par le service du cadastre ;

- un cédérom contenant les fichiers d’images des feuilles cadastrales annotées des points
d’appui (symbole et numéro) permettant la numérisation et le géoréférencement de la feuille. Il est précisé qu’à aucun moment l’image du plan cadastral ne doit être rééchantillonnée ;

- un fichier "NXY" au format texte reprenant l’ensemble des points déterminés sur la commune
avec leurs coordonnées, en métropole, en Lambert 93 ou CC 9 zones selon le système de projection retenu. Ce fichier comprendra une première ligne de texte contenant le nom de la commune puis la liste
des points (un point par ligne) sous la forme NséparateurXséparateurY ;

- un tirage sur papier au format A0 de chaque feuille annotée ;

- un dossier technique décrivant :

- la méthodologie employée pour le géoréférencement,

- les caractéristiques de la base de données géographiques utilisée pour l’opération.

## V. Vérification du rattachement

Le prestataire est soumis à une obligation de résultat. C’est pourquoi les travaux seront
contrôlés par la Direction générale des finances publiques (DGFiP). Le texte de référence utilisé est
l'arrêté du 16 septembre
2003, portant sur les classes de précision applicables aux catégories de travaux topographiques réalisés par l'État et par les collectivités locales, ou pour leur compte.

Ce contrôle portera, en la forme, sur le dossier remis par l’entrepreneur, et, quant au fond,
sur la qualité des résultats obtenus.

Les résultats obtenus seront contrôlés par échantillonnage sur le territoire communal que le
prestataire aura géoréférencé. Le contrôle consistera à déterminer à nouveau en coordonnées Lambert 93 ou CC 9 zones à partir du système de référence géographique RGF93, par procédés satellitaires, un
échantillon d’au moins 10 % du nombre total de points fournis par le prestataire par lot de feuilles de même échelle. Ces points de contrôle seront choisis par la DGFiP parmi les points clairement
identifiables sur le terrain. Les écarts obtenus permettront de déterminer si l’ensemble des points localisés par le prestataire appartiennent à la classe de précision souhaitée.

Le vérificateur détermine par procédés satellitaires (GPS) les points d’appui fournis par le
prestataire.

Pour chaque lot de feuilles de même échelle, la vérification sera réalisée par échantillonnage
selon la classe de précision planimétrique [xx] cm avec un coefficient de sécurité C égal à 2.

La classe de précision est donnée par la relation : [xx] = cm

où E représente l'échelle du lot de plans à géoréférencer (par exemple E=1/1 250).

La classe de précision [xx] obtenue sera arrondie à la dizaine de centimètres supérieure.

Le tableau ci-après reprend les classes de précision ainsi obtenues selon l’échelle du plan :

Échelle du plan

Classe de précision à retenir (cm)

1/6 25

140

1/1 000

230

1/1 250

280

1/2 000

450

1/2 500

560

1/4 000

890

1/5 000

1120

1/8 000

1780

Classes de précision selon l’échelle du plan

Pour tout échantillon comptant N points, on calcule l'écart moyen en position
Emoy pos. Celui-ci est défini par la moyenne arithmétique des écarts en position Epos relevés sur les points. On dit que la population dont est issu l'échantillon comptant N
points est de classe de précision [XX] cm lorsque simultanément les trois conditions a/ b/ et c/ sont remplies :

a/ l'écart moyen en position Emoy pos de l'échantillon est
inférieur à [XX] x (1+1/(2xC2)) cm où C est le coefficient de sécurité des mesures de contrôle ;

b/ le nombre N’ d'écarts dépassant le premier seuil T = k x [XX] x (1+1/(2xC2)) cm,
n'excède pas l'entier immédiatement supérieur à : 0,01 x N + 0,232 x √N où k prend les valeurs indiquées dans la table 1 en fonction du nombre n de coordonnées caractérisant la position des objets
géographiques, et suivant la même loi statistique.

n

1

2

3

k

3,23

2,42

2,11

Table 1

Pour les travaux cadastraux, n est égal à 2 et par conséquent, il faut retenir la
valeur 2,42 pour le coefficient k.

Lorsque N < 5, aucun écart supérieur à T n'est admis (cf. table 2 ci-dessous).

N

de 1 à 4

5 à 13

14 à 44

45 à 85

86 à 132

133 à 184

185 à 240

241 à 298

299 à 359

360 à 422

423 à 487

N'

0

1

2

3

4

5

6

7

8

9

10

Table 2

c) Le second seuil ne doit pas être dépassé :

Aucun écart en position dans l'échantillon n'excède le second seuil T = 1,5 x k x [XX] x (1+1/(2xC2)) cm.

Exemple : Pour un lot de planches au 1/2 500 dont l’échantillon de
vérification comporte 100 points, cet échantillon doit être de classe [560] cm. Pour cela, les trois conditions suivantes doivent être simultanément remplies avec C = 2 et k = 2,42 :

- l’écart moyen en position (moyenne arithmétique des écarts en position) de l’échantillon doit
être inférieur à 6,30 m ;

- le nombre d’écarts dépassant le premier seuil T = 15,25 m doit être inférieur ou égal à 4 ;

- aucun écart en position de l’échantillon n’excède le second seuil T= 22,87 m.

Toute difficulté d’interprétation devra être soumise à l’examen du service
du cadastre territorialement compétent.

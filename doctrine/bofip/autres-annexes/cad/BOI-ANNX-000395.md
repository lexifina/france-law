# ANNEXE - CAD - Vérification du calage des feuilles carroyées

- Identifiant : BOI-ANNX-000395-20130617
- Publié le : 2013-06-17
- Type : Autres annexes
- Série : CAD, CAD
- Bureau : DGFIP
- Page officielle : https://bofip.impots.gouv.fr/bofip/5294-PGP.html/identifiant=BOI-ANNX-000395-20130617
- Directeur de publication : Bruno Bézard, directeur général des finances publiques
- Références : Image:5292-PGP, Image:5293-PGP, Image:5734-PGP

## Texte

ANNEXE - CAD - Vérification du calage des feuilles carroyées

Nature de l’opération

Formules à appliquer

Tolérance associée

Feuilles carroyées

Calage sur les mêmes croisées de carroyage que le prestataire

- Xp (xp ; yp) : croisée de carroyage de coordonnées (xp ; yp) dans le système de référence en vigueur (Lambert 93, CC 9
zones, ou système en vigueur en DOM)1

- Xd (xd ; yd) : point résultant de la numérisation de coordonnées (xd ; yd) dans le système du prestataire

- Xt (xt ; yt) : point résultant de la numérisation de coordonnées (xt ; yt) dans le système de référence en vigueur

Les coordonnées (xt ; yt) s’obtiennent à partir des paramètres de la transformation (a, b, p, q) :

xt = p + a x xd - b x yd

yt = q + b x xd + a x yd

Calcul des écarts individuels en x et y

eix = xt - xp

eiy = yt - yp

Calcul des écarts individuels en position (résidu)

ep = √eix2 + eiy2

T (cm) = 0,04 x E, où E est le facteur d’échelle du plan

Exemple : 40 cm pour un plan au 1/1000

Calcul de la précision de la transformation

, où n est le nombre d’écarts individuels en position

Pas de tolérance

Nature de l’opération

Formules à appliquer

Tolérance associée

Feuilles non carroyées

Calage sur les mêmes points de calage que le prestataire

- Xp (xp ; yp) : point de calage de coordonnées (xp ; yp) dans le système de référence en vigueur (Lambert93, CC 9 zones,
ou système en vigueur en DOM)

- Xd (xd ; yd) : point résultant de la numérisation de coordonnées (xd ; yd) dans le système du prestataire

- Xt (xt ; yt) : point résultant de la numérisation de coordonnées (xt ; yt) dans le système de référence en vigueur.

Les coordonnées (xt ; yt) s’obtiennent à partir des paramètres de la transformation (a, b, p, q) :

xt = p + a x xd – b x yd

yt = q + b x xd + a x yd

Calcul des écarts individuels en x et y

eix = xt – xp

eiy = yt – yp

Calcul des écarts entre les résidus obtenus par le vérificateur et les résidus obtenus par le prestataire

e = ep(prestataire) – ep(vérificateur)

T (cm) = 0,015 x E, où E est le facteur d’échelle du plan.

Exemple : 15 cm pour un plan au 1/1000.

Calcul de la précision de la transformation

EMQ non significative

Vérification du calage des feuilles non carroyées

Nature de l’opération

Formules à appliquer

Tolérance associée

Pointé de contrôle

- Xc (xc ; yc) : point de contrôle issu du pointé du vérificateur

- nXb (xb ; yb) : point homologue dans le fichier du prestataire

Calcul des écarts individuels en position

ep = √(xb – xc)2 + (yb - yc)2

T (cm) = 0,03 x E, où E est le facteur d’échelle du plan

Exemple : 30 cm pour un plan au 1/1000

La proportion d’écarts hors tolérance ne doit pas dépasser 4% par feuille

Calcul de la moyenne quadratique des écarts individuels en position

, où n est le nombre des résidus inférieurs ou égaux à la tolérance

Vérification de la qualité des points numérisés

Nouveau dispositif de vérification de la numérisation des plans cadastraux

Contrôle de la précision

Nombre de feuilles vérifiées

Le processus de vérification est dégressif et différencié :

- 1 commune à numériser : au moins 25% des feuilles

- plusieurs communes à numériser : au moins 25% des feuilles pour la commune comportant le plus grand nombre de planches
cadastrales et au moins 10% pour chaque commune suivante

Choix des feuilles à vérifier

Échantillon représentatif des différents types de plans de la commune (mode de confection, densité du bâti, morcellement
parcellaire)

Contrôle de la digitalisation

Le processus de vérification de la digitalisation est différencié :

- feuilles à forte densité ou à coefficient de morcellement élevé : 100 points de contrôle par feuille

- autres cas : de 50 à 100 points de contrôle par feuille

Contrôle

de

l'exhaustivité

Nombre de feuilles vérifiées

Le processus de vérification est dégressif et différencié :

- contrôle systématique de 50 % des feuilles, choisies parmi les feuilles à forte densité

- autres feuilles : en fonction des résultats du premier contrôle :

- si la numérisation est de qualité : contrôle allégé

- si la numérisation présente un grand nombre d’anomalies : rejet

Principes d'échantillonnage des feuilles pour la vérification

1. Les coordonnées des croisées de carroyage, connues en Lambert zones, seront
reprojetées dans le système de projection légal grâce au logiciel "Circé", téléchargeable gratuitement sur le site internet de l'IGN qui permet de transformer des coordonnées "Lambert zones" en
coordonnées "Lambert 93" ou "CC 9 zones", ou au logiciel interne "Géo3D" téléchargeable sur l’intranet Pl@net du CSI d’Angers.

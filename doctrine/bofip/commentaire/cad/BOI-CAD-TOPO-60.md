# CAD - Travaux topographiques du cadastre - La vérification des travaux topographiques

- Identifiant : BOI-CAD-TOPO-60-20170503
- Publié le : 2017-05-03
- Type : Commentaire
- Série : CAD, TOPO
- Bureau : DGFIP
- Page officielle : https://bofip.impots.gouv.fr/bofip/5195-PGP.html/identifiant=BOI-CAD-TOPO-60-20170503
- Directeur de publication : Bruno Parent, directeur général des finances publiques
- Références : Contenu:5101-PGP, Contenu:5193-PGP, Contenu:5260-PGP, Contenu:5275-PGP, Contenu:5312-PGP, Image:6017-PGP, Fichier:7490-PGP, Fichier:7491-PGP

## Texte

CAD - Travaux topographiques du cadastre - La vérification des travaux topographiques

## I. Le contexte réglementaire

1

L'arrêté du 16 septembre 2003 et sa
circulaire portent sur les classes de précision
applicables aux travaux topographiques réalisés par l'État, les collectivités locales et leurs établissements publics ou exécutés pour leur compte. Il remplace
l'arrêté du 21 janvier 1980 relatif aux tolérances applicables en matière de travaux topographiques.

10

Tous les travaux topographiques doivent être spécifiés et évalués selon les modalités définies
dans l'arrêté du 16 septembre 2003.

Une exception : les aménagements fonciers agricoles et forestiers dont le marché public a été
conclu avant cette date seront évalués conformément aux prescriptions de l'arrêté du 21 janvier 1980.

La réglementation actuelle concerne l'ensemble des travaux topographiques de la Direction
générale des finances publiques (DGFiP) : les canevas, la confection de plans neufs (remaniement, aménagement foncier agricole et forestier) et le géoréférencement du plan cadastral.

Il permet au donneur d'ordre de spécifier la précision souhaitée, indépendamment des moyens mis
en œuvre et met en place les modalités de son contrôle.

20

Le principe général consiste en un contrôle des écarts en position sur des points
caractéristiques, des objets levés, identifiés, ne présentant aucun caractère d’ambiguïté et déterminés par le donneur d'ordre avec des moyens de précision au moins égale à deux fois celle prévue dans
le contrat.

Les écarts en position sont analysés à la lumière du modèle statistique standard ou à l'aide
d'un gabarit d'erreurs spécifiques défini dans le contrat.

## II. Les classes de précision

### A. Les différentes erreurs

#### 1. L'erreur interne

30

L'erreur interne correspond à la cohérence des mesures entre elles, en dehors de toute
imprécision due au rattachement au système de référence.

Elle s'analyse à partir de l'écart entre les coordonnées obtenues pour chaque point par les
mesures de contrôle et celles que l'on obtient par calcul dans un système indépendant en appliquant la translation (et pour 2 ou 3 coordonnées, une rotation) la plus favorable possible, sur l’ensemble
des coordonnées fournies pour ces points. Les éventuels points d’appui inclus dans le canevas figurent avec leurs coordonnées déterminées dans le système indépendant.

#### 2. L'erreur propre au réseau légal de référence

40

L'erreur propre au réseau légal de référence correspond à l'imprécision des points du réseau
servant au rattachement au système légal.

Elle est spécifiée par l'Institut national de l'information géographique et forestière (IGN),
avec éventuellement plusieurs niveaux possibles en fonction des éléments du réseau effectivement utilisés lors du rattachement. Si la discordance relevée entre les points du réseau légal de référence
est plus importante que la précision spécifiée par le gestionnaire, alors la précision est remplacée dans toutes les évaluations ultérieures par la discordance de rattachement effectivement constatée.

#### 3. L'erreur de rattachement

50

L'erreur de rattachement s'analyse, lorsque cela est possible, à partir des écarts sur les
mesures permettant le lien entre le réseau légal de référence et le canevas lui-même. Un rattachement ne peut être considéré comme effectué que si le canevas considéré est rattaché à suffisamment de
points du réseau légal de référence pour mettre en évidence d'éventuelles discordances dans ce réseau. En outre, la précision fournie pour le rattachement doit être cohérente avec celle des éléments
du réseau légal de référence effectivement utilisés pour celui-ci.

### B. Les classes de précision

#### 1. La classe de précision interne

60

La classe de précision interne est associée à l'erreur interne.

Elle s’applique à l'écart entre les coordonnées obtenues pour chaque point par les mesures de
contrôle et celles que l'on obtient par calcul dans un système indépendant en appliquant la translation (et pour 2 ou 3 coordonnées, une rotation) la plus favorable possible, sur l’ensemble des
coordonnées fournies pour ces points. Les éventuels points d’appui inclus dans le canevas figurent avec leurs coordonnées déterminées dans le système indépendant.

#### 2. La classe de précision totale

65

La classe de précision totale, conçue pour être la plus communément employée s’applique aux
écarts entre les coordonnées fournies pour chaque point et celles que l'on obtient pour des mesures de contrôle acquises dans le système légal de référence.

L'erreur totale résulte de la composition des erreurs internes, des erreurs de rattachement,
et de l'erreur propre au réseau légal de référence. Elle est la composition quadratique des erreurs internes, de rattachement et de réseau.

Donc, l'erreur totale ne peut être inférieure à l'une de ces trois sources d'erreurs, et en
particulier à l'erreur propre du réseau légal de référence, telle qu'elle est spécifiée ou telle qu'elle résulte des discordances relevées lors du rattachement.

70

Si on appelle [yy] la classe de précision totale, [xx] la classe de précision interne, [vv] la
classe de précision du réseau légal, [ww] la classe de précision des mesures de rattachement et [zz] celle du rattachement du levé (avec [zz]² = [vv]² + [ww]²), alors ces classes de précision sont
liées par les relations :

[yy]² = [xx]² + [zz]²

[yy]² = [xx]² + [vv]² + [ww]²

### C. Vérification d'une classe de précision

73

L'article 5 de
l'arrêté du 16 septembre 2003 définit les
conditions à remplir pour valider une classe de précision selon le modèle standard.

Le principe est que sur un échantillon des points à contrôler, trois conditions cumulatives
doivent être remplies pour que cet échantillon soit d’une classe de précision [yy].

a) La première condition fait intervenir un écart moyen en position Emoypos. Il
correspond à la moyenne arithmétique des écarts en position Epos. Ces écarts en position représentent la distance euclidienne qui sépare un point avec des coordonnées prestataire du même
point avec des coordonnées contrôlées.

L'écart moyen en position Emoypos de l'échantillon doit être inférieur à :

[yy] x (1 + (2 x C2)-1) cm

C étant le coefficient de sécurité des mesures de contrôle.

Les deux autres conditions sont des seuils limites déduits de probabilités
statistiques.

b) Le premier seuil peut être dépassé mais par un nombre limité de points N'.

Le premier seuil est défini par :

T = k x [yy] x (1 + (2 x C2)-1) cm

N' ne doit pas excéder l'entier immédiatement supérieur à : 0,01 x N + 0,232 x
(N)1/2

(où k prend les valeurs indiquées dans la table 1 ci-dessous en fonction du
nombre n de coordonnées caractérisant la position des objets géographiques et suivant la même loi statistique).

Table 1 :

n

1

2

3

k

3,23

2,42

2,11

Table de valeurs 1

Lorsque n < 5, aucun écart supérieur à T n'est admis (cf.
table 2 ci-dessous).

Table 2 :

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

Table de valeurs 2

c) Le second seuil ne doit pas être dépassé.

Aucun écart en position dans l'échantillon ne doit excéder le second seuil défini
par :

T = 1,5 x k x [yy] x (1 + (2 x C2)-1) cm

## III. Les classes de précision à la DGFiP

### A. Le coefficient de sécurité

77

Les termes de l’article 3 de
l'arrêté du 16 septembre 2003 précisent qu'une
mesure n’est considérée comme mesure de contrôle que lorsque sont mis en œuvre des procédés fournissant une précision meilleure que celle de la classe de précision recherchée, avec un coefficient de
sécurité C au moins égal à 2. C est « le rapport entre la classe de précision des points à contrôler et celle des déterminations de contrôle, classe de précision qui est elle-même évaluée selon les
règles de l’Art ».

80

Ce coefficient C, « garantie » de la qualité du contrôle, a été fixé à 2 par la DGFiP pour
l'ensemble de ses travaux.

Ainsi, les moyens mis en œuvre pour la vérification doivent garantir une précision deux fois
supérieure à celle exigée pour la réalisation des travaux en respectant les règles de l'Art. C'est pourquoi, l'utilisation des matériels GNSS (Global National Satellite System) est préconisée et
notamment la méthode GNSS « post-traitement ».

### B. Dissociation de la planimétrie et de l'altimétrie

85

L'arrêté indique par ailleurs, que l'on ne comptabilise ensemble que les données suivant le
même modèle statistique selon la nature du lever.

Ainsi, le modèle altimétrique étant différent du modèle planimétrique, la DGFiP a défini des
classes de précision et des modalités de vérification des levers altimétriques et des levers planimétriques différentes.

90

Pour cette raison, la vérification de la stéréopréparation se fera en deux étapes et avec des
classes de précision différentes en planimétrie et altimétrie.

### C. Vérification d'une classe de précision

100

La classe de précision vérifiée par la DGFiP pour ses travaux techniques est toujours la
classe de précision totale.

#### 1. Choix de l'échantillon

103

Les points de contrôle sont choisis parmi des points caractéristiques, des objets levés,
identifiés, ne présentant aucun caractère d’ambiguïté en fonction :

- de leur mode de détermination initial et du risque d’imprécision sur chaque point ;

- du taux d’échantillonnage voulu ;

- du temps et des moyens dont on dispose.

En revanche, la méthode de contrôle ne dépend pas de la méthode de levé vérifiée. La méthode
de contrôle doit cependant permettre d'obtenir une classe de précision du levé de contrôle deux fois meilleure que la classe de précision vérifiée.

Le volume de l'échantillon de contrôle, retenu par la DGFiP, est spécifié ci-dessous pour
chaque type de travaux topographiques.

#### 2. Mise en œuvre du contrôle

107

La vérification est conduite à la lumière des prescriptions de l'article 5 de
l'arrêté du 16 septembre 2003, le modèle standard
ayant été choisi par la DGFiP pour la validation des classes de précision.

Cette vérification de classe de précision est réalisée avec le logiciel mis à disposition des
services du cadastre.

### D. Les classes de précision à la DGFiP

110

L'ensemble des valeurs figurants dans ce paragraphes sont des valeurs maximales en
centimètres. Pour un lever topographique, toute classe de précision inférieure ou égale à la classe de précision attendue pour le lever est acceptée.

#### 1. Les canevas

##### a. Les canevas planimétriques

111

Les différentes valeurs des classes de précision relatives aux différents types de canevas
sont récapitulées dans le tableau ci-après :

Type de canevas planimétrique

Classes de précision (en cm)

Interne

Réseau d'appui

Mesures de rattachement

Totale

Points pérennes d'une densification de réseau

3

0,5

3

4

Divers travaux spéciaux tels l'élaboration ou la vérification d'une base d'étalonnage

2

2

Canevas cadastral de précision

4

0,5

3

5

Canevas cadastral ordinaire

9

2

3

10

Canevas préalable à un aménagement foncier agricole et forestier (AFAF)

9

2

3

10

Canevas d'appui d'une prise de vues permettant la confection d'un plan de classe de précision [10] cm

4

0,5

3

5

Canevas d'appui d'une prise de vues permettant la confection d'un plan de classe de précision [20] cm

9

2

3

10

Tableau des différentes valeurs des classes de précision relatives aux différents types de canevas

##### b. Les canevas altimétriques

112

Les différentes valeurs des classes de précision relatives au canevas altimétrique sont
récapitulées dans le tableau ci-après :

Type de canevas altimétrique

Classes de précision (en cm)

Interne

Réseau d'appui

Mesures de rattachement

Totale

Canevas d'appui d'une prise de vues

7

3

4

9

Tableau des différentes valeurs des classes de précision relatives au canevas altimétrique

##### c. Les canevas d'appui de géoréférencement

113

Les différentes valeurs des classes de précision relatives au canevas d'appui pour des
travaux de géoréférencement sont récapitulées dans le tableau ci-après :

Type de canevas

Classes de précision (en cm)

Interne

Réseau d'appui

Mesures de rattachement

Totale

Canevas d'appui pour travaux de géoréférencement

40

14

40

60

Tableau des différentes valeurs des classes de précision relatives au canevas d'appui pour des travaux de géoréférencement

#### 2. Le lever de détails

115

Les différentes valeurs des classes de précision relatives au lever de détails sont
récapitulées dans le tableau ci-après :

Type de lever

Classes de précision (en cm)

Interne

Réseau d'appui

Mesures de rattachement

Totale

Lever de détails pour établir un plan de classe de précision [10] cm

8

5

5

10

Lever de détails pour établir un plan de classe de précision [20] cm

10

15

5

20

Tableau des différentes valeurs des classes de précision relatives au lever de détails

#### 3. La confection de plans cadastraux

117

L'arrêté du 21
janvier 1980 avait défini la notion de catégories de plans (P1, P2, P3, P4, etc.) en fonction de l'échelle et déterminé un coefficient Q correspondant à chaque catégorie.

L'article 6 de la
circulaire relative à la mise en œuvre de l'arrêté du
16 septembre 2003 a établi une correspondance entre le coefficient Q, la classe de précision totale approchée, l'échelle de constitution et la catégorie du plan.

Elle est rappelée dans le tableau ci-après :

Catégorie planimétrique

Échelle

Coefficient Q

Classe de précision

(en cm)

P3

1/500

10

10

P4

1/1 000 ou 1/2 000

20

20

P5

1/2 000 (AFAF)

40

40

Détail de la confection de plans cadastraux

Remarques :

Les plans d'aménagement foncier agricole et forestier à l'échelle du 1/2 000 dont le marché
public a été conclu antérieurement à la date de publication de la présente documentation (12 septembre 2012) sont considérés comme des plans de classe de précision [40] cm ou catégorie P5.

Les plans d'aménagement foncier agricole et forestier à l'échelle du 1/2 000 dont le marché
public a été conclu postérieurement à la date de publication de la présente documentation (12 septembre 2012) sont à confectionner comme des plans de classe de précision [20] cm ou catégorie P4.

## IV. La vérification des travaux topographiques

### A. Vérification d'un canevas

119

Pour la conduite des travaux de vérification de canevas, on peut distinguer deux types de
vérification :

- une vérification interne (avant rattachement au système légal de référence) ;

- une vérification totale (après rattachement).

120

Pour la vérification de travaux en régie, on privilégie la vérification de la classe de
précision totale, ce qui conduit à ne vérifier la classe de précision interne que lorsque la classe de précision totale s'avère insuffisante.

Pour les travaux de vérification réalisés pour des tiers, on se réfère aux prescriptions du
cahier des charges fourni par le donneur d'ordre.

130

Le contrôle des travaux passe par une analyse statistique à l'issue des opérations.
L'arrêté du 16 septembre 2003 impose, dans le
principe, d'effectuer un levé de vérification avec une précision meilleure que celle du levé vérifié. Le coefficient de sécurité étant égal à 2 pour les travaux réalisés par la DGFiP, ce principe
incite à privilégier les méthodes de levé GNSS (Global National Satellite System) les plus sûres (il convient de se référer au BOI-CAD-TOPO-10 relatif au canevas). Aussi,
pour tout canevas, la méthode « temps réel » RTK (Real Time Kinematic) peut être mise en oeuvre.

Par contre, compte-tenu de la précision planimétrique garantie par les gestionnaires de
réseau (5 cm), la méthode « temps réel » NRTK (Network Real Time Kinematic) ne doit pas être mise en œuvre pour la vérification de points de canevas dont la classe de précision est inférieure ou égale
à [10 cm]. Sont concernés par cette restriction tous les canevas planimétriques cités au III-D-1-a § 111.

Ainsi, seule la classe de précision d'un canevas d'appui de géoréférencement peut être
vérifiée par la méthode GNSS « temps réel » NRTK.

Dans les mêmes conditions, la méthode « temps réel » NRTK est aussi proscrite pour vérifier
la classe de précision d'un canevas altimétrique.

#### 1. Choix des points

135

Dans un premier temps, la vérification technique sur le terrain a pour but d'apprécier le
choix et la pérennité des points observés. Cette appréciation est réalisée par l'examen des éléments suivants :

- la matérialisation de tous les points ;

- le bon choix de l’emplacement des bornes (visées d'orientations existantes, conservation
de la borne) ;

- les fiches signalétiques (repérage correct, contrôle des cotes de repérage, etc.).

140

Le volume de points de contrôle est laissé à l'appréciation du vérificateur qui l'adapte au
canevas à vérifier. Cependant, l'échantillon des points de contrôle doit représenter au moins 20 % des points du canevas vérifié.

#### 2. Vérification de la classe de précision

145

Pour chaque point contrôlé, il convient de calculer l’écart en position entre sa
détermination initiale et celle de contrôle et de vérifier le respect des tolérances applicables au modèle standard conformément aux prescriptions figurant au
II-C § 73.

Pour chaque type de canevas vérifié, la valeur de la classe de précision totale ainsi que
les différents seuils attachés à chaque valeur sont récapitulés dans le tableau ci dessous :

Type de canevas

Classe de précision totale (cm)

Emoypos inférieur à (cm)

1er seuil (cm)

2ème seuil (cm)

Points pérennes d'une densification de réseau

4

4,50

10,89

16,34

Divers travaux spéciaux tels l'élaboration ou la vérification d'une base d'étalonnage

2

2,25

5,45

8,17

Canevas de précision

5

5,63

13,61

20,42

Canevas ordinaire

10

11,25

27,23

40,84

Canevas préalable à un AFAF

10

11,25

27,23

40,84

Canevas d'appui d'une prise de vues permettant la confection d'un plan de classe de précision [10] cm

5

5,63

13,61

20,42

Canevas d'appui d'une prise de vues permettant la confection d'un plan de classe de précision [20] cm

10

11,25

27,23

40,85

Canevas d'appui de géoréférencement

60

67,50

163,35

245,03

Tableau récapitulant pour chaque type de canevas vérifié, la valeur de la classe de précision totale ainsi que les différents seuils attachés à chaque valeur

En fonction des résultats obtenus, le vérificateur prononce l'acceptation pure et simple des
travaux, l'acceptation des travaux sous réserve de rectification des écarts constatés dépassant les seuils, soit le refus des travaux.

Ces éléments sont consignés dans un rapport de vérification
n° 6160-SD et ses intercalaires n° 6161-SD.

### B. Vérification d'un remaniement du plan

#### 1. Vérification de la classe de précision du plan

150

Cette vérification a pour but de contrôler que le plan refait possède la classe de précision
totale définie conformément au tableau relatif à la classe de précision des plans cadastraux du III-D-3 § 117.

Les points de contrôle sont choisis parmi des points caractéristiques, des objets levés,
identifiés, ne présentant aucun caractère d’ambiguïté, Les coordonnées de ces points sont déterminées soit par rayonnement, soit par lever GNSS et sont comparées à celles issues du plan numérique
refait.

La vérification est exécutée obligatoirement sur le terrain en présence du géomètre.

160

La volumétrie de l'échantillon de contrôle est laissé à l'appréciation du vérificateur qui
l'adapte à la situation rencontrée. Cependant, le contrôle doit porter sur au moins 20 % des sections réalisées. Pour chacune de ces sections, le vérificateur doit faire porter son contrôle sur un
échantillon d'au moins 80 points. Cette limite peut être abaissée pour l'adapter au volume d'éléments présents sur la feuille de plan.

Les écarts obtenus sont analysés à la lumière des prescriptions de l'article 5 de
l'arrêté du 16 septembre 2003. Les différentes
valeurs des seuils en fonction de la classe de précision et de l'échelle du plan sont récapitulées dans le tableau ci dessous :

Échelle de confection

du plan de remaniement

Classe de précision totale (cm)

Emoypos inférieur à (cm)

1er seuil (cm)

2ème seuil (cm)

1/500

10

11,25

27,23

40,84

1/1 000 ou 1/2 000

20

22,50

54,45

81,68

Tableau récapitulant les différentes valeurs des seuils en fonction de la classe de précision et de l'échelle du plan

En fonction des résultats obtenus, le vérificateur prononce l'acceptation pure et simple des
travaux , l'acceptation des travaux sous réserve de rectification des écarts constatés dépassant les seuils, soit le refus des travaux.

Ces éléments sont consignés dans un rapport de vérification
n° 6160-SD et ses intercalaires n° 6161-SD.

Remarque importante :

Pour les mêmes raisons que celles évoqués lors du contrôle de canevas, la vérification d'un
plan de classe de précision [10 cm] ne peut être réalisée par la méthode GNSS « temps réel » NRTK. Dans ce cas, les méthodes GNSS « temps réel » RTK ou de « post-traitement » sont adaptées.

#### 2. Vérification du récolement du bornage (uniquement en Alsace-Moselle)

165

La vérification du récolement du bornage est indépendante de celle de la valeur
topographique du plan.

170

Cette vérification a pour but de s'assurer, par sondage, de la sincérité des cotes figurant
sur le plan. Elle est effectuée conjointement avec celle de la valeur topographique.

Elle conduit à mesurer sur le terrain, entre bornes, des longueurs qui sont par ailleurs
cotées sur le plan d'aménagement foncier rural.

Les écarts entre les longueurs mesurées et les cotes inscrites au plan sont comparés à la
tolérance T suivante :

T = 6 + 0,57 x (L)1/2 + 0,06 x L

formule dans laquelle T est exprimée en centimètres et L en mètres.

Un tableau donnant la valeur de cette tolérance en fonction de la longueur mesurée figure au
BOI-ANNX-000392.

Remarque :

Lors des mesurages de vérification effectués sur le terrain, il est recommandé de ne pas
mesurer uniquement des longueurs périmétriques entre bornes dont les cotes figurent sur le plan mais d'effectuer également quelques mesurages à l'intérieur de la feuille vérifiée.

180

La volumétrie de l'échantillon de contrôle est laissé à l'appréciation du vérificateur qui
l'adapte à la situation rencontrée. Cependant, le contrôle doit porter sur au moins 20 % des sections réalisées par le géomètre aménageur. Pour chacune de ces sections, le vérificateur doit faire
porter son contrôle sur un échantillon d'au moins 40 mesurages de cotes figurant sur le plan. Cette limite peut être abaissée pour l'adapter au volume d'éléments présents sur la feuille de plan.

### C. Vérification d'un aménagement foncier agricole et forestier

185

La vérification technique relative à un aménagement foncier agricole et forestier (AFAF)
portent sur le récolement du bornage, le calcul des contenances parcellaires et la classe de précision totale du plan.

#### 1. Vérification du récolement de bornage

190

Cette vérification est conduite selon les mêmes modalités que celles prévues dans le cadre
d'un remaniement du plan en Alsace-Moselle (cf. IV-B-2 § 165 et suiv.).

#### 2. Vérification du calcul des contenances parcellaires

195

L'arrêté du 16 septembre 2003 n'évoquant pas les
tolérances applicables à l'écart entre deux déterminations indépendantes des contenances des parcelles, deux cas sont à envisager selon que le plan d'aménagement foncier rural a été confectionné par
le géomètre aménageur en mode graphique ou en mode numérique.

200

Si le plan d'aménagement foncier rural a été confectionné en mode graphique, la vérification
du calcul des contenances est conduite par sondage suivant les pratiques antérieures et par référence aux tolérances figurant au BOI-ANNX-000399. Cette vérification doit
porter sur au moins 20 % du volume des parcelles à contrôler. Un tableau donnant la valeur de ces tolérances en fonction de la surface contrôlée figure au
BOI-ANNX-000389.

210

Si le plan a été confectionné en mode numérique, la vérification du calcul de contenance
doit permettre de s'assurer que le géomètre aménageur a bien effectué un calcul des contenances à partir des coordonnées cartésiennes de tous les sommets de la parcelle. Cette vérification est
effectuée par sondage sur au moins 20 % du volume des parcelles à contrôler. Les écarts constatés ne devront pas excéder un mètre carré pour tenir compte des règles d'arrondis.

#### 3. Vérification de la valeur topographique ou de la classe de précision du plan

##### a. AFAF dont les travaux ont débuté avant 2003

215

Lorsque les travaux ont été commandés avant la parution de
l'arrêté du 16 septembre 2003, ils doivent être
conformes aux prescriptions de l'arrêté du 21 janvier 1980. La vérification porte sur la valeur topographique du plan.

220

Cette vérification a pour objet de s'assurer que le plan a la précision requise et peut, dès
lors, être classé dans la catégorie à laquelle il doit appartenir. Les plans d'AFAF doivent appartenir, suivant leur échelle de confection, aux catégories suivantes :

- plans au 1/1 000 : catégorie P4 ;

- plans au 1/2 000 : catégorie P5.

La vérification est exécutée obligatoirement sur le terrain, en présence du géomètre
aménageur.

Afin d'éviter d'introduire des erreurs propres à la vérification -ce qui fausserait
l'appréciation à formuler quant à la catégorie dont relève effectivement le plan- les mesurages sont :

- soit exécutés directement au ruban, sous réserve que la mesure de contrôle puisse être
effectuée en une seule portée ;

- soit par rayonnement, à l'aide d'un tachéomètre ;

- soit directement à partir d'un équipement GNSS.

Dans cette dernière éventualité, la longueur « terrain » entre deux points rayonnés depuis
un point quelconque de station est calculée au bureau, à partir des coordonnées locales de ces points.

Les longueurs « terrain » Lt sont ensuite comparées aux longueurs homologues
Lp mesurées sur le plan.

230

La volumétrie de l'échantillon de contrôle est laissé à l'appréciation du vérificateur qui
l'adapte à la situation rencontrée. Cependant, le contrôle doit porter sur au moins 20 % des sections réalisées par le géomètre aménageur. Pour chacune de ces sections, le vérificateur doit faire
porter son contrôle sur un échantillon d'au moins 40 longueurs. Cette limite peut être abaissée pour l'adapter au volume d'éléments présents sur la feuille de plan.

Pour chaque feuille vérifiée, le nombre d'écarts individuels hors tolérance est inférieur ou
égal à la valeur admissible fixée par le tableau suivant :

Nombre d'écarts individuels n

< 20

de 20 à 49

de 50 à 99

> 100

Nombre d'écarts hors tolérance admissible

1

2

3

4 % de n

Tableau fixant pour chaque feuille vérifiée, le nombre d'écarts individuels hors tolérance est inférieur ou égal à la valeur admissible

Il est procédé dans ce cas au calcul de la moyenne quadratique des écarts individuels
Emq, les écarts hors tolérance n'étant pas pris en compte pour ce calcul. Cette moyenne doit être inférieure ou égale à la tolérance T suivante :

T = cm

formule dans laquelle :

- n' est le nombre d'écarts individuels retenus pour calculer Emq ;

- Q dépend de la catégorie du plan.

Si cette condition est satisfaite, le plan est considéré comme ayant la précision requise
sous réserve de mettre en accord le plan (ou le fichier) et les cotes de vérification en ce qui concerne les écarts dépassant la tolérance.

Tous ces éléments sont consignés dans un rapport de vérification
n° 6160-SD et ses intercalaires n° 6161-SD.

##### b. AFAF dont les travaux ont débuté après 2003

240

Les travaux de vérification de la classe de précision des plans confectionnés dans le cadre
d'un AFAF sont conduits de manière identique à ceux réalisés dans le cadre d'un remaniement.

250

La volumétrie de l'échantillon de contrôle est laissé à l'appréciation du vérificateur qui
l'adapte à la situation rencontrée. Cependant, le contrôle doit porter sur au moins 20 % des sections réalisées par le géomètre aménageur. Pour chacune de ces sections, le vérificateur doit faire
porter son contrôle sur un échantillon d'au moins 80 points. Cette limite peut être abaissée pour l'adapter au volume d'éléments présents sur la feuille de plan.

La vérification est exécutée obligatoirement sur le terrain, en présence du géomètre
aménageur.

260

Les écarts obtenus sont analysés à la lumière des prescriptions de l'article 5 de
l'arrêté du 16 septembre 2003. Les différentes
valeurs des seuils en fonction de la classe de précision et de l'échelle du plan sont récapitulées dans le tableau ci dessous :

Échelle de confection

du plan aménagé

Classe de précision totale (cm)

Emoypos inférieur à (cm)

1er seuil (cm)

2ème seuil (cm)

1/1 000 ou 1/2 000

20

22,50

54,45

81,68

Tableau des différentes valeurs des seuils en fonction de la classe de précision et de l'échelle du plan

Remarque :

Les plans d'aménagement foncier agricole et forestier à l'échelle du 1/2 000 dont le marché
public a été conclu après 2003 et antérieurement à la date de publication de la présente documentation (12 septembre 2012) sont considérés comme des plans de classe de précision totale [40] cm ou
catégorie P5.

#### 4. Rapport de vérification

265

Les constatations faites au cours de la vérification technique sont relatées dans un rapport
n° 6160-SD auquel sont annexés les intercalaires n° 6161-SD à raison d'une par nature de contrôle.

Ces documents sont transmis au géomètre aménageur pour suite utile.

Puis, avant de les communiquer au maître d'ouvrage, le vérificateur y inscrit, si
nécessaire, ses nouvelles observations en concluant à la fin du rapport :

- soit à l'acceptation pure et simple des travaux ;

- soit à l'acceptation sous conditions de rectifier les éléments ayant conduit à des
réserves. Le rapport fera alors état des rectifications à effectuer ;

- soit au refus des travaux. Ceux-ci seront alors, à la diligence du maître d'ouvrage,
repris par le géomètre aménageur et soumis à nouveau à l'acceptation du service du cadastre.

### D. Vérification du géoréférencement du plan

#### 1. Généralités

270

La vérification du géoréférencement est adaptée selon que les travaux ont été réalisés en
régie ou externalisés auprès d'un prestataire.

Les classes de précision à retenir sont celles définies ci-après, indépendantes du mode
opératoire choisi.

#### 2. La classe de précision d'un géoréférencement

275

Pour les travaux de rattachement au système de référence des feuilles de plan non carroyées,
la vérification est réalisée par échantillonnage, pour chaque lot de feuilles de même échelle, selon la classe de précision planimétrique totale [YY] cm avec un coefficient de sécurité C égal à 2.

280

La classe de précision totale à retenir, pour chaque lot de feuilles d’échelle identique,
dépend de l’échelle du plan à rattacher. Elle est donnée par la relation suivante :

[YY] = 2 / (9 x E) cm

où E représente l’échelle du lot de plans à géoréférencer.

La classe de précision totale [YY] obtenue par la relation ci-avant sera arrondie à la
dizaine de centimètres supérieure.

Le tableau ci-après reprend les classes de précision ainsi obtenues selon l’échelle du plan
géoréférencé :

Échelle du plan

Classe de précision totale

à retenir (en m)

1/625

1,4

1/1 000

2,3

1/1 250

2,8

1/2 000

4,5

1/2 500

5,6

1/4 000

8,9

1/5 000

11,2

1/8 000

17,8

Tableau des classes de précision obtenues selon l’échelle du plan géoréférencé

La vérification est conduite conformément aux indications portées aux IV-D 3 à 5 §
285 et suivants. Le tableau ci- dessous récapitule les différentes valeurs (en centimètres) des seuils en fonction de l'échelle du plan géoréférencé :

Échelle

Emoypos inférieur à

1er seuil

2ème seuil

T = [xx] x (1 + (2 x C2)-1) m

T = k x [xx] x (1 + (2 x C2)-1) m

T = 1,5 x k x [xx] x (1 + (2 x C2)-1) m

1/625

1,58

3,82

5,73

1/1 000

2,59

6,27

9,41

1/1 250

3,15

7,62

11,43

1/2 000

5,06

12,25

18,38

1/2 500

6,3

15,25

22,87

1/4 000

10,01

24,22

36,33

1/5 000

12,6

30,49

45,74

1/6 000

20,03

48,47

72,71

Valeurs des seuils en fonction de l'échelle du plan géoréférencé

Avec C=2 et k=2,42

Les travaux devront remplir simultanément les trois conditions pour être
acceptés.

En fonction des résultats obtenus, le vérificateur prononce l'acceptation pure et simple des
travaux, l'acceptation des travaux sous réserve de rectification des écarts constatés dépassant les seuils, soit le refus des travaux.

Ces éléments sont consignés dans un rapport de vérification
n° 6160-SD et ses intercalaires n° 6161-SD.

#### 3. La vérification d'un géoréférencement réalisé en régie

##### a. Pour les feuilles possédant un carroyage dans un ancien système de coordonnées

285

Pour les feuilles de plan possédant un carroyage dans un ancien système de coordonnées comme
par exemple le système Lambert zones en métropole, la vérification sera conduite par échantillonnage sur l'ensemble des fichiers de géoréférencement produits selon les prescriptions du
BOI-CAD-TOPO-50 relatif au géoréférencement du plan cadastral.

290

Ce contrôle ne consiste pas en la vérification du respect d'une classe de précision mais est
réalisé par le recalcul avec l'application d'initiative locale dédiée à ce type de travaux d'au moins 10 % du nombre de fichiers de géoréférencement.

La vérification portera également sur le choix de la projection légale (par exemple, numéro
de zone correcte pour la projection CC 9 zones en métropole).

##### b. Pour les feuilles ne possédant pas de carroyage

300

Le géoréférencement est réalisé en régie par calcul en bloc, selon les prescriptions du
BOI-CAD-TOPO-50 relatif au géoréférencement du plan cadastral et est vérifié conformément aux dispositions ci-après. Cette vérification porte sur les fichiers de
géoréférencement issus du calcul en bloc et produits par le logiciel d'initiative locale de la DGFiP.

Ainsi, pour chaque lot de feuilles de même échelle (ou de lot de fichiers de
géoréférencement de feuilles à même échelle), l'échantillon de contrôle est composé d'au moins 20 % du nombre total de fichiers du lot en prenant soin qu'au moins un fichier de géoréférencement soit
vérifié par commune.

Pour chaque feuille de plan, les fichiers issus du calcul en bloc fournissent, en métropole,
dans le système de coordonnées CC 9 zones de la commune et dans le système de coordonnées « pixel » de la feuille, les coordonnées des quatre coins du fichier image de la feuille.

Pour vérifier un fichier de géoréférencement, le vérificateur identifiera un point sur le
terrain et son homologue sur la feuille de plan. Ses coordonnées de contrôle sont obtenues sur le terrain par procédés satellitaires et ses coordonnées issus du calcul en bloc sont obtenues dans PCI
image après avoir géoréférencé la feuille de plan où se trouve le point de contrôle avec le fichier de géoréférencement contrôlé.

Les classes de précision à retenir sont celles fixées par la DGFiP au
IV-D-2 § 275 à 280.

310

Cependant, il convient d'adapter le volume de l'échantillon de contrôle en fonction d'une
part, de la qualité du plan cadastral à géoréférencer et d'autre part de la nature du terrain. Le volume de l'échantillon de contrôle pourra être augmenté dans les zones montagneuses ou à fortes
dénivelées et les zones frontalières ou côtières.

Remarque :

Les feuilles de plan disposant d'un carroyage incluses dans le calcul en bloc sont exclues de
cette vérification puisqu'elles sont vérifiée selon les prescriptions du IV-D-3-a § 285 à 290.

#### 4. La vérification d'un géoréférencement réalisé par un prestataire

315

Aucune méthodologie n'est imposée au prestataire chargé des travaux, qui a seulement une
obligation de résultats (respect des classes de précision totales fixées par la DGFiP au IV-D-2 § 275 à 280.

320

Le contrôle d'un géoréférencement porte, en la forme, sur le dossier remis par le
prestataire (il convient de se reporter au BOI-CAD-TOPO-50 relatif au géoréférencement du plan cadastral) et, quant au fond, sur la qualité des résultats obtenus.

Les résultats obtenus sont contrôlés par échantillonnage sur la zone que le prestataire aura
géoréférencée. Le contrôle consiste à déterminer à nouveau dans le système de coordonnées retenu (Lambert 93 ou CC 9 zones pour la métropole) à partir du système national de référence géodésique RGF93
pour la métropole au moins 10 % du nombre total de points fournis par le prestataire pour chaque lot de feuilles de même échelle en veillant à ce que l'échantillon de contrôle porte sur toutes les
communes à vérifier.

Ces points de contrôle sont choisis par la DGFiP parmi les seuls points clairement
identifiables sur le terrain et seront déterminés par procédés satellitaires.

330

Dans le cas où des parties importantes de la zone à géoréférencer ne comporteraient que très
peu de points identifiables à la fois sur le plan cadastral et sur le terrain, le vérificateur déterminera sur le terrain des points judicieusement choisis pour permettre leur report par construction
sur le plan cadastral image et ainsi en déduire (dans l’application PCI Image) une nouvelle détermination pour un point fourni par le prestataire.

Remarque :

Les points déterminés par le prestataire ne doivent pas être utilisés par le vérificateur
comme points d’appui connus en coordonnées pour les opérations GNSS.

#### 5. La vérification des fichiers de géoréférencement obtenus auprès de l'IGN

340

Compte tenu des spécificités de ce prestataire et de sa méthodologie de géoréférencement
connue de la DGFiP, la méthode de vérification figurant au IV-D-4 § 315 à 330 doit être adaptée en tenant compte des indications ci-après.

Pour chaque lot de feuilles de même échelle (ou de lot de fichiers de géoréférencement de
feuilles à même échelle), l'échantillon de contrôle est composé d'au moins 20 % du nombre total de fichiers du lot en prenant soin qu'au moins un fichier de géoréférencement soit vérifié par commune.

350

Les feuilles de plan disposant d'un carroyage sont exclues de la vérification puisque pour
ces feuilles, le géoréférencement est obtenu dans PCI image à partir du carroyage et non à partir du fichier de géoréférencement de l'IGN (il convient de se reporter au
BOI-CAD-TOPO-50 relatif au géoréférencement du plan cadastral).

Pour chaque feuille de plan, les fichiers de l'IGN fournissent, en métropole, dans le
système de coordonnées CC 9 zones de la commune et dans le système de coordonnées « pixel » de la feuille, les coordonnées des quatre coins du fichier image de la feuille.

Pour vérifier un fichier de géoréférencement, le vérificateur identifiera un point sur le
terrain et son homologue sur la feuille de plan. Ses coordonnées de contrôle sont obtenues sur le terrain par procédés satellitaires et ses coordonnées « IGN » sont obtenues dans PCI image après avoir
géoréférencé la feuille de plan où se trouve le point de contrôle avec le fichier de l'IGN.

Les classes de précision à retenir sont celles fixées par la DGFiP au
IV-D-2 § 275 à 280.

Cependant, il convient d'adapter le volume de l'échantillon de contrôle en fonction d'une
part, de la qualité du plan cadastral à géoréférencer et d'autre part de la nature du terrain. Le volume de l'échantillon de contrôle pourra être augmenté dans les zones montagneuses ou à fortes
dénivelées et les zones frontalières ou côtières.

Le vérificateur pourra s'aider du fichier communal de métadonnées accompagnant les fichiers
de géoréférencement de l'IGN qui fournit diverses informations sur le géoréférencement réalisé par l'IGN.

La vérification de ce type de géoréférencement permettra d'orienter le
service vers le choix d'utiliser ou non, partiellement ou en totalité, les fichiers de l'IGN.

Le rapport de vérification n° 6160-SD et ses intercalaires
n° 6161-SD seront systématiquement adressés à l'administration centrale (bureau du cadastre) accompagnés de tous les éléments utiles à l'analyse du rapport (feuilles de
plan image, fichiers de géoréférencement, etc.).

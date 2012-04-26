# Article Annexe III

INFORMATIONS PÉRIODIQUEMENT RELEVÉES PAR LES GESTIONNAIRES D'INFRASTRUCTURES

Tableau 1. - Description annuelle des segments de réseau

composant le réseau ferroviaire au 31 décembre

VARIABLE

|

DESCRIPTION

|

CODIFICATION

(longueur)

|

COMPLÉMENTS

|

Année

|

Année des résultats au 1er janvier

|

4

|

|

Période

|

Période de référence

|

2

|

L'année est codée A0

|

Réseau

|

Nom du gestionnaire de l'infrastructure

|

15

|

|

Segment

|

Segment de réseau

|

8

|

Le code du segment de réseau est formé du code ISO-3166-alpha2 du pays + "S" + direction (1 ou 2) + nombre sur 6 positions

|

LongitudeE1

|

Longitude de l'extrémité 1 du segment

|

10

|

Mesure angulaire par rapport au méridien de Greenwich

|

LatitudeE1

|

Latitude de l'extrémité 1 du segment

|

10

|

Mesure angulaire par rapport à l'équateur

|

Lib_E1

|

Nom de l'extrémité 1 du segment

|

40

|

|

UIC_E1

|

Code UIC de la gare si l'extrémité 1 du segment est une gare

|

8

|

Le code UIC de la gare est formé par la concaténation du code d'infrastructure ferroviaire sur 2 caractères, du code gare sur 5 caractères et du code d'autocontrôle sur 1 caractère

|

LongitudeE2

|

Longitude de l'extrémité 2 du segment

|

10

|

Mesure angulaire par rapport au méridien de Greenwich

|

LatitudeE2

|

Latitude de l'extrémité 2 du segment

|

10

|

Mesure angulaire par rapport à l'équateur

|

Lib_E2

|

Libellé de l'extrémité 2 du segment

|

40

|

|

UIC_E1

|

Code UIC de la gare si l'extrémité 2 du segment est une gare

|

8

|

Le code UIC de la gare est formé par la concaténation du code d'infrastructure ferroviaire sur 2 caractères, du code gare sur 5 caractères et du code d'autocontrôle sur 1 caractère

|

Longueur

|

Longueur du segment

|

4

|

Longueur en kilomètres

|

Ten

|

Appartenance du segment au réseau transeuropéen de transport (Ten)

|

1

|

- 1 : oui, le segment appartient à Ten ;

- 0 : non, le segment n'appartient pas à Ten.

|

AGC

|

Numéro de lignes selon l'accord européen sur les grandes lignes internationales de chemin de fer (AGC)

|

4

|

Cf. annexe I de l'accord européen sur les grandes lignes internationales de chemin de fer (AGC)

|

Gauge

|

Ecartement des voies

|

4

|

Ecartement en mètres

|

Voies

|

Nombre de voies composant le segment

|

1

|

Variable numérique

|

Electrifié

|

Identifiant d'électrification du segment

|

1

|

- 1 : oui, le segment est électrifié ;

- 0 : non, le segment n'est pas électrifié.

Si une partie du segment n'est pas électrifiée, le segment est considéré comme non électrifié.

|

Courant

|

Le type de courant lorsque le segment est électrifié

|

15

|

Le type du courant est défini par 3 éléments concaténés :

- AC/DC ;

- fréquence ;

- voltage.

|

Code_UIC

|

Le code UIC de la ligne de chemin de fer à laquelle se rapporte le segment

|

3

|

Le code UIC de la ligne permet de retrouver le segment avec le système GISCO d'information géographique de la Commission européenne

|

Tableau 2. - Informations annuelles de circulation et de recettes tarifaires sur le réseau ferroviaire

VARIABLE

|

DESCRIPTION

|

CODIFICATION

(longueur)

|

COMPLÉMENTS

|

Année

|

Année des résultats

|

4

|

|

Période

|

Période de référence

|

2

|

Constante codée A0

|

Réseau

|

Nom du gestionnaire de l'infrastructure

|

15

|

|

Segment

|

Segment de réseau

|

8

|

Code d'identification du réseau issu de la table descriptive des segments de réseau français (cf. tableau 1 annexe 4)

|

Ten

|

Appartenance du segment au réseau transeuropéen de transport (Ten)

|

1

|

- 1 : oui, le segment appartient à Ten ;

- 0 : non, le segment n'appartient pas à Ten.

|

Trains_marchn

|

Nombre annuel de trains ayant transporté des marchandises

|

15

|

Variable numérique

|

Trains_marchv

|

Recette tarifaire de transport de fret en € hors taxes

|

5

|

Variable numérique

|

Trains_passn

|

Nombre annuel de trains ayant transporté des voyageurs

|

15

|

Variable numérique

|

Trains_passv

|

Recette tarifaire de transport de voyageurs en € hors taxes

|

5

|

Variable numérique

|

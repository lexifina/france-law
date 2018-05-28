# Nantes Métropole : délibération Spécifications-SCDL-Délibérations_v2_0 (2) — Spécifications-SCDL-Délibérations_v2_0 (2).pdf

- Collectivité : Nantes Métropole
- SIREN : 244400404
- Date : 2018-05-28
- Objet : Spécifications-SCDL-Délibérations_v2_0 (2).pdf
- Pages : 4
- Acte publié : https://data.nantesmetropole.fr/api/v2/catalog/datasets/214401507_deliberations-conseil-municipal-sagl/attachments/specifications_scdl_deliberations_v2_0_2_pdf
- Jeu de données : https://www.data.gouv.fr/datasets/67f70b05c7f49c50e69ac770

## Texte

ODL / SCLD - Délibérations - v2.0
p1/
Délibérations
Liste des délibérations adoptées par une assemblée 
locale
Collectivités concernées : COM | INTERCO | DEP | REG
Source : Opendatafrance
Version : 2.0
Le : 28 mai 2018
Etat : validée
Cadrage
Contexte de production des données
Les données de la “liste des délibérations adoptées par une assemblée locale” sont produites par la 
collectivité délibérante. Les délibérations doivent être transmises pour contrôle de légalité à la 
préfecture, elles sont affichées sur les panneaux d’affichage public de l’institution (C'est la série 
d'obligations imposées par la Loi (CGCT), quelque soit l'ordre dans lequel elles interviennent, qui doit 
être accomplie pour que la délibération devienne exécutoire).
Les délibérations font partie du projet ACTES qui vise à dématérialiser la transmission des actes des 
collectivités territoriales soumis au contrôle de légalité.
Références utiles
●
Contrôle de légalité des actes des collectivités territoriales - Wikipedia
●
Schéma logique de formation des délibérations
Synthèse des données essentielles

ODL / SCLD - Délibérations - v2.0
p2/
Le jeu de données DELIBERATIONS doit contenir les données essentielles suivantes (les 
champs obligatoires sont en gras) :
1.
Nom officiel de la collectivité délibérante
2.
Identifiant unique de la collectivité délibérante (SIRET)
3.
Identifiant interne de délibération respectant le formalisme propre à la 
collectivité
4.
Date du vote de la délibération
5.
Code de l’indexation de niveau 2 de la nomenclature Actes
6.
Intitulé de l’indexation des niveaux 1 et 2 de la nomenclature Actes
7.
Description de l’objet de la délibération
8.
Année de l’exercice budgétaire sur lequel s'applique la décision si celle-ci a un 
impact budgétaire
9.
Nom du budget si la délibération engendre une affection budgétaire
10. Code de l’entité exerçant le contrôle de légalité
11. Date d’enregistrement de la délibération au contrôle de légalité
12. Décompte de l’effectif total des élus susceptibles de participer au vote
13. Décompte de l’effectif total des élus ayant réellement participé au vote
14. Nombre de votes Pour
15. Nombre de votes Contre
16. Nombre de votes Abstention
17. Lien vers le document de la délibération
Spécifications détaillées
Champ
Objet
Obligat
oire
Type / Format / 
Exemple
Commentaires et 
Références
COLL_NOM

Nom officiel de la 
collectivité délibérante
OUI
texte / libre / Ex : 
Toulouse Métropole
Confort pour les 
humains
COLL_SIRET

Identifiant unique de la 
collectivité délibérante 
(SIRET)
OUI
Identifiant du Système 
d'Identification du 
Répertoire des 
Etablissements 
(SIRET) / Chaine 
numérique 9+5 
chiffres d’un seul 
tenant / Ex : 
79768123600015
Indispensable pour les 
machines
(rq : le code INSEE ne 
permettrait pas de traiter 
les EPCI) 
DELIB_ID

Identifiant interne de 
délibération respectant 
le formalisme propre à 
OUI
Texte / Libre / Ex : 
1DL15494

ODL / SCLD - Délibérations - v2.0
p3/
la collectivité
DELIB_DATE

Date du vote de la 
délibération
OUI
Date / AAAA-MM-JJ / 
Ex : 2015-09-12
Format international 
ISO-8601
DELIB_MATIERE_
CODE

Code de l’indexation de 
niveau 2 de la 
nomenclature Actes
OUI
Texte / Numéro 
d’identification dans 
l’arborescence / Ex : 
7.10
Exemple de 
nomenclature sur 2 
niveaux de la Préfécture 
de Moselle
DELIB_MATIERE_
NOM

Intitulé de l’indexation 
des niveaux 1 et 2 de 
la nomenclature Actes
OUI
Intitulé de matière 
niveau 1 suivi de 
l’intitulé de sous-
matière niveau 2 
séparés par « / ».
Exemple de 
nomenclature sur 2 
niveaux de la Préfécture 
de Moselle
DELIB_OBJET

Description de l’objet 
de la délibération
OUI
Texte / Libre / Ex : 
Attribution du marché 
à xxx
Ne doit pas contenir 
d’information à 
caractère personnel 
(nom personnel du 
bénéficiaire, …)
BUDGET_ANNEE

Année de l’exercice 
budgétaire sur lequel 
s'applique la décision si 
celle-ci a un impact 
budgétaire
NON
Date / AAAA / Ex : 
2016 ou intervalle 
entre 2 années 
séparées par un “/” Ex 
: 2016/2017
Format international 
ISO-8601
BUDGET_NOM

Nom du budget si la 
délibération engendre 
une affection 
budgétaire
NON
Texte / Libre / Ex : 
Budget annexe 
déchets-collecte et 
traitement
PREF_ID

Code de l’entité 
exerçant le contrôle de 
légalité 
NON
Pour les préfectures : 
PREFNNN (7 
caractères)
Pour les sous-
préfectures : 
SPREFNNNM (9 
caractères)
Pour les SGAR : 
SGARNNN (7 
caractères)
Où NNN : numéro sur 
3 caractères du 
département et M : 
numéro sur un chiffre 
de l’arrondissement
Voir les codifications 
utilisées dans le cadre 
d’Actes : annexe p.28 / 
paragraphe 7.2
PREF_DATE

Date d’enregistrement 
de la délibération au 
contrôle de légalité
NON
Date / AAAA-MM-JJ / 
Ex : 2016-07-16
Format international 
ISO-8601

ODL / SCLD - Délibérations - v2.0
p4/
VOTE_EFFFECTIF

Décompte de l’effectif 
total des élus 
susceptibles de 
participer au vote
NON
Nombre entier / NNN / 
Ex : 56

VOTE_REEL

Décompte de l’effectif 
total des élus ayant 
réellement participé au 
vote
NON
Nombre entier / NNN / 
Ex : 54 (présents plus 
éventuelles 
procurations)

VOTE_POUR

Nombre de votes Pour
NON
Nombre entier / NNN / 
Ex : 50

VOTE_CONTRE

Nombre de votes 
Contre
NON
Nombre entier / NNN / 
Ex : 1

VOTE_ABST

Nombre de votes 
Abstention
NON
Nombre entier / NNN / 
Ex : 3

DELIB_URL

Lien vers le document 
de la délibération
NON
Texte sous forme d’url 
unique
Fortement 
recommandé pour les 
collectivités qui 
dispose d’un outil de 
publication web des 
délibérations
- Les délibérations 
contenant des données 
à caractère personnel 
n'ont pas vocation à être 
publiées en open data
- de préférence avec 
une url en https
Historique des modifications :
●
Réorganisation de l’ordre des champs (champs obligatoires en premier)
●
Clarification des références aux codifications issues de Actes
●
Changement du statut obligatoire ou non de certains champs
●
Mise en cohérence et renommage de certains champs
●
Création d’un champ DELIB_MATIERE_NOM
●
Supression des champs suivants : BUDGET_SIRET, DELIB_TYPE_SEANCE, et 
DELIB_RESUME

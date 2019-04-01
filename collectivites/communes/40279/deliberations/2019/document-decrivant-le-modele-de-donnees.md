# Saint-Paul-lès-Dax : délibération — Document décrivant le modèle de données

- Collectivité : Saint-Paul-lès-Dax
- SIREN : 214002792
- Code INSEE : 40279
- Date : 2019-04-01 (date de mise en ligne sur data.gouv.fr ; la date de l'acte n'est pas lisible dans le fichier)
- Objet : Document décrivant le modèle de données
- Pages : 4
- Acte publié : https://static.data.gouv.fr/resources/deliberations-du-conseil-municipal-4/20190704-161617/spec-deliberations-saint-paul-les-dax.pdf
- Jeu de données : https://www.data.gouv.fr/datasets/5ca2743e634f413f06a425f3

## Texte

Délibérations du Conseil Municipal 
1/4 
Délibérations du Conseil Municipal 

Liste des délibérations adoptées par le Conseil Municipal 
de Saint-Paul-lès-Dax 

Collectivité : Commune de SAINT-PAUL-LES-DAX 

Source : Service QSI – Ville de Saint-Paul-lès-Dax 
Version : 2.0 
Date : 04/07/2019 
Etat : validé 

Objet 

Ce jeu de données dresse la liste des délibérations adoptées par le Conseil Municipal de la 
ville de Saint-Paul-lès-Dax depuis 2015. 
Il décrit les délibérations et propose pour chaque délibération un lien de téléchargement du 
document après transmission au contrôle de légalité. 

Ce document décrit les détails de chaque champ. 

Délibérations du Conseil Municipal 
2/4 
Synthèse des données essentielles 

Le jeu de données contient les données essentielles suivantes : 

 Identifiant unique de la collectivité sur laquelle s'applique la décision 
 Numéro de délibération (unique dans l'année ou dans le conseil) 
 Date du vote de la délibération (généralement date du conseil) 
 Catégorie de délibération 
 Objet de la délibération 
 Type de budget (Budget Principal ou Budget Annexe) si la délibération engendre une 
affection budgétaire 
 Identification de l’entité exerçant le contrôle de légalité 
 Date de réception de la délibération en préfecture pour le contrôle de légalité 
 Nombre d'effectif d'élus participant au vote et Nombre réel de votants 
 Nombre de votes Pour, Contre, Abstention 
 Lien vers la délibération 

Délibérations du Conseil Municipal 
3/4 
Spécifications détaillées 

Nom du champ 
Description 
Type / Format / Exemple 
COLL_NOM 
Nom officiel de la collectivité 
délibérante 
Texte 
Ex : Ville de SAINT-PAUL-LES-
DAX 
COLL_SIRET 
Identifiant du Système d'Identification 
du Répertoire des Etablissements 
(SIRET) de la collectivité attribuant la 
subvention, composé de 9 chiffres 
SIREN + 5 chiffres NIC d’un seul 
tenant 
Texte 
Ex : 23350001600040 
DELIB_ID 
Identifiant interne de délibération 
respectant le formalisme propre à la 
collectivité 
Texte 
Ex : 2019-04-7 
DELIB_DATE 
Date de décision de l'acte, celle à 
laquelle la délibération a été adoptée 
par la collectivité au format AAAA-
MM-JJ suivant la norme internationale 
ISO 8601 
Date 
Exemple : 2017-03-10 
DELIB_MATIERE_CODE 
Ce code correspond à celui de 
l'indexation de niveau 2 dans la 
structure arborescente de classement 
en matières et sous-matières (5 
niveaux de profondeur) de la 
nomenclature ACTES (Aide au 
Contrôle de légaliTé dématErialiSé). 
Si le champ est renseigné, sa valeur 
doit correspondre au nom de matière 
de DELIB_MATIERE_NOM 
Texte 
Exemple : 8 
DELIB_MATIERE_NOM 
Nom de matière. Ce nom peut être 
issu de la nomenclature ACTES ou 
d'un référentiel propre à la collectivité 
Texte 
Ex : Urbanisme 
DELIB_OBJET 
Description de l'objet de la 
délibération 
Texte 
Exemple : Vente d'un local 
communal 
BUDGET_ANNEE 
Année de l'exercice budgétaire sur 
lequel s'applique la décision si celle-ci 
a un impact budgétaire. Format AAAA 
pour une année ou AAAA/AAAA pour 
un intervalle entre deux années 
suivant la norme internationale ISO 
8601 
Texte 
Exemple : 2018 
BUDGET_NOM 
Ce champ ne peut être renseigné que 
si la délibération engendre une 
affection budgétaire 
Texte 
Exemple : Budget annexe Eau 

Délibérations du Conseil Municipal 
4/4 
PREF_ID 
Cet identifiant dépend de l'entité 
concernée. Pour les préfectures, il est 
codé 'PREFNNN' sur 7 caractères. 
Pour les sous-préfectures, il est codé 
'SPREFNNNM' sur 9 caractères. 
‘NNN' correspond au numéro sur 3 
caractères du département préfixé 
par '0' et incluant 'A' et 'B' pour les 
départements corses. 'M' correspond 
au numéro sur un chiffre de 
l'arrondissement 
Texte 
Exemple : PREF040 
PREF_DATE 
Date d'enregistrement de la 
délibération au contrôle de légalité au 
format AAAA-MM-JJ suivant la norme 
internationale ISO 8601. Ce champ 
ne peut être renseigné que si la 
délibération a effectivement été 
transmise et que sa date 
d'enregistrement est connue 
Date 
Exemple : 2017-03-14 
VOTE_EFFECTIF 
Effectif théorique des votants. 
Décompte de l'effectif total des 
représentants élus susceptibles de 
participer au vote 
Nombre entier 
Exemple : 33 
VOTE_REEL 
Effectif réel des votants. Décompte de 
l’effectif total des élus ayant 
réellement participé au vote 
(exclusion des absents) 
Nombre entier 
Exemple : 28 
VOTE_POUR 
Décompte du nombre total de votes 
'Pour' 
Nombre entier 
Exemple : 22 
VOTE_CONTRE 
Décompte du nombre total de votes 
'Contre' 
Nombre entier 
Exemple : 4 
VOTE_ABSTENTION 
Décompte du nombre total 
d'abstentions 
Nombre entier 
Exemple : 2 
DELIB_URL 
Lien vers le document de la 
délibération 
Texte 
Exemple : 
http://37.18.162.139/Delib/2018-
02-1.pdf

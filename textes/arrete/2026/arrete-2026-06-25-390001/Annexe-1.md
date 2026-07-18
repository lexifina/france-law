# Article Annexe 1

DONNÉES RELATIVES AUX OPÉRATEURS, À LEURS ÉTABLISSEMENTS ET AUX SITES D'ÉLEVAGE PORCIN (EGET)

A. Listes des tables

Thème |

Nom de la table |

Description |

DÉTENTEUR |

DÉTENTEUR |

Référentiel des détenteurs |

EXPLOITATION |

EXPLOITATION |

Référentiel des exploitations |

Lien exploitation - détenteur |

Lien de détention exploitation - détenteur |

Activité exploitation |

Périodes d'activité d'exploitation |

EGET |

EGET |

Référentiel des EGET porcines |

Activité EGET |

Période d'activité d'EGET porcine |

Rattachement EGET-exploitation |

Période de rattachement EGET porcines - exploitations |

B. Dictionnaire des données

1. Détenteurs

Attribut |

Description |

Format |

Type (obligatoire,

facultatif) |

Code pays |

Code pays détenteur |

CHAR (2) |

O |

Numéro détenteur |

Numéro détenteur |

VARCHAR (12) |

O |

Raison sociale |

Raison sociale ou situation civile |

VARCHAR (4) |

O |

Nom |

Nom du détenteur |

VARCHAR (30) |

O |

Adresse 1 |

Adresse 1 du détenteur |

VARCHAR (30) |

F |

Adresse 2 |

Adresse 2 du détenteur |

VARCHAR( 30) |

F |

Code postal |

Code localisation (code postal) du détenteur |

VARCHAR (5) |

O |

Commune |

Commune du détenteur |

VARCHAR (30) |

O |

SIREN |

Numéro de SIREN du détenteur |

VARCHAR (9) |

F |

Code pays résidence |

Code pays de résidence du détenteur |

CHAR (2) |

O |

Date de réception |

Date de réception en BDNI |

DATETIME |

O |

Apporteur |

Apporteur |

VARCHAR (12) |

O |

Date de création |

Date de création en BDNI |

DATETIME |

O |

Statut |

Statut en BDNI (actif ou Reprise) |

CHAR (1) |

O |

2. Exploitations

Attribut |

Description |

Format |

Type (obligatoire,

facultatif) |

Code pays |

Code pays exploitation |

CHAR (2) |

O |

Numéro exploitation |

Numéro exploitation |

VARCHAR (12) |

O |

Type |

Type d'exploitation |

CHAR (2) |

O |

Raison sociale |

Raison sociale ou situation civile |

VARCHAR (4) |

F |

Nom |

Nom de l'exploitation |

VARCHAR (30) |

F |

Adresse 1 |

Adresse 1 de l'exploitation |

VARCHAR (30) |

F |

Adresse 2 |

Adresse 2 de l'exploitation |

VARCHAR (30) |

F |

Code postal |

Code localisation (code postal) de l'exploitation |

VARCHAR (5) |

O |

Commune |

Commune de l'exploitation |

VARCHAR (30) |

O |

SIRET |

Numéro de SIRET de l'exploitation |

VARCHAR (14) |

F |

Code pays détenteur |

Code pays du détenteur actif |

VARCHAR (2) |

O |

Numéro détenteur |

Numéro du détenteur actif |

VARCHAR (12) |

O |

Latitude |

Coordonnée WGS84 : latitude |

NUMERIC (9,6) |

F |

Longitude |

Coordonnée WGS84 : longitude |

NUMERIC (9,6) |

F |

Date de réception |

Date de réception en BDNI |

DATETIME |

O |

Apporteur |

Apporteur |

VARCHAR (12) |

O |

Date de création |

Date de création en BDNI |

DATETIME |

O |

Statut |

Statut en BDNI (actif ou reprise) |

CHAR (1) |

O |

3. Liens exploitation - détenteur

Attribut |

Description |

Format |

Type (obligatoire,

facultatif) |

Code pays exploitation |

Code pays exploitation |

CHAR (2) |

O |

Numéro exploitation |

Numéro exploitation |

VARCHAR (12) |

O |

Code pays détenteur |

Code pays du détenteur |

CHAR (2) |

O |

Numéro détenteur |

Numéro du détenteur |

VARCHAR (12) |

O |

Date de lien |

Date début de lien de détention |

DATETIME |

O |

Complétude de date |

Complétude de la date de début du lien (0, 1, 2) |

NUMERIC (1) |

O |

Date de réception |

Date de réception en BDNI |

DATETIME |

O |

Apporteur |

Apporteur |

VARCHAR (12) |

O |

Date de création |

Date de création en BDNI |

DATETIME |

O |

Statut |

Statut en BDNI (actif ou Reprise) |

CHAR (1) |

O |

4. Activité des exploitations

Attribut |

Description |

Format |

Type (obligatoire,

facultatif) |

Code pays exploitation |

Code pays exploitation |

CHAR (2) |

O |

Numéro exploitation |

Numéro exploitation |

VARCHAR (12) |

O |

Code espèce |

Code de l'espèce détenue |

CHAR (1) |

O |

Date début d'activité |

Date début d'activité pour l'espèce détenue |

DATETIME |

O |

Complétude date |

Complétude de la date de début d'activité |

NUMERIC (1) |

O |

Date fin activité |

Date de fin d'activité pour l'espèce détenue |

DATETIME |

F |

Complétude date |

Complétude de la date de fin d'activité |

NUMERIC (1) |

F |

Date de réception |

Date de réception en BDNI |

DATETIME |

O |

Apporteur |

Apporteur |

VARCHAR (12) |

O |

Date de création |

Date de création en BDNI |

DATETIME |

O |

Statut |

Statut en BDNI (actif ou reprise) |

CHAR (1) |

O |

5. EGET porcines

Attribut |

Description |

Format |

Type (obligatoire,

facultatif) |

Code pays EGET |

Code pays de l'EGET |

CHAR 2 |

O |

Numéro EGET |

Numéro d'identification de l'EGET |

VARCHAR (12) |

O |

Type production |

Type de production (= P) |

CHAR (1) |

O |

Adresse 1 |

Adresse 1 de l'EGET |

VARCHAR (30) |

F |

Adresse 2 |

Adresse 2 de l'EGET |

VARCHAR (30) |

F |

Code postal |

Code postal de l'EGET |

VARCHAR (5) |

O |

Commune |

Commune de l'EGET |

VARCHAR (30) |

O |

Date de réception |

Date de réception en BDNI |

DATETIME |

O |

Latitude |

Coordonnée WGS84 : Latitude |

NUMERIC (9,6) |

F |

Longitude |

Coordonnée WGS84 : Longitude |

NUMERIC (9,6) |

F |

Apporteur |

Apporteur |

VARCHAR (12) |

O |

Date de création |

Date de création en BDNI |

DATETIME |

O |

Statut |

Statut |

CHAR (1) |

O |

6. Activité des EGETS

Attribut |

Description |

Format |

Type (obligatoire,

facultatif) |

Code pays |

Code pays de l'EGET |

CHAR (2) |

O |

Numéro EGET |

Numéro d'identification de l'EGET |

VARCHAR (12) |

O |

Type de production |

Type de production de l'EGET (=P) |

CHAR (1) |

O |

Date de début |

Date de début d'activité de l'EGET |

DATETIME |

O |

Complétude |

Complétude de la date de début d'activité |

NUMERIC (1) |

O |

Date de fin |

Date fin d'activité de l'EGET |

DATETIME |

F |

Complétude |

Complétude de la date de fin d'activité |

NUMERIC (1) |

F |

Date de réception |

Date de réception en BDNI |

CHAR (1) |

O |

Apporteur |

Apporteur |

VARCHAR (12) |

O |

Date de création |

Date de création en BDNI |

DATETIME |

O |

Statut |

Statut |

CHAR (1) |

O |

7. Rattachements EGET - exploitations

Attribut |

Description |

Format |

Type (obligatoire,

facultatif) |

Code pays |

Code pays de l'EGET |

CHAR (2) |

O |

Numéro EGET |

Numéro d'identification de l'EGET |

VARCHAR (12) |

O |

Type de production |

Type de production de l'EGET |

CHAR (1) |

O |

Code pays |

Code pays de l'exploitation de rattachement |

CHAR (2) |

O |

Numéro exploitation |

Numéro de l'exploitation de rattachement |

VARCHAR (12) |

O |

Date début |

Date de début de rattachement |

DATETIME |

O |

Complétude |

Complétude de la date de début de rattachement |

NUMERIC (1) |

O |

Date de réception |

Date de réception en BDNI |

DATETIME |

O |

Apporteur |

Apporteur |

VARCHAR (12) |

O |

Date de création |

Date de création en BDNI |

DATETIME |

O |

Statut |

Statut |

CHAR (1) |

O |

C. Mise à disposition pour la base de données nationale de traçabilité des porcins

- ces données sont transmises depuis la base de données nationale d'identification (BDNI) vers la base de données nationale de traçabilité des porcins ;

- deux types de transfert sont mis en place :

- un transfert hebdomadaire intégral : transmettre l'ensemble des données ;

- un transfert quotidien différentiel : transmettre les données créées ou invalidées depuis le dernier transfert intégral ;

- la base de données nationale de traçabilité des porcins transmet, sur demande du ministère en charge de l'agriculture, ces données recueillies aux systèmes désignés par ledit ministère ;

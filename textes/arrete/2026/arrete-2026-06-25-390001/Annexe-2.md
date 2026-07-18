# Article Annexe 2

DONNÉES RELATIVES AUX MOUVEMENTS PORCINS

A. Dictionnaire des données

1. Mouvement

Attribut |

Description |

Format |

Type (obligatoire,

facultatif) |

Identifiant du mouvement |

Identifiant unique du mouvement |

NUMERIC (6) |

O |

Type lieu |

Type du lieu du mouvement :

Source : table de référence "Type lieu" |

VARCHAR (1) |

O |

Type site |

Type du site de l'élevage : = EGET si le type de lieu = EGET |

VARCHAR (5) |

F |

Code pays lieu |

Code pays du lieu de mouvement

Source : table de référence "Pays" |

VARCHAR (2) |

O |

Identifiant lieu |

Identifiant du lieu de mouvement |

VARCHAR (25) |

O |

Type mouvement |

Type de mouvement

Source : Table de référence "Type Mouvement" |

VARCHAR (1) |

O |

Date |

Date du mouvement |

DATETIME |

O |

Nom transporteur |

Nom du transporteur |

VARCHAR (80) |

O |

Numéro agrément |

Numéro d'agrément du transporteur :

Source : Table de référence "Transporteurs" |

VARCHAR (45) |

O |

Numéro immatriculation |

N° d'immatriculation du camion |

VARCHAR (25) |

O |

Code pays OT |

Code pays de l'opérateur de transport

Source : table de référence "Pays" |

VARCHAR (2) |

O |

Identifiant OT |

Identifiant de l'opérateur

Source : table de référence : "Opérateurs de transport" |

VARCHAR (12) |

O |

Camion vide avant |

Camion vide avant le mouvement (oui ou non) |

NUMERIC (2) |

F |

Camion vide après |

Camion vide après le mouvement (oui ou non) |

NUMERIC (2) |

F |

Délégation |

Délégation de notification (oui ou non) |

NUMERIC (2) |

O |

Nombre d'animaux |

Nombre d'animaux déplacés |

NUMERIC (4) |

O |

Type d'animaux |

Type d'animaux déplacés :

Source : table de référence "Type animaux" |

VARCHAR (2) |

O |

Ordre chrono |

Ordre chronologique du mouvement dans la tournée |

NUMERIC (3) |

F |

Délai notification |

Délai de notification du mouvement (en jours) |

NUMERIC (3) |

O |

Typologie mouvement |

Typologie de mouvement :

Source : table de référence Typologie_Mouvements |

VARCHAR (2) |

O |

Identifiant tournée |

Identifiant unique de la tournée |

NUMERIC (6) |

F |

2. Transporteurs

Attribut |

Description |

Format |

Type (obligatoire,

facultatif) |

Numéro d'agrément |

N° d'agrément du transporteur |

VARCHAR (14) |

F |

Date d'agrément |

Date d'agrément |

DATETIME |

F |

Autorité |

Autorité de dé livraison de l'agrément |

VARCHAR (80) |

F |

Raison sociale |

Nom de société de transport |

VARCHAR (80) |

F |

Nom transporteur |

Nom du transporteur |

VARCHAR (30) |

O |

Prénom transporteur |

Prénom du transporteur |

VARCHAR (30) |

F |

N° immatriculation |

N° d'immatriculation du véhicule |

VARCHAR (25) |

O |

Type de véhicule |

Type de véhicule (remorque, camion…) |

VARCHAR (16) |

F |

3. Opérateurs de transport

Attribut |

Description |

Format |

Type (obligatoire,

facultatif) |

Code pays |

Code pays de l'opérateur

Source : table de référence "Pays" |

VARCHAR (2) |

O |

Identifiant |

Identifiant unique de l'opérateur |

VARCHAR (12) |

O |

Nom |

Nom de l'opérateur |

VARCHAR (30) |

O |

4. Sites d'élevage étrangers

Attribut |

Description |

Format |

Type (obligatoire,

facultatif) |

Code pays |

Code Pays du site

Source : table de référence "Pays" |

VARCHAR (2) |

O |

Identifiant |

Identifiant du site |

VARCHAR (12) |

O |

Adresse |

Adresse du site |

VARCHAR (30) |

O |

5. Tables de références

Table |

Attribut |

Libellé |

Format |

Type (obligatoire, facultatif) |

Pays |

Code |

Code pays |

VARCHAR (2) |

O |

Libellé |

Libellé pays |

VARCHAR (45) |

O |

Type lieu |

Code |

Code type lieu |

VARCHAR (1) |

O |

Libellé |

Libellé type lieu |

VARCHAR (45) |

O |

Type mouvement |

Code |

Code type mouvement |

VARCHAR (1) |

O |

Libellé |

Libellé type mouvement |

VARCHAR (45) |

O |

Typologie mouvement |

Code |

Code typologie mouvement |

VARCHAR (2) |

O |

Libellé |

Libellé typologie mouvement |

VARCHAR (45) |

O |

Type animaux |

Code |

Code type animaux |

VARCHAR (2) |

O |

Libellé |

Libellé type animaux |

VARCHAR (45) |

O |

6. Contenu des tables de référence

Table |

Code |

Libellé |

Pays |

Dernière liste à jour ISO (2 alphanumériques) prise en compte. |

Type lieu |

S |

Site |

E |

N° EDE d'une exploitation hors élevage |

C |

Immatriculation d'un camion |

Type mouvement |

C |

Chargement |

D |

Déchargement |

Typologie mouvement |

TR |

Tournée |

MI |

Mouvement Isolé |

LO |

Déduit d'un lot |

RC |

Lot avec rupture de charge |

Type animaux |

08 |

Porcelets 8 kg |

25 |

Porcelets 25 kg |

CH |

Porcs charcutiers |

RP |

Reproducteurs |

RF |

Réforme |

MO |

Morts transport |

MQ |

Manquants |

SA |

Sangliers |

B. Mise à disposition pour le système d'information de l'alimentation

- ces données sont transmises depuis la base de données nationale de traçabilité des porcins vers le système d'information de l'alimentation et vers les systèmes désignés par le ministère en charge de l'agriculture ;

- les flux mis en place dans ce cadre sont les suivants :

- un flux d'initialisation (T0) destiné à transmettre les données de mouvements collectées durant les 5 dernières années ainsi que les tables de référence ;

- un flux différentiel de création ou de mise à jour de mouvement. La fréquence d'envoi des informations par ce flux est déterminée par le ministère chargé de l'agriculture et pourra aller jusqu'à consister en un flux unitaire à chaque création ou mise à jour ;

- une opération de comparaison des contenus des deux bases est réalisée une fois par an au moins. Elle pourra conduire, au besoin, à lancer un flux de rephasage spécifique pour aligner les données des deux bases ;

- dans le cadre du lancement du programme SINEMA, ces données seront revues, complétées et transmises depuis la base de données nationale de traçabilité des porcins vers le système d'information de l'alimentation.

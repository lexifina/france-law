# Article Annexe 3

DONNÉES RELATIVES À LA DÉCLARATION D'ACTIVITÉ DES SITES D'ÉLEVAGE PORCIN

A. Dictionnaire des données

1. Déclaration d'activité

Attribut |

Description |

Format |

Type (obligatoire,

facultatif) |

Code pays site |

Code pays site d'élevage (= FR) |

VARCHAR (2) |

O |

Identifiant site |

Identifiant (indicatif de marquage) du site d'élevage |

VARCHAR (12) |

O |

Type porcin |

Source : table de référence "Type porcins" |

VARCHAR (3) |

O |

Type production |

Source : table de référence "Type production" |

VARCHAR (3) |

O |

Type élevage |

Source : table de référence "Type élevage" |

VARCHAR (2) |

O |

Mode élevage plein-air |

Source : table de référence "Mode élevage plein air" |

VARCHAR (2) |

O |

Nb places reproducteurs |

|

NUMERIC (5) |

O |

Nb places post-sevrage |

|

NUMERIC (5) |

O |

Nb places engraissement |

|

NUMERIC (5) |

O |

Date déclaration d'activité |

|

DATETIME |

O |

2. Tables de référence

Table |

Attribut |

Libellé |

Format |

Type (obligatoire, facultatif) |

Type porcin |

Code |

Code type porcin |

VARCHAR (3) |

O |

Libellé |

Libellé type porcin |

VARCHAR (45) |

O |

Type production |

Code |

Code type production |

VARCHAR (3) |

O |

Libellé |

Libellé type production |

VARCHAR (45) |

O |

Type élevage |

Code |

Code type élevage |

VARCHAR (2) |

O |

Libellé |

Libellé type élevage |

VARCHAR (45) |

O |

Mode élevage plein air |

Code |

Code mode d'élevage plein air |

VARCHAR (2) |

O |

Libellé |

Libellé mode d'élevage plein air |

VARCHAR (45) |

O |

3. Contenu des tables de référence

Table |

Code |

Libellé |

Type porcin |

PO |

Porcs |

SAB |

Sangliers catégorie B (boucherie, autres) |

SAA |

Sangliers de catégorie A (repeuplement) |

Type production |

PR |

Production de rente (animaux commercialisés) |

SE |

Sélection |

MU |

Multiplication |

CI |

Centre Insémination |

PRF |

Production familiale (consommation personnelle) |

HAR |

Hors animaux de rente (non consommés) |

SA |

Sangliers |

Type élevage |

NA |

Naisseur |

NP |

Naisseur - Post-sevreur |

EN |

Engraisseur |

NE |

Naisseur - Engraisseur |

PE |

Post-sevreur - Engraisseur |

PS |

Post-sevreur |

QN |

Quarantaine |

CC |

Centre de collecte |

AC |

Porcs d'agréments (animal de compagnie) |

LE |

Porcs d'exposition (parc, refuge, zoo…) |

LR |

Laboratoire/recherche |

SA |

Sangliers |

Mode élevage plein air |

NO |

Non |

NA |

Naissage < 4 semaines |

NP |

Naissage - Post-sevrage |

NE |

Naissage - Engraissement |

PS |

Post-sevrage |

PE |

Post-sevrage - Engraissement |

EN |

Engraissement |

TO |

Totalité |

B. Mise à disposition pour la DGAL

- ces données sont transmises depuis la base de données nationale de traçabilité des porcins vers le système d'information de la DGAL et vers les systèmes désignés par le ministère en charge de l'agriculture ;

- les flux mis en place dans ce cadre sont les suivants :

- un flux d'initialisation (T0) destiné à transmettre les données relatives à la déclaration d'activité telles qu'enregistrées au moment du T0 ainsi que les tables de référence ;

- un flux différentiel de création ou de mise à jour relatives à la déclaration d'activité. La fréquence d'envoi des informations par ce flux est déterminée par le ministère chargé de l'agriculture et pourra aller jusqu'à consister en un flux unitaire à chaque création ou mise à jour ;

- une opération de comparaison des contenus des bases source et cible est réalisée une fois par an au moins. Elle pourra conduire, au besoin, à lancer un flux de rephasage spécifique pour aligner les données dans ces bases.

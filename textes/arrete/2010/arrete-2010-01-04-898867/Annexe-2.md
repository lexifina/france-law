# Article Annexe 2

ALGORITHME DE CALCUL DE CLÉ MODULO 23

1. Si la zone ROLDEB (début du numéro de dette) n'est pas numérique, la remplacer par "00".

2. Diviser l'association des zones Exercice (2 derniers chiffres de ROLEX), code facture (ROLPER), numéro de dette (ROLDEB, ROLDET), soit un ensemble de 18 caractères, par 23.

Le reste de la division = R.

Calculer K = R + 1 et rechercher la correspondance dans la table suivante :

K=

|

1

|

2

|

3

|

4

|

5

|

6

|

7

|

8

|

9

|

10

|

11

|

12

|

13

|

14

|

15

|

16

|

17

|

18

|

19

|

20

|

21

|

22

|

23

|

clé

|

A

|

B

|

C

|

D

|

E

|

F

|

G

|

H

|

J

|

K

|

L

|

M

|

N

|

P

|

Q

|

R

|

S

|

T

|

U

|

V

|

W

|

X

|

Y

|

NB : Difficultés pouvant survenir lors du calcul de la lettre clé :

Dans l'hypothèse de système limitant à moins de 18 caractères les zones numériques, il conviendra de découper en 2 × 9 caractères l'ensemble : exercice, code facture, numéro d'ordre.

Le premier sous-ensemble de 9 caractères sera divisé par 23.

Le reste de cette division sera accolé devant le deuxième sous-ensemble de 9 caractères, le tout (dividende de 11 caractères au minimum) sera divisé par 23. Le reste de cette dernière division = R.

Description des zones du fichier ROLMRE

Vous pouvez consulter le tableau dans le

JOn° 51 du 02/03/2010 texte numéro 2

Vous pouvez consulter le tableau dans le

JOn° 51 du 02/03/2010 texte numéro 2

Développement du fichier ROLMRE

Création d'articles de code 2, 3 et 4

I. - Présentation générale

Jusqu'à présent, le protocole ROLMRE n'a comporté qu'un seul type d'article :

- répondant à la fonction initiale du fichier de liaison, la transmission de dettes à prendre en charge dans les applications du Trésor ;

- de code mouvement ROLMVT égal à 1 (cf. 311).

Depuis 1999, d'autres types d'article ont été créés, afin de gérer des fonctionnalités nouvelles des applications.

Cependant, il est important de noter que l'article de code 1, dans sa présente version adaptée à l'euro et à l'an 2000, ne sera pas modifié et permettra toujours les traitements courants des applications.

Les nouveaux développements de l'application EAU concernent :

- La gestion d'un compte client :

articles de code 2 : initialisation (= attribution) du numéro de compte client.

articles de code 3 : modification du numéro de compte client.

- La mise en place de prélèvements périodiques :

articles de code 4 : re-présentation d'un prélèvement préalablement rejeté.

Ces nouveaux articles ont les caractéristiques communes suivantes :

- ils sont de structure strictement identique à celle des articles de code 1 ;

- ils se rapportent toujours à une dette déjà prise en charge dans les applications.

1. La gestion d'un code client.

L'arrêté du 10 juillet 1996 relatif aux factures de distribution de l'eau et de collecte et de traitement des eaux usées dispose, entre autres, qu'à chaque nouvelle facturation le solde restant dû sur les précédentes factures doit être rappelé .

Permettre à l'ordonnateur de disposer des éléments de calcul de ce solde restant dû a donné lieu, dans un premier temps, à la création du fichier retour FLUOR.

Pour que ce dispositif fonctionne correctement et afin de pouvoir imputer sur les dettes antérieures non soldées le reliquat des sommes versées par l'usager, il est nécessaire de disposer d'un identifiant stable de ce dernier.

Cette information est fournie par le numéro de compte client (rubrique ROLCLI, cf. § 3196).

Dette à prendre en charge :

le numéro de compte client est transmis, en même temps que les autres éléments de cette dette, par un article de code 1.

Dette déjà prise en charge, sans numéro de compte client :

il est créé, spécialement à cet usage, un article de code 2 : initialisation du numéro de compte client.

Dette déjà prise en charge, avec numéro de compte client erroné :

il est créé spécialement un article de code 3 : modification du numéro de compte client.

2. La mise en place des prélèvements périodiques.

Il s'agit de permettre au redevable de régler en plusieurs fois ses factures d'eau et d'assainissement.

Dans les applications, le système de transmission des fichiers ROLMRE est le suivant :

- chaque prélèvement à l'échéance est considéré comme une dette normale , faisant l'objet d'un rôle et transmise par un article de code 1 ;

- en cas de rejet du prélèvement, la dette correspondante doit être représentée à l'échéance suivante, pour faire l'objet d'un nouveau prélèvement : pour cela il est créé un article de code 4 qui n'a pas à être pris en charge.

En particulier, tout rejet étant total, les montants représentés doivent être identiques à ceux pris en charge.

Dans chacun de ces articles de code 1 ou 4, le code monnaie ROLMONNAIE doit être servi de façon à préciser si le prélèvement s'effectuera sur un compte tenu en euros (ROLMONNAIE = E ) ou en francs (ROLMONNAIE = F ).

II. - Constitution des nouveaux types d'article

Les rubriques à servir obligatoirement sont indiquées dans le tableau ci-dessous.

Description des zones du fichier ROLMRE

Vous pouvez consulter le tableau dans le

JOn° 51 du 02/03/2010 texte numéro 2

Vous pouvez consulter le tableau dans le

JOn° 51 du 02/03/2010 texte numéro 2

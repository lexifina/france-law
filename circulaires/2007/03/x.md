# CAHIER DES CHARGES DU DISPOSITIF DE DIAGNOSTIC DES SYSTEMES EMBARQUES DE CONTROLE DES EMISSIONS DU VEHICULE

- État : en vigueur (publiée)
- NOR : -
- Numéro : SR / V / 037
- Date de signature : 2007-03-01
- Mise en ligne : 2009-03-31
- Ministères : 5
- Domaines : Ecologie, développement durable, Transports, équipement, logement, tourisme, mer
- Mots-clés : Energie, environnement; Energie_environnement ; Energie_Climat ; Véhicules
- Annexes : 0
- Cerfa : -
- Identifiant : 26598 (PDF officiel : pdf/2009/03/cir_26598.pdf)

## Texte

Transports
INSTRUCTION TECHNIQUE
B
1/9
SR / V / 037
CAHIER DES CHARGES DU DISPOSITIF DE DIAGNOSTIC
DES SYSTEMES EMBARQUES DE CONTROLE DES
EMISSIONS DU VEHICULE
01/03/2007
SOMMAIRE
1.
OBJET ET DOMAINE D'APPLICATION.............................................................................................................. 1
2.
REFERENCES NORMATIVES ET REGLEMENTAIRES ................................................................................... 2
3.
DEFINITIONS ......................................................................................................................................................... 3
3.1 – Code d’erreur............................................................................................................................................................. 3
3.2 – Système OBD ............................................................................................................................................................ 4
3.3 – Constructeur............................................................................................................................................................... 4
4.
SPECIFICATIONS RELATIVES A L’ARCHITECTURE PRODUIT .................................................................. 4
5.
SPECIFICATIONS RELATIVES AU MODE OPERATOIRE .............................................................................. 5
6.
SPECIFICATIONS RELATIVES A l’ENVIRONNEMENT.................................................................................. 6
7.
SPECIFICATIONS RELATIVES A L’ALIMENTATION ELECTRIQUE ........................................................... 6
8.
SPECIFICATIONS RELATIVES A LA CONNEXION AVEC LE VEHICULE .................................................. 6
9.
SPECIFICATIONS RELATIVES A LA RECONNAISSANCE DES PROTOCOLES ......................................... 6
10.
AcQUISITION, TRAITEMENT ET AFFICHAGE................................................................................................. 7
11.
FONCTIONNALITE ............................................................................................................................................... 7
12.
TRACABILITE DE L’ESSAI.................................................................................................................................. 7
13.
SPECIFICATIONS RELATIVES A LA MISE A JOUR DES INFORMATIONS TECHNIQUES....................... 8
14.
DOCUMENTATION............................................................................................................................................... 9
15.
EVOLUTIONS DE L’APPAREIL........................................................................................................................... 9
__________________________________________________________________________
1. OBJET ET DOMAINE D'APPLICATION
La présente instruction technique a pour objet de définir le cahier des charges du dispositif de
diagnostic des systèmes embarqués de contrôle des émissions polluantes des véhicules légers
conformément aux dispositions du point 1.6.3. de l'annexe 3 de l'arrêté du 18 juin 1991 modifié et les
spécifications de l’option complémentaire qui peut être proposée pour les véhicules lourds.
Elle annule et remplace l’instruction technique SR/V/037 indice A à compter du 01/03/2007.
Un dispositif de diagnostic des systèmes embarqués de contrôle des émissions polluantes du véhicule
comprend :
a) Un système d'acquisition et d'affichage du résultat respectant les spécifications fonctionnelles de la
norme ISO 15031-4 "Véhicules routiers - Communication entre un véhicule et un équipement externe
pour le diagnostic relatif aux émissions - Partie 5: Services de diagnostic relatif aux émissions" .
b) Un système de connexion entre le lecteur et l’interface du véhicule pour les véhicules légers.
c) Un système de connexion entre le lecteur et l’interface du véhicule pour les véhicules lourds
lorsque l’option complémentaire est proposée.

Transports
INSTRUCTION TECHNIQUE
B
2/9
SR / V / 037
CAHIER DES CHARGES DU DISPOSITIF DE DIAGNOSTIC
DES SYSTEMES EMBARQUES DE CONTROLE DES
EMISSIONS DU VEHICULE
01/03/2007
Ce dispositif doit être conforme :
- Aux exigences essentielles de sécurité et de santé spécifiées dans l'Article R 233.83 
"Equipements de travail et moyens de protection".
- Aux spécifications particulières définies ci-après.
Ces équipements doivent faire l’objet d’un marquage CE.
2. REFERENCES NORMATIVES ET REGLEMENTAIRES
La présente instruction technique comporte par référence des dispositions d'autres publications. 
Directive 70/220/CE et ses amendements
Concernant le rapprochement des législations des Etats membres relatives aux mesures à prendre
contre la pollution de l’air par les émissions des véhicules à moteur
Directive 2005/55/CE et ses amendements
concernant le rapprochement des législations des États membres relatives aux mesures à prendre
contre les émissions de gaz polluants et de particules polluantes provenant des moteurs à allumage par
compression destinés à la propulsion des véhicules et les émissions de gaz polluants provenant des
moteurs à allumage commandé fonctionnant au gaz naturel ou au gaz de pétrole liquéfié et destinés à
la propulsion des véhicules
Norme ISO 15031
"Véhicules routiers - Communication entre un véhicule et un équipement externe pour le diagnostic
relatif aux émissions "
ISO 9141-2: 1994 (modifié en 1996)
"Véhicules routiers - Systèmes de diagnostic - Partie 2: Caractéristiques CARB de l’échange de
données numériques"
SAE J 1850: mars 1998 
Communication de données de classe B "Interface de réseau". Les messages relatifs aux émissions
doivent utiliser le contrôle de redondance cyclique et l'en-tête à trois octets, mais pas la séparation
interoctets ni le total de contrôle 
ISO 14230
- Partie 4: "Véhicules routiers - Systèmes de diagnostic - Protocole "Keyword 2000" - Partie 4:
Exigences pour les systèmes relatifs aux émissions" 

Transports
INSTRUCTION TECHNIQUE
B
3/9
SR / V / 037
CAHIER DES CHARGES DU DISPOSITIF DE DIAGNOSTIC
DES SYSTEMES EMBARQUES DE CONTROLE DES
EMISSIONS DU VEHICULE
01/03/2007
ISO 15765-4
 "Véhicules routiers - Systèmes de diagnostic sur CAN - Partie 4: Exigences pour les systèmes relatifs
aux émissions" .
SAE J2012
- Diagnostic Trouble Code Définitions Equivalent to ISO 15031-6". 
SAE J1939
- Recommanded Practice for a Serial Control and Communications Vehicle Network" .
SAE J1939-13
- Off board Diagnostic Connector
SAE J1939-73
- Application layer - Diagnostics
Article R233.83 relatif aux équipements de travail et moyens de protection.
ARRETE du 18 juin 1991 modifié relatif à la mise en place et à l'organisation du Contrôle Technique
des véhicules dont le poids n'excède pas 3,5 tonnes.
3. DEFINITIONS
3.1 – Code d’erreur
Les erreurs sont enregistrées en utilisant des codes d’erreur conformes à ceux figurant au point 6. 3 de
la norme ISO 15031-6 "Véhicules routiers - Communication entre un véhicule et un équipement
externe pour le diagnostic relatif aux émissions - Partie 6: Définition des codes d’anomalie"
concernant les "codes d’anomalie du système de diagnostic relatif aux émissions". Si cela est
impossible, le constructeur peut utiliser des codes d’anomalie visés aux points 5. 3 et 5. 6 de la norme
ISO 15031-6.
Des codes supplémentaires peuvent être fournis en unités normalisées sur la base des spécifications
données au point 6. 5. 3 du présent appendice 1 de l’annexe XI de la directive 70/220 modifiée. Dans
ce cas, les signaux effectifs doivent être clairement identifiés et séparément des codes erreurs.
Pour l’option complémentaire (PL), le constructeur peut également utiliser les codes défauts prescrits
par les normes SAE J2012 ou SAE J1939-13

Transports
INSTRUCTION TECHNIQUE
B
4/9
SR / V / 037
CAHIER DES CHARGES DU DISPOSITIF DE DIAGNOSTIC
DES SYSTEMES EMBARQUES DE CONTROLE DES
EMISSIONS DU VEHICULE
01/03/2007
3.2 – Système OBD
 Le système OBD est un système de diagnostic embarqué pour contrôle des émissions, capable de
déceler l’origine probable d’un dysfonctionnement au moyen de codes d’erreurs stockés dans le ou les
calculateurs du véhicule.
 Le système OBD doit surveiller les défauts suivants :

- D’une part :

- L’efficacité du catalyseur (E/D)*

- Le fonctionnement et l’intégrité du filtre à particules (D)*

- Le fonctionnement du système d’alimentation en carburant (E/D)*

- Le fonctionnement des sondes à oxygène (E)*

- La présence de ratés de combustion (E)*
- Tous les autres composants du GMP (moteur et boite de vitesse) relatifs aux
émissions et connectés à un ordinateur dont la défaillance peut entraîner des émissions
supérieures aux seuils OBD (E/D)*
- D’autre part, la continuité électrique de tous les composants du GMP
*E : Essence / D : Diesel
3.3 – Constructeur
Fabricant du dispositif de diagnostic des systèmes embarqués de contrôle des émissions polluantes, ou
son représentant.
4. SPECIFICATIONS RELATIVES A L’ARCHITECTURE PRODUIT
 Le diagnostic des systèmes embarqués de contrôle des émissions polluantes d’un véhicule doit
comporter :
• une solution d’affichage (intégrée ou déportée)
• une solution d’acquittement (intégrée ou déportée)
• une solution de saisie (intégrée ou déportée)
• une solution de transfert des données vers l’informatique du centre (intégrée ou déportée) et
une solution d’impression (intégrée ou déportée)
• un mode CT / DIAG avec un verrouillage du mode contrôleur (codification d’un message sur
le rapport d’impression indiquant que le mode contrôleur a été déverrouillé) afin de n’avoir
accès qu’aux services définis dans la norme ISO 15031 : 1 (Données courantes), 3 (Codes
défauts mémorisés), 9 (VIN, etc.).
• une plaque d’identification : marque, type, numéro de série, plage de tension d’alimentation,
N° du certificat de qualification et la ou les catégories de véhicules pour lequel il a été qualifié
(Véhicules légers / Véhicules lourds). 

Transports
INSTRUCTION TECHNIQUE
B
5/9
SR / V / 037
CAHIER DES CHARGES DU DISPOSITIF DE DIAGNOSTIC
DES SYSTEMES EMBARQUES DE CONTROLE DES
EMISSIONS DU VEHICULE
01/03/2007
5. SPECIFICATIONS RELATIVES AU MODE OPERATOIRE
Action 
Message scantool
Interface opérateur
1- Connexion de l’appareil
2- Contact ON
Acquittement de la connexion*
3- Identification véhicule
N° d’immatriculation
Saisie ou sélection du véhicule
4-
Interrogation 
contrôleur 
sur
l’état visuel du témoin OBD
(MIL) A/E
Réponse du contrôleur O/N
Si N : arrêt procédure (ligne 5)
Si O : aller ligne 6
5-
Arrêt procédure (Aller ligne 10)
ou attente démarrage moteur
6-Démarrage moteur
Moteur démarré : acquittement*
7- Départ des 3 minutes** de
test (au maximum)
Reconnaissance 
du 
(des)
protocole(s) O/N
Si 
O : 
affichage 
du 
(des)
protocole(s)
Si N : Aller au 10 (message
protocole non reconnu)
8- 
Tests en cours, interrogation et
remontée des informations (§ 10
du cahier des charges)
9- Fin des 3 minutes de test (au
maximum) 
à 
l’affichage 
du
message d’interrogation
Interrogation 
contrôleur 
sur
l’état visuel du témoin OBD
(MIL) A/E/CP
Sélection par le contrôleur de
l’état du témoin OBD (MIL)
10- 
Message 
Système 
OBD
Conforme / Système OBD non-
conforme 
/ 
Protocole 
non
reconnu
Transfert 
et 
affichage 
de
l’ensemble 
des 
informations
référencées au § 10 du cahier des
charges
11-
Impression ou Transfert des
informations
Accusé 
de 
transmission
conforme avec demande de
relance si échec
12-
Procédure terminée
13- Contact OFF
14-Déconnexion de l’appareil
* Dans le cas d’un acquittement automatique, l’appareil doit impérativement disposer d’une
fonction acquittement manuel
** Dès que la remontée des informations est effective, le test peut être suspendu, il n’est pas
nécessaire d’afficher le temps écoulé. 
Nota : En cas d’interruption de liaison, l’essai complet doit être renouvelé (phase 1). 

Transports
INSTRUCTION TECHNIQUE
B
6/9
SR / V / 037
CAHIER DES CHARGES DU DISPOSITIF DE DIAGNOSTIC
DES SYSTEMES EMBARQUES DE CONTROLE DES
EMISSIONS DU VEHICULE
01/03/2007
6. SPECIFICATIONS RELATIVES A L’ENVIRONNEMENT
Le fabricant doit apporter la preuve de la conformité CE de l’appareil, et en particulier les normes
CEM applicables.
7. SPECIFICATIONS RELATIVES A L’ALIMENTATION ELECTRIQUE
Le dispositif de diagnostic des systèmes embarqués de contrôle des émissions polluantes doit pouvoir
être alimenté par la prise OBD d’un véhicule léger et d’un véhicule lourd si l’option complémentaire
est proposée. Il doit, en outre, disposer d’une alimentation indépendante pour garantir l’alimentation
du dispositif quelque soit le véhicule.
8. SPECIFICATIONS RELATIVES A LA CONNEXION AVEC LE VEHICULE
Le système de connexion entre le lecteur et l’interface du véhicule doit respecter les prescriptions des
normes :
- 
Pour les véhicules légers : ISO 15031-3 et SAE J1962.
- 
Pour les véhicules lourds : ISO 15031-3 et SAE J1939-13.
9. SPECIFICATIONS 
RELATIVES 
A 
LA 
RECONNAISSANCE 
DES
PROTOCOLES
Le dispositif de diagnostic des systèmes embarqués de contrôle des émissions polluantes doit
sélectionner automatiquement le SERVICE 01 "Données courantes" dans le système OBD de l'unité
de commande.
Le lecteur doit interroger les protocoles admissibles dans l'ordre suivant :
1. 
ISO 9141-2 5-Baud
2. 
ISO 14230-4 (Protocole Keyword 2000) 5-Baud
3. 
ISO 14230-4 (Protocole Keyword 2000) Fast
4. 
SAE J1850 PWM
5. 
SAE J1850 VPW
6. 
ISO 15765-4 (CAN) 11 bits {250 – 500 kbits/s}
7. 
ISO 15765-4 (CAN) 29 bits {250 – 500 kbits/s} 
8. 
SAE J1939 (pour les véhicules lourds, si l’option complémentaire est proposée)
Certains véhicules peuvent présenter plusieurs protocoles différents intégrés. Cette situation demande à
ce que le dispositif de diagnostic des systèmes embarqués de contrôle des émissions polluantes balaye
systématiquement l’ensemble des protocoles.
Tous les protocoles de communication admissibles selon la directive 70/220 et ses amendements
(dans leur version en vigueur à la date de publication de la présente SR/V) doivent être reconnus
automatiquement.

Transports
INSTRUCTION TECHNIQUE
B
7/9
SR / V / 037
CAHIER DES CHARGES DU DISPOSITIF DE DIAGNOSTIC
DES SYSTEMES EMBARQUES DE CONTROLE DES
EMISSIONS DU VEHICULE
01/03/2007
Le dispositif de diagnostic des systèmes embarqués de contrôle des émissions polluantes doit indiquer
le type de protocole utilisé.
10. ACQUISITION, TRAITEMENT ET AFFICHAGE
Le dispositif de diagnostic des systèmes embarqués de contrôle des émissions polluantes doit
permettre la consultation à l’écran :
• Le VIN du véhicule contrôlé (si présent au calculateur dans le respect du format normalisé) ;
• Les codes erreurs confirmés (sans libellé) ;
• La somme des codes erreurs confirmés ;
• L’état du témoin OBD (MIL) au calculateur ; 
• La distance parcourue par le véhicule depuis l’allumage du témoin OBD (MIL), si présent ;
• Les conditions de fonctionnement du moteur (mesures courantes : températures eau - huile,
régime moteur).
• Pour les véhicules lourds (si l’option complémentaire est proposée), le(s) numéro(s)
d’homologation calculateur(s), si présent(s) dans le respect du format normalisé. 
11. FONCTIONNALITE
Le dispositif de diagnostic des systèmes embarqués de contrôle des émissions polluantes ne doit pas
permettre dans sa configuration « CT : contrôle technique » de modifier les informations relevées et
d’effacer des données.
La mise en œuvre du dispositif dans une configuration autre que « contrôle technique » ne doit pas
être possible par l’opérateur.
12. TRACABILITE DE L’ESSAI
Le dispositif de diagnostic des systèmes embarqués de contrôle des émissions polluantes doit pouvoir
transmettre à un périphérique les paramètres suivants :
- 
Numéro d’immatriculation (O);
- 
Identification de la version du logiciel du dispositif de diagnostic des systèmes embarqués de
contrôle des émissions polluantes (O);
- 
Date et heure de l'essai (O) ;
- 
Numéro de série du véhicule (VIN), si présent au calculateur dans le respect du format
normalisé (O) ;
- 
Les codes erreurs confirmés sur l’ensemble des calculateurs (C) ;
- 
La somme des codes erreurs confirmés sur l’ensemble des calculateurs (O) ;
- 
L’état visuel du témoin OBD moteur à l’arrêt, contact sur ON : s’est allumé /est resté
éteint (O);
- 
L’état visuel du témoin OBD (MIL), moteur tournant : allumé / éteint / clignotant
permanent (O) ;

Transports
INSTRUCTION TECHNIQUE
B
8/9
SR / V / 037
CAHIER DES CHARGES DU DISPOSITIF DE DIAGNOSTIC
DES SYSTEMES EMBARQUES DE CONTROLE DES
EMISSIONS DU VEHICULE
01/03/2007
- 
L’état du statut du témoin OBD (MIL), au calculateur : allumé / éteint (O) ;
- 
La distance parcourue la plus élevée par le véhicule depuis l’allumage du témoin OBD au
calculateur, si présent (C);
- 
Les protocoles détectés dans l’étape 7 du mode opératoire décrit au § 5 suivant les modalités
ci-après (O) ;
N°
Protocole
Libellé affiché et imprimé
1
ISO 9141-2 5-Baud
ISO 9141
2
ISO 14230-4 (Protocole Keyword 2000) 5-Baud
ISO 14230-4 (Protocole Keyword 2000) Fast
ISO 14230
3
SAE J1850 VPW
SAE J1850 VPW
4
SAE J1850 PWM
SAE J1850 PWM
5
ISO 15765-4 (CAN) 11 bits {250 – 500 kbits/s}
ISO 15765-4 (CAN) 29 bits {250 – 500 kbits/s}
ISO 15765
6
SAE J1939 (pour les véhicules lourds, si l’option
complémentaire est proposée)
SAE J1939
- 
La conclusion du test : Système OBD conforme, Système OBD non-conforme, Protocole non
reconnu (O) ;
- 
L’indication du mode utilisé : MODE CT ou MODE DIAG (O) ;
- 
Le(s) numéro(s) d’homologation calculateur(s), si présent(s) dans le respect du format
normalisé (C) ;
- 
La ou les catégories de véhicules pour lesquelles l’appareil a été qualifié (TYPE VL ou TYPE
VL-PL) (O).
(O) Ligne obligatoire 
(C) Sous condition
Ces informations doivent être archivées avec les données informatiques du contrôle technique
correspondant ou imprimées sur un relevé.
13. SPECIFICATIONS RELATIVES A LA MISE A JOUR DES INFORMATIONS
TECHNIQUES
Le constructeur doit permettre une mise à jour des bases de données non réalisable par l’opérateur.
Elle doit être réalisable par le constructeur soit par télémaintenance soit par intervention de ses
représentants.

Transports
INSTRUCTION TECHNIQUE
B
9/9
SR / V / 037
CAHIER DES CHARGES DU DISPOSITIF DE DIAGNOSTIC
DES SYSTEMES EMBARQUES DE CONTROLE DES
EMISSIONS DU VEHICULE
01/03/2007
14. DOCUMENTATION
Chaque dispositif de diagnostic doit être associé à une documentation complète rédigée en langue
française comprenant au minimum :
1. Une notice d'utilisation décrivant de manière précise les modalités des différentes opérations
possibles et attirant l'attention de l'utilisateur sur les risques que peut présenter une mauvaise
utilisation du dispositif.
2. Copie du certificat de qualification de type délivré par l’organisme désigné par le ministère
chargé des transports mentionnant la ou les catégories de véhicules pour lesquels l’appareil a
été qualifié (Véhicules légers, Véhicules lourds).
3. Attestation du constructeur justifiant de la conformité de l’appareil livré par rapport au type
qualifié.
15. EVOLUTIONS DE L’APPAREIL
La gestion des versions majeures et mineures du logiciel doit être définie dans le dossier de
présentation.
Les évolutions majeures sont soumises à un nouvel essai réalisé par l’organisme désigné par le
ministère chargé des transports.
Les évolutions mineures doivent faire l’objet d’une déclaration auprès de l’organisme désigné par le
ministère chargé des transports qui a délivré le certificat de qualification de type.
Bernard GAUVIN
 Ingénieur général des mines

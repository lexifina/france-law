# Article Annexe

MODALITÉS DE PRISE EN COMPTE DU SYSTÈME COMBINEO DANS LA RÉGLEMENTATION THERMIQUE 2005

1. Définition du système COMBINEO

Au sens du présent arrêté, le système COMBINEO, modèle 185 LS, est un système compact, capable de réaliser la ventilation, le chauffage et la production d'eau chaude sanitaire. Il fonctionne avec une pompe à chaleur puisant ses calories sur l'air extrait. La production d'eau chaude sanitaire se fait en priorité par rapport au chauffage.

Ce système assure le besoin de régénération de l'air du bâtiment et le besoin de chauffage par ventilation mécanique contrôlée de type double flux thermodynamique.

Une grande partie de l'énergie perdue à travers l'extraction de l'air est récupérée via un échangeur statique et transmise à l'air neuf réinjecté dans le bâtiment.

L'énergie complémentaire nécessaire au maintien en température du bâtiment est apportée par une pompe à chaleur dont le condenseur est placé dans le flux d'air neuf, après l'échangeur statique.

Les besoins supplémentaires de chauffage du bâtiment lors des périodes hivernales fortes (cas de l'insuffisance de la pompe à chaleur) sont générés par un système d'appoint par effet joule piloté par COMBINEO, situé dans les pièces de vie (séjour, salon) et dans les salles de bain, couvrant a minima l'intégralité des déperditions de ces pièces.

COMBINEO assure la production d'eau chaude sanitaire, stockée dans un ballon émaillé.

L'énergie nécessaire au chauffage de l'eau chaude sanitaire est apportée par la pompe à chaleur qui va puiser les calories de l'air extrait du bâtiment à travers un échangeur pour les restituer dans un condenseur au contact du ballon de stockage.

En cas de besoin supplémentaire ponctuel de production d'eau chaude (cas de fort tirage sur une période courte), l'appoint de chauffage de l'eau est réalisé par un élément chauffant électrique direct, intégré au ballon de stockage de COMBINEO.

2. Domaine d'application

Cette méthode s'applique uniquement aux maisons individuelles répondant aux critères suivants :

Surface habitable ≤ 200 m².

Typologies de maison : T3 à T6, avec un débit total extrait ≤ 240 m³/h.

Déperditions par le bâti : Coefficient HT (HT = Ubat * Senveloppe) inférieur ou égal aux valeurs indiquées dans le tableau 1, où :

Ubat représente le coefficient moyen de déperdition par les parois et les baies du bâtiment défini à l'article 15 de l'arrêté du 24 mai 2006 susvisé ;

Senveloppe représente la surface totale des parois déperditives du bâtiment.

Tableau 1. Seuils du coefficient HT max

ZONE CLIMATIQUE

|

H1

|

H2

|

H3

|

HT max (en W/K)

|

100 |

110 |

120 |

Perméabilité à l'air : Q4Pa_surf ≤ 0,60 m³/h/m².

Ambiance régulée par zone de 100 m² maximum.

Zone de bruit BR1 pour les maisons équipées du modèle COMBINEO avec by-pass manuel de l'échangeur.

3. Méthode de prise en compte dans les calculs pour la partie non directement modélisable

La présente méthode propose l'intégration du système COMBINEO, dans la méthode de calcul Th-C-E, en trois phases :

1. Le prétraitement qui permet :

― de calculer la part de chauffage du système COMBINEO et celle de l'appoint (salon + salle de bains), notées βCH_COMBINEO, βCH_appoint_SALON et βCH_appoint_SDB

― de calculer les coefficients correctifs des consommations énergétiques d'ECS et d'auxiliaires de ventilation, notés aECS et aVENT

2. Les données à saisir dans la méthode de calcul Th-C-E afin de caractériser le système COMBINEO avec son appoint. Ces données sont issues du prétraitement.

3. Le post-traitement qui permet de corriger les consommations énergétiques d'ECS et d'auxiliaires de ventilation à partir des coefficients aECS et aVENT.

3.1. Prétraitement

La production d'ECS étant prioritaire sur le chauffage, il y a besoin d'une énergie d'appoint pour assurer le chauffage pendant les heures de production d'ECS.

Il est donc nécessaire de déterminer heure par heure la part de chauffage assurée par le système COMBINEO et celle assurée par l'appoint.

3.1.1. Calcul de la part de chauffage assurée par le système COMBINEO et par l'appoint

3.1.1.1. Calcul des déperditions totales du bâtiment

Le calcul du coefficient de déperdition par le bâti s'effectue de la façon suivante :

HT = Ubat × Senveloppe (en W/K)

avec :

Ubat : coefficient moyen de déperdition par transmission à travers les parois déperditives séparant le volume chauffé du bâtiment de l'extérieur, du sol et des locaux non chauffés (en W/[m².K]) ;

Senveloppe : surface intérieure totale des parois qui séparent le volume chauffé de l'extérieur, du sol et les locaux non chauffés (en m²).

Le calcul du coefficient de déperdition par le renouvellement d'air du bâtiment s'effectue de la façon suivante :

HV = 0,34 × Qva × (1 ― 0,9 × hECH (en W/K)

avec :

hECH : Efficacité de l'échangeur (en %). Les valeurs sont disponibles dans le tableau 9 ;

Qva : débit spécifique moyen (en m³/h) qui s'exprime sous la forme suivante :

Qva = (Qv_pointe × Dugd + Qv_base × (168 ― Dugd))/168 (en m³/h)

avec :

Dugd : durée d'utilisation en grand débit. Ce coefficient est égal à 7 h/semaine ;

Qv_pointe et Qv_base : débits de pointe et de base définis selon la typologie du logement (en m³/h).

Le calcul des déperditions totales du bâtiment s'effectue de la façon suivante :

D(Text) = (HT + HV) × (uamb ― uext) (en W)

avec :

HT : coefficient de déperdition par le bâti (en W/K) ;

HV : coefficient de déperdition par le renouvellement d'air du bâtiment (en W/K) ;

uamb : température du local. Ce coefficient est égal à 19 °C en période d'occupation et à 16 °C en période d'inoccupation ;

uext : température extérieure (en °C).

3.1.1.2. Calcul de la puissance PAC chauffage disponible

Lorsqu'il y a production simultanée de chauffage et d'ECS, la PAC utilise en priorité tout ou partie de la puissance totale disponible pour produire l'ECS. Cette part de puissance, bECS_utilisée, s'exprime de la façon suivante :

Vous pouvez consulter le tableau dans le JO n° 292 du 17/12/2011 texte numéro 7

avec :

PECS : puissance du COMBINEO pour la production d'ECS (en W) ;

PECS_utilisée : puissance de la PAC utilisée pour la production d'ECS (en W).

La part de la puissance de la PAC disponible pour la production de chauffage est calculée de la façon suivante :

bCH_dispo = 1 ― bECS_utilisée

avec :

bECS_utilisée : part de la puissance de la PAC utilisée pour la production d'ECS (en %).

Le calcul de la puissance de la PAC disponible pour la production de chauffage s'effectue de la façon suivante :

PCH_dispo = PCH × bCH_dispo (en W)

avec :

PCH : puissance du COMBINEO pour la production de chauffage (en W) ;

bCH_dispo : part de la puissance de la PAC disponible pour la production de chauffage.

3.1.1.3. Calcul de la part de chauffage assurée par l'appoint

Lorsque PCH_dispo D(Text), l'appoint est nul.

Lorsque PCH_dispo ¸ D(Text), le calcul de la puissance de l'appoint nécessaire pour la production de chauffage s'effectue de la façon suivante :

PCH_appoint = D(Text) ― PCH_dispo (en W)

avec :

D(Text) : déperditions totales du bâtiment (en W) ;

PCH_dispo : puissance de la PAC disponible pour le chauffage (en W).

Le calcul de la part de chauffage assurée par l'appoint s'effectue de la façon suivante :

Vous pouvez consulter le tableau dans le JO n° 292 du 17/12/2011 texte numéro 7

avec :

PCH_appoint : puissance de l'appoint nécessaire pour la production de chauffage (en W) ;

D(Text) : déperditions totales du bâtiment (en W).

3.1.1.4. Calcul de la part de chauffage assurée par le système COMBINEO

Le calcul de la part de chauffage assurée par le système COMBINEO s'effectue de la façon suivante :

βCH_COMBINEO = 1 ― βCH_appoint

avec :

βCH_appoint : part de chauffage assurée par l'appoint (en %).

Les mois de juin, juillet, août et septembre sont considérés comme mois de non-chauffe.

3.1.1.5. Répartition du chauffage selon les pièces

Tableau 2. Répartition des parts d'appoint du chauffage selon les pièces

|

SALLE DE BAINS

|

SALON/SÉJOUR

|

TOUTES LES AUTRES PIÈCES

|

Type émetteur

|

Emetteur à effet joule direct |

Emetteur à effet joule direct |

COMBINEO |

Répartition

du chauffage

|

bch_appoint_SDB = SSDB/Shab

SSDB : surface de la salle de bains

Shab : surface habitable |

bch_appoint_SALON = bch_appoint ― bch_appoint_SDB |

bch_COMBINEO |

3.1.2. Calcul du coefficient correctif de la consommation énergétique d'ECS

3.1.2.1. Calcul des besoins horaires d'ECS

Le calcul des besoins d'ECS, au pas de temps horaire, s'effectue de la façon suivante :

Qw = rw × Cw × Vuw × (uuw ― ucw) × RatECS (en Wh)

avec :

rw : masse volumique de l'eau, rw = 1 kg/l ;

Cw : capacité calorifique massique de l'eau, Cw = 1,163 Wh/(kg.K) ;

uuw : température de l'eau chaude mitigée utilisée au puisage ;

ucw : température de l'eau froide entrant dans le système de préparation d'eau chaude ;

RatECS : ratio des besoins assurés par le système de production aux besoins totaux de la zone ;

Vuw : volume d'eau chaude mitigée utilisé chaque heure pendant la période normale. Ce coefficient est calculé comme suit :

Vuw = a × ah × Nu (en l)

avec :

a : besoins unitaires exprimés en litres d'eau à 40 °C ;

ah : coefficient horaire de la clé de répartition des besoins d'ECS ;

Nu : nombre d'unités à considérer.

3.1.2.2. Calcul des pertes de distribution

Le calcul des pertes de distribution au pas de temps horaire s'effectue de la façon suivante en considérant la production d'ECS individuelle, dans le volume chauffé :

Qd,w = Qd,w_ind,vc = 0.5 × 0,2 × RatECS × Qw (en Wh)

avec :

Qw : besoins horaires d'ECS (en Wh) ;

RatECS : ratio des besoins d'ECS assurés par le système de production aux besoins totaux d'ECS de la zone.

3.1.2.3. Calcul des pertes de stockage

Le calcul des pertes de stockage au pas de temps horaire s'effectue de la façon suivante :

Vous pouvez consulter le tableau dans le JO n° 292 du 17/12/2011 texte numéro 7

avec :

Vs : volume de stockage (en litre) ;

Cr : constante de refroidissement, Cr = 0,19 Wh/(l.K.jr) ;

uECS : température de stockage, pour le système COMBINEO ce coefficient est égal à 50 °C ;

uamb : température ambiante du local, ce coefficient est égal à 19 °C en période d'occupation et à 16 °C en période d'inoccupation.

3.1.2.4. Calcul des besoins totaux horaires pour la production d'ECS

Le calcul des besoins totaux au pas de temps horaire pour la production d'ECS s'effectue de la façon suivante :

Qecs = Qw + Qd,w + Qg,w (en Wh)

avec :

Qw : besoins horaires d'ECS (en Wh) ;

Qd,w : pertes de distribution horaires (en Wh) ;

Qg,w : pertes de stockage horaires (en Wh).

3.1.2.5. Calcul des consommations énergétiques horaires d'ECS avec le système COMBINEO

Le calcul de la consommation énergétique horaire d'ECS avec le système COMBINEO s'effectue de la façon suivante :

Vous pouvez consulter le tableau dans le JO n° 292 du 17/12/2011 texte numéro 7

avec :

QECS : besoins totaux horaires pour la production d'ECS (en Wh) ;

COPECS : coefficient de performance du système COMBINEO pour la production d'ECS.

3.1.2.6. Calcul du coefficient correctif de la consommation énergétique d'ECS

Le calcul du coefficient de correction de la consommation énergétique d'ECS s'effectue de la façon suivante :

Vous pouvez consulter le tableau dans le JO n° 292 du 17/12/2011 texte numéro 7

avec :

CECS_COMBINEO : consommation énergétique horaire d'ECS avec le système COMBINEO (en Wh) ;

CECS_05 : consommation énergétique d'ECS d'un ballon d'eau chaude électrique (en Wh) dont les caractéristiques techniques sont identiques à celui du COMBINEO avec des pertes de stockage calées sur les règles Th-C-E 2005, à savoir : uECS = 65 °C et uamb = 20 °C.

3.1.3. Calcul du coefficient correctif de la consommation énergétique des auxiliaires de ventilation

Le calcul des consommations énergétiques d'auxiliaires de ventilation se fait comme suit :

― lorsqu'il y a production de chauffage et/ou d'ECS, la puissance des ventilateurs est directement intégrée dans les COPCH et COPECS. Leur consommation énergétique impacte alors les consommations énergétiques de chauffage et/ou d'ECS ;

― lorsqu'il n'y a pas de production de chauffage ni d'ECS, la puissance des ventilateurs est comptabilisée dans la puissance de ventilation et leur consommation énergétique impacte alors la consommation énergétique des auxiliaires de ventilation.

3.1.3.1. Calcul du taux de fonctionnement de la PAC

Le calcul du taux de fonctionnement de la PAC s'effectue de la façon suivante :

Vous pouvez consulter le tableau dans le JO n° 292 du 17/12/2011 texte numéro 7

avec :

PECS_utilisée : puissance de la PAC utilisée pour la production d'ECS (en W) ;

PECS : puissance du COMBINEO pour la production d'ECS (en W) ;

PCH_utilisée : puissance de la PAC utilisée pour le chauffage (en W) ;

PCH : puissance du COMBINEO pour la production de chauffage (en W).

3.1.3.2. Calcul du coefficient correctif de la consommation énergétique des auxiliaires de ventilation

Le calcul du coefficient de correction de la consommation énergétique des auxiliaires de ventilation s'effectue de la façon suivante :

aVENT = 1 ― aPAC

avec :

aPAC : taux de fonctionnement de la PAC.

3.2. Intégration du système COMBINEO dans Th-C-E

L'intégration du système COMBINEO dans la méthode Th-C-E s'effectue de la façon suivante :

3.2.1. Génération de chauffage

Une génération pour le COMBINEO : Système thermodynamique Air rejeté/Air extérieur, COPCH non certifié, avec régulation en Tout Ou Rien.

Une génération pour l'appoint effet joule : système effet joule direct, saisi conformément aux règles Th-C-E.

3.2.2. Emission de chauffage

Dans la méthode de calcul Th-C-E, trois émissions de chauffage sont créées :

1 pour le COMBINEO suivant le tableau 3 ;

1 pour l'appoint dans le salon/séjour suivant le tableau 4 ;

1 pour l'appoint dans les salles de bains suivant le tableau 5.

Par défaut, les caractéristiques des émetteurs de chaleur correspondent aux valeurs définies par défaut dans les règles Th-C-E.

Tableau 3. Description de l'émetteur 1 par soufflage d'air chaud du COMBINEO

ÉMETTEUR 1 - SOUFFLAGE D'AIR CHAUD (COMBINEO)

|

Type d'émetteur |

Chauffage seul |

Ventilateurs liés aux émetteurs |

Pas de ventilateur |

Puissance des ventilateurs |

― |

Perte au dos des émetteurs |

― |

Surface |

Surface totale (Shab) |

Hauteur sous plafond |

Propre au projet |

Type de chauffage |

Electrique autre (thermodynamique) |

Type d'émetteur chaud |

Air soufflé |

Lien avec la génération |

Génération 1 : COMBINEO |

Part de besoin assurée par ce système |

bCH_COMBINEO |

Variation spatiale |

Classe B |

Variation temporelle |

Couple régulateur-émetteur permettant l'arrêt total de l'émission |

Lien vers CTA à débit variable |

Pas de lien |

Réseau chaud |

Inexistant ou pertes nulles |

Tableau 4. Description de l'émetteur 2 par effet joule dans le salon/séjour

ÉMETTEUR 2 - APPOINT SALON/SÉJOUR |

Type d'émetteur |

Chauffage seul |

|

|

Ventilateurs liés aux émetteurs |

Pas de ventilateur |

|

|

Puissance des ventilateurs |

― |

|

|

Perte au dos des émetteurs |

Propre au projet |

|

|

Surface |

Surface totale (Shab) |

|

|

Hauteur sous plafond |

Propre au projet |

|

|

Type de chauffage |

Electrique direct |

|

|

Type d'émetteur chaud |

PRE ou panneau rayonnant ou convecteur |

|

|

Lien avec la génération |

Génération 2 - appoint par effet joule |

|

|

Part de besoin assurée par ce système |

bCH_appoint_SALON |

|

|

Variation spatiale |

Classe A si PRE |

Classe B

si panneau rayonnant |

Classe C si convecteur |

Variation temporelle |

Couple régulateur/émetteur

permettant l'arrêt total

de l'émission

ou

valeur connue si variation

temporelle certifiée |

Emetteur électrique direct avec thermostat intégré certifié

ou

valeur connue si variation temporelle certifiée |

Tableau 5. Description de l'émetteur 3 par effet joule dans les salles de bains

ÉMETTEUR 3 - APPOINT SALLES DE BAINS |

Type d'émetteur |

Chauffage seul |

|

Ventilateurs liés aux émetteurs |

Pas de ventilateur |

|

Puissance des ventilateurs |

― |

|

Perte au dos des émetteurs |

Propre au projet |

|

Surface |

Surface totale (Shab) |

|

Hauteur sous plafond |

Propre au projet |

|

Type de chauffage |

Electrique direct |

|

Type d'émetteur chaud |

Panneau rayonnant ou convecteur |

|

Lien avec la génération |

Génération 2 - appoint par effet joule |

|

Part de besoin assurée par ce système |

bCH_appoint_SDB |

|

Variation spatiale |

Classe B si panneau rayonnant |

Classe C si convecteur |

Variation temporelle |

Emetteur électrique direct avec thermostat intégré certifié

ou

valeur connue si variation temporelle certifiée |

3.2.3. Production d'ECS

La production d'ECS est modélisée dans la méthode de calcul Th-C-E par un ballon électrique de capacité et de performances équivalentes au ballon du COMBINEO, à savoir :

Volume du ballon : 185 L

Constante de refroidissement : Cr = 0.19 Wh/l.K.jr

3.2.4. Ventilation

Le système de ventilation est modélisé dans la méthode de calcul Th-C-E par une ventilation mécanique contrôlée de type double flux thermodynamique avec les caractéristiques détaillées dans les tableaux 6 et 7 suivants :

Tableau 6. Description de la CTA

CENTRALE DE TRAITEMENT D'AIR - DF COMBINEO |

Type de ventilation |

Double flux hygiénique |

Puissance des ventilateurs en occupation |

PVENT |

Type de réseau aéraulique |

Autre cas et type par défaut, classe C |

Présence de filtres de classe F5 à F9 |

Oui |

Présence d'un échangeur |

Oui |

Efficacité de l'échangeur |

bECH |

Valeur certifiée |

Non |

Puissance électrique des auxiliaires |

0 W |

Bypassage de l'échangeur |

Arrêt manuel ou automatique de l'échangeur hors période de chauffage |

Génération associée à l'antigel |

Pas de lien |

Tableau 7. Description de la ventilation

VENTILATION |

Description des logements |

Propre au projet |

Type de ventilation |

Ventilation mécanique double flux |

Lien vers la CTA |

Centrale de traitement d'air ― DF COMBINEO |

Composant de ventilation : Cdep |

Autoréglable |

Gestion de la ventilation |

Dispositif avec temporisateur |

Les données de sortie issues du prétraitement qui doivent être saisies dans la méthode de calcul Th-C-E sont définies dans le tableau 8 suivant :

Tableau 8. Données issues du prétraitement à saisir dans la méthode Th-C-E

PARTIES DE Th-C-E

à alimenter |

DÉNOMINATION |

DONNÉES À SAISIR

pour caractériser

le système COMBINEO |

Production de chauffage |

Puissance nominale |

PCH |

|

COP nominal |

COPCH |

Emetteurs de chauffage |

Part de besoin assurée par COMBINEO |

bCH_COMBINEO |

|

Part de besoin assurée par l'appoint salon/séjour |

bCH_appoint_SALON |

|

Part de besoin assurée par l'appoint salle de bains |

bCH_appoint_SDB |

Ventilation |

Puissance des ventilateurs en occupation |

PVENT |

|

Efficacité de l'échangeur |

hECH |

3.3. Post-traitement

Le calcul de la consommation énergétique d'ECS du projet utilisant le système COMBINEO s'effectue de la façon suivante :

CECS_projet = CEP-ECS × aECS (en kWhEP/[m².an])

avec :

CEPS-ECS : consommation énergétique d'ECS déterminée selon la méthode de calcul Th-C-E intégrant le système COMBINEO (en kWhEP/[m².an]) ;

aECS : coefficient de correction de la consommation énergétique d'ECS.

Le calcul de la consommation énergétique des auxiliaires de ventilation du projet utilisant le système COMBINEO (CAUX_VENT_projet) s'effectue de la façon suivante :

CAUX_VENT_projet = CEP_AUX_VENT × aVENT (en kWhEP/[m².an])

avec :

CEP_AUX_VENT : consommation énergétique des auxiliaires de ventilation déterminée selon la méthode de calcul Th-C-E intégrant le système COMBINEO (en kWhEP/[m².an]) ;

aVENT : coefficient de correction de la consommation énergétique des auxiliaires de ventilation.

3.4. Données techniques

3.1.1. Caractéristiques du COMBINEO

Le tableau 9 ci-dessous fournit les puissances et COP disponibles (ECS et chauffage) et les données de ventilation (PVENT et hECH) pour différentes conditions de températures extérieures (de ― 15 °C à 40 °C) et de débits de ventilation (95, 150 et 240 m³/h).

Les caractéristiques du COMBINEO correspondant à des conditions de fonctionnement (T° et/ou débit) intermédiaires à celles détaillés dans le tableau 9 ci-dessous, peuvent être déterminées par inter et extrapolation.

Tableau 9. Données caractéristiques du COMBINEO 185 LS

DÉBIT D'AIR |

T° AIR

extérieur

(°C) |

PUISSANCE

électrique

de ventilateur :

PVENT (W) |

EFFICACITÉ

échangeur

hECH (%) |

PUISSANCE

électrique

compresseur

(W) |

FONCTIONNEMENT ECS |

FONCTIONNEMENT

chauffage |

|

|

PECS (W) |

COPECS |

PCH (W) |

COPCH |

95 m³/h |

― 15 |

50 |

89,8 % |

482 |

658 |

1,24 |

811 |

1,52 |

|

― 10 |

50 |

89,8 % |

482 |

717 |

1,35 |

869 |

1,63 |

|

― 5 |

50 |

89,8 % |

482 |

775 |

1,46 |

927 |

1,74 |

|

0 |

50 |

89,8 % |

482 |

834 |

1,57 |

986 |

1,85 |

|

5 |

50 |

89,8 % |

482 |

892 |

1,68 |

1 044 |

1,96 |

|

10 |

50 |

89,8 % |

482 |

950 |

1,79 |

1 103 |

2,07 |

|

15 |

50 |

89,8 % |

482 |

1 009 |

1,90 |

1 161 |

2,18 |

|

20 |

50 |

89,8 % |

482 |

1 067 |

2,01 |

1 219 |

2,29 |

|

25 |

50 |

89,8 % |

482 |

1 125 |

2,12 |

1 278 |

2,40 |

|

30 |

50 |

89,8 % |

482 |

1 184 |

2,22 |

1 336 |

2,51 |

|

35 |

50 |

89,8 % |

482 |

1 242 |

2,33 |

1 394 |

2,62 |

|

40 |

50 |

89,8 % |

482 |

1 300 |

2,44 |

1 453 |

2,73 |

150 m³/h |

― 15 |

55 |

89,4 % |

490 |

464 |

0,85 |

868 |

1,59 |

|

― 10 |

55 |

89,4 % |

490 |

590 |

1,08 |

994 |

1,82 |

|

― 5 |

55 |

89,4 % |

490 |

716 |

1,31 |

1 120 |

2,05 |

|

0 |

55 |

89,4 % |

490 |

842 |

1,54 |

1 246 |

2,29 |

|

5 |

55 |

89,4 % |

490 |

968 |

1,78 |

1 372 |

2,52 |

|

10 |

55 |

89,4 % |

490 |

1 094 |

2,01 |

1 498 |

2,75 |

|

15 |

55 |

89,4 % |

490 |

1 220 |

2,24 |

1 624 |

2,98 |

|

20 |

55 |

89,4 % |

490 |

1 347 |

2,47 |

1 751 |

3,21 |

|

25 |

55 |

89,4 % |

490 |

1 473 |

2,70 |

1 877 |

3,44 |

|

30 |

55 |

89,4 % |

490 |

1 599 |

2,93 |

2 003 |

3,68 |

|

35 |

55 |

89,4 % |

490 |

1 725 |

3,17 |

2 129 |

3,91 |

|

40 |

55 |

89,4 % |

490 |

1 851 |

3,40 |

2 255 |

4,14 |

240 m³/h |

― 15 |

110 |

88,0 % |

482 |

104 |

0,18 |

607 |

1,02 |

|

― 10 |

110 |

88,0 % |

482 |

321 |

0,54 |

824 |

1,39 |

|

― 5 |

110 |

88,0 % |

482 |

538 |

0,91 |

1 040 |

1,76 |

|

0 |

110 |

88,0 % |

482 |

755 |

1,27 |

1 257 |

2,12 |

|

5 |

110 |

88,0 % |

482 |

971 |

1,64 |

1 474 |

2,49 |

|

10 |

110 |

88,0 % |

482 |

1 188 |

2,01 |

1 691 |

2,86 |

|

15 |

110 |

88,0 % |

482 |

1 405 |

2,37 |

1 907 |

3,22 |

|

20 |

110 |

88,0 % |

482 |

1 622 |

2,74 |

2 124 |

3,59 |

|

25 |

110 |

88,0 % |

482 |

1 838 |

3,11 |

2 341 |

3,95 |

|

30 |

110 |

88,0 % |

482 |

2 055 |

3,47 |

2 558 |

4,32 |

|

35 |

110 |

88,0 % |

482 |

2 272 |

3,84 |

2 774 |

4,69 |

|

40 |

110 |

88,0 % |

482 |

2 489 |

4,20 |

2 991 |

5,05 |

3.1.2. Données de ventilation liées à la typologie de bâtiment

Il est possible de renseigner les débits de ventilation (base et pointe) par deux moyens :

― en les renseignant directement si les valeurs sont connues ;

― en se référant au tableau 10 ci-dessous, selon le type de logement :

Tableau 10. Débits réglementaires selon la typologie

TYPOLOGIE |

DÉBIT BASE (m³/h) |

DÉBIT POINTE (m³/h) |

T3 1 SDB 1 WC |

90 |

150 |

T3 1 SDB 2 WC |

105 |

165 |

T3 2 SDB 1 WC |

120 |

180 |

T3 2 SDB 2 WC |

135 |

195 |

T4 1 SDB 1 WC |

105 |

180 |

T4 1 SDB 2 WC |

105 |

180 |

T4 2 SDB 1 WC |

135 |

210 |

T4 2 SDB 2 WC |

135 |

210 |

T5 1 SDB 1 WC |

105 |

195 |

T5 1 SDB 2 WC |

105 |

195 |

T5 2 SDB 1 WC |

135 |

225 |

T5 2 SDB 2 WC |

135 |

225 |

T6 2 SDB 1 WC |

135 |

225 |

T6 2 SDB 2 WC |

135 |

225 |

Cellier |

― |

15 |

3.1.3. Corrections de la température extérieure en fonction de l'altitude

Tableau 11. Correction de la température extérieure selon l'altitude

ALTITUDE (m) |

CORRECTION T° EXT. (°C) |

Alt 400 m |

0 |

400 m ¸ Alt 800 m |

― 2 |

Alt ¹ 800 m |

― 4 |

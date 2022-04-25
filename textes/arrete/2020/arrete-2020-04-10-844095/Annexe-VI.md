# Article Annexe VI

MODALITÉS DE TRANSMISSION À LA BASE DE DONNÉES

Modèle de fichier d'échange de données standardisées

Les données sont organisées suivant 5 tables :

Table 1 : Données administratives sur l'assujetti-Gestion des comptes utilisateurs : Identifiant société-Identification du référent-Identification des délégués et mandataires)

Table 2 : Données administratives bâtimentaires : Identification du bâtiment, partie de bâtiment ou ensemble de bâtiments (Adresse, références foncières)

Table 3 : Données sur la situation de référence : Identification de l'année de référence-Consommations énergétiques de l'année de référence-Catégories d'activités concernés et indicateurs d'intensité d'usages

Table 4 : Données de consommations énergétiques annuelles par type d'énergie et des indicateurs d'intensité d'usage correspondants

Table 5 : Données sur les caractéristiques bâtimentaires : Système constructif-Caractéristiques de l'enveloppe du bâtiment.

Table 6 : Données sur les systèmes techniques bâtimentaire (types d'énergie, de générateur, d'émetteur, de ventilation, eau chaude sanitaire, éclairage, autres équipements immobiliers).

Les tables 5 et 6 sont relatives à des données qui peuvent être renseignées de façon facultative sur OPERAT. Le renseignement de ces données permet aux assujettis de capitaliser leurs données patrimoniales et de procéder, le cas échéant, à des requêtes qui leur permettront d'établir des échantillons dans la perspective d'élaboration d'études diagnostiques ou de dossiers techniques de modulation des objectifs.

Une grande majorité des données sont recueillies par sélection dans le cadre de menues déroulants.

Les données attributaires de ces tables sont les suivantes :

Table 1.-Données administratives sur l'assujetti-Gestion des comptes utilisateurs

Cette table concerne la création de compte et d'accès sur OPERAT. Certaines données peuvent être récupérée par l'intermédiaire de l'application SIRENE (Cf. Guide utilisateur OPERAT)

Désignation de la donnée attributaire |

Modalité de renseignement de la donnée |

Table 1A-Données administratives relative à la structure assujettie |

Nature de la structure

(Etat-Collectivités territoriales-Privé) |

Sélection par menu déroulant (2 à 3 niveaux)

-Etat et ses opérateurs

-Ministère et services centraux de ministère

-Services déconcentrés de l'Etat

-Opérateur de l'Etat

-Collectivités territoriales et leurs opérateurs

-Région

-Département

-Etablissement Public de Coopération Intercommunale

-Métropole

-Communauté urbaine

-Communauté d'agglomération

-Communauté de communes

-Syndicat Intercommunal (vocation unique ou multiple)

-Commune

-Opérateur de Collectivité Territoriale

-Entreprises tertiaires des secteurs public et privé (quel que soit le secteur d'activité)

-Entreprise (plusieurs salariés)

-Association

-Profession libérale individuelle

-Propriétaires immobiliers

-Société civile immobilière et/ ou Foncière

-Particulier. |

Nom de la structure |

Données alphanumérique (Recueil via API SIRENE) |

Identifiant national de la structure

Numéro SIREN |

9 chiffres (Recueil via API SIRENE) |

Branche d'activité de la structure

Code APE (Activité principale exercée) |

Code APE (ou code NAF) : 5 caractères (4 chiffres et une lettre)

(Recueil via API SIRENE) |

Adresse du siège de la structure |

Adresse correspondant au Siren (format adresse : n°-Voie-Code postale-Ville)

(Recueil via API SIRENE) |

Identifiant de la sous-structure (établissement au niveau local)

Numéro SIRET (le cas échéant) |

SIRET : Siren (9 chiffres) + le numéro NIC (5 chiffres)

(Recueil via API SIRENE) |

Adresse de la sous-structure (établissement au niveau local) |

Adresse correspondant au Siret (format adresse : n°-Voie-Code postale-Ville)

(Recueil via API SIRENE) |

Table 1B-Données administratives de Groupe de Structures assujetties

Le cas échéant-Mutualisation des résultats à l'échelle de tout ou partie d'un patrimoine d'entités fonctionnelles |

Dénomination officielle du groupe de structures |

Données alphanumérique (déclaratif sur OPERAT) |

Adresse du groupe de structures |

Adresse correspondant au Siren (format adresse : n°-Voie-Code postale-Ville)

(Recueil via API SIRENE) |

Dénomination de la structure référente du groupe de structures (si différente du groupe de structures) |

Données alphanumérique (déclaratif sur OPERAT) |

Identifiant national de la structure référente du groupe de structures Numéro SIREN |

9 chiffres (Récupération de la donnée déjà renseignée) |

Structures intégrées dans le groupe de structures-Identification Numéro SIRET concerné |

SIRET 1 : Siren (9 chiffres) + le numéro NIC (5 chiffres)

SIRET 2 : Siren (9 chiffres) + le numéro NIC (5 chiffres)

SIRET x : Siren (9 chiffres) + le numéro NIC (5 chiffres)

Récupération de la donnée déjà renseignée |

Représentant légal de la structure référente du groupe de structures |

Nom-Prénom-Profil représentant légal |

Adresse mail du représentant légal du groupe de structures |

Adresse mail valide (nominative ou structure) |

Table 1C-Création de comptes utilisateurs de la structure et sous structures assujetties |

Représentant légal de la structure correspondant au SIREN

Tout pouvoir sur les données OPERAT renseignées pour la structure |

Nom-Prénom-Profil représentant légal |

Courriel du représentant légal de la structure (droit d'accès par mot de passe) |

Adresse mail valide (nominative ou structure) |

Référent de la structure ou Référent d'une sous-structure

Tout pouvoir sur les données OPERAT renseignées pour la structure ou la sous-structure mais sans responsabilité légale |

Nom-Prénom-Profil du référent |

Courriel du référent de la structure ou de la sous-structure (établissement au niveau local)-Facultatif |

Adresse mail valide (nominative ou établissement) |

Correspondant

Tout pouvoir sur les données OPERAT renseignées sur un périmètre déterminé, mais sans responsabilité légale |

Nom-Prénom-Profil correspondant |

Courriel du correspondant |

Adresse mail valide (nominative ou établissement) |

Table 1D-Création de comptes mandataires d'une structure ou sous-structure |

Identification Mandataire x |

Données alphanumérique |

Identité du mandataire |

Nom-Prénom-Profil mandataire |

Rôle du mandataire (facultatif)

Habilité à renseigner des données techniques, des données d'occupation, de plans d'actions ou de données de consommations sur le périmètre bâtimentaire qui lui est affecté |

Sélection par menu déroulant (choix)

-Gestionnaire Immobilier de la Structure (interne à la structure ou au groupe)-Asset manager et Property manager

-Gestionnaire technique (interne à la structure ou au groupe)-Energy manager ou Exploitant d'une entité fonctionnelle

-Syndic de copropriété ou Gestionnaires immobilier externe à la structure-Propriétaire d'un preneur à bail

-Bureau d'études et conseils en performance énergétique, gestionnaire exploitant (externe à la structure ou au groupe de structure)

-Autres (à préciser) |

Périmètre d'intervention du profil utilisateur

(facultatif) |

Sélection par menu déroulant (choix)

-Périmètre bâtimentaire (groupe de bâtiments) : définition d'un périmètre spécifique

-Nationale pour la structure ou le groupe de structure

Autre périmètre géographique

-Régional

-Départemental

-Supra-communal

-Communal

-Ponctuelle-lié à l'établissement assujetti |

Table 2.-Données bâtimentaires

Cette table concerne les données bâtimentaires qui permettent des modifications du périmètre de remontées de données de consommation notamment en cas de transaction immobilière (vente, nouveau contrat de bail) ou de mise en place de sous comptage au niveau de plusieurs bâtiments assujettis situés sur un même site. Une exploitation de Géoportail peut permettre d'accéder aux informations utiles au renseignement de cette table de données.

Désignation de la donnée attributaire |

Modalité de renseignement de la donnée |

Table 2-Données bâtimentaires

Bâtiment, parties de bâtiments ou ensemble de bâtiments |

Qualité de l'assujetti au niveau de l'entité fonctionnelle assujettie (bâtiment, partie de bâtiment ou ensemble de bâtiments) |

Sélection par menu déroulant

-Propriétaire occupant

-Propriétaire bailleur

-Preneur à bail ou occupant |

Cas d'assujettissement

(Cf. article II de l'article R 131-38 du code de la construction ou de l'habitation)

Importation via API possible |

Sélection par menu déroulant (choix)

- Cas 1a-Bâtiment hébergeant exclusivement des activités tertiaires (avec ou sans activités non tertiaires accessoires) sur une seule entité fonctionnelle (propriétaire occupant unique ou mono locataire)

- Cas 1b-Bâtiment hébergeant exclusivement des activités tertiaires (avec ou sans activités non tertiaires) en multi-occupation-Lot (s)

- Cas 2-Partie (s) de bâtiment hébergeant des activités tertiaires-Lot (s)

- Cas 3-Ensemble de bâtiments situés sur une même unité foncière ou sur un même site hébergeant des activités tertiaires-Site |

Création d'un Identifiant unique bâtimentaire |

Référence cadastrale (Cas 1 à 3)

Références INSEE et cadastrales

Importation via API possible |

-Code commune INSEE-Dénomination commune

-Référence cadastrale de la parcelle ou des parcelles :

Préfixe-Section-N° Parcelle

https://www.geoportail.gouv.fr/donnees/parcelles-cadastrales

https://www.cadastre.gouv.fr/scpc/rechercherParReferenceCadastrale.do

|

Identifiant bâtiment unique (Cas 1 et 2)

Identifiant des bâtiments hébergeant des activités tertiaires situés sur une même unité foncière ou sur un même site (Cas 3) Importation via API possible |

-Dénomination bâtiment 1 : Identifiant alphanumérique

-Dénomination bâtiment 2 : Identifiant alphanumérique

-Dénomination bâtiment 3 : Identifiant alphanumérique

-Dénomination bâtiment 4 à x : Identifiant alphanumérique |

Identification de ou des parties de bâtiments (Cas 1 à 3)-Numéro (s) de Lot (s)

Importation via API possible

|

-Numéro (s) de (s) Lot (s) concerné (s) pour la structure assujettie |

Référentiel patrimonial spécifique de l'assujetti Importation via API possible |

-Code identifiant du référentiel assujetti (alphanumérique 10-12 caractères) |

Référence des points de livraisons de Gestionnaire de Réseau de Distribution

Importation via API possible |

Sélection par menu déroulant (choix) et renseignement des références

- Réseau électrique (Enedis, RTE, etc.) : Identifiant (s) de Point de livraison (PDL) ou Référence Acheminement Electricité à renseigner

- Réseau gaz (GRDF) Identifiant (s) de PDL à renseigner

- Réseau de chaleur :

-Identifiant du Réseau de chaleur (liste)

-Identifiant (s) de la sous-station

- Point de livraison spécifique IRVE (Installation de recharge des véhicules électriques ou hybrides rechargeables)

- Aucun point de livraison |

Table 3.-Données sur la situation de référence

Cette table concerne les données sur la situation de référence : Identification de l'année de référence-Consommations énergétiques de l'année de référence-Catégories d'activités concernés et indicateurs d'intensité d'usages.

Désignation de la donnée attributaire |

Modalité de renseignement de la donnée |

Table 3-Données Situation de référence de l'entité fonctionnelle assujettie |

Identifiant de l'établissement au niveau local

Numéro SIRET (le cas échéant) |

SIRET : Siren (9 chiffres) + le numéro NIC (5 chiffres)

(Recueil via API SIRENE)

-Numéro de Département : à renseigner

-Affectation automatique de la zone géographique (sélection des tables correspondantes pour la valeur CVC) |

Station météorologique de référence |

-Identification de la station météorologique de référence du département par défaut

-Choix d'une autre station météorologique de départements limitrophes (adaptation au contexte local) Sélection par menu déroulant |

Année de référence

Importation via API possible |

-Année antérieure à 2020 (comprise entre 2010 et 2019) : Identification de l'année

-Première année pleine d'exploitation remontée sur OPERAT

-Mois de début de la plage de 12 mois consécutif (liste)

→ Détermination de la plage annuelle de consommation |

Consommation de référence

Importation via API possible |

Sélection par menu déroulant (choix) des types d'énergies utilisées et renseignement des données de consommations de l'année de référence

-Electricité (kWh) : consommation année de référence

-Gaz naturel-réseaux (kWh) : consommation année de référence

-Gaz naturel liquéfié (kg) : consommation année de référence

-Gaz propane (m3) : consommation année de référence

-Gaz propane (kg) : consommation année de référence

-Gaz butane (m3) : consommation année de référence

-Gaz butane (kg) : consommation année de référence

-Fioul domestique (l) : consommation année de référence

-Charbon-agglomérés et briquettes (kg) : consommation année de référence

-Houille (kg) : consommation année de référence

-Bois-Plaquettes d'industrie (kg) : consommation année de référence

-Bois-Plaquettes forestières (kg) : consommation année de référence

-Bois-Granulés (pellets) ou briquettes (kg) : consommation année de référence

-Bois-Bûches (Stère) : consommation année de référence

-Réseau de chaleur (kWh) : consommation année de référence

-Réseau de froid (kWh électrique) : consommation année de référence |

Consommation énergétique relative à la recharge des véhicules électriques ou hybrides rechargeables (IRVE)-Année de référence |

-Recharge des véhicules électriques ou hybrides rechargeables (IRVE)-consommation année de référence |

Catégories d'activités et sous-catégories d'activités

Obligatoire permet de déterminer l'objectif exprimé en valeur absolue mais également l'objectif en valeur relative en prenant en considération la surface assujettie |

-Sélection des activités et des sous catégories éventuelles concernées Sélection par menu déroulant

-Renseignement des données surfaciques correspondantes pour chaque catégories et sous-catégories sélectionnées

Le détail en sous catégories n'est pas obligatoire si les données surfaciques correspondantes relatives à l'année de référence ne sont pas connues. Néanmoins, la détermination d'une surface totale est obligatoire ou par défaut elle correspondra à l'information recueillie pour la première remontée de consommation annuelle. |

Indicateurs d'intensité d'usage

Si disponibles, sinon ils correspondront par défaut à ceux des valeurs étalons mentionnées dans les tables de valeurs absolues de l'Annexe II (Corrélation avec les consommations).

Importation via API possible (nécessite des tables renseignées avec toutes les catégories ou les catégories concernées au même format. |

Sélection par menu déroulant (choix)

-Indicateurs d'intensité d'usages de l'année de référence connus :

-Renseignement des indicateurs d'intensité d'usage temporels et surfaciques.

-Indicateurs d'intensité d'usage étalons par défaut |

Table 4.-Données de consommations énergétiques annuelles et des indicateurs d'intensité d'usage correspondants

Cette table concerne les données de consommations énergétiques annuelles par type d'énergie. Elle est accessoirement complétée par le renseignement des indicateurs d'intensité d'usage s'ils ont évolués qui permettent de procéder à la modulation des objectifs en fonction du volume d'activité (Cf. article 10 du présent arrêté).

Désignation de la donnée attributaire |

Modalité de renseignement de la donnée |

Table 4 a-Données de consommations énergétiques annuelles |

Référence de l'année et de la plage de consommation annuelle

Donnée à rendre la plus pérenne possible

Importation via API possible |

-Identification de l'année

-Mois de début de la plage de 12 mois consécutif (liste)

→ Détermination de la plage annuelle de consommation

Proposition automatique de l'information issue de la Table 3, mais qui peut être modifiée. |

Périmètre des consommations |

-Consommations individuelles de l'entité fonctionnelle

-Consommations réparties bénéficiant à l'entité fonctionnelle

-Consommations des espaces communs affectées à l'entité fonctionnelle |

Consommations énergétiques annuelles

Importation via API possible |

Sélection par menu déroulant (choix) des types d'énergies utilisées et renseignement des données de consommations de l'année écoulée.

-Electricité (kWh) : consommation année n-1

-Gaz naturel-réseaux (kWh) : consommation année n-1

-Gaz propane (m3) : consommation année n-1

-Gaz propane (kg) : consommation année n-1

-Gaz butane (m3) : consommation année n-1

-Gaz butane (kg) : consommation année n-1

-Charbon-agglomérés et briquettes (kg) : consommation année n-1

-Houille (kg) : consommation année n-1

-Bois-Plaquettes d'industrie (kg) : consommation année n-1

-Bois-Plaquettes forestières (kg) : consommation année n-1

-Bois-Granulés (pellets) ou briquettes (kg) : consommation année n-1

-Bois-Bûches (Stère) : consommation année n-1

-Réseau de chaleur (kWh) : consommation année n-1

-Réseau de froid (kWh électrique) : consommation année n-1 |

Consommation énergétique relative à la recharge des véhicules électriques ou hybrides rechargeables (IRVE)-Consommation annuelle |

-Recharge des véhicules électriques ou hybrides rechargeables (IRVE)-consommation annuelle |

Remontée de données de consommations par les gestionnaires de réseaux de distribution (GRD)

Choix de l'option de collecte de données lorsqu'il existe une convention entre l'ADEME et les GRD

|

- Electricité (Convention Enedis, RTE, etc)

- Gaz (Convention GRDF)

- Réseau de chaleur (liste de Réseau de chaleur urbain ayant passé une convention avec l'ADEME)

- Réseau de froid (liste de Réseau de froid urbain ayant passé une convention avec l'ADEME) |

Table 4 b-Evolution des indicateurs d'intensité d'usage |

Evolution des indicateurs d'intensité d'usage

Affichage par défaut des indicateurs de l'année précédente ou de l'année de référence (Corrélation avec les consommations).

Importation via API possible (nécessite des tables renseignées avec toutes les catégories ou les catégories concernées au même format. |

Sélection par menu déroulant (choix)

-Valeurs étalons des indicateurs d'intensité d'usage par défaut

-Indicateurs d'intensité d'usages de l'année écoulée :

-Sélection des activités et des sous catégories éventuelles concernées par une évolution ;

-Renseignement éventuelle des données surfaciques correspondantes pour les catégories et sous-catégories sélectionnées (liées à l'évolution) ;

-Renseignement des indicateurs d'intensité d'usage temporel et surfaciques qui ont évolués. |

Table 5.-Données sur les caractéristiques bâtimentaires (Facultative)

Cette table concerne les données sur les caractéristiques bâtimentaires : Système constructif-Caractéristiques de l'enveloppe du bâtiment.

Désignation de la donnée attributaire |

Modalité de renseignement de la donnée |

Table 5a-Données sur les caractéristiques générales bâtimentaires |

Epoque de construction

Importation via API possible |

Sélection par menu déroulant (choix) de l'époque de construction.

- Avant 1400-Moyen âge et antiquité

- 1400 à 1700-Renaissance

- 1700 à 1800-Baroque

- 1800 à 1899-Néoclassique, Haussmannien

- 1900 à 1947-Moderne (Pré-rationalisme, Bauhaus, Style international)

- 1948 à 1979-Post Moderne (Béton, charpentes métalliques, etc.)

- 1980 à 2000-RT 1978 non contraignante

- 2001-2012-RT 2000 et 2005 ou référence équivalente (non assujetti RT)

- 2013-2021-RT 2012 ou référence équivalente (non assujetti RT)

- A partir de 2021-RE2020 ou référence équivalente (non assujetti RE)

|

Type de patrimoine

Importation via API possible |

Sélection par menu déroulant (choix) de la typologie de patrimoine.

-Bâtiment classé au titre des monuments historiques

-Bâtiment inscrit au titre des monuments historiques

-Bâtiment situés dans les abords de monuments historiques (à moins de 500 m et en covisibilité, ou périmètre délimité des abords)

-Bâtiment situé en site patrimonial remarquable

-Bâtiment bénéficiant du label Architecture contemporaine remarquable

-Bâtiment protégé ou soumis à prescription par le règlement du PLU (articles L151-18 et L151-19 du code de l'urbanisme)

-Bâtiment situé dans un site classé ou inscrit au titre du code de l'environnement

-Construction courante

-Construction atypique

-Modèle industriel |

Forme du bâtiment et mitoyenneté |

Sélection par menu déroulant (choix) de la forme du bâtiment.

Forme (emprise au sol)

-Rectangulaire ou carré

-Rectangulaire avec décrochés

-L ou U

-Forme complexe

Hauteur moyenne des niveaux

-Moins de 2,50 m

-Entre 2,50 et 3,00 m

-Entre 3,00 et 4,00 m

-Plus de 4,00 m

Mitoyenneté

-Absence de paroi mitoyenne

-Mitoyenneté limitée à un pignon

-Mitoyenneté limitée à deux pignons

Co-activité non tertiaire dans le bâtiment

-Présence de co-activité non tertiaire |

Référence de la Base Permanente des équipements |

Sélection par menu déroulant (choix) |

Table 5b-Données sur les caractéristiques de l'enveloppe bâtimentaire |

Façade (Typologie)

Importation via API possible |

Sélection par menu déroulant (choix) de la typologie de façade.

-Mur porteur maçonné pierre

-Mur porteur maçonné brique

-Briques pleines autoporteuses (monomur)

-Mur bloc alvéolé béton

-Structure poteau BA et remplissage brique creuse

-Structure poteau BA et remplissage brique pleine

-Structure poteau BA et remplissage bloc alvéolé béton

-Structure poteau BA et remplissage maçonné autre

-Mur voile porteur Béton Armé

-Panneaux béton préfabriqués

-Structure bois porteuse et remplissage (Colombage)

-Panneaux ossatures bois

-Panneaux léger simple peau (structure métallique, BA, bois lamellé collé ou lamellé croisé)

-Panneaux léger double peau (structure métallique, BA, bois lamellé collé ou lamellé croisé)

-Façade rideau vitrée simple peau

-Façade rideau vitrée double peau

Contraintes sur façade

-Façade classé

-Décor à valeur patrimoniale (modénature) |

Isolation thermique des façades

Importation via API possible |

Sélection par menu déroulant (choix) de la présence d'isolation en façade.

-Absence d'isolation

-Isolation partielle

-Isolation complète |

Isolation thermique des pignons

Importation via API possible |

Sélection par menu déroulant (choix) de la présence d'isolation en pignon.

-Absence d'isolation

-Isolation partielle

-Isolation complète |

Mode d'isolation thermique principal

Importation via API possible |

Sélection par menu déroulant (choix) de la typologie d'isolation.

-Contre cloison avec vide

-Isolation par l'intérieur-épaisseur inférieure ou égale à 5 cm

-Isolation par l'intérieur-épaisseur supérieure à 6 cm

-Isolation par l'extérieure

-Isolation intégrée dans la paroi |

Traitement thermique des menuiseries

Importation via API possible |

Sélection par menu déroulant (choix) de la typologie de vitrage

-Simple vitrage

-Double vitrage avant 1995

-Double vitrage après 1995

-Triple vitrage |

Toiture (Typologie)

Importation via API possible |

Sélection par menu déroulant (choix) de la typologie de toiture.

-Local non contigu à la toiture (dernier niveau non tertiaire)

-Plancher sous combles perdus

-Toiture terrasse sur plancher haut lourd

-Toiture bac acier-éléments métalliques

-Toiture faible pente < 30°

-Toiture faible pente 45° ou proche |

Traitement thermique de la toiture

Importation via API possible |

Sélection par menu déroulant (choix) du traitement thermique en toiture.

-Absence d'isolation

-Isolation-épaisseur < 5 cm

-Isolation-épaisseur comprise entre 5 et 10 cm

-Isolation-épaisseur comprise entre 10 et 20 cm

-Isolation-épaisseur supérieure à 20 cm |

Plancher bas (Typologie)

Importation via API possible |

Sélection par menu déroulant (choix) de l'époque de construction.

-Local non contigu au plancher bas (niveau inférieur non tertiaire)

-Dalle sur terre-plein

-Vide sanitaire

-Sous-Sol |

Isolation thermique du plancher bas

Importation via API possible |

Sélection par menu déroulant (choix) de la typologie de patrimoine.

-Absence d'isolation

-Isolation-épaisseur < 5 cm

-Isolation-épaisseur comprise entre 5 et 10 cm

-Isolation-épaisseur comprise entre 10 et 20 cm

-Isolation-épaisseur supérieure à 20 cm |

Table 6.-Données sur les systèmes techniques bâtimentaires (Facultative)

Cette table concerne les données sur les systèmes techniques bâtimentaire (types d'énergie, de générateur, d'émetteur, de ventilation, eau chaude sanitaire, éclairage, autres équipements immobiliers).

Désignation de la donnée attributaire |

Modalité de renseignement de la donnée |

Table 6-Données sur les systèmes techniques bâtimentaires |

Générateur principal de chauffage

Importation via API possible |

Sélection par menu déroulant (choix) de l'époque de construction.

-Absence de chauffage du local

-Chaudière Gaz individuelle

-Chaudière Gaz collective

-Chaudière fioul domestique

-Chaudière Biomasse individuelle

-Chaudière Biomasse collective

-PAC collective

-PAC individuelle

-PAC individuelle-Climatiseur réversible

-Réseau de chaleur (sous-station)

-Cogénération |

Type principal d'émetteur de chauffage

Importation via API possible |

Sélection par menu déroulant (choix) de la typologie de patrimoine.

-Absence d'émetteur

-Radiateur à eau

-Convecteur-casette

-Radiateur à panneaux rayonnants

-Radiateur à énergie maîtrisée sec (céramique-fonte)

-Radiateur à énergie maîtrisée fluide (liquide caloporteur)

-Plancher chauffant électrique

-Plafond rayonnant électrique

-Plancher chauffant boucle d'eau chaude

-Centrale de traitement de l'air

-Mur chauffant hydraulique

-Vitrage chauffant

-Autres : Compléter |

Générateur principal de rafraîchissement

Importation via API possible |

Sélection par menu déroulant (choix) de l'époque de construction.

-Absence de rafraichissement

-Climatiseur

-PAC réversible sur air

-Groupe eau glacée

-Tour aéroréfrigérante

-Free Cooling (Surventilation nocturne)

-Geo Cooling-Puits Canadiens

-Chaudière Biomasse collective

-Réseau de froid (sous-station)

-Brassage de l'air |

Type principal de ventilation

Importation via API possible |

Sélection par menu déroulant (choix) de l'époque de construction.

-Absence de dispositif de ventilation

-Ventilation naturelle par conduits d'aération

-Ventilation mécanique simple flux dans les pièces humides

-Ventilation mécanique double flux

-Centrale de traitement de l'air

-Autres : Compléter |

Type de production d'eau chaude sanitaire

Importation via API possible |

Sélection par menu déroulant (choix) de l'époque de construction.

-Absence de production d'eau chaude sanitaire

-Chaudière Gaz individuelle

-Chaudière Gaz collective

-Chaudière fioul domestique

-Chaudière Biomasse individuelle

-Chaudière Biomasse collective

-Ballon électrique

-Chauffe-eau thermodynamique

-PAC collective

-Solaire thermique

-Réseau de chaleur (sous-station)

-Cogénération |

Type d'éclairage

Importation via API possible |

Sélection par menu déroulant (choix) de l'époque de construction.

Eclairage naturel des locaux

-Absence d'éclairage naturel

-Eclairage zénithal :

-Verrière

-Lanterneau

-Shed orienté Nord

Eclairage naturel des circulations

-Non concerné

-Absence d'éclairage naturel des circulations

-Présence de second jour

-Eclairage zénithal :

-Verrière

-Lanterneau

-Shed orienté Nord

Eclairage artificiel des locaux

-Lampes

-Tubes

-LED

-OLED |

Autres équipements immobiliers

Importation via API possible |

Sélection par menu déroulant (choix) de l'époque de construction.

-Ascenseurs :

-Nombre de niveau desservis : à renseigner

-Nombre : à renseigner

-Capacité individuelle : à renseigner personnes

-Escalier mécanique :

-Fonctionnement continu-Nombre : à renseigner

-Asservi à la détection-Nombre : à renseigner

-Trottoir mécanique :

-Fonctionnement continu-Nombre : à renseigner

-Asservi à la détection-Nombre : à renseigner |

Système d'automatisation et de contrôle des systèmes techniques (BACS-Building Automation Control System)

Classification selon la norme NF EN15232-1 |

Sélection par menu déroulant (choix).

- Niveau de régulation A (très évolué)

- Niveau de régulation B (évolué)

- Niveau de régulation C (standard)

- Niveau de régulation D (absence de régulation) |

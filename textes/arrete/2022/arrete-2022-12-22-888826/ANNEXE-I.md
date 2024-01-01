# Article ANNEXE I

RÉFÉRENTIEL DES DONNÉES RELATIF AUX MARCHÉS PUBLICS

Le jeu de caractère (encoding) à utiliser est UTF-8.

Nom du champ |

Obligatoire/

Conditionnel |

Format |

Norme et nomenclature

de référence |

Identifiant unique de marché public |

Numéro d'identification unique du marché public

Nom du champ :

id |

Obligatoire |

Texte

Identifiant du marché public

Composition : numéro interne (1 caractère minimum à 16 caractères maximum) propre au système d'information de l'acheteur

Exemples :

-v1234 _ AB-mp

-MP00457363712701

-2022-0425 |

|

Caractéristiques de l'acheteur |

Acheteur ou mandataire

Nom du bloc :

acheteur |

|

Objet (propriétés ci-après)

Si le marché public est passé par un groupement d'acheteurs, c'est le mandataire du groupement qui est décrit dans les données. |

|

Numéro d'inscription SIRET de l'acheteur

Nom du champ :

acheteur > id |

Obligatoire |

Identifiant du Système d'Identification du Répertoire des Etablissements (SIRET)

Type INSEE : ChaineNumeriqueType

Taille : 14 |

http://xml.insee.fr/schema/siret.html#SIRET_stype

|

Caractéristiques du marché public |

Nature du marché public

Nom du champ :

nature |

Obligatoire |

Nature du marché public

Champ limité à une des valeurs suivantes (un seul choix possible) :

-Marché

-Marché de partenariat

-Marché de défense ou de sécurité |

|

Objet du marché public ou du lot

Nom du champ :

objet |

Obligatoire |

Texte

Limité à 1 000 caractères. |

|

Technique d'achat

Nom du champ :

technique |

Obligatoire |

Champ limité à une ou plusieurs des valeurs suivantes (plusieurs choix possibles) :

-Accord-cadre

-Concours

-Système de qualification

-Système d'acquisition dynamique

-Catalogue électronique

-Enchère électronique

-Sans objet |

|

Modalité d'exécution du marché public

Nom du champ :

modaliteExecution |

Obligatoire |

Champ limité à une ou plusieurs des valeurs suivantes (plusieurs choix possibles) :

-Tranches

-Bons de commande

-Marchés subséquents

-Sans objet |

|

Numéro d'identification unique de l'accord-cadre auquel est rattaché le marché subséquent

Nom du champ :

idAccordCadre |

Conditionnel |

Texte

Identifiant de l'accord-cadre

L'identifiant saisi est celui de l'accord-cadre sur lequel est fondé le marché subséquent, objet de la déclaration.

Ce champ a le même format que l'identifiant de marché public (id).

Si ce marché public n'est pas lié à un accord-cadre, laisser ce champ vide. |

|

Code CPV principal

Nom du champ :

codeCPV |

Obligatoire |

Texte

Le code CPV principal (10 caractères)

Exemple : 03452000-3 (Arbres) |

Système de classification CPV 2008 ( https://simap.ted.europa.eu/fr/web/simap/cpv) |

Procédure de passation du marché public

Nom du champ :

procedure |

Obligatoire |

Champ limité à une des valeurs suivantes (un seul choix possible) :

-Procédure adaptée

-Appel d'offres ouvert

-Appel d'offres restreint

-Procédure avec négociation

-Marché passé sans publicité ni mise en concurrence préalable

-Dialogue compétitif |

|

Lieu principal d'exécution

Nom du bloc :

lieuExecution |

|

Objet (propriétés ci-après) |

|

Identifiant du lieu principal d'exécution

Nom du champ :

lieuExecution > code |

Obligatoire |

Texte

Code du lieu d'exécution (code postal, commune, canton, arrondissement, département, région, pays

Exemples :

-2B002

-35136

-75018

-13

-91

-99132 |

|

Type de code du lieu principal d'exécution

Nom du champ :

lieuExecution > typeCode |

Obligatoire |

Le type de code utilisé pour désigner le lieu principal d'exécution. Hormis le " Code postal ", les codes sont des codes géographiques gérés par l'INSEE (http :// www. insee. fr/ fr/ methodes/ nomenclatures/ cog/ default. asp)

Valeurs possibles (un seul choix possible) :

-Code postal

-Code commune

-Code arrondissement

-Code canton

-Code département

-Code région

-Code pays |

|

Durée totale du marché public en nombre de mois

Nom du champ :

dureeMois |

Obligatoire |

Unité : en mois

Nombre entier

Valeur minimum : 1

Si la durée n'est pas un nombre exact de mois, arrondir au nombre entier supérieur.

Exemples :

-9 pour 9 mois

-1 pour 2 semaines

-2 pour 1 mois et 3 semaines

Si, une fois les données du marché publiées, une modification de la durée du marché intervient, elle doit être retranscrite dans le bloc modifications et la propriété dureeMois initiale ne doit pas être modifiée. |

|

Date de notification

Nom du champ :

dateNotification |

Obligatoire |

Date de la réception de la notification par le titulaire

Date de notification du marché au format AAAA-MM-JJ

Type INSEE : DateType

Expression régulière de validation ('d { 4 }-'d { 2 }-'d { 2 })

Exemple : 2022-02-14 |

ISO 8601,

format étendu

http://xml.insee.fr/schema/commun.html#Date_stype

|

Considération sociale

Nom du champ

considerationsSociales |

Obligatoire |

Champ limité à une ou plusieurs valeurs suivantes (plusieurs choix possibles) :

-Clause sociale

-Critère social

-Marché réservé

Ou :

-Pas de considération sociale |

|

Considération environnementale

Nom du champ :

considerationsEnvironnementales |

Obligatoire |

Champ Liste, limité à une ou plusieurs valeurs suivantes (plusieurs choix possibles) :

-Clause environnementale

-Critère environnemental

Ou :

-Pas de considération environnementale |

|

Marché comportant des travaux, services ou fournitures innovants

Nom du champ :

marcheInnovant |

Obligatoire |

Booléen

Champ limité à une des deux valeurs suivantes (un seul choix possible) :

-oui

-non |

|

Part des produits issus de l'Union européenne

Nom du champ :

origineUE |

Obligatoire |

Nombre décimal

Ne peut pas être inférieur à la valeur de origineFrance (ci-dessous), la France faisant partie de l'Union européenne.

Le séparateur décimal est le point.

Exemples : 1 pour 100 %, 0.6 pour 60 %, 0.45 pour 45 %, 0 pour 0 % |

Nombre JSON

Nombre XML |

Part de produits fabriqués en France

Nom du champ :

origineFrance |

Obligatoire |

Nombre décimal

Le séparateur décimal est le point.

Exemples : 1 pour 100 %, 0.6 pour 60 %, 0.45 pour 45 %, 0 pour 0 % |

Nombre JSON ( https://json-schema.org/understanding-json-schema/reference/numeric#number)

Nombre XML ( https://www.w3.org/TR/xmlschema-2/#decimal) |

CCAG de référence

Nom du champ :

ccag |

Obligatoire |

Champ limité à une des valeurs suivantes (un seul choix possible) :

-Travaux

-Maitrise d'œuvre

-Fournitures courantes et services

-Marchés industriels

-Prestations intellectuelles

-Techniques de l'information et de la communication

-Pas de CCAG |

|

Caractéristiques financières |

Nombre d'offres reçues

Nom du champ :

offresRecues |

Obligatoire |

Toutes les offres reçues (comprenant les offres irrégulières, inacceptables, inappropriées et anormalement basses)

Nombre entier

Valeur minimale : 1 |

|

Montant HT forfaitaire en euros ou estimé maximum en euros

Nom du champ :

montant |

Obligatoire |

Nombre décimal

Montant initial du marché hors taxes en €

Si, une fois les données du marché publiées, une modification du montant intervient, elle doit être retranscrite dans le bloc modifications et la propriété montant initiale ne doit pas être modifiée.

Le séparateur décimal est le point.

Exemple : 14982.29 |

Nombre JSON

Nombre XML |

Forme du prix

Nom du champ :

formePrix |

Obligatoire |

Champ limité à une des valeurs suivantes (un seul choix possible) :

-Unitaire

-Forfaitaire

-Mixte |

|

Type de prix

Nom du champ :

typePrix |

Obligatoire |

Champ limité à une ou plusieurs des valeurs suivantes (plusieurs choix possibles) :

-Définitif ferme

-Définitif actualisable

-Définitif révisable

-Provisoire |

|

Attribution d'une avance

Nom du champ :

attributionAvance |

Obligatoire |

Booléen

Champ limité à une des deux valeurs suivantes (un seul choix possible) :

-oui

-non

Possibilité de répondre non pour les entités adjudicatrices |

|

Taux de l'avance attribuée

Nom du champ :

tauxAvance |

Conditionnel |

Nombre décimal

Taux de l'avance attribuée au titulaire principal du marché.

Si attributionAvance est oui, ce nombre doit être supérieur à 0.

Le séparateur décimal est le point.

Exemple : 1 pour 100 %, 0.6 pour 60 %, 0.45 pour 45 %, 0 pour 0 % |

Nombre JSON

Nombre XML |

Caractéristiques d'identification des opérateurs économiques |

Titulaires

Nom du bloc :

titulaires |

|

Liste d'objets

(voir les propriétés ci-après)

Si le marché public n'a qu'un seul titulaire, c'est malgré tout une liste à une entrée.

Si une fois les données initiales du marché publiées des modifications des données des titulaires interviennent, elles doivent être retranscrites dans le bloc modifications et non modifiées dans l'objet Titulaires. |

|

Identifiant du titulaire

Nom du champ :

titulaires > id |

Obligatoire |

Texte

Types d'identifiants possibles (favoriser le SIRET) :

-SIRET (identifiant français, 14 chiffres)

-TVA (numéro de TVA intracommunautaire, pour les entreprises de pays membres de l'Union Européenne)

-TAHITI (identifiants pour Tahiti et la Polynésie française, 9 chiffres)

-RIDET (identifiants pour la Nouvelle-Calédonie, 10 chiffres)

-FRWF (identifiants pour Wallis-et-Futuna, " FRWF " + 14 premières lettres de la raison sociale). Ex : FRWFDURANDCHAUFFAG

-IREP (personnes physiques françaises, 5 chiffres + LIEU DE NAISSANCE + NOM + PRENOM). Ex : 18102VANNESDURANDMATHIEU

-HORS-UE (identifiants pour les entreprises de pays non membres de l'Union Européenne. Code pays ISO 3166 + 16 premiers caractères de la dénomination sociale). Ex : BRDASILVAMOTORES |

|

Type d'identifiant

Nom du champ :

titulaires > typeIdentifiant |

Obligatoire |

Champ limité à une des valeurs suivantes (un seul choix) :

-SIRET

-TVA

-TAHITI

-RIDET

-FRWF

-IREP

-HORS-UE |

|

Type de groupement d'opérateurs économiques

Nom du champ :

typeGroupementOperateurs |

Obligatoire |

Champ limité à une des valeurs suivantes (un seul choix possible) :

-Conjoint

-Solidaire

-Pas de groupement |

|

Sous-traitance déclarée pendant la phase de passation

Nom du champ :

sousTraitanceDeclaree |

Obligatoire |

Booléen

Champ limité à une des deux valeurs suivantes (un seul choix possible) :

-oui

-non |

|

Date de publication des données essentielles du marché public

Nom du champ : datePublicationDonnees |

Obligatoire |

La date à laquelle les données du marché ont été publiées.

Date au format AAAA-MM-JJ

Type INSEE : DateType

Expression régulière de validation ('d { 4 }-'d { 2 }-'d { 2 })

Exemple : 2022-02-14 |

ISO 8601,

format étendu

http://xml.insee.fr/schema/commun.html#Date_stype

|

Actes de sous-traitance ‍ |

Actes de sous-traitance

Nom du bloc :

actesSousTraitance |

|

Liste d'objets (voir propriétés ci-après)

Si le marché public n'a qu'un seul acte de sous-traitance, c'est malgré tout une liste à une entrée. |

|

Numéro d'identification de l'acte spécial de sous-traitance

Nom du champ :

actesSousTraitance > id |

Conditionnel |

Nombre entier

Doit être unique dans la liste d'objets.

Valeur minimale : 1

Les numéros d'identification doivent être attribués en ordre croissant, en suivant l'ordre des notifications.

En l'absence de sous-traitance, ce champ est laissé vide. |

|

Identification du sous-traitant

Nom du bloc :

actesSousTraitance > sousTraitant |

|

Objet |

|

Identifiant du sous-traitant

Nom du champ :

actesSousTraitance > sousTraitant > id |

Conditionnel |

Texte

Mêmes types d'identifiants autorisés que pour titulaires > id. |

|

Type d'identifiant

Nom du champ :

actesSousTraitance > sousTraitant > typeIdentifiant |

Conditionnel |

Texte

Champ limité à une seule valeur : mêmes valeurs possibles que pour titulaires > typeIdentifiant. |

|

Durée du contrat de sous-traitance en nombre de mois

Nom du champ :

actesSousTraitance > dureeMois |

Conditionnel |

Unité : en mois

Nombre entier

Valeur minimum : 1

Ce champ a le même format que la durée de marché public (dureeMois). |

|

Date de notification de l'acte spécial de sous-traitance

Nom du champ :

actesSousTraitance > dateNotification |

Conditionnel |

Date de la réception de la notification de l'acte spécial de sous-traitance par le titulaire.

Date de notification de l'acte spécial de sous-traitance au format AAAA-MM-JJ

Type INSEE : DateType

Expression régulière de validation ('d { 4 }-'d { 2 }-'d { 2 })

Exemple : 2022-02-24 |

ISO 8601,

format étendu

http://xml.insee.fr/schema/commun.html#Date_stype

|

Montant en euros HT attribué au sous-traitant

Nom du champ :

actesSousTraitance > montant |

Conditionnel |

Unité : en euros

Nombre décimal

Montant attribué au sous-traitant hors taxes en € (ou montant estimé maximum attribué en €)

Le séparateur décimal est le point.

Exemple : 14982.29 |

Nombre JSON

Nombre XML |

Modalités de variation du prix du contrat de sous-traitance

Nom du champ :

actesSousTraitance > variationPrix |

Conditionnel |

Champ limité à une des valeurs suivantes (un seul choix possible) :

-Ferme

-Actualisable

-Révisable |

|

Date de publication des données essentielles de l'acte spécial de sous-traitance

Nom du champ : actesSousTraitance > datePublicationDonnees |

Conditionnel |

La date à laquelle les données de l'acte spécial de sous-traitance ont été publiées.

Date au format AAAA-MM-JJ

Type INSEE : DateType

Expression régulière de validation ('d { 4 }-'d { 2 }-'d { 2 })

Exemple : 2022-02-14 |

ISO 8601,

format étendu

http://xml.insee.fr/schema/commun.html#Date_stype

|

Modifications du marché public |

Modifications du marché public

Nom du bloc :

modifications |

|

Liste d'objets (voir propriétés ci-après)

Si le marché public n'a qu'une seule modification, c'est malgré tout une liste à une entrée. |

|

Numéro d'identification de la modification

Nom du champ :

modifications > id |

Conditionnel |

Nombre entier

Doit être unique dans la liste d'objets.

Valeur minimale : 1

Les numéros d'identification doivent être attribués en ordre croissant, en suivant l'ordre des notifications. |

|

Durée modifiée du marché public en nombre de mois

Nom du champ :

modifications > dureeMois |

Conditionnel |

Unité : en mois

Nombre entier

Valeur minimum : 1

Ce champ a le même format que la durée de marché public (dureeMois). |

|

Montant en euros HT modifié du marché public

Nom du champ :

modifications > montant |

Conditionnel |

Nombre décimal

Montant hors taxes en €

(ou montant estimé maximum en € dans le cas d'un accord cadre)

Le séparateur décimal est le point.

Exemple : 14982.29 |

Nombre JSON

Nombre XML |

Titulaires modifiés

Nom du bloc :

modifications > titulaires |

|

Liste d'objets

(voir les propriétés ci-après) |

|

Identifiant du titulaire modifié

Nom du champ :

modifications > titulaires > id |

Conditionnel |

Texte

Mêmes types d'identifiants autorisés que pour titulaires > id. |

|

Type d'identifiant du titulaire modifié

Nom du champ :

modifications > titulaires > typeIdentifiant |

Conditionnel |

Texte

Champ limité à une seule valeur : mêmes valeurs possibles que pour titulaires > typeIdentifiant. |

|

Date de la notification de la modification apportée au marché public

Nom du champ :

modifications > dateNotificationModification |

Conditionnel |

Date de la réception de la notification de la modification par le titulaire au format AAAA-MM-JJ

Type INSEE : DateType

Expression régulière de validation ('d { 4 }-'d { 2 }-'d { 2 })

Exemple : 2022-02-14 |

ISO 8601,

format étendu

http://xml.insee.fr/schema/commun.html#Date_stype

|

Date de publication des données essentielles de la modification apportée au marché public

Nom du champ : modifications > datePublicationDonneesModification |

Conditionnel |

La date à laquelle les données de la modification ont été publiées.

Date au format AAAA-MM-JJ

Type INSEE : DateType

Expression régulière de validation ('d { 4 }-'d { 2 }-'d { 2 })

Exemple : 2022-02-14 |

ISO 8601,

format étendu

http://xml.insee.fr/schema/commun.html#Date_stype

|

Modifications de sous-traitance pendant l'exécution |

Modification de sous-traitance pendant l'exécution

Nom du bloc :

modificationsActesSousTraitance |

|

Liste d'objets (voir propriétés ci-après)

Si le marché public n'a qu'une seule modification de sous-traitance, c'est malgré tout une liste à une entrée. |

|

Numéro d'identification de l'acte spécial de sous-traitance modifié

Nom du champ :

modificationsActesSousTraitance > id |

Conditionnel |

Nombre entier

Doit correspondre au numéro d'identifiant dans actesSousTraitance > id |

|

Durée modifiée du contrat de sous-traitance en nombre de mois

Nom du champ :

modificationsActesSousTraitance > dureeMois |

Conditionnel |

Unité : en mois

Nombre entier

Valeur minimum : 1

Si la durée n'est pas un nombre exact de mois, arrondir au nombre supérieur.

Exemples :

-9 pour 9 mois

-1 pour 2 semaines

-2 pour 1 mois et 3 semaines |

|

Date de notification de la modification de l'acte spécial de sous-traitance

Nom du champ :

modificationsActesSousTraitance > dateNotificationModificationSousTraitance |

Conditionnel |

Date de la réception de la notification de la modification de l'acte spécial de sous-traitance au format AAAA-MM-JJ

Type INSEE : DateType

Expression régulière de validation ('d { 4 }-'d { 2 }-'d { 2 })

Exemple : 2022-02-14 |

ISO 8601,

format étendu

http://xml.insee.fr/schema/commun.html#Date_stype

|

Montant en euros HT modifié de l'acte spécial de sous-traitance

Nom du champ :

modificationsActesSousTraitance > montant |

Conditionnel |

Unité : en euros

Nombre décimal

Montant attribué au sous-traitant hors taxes en € (ou montant estimé maximum en € attribué modifié)

Le séparateur décimal est le point.

Exemple : 14982.29 |

Nombre JSON

Nombre XML |

Date de publication des données essentielles de la modification de l'acte spécial de sous-traitance

Nom du champ : modificationsActesSousTraitance > datePublicationDonnees |

Conditionnel |

La date à laquelle les données de la modification d'acte de sous-traitance ont été publiées.

Date au format AAAA-MM-JJ

Type INSEE : DateType

Expression régulière de validation ('d { 4 }-'d { 2 }-'d { 2 })

Exemple : 2022-02-14 |

ISO 8601,

format étendu

http://xml.insee.fr/schema/commun.html#Date_stype

|

NOTA :

Conformément à l’article 3 de l’arrêté du 22 décembre 2023 (NOR : ECOM2332906A), ces dispositions entrent en vigueur le 1er janvier 2024 sur l'ensemble du territoire de la République.

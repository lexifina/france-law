# Article Annexe I

RÉFÉRENTIEL DES DONNÉES RELATIF AUX MARCHÉS PUBLICS

Le jeu de caractère (encoding) à utiliser est UTF-8.

Nom du champ |

Obligatoire |

Format |

Norme et nomenclature

de référence |

Identifiant unique de marché public |

Numéro d'identification unique de marché public

Format pivot :

id |

Oui |

Texte

Identifiant de marché

[année de notification (4)] [numéro interne (1-10)] [numéro d'ordre de la modification (2)]

Exemple : 2018123456789000 |

|

Caractéristiques de l'acheteur |

Acheteur ou mandataire

Format pivot

acheteur |

Oui |

Objet (propriétés ci-après)

Si le marché est passé par un groupement d'acheteurs, c'est le mandataire du groupement qui est décrit dans les données. |

|

Identification de l'acheteur

Format pivot :

acheteur > id |

Oui |

Identifiant du Système d'Identification du Répertoire des Etablissements (SIRET)

Type INSEE : ChaineNumeriqueType

Taille : 14 |

http :// xml. insee. fr/ schema/ siret. html # SIRET _ stype |

Nom de l'acheteur

Format pivot :

acheteur > nom |

Oui |

Texte

Nom de l'acheteur (le caractère univoque est assuré par le SIRET)

Exemple : " CONSEIL REGIONAL DE BRETAGNE "

Type INSEE : ChaineFrancaisOfficielType

[A-Za-zÀÂÄÇÉÈÊËÎÏÔÖÙÛÜŸàâäçéèêëîïôöùûüÿÆŒæœ'-'] * |

http :// xml. insee. fr/ schema/ commun. html # ChaineFrancaisOfficiel _ stype |

Caractéristiques du marché public |

Nature du marché

Format pivot :

nature |

Oui |

Texte

Nature du marché

Valeurs possibles :

-Marché

-Marché de partenariat

-Accord-cadre

-Marché subséquent |

|

Objet du marché ou du lot

Format pivot :

objet |

Oui |

Texte

Limité à 256 caractères. |

|

Code CPV principal

Format pivot :

codeCPV |

Oui |

Texte

Le code CPV principal (8 caractères)

Exemple : 45112500 |

|

Procédure de passation de marché

Format pivot :

procedure |

Oui |

Texte

Valeurs possibles :

-Procédure adaptée

-Appel d'offres ouvert

-Appel d'offres restreint

-Procédure concurrentielle avec négociation

-Procédure négociée avec mise en concurrence préalable

-Marché négocié sans publicité ni mise en concurrence préalable

-Dialogue compétitif |

|

Lieu principal d'exécution

Format pivot :

lieuExecution |

Oui |

Objet (propriétés ci-après) |

|

Code du lieu d'exécution

Format pivot :

lieuExecution > code |

Oui |

Texte

Code du lieu d'exécution (code postal, commune, canton, arrondissement, département, région, pays)

Exemple : " 2B002 " |

|

Type de code du lieu d'exécution

Format pivot :

lieuExecution > typeCode |

Oui |

Texte

Le type de code utilisé pour désigner le lieu d'exécution. Hormis le Code postal , les codes sont des codes géographiques gérés par l'INSEE (http :// www. insee. fr/ fr/ methodes/ nomenclatures/ cog/ default. asp)

Valeurs possibles :

-Code postal

-Code commune

-Code arrondissement

-Code canton

-Code département

-Code région

-Code pays |

|

Nom du lieu d'exécution

Format pivot :

lieuExecution > nom |

Oui |

Texte

Nom du lieu d'exécution

Type INSEE : ChaineFrancaisOfficielType

[A-Za-zÀÂÄÇÉÈÊËÎÏÔÖÙÛÜŸàâäçéèêëîïôöùûüÿÆŒæœ'-'] * |

http :// xml. insee. fr/ schema/ commun. html # ChaineFrancaisOfficiel _ stype |

Durée initiale du marché

Format pivot :

dureeMois |

Oui |

Nombre

Valeur minimum : 1

Si la durée n'est pas un nombre exact de mois, arrondir au nombre entier supérieur.

Valeur arrondie au nombre entier supérieur.

Exemples :

-9 pour 9 mois

-1 pour 2 semaines

-2 pour 1 mois et 3 semaines

Si une fois les données initiales du marché publiées une modification de la durée du marché intervient, elle doit être retranscrite via un objet enfant de Modifications et la propriété dureeMois initiale ne doit pas être modifiée. |

|

Date de notification

Format pivot :

dateNotification |

Oui |

Date de notification du marché au format AAAA-MM-JJ

Type INSEE : DateType

Expression régulière de validation ('d { 4 }-'d { 2 }-'d { 2 })

Exemple : 2016-02-24 |

ISO 8601,

format étendu

http :// xml. insee. fr/ schema/ commun. html # Date _ stype |

Date initiale de publication des données essentielles

Format pivot :

datePublicationDonnees |

Oui |

Date à laquelle les données essentielles du marché décrit ont été publiées pour la première fois. Cette date n'est donc pas mise à jour en cas de modification du marché.

Date au format AAAA-MM-JJ

Type INSEE : DateType

Expression régulière de validation ('d { 4 }-'d { 2 }-'d { 2 })

Exemple : 2016-02-24 |

ISO 8601,

format étendu

http :// xml. insee. fr/ schema/ commun. html # Date _ stype |

Caractéristiques financières |

Montant forfaitaire ou estimé maximum HT

Format pivot :

montant |

Oui |

Décimal

Montant du marché hors taxes en €

Le séparateur décimal est le point.

Exemple : 14982.29 |

|

Forme du prix

Format pivot :

formePrix |

Oui |

Texte (plusieurs choix possibles)

-Ferme

-Ferme et actualisable

-Révisable |

|

Caractéristiques d'identification des opérateurs économiques |

Titulaires

Format pivot :

titulaires |

Oui |

Liste d'objets

(voir les propriétés ci-après)

Si le marché n'a qu'un seul titulaire, c'est malgré tout une liste à une entrée.

Si une fois les données initiales du marché publiées des modifications des données des titulaires interviennent, elles doivent être retranscrites via un objet enfant de Modifications et non modifiées dans l'objet Titulaires. |

|

Identifiant du titulaire

Format pivot :

titulaires > id |

Oui |

Texte

Types d'identifiants possibles (favoriser le SIRET) :

-SIRET (identifiant français, 14 chiffres)

-TVA (numéro de TVA intracommunautaire, pour les entreprises de pays membres de l'Union Européenne)

-TAHITI (identifiants pour Tahiti et la Polynésie française, 9 chiffres)

-RIDET (identifiants pour la Nouvelle-Calédonie, 10 chiffres)

-FRWF (identifiants pour Wallis-et-Futuna, FRWF + 14 premières lettres de la raison sociale. Ex : FRWFDURANDCHAUFFAG)

-IREP (personnes physiques françaises, 5 chiffres + LIEU DE NAISSANCE + NOM + PRENOM. Ex : 18102VANNESDURANDMATHIEU)

-HORS-UE (identifiants pour les entreprises de pays non membres de l'Union Européenne. Code pays ISO 3166 + 16 premiers caractères de la dénomination sociale. Ex : BRDASILVAMOTORES) |

|

Type d'identifiant

Format pivot :

titulaires > typeIdentifiant |

Oui |

Texte

Valeurs possibles :

-SIRET

-TVA

-TAHITI

-RIDET

-FRWF

-IREP

-HORS UE |

|

Dénomination sociale

Format pivot :

titulaires > denominationSociale |

Oui |

Texte

Nom de l'opérateur économique intervenant sur le marché (le caractère univoque est assuré par le SIRET)

Exemple : " Transit 2000 SA " |

|

Modification du marché |

Modifications du marché (avenants)

Fomat pivot :

modifications |

Oui, si le marché comporte des modifications |

Liste d'objets (voir propriétés ci-après) |

|

Objet de la modification

Fomat pivot :

modifications > objetModification |

Oui |

Texte

Limité à 256 caractères.

Exemple : Modification du titulaire du marché. Nouveau titulaire : Rodriguez SAS . |

http :// xml. insee. fr/ schema/ commun. html # ChaineFrancaisOfficiel _ stype |

Date de publication des données de la modification

Format pivot :

modifications > datePublicationDonneesModification |

Oui |

Texte

Date de la republication des données incluant la modification au format AAAA-MM-JJ

Type INSEE : DateType

Expression régulière de validation ('d { 4 }-'d { 2 }-'d { 2 })

Exemple : 2016-02-24 |

ISO 8601,

format étendu

http :// xml. insee. fr/ schema/ commun. html # Date _ stype |

Modification de la durée

Format pivot :

modifications > dureeMois |

Oui, si la modification porte sur la durée |

Nombre

Valeur minimum : 1

Si la durée n'est pas un nombre exact de mois, arrondir au nombre supérieur.

Valeur arrondie au nombre supérieur.

Exemples :

-9 pour 9 mois

-1 pour 2 semaines

-2 pour 1 mois et 3 semaines |

|

Modification du montant

Format pivot :

modifications > montant |

Oui, si la modification porte sur le montant attribué HT |

Décimal

Montant hors taxes en €

Le séparateur décimal est le point.

Exemple : 14982.29 |

|

Modification des titulaires

Format pivot :

modifications > titulaires |

Oui, si la modification porte sur les titulaires |

Liste d'objets

(voir les propriétés ci-après) |

|

Identifiant du titulaire

Format pivot :

modifications > titulaires > id |

Oui, si la modification porte sur les titulaires |

Texte

Types d'identifiants possibles (favoriser le SIRET) :

-SIRET (identifiant français, 14 chiffres)

-TVA (numéro de TVA intracommunautaire, pour les entreprises de pays membres de l'Union Européenne)

-TAHITI (identifiants pour Tahiti et la Polynésie française, 9 chiffres)

-RIDET (identifiants pour la Nouvelle-Calédonie, 10 chiffres)

-FRWF (identifiants pour Wallis-et-Futuna, FRWF + 14 premières lettres de la raison sociale. Ex : FRWFDURANDCHAUFFAG)

-IREP (personnes physiques françaises, 5 chiffres + LIEU DE NAISSANCE + NOM + PRENOM. Ex : 18102VANNESDURANDMATHIEU)

-HORS-UE (identifiants pour les entreprises de pays non membres de l'Union Européenne. Code pays ISO 3166 + 16 premiers caractères de la dénomination sociale. Ex : BRDASILVAMOTORES) |

|

Type d'identifiant

Format pivot :

modifications > titulaires > typeIdentifiant |

Oui, si la modification porte sur les titulaires |

Texte

Valeurs possibles :

-SIRET

-TVA

-TAHITI

-RIDET

-FRWF

-IREP

-HORS UE |

|

Dénomination sociale

Format pivot :

modifications > titulaires > denominationSociale |

Oui, si la modification porte sur les titulaires |

Texte

Nom de l'opérateur économique intervenant sur le marché (le caractère univoque est assuré par l'identifiant)

Exemple : " Transit 2000 SA " |

|

Date de la notification de la modification

Format pivot :

modifications > dateSignatureModification |

Oui |

Texte

Date de signature du marché au format AAAA-MM-JJ

Type INSEE : DateType

Expression régulière de validation ('d { 4 }-'d { 2 }-'d { 2 })

Exemple : 2016-02-24 |

ISO 8601,

format étendu

http :// xml. insee. fr/ schema/ commun. html # Date _ stype |

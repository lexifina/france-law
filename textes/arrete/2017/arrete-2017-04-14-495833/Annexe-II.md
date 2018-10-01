# Article Annexe II

RÉFÉRENTIEL DES DONNÉES RELATIF AUX CONTRATS DE CONCESSION

Le jeu de caractère (encoding) à utiliser est UTF-8.

Nom du champ |

Obligatoire |

Format |

Norme et nomenclature de référence |

Identifiant unique de contrat concession |

Numéro d'identification unique de contrat concession

Format pivot :

id |

Oui |

Texte

Identifiant de contrat de concession

[année de notification (4)] [numéro interne (1-10)] [numéro d'ordre de la modification (2)]

Exemple : 2018123456789000 |

|

Caractéristiques de l'autorité concédante |

Autorité concédante

Format pivot :

autoriteConcedante |

Oui |

Objet (propriétés ci-après)

Si le contrat de concession est passé par un groupement, c'est le mandataire du groupement qui est décrit dans les données. |

|

Identification de l'autorité concédante

Format pivot :

autoriteConcedante > id |

Oui |

Identifiant du Système d'Identification du Répertoire des Etablissements (SIRET)

Type INSEE : ChaineNumeriqueType

Taille : 14 |

http :// xml. insee. fr/ schema/ siret. html # SIRET _ stype |

Nom de l'autorité concédante

Format pivot :

autoriteConcedante > nom |

Oui |

Texte

Nom de l'autorité concédante (le caractère univoque est assuré par le SIRET)

Exemple : " CONSEIL REGIONAL DE BRETAGNE "

Type INSEE : ChaineFrancaisOfficielType

[A-Za-zÀÂÄÇÉÈÊËÎÏÔÖÙÛÜŸàâäçéèêëîïôöùûüÿÆŒæœ'-'] * |

http :// xml. insee. fr/ schema/ commun. html # ChaineFrancaisOfficiel _ stype |

Caractéristiques du contrat de concession |

Nature du contrat de concession

Format pivot :

nature |

Oui |

Texte

Valeurs possibles :

-Concession de travaux

-Concession de service

-Concession de service public

-Délégation de service public |

|

Objet du contrat de concession

Format pivot :

objet |

Oui |

Texte

Limité à 256 caractères. |

|

Procédure de passation utilisée

Format pivot :

procedure |

Oui |

Texte

Valeurs possibles :

-Procédure négociée ouverte

-Procédure non négociée ouverte

-Procédure négociée restreinte

-Procédure non négociée restreinte |

|

Lieu principal d'exécution

Format pivot :

lieuExecution |

Oui |

Objet (propriétés ci-après) |

|

Code du lieu exécution

Format pivot :

lieuExecution > code |

Oui |

Texte

Code du lieu d'exécution (code postal, commune, canton, arrondissement, département, région, pays)

Exemple : " 2B002 " " |

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

Durée initiale du contrat de concession

Format pivot :

dureeMois |

Oui |

Nombre

Valeur minimum : 1

Si la durée n'est pas un nombre entier de mois, arrondir au nombre entier supérieur.

Valeur arrondie au nombre entier supérieur.

Exemples :

-9 pour 9 mois

-1 pour 2 semaines

-2 pour 1 mois et 3 semaines |

|

Date de signature

Format pivot :

dateSignature |

Oui |

Date de signature du contrat de concession au format AAAA-MM-JJ

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

Date à laquelle les données essentielles du contrat de concession ont été publiées pour la première fois sur le profil d'acheteur. Cette date n'est donc pas mise à jour en cas de modification du contrat concession.

Date au format AAAA-MM-JJ

Type INSEE : DateType

Expression régulière de validation ('d { 4 }-'d { 2 }-'d { 2 })

Exemple : 2016-02-24 |

ISO 8601,

format étendu

http :// xml. insee. fr/ schema/ commun. html # Date _ stype |

Date de début d'exécution

Format pivot :

dateDebutExecution |

Oui |

Date de début d'exécution du contrat de concession

Date au format AAAA-MM-JJ

Type INSEE : DateType

Expression régulière de validation ('d { 4 }-'d { 2 }-'d { 2 })

Exemple : 2016-02-24 |

ISO 8601,

format étendu

http :// xml. insee. fr/ schema/ commun. html # Date _ stype |

Caractéristiques financières |

Valeur globale HT attribuée

Format pivot :

valeurGlobale |

Oui |

Décimal

Le séparateur décimal est le point.

Exemple : 14982.29 |

|

Montant de la subvention publique

Format pivot :

montantSubventionPublique |

Oui |

Décimal

Le séparateur décimal est le point.

Exemple : 14982.29 |

|

Données d'exécution du contrat de concession |

Données d'exécution du contrat de concession

Format pivot :

donneesExecution |

Oui |

Liste d'objets

Les données d'exécution du contrat de concession à une date donnée. Tous les ans, l'autorité concédante publie les données d'exécution, jusqu'à la fin du contrat de concession.

Ces données ne sont inclues qu'à partir de la première année, pas lors de la publication initiale des données qui fait suite à la notification. |

|

Date de publication des données d'exécution

Format pivot :

donneesExecution > datePublicationDonneesExecution |

Oui |

La date à laquelle les données d'exécution ont été publiées.

Date au format AAAA-MM-JJ

Type INSEE : DateType

Expression régulière de validation ('d { 4 }-'d { 2 }-'d { 2 })

Exemple : 2016-02-24 |

|

Dépenses d'investissement

Format pivot :

donneesExecution > depensesInvestissement |

Oui |

Décimal

Les dépenses d'investissement réalisées par le concessionnaire.

Le séparateur décimal est le point.

Exemple : 14982.29 |

|

Tarifs à la charge des usagers

Format pivot :

donneesExecution > tarifs |

Oui |

Liste d'objets (propriétés ci-après)

Les principaux tarifs à la charge des usagers. |

|

Intitulé du tarif

Format pivot :

donneesExecution > tarifs > intituleTarif |

Oui |

Texte

Intitulé du tarif

Maximum 256 caractères |

|

Tarif

Format pivot :

donneesExecution > tarifs > tarif |

Oui |

Décimal

Le séparateur décimal est le point.

Exemple : 14.29 |

|

Caractéristiques d'identification des opérateurs économiques |

Concessionnaires

Format pivot :

concessionnaires |

Oui |

Liste d'objets

(voir les propriétés ci-après)

Si le contrat de concession n'a qu'un seul concessionnaire, c'est malgré tout une liste à une entrée.

Si une fois les données initiales du contrat de concession publiées des modifications des données des titulaires interviennent, elles doivent être retranscrites via un objet enfant de Modifications et non modifiées dans l'objet Titulaires. |

|

Identifiant du concessionnaire

Format pivot :

concessionnaires > id |

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

concessionnaires > typeIdentifiant |

Oui |

Texte

Valeurs possibles :

-SIRET

-TVA

-TAHITI

-RIDET

-FRWF

-IREP

-HORS-UE |

|

Dénomination sociale

Format pivot :

concessionnaires > denominationSociale |

Oui |

Texte

Nom de l'opérateur économique intervenant sur le contrat de concession (le caractère univoque est assuré par l'identifiant)

Exemple : " Transit 2000 SA " |

|

Modification du contrat de concession |

Modifications du contrat de concession

Fomat pivot :

modifications |

Oui |

Liste d'objets (voir propriétés ci-après) |

|

Objet de la modification

Fomat pivot :

modifications > objetModification |

Oui |

Texte

Limité à 256 caractères.

Exemple : Modification du concessionnaire. Nouveau concessionnaire : Rodriguez SAS . |

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

Nouvelle durée du contrat de concession.

Valeur minimum : 1 |

|

Modification de la valeur globale HT

Format pivot :

modifications > valeurGlobale |

Oui, si la modification porte sur la valeur globale |

Décimal

Nouvelle valeur globale du contrat de concession.

Le séparateur décimal est le point.

Exemple : 14982.29 |

|

Date de signature de la modification

Format pivot :

modifications > dateSignatureModification |

Oui |

Texte

Date de signature de la modification au contrat de concession au format AAAA-MM-JJ

Type INSEE : DateType

Expression régulière de validation ('d { 4 }-'d { 2 }-'d { 2 })

Exemple : 2016-02-24 |

ISO 8601,

format étendu

http :// xml. insee. fr/ schema/ commun. html # Date _ stype |

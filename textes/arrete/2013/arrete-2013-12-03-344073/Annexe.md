# Article Annexe

FORMAT DES DÉCLARATIONS

Pour faciliter la lecture de la présente annexe, il est précisé que le terme “ influenceur ” utilisé dans celle-ci renvoie aux bénéficiaires suivants mentionnés au I de l'article L. 1453-1 du code de la santé publique : “ 7° bis Les personnes qui, dans les médias ou sur les réseaux sociaux, présentent un ou plusieurs produits de santé, de manière à influencer le public ” ;

1. Généralités

RÈGLES LIÉES À CHAQUE DÉCLARATION |

Toute déclaration est enregistrée au moyen d'un couple unique composé de :

-l'identifiant interne à la base identifiant l'entreprise ;

-et de l'identifiant unique attribué par l'entreprise à chaque ligne déclarée.

|

L'identifiant interne de l'entreprise :

-est automatiquement enregistré par le système lorsque l'utilisateur se rend sur l'écran Déclarer correspondant à l'entreprise pour saisir en ligne dans le tableau ;

-doit être renseigné par l'utilisateur entreprise lorsque la déclaration s'effectue par envoi automatique par l'intermédiaire du webservice.

|

RÈGLES LIÉES AUX FORMAT |

Un champ obligatoire non rempli génère une erreur (donc la ligne n'est pas transmise et enregistrée en base) |

Un champ de type Liste dont la valeur n'appartient pas à la liste des valeurs possibles génère une erreur |

Un champ dont la valeur ne correspond pas à son format génère une erreur |

Une valeur non-renseignée correspond à aucun caractère (et non pas à un caractère espace par exemple) |

2. Déclaration

Par saisie en ligne ou envoi par webservice :

NOM DU CHAMP |

OBLIGATOIRE/ FACULTATIF |

DESCRIPTION |

FORMAT |

LISTE DE VALEURS Codes à utiliser pour le Webservice = Libellés à utiliser pour la saisie en ligne |

Action |

Obligatoire |

. Action de déclaration à indiquer.

. Une seule valeur attendue.

|

Liste |

-C = Création

-M = Modification

-S = Suppression

|

Déclaration |

Obligatoire |

. Type de déclaration à indiquer.

. Une seule valeur attendue.

|

Liste |

-convention = Convention

-rémunération = Rémunération

-avantage = Avantage

|

Identifiant unique |

Obligatoire |

. Identifiant unique de déclaration dans le système de l'entreprise déclarante à indiquer.

. Cette valeur joue le rôle de clé pour identifier de manière unique la déclaration. Elle est fournie en entrée par l'entreprise pour pouvoir par exemple procéder à une correction ultérieure.

. Format : [0-9] [A-Z], caractères “ tiret ” et “ underscore ” autorisés, 128 caractères maximum.

|

Texte |

|

Identifiant de la convention liée |

Obligatoire pour une rémunération |

. Identifiant unique de la convention à laquelle est liée obligatoirement une rémunération.

. Format : [0-9] [A-Z], caractères " tiret " et " underscore " autorisés, 128 caractères maximum.

|

Texte |

|

Facultatif pour un avantage |

. Identifiant unique de la convention à laquelle peut être lié un avantage.

. Format : [0-9] [A-Z], caractères " tiret " et " underscore " autorisés, 128 caractères maximum.

|

|

|

Objet convention/ nature avantage |

Obligatoire pour les conventions et les avantages |

. Objet de la convention/ nature de l'avantage

. Une seule valeur attendue.

|

Liste |

Typologie pour les objets de convention :

-ADS = Achat de documentation scientifique

-AUTRE = Autre

-AECES = Contrat d'achat ou de location d'espaces dans le cadre de manifestations scientifiques

-AEP = Contrat d'achat ou de location d'espaces publicitaires

-CEAS = Contrat de conseil/ d'expertise autre que scientifique

-CES = Contrat d'expert scientifique

-EEE = Enquête, étude, étude de marché (hors recherche)

-CDLE = Cession de droits/ licence d'exploitation

-CEVS = Contrat d'évaluation scientifique

-CI = Contrat d'interview

-IC = Contrat de participation à une manifestation

-CIM = Contrat d'intervenant à une manifestation

-RB = Contrat de remise d'une bourse de recherche

-RP = Contrat de remise de prix

-RS = Contrat de recherche scientifique

-DON = Mécénat

-ED = Edition

-EPC = Evaluation produit cosmétique

-FOR = Formation

-PARR = Parrainage

-PART = Partenariat

-VPC = Vigilance produit cosmétique

Typologie pour les natures d'avantage :

-AUTRE = Autre

-BR = Bourse de recherche

-BF = Bourse de formation

-DEF = Défraiement

-DF = Don ou prêt pour la formation

-DM = Don de matériel

-DE = Don d'échantillons

-DO = Don d'ouvrages

-DP = Don ou prêt pour la recherche

-DFT = Don de fonctionnement

-FI = Frais d'inscription à une manifestation

-FRO = Frais de réunion/ d'organisation

-FT = Frais de transport

-HC = Hospitalité-collation

-HH = Hospitalité-hébergement

-HR = Hospitalité-restauration

-IND = Indemnisation

-PM = Prêt de matériel

-PR = Prix de recherche

|

Autre |

Obligatoire si la valeur " Autre " a été saisie dans le champ " Objet convention/ nature avantage " |

. Si la valeur " Autre " a été saisie dans le champ " Objet convention/ nature avantage ", indiquer dans ce champ les compléments nécessaires pour préciser l'objet de la convention ou la nature de l'avantage.

. Format : 255 caractères maximum.

|

Texte |

|

Montant |

Obligatoire |

. Montant des conventions, des rémunérations et des avantages.

. Nombre entier.

. Montant en euros.

. Montant supérieur ou égal à 10 € pour les rémunérations et les avantages.

|

Montant |

|

Date de signature/

versement

|

Obligatoire |

. Date de signature des conventions.

. Date de versement des rémunérations et des avantages.

. Format : jj/ mm/ aaaa.

|

Date |

|

Date de début |

Obligatoire pour les conventions |

. Date de début de la convention.

. Format : jj/ mm/ aaaa.

|

Date |

|

Date de fin |

Facultative pour les conventions |

. Date de fin de la convention.

. Format : jj/ mm/ aaaa.

. La date de fin doit être supérieure ou égale à la date début.

|

Date |

|

Informations convention |

Obligatoire |

. Lorsque la convention a pour objet une manifestation, indiquer l'organisateur, le nom, la date et le lieu de la manifestation.

. Format : 255 caractères maximum.

|

Texte |

|

Facultatif |

. Indiquer des précisions sur la convention.

. Format : 255 caractères maximum.

|

Catégorie de bénéficiaire |

Obligatoire |

. Catégorie du bénéficiaire.

. Une seule valeur possible.

|

Liste |

Personnes physiques :

-ETU = Etudiant

-INF = Influenceur

-PRS = Professionnel de santé

-VET = Vétérinaire

Personnes morales :

-FON = Académie, fondation, société savante et organisme de conseils

-APS = Association de professionnels de santé

-ADU = Association d'étudiants

-AUS = Association d'usagers du système de santé

-LOG = Editeur de logiciel

-ETA = Etablissement de santé

-AGR = Groupement professionnel agricole

-SAN = Groupement sanitaire

-PMO = Personne morale assurant la formation initiale ou continue des professionnels de santé

-PRE = Presse et média

-VPM = Vétérinaire personne morale

|

Type d'identifiant

professionnel

|

Obligatoire |

. Type d'identifiant utilisé pour identifier le bénéficiaire.

. Une seule valeur possible.

|

Liste |

Les valeurs sont les mêmes pour la saisie en ligne et le web service.

Pour les professionnels de santé :

-RPPS/ ADELI

-ORDRE

-AUTRE

Pour les étudiants :

-RPPS/ ADELI

-AUTRE

Pour les vétérinaires :

-ORDRE

-AUTRE

Pour les influenceurs :

-AUTRE

Pour les personnes morales :

-SIREN

-FINESS

-RNA

-AMALIA

-AUTRE

|

Numéro d'identifiant professionnel |

Obligatoire sauf pour la catégorie de bénéficiaire " Influenceur " |

. Valeur de l'identifiant du bénéficiaire correspondant au Type d'identifiant professionnel choisi :

-Si le Type d'identifiant professionnel est RPPS/ ADELI : identifiant personnel du bénéficiaire dans le Répertoire Partagé des Professionnel de Santé ;

-Si le Type d'identifiant professionnel est ORDRE : numéro d'inscription à l'ordre ;

-Si le Type d'identifiant professionnel est SIREN : le numéro siren ;

-Si le Type d'identifiant professionnel est FINESS : le numéro finess ;

-Si le Type d'identifiant professionnel est RNA : le numéro rna ;

-Si le Type d'identifiant professionnel est AMALIA : le numéro amalia ;

-Si le Type d'identifiant professionnel est AUTRE : valeur à renseigner. Ne rien mettre si inconnu.

. Format : 255 caractères maximum.

|

Texte |

|

Profession |

Obligatoire pour la catégorie de bénéficiaire " Professionnel de santé " |

. Qualité/ profession du bénéficiaire.

. Une seule valeur possible.

|

Liste |

-10 = Médecin

-21 = Pharmacien

-26 = Audioprothésiste

-31 = Assistant dentaire

-32 = Physicien médical

-36 = Ambulancier

-37 = Auxiliaire de puériculture

-40 = Chirurgien-Dentiste

-50 = Sage-Femme

-60 = Infirmier

-69 = Infirmier psychiatrique

-70 = Masseur-Kinésithérapeute

-80 = Pédicure-Podologue

-81 = Orthoprothésiste

-82 = Podo-Orthésiste

-83 = Orthopédiste-Orthésiste

-84 = Oculariste

-85 = Epithésiste

-86 = Technicien de laboratoire médical

-91 = Orthophoniste

-92 = Orthoptiste

-94 = Ergothérapeute

-95 = Diététicien

-96 = Psychomotricien

-98 = Manipulateur ERM

-313 = Aide-soignant

-316 = Préparateur en pharmacie hospitalière

-317 = Préparateur en pharmacie officine

|

Facultatif pour la catégorie de bénéficiaire " Etudiant " |

. Qualité/ profession du bénéficiaire.

. Une seule valeur possible.

|

Liste |

-10 = Médecin

-21 = Pharmacien

-26 = Audioprothésiste

-31 = Assistant dentaire

-32 = Physicien médical

-36 = Ambulancier

-37 = Auxiliaire de puériculture

-40 = Chirurgien-Dentiste

-50 = Sage-Femme

-60 = Infirmier

-69 = Infirmier psychiatrique

-70 = Masseur-Kinésithérapeute

-80 = Pédicure-Podologue

-81 = Orthoprothésiste

-82 = Podo-Orthésiste

-83 = Orthopédiste-Orthésiste

-84 = Oculariste

-85 = Epithésiste

-86 = Technicien de laboratoire médical

-91 = Orthophoniste

-92 = Orthoptiste

-94 = Ergothérapeute

-95 = Diététicien

-96 = Psychomotricien

-98 = Manipulateur ERM

-313 = Aide-soignant

-316 = Préparateur en pharmacie hospitalière

-317 = Préparateur en pharmacie officine

-VET = Vétérinaire

|

Identité/ Nom |

Obligatoire |

. Pour les personnes physiques :

-Nom d'un professionnel de santé, d'un vétérinaire ou d'un étudiant ;

-Dénomination d'un influenceur.

. Pour les personnes morales :

-Nom de l'établissement ou de l'association ;

-Dénomination sociale d'une entreprise.

. Format : 255 caractères.

|

Texte |

|

Prénom |

Obligatoire sauf pour la catégorie de bénéficiaire " Influenceur " |

. Prénom d'une personne physique hors catégorie professionnelle " Influenceur " : professionnel de santé, vétérinaire ou étudiant.

. Format : 255 caractères.

|

Texte |

|

Structure d'exercice/

de rattachement

|

Obligatoire pour la catégorie de bénéficiaire " Etudiant " |

. Nom de l'établissement d'enseignement ou de l'organisme de rattachement.

. Format : 255 caractères maximum.

|

Texte |

|

Facultatif pour les catégories de bénéficiaire " Professionnel de santé " et " Vétérinaire " |

. Indiquer des précisions sur la structure d'exercice.

. Format : 255 caractères maximum.

|

Texte |

|

Pays |

Obligatoire sauf pour la catégorie de bénéficiaire " Influenceur " |

. Pays du bénéficiaire.

. Une seule valeur possible.

|

Liste |

Norme ISO 3166-1 alpha-2 |

Code postal |

Obligatoire sauf pour la catégorie de bénéficiaire " Influenceur " |

. Pour les personnes physiques :

-Si la catégorie de bénéficiaire est " Professionnel de santé " ou " Vétérinaire " : le code postal de l'adresse professionnelle ;

-Si la catégorie de bénéficiaire est " Etudiant " : le code postal de l'adresse de son établissement de rattachement.

. Pour les personnes morales :

-Le code postal de l'adresse de l'établissement ;

-Le code postal d'adresse du siège social de l'entreprise ou de l'association.

. Format : 255 caractères maximum.

|

Code postal |

|

Ville |

Obligatoire sauf pour la catégorie de bénéficiaire " Influenceur " |

. Pour les personnes physiques :

-Si la catégorie de bénéficiaire est " Professionnel de santé " ou " Vétérinaire " : la ville de l'adresse professionnelle ;

-Si la catégorie de bénéficiaire est " Etudiant " : la ville de l'adresse de son établissement de rattachement.

. Pour les personnes morales ;

-La ville de l'adresse de l'établissement ;

-La ville de l'adresse du siège social de l'entreprise ou de l'association.

. Format : 255 caractères maximum.

|

Texte |

|

Adresse |

Obligatoire sauf pour la catégorie de bénéficiaire " Influenceur " |

. Pour les personnes physiques :

-Si la catégorie est " Professionnel de santé " ou " Vétérinaire " : l'adresse professionnelle ;

-Si la catégorie de bénéficiaire est " Etudiant " : l'adresse de son établissement de rattachement.

. Pour les personnes morales :

-L'adresse de l'établissement ;

-L'adresse du siège social de l'entreprise ou de l'association.

. Format : 255 caractères maximum.

|

Texte |

|

Champ supplémentaire pour l'envoi par webservice :

NOM DU CHAMP |

OBLIGATOIRE/ FACULTATIF |

DESCRIPTION |

FORMAT |

LISTE DE VALEUR |

Demande de

rectification

|

Obligatoire |

. Pour indiquer si la déclaration est faite en réponse à une demande de rectification d'un bénéficiaire.

. Si l'Action sur une déclaration est " Modification " ou " Suppression ", indiquer une seule valeur possible.

. Si la valeur " Oui " est indiquée : l'action une fois enregistrée éteint la demande de rectification sur la déclaration et le marqueur disparaît sur le site grand public.

|

Liste |

-OUI-NON |

.

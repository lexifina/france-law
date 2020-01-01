# Article Annexe 1

ANNEXE 1

LISTE DES DONNÉES OBLIGATOIREMENT TRANSMISES PAR L'EXPLOITANT DU DÉFIBRILLATEUR

LISTE DES DONNÉES OBLIGATOIRES |

DONNÉES RELATIVES À L'IDENTIFICATION ET À LA LOCALISATION DU DAE |

Champ |

Libellé |

Type |

Description |

Exemple |

Valeur |

Diffusion |

etat_valid |

Validation par l'exploitant des données |

Chaîne de caractères

Enumération |

Un seul choix parmi les possibilités suivantes : validées, en attente de validation, mises en doute |

|

Technique |

Publique |

nom |

Nom donné au DAE |

Chaîne de caractères |

Nom du défibrillateur déterminé librement |

DAE-MinSanté-Duquesne DAE-Boulangerie-avenue-Kléber |

Obligatoire |

Publique |

lat_coor1 |

Coordonnée de latitude |

Nombre réel |

Les coordonnées sont exprimées conformément à la projection légale. Le signe de séparation entre les parties entière et décimale du nombre est le point. |

|

Obligatoire |

Publique |

long_coor1 |

Coordonnée de longitude |

Nombre réel |

Les coordonnées sont exprimées conformément à la projection légale. Le signe de séparation entre les parties entière et décimale du nombre est le point. |

|

Obligatoire |

Publique |

DONNÉES RELATIVES AUX MODALITÉS D'ACCÈS DU DAE |

Champ |

Libellé |

Type |

Description |

Exemple |

Valeur |

Diffusion |

acc |

Environnement d'accès du DAE |

Chaîne de caractères

Enumération |

Un seul choix possible parmi les 2 possibilités suivantes : intérieur ou extérieur |

|

Obligatoire |

Publique |

acc_lib |

Accès libre du DAE |

Booléen |

Présence d'un DAE en accès libre, avec la possibilité de l'utiliser sans l'intervention d'une personne habilitée (par exemple dans le cas où le DAE serait dans un coffre fermé à clé). Un seul choix parmi les deux possibilités suivantes : OUI/NON |

|

Obligatoire |

Publique |

Champ |

Libellé |

Type |

Description |

Exemple |

Valeur |

Diffusion |

disp_j |

Jours d'accessibilité de l'appareil |

Chaîne de caractères Enumération |

Jours lors desquels le DAE est accessible. Plusieurs choix possibles parmi les propositions suivantes : 7j/7, lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche, jours fériés, événements |

Lundi, mercredi, vendredi |

Obligatoire |

Publique |

disp_h |

Heures d'accessibilité de l'appareil |

Chaîne de caractères Enumération |

Heures lors desquelles le DAE est accessible. Plusieurs choix possibles parmi les propositions suivantes : 24h/24, heures ouvrables, heures de nuit |

Heures ouvrables |

Obligatoire |

Publique |

tel1 |

Numéro de téléphone 1 sur le site d'implantation du DAE |

Chaîne de caractères |

Numéro de téléphone de la personne à contacter sur le site d'implantation du DAE, effectivement joignable. Conformité au standard norme ITU E123 et E164. Aucun séparateur entre les chiffres ne doit être utilisé |

+33601020304 |

Obligatoire |

Limitée |

DONNÉES RELATIVES AUX CARACTÉRISTIQUES TECHNIQUES DU DAE |

Champ |

Libellé |

Type |

Description |

Exemple |

Valeur |

Diffusion |

etat_fonct |

Etat de fonctionnement du DAE |

Chaîne de caractères Enumération |

Un seul choix parmi les possibilités suivantes : En fonctionnement / Hors service / Supprimé définitivement / Absent momentanément / Inconnu |

|

Obligatoire |

Publique |

fab_rais |

Raison sociale du fabricant du DAE |

Chaîne de caractères |

Telle qu'elle est indiquée sur le registre du commerce, en dehors de tout nom commercial |

CardiacScience, Philips, PhysioControl, Shiller, Zoll |

Obligatoire |

Limitée |

modele |

Nom du modèle de DAE |

Chaîne de caractères |

Nom tel qu'il est inscrit sur le DAE et/ou sa notice |

G3, HS1, CR+, Fredeasy, AED PLUS |

Obligatoire |

Limitée |

num_serie |

Numéro de série du DAE |

Chaîne de caractères |

Numéro tel qu'il est inscrit sur le DAE |

X09E409930 |

Obligatoire |

Limitée |

dermnt |

Date de la dernière maintenance du DAE |

Date |

Les dates sont exprimées au format ISO 8601. La déclaration se fera selon le format suivant : AAAA-MM-JJ |

2020-02-01 |

Obligatoire |

Publique |

DONNÉES RELATIVES À L'EXPLOITANT |

Champ |

Libellé |

Type |

Description |

Exemple |

Valeur |

Diffusion |

expt_siren |

Numéro SIREN de l'exploitant |

Chaîne de caractères |

Chaîne de 9 chiffres telle qu'elle est délivrée par l'INSEE |

|

Obligatoire |

Limitée |

expt_rais |

Raison sociale de l'exploitant, personne morale |

Chaîne de caractères |

Telle qu'elle est indiquée sur le registre du commerce, en dehors de tout nom commercial. L'exploitant est le propriétaire du DAE, seul responsable de la déclaration sur la base |

|

Obligatoire |

Publique |

expt_tel1 |

Numéro de téléphone 1 de l'exploitant |

Chaîne de caractères |

Conformité au standard norme ITU E123 et E164. Aucun séparateur entre les chiffres ne doit être utilisé |

+33601020304 |

Obligatoire |

Limitée |

expt_email |

Adresse électronique de l'exploitant |

Chaîne de caractères |

Conformité au standard |

|

Obligatoire |

Limitée |

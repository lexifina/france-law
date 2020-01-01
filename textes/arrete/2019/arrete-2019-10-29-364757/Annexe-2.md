# Article Annexe 2

ANNEXE 2

LISTE DES DONNÉES COMPLÉMENTAIRES NON OBLIGATOIRES TRANSMISES PAR L'EXPLOITANT DU DÉFIBRILLATEUR

LISTE DES DONNÉES COMPLÉMENTAIRES NON OBLIGATOIRES |

DONNÉES RELATIVES À L'IDENTIFICATION ET À LA LOCALISATION DU DAE |

Champ |

Libellé |

Type |

Description |

Exemple |

Valeur |

Diffusion |

adr_num |

Numéro de la voie et, le cas échéant, suffixe d'implantation du DAE |

Chaîne de caractères |

Cette information suffixée peut être un indice de répétition ('bis', 'ter', 'qua', 'qui', etc. codés sur 3 caractères en minuscules) ou un complément comme le nom d'entrée d'immeuble ('a', 'b', 'c', 'a1', 'b2', 'lesmimosas', etc. codés en minuscules non accentuées, sans espace ni limite du nombre de caractères). Dans le cas des voies ou des lieux-dits sans adresse, la valeur '99999' est attendue. Dans le cas d'une adresse indiquant un intervalle entre deux numéros, ces derniers sont séparés par une barre oblique. Conformité au format Base Adresse Locale (BAL) en priorité et le cas échéant suivant les standards de la Base Adresse Nationale (BAN) |

3bis 4b 21/25 |

Facultatif |

Publique |

adr_voie |

Type et nom de la voie ou lieu-dit d'implantation du DAE |

Chaîne de caractères Champ libre |

Champ libre à compléter en majuscules et minuscules accentuées. Maximum 255 caractères. Conformité au format Base Adresse Locale (BAL) en priorité et le cas échéant suivant les standards de la Base Adresse Nationale (BAN) |

avenue Duquesne |

Facultatif |

Publique |

DONNÉES RELATIVES AUX MODALITÉS D'ACCÈS DU DAE |

Champ |

Libellé |

Type |

Description |

Exemple |

Valeur |

Diffusion |

acc_pcsec |

Poste de sécurité |

Booléen |

Présence d'un poste de sécurité au sein du bâtiment. Un seul choix parmi les deux possibilités suivantes : OUI/NON |

|

Facultative |

Publique |

acc_acc |

Présence d'un accueil public |

Booléen |

Présence de personnels d'accueil dans le bâtiment. Un seul choix parmi les deux possibilités suivantes : OUI/NON |

|

Facultative |

Publique |

acc_etg |

Etage d'accessibilité du DAE |

Chaîne de caractères Champ libre |

Etage du bâtiment dans lequel le DAE est accessible. L'étage est saisi en valeur numérique selon la convention suivante : 0 signifie rez-de chaussée, -1 signifie sous-sol, 1 signifie 1er étage, etc. Champ libre à compléter en majuscules et minuscules accentuées. Maximum 255 caractères |

0 -1 |

Facultative |

Publique |

acc_complt |

Complément d'information sur l'accès au DAE |

Chaîne de caractères Champ libre |

Les informations sur la situation du DAE sont saisies de manière libre et sans limite de caractères, en veillant à être le plus clair possible et à utiliser des repères facilement identifiables (machines à café, extincteur, etc.). Champ libre à compléter en majuscules et minuscules accentuées. |

Au bout du couloir gauche, dans un renfoncement à droite |

Facultative |

Publique |

photo1 |

Photo 1 du DAE dans son environnement |

Chaîne de caractères |

Photo au format url. Il est préconisé un plan large pour que le DAE soit visible dans son environnement. La photo déposée devra être libre de droit, sous format Open Source. |

|

Facultative |

Publique |

Champ |

Libellé |

Type |

Description |

Exemple |

Valeur |

Diffusion |

photo2 |

Photo 2 du DAE dans son environnement |

Chaîne de caractères |

Photo au format url. Il est préconisé un plan large pour que le DAE soit visible dans son environnement. La photo déposée devra être libre de droit, sous format Open Source. |

|

Facultative |

Publique |

disp_complt |

Complément d'information sur la disponibilité du DAE |

Chaîne de caractères Champ libre |

Toutes informations complémentaires concernant la disponibilité jugées utiles au format OpenstreetMap. Champ libre à compléter en majuscules et minuscules accentuées. Maximum 255 caractères |

Mo-Fr 08 : 00-09 : 00 |

Facultative |

Publique |

tel2 |

Numéro 2 de téléphone sur le site d'implantation du DAE |

Chaîne de caractères |

Numéro de téléphone de la personne à contacter sur le site d'implantation du DAE. Conformité au standard norme ITU E123 et E164. Aucun séparateur entre les chiffres ne doit être utilisé |

+33102030405 |

Facultative |

Limitée |

site_email |

Adresse email de contact du site où le DAE a été implanté |

Chaîne de caractères |

Conformité au standard |

|

Facultative |

Limitée |

DONNÉES RELATIVES AUX CARACTÉRISTIQUES TECHNIQUES DU DAE |

Champ |

Libellé |

Type |

Description |

Exemple |

Valeur |

Diffusion |

date_instal |

Date d'installation du DAE |

Date |

Les dates sont exprimées au format ISO 8601. La déclaration se fera selon le format suivant : AAAA-MM-JJ |

2020-02-01 |

Facultative |

Publique |

fab_siren |

Numéro SIREN du fabricant du DAE |

Chaîne de caractères |

Chaîne de 9 chiffres telle qu'elle est indiquée sur le registre du commerce |

|

Facultative |

Limitée |

mnt_siren |

Numéro SIREN du mainteneur du DAE |

Champ numérique |

Chaîne de 9 chiffres telle qu'elle est indiquée sur le registre du commerce |

|

Facultative |

Limitée |

Champ |

Libellé |

Type |

Description |

Exemple |

Valeur |

Diffusion |

id_euro |

Identifiant unique du dispositif (IUD européen) |

Chaîne de caractères |

Numéro tel qu'il sera inscrit sur le DAE |

|

Facultative |

Publique |

lc_ped |

Présence d'électrodes pédiatriques |

Booléen |

Indiquer la présence ou non d'électrodes pédiatriques avec l'appareil. Un seul choix parmi les deux possibilités suivantes : OUI/NON |

|

Facultative |

Publique |

dtpr_lcped |

Date de péremption des électrodes pédiatriques |

Date |

Les dates sont exprimées au format ISO 8601. La déclaration se fera selon le format suivant : AAAA-MM-JJ |

2020-02-01 |

Facultative |

Publique |

dtpr_lcad |

Date de péremption des électrodes adultes |

Date |

Les dates sont exprimées au format ISO 8601. La déclaration se fera selon le format suivant : AAAA-MM-JJ |

2020-02-01 |

Facultative |

Publique |

dtpr_bat |

Date de péremption de la batterie |

Date |

Les dates sont exprimées au format ISO 8601. La déclaration se fera selon le format suivant : AAAA-MM-JJ |

2020-02-01 |

Facultative |

Publique |

freq_mnt |

Fréquence de la maintenance |

Chaîne de caractères Champ libre |

Echelle de temps entre deux interventions de maintenance sur un appareil. Champ libre à compléter en majuscules et minuscules accentuées. Maximum 255 caractères |

2 fois par an 1 fois tous les deux mois |

Facultative |

Publique |

dispsurv |

Dispositif de surveillance à distance du DAE |

Booléen |

Le DAE est-il équipé d'un dispositif connecté de surveillance à distance ? Un seul choix parmi les deux possibilités suivantes : OUI/NON |

|

Facultative |

Publique |

DONNÉES RELATIVES À L'EXPLOITANT |

Champ |

Libellé |

Type |

Description |

Exemple |

Valeur |

Diffusion |

expt_tel2 |

Numéro de téléphone 2 de l'exploitant |

Champ numérique |

Conformité au standard norme ITU E123 et E164.

Aucun séparateur entre les chiffres ne doit être utilisé |

+33102030405 |

Facultative |

Limitée |

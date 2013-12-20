# Article Annexe

FORMAT CSV

Généralités

FORMAT

|

DESCRIPTION

|

EXEMPLE DE VALEUR

|

TEXTE

|

Alphanumérique en majuscules sans accent et de longueur au plus égale à 256 caractères

|

MEDECIN

|

IDENTIFIANT

|

[0-9][A-Z] - Caractères tiret et underscore autorisés - Longueur au plus égale à 128 caractères

|

1234-67

|

MONTANT

|

Montant : entier arrondi à l'euro supérieur au plus égal à 1 000 000 (à valider)

|

159

|

CODEPOSTAL

|

Code postal : alphanumérique sur 10 caractères

|

75008

|

DATE

|

Date : JJ/MM/AAAA sur 10 caractères

|

05/09/2013

|

LISTE

|

Valeur parmi une liste de valeurs possibles - Entre crochets

|

[RPPS]

|

.

RÈGLES DE GESTION LIÉES AU FICHIER CSV

|

Format : UTF-8

|

Séparateur : Pipe (c'est-à-dire |)

|

En-tête de colonne sur la première ligne : oui (obligatoire)

|

Nom du fichier : identifiant#AAAAMMJJ#HHmmss#declaration.csv

|

Avec identifiant = identifiant de connexion du compte déclarant obtenu lors de l'inscription au site unique

|

Exemple : 12345678#20130905#205612#declaration.csv

|

.

RÈGLES DE GESTION LIÉES AU FORMAT

|

Un champ obligatoire non rempli génère une erreur (donc la ligne de déclaration n'est pas importée)

|

Un champ de type LISTE dont la valeur n'appartient pas à la liste des valeurs possibles génère une erreur

|

Un champ dont la valeur ne correspond pas à son format génère une erreur

|

.

AUTRES RÈGLES DE GESTION

|

Une valeur non renseignée ne correspond à aucun caractère (et non un caractère espace par exemple)

|

Exemple en 3e position : [A]|21/09/2013||Manifestation

|

Aucune valeur ne peut contenir le caractère pipe (|)

|

Déclaration

NOM

du champ

|

OBLIGATOIRE

|

UNICITÉ

|

DESCRIPTIF

du champ

|

FORMAT

|

LISTE

de valeurs/

commentaire

|

RÈGLE

de gestion

alerte

|

RÈGLE

de gestion

erreur

|

ENTREPRISE_IDENTIFIANT

|

Oui

|

Le couple (ENTREPRISE

IDENTIFIANT, LIGNE_IDENTIFIANT) est unique

|

Identifiant unique de l'entreprise ayant signé cette convention ou versé cet avantage

|

IDENTIFIANT

|

Cette valeur permet d'attacher cette ligne de déclaration à l'entreprise (mandant) concernée si une entreprise (mandataire) transmet cette ligne de déclaration. Cette colonne permet de gérer le cas d'une entreprise qui déclare pour d'autres entreprises lui ayant donné mandat. Sinon l'entreprise déclarante indique son propre identifiant récupéré lors de son inscription sur le site unique.

|

|

Si la valeur ENTREPRISE_IDENTIFIANt#LIGNE

_IDENTIFIANT existe déjà dans le système et que la valeur LIGNE_ACTION est égale à [C] ;

Si la valeur ENTREPRISE_IDENTIFIANt#LIGNE_

IDENTIFIANT n'existe pas dans le système et que la valeur LIGNE_ACTION est égale à [M] ou [V] ;

Si la valeur ENTREPRISE_IDENTIFIANT n'existe pas dans le système ;

Si la valeur ENTREPRISE_IDENTIFIANT n'est pas un compte (ou un sous-compte) géré par le compte de l'utilisateur qui importe le fichier ou appelle le service web (gestion des habilitations).

|

LIGNE_IDENTIFIANT

|

Oui

|

Identifiant unique de la ligne de déclaration (convention ou avantage) dans le système de l'entreprise déclarante

|

IDENTIFIANT

|

Cette valeur joue le rôle de clé pour identifier de manière unique cette ligne de déclaration (avantage ou convention). Elle est fournie en entrée par l'entreprise pour pouvoir par exemple procéder à une correction ultérieure.

|

|

|

LIGNE_ACTION

|

Oui

|

Non

|

Code action

|

LISTE

|

[C] pour Création ;

[M] pour Modification ;

[S] pour Suppression ;

[V] pour Validation (cas d'un retour suite à alerte).

Important : lorsque le champ LIGNE_ACTION est égal à [V], aucun contrôle de type ALERTE n'est réalisé puisque l'entreprise valide les données de cette ligne de déclaration. En revanche les contrôles de type ERREUR sont toujours exécutés.

|

|

|

LIGNE_DEMANDE_

RECTIFICATION

|

Oui

|

Non

|

Ligne corrige une demande de rectification d'un bénéficiaire.

|

LISTE

|

[O] Oui ;

[N] Non.

Si [O], suppression du marqueur de demande de rectification du bénéficiaire sur le site grand public.

|

|

|

BENEF_CATEGORIE

|

Oui

|

Non

|

Catégorie du bénéficiaire

|

LISTE

|

[PRS] Les professionnels de santé relevant de la quatrième partie du présent code ;

[APS] Les associations de professionnels de santé ;

[ETU] Les étudiants se destinant aux professions relevant de la quatrième partie du présent code ainsi que les associations et groupements les représentant ;

[AUS] Les associations d'usagers du système de santé ;

[ETA] Les établissements de santé relevant de la sixième partie du présent code ;

[FON] Les fondations, les sociétés savantes et les sociétés ou organismes de conseil intervenant dans le secteur des produits ou prestations mentionnés au premier alinéa ;

[PRE] Les entreprises éditrices de presse, les éditeurs de services de radio ou de télévision et les éditeurs de services de communication au public en ligne ;

[LOG] Les éditeurs de logiciels d'aide à la prescription et à la délivrance ;

[PMO] Les personnes morales assurant la formation initiale des professionnels de santé mentionnés au 1° ou participant à cette formation.

|

|

|

BENEF_NOM

|

Oui si le champ BENEF_CATEGORIE a la valeur [PRS] ou [ETU] ;

Non sinon.

|

Non

|

Nom du bénéficiaire

|

TEXTE

|

|

Valeur renseignée alors que la valeur du champ BENEF_CATEGORIE est différente de [PRS] et [ETU].

|

|

BENEF_PRENOM

|

Oui si le champ BENEF_CATEGORIE a la valeur [PRS] ou [ETU] ;

Non sinon.

|

Non

|

Prénom du bénéficiaire

|

TEXTE

|

|

Valeur renseignée alors que la valeur du champ BENEF_CATEGORIE est différente de [PRS] et [ETU].

|

|

BENEF_QUALITE

|

Oui si le champ BENEF_CATEGORIE a la valeur [PRS] ;

Non sinon.

|

Non

|

Qualité/profession du bénéficiaire

|

LISTE

|

[10] Médecin ;

[40] Chirurgien-dentiste ;

[50] Sage-femme ;

[21] Pharmacien ;

[01] Préparateur en pharmacie et préparateur en pharmacie hospitalière ;

[60] Infirmier ;

[70] Masseur-kinésithérapeute ;

[80] Pédicure-podologue ;

[94] Ergothérapeute ;

[96] Psychomotricien ;

[91] Orthophoniste ;

[92] Orthoptiste ;

[98] Manipulateur d'électroradiologie médicale ;

[86] Technicien de laboratoire médical ;

[05] Audioprothésiste ;

[28] Opticien-lunetier ;

[82] Prothésiste et orthésiste pour l'appareillage des personnes handicapées ;

[95] Diététicien ;

[02] Aide-soignant ;

[03] Auxiliaire de puériculture ;

[04] Ambulancier.

|

Valeur renseignée alors que la valeur du champ BENEF_CATEGORIE est différente de [PRS].

|

|

BENEF_ADRESSE1

|

Oui si le champ BENEF_CATEGORIE a la valeur [PRS] ou [APS] ou [AUS] ou [ETA] ou [FON] ou [PRE] ou [LOG] ou [PMO] ;

Non sinon.

|

Non

|

Adresse du bénéficiaire

|

TEXTE

|

Adresse professionnelle si la valeur du champ BENEF_CATEGORIE est égale à [PRS] ;

Adresse siège social ou équivalent si la valeur du champ BENEF_CATEGORIE est égale à [APS] ou [AUS] ou [ETA] ou [FON] ou [PRE] ou [LOG] ou [PMO].

|

Valeur renseignée alors que la valeur du champ BENEF_CATEGORIE est différente de [PRS] ou [APS] ou [AUS] ou [ETA] ou [FON] ou [PRE] ou [LOG] ou [PMO].

|

|

BENEF_ADRESSE2

|

Non

|

Non

|

Complément 1 de l'adresse du bénéficiaire

|

TEXTE

|

|

Valeur renseignée alors que la valeur du champ BENEF_CATEGORIE est différente de [PRS] ou [APS] ou [AUS] ou [ETA] ou [FON] ou [PRE] ou [LOG] ou [PMO].

|

|

BENEF_ADRESSE3

|

Non

|

Non

|

Complément 2 de l'adresse du bénéficiaire

|

TEXTE

|

|

Valeur renseignée alors que la valeur du champ BENEF_CATEGORIE est différente de [PRS] ou [APS] ou [AUS] ou [ETA] ou [FON] ou [PRE] ou [LOG] ou [PMO].

|

|

BENEF_ADRESSE4

|

Non

|

Non

|

Complément 3 de l'adresse du bénéficiaire

|

TEXTE

|

|

Valeur renseignée alors que la valeur du champ BENEF_CATEGORIE est différente de [PRS] ou [APS] ou [AUS] ou [ETA] ou [FON] ou [PRE] ou [LOG] ou [PMO].

|

|

BENEF_CODEPOSTAL

|

Oui si le champ BENEF_CATEGORIE a la valeur [PRS] ou [APS] ou [AUS] ou [ETA] ou [FON] ou [PRE] ou [LOG] ou [PMO] ;

Non sinon.

|

Non

|

Code postal du bénéficiaire

|

CODEPOSTAL

|

|

Valeur renseignée alors que la valeur du champ BENEF_CATEGORIE est différente de [PRS] ou [APS] ou [AUS] ou [ETA] ou [FON] ou [PRE] ou [LOG] ou [PMO].

|

|

BENEF_VILLE

|

Oui si le champ BENEF_CATEGORIE a la valeur [PRS] ou [APS] ou [AUS] ou [ETA] ou [FON] ou [PRE] ou [LOG] ou [PMO] ;

Non sinon.

|

Non

|

Ville du bénéficiaire

|

LISTE

|

|

Valeur renseignée alors que la valeur du champ BENEF_CATEGORIE est différente de [PRS] ou [APS] ou [AUS] ou [ETA] ou [FON] ou [PRE] ou [LOG] ou [PMO].

|

|

BENEF_PAYS

|

Oui si le champ BENEF_CATEGORIE a la valeur [PRS] ou [APS] ou [AUS] ou [ETA] ou [FON] ou [PRE] ou [LOG] ou [PMO] ;

Non sinon.

|

Non

|

Pays du bénéficiaire

|

LISTE

|

Norme ISO 3166-1 alpha-2 (entre crochets).

Exemple : [FR] pour France.

|

Valeur renseignée alors que la valeur du champ BENEF_CATEGORIE est différente de [PRS] ou [APS] ou [AUS] ou [ETA] ou [FON] ou [PRE] ou [LOG] ou [PMO].

|

|

BENEF_TITRE

|

Non

|

Non

|

Titre du bénéficiaire

|

LISTE

|

[PR] Professeur ;

[MG] Médecin général ;

[PG] Pharmacien général ;

[PC] Pharmacien-chef ;

[MC] Médecin-chef ;

[DR] Docteur ;

[AUTRE] Autre.

|

Valeur renseignée alors que la valeur du champ BENEF_CATEGORIE est différente de [PRS].

|

|

BENEF_SPECIALITE

|

Non

|

Non

|

Spécialité (ou discipline) du bénéficiaire

|

LISTE

|

[SCD01] Orthopédie dento-faciale ;

[SCD02] Chirurgie orale ;

[SCD03] Médecine bucco-dentaire ;

[SM01] Anatomie et cytologie pathologiques ;

[SM02] Anesthésie-réanimation ;

[SM03] Biologie médicale ;

[SM04] Cardiologie et maladies vasculaires ;

[SM05] Chirurgie générale ;

[SM06] Chirurgie maxillo-faciale ;

[SM07] Chirurgie maxillo-faciale et stomatologie ;

[SM08] Chirurgie orthopédique et traumatologie ;

[SM09] Chirurgie infantile ;

|

Valeur renseignée alors que la valeur du champ BENEF_CATEGORIE est différente de [PRS].

|

|

[SM10] Chirurgie plastique reconstructrice et esthétique ;

[SM11] Chirurgie thoracique et cardio-vasculaire ;

[SM12] Chirurgie urologique ;

[SM13] Chirurgie vasculaire ;

[SM14] Chirurgie viscérale et digestive ;

[SM15] Dermatologie et vénéréologie ;

[SM16] Endocrinologie et métabolisme ;

[SM17] Génétique médicale ;

[SM18] Gériatrie ;

[SM19] Gynécologie médicale ;

|

[SM20] Gynécologie-obstétrique ;

[SM21] Hématologie ;

[SM22] Hématologie (option maladie du sang) ;

[SM23] Hématologie (option onco-hématologie) ;

[SM24] Gastro-entérologie et hépatologie ;

[SM25] Médecine du travail ;

[SM26] Qualifié en médecine générale ;

[SM27] Médecine interne ;

[SM28] Médecine nucléaire ;

[SM29] Médecine physique et réadaptation ;

[SM30] Néphrologie ;

[SM31] Neuro-chirurgie ;

[SM32] Neurologie ;

[SM33] Neuro-psychiatrie ;

[SM34] ORL et chirurgie cervico-faciale ;

[SM35] Oncologie (option onco-hématologie) ;

|

[SM36] Oncologie (option médicale) ;

[SM37] Oncologie (option radiothérapie) ;

[SM38] Ophtalmologie ;

[SM39] Oto-rhino-laryngologie ;

[SM40] Pédiatrie ;

[SM41] Pneumologie ;

[SM42] Psychiatrie ;

[SM43] Psychiatrie (option enfant et adolescent) ;

[SM44] Radiodiagnostic ;

[SM45] Radiothérapie ;

[SM46] Réanimation médicale ;

[SM47] Recherche médicale ;

[SM48] Rhumatologie ;

[SM49] Santé publique et médecine sociale ;

[SM50] Stomatologie ;

[SM51] Gynéco-obstétrique et gynécologie médicale option ;

|

[SM52] Gynéco-obstétrique et gynécologie médicale option ;

[SM53] Spécialiste en médecine générale ;

[SM54] Médecine générale ;

[SM55] Radiodiagnostic et radio-thérapie ;

[SM99] ORL et ophtalmologie ;

[SP01] Radiopharmacie ;

[SP02] Hygiène ;

[SP03] Pharmacovigilance ;

[SP04] Hémovigilance ;

[AUTRE] Autre.

|

BENEF_QUALIFICATION

|

Non

|

Non

|

Qualification du bénéficiaire

|

TEXTE

|

Champ volontairement libre

|

Valeur renseignée alors que la valeur du champ BENEF_CATEGORIE est différente de [PRS].

|

|

BENEF_IDENTIFIANT_TYPE

|

Oui

|

Non

|

Type d'identifiant utilisé pour identifier le bénéficiaire

|

LISTE

|

[RPPS] pour l'identifiant personnel du bénéficiaire dans le répertoire partagé des professionnels de santé ;

[ORDRE] pour le numéro d'inscription à l'ordre ;

[AUTRE] pour les autres cas.

|

|

|

BENEF_IDENTIFIANT_VALEUR

|

Oui

|

Non

|

Valeur de l'identifiant du bénéficiaire

|

TEXTE

|

Si le champ BENEF_IDENTIFIANT_TYPE égal à [RPPS], identifiant personnel du bénéficiaire dans le répertoire partagé des professionnels de santé ;

Si le champ BENEF_IDENTIFIANT_TYPE égal à [ORDRE], numéro d'inscription à l'ordre ;

[SO] si le champ BENEF_IDENTIFIANT_TYPE égal à [AUTRE] et la valeur est non renseignée ;

Valeur libre si le champ BENEF_IDENTIFIANT_TYPE égal à [AUTRE] et la valeur est renseignée.

|

|

|

BENEF_ETABLISSEMENT

|

Oui si le champ BENEF_CATEGORIE a la valeur [ETU] ;

Non sinon.

|

Non

|

Nom de l'établissement d'enseignement

|

TEXTE

|

|

Valeur renseignée alors que la valeur du champ BENEF_CATEGORIE est différente de [ETU].

|

|

BENEF_ETABLISSEMENT_

CODEPOSTAL

|

Oui si le champ BENEF_CATEGORIE a la valeur [ETU] ;

Non sinon.

|

Non

|

Code postal de l'établissement d'enseignement

|

CODEPOSTAL

|

|

Valeur renseignée alors que la valeur du champ BENEF_CATEGORIE est différente de [ETU].

|

|

BENEF_ETABLISSEMENT_VILLE

|

Oui si le champ BENEF_CATEGORIE a la valeur [ETU] ;

Non sinon.

|

Non

|

Ville de l'établissement d'enseignement

|

TEXTE

|

|

Valeur renseignée alors que la valeur du champ BENEF_CATEGORIE est différente de [ETU].

|

|

BENEF_DENOMINATIONSOCIALE

|

Oui si le champ BENEF_CATEGORIE a la valeur [APS] ou [AUS] ou [ETA] ou [FON] ou [PRE] ou [LOG] ou [PMO] ;

Non sinon.

|

Non

|

Dénomination sociale du bénéficiaire

|

TEXTE

|

|

Valeur renseignée alors que la valeur du champ BENEF_CATEGORIE est différente de [APS] ou [AUS] ou [ETA] ou [FON] ou [PRE] ou [LOG] ou [PMO].

|

|

BENEF_OBJETSOCIAL

|

Oui si le champ BENEF_CATEGORIE a la valeur [APS] ou [AUS] ou [ETA] ou [FON] ou [PRE] ou [LOG] ou [PMO] ;

Non sinon.

|

Non

|

Objet social du bénéficiaire

|

TEXTE

|

|

Valeur renseignée alors que la valeur du champ BENEF_CATEGORIE est différente de [APS] ou [AUS] ou [ETA] ou [FON] ou [PRE] ou [LOG] ou [PMO].

|

|

LIGNE_TYPE

|

Oui

|

Non

|

Avantage ou convention

|

LISTE

|

[A] pour Avantage ;

[C] pour Convention.

|

|

|

CONV_DATE_SIGNATURE

|

Oui si le champ LIGNE_TYPE est égal à [C] ;

Non sinon (dans ce cas les lignes sont ignorées).

|

Non

|

Date de signature de la convention

|

DATE

|

Format JJ/MM/AAAA

|

Valeur renseignée alors que la valeur du champ LIGNE_TYPE est différente de [C].

|

|

CONV_OBJET

|

|

Non

|

Objet de la convention

|

TEXTE

|

|

Valeur renseignée alors que la valeur du champ LIGNE_TYPE est différente de [C].

|

|

CONV_DATE_DEBUT

|

|

Non

|

Date de début de couverture de la convention

|

DATE

|

Format JJ/MM/AAAA

|

Valeur renseignée alors que la valeur du champ LIGNE_TYPE est différente de [C].

|

|

CONV_DATE_FIN

|

Non

|

Non

|

Date de fin de couverture de la convention

|

DATE

|

Format JJ/MM/AAAA

|

Valeur renseignée alors que la valeur du champ LIGNE_TYPE est différente de [C].

|

|

CONV_EVENEMENT_DATE

|

Non

|

Non

|

Date de l'événement lié à la convention

|

DATE

|

Format JJ/MM/AAAA

A compléter si la convention concerne une manifestation (remplace le dépôt du programme sous forme de PDF)

|

Valeur renseignée alors que la valeur du champ LIGNE_TYPE est différente de [C].

|

|

CONV_EVENEMENT_NOM

|

Non

|

Non

|

Nom de l'événement lié à la convention

|

TEXTE

|

A compléter si la convention concerne une manifestation (remplace le dépôt du programme sous forme de PDF)

|

Valeur renseignée alors que la valeur du champ LIGNE_TYPE est différente de [C].

|

|

CONV_EVENEMENT_LIEU

|

Non

|

Non

|

Lieu de l'événement lié à la convention

|

TEXTE

|

A compléter si la convention concerne une manifestation (remplace le dépôt du programme sous forme de PDF)

|

Valeur renseignée alors que la valeur du champ LIGNE_TYPE est différente de [C].

|

|

AVANT_DATE

|

Oui si le champ LIGNE_TYPE est égal à [A] ;

Non sinon (dans ce cas les lignes sont ignorées).

|

Non

|

Date où l'avantage a été accordé

|

DATE

|

Format JJ/MM/AAAA

|

Valeur renseignée alors que la valeur du champ LIGNE_TYPE est différente de [A].

|

|

AVANT_MONTANT_TTC

|

Non

|

Montant TTC arrondi à l'euro le plus proche

|

MONTANT

|

|

> 15 000 €

Valeur renseignée alors que la valeur du champ LIGNE_TYPE est différente de [A]

|

< 10 €

|

AVANT_NATURE

|

|

Non

|

Nature de l'avantage accordé

|

TEXTE

|

|

Valeur renseignée alors que la valeur du champ LIGNE_TYPE est différente de [A].

|

|

AVANT_CONVENTION_LIE

|

Non

|

Non

|

Intitulé ou référence de la convention éventuellement liée à cet avantage (pas de lien informatique avec la convention)

|

TEXTE

|

|

Valeur renseignée alors que la valeur du champ LIGNE_TYPE est différente de [A].

|

|

Pièce jointe

Nom de la pièce jointe

|

ENTREPRISE_IDENTIFIANT#LIGNE_IDENTIFIANT (doit correspondre aux deux premières colonnes du fichier CSV)

|

Extension

|

pdf

|

Longueur du nom

|

inférieure à 256 caractères

|

Règles de gestion liées à la pièce jointe : si le fichier existe déjà, il est écrasé sans alerte ni erreur.

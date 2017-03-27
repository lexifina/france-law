# Article Annexe

FORMAT CSV

Généralités

RÈGLES DE GESTION LIÉES AU FICHIER CSV |

Format : UTF-8 |

Séparateur : Pipe (c'est-à-dire |) |

En-tête de colonne sur la première ligne : oui (obligatoire) |

Nom du fichier : identifiant # AAAAMMJJ # HHmmss # declaration. csv |

Avec identifiant = = identifiant de connexion du compte déclarant obtenu lors de l'inscription au site unique |

Exemple : 12345678 # 20130905 # 205612 # declaration. csv |

RÈGLES DE GESTION LIÉES AU FORMAT |

Un champ obligatoire non rempli génère une erreur (donc la ligne de déclaration n'est pas importée) |

Un champ de type LISTE dont la valeur n'appartient pas à la liste des valeurs possibles génère une erreur |

Un champ dont la valeur ne correspond à à son format génère une erreur |

AUTRES RÈGLES DE GESTION |

Une valeur non renseignée correspond à aucun caractère (et non un caractère espace par exemple) |

Exemple en 3e position : [A] | 21/09/2013 | | Manifestation |

Aucune valeur ne peut contenir le caractère pipe (|) |

Déclaration

NOM DU CHAMP |

OBLIGATOIRE |

UNICITÉ |

DESCRIPTIF

du champ |

FORMAT |

LISTE DE VALEURS/

commentaire |

ENTREPRISE _ IDENTIFIANT |

Oui |

Le couple

(ENTREPRISE _ IDENTIFIANT,

LIGNE _ IDENTIFIANT) est unique |

Identifiant unique de l'entreprise ayant signé cette convention ou versé cet avantage |

IDENTIFIANT |

Cette valeur permet d'attacher cette ligne de déclaration à l'entreprise (mandant) concernée si une entreprise (mandataire) transmet cette ligne de déclaration. Cette colonne permet de gérer le cas d'une entreprise qui déclare pour d'autres entreprises lui ayant donné mandat. Sinon l'entreprise déclarante indique son propre identifiant récupéré lors de son inscription sur le site unique. |

LIGNE _ IDENTIFIANT |

Oui |

Identifiant unique de la ligne de déclaration (convention ou avantage) dans le système de l'entreprise déclarante |

IDENTIFIANT |

Cette valeur joue le rôle de clé pour identifier de manière unique cette ligne de déclaration (avantage, rémunération ou convention). Elle est fournie en entrée par l'entreprise pour pouvoir par exemple procéder à une correction ultérieure. |

LIGNE _ ACTION |

Oui |

Non |

Code action |

LISTE |

-[C] pour Création

-[M] pour Modification

-[S] pour Suppression

-[V] pour Validation (cas d'un retour suite à alerte) Important : lorsque le champ LIGNE _ ACTION est égal à [V], aucun contrôle de type ALERTE n'est réalisé puisque l'entreprise valide les données de cette ligne de déclaration. Par contre les contrôle de type ERREUR sont toujours exécutés. |

LIGNE _ DEMANDE _ RECTIFICATION |

Oui |

Non |

Ligne corrige une demande de rectification d'un bénéficiaire. |

LISTE |

-[O] Oui

-[N] Non

Si [O], suppression du marqueur de demande de rectification du bénéficiaire sur le site grand public |

BENEF _ CATEGORIE |

Oui |

Non |

Catégorie

du bénéficiaire |

LISTE |

-[PRS] Les professionnels de santé relevant de la quatrième partie du présent code

-[APS] Les associations de professionnels de santé

-[ETU] Les étudiants se destinant aux professions relevant de la quatrième partie du présent code ainsi que les associations et groupements les représentant

-[AUS] Les associations d'usagers du système de santé

-[ETA] Les établissements de santé relevant de la sixième partie du présent code

-[FON] Les académies, fondations, les sociétés savantes et les sociétés ou organismes de conseil intervenant dans le secteur des produits ou prestations mentionnés au premier alinéa

-[PRE] Les entreprises éditrices de presse, les éditeurs de services de radio ou de télévision et les éditeurs de services de communication au public en ligne

-[LOG] Les éditeurs de logiciels d'aide à la prescription et à la délivrance

-[PMO] Les personnes morales assurant la formation initiale ou continue des professionnels de santé mentionnés au 1° ou participant à cette formation

-[ADU] Les associations d

'étudiants

-[VET] Les vétérinaires

-[SAN] Les groupements de défense sanitaire

-[AGR] Les groupements reconnus de producteurs, les groupements professionnels agricoles |

BENEF _ NOM |

-Oui si le champ BENEF _ CATEGORIE a la valeur [PRS] ou [ETU] ou [VET]

-Non sinon |

Non |

Nom du bénéficiaire |

TEXTE |

|

BENEF _ PRENOM |

-Oui si le champ BENEF _ CATEGORIE a la valeur [PRS] ou [ETU] ou [VET]

-Non sinon |

Non |

Prénom

du bénéficiaire |

TEXTE |

|

BENEF _ QUALITE |

-Oui si le champ BENEF _ CATEGORIE a la valeur [PRS]

-Non sinon |

Non |

Qualité/ profession

du bénéficiaire |

LISTE |

-[10] Médecin

-[40] Chirurgien-dentiste

-[50] Sage-femme

-[21] Pharmacien

-[01] Préparateur en pharmacie et préparateur en pharmacie hospitalière

-[60] Infirmier

-[70] Masseur-kinésithérapeute

-[80] Pédicure-podologue

-[94] Ergothérapeute

-[96] Psychomotricien

-[91] Orthophoniste

-[92] Orthoptiste

-[98] Manipulateur d'électroradiologie médicale

-[86] Technicien de laboratoire médical

-[05] Audioprothésiste

-[28] Opticien-lunetier

-[82] Prothésiste et orthésiste pour l'appareillage des personnes handicapées

-[95] Diététicien

-[02] Aide soignant

-[03] Auxiliaire de puériculture

-[04] Ambulancier

-[ADE] Assistant dentaire |

BENEF _ ADRESSE1 |

-Oui si le champ BENEF _ CATEGORIE a la valeur [PRS] ou [APS] ou [AUS] ou [ETA] ou [FON] ou [PRE] ou [LOG] ou [PMO] ou [ADU] ou [AGR] ou [SAN] ou [VET]

-Non sinon |

Non |

Adresse

du bénéficiaire |

TEXTE |

-Adresse professionnelle si la valeur du champ BENEF _ CATEGORIE est égale à [PRS] ou [VET]

-Adresse siège social ou équivalent si la valeur du champ BENEF _ CATEGORIE est égale à

[APS] ou [AUS] ou [ETA] ou [FON] ou [PRE] ou [LOG] ou [PMO] ou [ADU] |

BENEF _ ADRESSE2 |

Non |

Non |

Complément 1

de l'adresse

du bénéficiaire |

TEXTE |

BENEF _ ADRESSE3 |

Non |

Non |

Complément 2

de l'adresse

du bénéficiaire |

TEXTE |

BENEF _ ADRESSE4 |

Non |

Non |

Complément 3

de l'adresse

du bénéficiaire |

TEXTE |

BENEF _ CODEPOSTAL |

-Oui si le champ BENEF _ CATEGORIE a la valeur [PRS] ou [APS] ou [AUS] ou [ETA] ou [FON] ou [PRE] ou [LOG] ou [PMO] ou [ADU] ou [AGR] ou [SAN] ou [VET]

-Non sinon |

Non |

Code postal

du bénéficiaire |

CODEPOSTAL |

BENEF _ VILLE |

-Oui si le champ BENEF _ CATEGORIE a la valeur [PRS] ou [APS] ou [AUS] ou [ETA] ou [FON] ou [PRE] ou [LOG] ou [PMO] ou [AGR] ou [SAN] ou [VET]

-Non sinon |

Non |

Ville du bénéficiaire |

TEXTE |

BENEF _ PAYS |

-Oui si le champ BENEF _ CATEGORIE a la valeur [PRS] ou [APS] ou [AUS] ou [ETA] ou [FON] ou [PRE] ou [LOG] ou [PMO] ou [ADU] ou [AGR] ou [SAN] ou [VET]

-Non sinon |

Non |

Pays du bénéficiaire |

LISTE |

-Norme ISO 3166-1 alpha-2 (entre crochet) Exemple : [FR] pour France |

BENEF _ TITRE |

Non |

Non |

Titre du bénéficiaire |

LISTE |

-[PR] Professeur

-[MG] Médecin Général

-[PG] Pharmacien Général

-[PC] Pharmacien Chef

-[MC] Médecin chef

-[DR] Docteur

-[AUTRE] Autre |

BENEF _ SPECIALITE |

Non |

Non |

Spécialité (ou discipline) du bénéficiaire |

LISTE |

-[SCD01] Orthopédie dento-faciale

-[SCD02] Chirurgie Orale

-[SCD03] Médecine Bucco-Dentaire

-[SM01] Anatomie et cytologie pathologiques

-[SM02] Anesthesie-réanimation

-[SM03] Biologie médicale

-[SM04] Cardiologie et maladies vasculaires

-[SM05] Chirurgie générale

-[SM06] Chirurgie maxillo-faciale

-[SM07] Chirurgie maxillo-faciale et stomatologie

-[SM08] Chirurgie orthopédique et traumatologie

-[SM09] Chirurgie infantile

-[SM10] Chirurgie plastique reconstructrice et esthétique

-[SM11] Chirurgie thoracique et cardio-vasculaire

-[SM12] Chirurgie urologique

-[SM13] Chirurgie vasculaire

-[SM14] Chirurgie viscérale et digestive

-[SM15] Dermatologie et vénéréologie

-[SM16] Endocrinologie et métabolisme

-[SM17] Génétique médicale

-[SM18] Gériatrie

-[SM19] Gynécologie médicale

-[SM20] Gynécologie-obstétrique

-[SM21] Hématologie

-[SM22] Hématologie (option Maladie du sang)

-[SM23] Hématologie (option Onco-hématologie)

-[SM24] Gastro-entérologie et hépatologie

-[SM25] Médecine du travail

-[SM26] Qualifié en Médecine Générale

-[SM27] Médecine interne

-[SM28] Médecine nucléaire

-[SM29] Médecine physique et réadaptation

-[SM30] Néphrologie

-[SM31] Neuro-chirurgie

-[SM32] Neurologie

-[SM33] Neuro-psychiatrie

-[SM34] ORL et chirurgie cervico faciale

-[SM35] Oncologie (option onco-hématologie)

-[SM36] Oncologie option médicale

-[SM37] Oncologie option radiothérapie

-[SM38] Ophtalmologie

-[SM39] Oto-rhino-laryngologie

-[SM40] Pédiatrie

-[SM41] Pneumologie-

[SM42] Psychiatrie

-[SM43] Psychiatrie option enfant & adolescent-[SM44] Radio-diagnostic

-[SM45] Radio-thérapie

-[SM46] Réanimation médicale

-[SM47] Recherche médicale

-[SM48] Rhumatologie

-[SM49] Santé publique et médecine sociale

-[SM50] Stomatologie

-[SM51] Gynéco-obstétrique et gynécologie médicale option 1

-[SM52] Gynéco-obstétrique et gynécologie médicale option 2

-[SM53] Spécialiste en Médecine Générale

-[SM54] Médecine Générale

-[SM55] Radio-diagnostic et Radio-Thérapie

-[SM99] ORL et ophtalmologie

-[SP01] Radio-pharmacie

-[SP02] Hygiène

-[SP03] Pharmacovigilance

-[SP04] Hémovigilance

-[AUTRE] Autre |

BENEF _ IDENTIFIANT _ TYPE |

Oui |

Non |

Type d'identifiant utilisé pour identifier le bénéficiaire |

LISTE |

-Si le champ BENEF _ CATEGORIE est égale à [PRS], les valeurs autorisées sont :'[RPPS] pour l'identifiant personnel du bénéficiaire dans le Répertoire Partagé des Professionnel de Santé, [ORDRE] pour le numéro d'inscription à l'ordre, [AUTRE] pour les autres cas

-Si le champ BENEF _ CATEGORIE est égale à [VET], les valeurs autorisées sont :'[ORDRE] pour le numéro d'inscription à l'ordre

-Si le champ BENEF _ CATEGORIE est égale à [APS] ou [AUS] ou [ETA] ou [FON] ou [PRE] ou [LOG] ou [PMO] ou [ADU] ou [SAN] ou [AGR], les valeurs autorisées sont :'[SIREN] pour le numéro SIREN, [FINESS] pour le numéro FINESS, [AUTRE] pour les autres cas

-Si le champ BENEF _ CATEGORIE est égale à [ETU], les valeurs autorisées sont : [RPPS], [AUTRE] |

BENEF _ IDENTIFIANT _ VALEUR |

-Oui si BENEF _ IDENTIFIANT _ TYPE différent de [AUTRE]

-Non sinon |

Non |

Valeur

de l'identifiant

du bénéficiaire |

TEXTE |

-Si le champ BENEF _ IDENTIFIANT _ TYPE égal à [RPPS], identifiant personnel du bénéficiaire dans le Répertoire Partagé des Professionnel de Santé

-Si le champ BENEF _ IDENTIFIANT _ TYPE égal à [ORDRE], numéro d'inscription à l'ordre

-Si le champ BENEF _ IDENTIFIANT _ TYPE égal à [SIREN], le numéro siren

-Si le champ BENEF _ IDENTIFIANT _ TYPE égal à [FINESS], le numéro finess.

-Valeur libre si le champ BENEF _ IDENTIFIANT _ TYPE égal à [AUTRE] et la valeur est renseignée. Ne rien mettre si inconnu. |

BENEF _ ETABLISSEMENT |

-Oui si le champ BENEF _ CATEGORIE a la valeur [ETU]

-Non sinon |

Non |

Nom

de l'établissement d'enseignement |

TEXTE |

|

BENEF _ ETABLISSEMENT _ CODEPOSTAL |

-Oui si le champ BENEF _ CATEGORIE a la valeur [ETU]

-Non sinon |

Non |

Code postal

de l'établissement

d'enseignement |

CODEPOSTAL |

|

BENEF _ ETABLISSEMENT _ VILLE |

-Oui si le champ BENEF _ CATEGORIE a la valeur [ETU]

-Non sinon |

Non |

Ville

de l'établissement

d'enseignement |

TEXTE |

|

BENEF _ DENOMINATIONSOCIALE |

-Oui si le champ BENEF _ CATEGORIE a la valeur [APS] ou [AUS] ou [ETA] ou [FON] ou [PRE] ou [LOG] ou [PMO] ou [ADU] ou [AGR] ou [SAN]

-Non sinon |

Non |

Dénomination

sociale

du bénéficiaire |

TEXTE |

|

BENEF _ OBJETSOCIAL |

-Oui si le champ BENEF _ CATEGORIE a la valeur [APS] ou [AUS] ou [ETA] ou [FON] ou [PRE] ou [LOG] ou [PMO] ou [ADU] ou [AGR] ou [SAN]

-Non sinon |

Non |

Objet social

du bénéficiaire |

TEXTE |

|

LIGNE _ TYPE |

Oui |

Non |

Avantage ou convention ou rémunération |

LISTE |

-[A] pour Avantage

-[C] pour Convention

-[R] pour Rémunération |

CONV _ DATE _ SIGNATURE |

-Oui si le champ LIGNE _ TYPE est égal à [C]

-Non sinon (dans ce cas les lignes sont ignorées) |

Non |

Date de signature de la convention |

DATE |

Format JJ/ MM/ AAAA |

CONV _ OBJET |

|

Non |

Objet

de la convention |

LISTE |

-[A] Autre (PRECISER DANS LA COLONNE CONV _ OBJET _ AUTRE)

-[ADS] Achat de documentation scientifique

-[AECES] Achat/ location d'espaces dans le cadre d'événements scientifiques

-[AEP] Achat/ location d'espace publicitaire

-[APS] Autres prestations de services

-[CDLE] Cession de droits/ licence d'exploitation

-[CEAS] Contrat/ expertise autre que scientifique

-[CES] Contrat d'expert scientifique, contrat dans le cadre d'une recherche, contrat de consultant

-[CI] Contrat d'interview

-[CIM] Contrat d'intervenant à une manifestation/ orateur

-[DON] Don/ Mécénat

-[ED] Edition

-[EEE] Enquête/ Etude/ Etude de marché (hors recherche)

-[EPC] Evaluation produit cosmétique

-[FOR] Formation

-[HOS] Hospitalité

-[IC] Inscription congrès

-[PARR] Parrainage

-[PART] Partenariat

-[PM] Prêt de matériel

-[RB] Remise d'une bourse

-[RP] Remise de prix

-[RS] Recherche scientifique

-[VPC] Vigilance produit cosmétique |

CONV _ OBJET _ AUTRE |

|

Non |

Précision de l'objet de la convention |

TEXTE |

|

CONV _ DATE _ DEBUT |

|

Non |

Date de début

de couverture

de la convention |

DATE |

Format JJ/ MM/ AAAA |

CONV _ DATE _ FIN |

Non |

Non |

Date de fin

de couverture

de la convention |

DATE |

Format JJ/ MM/ AAAA |

CONV _ MONTANT |

Non |

Non |

Somme versée

au titre

de la convention (Montant) |

MONTANT |

|

CONV _ EVENEMENT _ DATE |

Non |

Non |

Date

de l'événement

lié à la convention |

DATE |

Format JJ/ MM/ AAAA A compléter si la convention concerne une manifestation (remplace le dépôt du programme sous forme de PDF) |

CONV _ EVENEMENT _ NOM |

Non |

Non |

Nom

de l'événement

lié à la convention |

TEXTE |

A compléter si la convention concerne une manifestation (remplace le dépôt du programme sous forme de PDF) |

CONV _ EVENEMENT _ LIEU |

Non |

Non |

Lieu

de l'événement

lié à la convention |

TEXTE |

A compléter si la convention concerne une manifestation (remplace le dépôt du programme sous forme de PDF) |

CONV _ EVENEMENT _ ORGANISATEUR |

Non |

Non |

Organisateur

de l'événement

lié à la convention |

TEXTE |

A compléter si la convention concerne une manifestation (remplace le dépôt du programme sous forme de PDF) |

AVANT _ DATE |

-Oui si le champ LIGNE _ TYPE est égal à [A]

-Non sinon (dans ce cas les lignes sont ignorées) |

Non |

Date

où l'avantage

a été accordé |

DATE |

Format JJ/ MM/ AAAA |

AVANT _ MONTANT |

Non |

Montant arrondi

à l'euro

le plus proche |

MONTANT |

|

AVANT _ NATURE |

Non |

Nature

de l'avantage

accordé |

TEXTE |

|

AVANT _ CONVENTION _ LIE |

Non |

Non |

Identifiant

de la convention

éventuellement liée à cet avantage |

TEXTE |

|

REMU _ DATE |

-Oui si le champ LIGNE _ TYPE est égal à [R]

-Non sinon (dans ce cas les lignes sont ignorées) |

Non |

Date

où la rémunération

a été versée |

DATE |

Format JJ/ MM/ AAAA |

REMU _ MONTANT |

Non |

Montant

arrondi

à l'euro

le plus proche |

MONTANT |

|

REMU _ CONVENTION _ LIEE |

Non |

Identifiant

de la convention

active liée

à cette rémunération |

TEXTE |

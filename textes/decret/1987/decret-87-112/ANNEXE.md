# Article ANNEXE

Déclaration sur bande magnétique

Le support :

- Bandes 9 pistes (standard).

- Codification EBCDIC ou ASCII.

- Sans aucun label.

- Densité : 1 600 ou 6 250 bpi.

- Facteur de blocage inférieur à 10.

- Un seul fichier physique par bande.

- Les fichiers multi-volumes sont acceptés.

Structure du fichier :

Pour chaque établissement :

1 enregistrement en tête (020).

N enregistrements détails (200).

1 enregistrement fin (300).

Plusieurs établissements possibles par bande.

Dessins des enregistrements :

Lrecl : 300.

Organisation séquentielle.

Détail des formats dans le tableau ci-après.

Déclaration sur disquette 8 pouces

Le support :

- 8 pouces au format 3740.

- Double face, double densité.

- Label raison sociale.

- Un seul fichier physique par disquette.

Structure du fichier :

Pour chaque établissement :

1 enregistrement en tête (020).

N enregistrements détails (200).

1 enregistrement fin (300).

Tous ces enregistrements sont tronçonnés en 3 secteurs de 128 octets.

Chaque enregistrement est complété à 384 par ajout de 84 blancs qui se retrouvent en fin de 3e secteur.

Plusieurs établissements possibles par disquette.

Dessins des enregistrements :

Lrecl: 384.

Organisation séquentielle.

Détail des formats dans le tableau ci-après.

Déclaration sur disquette 5 pouces 1/4

Le support :

- 5J 1/4 au format IBM/PC ou vrai compatible.

- DOS 2.1. et au-dessus.

- Densité 360 Ko ou 120 Ko.

Structure du fichier :

Pour chaque établissement :

1 enregistrement en tête (020).

N enregistrements détails (200).

1 enregistrement fin (300).

Plusieurs établissements possibles par disquettes.

Dessins des enregistrements :

Lrecl : 300.

Organisation séquentielle.

Détail des formats dans le tableau ci-après.

Codification des informations spécifiques

pour les élections prud'homales

Suffixe de l'identifiant :

Pour le cas où l'identifiant de l'entreprise est commun à plusieurs établissements, distinguez chaque établissement à l'aide de ce suffixe, en adoptant une classification numérique et/ou alphabétique.

Type d'employeur :

Blanc : Etablissement.

01 : Exploitation agricole.

02 : Particulier.

03 : Autres.

Collège électoral (pour chaque électeur) :

1 : Salariés de l'encadrement et autres salariés.

2 : Employeurs et salariés assimilés à des employeurs.

Section (pour chaque électeur) :

1 : Industrie.

2 : Commerce et services commerciaux.

3 : Agriculture.

4 : Activités diverses.

5 : Encadrement.

Lieu de vote (pour chaque électeur) :

1 : Commune de l'établissement.

2 : Commune du domicile du salarié.

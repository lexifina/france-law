# Article Annexe 1

CODAGE DES BALISES DE DÉTRESSE AÉRONAUTIQUES

1. Protocole de localisation

Dans le protocole de localisation normalisé (standard location protocol), toutes les données d'identification et de localisation sont codées en binaire, le bit de plus faible poids étant à droite.

Dans le protocole de localisation normalisé, l'identification de la balise ou de l'aéronef est codée de façon standard sur 24 bits dans la première partie du message (PDF1). Une information de position avec une résolution de 15 minutes se trouve également dans cette première partie. Une résolution plus fine (4 secondes) de la position est également codée dans la deuxième partie du message (PDF2).

Pour l'information d'identification, seuls sont autorisés le code 24 bits de l'adresse de l'aéronef ou le numéro de série de la balise (ELT ou PLB).

Lorsqu'un aéronef est doté de plusieurs balises de détresse, une seule doit comporter l'adresse 24 bits. Toutes les autres doivent être codées avec le numéro de série de la balise.

1.1. Codage du premier champ de données protégé (PDF1)

1.1.1. Avec l'adresse 24 bits de l'aéronef

BITS

|

25

|

26

|

27 À 36

|

37 À 40

|

41 À 64

|

65

|

66 À 74

|

75

|

76 À 85

|

|

1

|

0

|

Code pays

|

0011

|

Adresse 24 bits

de l'aéronef

|

Pos lat.

|

Lat.

|

Pos long.

|

Long

|

Bit 25 : 1 pour message long.

Bit 26 : 0 pour protocole de localisation.

Bits 27 à 36 : 227 pour la France métropolitaine ; 226 pour les appareils de la défense ; 329 pour la Guadeloupe ; 347 pour la Martinique ; 540 pour la Nouvelle-Calédonie ; 546 pour la Polynésie française ; 578 pour Wallis et Futuna ; 660 pour La Réunion et Mayotte ; 745 pour la Guyane française.

Bits 37 à 40 : 0011 indique qu'il s'agit d'une adresse 24 bits.

Bits 41 à 64 : adresse 24 bits de l'aéronef.

Bit 65 : 0 indique qu'il s'agit d'une latitude Nord ; 1 indique qu'il s'agit d'une latitude Sud.

Bits 66 à 74 : valeur en degrés de la latitude (de 0 à 90 par incrémentation de 1/4 de degré).

Bit 75 : 0 indique qu'il s'agit d'une longitude Est ; 1 indique qu'il s'agit d'une longitude Ouest.

Bits 76 à 85 : valeur en degrés de la longitude (de 0 à 180 par incrémentation de 1/4 de degré).

|

1.1.2. Avec le numéro de série de la balise

Bits

|

25

|

26

|

27 À 36

|

37 À 40

|

41 À 50

|

51 À 64

|

65

|

66 À 74

|

75

|

76 À 85

|

|

1

|

0

|

Code pays

|

XXXX

|

TAC

|

Numéro de série

|

Pos

lat.

|

Lat.

|

Pos long.

|

Long

|

Bit 25 : 1 pour message long.

Bit 26 : 0 pour protocole de localisation.

Bits 27 à 36 : 227 pour la France métropolitaine ; 226 pour les appareils de la défense ; 329 pour la Guadeloupe ; 347 pour la Martinique ; 540 pour la Nouvelle-Calédonie ; 546 pour la Polynésie française ; 578 pour Wallis et Futuna ; 660 pour La Réunion et Mayotte ; 745 pour la Guyane française.

Bits 37 à 40 : 0100 indique qu'il s'agit d'un ELT ; 0111 indique qu'il s'agit d'une PLB.

Bits 41 à 50 : numéro du certificat d'approbation de type COSPAS/SARSAT de la balise de détresse.

Bits 51 à 64 : numéro de série de la balise de détresse.

Bit 65 : 0 indique qu'il s'agit d'une latitude Nord ; 1 indique qu'il s'agit d'une latitude Sud.

Bits 66 à 74 : valeur en degrés de la latitude (de 0 à 90 par incrémentation de 1/4 de degré).

Bit 75 : 0 indique qu'il s'agit d'une longitude Est ; 1 indique qu'il s'agit d'une longitude Ouest.

Bits 76 à 85 : valeur en degrés de la longitude (de 0 à 180 par incrémentation de 1/4 de degré).

|

1.2. Codage du second champ de données protégé (PDF2)

Le codage de ce second champ de données protégé est identique pour tous les protocoles de localisation normalisés.

Bits

|

107 À 110

|

111

|

112

|

113

|

114 À 118

|

119 À 122

|

123

|

124 À 128

|

129 À 132

|

|

1101

|

0 ou 1

|

0 ou 1

|

Signe

|

Minutes

|

Secondes

|

Signe

|

Minutes

|

Secondes

|

Bit 107 à 110 : 1101 valeur fixe.

Bit 111 : 0 signifie que la position codée dans PDF-1 est issue d'un dispositif de navigation externe ; 1 signifie que la position codée dans PDF-1 est issue d'un dispositif de navigation interne.

Bit 112 : 0 signifie qu'il n'y a pas de transmetteur 121,5 MHz dans la balise ; 1 signifie qu'il y a un transmetteur 121,5 MHz dans la balise.

Bits 113 à 122 : présentent la correction à apporter à la latitude codée dans PDF-1, avec une précision de 4 secondes.

Bit 113 : 0 correspond au signe ― (moins) ; 1 correspond au signe + (plus).

Bits 114 à 118 : minutes (de 0 à 30 par incrémentation de 1 minute).

Bits 119 à 122 : secondes (de 0 à 56 par incrémentation de 4 secondes).

Bits 123 à 132 : présentent la correction à apporter à la longitude codée dans PDF-1, avec une précision de 4 secondes.

Bit 123 : 0 correspond au signe ― (moins) ; 1 correspond au signe + (plus).

Bits 124 à 128 : minutes (de 0 à 30 par incrémentation de 1 minute).

Bits 129 à 132 : secondes (de 0 à 56 par incrémentation de 4 secondes).

|

2. Protocole d'usager

Les protocoles d'usager, autorisés dans les conditions décrites à l'article 7, sont les protocoles utilisant l'adresse 24 bits de l'aéronef ou le numéro de série de la balise.

Dans le cas des ELT sans données de navigation, on utilise le format de message court. Dans le cas des ELT avec des données de navigation, on utilise le format de message long.

2.1. Format de message court

2.1.1. Avec l'adresse 24 bits de l'aéronef

Bits

|

25

|

26

|

27 À 36

|

37 À 39

|

40 À 42

|

43

|

44 À 67

|

68 À 73

|

74 À 83

|

84 ET 85

|

|

0

|

1

|

Code pays

|

011

|

011

|

1

|

Adresse 24 bits

de l'aéronef

|

Numéro

de l'ELT

|

TAC

|

01

|

Bit 25 : 0 pour message court.

Bit 26 : 1.

Bits 27 à 36 : 227 pour la France métropolitaine ; 226 pour les appareils de la défense ; 329 pour la Guadeloupe ; 347 pour la Martinique ; 540 pour la Nouvelle-Calédonie ; 546 pour la Polynésie française ; 578 pour Wallis et Futuna ; 660 pour La Réunion et Mayotte ; 745 pour la Guyane française.

Bits 37 à 39 : 011 indique qu'il s'agit d'un protocole de série.

Bits 40 à 42 : 011 indique qu'il s'agit d'un ELT codé avec l'adresse 24 bits de l'aéronef.

Bit 43 : 1 indique que le certificat d'approbation de type de COSPAS/SARSAT est encodé dans les bits 74 à 83.

Bits 44 à 67 : adresse 24 bits de l'aéronef.

Bits 68 à 73 : numéro de l'ELT lorsque plusieurs ELT sont à bord ; 0 s'il n'y en a qu'un.

Bit 74 à 83 : numéro du certificat d'approbation de type délivré par COSPAS/SARSAT pour ce type de balise.

Bits 84 à 85 : 01 indique la présence d'un moyen de radiolocalisation émettant sur 121,5 MHz.

|

Nota. ― Le numéro de l'ELT lorsque plusieurs ELT sont à bord (bits 68 à 73) ainsi que le numéro de certificat d'approbation de type COSPAS/SARSAT (bits 74 à 83) sont encodés en binaire, le bit de plus faible poids étant à droite.

2.1.2. Avec le numéro de série de la balise

Bits

|

25

|

26

|

27 À 36

|

37 À 39

|

40 À 42

|

43

|

44 À 63

|

64 À 73

|

74 À 83

|

84 ET 85

|

|

0

|

1

|

Code pays

|

011

|

000

|

1

|

N° de série

|

0000000000

|

TAC

|

01

|

Bit 25 : 0 pour message court.

Bit 26 : 1.

Bits 27 à 36 : 227 pour la France métropolitaine ; 226 pour les appareils de la défense ; 329 pour la Guadeloupe ; 347 pour la Martinique ; 540 pour la Nouvelle-Calédonie ; 546 pour la Polynésie française ; 578 pour Wallis et Futuna ; 660 pour La Réunion et Mayotte ; 745 pour la Guyane française.

Bits 37 à 39 : 011 indique qu'il s'agit d'un protocole de série.

Bits 40 à 42 : 000 indique qu'il s'agit d'un ELT codé avec le numéro de série de la balise.

Bit 43 : 1 indique que le certificat d'approbation de type de COSPAS/SARSAT est encodé dans les bits 74 à 83.

Bits 44 à 63 : numéro de série de l'ELT.

Bit 64 à 73 : 10 bits, tous à 0 .

Bits 74 à 83 : numéro de certificat d'approbation de type COSPAS/SARSAT.

Bits 84 à 85 : 01 indique la présence d'un appareil de radiolocalisation auxiliaire fonctionnant sur la fréquence 121,5 MHz.

|

Nota. ― Le numéro de série de la balise (bits 44 à 63) ainsi que le numéro de certificat d'approbation de type COSPAS/SARSAT (bits 74 à 83) sont encodés en binaire, le bit de plus faible poids étant à droite.

2.2. Format de message long

Lorsqu'il s'agit d'un protocole de localisation d'usager (user location protocol), la précision issue des indications fournies par un dispositif de navigation est moins précise que dans le cas d'un protocole de localisation normalisé (standard location protocol).

Dans ce cas, le champ de données protégé (PDF1) est le même que dans le cas d'un message court (paragraphe 2.1), à l'exception du bit 25 qui prend la valeur 1.

Champ de données protégé (PDF2)

Bits

|

107

|

108

|

109 À 115

|

116 À 119

|

120

|

121 À 128

|

129 À 132

|

|

Source

|

N/S

|

Degrés

|

Minutes

|

E/W

|

Degrés

|

Minutes

|

Bit 107 : 0 indique que la position est issue d'un dispositif de navigation externe ; 1 indique que la position est issue d'un dispositif de Navigation interne.

Bit 108 : 0 indique qu'il s'agit d'une latitude Nord ; 1 indique qu'il s'agit d'une latitude Sud.

Bit 109 à 115 : position en degrés (0° à 90°) par incrémentation de 1°.

Bit 116 à 119 : position en minutes (0' à 56') par incrémentation de 4'.

Bit 120 : 0 indique qu'il s'agit d'une longitude Est ; 1 indique qu'il s'agit d'une longitude Ouest.

Bits 121 à 128 : position en degrés (0° à 180°) par incrémentation de 1°.

Bits 129 à 132 : position en minutes (0' à 56') par incrémentation de 4'.

|

Nota. ― La valeur par défaut pour les bits de 108 à 119 est : 011111110000.

La valeur par défaut pour les bits de 120 à 132 est : 0111111110000.

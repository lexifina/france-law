# Article Annexe 1

I. - Critères utilisés dans la modélisation des passages des résidents dans les structures des urgences (SU)

Un modèle de " quasi-Poisson " (1) (variables en log) a été appliqué pour modéliser le nombre de passages de résidents par code géographique PMSI des communes en fonction des critères ci-dessous :

|

Variables (centrées-réduites, sauf intercept) |

Coefficients |

|

Intercept (constante) |

7,51 |

Caractéristiques de la population |

Population municipale du code géo PMSI |

0,94 |

Part de la population du code géo PMSI < 3ans |

0,06 |

Part de la population du code géo PMSI >75 ans |

0,08 |

Revenu médian pondéré du code géo PMSI |

- 0,02 |

Proportion de population non scolarisée de 15 ans et plus dont le diplôme le plus élevé est le BEPC |

0,05 |

Caractéristiques du territoire |

Proportion de la population vivant en zone de montagne |

0,03 |

Temps accès au SU plus proche |

- 0,22 |

Caractéristiques de l'offre de médecine de ville |

APL (2) médecin généraliste |

- 0,04 |

Taux de bénéficiaires de plus de 20 ans sans médecin traitant |

0,04 |

Simili APL actes SNP CCAM MG |

- 0,04 |

APL Psychiatres |

- 0,03 |

APL Masseurs-kinésithérapeutes |

- 0,06 |

Caractéristiques de l'état de santé de la population |

Taux standardisé de mortalité |

0,04 |

Taux de prévalence standardisé - Diabète |

0,04 |

Taux de prévalence standardisé - Maternité (avec ou sans pathologies) |

0,02 |

Taux de prévalence standardisé - Maladies respiratoires |

0,03 |

Taux de prévalence standardisé - Affections de longue durée (dont ALD 31 et 32) pour d'autres causes |

0,02 |

Taux de prévalence standardisé - Maladies inflammatoires ou rares ou infection VIH |

0,04 |

(1) Technique de modélisation statistique utilisée.

(2) APL : accessibilité potentielle localisée. Cet indicateur, développé par la DREES et l'IRDES, mesure l'adéquation spatiale entre l'offre et la demande de soins de premier recours.

II. - Critères utilisés dans la modélisation du nombre d'interventions primaires SMUR

Un modèle de " quasi-Poisson " (variables en log) a été appliqué pour modéliser l'activité primaire des SMUR en fonction des critères ci-dessous :

|

Variables (centrées-réduites, sauf intercept) |

Coefficients |

|

Intercept (constante) |

6,52 |

Caractéristiques de la population |

Population municipale du code géo PMSI |

0,92 |

Part de la population du code géo PMSI >75 ans |

0,10 |

Caractéristiques du territoire |

Temps accès au SMUR le plus proche |

-0,04 |

Fréquentation touristique estimée (nuitées) des codes géo PMSI " Haute Montagne " |

0,14 |

Fréquentation touristique estimée (nuitées) des codes géo PMSI " Moyenne Montagne " |

0,07 |

Fréquentation touristique estimée (nuitées) des codes géo PMSI " Autres " |

0,06 |

Caractéristiques de l'état de santé de la population |

Taux standardisé de Mortalité |

0,11 |

III. - Calcul du besoin regional SU-SMUR

Pour chaque région, le besoin est calculé comme suit

- pour les SU : par la somme du nombre de passages au sein des structures des urgences de la région, modélisés par code géographique PMSI et attribués aux établissements sièges de structures des urgences au pro-rata de la répartition observée en 2024. A cela, les passages des non-résidents par établissement siège de structures des urgences de la région sont ajoutés, y compris les patients avec un code de commune de résidence inconnu, AME-SU (ex DG) ou non assuré non pris en charge par l'AM (ex OQN), ainsi que les patients résidant à l'étranger ou à plus de 90 minutes de l'établissement où a lieu le passage ;

- pour les SMUR : par la somme de l'activité primaire modélisée attribuée aux établissements de la région sièges de SMUR au prorata de la répartition observée au sein de la région en 2023-2024 après prise en compte des effets frontières entre régions. Pour l'Ile-de-France, l'activité 2024 des ambulances de réanimation de la brigade de sapeurs-pompiers de Paris a été déduite avant répartition du besoin entre implantations SMUR. A cela, l'activité secondaire SMUR (moyenne 2023-2024) telle que disponible dans SAE-Fichsup par établissement siège de SMUR de la région est ajoutée.

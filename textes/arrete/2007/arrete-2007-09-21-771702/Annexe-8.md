# Article Annexe 8

MODULE DE RÉPARTITION DES CONSOMMATIONS PAR LOGEMENT D'UN IMMEUBLE COLLECTIF EN CAS DE CHAUFFAGE INDIVIDUEL OU INDIVIDUEL CENTRALISÉ

8.1. Chauffage

Les consommations de la synthèse d'étude thermique sont réparties à l'appartement sur la base d'une répartition simplifiée des déperditions par l'enveloppe et le renouvellement d'air comme suit.

Les déperditions par l'enveloppe de l'appartement i, Denv(i), sont évaluées par la formule :

Denv(i) = 1.8*AbaiesNord(i) + 0.9*AbaiesEstOuest(i) + 0*AbaiesSud(i) + 0.3*Aplancherhaut(i) + 0.6*Aparoiesverticales(i) + 0.15*Aplancherbas(i)

Avec :

- AbaiesNord(i), la surface de baies orientées au nord de l'appartement i (en m²) ;

- AbaiesEstOuest(i), la somme des surfaces de baies orientées à l'est et à l'ouest de l'appartement i (en m²) ;

- AbaiesSud(i), la surface de baies orientées au sud de l'appartement i (en m²) ;

- Aplancherhaut(i), la surface de plancher haut de l'appartement i, donnant sur l'extérieur ou un local non chauffé (en m²) ;

- Aparoiesverticales(i), la surface de parois verticales opaques de l'appartement i, donnant sur l'extérieur ou un local non chauffé (en m²) ;

- Aplancherbas(i), la surface de plancher bas de l'appartement i, donnant sur l'extérieur ou un local non chauffé (en m²).

Les déperditions par renouvellement d'air de l'appartement i, Dvent(i), sont évaluées par :

Dvent(i) = 0.34 * Ahabitable(i)

Avec Ahabitable(i), la surface habitable de l'appartement i (en m²).

Les déperditions totales de l'appartement i, Dtot(i), sont données par :

Dtot(i) = Denv(i) + Dvent(i)

La clé de répartition chauffage pour un appartement i, Cléch(i), a donc pour valeur :

Cléch(i) = Dtot(i) / Dtotbat

Avec Dtotbat = Σ Dtot (i), somme des déperditions de tous les appartements du bâtiment.

Si des logements ont des sources d'énergie de chauffage différentes, la clé de répartition est calculée par type d'énergie.

Cette clé de répartition s'applique à la consommation de chauffage par mètre carré de surface habitable du bâtiment, calculée selon les règles Th-C-E.

8.2. Eau chaude sanitaire

La clé de répartition est calculée en fonction des besoins d'ECS de l'appartement, calculés selon les règles Th-CE de la RT 2005.

Le besoin en eau chaude sanitaire de l'appartement i, Becs(i) est calculé comme suit :

- si Ahabitable(i) < 27 m² : Becs(i) = 470.9*ln (Ahabitable(i)) - 1075) (en kWh), (1)

- Becs(i) = 17.7*Ahabitable(i) (en kWh) sinon.

La clé de répartition des besoins d'eau chaude sanitaire pour un appartement i, Cléecs(i), est donnée par :

Cléecs(i) = Becs(i) / Becsbat

Avec Becsbat = Σ Becs(i), somme des besoins d'ECS de tous les appartements du bâtiment.

Si des logements ont des sources d'énergie différentes pour la production d'ECS, la clé de répartition est calculée par type d'énergie.

Cette clé de répartition s'applique à la consommation d'eau chaude sanitaire par mètre carré de surface habitable du bâtiment, calculée selon les règles Th-C-E.

8.3. Refroidissement

Les consommations de refroidissement par mètre carré de surface habitable seront prises égales à celles de la partie refroidie du bâtiment.

NOTA :

(1) Il convient de lire - si Ahabitable(i) > 27 m² : Becs(i) = 470.9*ln (Ahabitable(i)) - 1075 (en kWh).

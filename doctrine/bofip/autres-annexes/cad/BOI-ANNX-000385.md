# ANNEXE - CAD - Trajectographie

- Identifiant : BOI-ANNX-000385-20130617
- Publié le : 2013-06-17
- Type : Autres annexes
- Série : CAD, CAD
- Bureau : DGFIP
- Page officielle : https://bofip.impots.gouv.fr/bofip/5223-PGP.html/identifiant=BOI-ANNX-000385-20130617
- Directeur de publication : Bruno Bézard, directeur général des finances publiques
- Références : Image:5222-PGP

## Texte

ANNEXE - CAD - Trajectographie

1

Un avion évolue selon trois axes. Ces axes sont appelés en aviation roulis (roll), tangage
(pitch), lacet (yaw). En photogrammétrie ces trois axes sont dénommés par les lettres grecs (ω,φ,k)

10

En vol, les informations suivantes sont enregistrées :

- les données GPS avec une fréquence de 1 Hz (toutes les 1 secondes) ;

- les tops caméra en temps GPS ;

- les données inertielles (accélérations instantanées et angles d’attitude) avec une fréquence
de 256 Hz dans un système local orienté suivant le nord géographique.

Au sol, le post-traitement des données suivant est réalisé :

- calcul des centres de phases de l’antenne GPS à une fréquence de 1 Hz, soit pour un avion
volant à 100 m/s (360 km/h) un point tous les 100 mètres ;

- utilisation des données de l’IMU à 256 Hz pour calculer un points tous les 40 cm par double
intégration des accélérations instantanées mesurées par la centrale à inertie (IMU) ;

- application des offsets antenne IMU + IMU caméra pour avoir la trajectographie à 256 Hz au
niveau des CP de la caméra ;

- interpolation de la position définitive du CP à l’aide du top caméra sur un segment de 40 cm
;

- correction des angles d’attitude de la centrale à inertie c’est à dire calcul de l’angle
entre le système IMU(Row, Pitch, Yaw) orienté au nord géographique et le système caméra (Omega, Phi, Kappa) orienté suivant l’axe des Y de la projection utilisée, donc en utilisant la formule de
convergence des méridiens de la projection.

# CAD - Mise à jour du plan - Application d'un document d'arpentage au fichier immobilier et dans la documentation cadastrale - Archivage

- Identifiant : BOI-CAD-MAJ-10-40-20210512
- Publié le : 2021-05-12
- Type : Commentaire
- Série : CAD, MAJ
- Bureau : GF3A
- Page officielle : https://bofip.impots.gouv.fr/bofip/5259-PGP.html/identifiant=BOI-CAD-MAJ-10-40-20210512
- Directeur de publication : Jérôme Fournel, directeur général des finances publiques

## Texte

CAD - Mise à jour du plan - Application d'un document d'arpentage au fichier immobilier et dans la documentation cadastrale - Archivage

## I. Application dans la documentation littérale



### A. Publication au service de la publicité foncière et incidences dans la documentation cadastrale


1


La réforme de la publicité foncière de 1955, entrée en vigueur le 1er janvier 1956, a instauré une liaison étroite entre les services de la publicité foncière et le cadastre. En effet, l’identification des biens publiés au fichier immobilier doit être effectuée par référence au cadastre rénové, selon les dispositions de l’article 870 du code général des impôts (CGI).


Par ailleurs l'article 1402 du CGI stipule que les mutations cadastrales ne peuvent être effectuées qu’après publication au fichier immobilier de l’acte ou de la décision judiciaire constatant cette mutation. Ce principe de concordances des fichiers immobiliers et la documentation cadastrale est confirmé par les dispositions de l'article 2 du décret n° 55-22 du 4 janvier 1955 portant réforme de la publicité foncière et de l'article 17 du décret n° 55-1350 du 14 octobre 1955.



#### 1. Liaison FIDJI - BNDP


10


Lors de la publication d’un document d’arpentage au service de la publicité foncière, les données sont saisies dans l’application informatique FIDJI (fichier informatisé de la documentation juridique sur les immeubles). Ces informations concernent notamment :


- l’identification du document, la date de signature et la date de publication ;


- le type de changement occasionné (changement de consistance, de désignation) ;


- les références cadastrales des parcelles concernées par le document d’arpentage.


Les informations saisies dans FIDJI sont ensuite transmises et intégrées dans la BNDP (base nationale de données patrimoniales).



#### 2. Liaison BNDP - MAJIC


20


Des flux hebdomadaires existent entre les applications BNDP et MAJIC (application de mise à jour des informations cadastrales). Ces échanges d'informations concernent notamment les immeubles, les adresses des personnes et les documents de filiation.


La liaison automatique BNDP - MAJIC a pour effet de valider automatiquement dans MAJIC les documents de filiation publiés au service de la publicité foncière. On regroupe sous le terme document de filiation :


- les documents d’arpentage établis par les personnes agréées ;


- les croquis de conservation fonciers établis par le service du cadastre.


Un document de filiation n’est validé que lorsque les contrôles sur tous les lots d’analyse (parcelles mères actives, titulaires de droits, natures des droits exercés sur les parcelles concernées, etc) sont corrects. Dans le cas contraire, l'échec de la liaison est inscrit dans les listes d'anomalies, exploitées par le service du cadastre.



#### 3. Traitement des échecs de liaisons


30


Les échecs de la liaison automatique FIDJI - BNDP - MAJIC figurent dans le compte-rendu des mises à jour automatiques non réalisées ou à expertiser.


Les documents de filiation mentionnés dans ce compte-rendu doivent faire l’objet d’une exploitation manuelle dans MAJIC.


Il s’agira alors de valider le document en attribuant définitivement les numéros parcellaires dans l'application MAJIC.


Remarque : Les documents de filiation partiellement publiés engendrent systématiquement un échec dans la liaison BNDP – MAJIC .



#### 4. Conséquences de la validation d’un document de filiation


40


Suite à la validation du document de filiation, automatique ou manuelle, une tâche différée, dite de répercussion automatique, est déclenchée. Dans ce cas :


- les parcelles nouvelles (ou parcelles « filles ») deviennent actives ; dans le cas particulier du passage au domaine public, celui-ci devient alors définitif ;


- les parcelles anciennes (ou « parcelles « mères ») sont annulées.



### B. Mise au point fiscale


50


La mise au point fiscale des nouvelles parcelles actives est réalisée afin d’établir la base de la taxe foncière sur les propriétés non bâties.


La liaison automatique BNDP - MAJIC assure une partie de la mise au point fiscale des nouvelles parcelles. Elle permet d’une part, de répercuter automatiquement les natures de culture de la ou des parcelles mères sur la ou les parcelles filles et d’autre part, de placer les éléments bâtis sur la parcelle fille de plus petit numéro.


Il s’agira alors, depuis le bureau, de s’assurer que le bâti est placé sur la bonne parcelle et que les natures de culture attribuées automatiquement sont cohérentes et représentatives.


60


En cas d'incohérence ou d'échec dans le processus automatique, la mise au point fiscale est réalisée par le service du cadastre. Une mise au point fiscale plus précise pourra être effectuée lors de la tournée en commune du géomètre-cadastreur. Il modifiera éventuellement les natures de culture attribuées automatiquement ou depuis le bureau, et aura la possibilité de créer des subdivisions fiscales représentées ou non au plan.



## II. Application dans la documentation graphique



### A. Incorporation d’un document d’arpentage dans PCI


70


Le document d'arpentage publié et validé est appliqué dans la documentation graphique. Il s'agit d'incorporer dans la documentation graphique existante la modification demandée par le document d'arpentage en prenant en compte les limites nouvelles, les signes de mitoyenneté, les bornes le cas échéant, les nouveaux numéros des parcelles résultant de la modification.


Remarque : En l'absence d'une délimitation contradictoire et d'un procès-verbal de bornage, la simple matérialisation d'une opération foncière par l'implantation de repères durables (bornes, poteaux, pierres, etc.) ne constitue pas un bornage. Dès lors, les repères durables tels que matérialisés sur le terrain et représentés sur le fond de plan ne sont en aucun cas reconduits dans la documentation cadastrale.


80


Lors de l'incorporation, deux cas peuvent se présenter :


- le document a été vérifié et appliqué provisoirement dans PCI (qu'il soit numérique ou « papier ») : il s'agit alors de le sélectionner par son numéro d'ordre et de l'appliquer de façon définitive au plan cadastral après s'être assuré de la correcte implantation des parcelles-filles ;


- le document n'a pas été vérifié dans PCI ou y a été supprimé : le document de mise à jour est alors créé, en rappelant le numéro d'ordre du document d'arpentage. Les lots d'analyse sont appliqués et les nouvelles parcelles numérotées. Le document d'arpentage est alors incorporé de façon définitive au plan cadastral.


90


Le flux d'échange de données de MAJIC vers PCI apporte une partie des informations relatives aux lots d'analyse des documents de filiations informatisés : numéro du document, validation, contenances cadastrales, arpentage.



### B. Incidences de MAJIC dans PCI


100


Certaines données littérales, saisies dans MAJIC, sont répercutées automatiquement dans les applications PCI image et PCI vecteur pour permettre la consultation simultanée de la documentation graphique et littérale Les répercutions, qui interviennent deux jours après la validation dans MAJIC, concernent en particulier :


- les changements relatifs aux personnes et à l’attribution ;


- les changements relatifs aux propriétés non bâties (descriptif et adresse de la parcelle) .



## III. Archivage


110


Tous les documents d’arpentage sont conservés au service du cadastre de façon permanente, sous forme papier ou numérique.


Dans le cadre de documents d'arpentage numériques entièrement dématérialisés, les documents originaux portant la signature du géomètre agréé et des parties (chemise, extrait de plan et mandats éventuels) seront conservés par le rédacteur du document et communiqués, sur demande, au service du cadastre.


120


Par ailleurs, par une décision du 12 juillet 1995 (CE, 12 juillet 1995, n°119734), le Conseil d'État a consacré l’existence d’un régime spécifique de communication des documents cadastraux dérogatoire à la loi n° 78-753 du 17 juillet 1978 portant diverses mesures d'amélioration des relations entre l'administration et le public et diverses dispositions d'ordre administratif, social et fiscal relative à l’accès aux documents administratifs.


Dès lors, les services du cadastre doivent délivrer une copie des documents d'arpentage et des documents annexés (par exemple : les fonds de plan, les plans d'arpentage ou de bornage, les éléments du levé, les pouvoirs éventuels ) y compris les données numériques (à savoir le fichier au format DA numérique, le fichier « terrain » contenant les points nouveaux en « coordonnées de terrain » si le géomètre a effectué un levé en coordonnées, le fichier contenant le rapport de la transformation pratiquée si le géomètre a effectué une transformation sur le levé en coordonnées), à toute personne qui en fait la demande (professionnels et usagers), sans autorisation écrite préalable de son auteur.

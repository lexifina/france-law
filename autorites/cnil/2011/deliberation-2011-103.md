# Délibération n°2011-103 du 14 avril 2011 autorisant la mise en œuvre par le Crédit Mutuel ARKEA d’un traitement automatisé de données à caractère personnel ayant pour finalité la lutte contre la fraude à la carte bancaire

- Nature : Deliberation
- Type : Autre autorisation
- Numéro : 2011-103
- Date : 2011-04-14
- Publication : 2019-11-13
- État : VIGUEUR
- Légifrance : https://www.legifrance.gouv.fr/cnil/id/CNILTEXT000023976301

(demande d’autorisation n°1339419)

La Commission nationale de l’informatique et des libertés,

Vu la Convention n° 108 du Conseil de l’Europe pour la protection des personnes à l’égard du traitement automatisé des données à caractère personnel ;

Vu la directive 95/46/CE du Parlement européen et du Conseil du 24 octobre 1995 relative à la protection des personnes physiques à l’égard du traitement de données à caractère personnel et à la libre circulation de ces données ;

Vu la loi n° 78-17 du 6 janvier 1978 relative à l'informatique, aux fichiers et aux libertés, modifiée en 2004, notamment son article 25-I-4° ;

Vu le décret n° 2005-1309 du 20 octobre 2005 pris pour l’application de la loi n° 78-17 du 6 janvier 1978 relative à l’informatique, aux fichiers et aux libertés, modifié par le décret n°2007-451 du 25 mars 2007 ;

Vu la demande d’autorisation présentée par le Crédit Mutuel ARKEA relative à un traitement automatisé de données à caractère personnel ayant pour finalité la détection de fraude à la carte bancaire ;

Sur le rapport de Monsieur Jean Paul AMOUDRY, commissaire, et les observations de Madame Elisabeth ROLIN, commissaire du Gouvernement ;

Formule les observations suivantes :

Le Crédit Mutuel ARKEA a saisi la Commission nationale de l’informatique et des libertés d’un projet de traitement de données à caractère personnel dont la finalité est de détecter des suspicions de fraude à la carte bancaire.

Sur la procédure suivie auprès de la Commission

La Commission observe que le traitement a pour objet d’identifier des opérations réalisées par carte Mastercard susceptibles d’être constitutives d’une fraude. Dès lors, ce traitement peut avoir pour effet d’empêcher, même temporairement, le porteur de faire usage de son moyen de paiement.

Il en résulte que le traitement mis en œuvre peut avoir pour effet d’exclure des personnes du bénéfice d’une prestation, l’utilisation d’une carte bancaire, en l’absence de toute disposition législative ou réglementaire le prévoyant. Dès lors il relève du 4° de l’article 25 de la loi du 6 janvier 1978 modifiée et doit à ce titre être autorisé par la CNIL.

Sur les finalités et les caractéristiques du traitement

Le traitement vise à émettre des alertes en temps réel sur la base d’une analyse des transactions effectuées par les porteurs de cartes Mastercard. Celui-ci permet de détecter d’éventuelles opérations frauduleuses et d’en limiter les conséquences dommageables en permettant l’adoption de mesures adaptées, en l’occurrence un refus d’autorisation.

La Commission observe que les fraudes recherchées correspondent à des utilisations illégitimes d’une carte de paiement ou des données qui y sont attachées, lorsque ces utilisations risquent d’avoir des conséquences préjudiciables pour le porteur de la carte ou son établissement bancaire. Les utilisations d’une carte par son porteur légitime qui sont rendues irrégulières du seul fait d’un défaut de provision ne font pas partie des risques de fraude qui donnent lieu à la production d’alerte.

Les critères pris en compte pour la production des alertes sont :

la typologie de la transaction,

la typologie du commerçant,

le montant de la transaction,

le montant cumulé des transactions précédentes,

le nombre de transactions réalisées par le porteur dans ce type de commerce,

le lieu géographique de réalisation de la transaction.

L’ensemble de ces informations peuvent être analysées sur une période de 7 jours.

A chaque transaction, un niveau de risque global sous la forme d’une note de score est calculé sur la base de ces critères.

En cas de transaction identifiée comme susceptible de constituer une fraude, celle-ci fait l’objet d’un refus d’autorisation, elle est alors bloquée et une alerte est transmise au personnel du Back office fraude du Crédit Mutuel ARKEA.

Le traitement permet d’établir un modèle des risques d’utilisation frauduleuse élaboré sur la base d’un traitement statistique de l’historique des transactions réalisées par carte bancaire puis de l’appliquer lors du traitement des demandes d’autorisations transmises à la banque en cas de paiement réalisé auprès d’un commerçant acquéreur via un terminal de paiement électronique, lors d’un retrait effectué auprès d’un distributeur automatique ou en cas d’opérations de paiement en ligne.

La Commission constate que ce traitement n’a pas pour objet d’identifier des commerçants ou des terminaux de paiements auxquels correspondent un taux significatif d’utilisations frauduleuses ou de tentatives d’utilisations frauduleuses.

La Commission observe que le traitement de détection des alertes ne permet pas d’établir une liste des alertes générées pour une même carte bancaire ou un même compte.

La Commission remarque qu’en cas de refus d’autorisation, le personnel du Back office Fraude du Crédit Mutuel ARKEA transmet l’alerte au chargé de clientèle du porteur qui tente d’entrer en contact téléphonique avec ce dernier pour vérifier si celui-ci est à l’origine de la transaction ayant fait l’objet d’un refus d’autorisation. Lorsque le porteur confirme qu’il est à l’origine de la transaction, la carte sera débloquée pour les transactions futures.

La Commission constate que le personnel du Back office Fraude du Crédit Mutuel ARKEA n’est pas habilité à procéder de sa propre initiative, au blocage du moyen de paiement. En cas d’indices de fraude jugée élevée ou en présence de plusieurs alertes, il peut décider d’appliquer à la carte bancaire une restriction temporaire de fonctionnement.

La Commission observe que ce traitement ne peut donner lieu au blocage complet du moyen de paiement sans avoir au préalable obtenu le consentement du porteur.

La Commission insiste par ailleurs sur la nécessité de paramétrer le traitement automatisé en fonction d’un niveau de risque jugé acceptable par le responsable de traitement afin de ne pas multiplier inutilement le nombre de fausses alertes susceptibles de provoquer une gêne excessive pour les porteurs légitimes de cartes.

Sur les données traitées et la durée de conservation :

Les catégories de données traitées pour la production des alertes sont :

les informations relatives à la transaction (typologie, montant, montants cumulés des transactions précédentes, lieu géographique)

le type de commerce et le nombre de transactions réalisées par le porteur dans ce type de commerce.

Les catégories de données traitées par le Back office Fraude pour la gestion des alertes :

le numéro de la carte Mastercard et

le résultat du score.

Les alertes sont conservées pendant une durée de 5 jours. Ces données sont ensuite anonymisées afin de procéder à l’actualisation du modèle d’analyse.

La Commission considère que les données traitées sont adéquates, pertinentes et non excessives au regard de la finalité poursuivie.

Sur les destinataires du traitement

Seuls ont accès au traitement de gestion des alertes : le personnel du Back office Fraude du Crédit Mutuel ARKEA.

Les chargés de clientèle peuvent également avoir connaissance des alertes pour les seules transactions intéressant leurs clients.

Sur les modalités d’information et d’exercice des droits des personnes physiques

Les personnes concernées sont informées de la mise en œuvre de ce traitement lors de la signature du contrat porteur.

Elles peuvent exercer leur droit d’accès conformément aux dispositions de l’article 39 de la loi n°78-17 du 6 janvier 1978 modifiée en 2004.

Dans ces conditions, la Commission autorise, le Crédit Mutuel ARKEA à mettre en œuvre un traitement automatisé de données à caractère personnel ayant pour finalité la lutte contre la fraude à la carte bancaire.

Le Président

Alex TURK

# Article Annexe

DONNÉES

|

VARIABLES

|

Tarifs des séjours GHS.

|

GHS

|

Forfait journalier FJ.

|

FJ

|

Durée de séjour DS.

|

DS

|

Taux de remboursement TR.

|

TR

|

Taux de ticket modérateur TM.

|

= 1 ― TR

|

Ticket modérateur forfaitaire 18 €.

|

18 €

|

Coefficient géographique CG.

|

CG

|

Coefficient de transition CT.

|

CT

|

Modalités de détermination de la part payée par l'assurance maladie selon le cas

CAS DE PATIENT AVEC UN TICKET MODÉRATEUR À 20 %

|

Ticket modérateur M_TM.

|

M_TM = (GHS × CG × CT) × TM

|

Forfait journalier M_FJ.

|

M_FJ = (FJ × DS) + FJ (1)

|

Montant payé par l'assurance maladie AMO

|

Si M_TM ¸ M_FJ.

|

M_AMO = (GHS × CG × CT) × TR―(M_FJ-M_TM)

|

Si M_TM ¹ M_FJ.

|

M_AMO = (GHS × CG × CT × TR)

|

CAS DE PATIENT EXONÉRÉ DU TM ET NON EXONÉRÉ DU FORFAIT JOURNALIER

|

Ticket modérateur M_TM.

|

0

|

Forfait journalier M_FJ.

|

M_FJ = (FJ × DS) + FJ

|

Montant payé par l'assurance maladie AMO.

|

M_AMO = (GHS × CG × CT) ― ((FJ × DS) + FJ)

|

CAS DE PATIENT EXONÉRÉ DU TM ET DU FORFAIT JOURNALIER

|

Ticket modérateur M_TM.

|

0

|

Forfait journalier M_FJ.

|

0

|

Montant payé par l'assurance maladie AMO.

|

M_AMO = GHS × CG × CT

|

CAS DE PATIENT PRIS EN CHARGE À 100 %, SOUMIS AU TM DE 18 € ET NON EXONÉRÉ DU FORFAIT JOURNALIER

|

Ticket modérateur M_TM.

|

18 €

|

Forfait journalier M_FJ.

|

M_FJ = (FJ × DS) + FJ

|

Montant payé par l'assurance maladie AMO.

|

M_AMO = (GHS × CG × CT) ― ((FJ × DS) + FJ) ― 18

|

CAS DE PATIENT PRIS EN CHARGE À 100 %, SOUMIS AU TM DE 18 € ET EXONÉRÉ DU FORFAIT JOURNALIER

|

Ticket modérateur M_TM.

|

18 €

|

Forfait journalier M_FJ.

|

0

|

Montant payé par l'assurance maladie AMO.

|

M_AMO = (GHS × CG × CT) ― 18

|

(1) Le patient acquitte le forfait journalier le jour de sortie.

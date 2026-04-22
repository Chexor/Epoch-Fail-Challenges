---
type: theory
domain: "linear-algebra"
parent: "Matrix Structures"
related:
  - Matrix Structures
  - Eenheidsmatrix
  - Matrixvermenigvuldiging
theme: "matrix-reasoning"
aliases:
  - Matrix Notatie en Dimensies
---

# Matrix Notatie en Dimensies
#concept #linal

## 1. Wat is het kernprobleem?
Hoe noteer je matrices correct en hoe weet je welke bewerkingen wel of niet mogelijk zijn?

## 2. Intuitieve uitleg
Een matrix is een rooster van getallen met rijen en kolommen. De dimensie vertelt je hoe groot dat rooster is, bijvoorbeeld `2 x 3` voor 2 rijen en 3 kolommen.

## 3. Formele structuur
- een matrix met `m` rijen en `n` kolommen heeft dimensie `m x n`
- elementen noteer je vaak als `a_ij`, met `i` voor de rij en `j` voor de kolom
- dimensies bepalen of optellen, vermenigvuldigen en inverteren mogelijk zijn

## 4. Toepassing
Als matrix `A` dimensie `2 x 3` heeft en matrix `B` dimensie `3 x 4`, dan kan `A * B` wel bestaan, maar `B * A` niet noodzakelijk.

## 5. Examengerichte vertaling
- **Typische vraag:** Bepaal de dimensie van deze matrix en zeg welke bewerkingen mogelijk zijn.
- **Vaak gemaakte fout:** rijen en kolommen omwisselen of een matrixproduct proberen zonder dimensies te controleren.
- **Link met andere concepten:** [[Matrixvermenigvuldiging]], [[Eenheidsmatrix]]

## Context in het domein
- Overzicht: [[00_Overzicht Linear Algebra]]
- Toepassing: [[Matrixvermenigvuldiging]]

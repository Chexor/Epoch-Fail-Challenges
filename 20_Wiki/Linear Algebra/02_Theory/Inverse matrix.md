---
type: theory
domain: "linear-algebra"
parent: "Matrix Invertibility"
related:
  - Matrix Invertibility
  - Determinant: Betekenis en Berekening
  - Gauss-Jordan eliminatie (rref)
theme: "matrix-invertibility"
aliases:
  - Inverse Matrix
---

# Inverse Matrix
#concept #linal

## 1. Wat is het kernprobleem?
Hoe maak je een matrixbewerking ongedaan, zoals je bij getallen deelt om een vermenigvuldiging terug te draaien?

## 2. Intuitieve uitleg
De inverse van een matrix is de matrix die een transformatie terugdraait. Als `A` iets vervormt, dan probeert `A^-1` die vervorming ongedaan te maken.

## 3. Formele structuur
- Een matrix `A` is inverteerbaar als er een matrix `A^-1` bestaat waarvoor `A * A^-1 = I`
- Alleen vierkante matrices kunnen een inverse hebben
- Een inverse bestaat enkel als `det(A) != 0`

## 4. Toepassing
Bij het oplossen van `Ax = b` kun je, als `A` inverteerbaar is, schrijven:
- `x = A^-1 b`

Dat maakt de inverse belangrijk voor lineaire stelsels en matrixtransformaties.

## 5. Examengerichte vertaling
- **Typische vraag:** Wanneer bestaat de inverse van een matrix?
- **Vaak gemaakte fout:** Denken dat elke vierkante matrix automatisch een inverse heeft.
- **Link met andere concepten:** [[Determinant - Betekenis en Berekening]], [[Eenheidsmatrix]], [[Gauss-Jordan eliminatie (rref)]]

## Context in het domein
- Overzicht: [[00_Overzicht Linear Algebra]]
- Vergelijking: [[Singulier vs Inverteerbaar]]
- Uitwerking: [[Gauss-Jordan Worked Example]]

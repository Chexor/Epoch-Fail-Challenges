---
type: theory
domain: "linear-algebra"
parent: "Matrix Invertibility"
related:
  - Matrix Invertibility
  - Inverse Matrix
  - Singulier vs Inverteerbaar
theme: "matrix-reasoning"
aliases:
  - Determinant: Betekenis en Berekening
---

# Determinant: Betekenis en Berekening
#concept #linal

## 1. Wat is het kernprobleem?
Hoe kunnen we met een getal bepalen of een vierkante matrix informatie verliest of omkeerbaar blijft? Dat getal is de determinant.

## 2. Intuitieve uitleg
De determinant is de schaalfactor van oppervlakte of volume wanneer een matrix een vorm transformeert.

- `det(A) = 3`: de oppervlakte wordt drie keer zo groot
- `det(A) = 0`: de vorm wordt platgedrukt naar een lagere dimensie en de matrix is niet omkeerbaar
- `det(A) < 0`: de schaal verandert en de oriëntatie spiegelt mee

Kernidee: `det(A) != 0` betekent dat de matrix inverteerbaar is. `det(A) = 0` betekent dat ze singulier is.

## 3. Formele structuur

### Berekening (2x2)
Voor `A = [[a, b], [c, d]]` geldt:
- `det(A) = ad - bc`

### Berekening (3x3)
Voor 3x3-matrices gebruik je vaak de regel van Sarrus als visuele rekentechniek.

### Belangrijkste eigenschap
Een matrix `A` heeft een inverse als en slechts als `det(A) != 0`.

## 4. Toepassing
Voor welke waarde van `p` is `A = [[1, 2], [p, 4]]` singulier?

1. Stel de determinant op: `det(A) = (1 * 4) - (2 * p) = 4 - 2p`
2. Stel gelijk aan nul: `4 - 2p = 0`
3. Los op: `2p = 4`, dus `p = 2`

Conclusie: voor `p = 2` is de matrix singulier.

## 5. Examengerichte vertaling
- **Typische vraag:** Voor welke waarde van een parameter is deze matrix niet-inverteerbaar?
- **Vaak gemaakte fout:** mintekens vergeten in de determinantformule of regel van Sarrus.
- **Link met andere concepten:** [[Inverse matrix]], [[Singulier vs Inverteerbaar]], [[Gauss-Jordan eliminatie (rref)]]
- **Software:** Gebruik in `wxMaxima` het commando `determinant(A);` om snel te controleren.

## Context in het domein
- Overzicht: [[00_Overzicht Linear Algebra]]
- Vergelijking: [[Singulier vs Inverteerbaar]]

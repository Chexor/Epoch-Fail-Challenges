---
type: concept-topic
domain: "linear-algebra"
parent: "Matrix Transformations and Reduction"
related:
  - Matrix Transformations and Reduction
  - Gauss-Jordan Worked Example
  - Inverse Matrix
theme: "row-reduction"
aliases:
  - Gauss-Jordan Eliminatie (rref)
---

# Gauss-Jordan Eliminatie (rref)
#concept #linal

## 1. Wat is het kernprobleem?
Hoe vereenvoudig je een matrix systematisch zodat de oplossingstructuur van een stelsel of de inverse van een matrix zichtbaar wordt?

## 2. Intuitieve uitleg
Gauss-Jordan eliminatie is een gecontroleerde schoonmaakoperatie op rijen. Je herschrijft de matrix stap voor stap tot de belangrijke structuur meteen afleesbaar is.

## 3. Formele structuur
- doelvorm: reduced row echelon form (`rref`)
- toegelaten bewerkingen:
  - rijen wisselen
  - een rij vermenigvuldigen met een niet-nul getal
  - een veelvoud van een rij optellen bij een andere rij

## 4. Toepassing
Met Gauss-Jordan kun je:
- lineaire stelsels oplossen
- rang bepalen
- controleren of een matrix inverteerbaar is
- een inverse berekenen via een geaugmenteerde matrix

## 5. Examengerichte vertaling
- **Typische vraag:** Breng deze matrix naar rref en interpreteer het resultaat.
- **Vaak gemaakte fout:** rijoperaties uitvoeren zonder duidelijke pivotstrategie.
- **Link met andere concepten:** [[Inverse matrix]], [[Eenheidsmatrix]], [[Singulier vs Inverteerbaar]]

## Context in het domein
- Overzicht: [[00_Overzicht Linear Algebra]]
- Uitwerking: [[Gauss-Jordan Worked Example]]

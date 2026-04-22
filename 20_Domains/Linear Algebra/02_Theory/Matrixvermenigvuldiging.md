---
type: theory
domain: "linear-algebra"
parent: "Matrix Structures"
related:
  - Matrix Structures
  - Matrix notatie en dimensies
  - Eenheidsmatrix
theme: "matrix-reasoning"
aliases:
  - Matrixvermenigvuldiging
---

# Matrixvermenigvuldiging
#concept #linal

## 1. Wat is het kernprobleem?
Hoe combineer je twee matrices op een manier die lineaire transformaties en stelsels correct samenvoegt?

## 2. Intuitieve uitleg
Matrixvermenigvuldiging is geen gewone element-per-element vermenigvuldiging. Je combineert rijen van de eerste matrix met kolommen van de tweede om te berekenen hoe twee lineaire processen samen werken.

## 3. Formele structuur
- `A * B` bestaat alleen als het aantal kolommen van `A` gelijk is aan het aantal rijen van `B`
- het element op positie `(i, j)` is het dot product van rij `i` van `A` met kolom `j` van `B`
- matrixvermenigvuldiging is in het algemeen niet commutatief

## 4. Toepassing
Als `A` een eerste transformatie voorstelt en `B` een tweede, dan stelt `A * B` de samengestelde transformatie voor.

## 5. Examengerichte vertaling
- **Typische vraag:** Kan je deze twee matrices vermenigvuldigen en wat is het resultaat?
- **Vaak gemaakte fout:** dimensies niet eerst controleren of denken dat `A * B = B * A`.
- **Link met andere concepten:** [[Matrix notatie en dimensies]], [[Dot Product]], [[Eenheidsmatrix]]

## Context in het domein
- Overzicht: [[00_Overzicht Linear Algebra]]
- Voorwaarde: [[Matrix notatie en dimensies]]

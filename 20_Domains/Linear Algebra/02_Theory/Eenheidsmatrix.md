---
type: theory
domain: "linear-algebra"
parent: "Matrix Structures"
related:
  - Matrix Structures
  - Matrix notatie en dimensies
  - Matrixvermenigvuldiging
theme: "matrix-reasoning"
aliases:
  - Eenheidsmatrix
---

# Eenheidsmatrix
#concept #linal

## 1. Wat is het kernprobleem?
Welke matrix gedraagt zich bij vermenigvuldiging zoals het getal 1 dat doet bij gewone getallen?

## 2. Intuitieve uitleg
De eenheidsmatrix is de “neutrale matrix”. Als je een matrix ermee vermenigvuldigt, blijft die matrix hetzelfde, zolang de dimensies passen.

## 3. Formele structuur
- de eenheidsmatrix noteer je als `I`
- op de hoofddiagonaal staan enen, elders nullen
- voor een matrix `A` geldt: `A * I = A` en `I * A = A` wanneer de dimensies compatibel zijn

## 4. Toepassing
De eenheidsmatrix speelt een centrale rol bij:
- het herkennen van inverse matrices
- Gauss-Jordan eliminatie
- het noteren van neutrale transformaties

## 5. Examengerichte vertaling
- **Typische vraag:** Waarom is de eenheidsmatrix belangrijk bij het berekenen van een inverse?
- **Vaak gemaakte fout:** denken dat er maar één universele eenheidsmatrix bestaat, los van dimensie.
- **Link met andere concepten:** [[Inverse matrix]], [[Matrixvermenigvuldiging]], [[Gauss-Jordan eliminatie (rref)]]

## Context in het domein
- Overzicht: [[00_Overzicht Linear Algebra]]
- Uitwerking: [[Gauss-Jordan Worked Example]]

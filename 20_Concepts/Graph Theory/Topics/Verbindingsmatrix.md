---
type: concept-topic
domain: "graph-theory"
parent: "Graph Representation"
related:
  - Graph Representation
  - Graaf
  - Padlengte via Matrixmachten
  - Graph Matrix Methods
theme: "graph-representation"
aliases:
  - Verbindingsmatrix
---

# Verbindingsmatrix
#concept #grafen

## 1. Wat is het kernprobleem?
Hoe vertaal je een visuele graaf naar een wiskundige vorm waarop je berekeningen kunt uitvoeren?

## 2. Intuïtieve uitleg
De verbindingsmatrix is de tabelversie van een graaf. Ze registreert welke knopen rechtstreeks met elkaar verbonden zijn.

## 3. Formele structuur
- voor een graaf met `n` knopen is de verbindingsmatrix een `n x n`-matrix
- element `A_ij` geeft het aantal directe verbindingen van knoop `i` naar knoop `j`
- bij een niet-gerichte graaf is de matrix symmetrisch

## 4. Toepassing
Als `A_13 = 1`, dan is er een directe verbinding van knoop 1 naar knoop 3. Met deze matrix kun je daarna ook machten berekenen om paden te tellen.

## 5. Examengerichte vertaling
- **Typische vraag:** Stel de verbindingsmatrix op van deze graaf of reconstrueer de graaf vanuit de matrix.
- **Vaak gemaakte fout:** knoopvolgorde niet consistent houden of richting vergeten meenemen.
- **Link met andere concepten:** [[Graaf]], [[Gerichte vs Niet-gerichte Graaf]], [[Padlengte via Matrixmachten]]

## Context in het domein
- Overzicht: [[00_Overzicht Graph Theory]]
- Uitwerking: [[Paden Tellen met A^k Worked Example]]

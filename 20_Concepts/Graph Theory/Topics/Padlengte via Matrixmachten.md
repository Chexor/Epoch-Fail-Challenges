---
type: concept-topic
domain: "graph-theory"
parent: "Graph Matrix Methods"
related:
  - Graph Matrix Methods
  - Verbindingsmatrix
  - Paden Tellen met A^k Worked Example
theme: "path-counting"
aliases:
  - Padlengte via Matrixmachten
---

# Padlengte via Matrixmachten
#concept #grafen

## 1. Wat is het kernprobleem?
Hoe bepaal je systematisch hoeveel manieren er zijn om in exact `k` stappen van de ene knoop naar de andere te gaan?

## 2. Intuïtieve uitleg
De kracht van grafentheorie zit erin dat een netwerkprobleem kan veranderen in een matrixprobleem. Door de verbindingsmatrix tot een macht te verheffen, lees je het aantal paden van een bepaalde lengte rechtstreeks af.

## 3. Formele structuur
- als `A` de verbindingsmatrix is, dan geeft `(A^k)_ij` het aantal paden van lengte `k` van knoop `i` naar knoop `j`
- `A^2` telt paden met lengte 2
- `A^3` telt paden met lengte 3

## 4. Toepassing
Wil je weten hoeveel manieren er zijn om in 3 stappen van knoop A naar knoop B te gaan, dan bereken je `A^3` en lees je het juiste element af.

## 5. Examengerichte vertaling
- **Typische vraag:** Hoeveel paden van lengte 3 bestaan er tussen twee gegeven knopen?
- **Vaak gemaakte fout:** matrixvermenigvuldiging uitvoeren zonder de betekenis van het `(i,j)`-element te interpreteren.
- **Link met andere concepten:** [[Verbindingsmatrix]], [[Paden Tellen met A^k Worked Example]]

## Context in het domein
- Overzicht: [[00_Overzicht Graph Theory]]
- Uitwerking: [[Paden Tellen met A^k Worked Example]]

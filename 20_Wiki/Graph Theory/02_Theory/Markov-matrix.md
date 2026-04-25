---
type: theory
domain: "graph-theory"
parent: "Graph Representation"
related:
  - Graph Representation
  - Verbindingsmatrix
  - Padlengte via Matrixmachten
theme: "graph-representation"
aliases:
  - Markov-matrix
---

# Markov-matrix
#concept #grafen

## 1. Wat is het kernprobleem?
Hoe modelleer je overgangen tussen toestanden wanneer de verbindingen kansen voorstellen in plaats van vaste routes?

## 2. Intuïtieve uitleg
Een Markov-matrix is een speciale overgangsmatrix die zegt hoe waarschijnlijk het is om van de ene toestand naar de andere te gaan. Je kunt ze zien als een gerichte, gewogen graaf waarin elke stap een kansovergang voorstelt.

## 3. Formele structuur
- de elementen van de matrix zijn overgangskansen
- de som van de elementen per kolom of rij volgt een vaste normalisatie, afhankelijk van de conventie
- een stabiele toestand voldoet aan `M * X = X`

## 4. Toepassing
Markov-matrices worden gebruikt voor marktaandelen, toestandovergangen en populatiemodellen. Na herhaalde stappen zoek je vaak een evenwicht dat niet meer verandert.

## 5. Examengerichte vertaling
- **Typische vraag:** Bepaal de stabiele toestand van deze Markov-matrix.
- **Vaak gemaakte fout:** vergeten de extra normalisatievoorwaarde toe te voegen, zoals `x + y + z = 1`.
- **Link met andere concepten:** [[Verbindingsmatrix]], [[Paden Tellen met A^k Worked Example]], [[Eigenwaarden]]

## Context in het domein
- Overzicht: [[00_Overzicht Graph Theory]]

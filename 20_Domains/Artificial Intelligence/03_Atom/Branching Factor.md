---
type: atom
domain: "artificial-intelligence"
parent: State Space
related:
  - State Space
  - Search Algorithm
  - Breadth-First Search (BFS)
theme: "ai-basics-and-search"
aliases:
  - Branching Factor
---

# Branching Factor
#concept #ai

Branching factor is het gemiddeld aantal opvolgers dat een node in een state space heeft en bepaalt hoe snel een zoekruimte kan groeien.

## Korte kern

- branching factor wordt meestal genoteerd als `b`
- hoe groter `b`, hoe sneller het aantal mogelijke paden explodeert
- het is een kernbegrip in complexiteitsanalyse van zoekalgoritmes

## 1. Wat is het kernprobleem?
Hoe beschrijf je hoeveel nieuwe mogelijkheden een zoekalgoritme gemiddeld krijgt bij elke stap?

## 2. Intuitieve uitleg
De `branching factor` zegt hoeveel kinderen of opvolgers een node gemiddeld heeft. Hoe groter die waarde, hoe sneller de zoekruimte ontploft.

## 3. Formele structuur
- De branching factor wordt meestal aangeduid met `b`.
- `b` is het gemiddeld aantal opvolgers per node.
- In complexiteitsanalyses van zoekalgoritmes komt `b` vaak voor samen met de oplossingsdiepte `d`.
- Veel zoekalgoritmes hebben een tijdscomplexiteit van de vorm `O(b^d)`.

## 4. Snelle vergelijking

- [[Branching Factor]] = gemiddeld aantal opvolgers per node
- [[State Space]] = de volledige zoekruimte waarin die vertakkingen voorkomen
- [[Search Algorithm]] = procedure waarvan de moeilijkheid vaak mee door `b` bepaald wordt

## 5. Toepassing
Als elke toestand gemiddeld `3` opvolgers heeft en de oplossing zit op diepte `4`, dan groeit het aantal te onderzoeken nodes heel snel. Daarom wordt zoekgedrag moeilijk zodra `b` groot wordt.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** `b` is het gemiddeld aantal opvolgers per node, niet het totaal aantal nodes in de zoekruimte.
- **Veelvoorkomende misvatting:** denken dat de branching factor gewoon het aantal nodes van het probleem is.
- **Link met andere concepten:** [[State Space]], [[Search Algorithm]], [[Breadth-First Search (BFS)]], [[Depth-First Search (DFS)]], [[Bi-directional Search]]

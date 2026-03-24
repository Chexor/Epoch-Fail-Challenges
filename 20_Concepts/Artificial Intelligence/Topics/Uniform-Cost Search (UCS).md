---
type: concept-topic
domain: "artificial-intelligence"
parent: Cost-Based Search
related:
  - Cost-Based Search
  - Breadth-First Search (BFS)
  - A-star Search
  - UCS Worked Example
theme: "cost-based-search"
aliases:
  - Uniform-Cost Search (UCS)
---

# Uniform-Cost Search (UCS)
#concept #ai

## 1. Wat is het kernprobleem?
Hoe vind je de goedkoopste oplossing wanneer verbindingen verschillende kosten hebben?

## 2. Intuitieve uitleg
`UCS` kijkt niet naar het aantal stappen, maar naar de totale kost van het pad tot nu toe. Het goedkoopste frontier-pad krijgt altijd voorrang.

## 3. Formele structuur
- gebruikt een [[Priority Queue]]
- kiest de node met laagste `g(n)`
- `g(n)` is de cumulatieve kost vanaf de startnode
- is compleet als alle stapkosten positief zijn
- is optimaal

## 4. Toepassing
In een routeplanner met verschillende afstanden of kosten kan `UCS` een langer pad kiezen als dat in totaal goedkoper is.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** `UCS` kiest op basis van cumulatieve kost `g(n)`, niet op basis van diepte.
- **Veelvoorkomende misvatting:** `UCS` zien als enkel een gewogen versie van `BFS` zonder het centrale belang van `g(n)` te begrijpen.
- **Link met andere concepten:** [[Search Algorithm]], [[Breadth-First Search (BFS)]], [[A-star Search|A* Search]], [[Heuristiek]], [[Path Cost]], [[g(n)]], [[Frontier]], [[Explored Set]], [[Priority Queue]], [[BFS vs DFS vs UCS vs Greedy vs A-star|BFS vs DFS vs UCS vs Greedy vs A*]], [[BFS vs UCS]], [[Tree Search vs Graph Search]]
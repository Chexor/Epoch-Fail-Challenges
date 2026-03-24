---
type: concept-execution
domain: "artificial-intelligence"
parent: "Breadth-First Search (BFS)"
related:
  - Frontier
  - Queue
  - State Space
theme: "step-by-step-search-execution"
aliases:
  - BFS Worked Example
  - BFS
---

# BFS Worked Example
#concept #ai

## Ondersteund concept
- [[Breadth-First Search (BFS)]]

## Doel van deze uitwerking
Deze note toont hoe je `BFS` stap voor stap uitschrijft op een graaf. De nadruk ligt op de `queue`, de expansievolgorde en het gevonden pad.

## Context
Gebruik deze uitwerking wanneer je op examen een ongewogen graaf krijgt en moet tonen hoe `BFS` laag per laag zoekt.

## Voorbeeldgraaf
- start: `A`
- doel: `G`
- buren: `A -> B, C`, `B -> D, E`, `C -> F`, `D -> G`, `E -> G`, `F -> G`
- 
![[BFS Diagram.png]]
## Uitwerking
1. Start met `Queue: [A]`.
2. Expandeer `A` en voeg `A-B`, `A-C` toe: `Queue: [A-B, A-C]`.
3. Expandeer `A-B` en voeg `A-B-D`, `A-B-E` toe: `Queue: [A-C, A-B-D, A-B-E]`.
4. Expandeer `A-C` en voeg `A-C-F` toe: `Queue: [A-B-D, A-B-E, A-C-F]`.
5. Expandeer `A-B-D` en voeg `A-B-D-G` toe: `Queue: [A-B-E, A-C-F, A-B-D-G]`.
6. Het eerste doelpad dat gekozen wordt is `A-B-D-G`.

## Wat toont dit voorbeeld?
- `BFS` werkt laag per laag
- de `queue` bewaart de oudste open paden vooraan
- het eerste gevonden doel ligt op minimale diepte

## Typische fouten
- de `queue` behandelen alsof het een stack is
- vergeten volledige paden uit te schrijven
- denken dat `BFS` altijd het goedkoopste pad vindt, ook bij ongelijke kosten

## Verwante concepten
- [[Breadth-First Search (BFS)]]
- [[Queue]]
- [[Frontier]]
- [[BFS vs UCS]]

## Wat studeer je hierna?
- [[Depth-First Search (DFS)]]
- [[Uniform-Cost Search (UCS)]]
- [[BFS vs DFS vs UCS vs Greedy vs A-star|BFS vs DFS vs UCS vs Greedy vs A*]]

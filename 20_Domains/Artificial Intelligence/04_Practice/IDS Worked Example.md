---
type: practice
domain: "artificial-intelligence"
parent: "Iterative Deepening Search (IDS)"
related:
  - Depth-Limited Search (DLS)
  - Depth-First Search (DFS)
  - Frontier
theme: "step-by-step-search-execution"
aliases:
  - IDS Worked Example
  - IDS
---

# IDS Worked Example
#concept #ai

IDS Worked Example kort uitgelegd: wat het is, waarom het telt en wanneer je het gebruikt.
## Ondersteund concept
- [[Iterative Deepening Search (IDS)]]

## Doel van deze uitwerking
Deze note toont hoe `IDS` in rondes werkt met steeds grotere dieptelimiet.

## Context
Gebruik dit wanneer je op examen geen queue hoeft uit te schrijven, maar wel de opeenvolgende limieten en bezochte nodes moet tonen.

## Voorbeeldgraaf
- start: `A`
- doel: `G`
- structuur: `A -> B, C`, `B -> D, E`, `C -> F`, `D -> G`

![[IDS Diagram.png]]
## Uitwerking
1. Limiet `0`: bezoek `A` -> geen doel.
2. Limiet `1`: bezoek `A, B, C` -> geen doel.
3. Limiet `2`: bezoek `A, B, D, E, C, F` -> geen doel.
4. Limiet `3`: bezoek `A, B, D, G` -> doel gevonden.
5. Gevonden pad: `A-B-D-G`.

## Wat toont dit voorbeeld?
- `IDS` herhaalt een DFS-achtig proces met groeiende limiet
- het gebruikt weinig geheugen zoals `DFS`
- het vindt toch de ondiepste oplossing zoals `BFS`

## Typische fouten
- `IDS` behandelen alsof het gewone `DFS` is
- de limiet vergeten verhogen
- denken dat het herbezoeken van bovenste niveaus altijd heel duur is

## Verwante concepten
- [[Iterative Deepening Search (IDS)]]
- [[Depth-Limited Search (DLS)]]
- [[Depth-First Search (DFS)]]
- [[Breadth-First Search (BFS)]]

## Wat studeer je hierna?
- [[Depth-Limited Search (DLS)]]
- [[BFS vs DFS vs UCS vs Greedy vs A-star|BFS vs DFS vs UCS vs Greedy vs A*]]
- [[00_Overzicht Artificial Intelligence]]

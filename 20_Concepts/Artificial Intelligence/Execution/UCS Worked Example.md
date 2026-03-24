---
type: concept-execution
domain: "artificial-intelligence"
parent: "Uniform-Cost Search (UCS)"
related:
  - Priority Queue
  - g(n)
  - Path Cost
theme: "step-by-step-search-execution"
aliases:
  - UCS Worked Example
  - UCS
---

# UCS Worked Example
#concept #ai

## Ondersteund concept
- [[Uniform-Cost Search (UCS)]]

## Doel van deze uitwerking
Deze note toont hoe `UCS` een graaf doorloopt op basis van cumulatieve kost `g(n)` in plaats van diepte.

## Context
Gebruik dit wanneer een graaf gewogen is en je op examen de `priority queue` met kosten moet uitschrijven.

## Voorbeeldgraaf
- start: `A`
- doel: `G`
- kosten: `A-B=2`, `A-C=4`, `B-D=2`, `B-E=5`, `C-F=3`, `D-G=7`, `E-G=2`, `F-G=2`

![[UCS Diagram.png]]
## Uitwerking
1. Start met `PQ: [A (g=0)]`.
2. Expandeer `A`: `PQ: [A-B (2), A-C (4)]`.
3. Expandeer `A-B`: `PQ: [A-C (4), A-B-D (4), A-B-E (7)]`.
4. Expandeer `A-B-D`: `PQ: [A-C (4), A-B-E (7), A-B-D-G (11)]`.
5. Expandeer `A-C`: `PQ: [A-B-E (7), A-C-F (7), A-B-D-G (11)]`.
6. Expandeer `A-B-E`: `PQ: [A-C-F (7), A-B-E-G (9), A-B-D-G (11)]`.
7. Het eerste doelpad met laagste kost is `A-B-E-G` met `g=9`.

## Wat toont dit voorbeeld?
- `UCS` kiest op basis van [[g(n)]], niet op basis van diepte
- een langer pad kan goedkoper zijn dan een korter pad
- de `priority queue` moet na elke expansie opnieuw op kost bekeken worden

## Typische fouten
- `UCS` behandelen alsof het gewoon `BFS` is
- kosten vergeten bij te werken
- een gegenereerd doelpad al meteen als oplossing nemen zonder te kijken of het het goedkoopste frontier-pad is

## Verwante concepten
- [[Uniform-Cost Search (UCS)]]
- [[Priority Queue]]
- [[g(n)]]
- [[BFS vs UCS]]

## Wat studeer je hierna?
- [[Greedy Best-First Search]]
- [[A-star Search|A* Search]]
- [[Path Cost]]

---
type: concept-execution
domain: "artificial-intelligence"
parent: "A* Search"
related:
  - Priority Queue
  - g(n)
  - h(n)
  - f(n)
theme: "step-by-step-search-execution"
aliases:
  - A* Worked Example
  - A*
---

# A* Worked Example
#concept #ai

## Ondersteund concept
- [[A-star Search|A* Search]]

## Doel van deze uitwerking
Deze note toont hoe `A*` tegelijk rekening houdt met reeds gemaakte kost en geschatte resterende kost.

## Context
Gebruik dit wanneer je op examen `g(n)`, `h(n)` en `f(n)` stap voor stap moet noteren.

## Voorbeeldgraaf
- start: `A`
- doel: `G`
- kosten: `A-B=2`, `A-C=4`, `B-D=2`, `B-E=5`, `C-F=3`, `D-G=7`, `E-G=2`, `F-G=2`
- heuristieken: `h(A)=6`, `h(B)=4`, `h(C)=5`, `h(D)=6`, `h(E)=1`, `h(F)=2`, `h(G)=0`

![[A-star Diagram.png]]
## Uitwerking
1. Start met `PQ: [A (g=0, h=6, f=6)]`.
2. Expandeer `A`: `A-B (2,4,6)`, `A-C (4,5,9)` -> `PQ: [A-B (6), A-C (9)]`.
3. Expandeer `A-B`: `A-B-D (4,6,10)`, `A-B-E (7,1,8)` -> `PQ: [A-B-E (8), A-C (9), A-B-D (10)]`.
4. Expandeer `A-B-E`: `A-B-E-G (9,0,9)` -> `PQ: [A-C (9), A-B-E-G (9), A-B-D (10)]`.
5. Kies het doelpad `A-B-E-G` met totale kost `9`.

## Wat toont dit voorbeeld?
- `A*` combineert [[g(n)]] en [[h(n)]] in [[f(n)]]
- `A*` is minder bijziend dan `Greedy`
- een goede heuristiek maakt het zoeken veel efficiënter

## Typische fouten
- `f(n)` verkeerd berekenen
- `Greedy` en `A*` verwarren
- alleen `h(n)` noteren en `g(n)` vergeten

## Verwante concepten
- [[A-star Search|A* Search]]
- [[g(n)]]
- [[h(n)]]
- [[f(n)]]
- [[Admissible Heuristic]]

## Wat studeer je hierna?
- [[IDA-star (Iterative Deepening A-star)|IDA* (Iterative Deepening A*)]]
- [[Admissible vs Consistent Heuristic]]
- [[BFS vs DFS vs UCS vs Greedy vs A-star|BFS vs DFS vs UCS vs Greedy vs A*]]

---
type: concept-execution
domain: "artificial-intelligence"
parent: "Hill Climbing"
related:
  - Heuristiek
  - h(n)
  - Hill Climbing vs Greedy Best-First Search
theme: "step-by-step-search-execution"
aliases:
  - Hill Climbing Worked Example
  - Hill Climbing
---

# Hill Climbing Worked Example
#concept #ai

## Ondersteund concept
- [[Hill Climbing]]

## Doel van deze uitwerking
Deze note toont hoe `Hill Climbing` puur lokaal kiest en dus geen volledige frontier bijhoudt.

## Context
Gebruik dit wanneer je op examen moet uitleggen waarom `Hill Climbing` snel is, maar kan vastlopen of een suboptimale oplossing kan vinden.

## Voorbeeldgraaf
- start: `A`
- doel: `G`
- heuristieken: `h(A)=6`, `h(B)=4`, `h(C)=5`, `h(D)=6`, `h(E)=1`, `h(F)=2`, `h(G)=0`

![[Hill Climbing Diagram.png]]
## Uitwerking
1. Start in `A` met `h=6`.
2. Vergelijk de directe buren: `B (4)` en `C (5)`.
3. Kies `B`, want `4 < 5`.
4. Vergelijk vanuit `B` de buren `D (6)` en `E (1)`.
5. Kies `E`, want `1 < 6`.
6. Vanuit `E` kies je `G (0)`.
7. Gevonden pad: `A-B-E-G`.

## Wat toont dit voorbeeld?
- `Hill Climbing` kijkt alleen naar de huidige node en haar buren
- het gebruikt geen volledige [[Frontier]]
- het maakt alleen lokale verbeteringen

## Typische fouten
- `Hill Climbing` verwarren met `Greedy Best-First Search`
- scores van andere frontier-nodes meerekenen, terwijl die hier niet bestaan
- vergeten dat een lokale verbetering geen globale garantie geeft

## Verwante concepten
- [[Hill Climbing]]
- [[Heuristiek]]
- [[h(n)]]
- [[Hill Climbing vs Greedy Best-First Search]]

## Wat studeer je hierna?
- [[Greedy Best-First Search]]
- [[A-star Search|A* Search]]
- [[Heuristiek]]

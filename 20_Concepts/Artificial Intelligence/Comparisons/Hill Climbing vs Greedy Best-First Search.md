---
type: concept-comparison
domain: "artificial-intelligence"
parent: Heuristic Search
related:
  - Hill Climbing
  - Greedy Best-First Search
  - Heuristiek
theme: "local-vs-frontier-based-heuristic-search"
aliases:
  - Hill Climbing vs Greedy Best-First Search
---

# Hill Climbing vs Greedy Best-First Search
#concept #ai

## Wat wordt hier vergeleken?
- [[Hill Climbing]]
- [[Greedy Best-First Search]]

## Kernverschil
Beide algoritmes gebruiken een heuristiek, maar `Hill Climbing` denkt puur lokaal vanuit de huidige node, terwijl `Greedy Best-First Search` een volledige frontier bijhoudt en daaruit de beste node kiest.

## Vergelijking

| Aspect | Hill Climbing | Greedy Best-First Search |
| --- | --- | --- |
| Keuze | beste directe buur | beste node in volledige frontier |
| Frontier | meestal geen volledige frontier | wel een priority queue |
| Gebruikt `h(n)` | ja | ja |
| Geheugen | laag | hoger |
| Compleet | nee | niet algemeen |
| Optimaal | nee | nee |
| Typisch risico | local optimum, plateau, ridge | misleidende heuristiek over grotere zoekruimte |

## Wanneer gebruik je wat?
- **Hill Climbing:** als je snel lokaal wil verbeteren met weinig geheugen.
- **Greedy Best-First Search:** als je doelgericht wil zoeken, maar toch meerdere open opties wil onthouden.

## Waarom is dit onderscheid belangrijk?
Deze twee algoritmes lijken op elkaar omdat ze allebei heuristisch zijn. Het fundamentele verschil is dat `Hill Climbing` geen echte frontier-search is, terwijl `Greedy` dat wel is.

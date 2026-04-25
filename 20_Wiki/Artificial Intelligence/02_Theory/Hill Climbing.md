---
type: theory
domain: "artificial-intelligence"
parent: "[[Heuristic Search Algorithms]]"
related:
  - Greedy Best-First Search
  - Heuristic Search
  - Hill Climbing Worked Example
  - Hill Climbing Python Worked Example
theme: "heuristic-search"
aliases:
  - Hill Climbing
---

# Hill Climbing
#concept #ai

Hill Climbing is een lokale zoekmethode die telkens de beste directe buur kiest volgens een heuristiek, zonder een volledige frontier van alternatieven open te houden.

## Korte kern

- gebruikt lokale heuristische verbetering
- onthoudt meestal alleen de huidige toestand en haar buren
- is snel, maar kan vastlopen in lokale valkuilen

## Probleem

Hoe verbeter je snel een huidige toestand op basis van lokale informatie, zonder de volledige zoekruimte open te houden?

## Intuïtie

`Hill Climbing` kijkt alleen naar de huidige node en haar directe buren. Het kiest telkens de buur die er volgens de heuristiek het best uitziet.

## Toepassing

Bij een optimalisatieprobleem kan `Hill Climbing` snel een redelijke oplossing vinden, maar niet noodzakelijk de globale beste.

Kort Python-voorbeeld met een adjacency dict en heuristische scores:

```python
def hill_climbing(graph, heuristic, start, goal):
    path = [start]
    current = start

    while current != goal:
        neighbors = graph.get(current, [])
        if not neighbors:
            return path

        best_neighbor = min(neighbors, key=lambda node: heuristic[node])
        if heuristic[best_neighbor] >= heuristic[current]:
            return path

        path.append(best_neighbor)
        current = best_neighbor

    return path
```

Voor een volledige Python-uitwerking, zie [[Hill Climbing Python Worked Example]].

## Formeel

- gebruikt een `heuristiek`
- bewaart meestal alleen de huidige toestand en haar buren
- kiest lokaal de beste buur
- is niet compleet
- is niet optimaal
- kan vastlopen in een `local optimum`, `plateau` of `ridge`

## Verbanden

> **Valkuil:** `Hill Climbing` verwarren met `Greedy Best-First Search` omdat beide een heuristiek gebruiken.

- [[Heuristic]]
- [[Greedy Best-First Search]]
- [[A-star Search]]
- [[Hill Climbing Worked Example]]
- [[Hill Climbing Python Worked Example]]

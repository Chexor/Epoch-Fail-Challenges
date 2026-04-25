---
type: theory
domain: "artificial-intelligence"
parent: "[[Optimal Search Algorithms]]"
related:
  - Cost-Based Search
  - Breadth-First Search (BFS)
  - A-star Search
  - UCS Worked Example
  - UCS Python Worked Example
theme: "cost-based-search"
aliases:
  - Uniform-Cost Search (UCS)
---

# Uniform-Cost Search (UCS)
#concept #ai

Uniform-Cost Search (UCS) is een zoekalgoritme dat altijd het frontier-pad met de laagste cumulatieve kost kiest en daardoor de goedkoopste oplossing kan vinden bij positieve stapkosten.

## Korte kern

- gebruikt een [[Priority Queue]]
- kiest altijd de laagste [[g(n)]]
- is optimaal bij positieve stapkosten

## Probleem

Hoe vind je de goedkoopste oplossing wanneer verbindingen verschillende kosten hebben?

## Intuïtie

`UCS` kijkt niet naar het aantal stappen, maar naar de totale kost van het pad tot nu toe. Het goedkoopste frontier-pad krijgt altijd voorrang.

## Toepassing

In een routeplanner met verschillende afstanden of kosten kan `UCS` een langer pad kiezen als dat in totaal goedkoper is.

Kort Python-voorbeeld met een adjacency dict:

```python
import heapq


def ucs(graph, start, goal):
    frontier = [(0, [start])]
    best_cost = {start: 0}

    while frontier:
        cost, path = heapq.heappop(frontier)
        node = path[-1]

        if node == goal:
            return cost, path
        if cost > best_cost.get(node, float("inf")):
            continue

        for neighbor, step_cost in graph.get(node, []):
            new_cost = cost + step_cost
            if new_cost < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_cost
                heapq.heappush(frontier, (new_cost, path + [neighbor]))

    return None, None
```

Voor een volledige Python-uitwerking, zie [[UCS Python Worked Example]].

## Formeel

- gebruikt een [[Priority Queue]]
- kiest de node met laagste `g(n)`
- `g(n)` is de cumulatieve kost vanaf de startnode
- is compleet als alle stapkosten positief zijn
- is optimaal

## Verbanden

> **Valkuil:** `UCS` zien als enkel een gewogen versie van `BFS` zonder het centrale belang van `g(n)` te begrijpen.

- [[Search Algorithm]]
- [[Breadth-First Search (BFS)]]
- [[A-star Search]]
- [[Heuristic]]
- [[Path Cost]]
- **Relatie met Branch-and-Bound:** UCS kan worden gezien als een specifiek geval van het 'Branch and Bound' algoritme, waarbij de "bound" de kost van het beste pad is dat tot nu toe naar een node is gevonden. Nodes met een hogere kost worden later (of niet) geëxploreerd.

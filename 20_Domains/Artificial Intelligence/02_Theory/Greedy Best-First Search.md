---
type: theory
domain: "artificial-intelligence"
parent: "[[Heuristic Search Algorithms]]"
related:
  - Hill Climbing
  - A-star Search
  - Heuristic Search
  - Greedy Best-First Search Worked Example
  - Greedy Python Worked Example
theme: "heuristic-search"
aliases:
  - Greedy Best-First Search
---

# Greedy Best-First Search
#concept #ai

Greedy Best-First Search is een heuristisch zoekalgoritme dat altijd de frontier-node kiest die volgens de heuristiek het dichtst bij het doel lijkt.

## Korte kern

- gebruikt een [[Priority Queue]]
- kiest altijd de laagste [[h(n)]]
- zoekt doelgericht, maar negeert de al gemaakte kost

## Probleem

Hoe stuur je search zo snel mogelijk richting doel op basis van een heuristische schatting?

## Intuïtie

`Greedy Best-First Search` kiest altijd de frontier-node die het dichtst bij het doel lijkt. Het denkt dus vooral: "welke optie ziet er nu het meest veelbelovend uit?"

## Toepassing

Als de heuristiek heel informatief is, kan `Greedy` snel naar een doel leiden. Maar het kan ook misleid worden door een node die dichtbij lijkt, maar via een duur of slecht pad bereikbaar is.

Kort Python-voorbeeld met een adjacency dict en heuristische scores:

```python
import heapq


def greedy_best_first(graph, heuristic, start, goal):
    frontier = [(heuristic[start], [start])]
    visited = set()

    while frontier:
        _, path = heapq.heappop(frontier)
        node = path[-1]

        if node == goal:
            return path
        if node in visited:
            continue

        visited.add(node)
        for neighbor in graph.get(node, []):
            heapq.heappush(frontier, (heuristic[neighbor], path + [neighbor]))

    return None
```

Voor een volledige Python-uitwerking, zie [[Greedy Python Worked Example]].

## Formeel

- gebruikt een [[Priority Queue]]
- kiest de laagste `h(n)`
- kijkt niet naar de al gemaakte kost `g(n)`
- is vaak snel
- is niet optimaal
- is niet algemeen betrouwbaar compleet

## Verbanden

> **Valkuil:** denken dat een lage `h(n)` automatisch een goed totaal pad betekent.

- [[Heuristic]]
- [[A-star Search]]
- [[Hill Climbing]]
- [[Uniform-Cost Search (UCS)]]
- [[Frontier]]

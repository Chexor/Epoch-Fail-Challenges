---
type: theory
domain: "artificial-intelligence"
parent: "[[Blind Search Algorithms]]"
related:
  - Depth-First Search (DFS)
  - Blind Search
  - Uniform-Cost Search (UCS)
  - BFS Worked Example
  - BFS Python Worked Example
theme: "uninformed-search-strategies"
aliases:
  - Breadth-First Search (BFS)
---

# Breadth-First Search (BFS)
#concept #ai

Breadth-First Search (BFS) is een zoekalgoritme dat systematisch alle paden op kleinere diepte onderzoekt voor het diepere paden bekijkt.

## Korte kern

- gebruikt een [[Queue]] (`FIFO`)
- zoekt laag per laag vanuit de startnode
- optimaal bij gelijke stapkosten

## Probleem

Hoe vind je systematisch een oplossing door eerst alle ondiepe paden te onderzoeken?

## Intuïtie

`BFS` zoekt in lagen. Eerst bekijkt het alles op diepte `1`, dan alles op diepte `2`, enzovoort. Het verspreidt zich als een golf vanuit de startnode.

## Toepassing

In een ongewogen doolhof is `BFS` geschikt als je de oplossing met het kleinste aantal stappen zoekt.

Kort Python-voorbeeld met een adjacency dict:

```python
from collections import deque


def bfs(graph, start, goal):
    frontier = deque([[start]])
    visited = set()

    while frontier:
        path = frontier.popleft()
        node = path[-1]

        if node == goal:
            return path
        if node in visited:
            continue

        visited.add(node)
        for neighbor in graph.get(node, []):
            frontier.append(path + [neighbor])

    return None
```

Voor een volledige Python-uitwerking, zie [[BFS Python Worked Example]].

## Formeel

- gebruikt een [[Queue]] (`FIFO`)
- kiest altijd de node met de kleinste diepte
- is **compleet** bij eindige branching factor
- is **optimaal** als alle stapkosten gelijk zijn
- gebruikt veel geheugen omdat volledige niveaus in de frontier kunnen blijven staan

## Verbanden

> **Valkuil:** denken dat `BFS` altijd de goedkoopste oplossing vindt. Dat geldt alleen bij gelijke stapkosten.

- [[Search Algorithm]]
- [[State Space]]
- [[Depth-First Search (DFS)]]
- [[Uniform-Cost Search (UCS)]]
- [[Iterative Deepening Search (IDS)]]

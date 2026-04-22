---
type: theory
domain: "artificial-intelligence"
parent: "[[Blind Search Algorithms]]"
related:
  - Breadth-First Search (BFS)
  - Blind Search
  - Iterative Deepening Search (IDS)
  - DFS Worked Example
  - DFS Python Worked Example
theme: "uninformed-search-strategies"
aliases:
  - Depth-First Search (DFS)
---

# Depth-First Search (DFS)
#concept #ai

Depth-First Search (DFS) is een zoekalgoritme dat eerst 1 pad zo diep mogelijk volgt voor het terugkeert naar eerdere vertakkingen.

## Korte kern

- gebruikt een [[Stack]] (`LIFO`) of recursie
- zoekt eerst diep, pas daarna breed
- gebruikt weinig geheugen, maar is niet optimaal

## Probleem

Hoe zoek je snel met weinig geheugen door eerst een pad zo diep mogelijk te volgen?

## Intuïtie

`DFS` kiest een tak en volgt die zo diep mogelijk. Pas wanneer die tak stopt of faalt, keert het terug naar een vorige vertakking.

## Toepassing

`DFS` is nuttig als geheugen schaars is of als een oplossing mogelijk diep zit en je snel een eerste oplossing wil proberen te vinden.

Kort Python-voorbeeld met een adjacency dict:

```python
def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path
        if node in visited:
            continue

        visited.add(node)
        for neighbor in reversed(graph.get(node, [])):
            stack.append(path + [neighbor])

    return None
```

Voor een volledige Python-uitwerking, zie [[DFS Python Worked Example]].

## Formeel

- gebruikt een [[Stack]] (`LIFO`) of recursie
- kiest de diepste open node
- gebruikt weinig geheugen
- is in het algemeen niet compleet
- is niet optimaal

## Verbanden

> **Valkuil:** denken dat snel een doel bereiken automatisch betekent dat de gevonden oplossing goed is.

- [[Search Algorithm]]
- [[Breadth-First Search (BFS)]]
- [[Depth-Limited Search (DLS)]]
- [[Iterative Deepening Search (IDS)]]
- [[Hill Climbing]]

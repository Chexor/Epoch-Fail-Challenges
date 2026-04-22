---
type: theory
domain: "artificial-intelligence"
parent: "[[Blind Search Algorithms]]"
related:
  - Blind Search
  - Depth-First Search (DFS)
  - Iterative Deepening Search (IDS)
  - Search Algorithm
theme: "uninformed-search-strategies"
aliases:
  - Depth-Limited Search (DLS)
---

# Depth-Limited Search (DLS)
#concept #ai

Depth-Limited Search (DLS) is een variant van `DFS` die alleen zoekt tot een vooraf ingestelde maximale diepte en daaronder geen verdere expansie meer toelaat.

## Korte kern

- is `DFS` met een harde dieptelimiet `l`
- voorkomt oneindig diep afdalen in 1 tak
- is nuttig als bouwsteen voor [[Iterative Deepening Search (IDS)]]

## Probleem

Hoe beperk je `DFS` zodat het niet oneindig diep blijft zoeken?

## Intuïtie

`DLS` is `DFS` met een harde grens. Zodra de ingestelde diepte bereikt is, stopt het algoritme met verder afdalen in die tak.

## Toepassing

Als je weet dat een oplossing waarschijnlijk niet dieper dan bijvoorbeeld `5` stappen zit, kan `DLS` nuttig zijn om nutteloze diepe exploratie te vermijden.

Kort Python-voorbeeld met een adjacency dict:

```python
def dls(graph, start, goal, limit):
    stack = [([start], 0)]

    while stack:
        path, depth = stack.pop()
        node = path[-1]

        if node == goal:
            return path
        if depth == limit:
            continue

        for neighbor in reversed(graph.get(node, [])):
            stack.append((path + [neighbor], depth + 1))

    return None
```

Voor een grotere code-uitwerking, zie [[IDS Python Worked Example]] als de iteratieve versie van dit idee.

## Formeel

- gebruikt de logica van `DFS`
- voegt een dieptelimiet `l` toe
- voorkomt oneindig diep zoeken
- is niet volledig als de oplossing dieper zit dan de limiet
- is niet optimaal

## Verbanden

> **Valkuil:** denken dat een dieptelimiet altijd een veilige verbetering is.

- [[Depth-First Search (DFS)]]
- [[Iterative Deepening Search (IDS)]]
- [[Search Algorithm]]
- [[Blind Search]]
- [[Branching Factor]]

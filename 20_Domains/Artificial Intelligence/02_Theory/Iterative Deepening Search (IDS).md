---
type: theory
domain: "artificial-intelligence"
parent: "[[Blind Search Algorithms]]"
related:
  - Depth-First Search (DFS)
  - Depth-Limited Search (DLS)
  - Blind Search
  - IDS Worked Example
  - IDS Python Worked Example
  - Breadth-First Search (BFS)
theme: "uninformed-search-strategies"
aliases:
  - Iterative Deepening Search (IDS)
---

# Iterative Deepening Search (IDS)
#concept #ai

Iterative Deepening Search (IDS) is een zoekalgoritme dat herhaaldelijk depth-limited search uitvoert met steeds grotere dieptelimiet tot een oplossing gevonden wordt.

## Korte kern

- herhaalt [[Depth-Limited Search (DLS)]] met limieten `0, 1, 2, ...`
- combineert weinig geheugengebruik met systematisch zoeken
- optimaal bij gelijke stapkosten

## Probleem

Hoe combineer je het lage geheugengebruik van `DFS` met de volledigheid van `BFS`?

## Intuïtie

`IDS` voert meerdere rondes van `DLS` uit. Eerst zoek je tot diepte `0`, dan `1`, dan `2`, enzovoort, tot een oplossing gevonden wordt.

## Toepassing

`IDS` is nuttig wanneer je niet weet hoe diep de oplossing zit, maar wel de ondiepste oplossing wil vinden zonder het geheugenverbruik van `BFS`.

Kort Python-voorbeeld met een adjacency dict:

```python
def ids(graph, start, goal, max_depth):
    for limit in range(max_depth + 1):
        result = dls(graph, start, goal, limit)
        if result is not None:
            return result
    return None
```

Voor een volledige Python-uitwerking, zie [[IDS Python Worked Example]].

## Formeel

- herhaalt `Depth-Limited Search`
- verhoogt de limiet stapsgewijs
- is compleet
- is optimaal bij gelijke stapkosten
- gebruikt weinig geheugen

## Verbanden

> **Valkuil:** denken dat het herhalen van bovenste niveaus altijd onaanvaardbaar duur is.

- [[Depth-First Search (DFS)]]
- [[Depth-Limited Search (DLS)]]
- [[Breadth-First Search (BFS)]]
- [[Search Algorithm]]
- [[Blind Search]]

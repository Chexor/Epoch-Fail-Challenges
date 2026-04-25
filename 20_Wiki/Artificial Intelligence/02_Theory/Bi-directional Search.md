---
type: theory
domain: "artificial-intelligence"
parent: Blind Search
related:
  - Blind Search
  - Breadth-First Search (BFS)
  - State Space
  - Frontier
  - Search Algorithm
theme: "uninformed-search-strategies"
aliases:
  - Bi-directional Search
---

# Bi-directional Search
#concept #ai

Bi-directional Search is een zoekstrategie die tegelijk vanuit de start en vanuit het doel zoekt, zodat beide zoekfronten elkaar idealiter halverwege ontmoeten.

## Korte kern

- gebruikt 2 zoekrichtingen in plaats van 1
- kan de effectieve zoekdiepte sterk verkleinen
- werkt alleen goed als achterwaarts zoeken zinvol mogelijk is

## Probleem

Hoe verklein je de zoekdiepte door zowel vanuit de start als vanuit het doel te zoeken?

## Intuïtie

In plaats van de volledige afstand van start naar doel in één richting af te leggen, laat je twee zoekfronten naar elkaar toe groeien. Ze ontmoeten elkaar hopelijk ongeveer in het midden.

## Toepassing

Bij routeproblemen waarbij start en doel expliciet gekend zijn, kan `Bi-directional Search` veel sneller zijn dan een klassieke eenrichtingszoektocht.

Kort Python-voorbeeld met adjacency dicts:

```python
def bidirectional_search(start_frontier, goal_frontier):
    while start_frontier and goal_frontier:
        if start_frontier & goal_frontier:
            return start_frontier & goal_frontier
        break
    return set()
```

## Formeel

- gebruikt twee zoekprocessen
- één zoekt vooruit vanaf de start
- één zoekt achteruit vanaf het doel
- stopt wanneer beide frontiers elkaar raken
- kan de complexiteit reduceren van ongeveer `O(b^d)` naar `O(b^(d/2))`

## Verbanden

> **Valkuil:** vergeten dat achterwaarts zoeken of een omgekeerde probleemrepresentatie mogelijk moet zijn.

- [[Branching Factor]]
- [[State Space]]
- [[Search Algorithm]]
- [[Frontier]]
- [[Breadth-First Search (BFS)]]

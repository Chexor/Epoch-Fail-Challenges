---
type: practice
domain: "artificial-intelligence"
parent: "Breadth-First Search (BFS)"
related:
  - Breadth-First Search (BFS)
  - BFS Worked Example
  - Queue
  - Frontier
theme: "python-search-implementations"
aliases:
  - BFS Python Worked Example
  - BFS Python Example
---

# BFS Python Worked Example
#concept #ai

BFS Python Worked Example toont hoe je `Breadth-First Search` helder implementeert met een adjacency dict en een `queue`.

## Korte kern

- gebruikt `deque` als `FIFO`-queue
- bewaart paden expliciet zodat het resultaat direct leesbaar is
- toont hoe laag-per-laag zoeken in code werkt

## Ondersteund concept
- [[Breadth-First Search (BFS)]]

## Doel van deze uitwerking
Deze note toont een kleine, neutrale Python-implementatie van `BFS` die examenvriendelijk blijft en makkelijk te lezen is.

## Context
Gebruik dit wanneer je `BFS` niet alleen op papier wil tracen, maar ook wil zien hoe de `queue`, `visited set` en padopbouw in code samenwerken.

## Codevoorbeeld
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


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["G"],
    "E": ["G"],
    "F": ["G"],
    "G": [],
}

print(bfs(graph, "A", "G"))
```

## Stap-voor-stap uitleg
- `frontier` start met 1 pad: `['A']`
- telkens wordt het oudste pad uit de `queue` gehaald
- `visited` voorkomt dat dezelfde node opnieuw volledig verwerkt wordt
- voor elke buur wordt een nieuw pad gemaakt en achteraan toegevoegd
- het eerste gevonden doelpad is bij `BFS` het pad op minimale diepte

## Verwachte output of gedrag
- de functie geeft een pad terug zoals `['A', 'B', 'D', 'G']`
- de exacte vorm hangt af van de buurvolgorde in de adjacency dict
- bij een ongewogen graaf krijg je zo een oplossing met minimaal aantal stappen

## Uitwerking
1. Start met een `queue` die alleen het startpad bevat.
2. Haal telkens het oudste open pad uit de frontier.
3. Stop zodra de laatste node van dat pad het doel is.
4. Voeg anders alle buren als nieuwe paden achteraan toe.

## Wat toont dit voorbeeld?
- hoe `FIFO`-gedrag de laagstructuur van `BFS` veroorzaakt
- waarom buurvolgorde de exacte oplossing kan beinvloeden, maar niet het diepteniveau

## Typische fouten
- een gewone lijst gebruiken en per ongeluk `LIFO`-gedrag krijgen
- `visited` te laat of inconsistent gebruiken
- vergeten dat `BFS` alleen optimaal is bij gelijke stapkosten

## Verwante concepten
- [[Breadth-First Search (BFS)]]
- [[BFS Worked Example]]
- [[Queue]]
- [[Frontier]]

## Begripsafbakening en verbanden
- **Kernonderscheid:** dit is een code-uitwerking van `BFS`, geen vervanging van de conceptnote zelf.
- **Veelvoorkomende misvatting:** denken dat deze implementatie automatisch de goedkoopste oplossing zoekt; ze zoekt hier op minimale diepte.
- **Link met andere concepten:** [[Breadth-First Search (BFS)]], [[BFS Worked Example]], [[Queue]], [[Frontier]], [[State Space]]

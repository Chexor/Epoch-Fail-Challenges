---
type: practice
domain: "artificial-intelligence"
parent: "Greedy Best-First Search"
related:
  - Greedy Best-First Search
  - Greedy Best-First Search Worked Example
  - Heuristiek
  - Priority Queue
theme: "python-search-implementations"
aliases:
  - Greedy Python Worked Example
  - Greedy Best-First Search Python Example
---

# Greedy Python Worked Example
#concept #ai

Greedy Python Worked Example toont hoe je `Greedy Best-First Search` implementeert met een adjacency dict, heuristische scores en een `priority queue`.

## Korte kern

- kiest telkens de node met laagste `h(n)`
- gebruikt `heapq` als `priority queue`
- toont waarom doelgericht zoeken niet automatisch optimaal is

## Ondersteund concept
- [[Greedy Best-First Search]]

## Doel van deze uitwerking
Deze note toont een kleine Python-implementatie van `Greedy Best-First Search` die duidelijk maakt hoe de heuristiek de keuze volledig stuurt.

## Context
Gebruik dit wanneer je wil zien hoe `Greedy` verschilt van `UCS` en `A*`, vooral omdat alleen de geschatte resterende kost gebruikt wordt.

## Codevoorbeeld
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


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["G"],
    "E": [],
    "F": ["G"],
    "G": [],
}

heuristic = {
    "A": 5,
    "B": 4,
    "C": 1,
    "D": 6,
    "E": 7,
    "F": 2,
    "G": 0,
}

print(greedy_best_first(graph, heuristic, "A", "G"))
```

## Stap-voor-stap uitleg
- `frontier` bewaart open paden met hun heuristische score
- telkens wordt het pad gekozen waarvan de laatste node de laagste `h(n)` heeft
- al gemaakte kost telt hier niet mee
- `visited` voorkomt dat dezelfde node telkens opnieuw volledig verwerkt wordt

## Verwachte output of gedrag
- de functie geeft een pad terug zoals `['A', 'C', 'F', 'G']`
- het gekozen pad voelt doelgericht aan, maar is niet noodzakelijk het goedkoopste pad
- buur- en heuristiekwaarden bepalen sterk welke tak eerst gekozen wordt

## Uitwerking
1. Start met het startpad en diens heuristiek.
2. Neem telkens het open pad met laagste `h(n)`.
3. Voeg opvolgers toe met hun eigen heuristische score.
4. Stop zodra het gekozen pad op het doel eindigt.

## Wat toont dit voorbeeld?
- hoe `Greedy` volledig door `h(n)` gestuurd wordt
- waarom een "veelbelovende" node toch tot een minder goed totaalpad kan leiden

## Typische fouten
- `g(n)` toch mee opnemen en zo onbedoeld richting `A*` schuiven
- denken dat het eerste doelpad automatisch optimaal is
- een heuristiek gebruiken zonder te beseffen dat slechte schattingen het gedrag sterk kunnen misleiden

## Verwante concepten
- [[Greedy Best-First Search]]
- [[Greedy Best-First Search Worked Example]]
- [[Heuristic]]
- [[Priority Queue]]

## Begripsafbakening en verbanden
- **Kernonderscheid:** deze implementatie toont zuivere `Greedy Best-First Search`; de al gemaakte kost speelt geen rol.
- **Veelvoorkomende misvatting:** denken dat `Greedy` een snellere versie van `A*` is zonder inhoudelijk verschil; de keuzeregel is fundamenteel anders.
- **Link met andere concepten:** [[Greedy Best-First Search]], [[Greedy Best-First Search Worked Example]], [[Heuristic]], [[Priority Queue]], [[A-star Search]], [[Uniform-Cost Search (UCS)]]

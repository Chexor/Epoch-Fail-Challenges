---
type: practice
domain: "artificial-intelligence"
parent: "A-star Search"
related:
  - A-star Search
  - A-star Worked Example
  - f(n)
  - Priority Queue
theme: "python-search-implementations"
aliases:
  - A-star Python Worked Example
  - A* Python Worked Example
---

# A-star Python Worked Example
#concept #ai

A-star Python Worked Example toont hoe je `A* Search` implementeert met een gewogen adjacency dict, heuristische scores en een `priority queue`.

## Korte kern

- gebruikt `f(n) = g(n) + h(n)` als prioriteit
- combineert echte kost en schatting in 1 keuzeregel
- toont hoe `A*` operationeel verschilt van `Greedy` en `UCS`

## Ondersteund concept
- [[A-star Search]]

## Doel van deze uitwerking
Deze note toont een leesbare Python-implementatie van `A*` zodat de rol van `g(n)`, `h(n)` en `f(n)` in code meteen zichtbaar wordt.

## Context
Gebruik dit wanneer je wil zien hoe `A*` praktisch werkt op een gewogen graaf met een heuristiek die het zoeken richting doel stuurt.

## Codevoorbeeld
```python
import heapq


def a_star(graph, heuristic, start, goal):
    frontier = [(heuristic[start], 0, [start])]
    best_cost = {start: 0}

    while frontier:
        _, cost, path = heapq.heappop(frontier)
        node = path[-1]

        if node == goal:
            return cost, path
        if cost > best_cost.get(node, float("inf")):
            continue

        for neighbor, step_cost in graph.get(node, []):
            new_cost = cost + step_cost
            if new_cost < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(frontier, (priority, new_cost, path + [neighbor]))

    return None, None


graph = {
    "A": [("B", 2), ("C", 4)],
    "B": [("D", 2), ("E", 5)],
    "C": [("F", 1)],
    "D": [("G", 5)],
    "E": [("G", 2)],
    "F": [("G", 3)],
    "G": [],
}

heuristic = {
    "A": 5,
    "B": 4,
    "C": 2,
    "D": 4,
    "E": 1,
    "F": 2,
    "G": 0,
}

print(a_star(graph, heuristic, "A", "G"))
```

## Stap-voor-stap uitleg
- `frontier` bewaart triples van de vorm `(f, g, pad)`
- `g` houdt de echte kost tot nu toe bij
- `h` komt uit de heuristische tabel
- `f = g + h` bepaalt welke open kandidaat eerst onderzocht wordt
- `best_cost` voorkomt dat slechtere paden naar dezelfde node dominant blijven

## Verwachte output of gedrag
- de functie geeft iets terug zoals `(8, ['A', 'C', 'F', 'G'])`
- het gekozen pad hangt af van zowel echte kosten als heuristische waarden
- bij een goede heuristiek zoekt `A*` gerichter dan `UCS` en veiliger dan `Greedy`

## Uitwerking
1. Start met het triviale pad naar de startnode.
2. Bereken voor elk open pad een score `f = g + h`.
3. Kies telkens de kandidaat met de laagste `f`.
4. Werk betere kosten naar opvolgers bij en voeg die opnieuw toe.

## Wat toont dit voorbeeld?
- hoe `A*` theorie rechtstreeks naar een codepatroon vertaalt
- waarom `A*` noch zuivere kostzoeking noch zuivere heuristische zoeking is

## Typische fouten
- `h(n)` gebruiken zonder `g(n)` en zo per ongeluk `Greedy` implementeren
- `best_cost` weglaten waardoor slechtere paden te lang blijven meedraaien
- denken dat elke heuristiek automatisch de optimale garanties van `A*` bewaart

## Verwante concepten
- [[A-star Search]]
- [[A-star Worked Example]]
- [[f(n)]]
- [[Priority Queue]]

## Begripsafbakening en verbanden
- **Kernonderscheid:** deze note toont de Python-uitvoering van `A*`; de conceptnote legt de formele eigenschappen uit.
- **Veelvoorkomende misvatting:** denken dat `A*` gewoon `UCS` plus wat extra data is; de heuristische component verandert de zoekrichting fundamenteel.
- **Link met andere concepten:** [[A-star Search]], [[A-star Worked Example]], [[f(n)]], [[g(n)]], [[h(n)]], [[Priority Queue]], [[Greedy Best-First Search]], [[Uniform-Cost Search (UCS)]]

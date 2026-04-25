---
type: practice
domain: "artificial-intelligence"
parent: "Uniform-Cost Search (UCS)"
related:
  - Uniform-Cost Search (UCS)
  - UCS Worked Example
  - Priority Queue
  - g(n)
theme: "python-search-implementations"
aliases:
  - UCS Python Worked Example
  - Uniform-Cost Search Python Example
---

# UCS Python Worked Example
#concept #ai

UCS Python Worked Example toont hoe je `Uniform-Cost Search` implementeert met een adjacency dict en een `priority queue` op cumulatieve kost.

## Korte kern

- gebruikt `heapq` als `priority queue`
- kiest altijd het goedkoopste open pad
- laat zien waarom `g(n)` belangrijker is dan diepte

## Ondersteund concept
- [[Uniform-Cost Search (UCS)]]

## Doel van deze uitwerking
Deze note toont een neutrale Python-implementatie van `UCS` die het verband zichtbaar maakt tussen `path cost`, `g(n)` en de `priority queue`.

## Context
Gebruik dit wanneer je gewogen grafen bestudeert en wil zien hoe `UCS` in code verschilt van `BFS`.

## Codevoorbeeld
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


graph = {
    "A": [("B", 2), ("C", 4)],
    "B": [("D", 2), ("E", 5)],
    "C": [("F", 3)],
    "D": [("G", 7)],
    "E": [("G", 2)],
    "F": [("G", 2)],
    "G": [],
}

print(ucs(graph, "A", "G"))
```

## Stap-voor-stap uitleg
- `frontier` bewaart tuples van de vorm `(kost, pad)`
- `heapq` zorgt dat altijd het pad met laagste kost eerst gekozen wordt
- `best_cost` houdt bij wat de goedkoopste bekende kost per node is
- nieuwe paden worden alleen toegevoegd als ze echt goedkoper zijn

## Verwachte output of gedrag
- de functie geeft iets terug zoals `(9, ['A', 'B', 'E', 'G'])`
- een pad met meer stappen kan toch gekozen worden als de totale kost lager is
- de doelnode is pas veilig als ze uit de `priority queue` gehaald wordt als goedkoopste open pad

## Uitwerking
1. Start met het triviale pad naar de startnode met kost `0`.
2. Neem altijd het open pad met de laagste cumulatieve kost.
3. Werk kosten naar buren bij en voeg alleen betere paden toe.
4. Stop wanneer het goedkoopste open pad op het doel eindigt.

## Wat toont dit voorbeeld?
- hoe `UCS` op kost sorteert in plaats van op diepte
- waarom `best_cost` nodig is om slechtere paden te negeren

## Typische fouten
- een gewone lijst gebruiken zonder echte prioriteit op kost
- buurpaden toevoegen zonder kosten op te tellen
- een doelpad te vroeg accepteren zodra het alleen maar gegenereerd is

## Verwante concepten
- [[Uniform-Cost Search (UCS)]]
- [[UCS Worked Example]]
- [[Priority Queue]]
- [[g(n)]]

## Begripsafbakening en verbanden
- **Kernonderscheid:** deze note toont de operationele Python-versie van `UCS`, terwijl de theory-note de theorie en garanties samenvat.
- **Veelvoorkomende misvatting:** denken dat `UCS` gewoon `BFS` met getallen is; de keuzeregel verandert fundamenteel.
- **Link met andere concepten:** [[Uniform-Cost Search (UCS)]], [[UCS Worked Example]], [[Priority Queue]], [[g(n)]], [[Path Cost]], [[A-star Search]]

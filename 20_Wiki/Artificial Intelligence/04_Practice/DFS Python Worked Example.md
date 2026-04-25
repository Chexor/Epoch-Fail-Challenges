---
type: practice
domain: "artificial-intelligence"
parent: "Depth-First Search (DFS)"
related:
  - Depth-First Search (DFS)
  - DFS Worked Example
  - Stack
  - Frontier
theme: "python-search-implementations"
aliases:
  - DFS Python Worked Example
  - DFS Python Example
---

# DFS Python Worked Example
#concept #ai

DFS Python Worked Example toont hoe je `Depth-First Search` helder implementeert met een adjacency dict en een `stack`.

## Korte kern

- gebruikt een expliciete `stack`
- volgt 1 tak zo diep mogelijk voor het terugkeert
- toont hoe buurvolgorde het gedrag van `DFS` sterk beinvloedt

## Ondersteund concept
- [[Depth-First Search (DFS)]]

## Doel van deze uitwerking
Deze note toont een kleine Python-implementatie van `DFS` die de kern van het algoritme zichtbaar maakt zonder overbodige technische ruis.

## Context
Gebruik dit wanneer je wil zien hoe `DFS` operationeel verschilt van `BFS`, vooral qua datastructuur en uitbreidingsvolgorde.

## Codevoorbeeld
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


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["G"],
    "E": [],
    "F": [],
    "G": [],
}

print(dfs(graph, "A", "G"))
```

## Stap-voor-stap uitleg
- `stack` bewaart open paden, met het recentste pad bovenaan
- `pop()` kiest altijd het laatst toegevoegde pad
- `reversed(...)` zorgt dat de linkse buur eerst verder onderzocht wordt
- het algoritme duikt zo snel diep in 1 tak voor het terugkomt

## Verwachte output of gedrag
- de functie geeft een pad terug zoals `['A', 'B', 'D', 'G']`
- verander je de buurvolgorde, dan kan `DFS` een heel andere tak eerst volgen
- de eerste gevonden oplossing is niet noodzakelijk de beste oplossing

## Uitwerking
1. Start met een `stack` die enkel het startpad bevat.
2. Neem telkens het laatst toegevoegde open pad.
3. Controleer of de laatste node het doel is.
4. Voeg nieuwe paden toe zodat de gewenste buurvolgorde behouden blijft.

## Wat toont dit voorbeeld?
- hoe `LIFO`-gedrag `DFS` diep in 1 tak stuurt
- waarom `DFS` weinig geheugen gebruikt maar minder veilige garanties heeft

## Typische fouten
- buren in de verkeerde volgorde op de `stack` zetten
- aannemen dat het eerste gevonden pad ook optimaal is
- `DFS` verwarren met een heuristische methode zoals `Hill Climbing`

## Verwante concepten
- [[Depth-First Search (DFS)]]
- [[DFS Worked Example]]
- [[Stack]]
- [[Frontier]]

## Begripsafbakening en verbanden
- **Kernonderscheid:** deze note toont de implementatiekant van `DFS`; de theoretische garanties staan in de theory-note.
- **Veelvoorkomende misvatting:** denken dat `DFS` altijd dezelfde volgorde volgt; die hangt sterk af van de buurvolgorde.
- **Link met andere concepten:** [[Depth-First Search (DFS)]], [[DFS Worked Example]], [[Stack]], [[Frontier]], [[Iterative Deepening Search (IDS)]]

---
type: practice
domain: "artificial-intelligence"
parent: "Iterative Deepening Search (IDS)"
related:
  - Iterative Deepening Search (IDS)
  - IDS Worked Example
  - Depth-Limited Search (DLS)
  - Depth-First Search (DFS)
theme: "python-search-implementations"
aliases:
  - IDS Python Worked Example
  - Iterative Deepening Search Python Example
---

# IDS Python Worked Example
#concept #ai

IDS Python Worked Example toont hoe je `Iterative Deepening Search` implementeert door `Depth-Limited Search` herhaaldelijk uit te voeren met oplopende limieten.

## Korte kern

- herhaalt `DLS` met limieten `0, 1, 2, ...`
- gebruikt weinig geheugen zoals `DFS`
- houdt de zoeklogica leesbaar door `DLS` apart te definiëren

## Ondersteund concept
- [[Iterative Deepening Search (IDS)]]

## Doel van deze uitwerking
Deze note toont een neutrale Python-uitwerking van `IDS` zodat de relatie tussen `DFS`, `DLS` en systematische limietverhoging helder wordt.

## Context
Gebruik dit wanneer je wil begrijpen hoe `IDS` operationeel werkt zonder de geheugenkost van `BFS`.

## Codevoorbeeld
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


def ids(graph, start, goal, max_depth):
    for limit in range(max_depth + 1):
        result = dls(graph, start, goal, limit)
        if result is not None:
            return result
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

print(ids(graph, "A", "G", 4))
```

## Stap-voor-stap uitleg
- `dls(...)` voert 1 depth-limited ronde uit
- `ids(...)` verhoogt de limiet stapsgewijs
- elke nieuwe ronde start opnieuw vanaf de root
- zodra een limiet de oplossing toelaat, stopt `IDS`

## Verwachte output of gedrag
- de functie geeft een pad terug zoals `['A', 'B', 'D', 'G']`
- bovenste niveaus worden meerdere keren opnieuw bezocht
- het algoritme blijft toch geheugenefficiënt omdat het per ronde depth-first werkt

## Uitwerking
1. Start met limiet `0`.
2. Voer `DLS` uit tot die limiet.
3. Verhoog de limiet met `1` als geen oplossing gevonden is.
4. Stop zodra een ronde wel een doelpad oplevert.

## Wat toont dit voorbeeld?
- hoe `IDS` `DFS`-achtig geheugen koppelt aan systematische dekking
- waarom herhaling van ondiepe niveaus de prijs is voor dat lage geheugen

## Typische fouten
- de limiet niet verhogen na een mislukte ronde
- `IDS` verwarren met 1 enkele `DLS`-run
- vergeten dat buurvolgorde nog altijd meespeelt binnen elke depth-first ronde

## Verwante concepten
- [[Iterative Deepening Search (IDS)]]
- [[IDS Worked Example]]
- [[Depth-Limited Search (DLS)]]
- [[Depth-First Search (DFS)]]

## Begripsafbakening en verbanden
- **Kernonderscheid:** deze note toont de Python-uitvoering van `IDS`; de conceptnote legt uit waarom deze strategie theoretisch interessant is.
- **Veelvoorkomende misvatting:** denken dat `IDS` alleen maar inefficiënt is door herhaling; de geheugenkant is precies de winst.
- **Link met andere concepten:** [[Iterative Deepening Search (IDS)]], [[IDS Worked Example]], [[Depth-Limited Search (DLS)]], [[Depth-First Search (DFS)]], [[Breadth-First Search (BFS)]]

---
type: practice
domain: "artificial-intelligence"
parent: "Hill Climbing"
related:
  - Hill Climbing
  - Hill Climbing Worked Example
  - Heuristiek
  - h(n)
theme: "python-search-implementations"
aliases:
  - Hill Climbing Python Worked Example
  - Hill Climbing Python Example
---

# Hill Climbing Python Worked Example
#concept #ai

Hill Climbing Python Worked Example toont hoe je `Hill Climbing` implementeert met een adjacency dict en lokale heuristische keuzes zonder volledige frontier.

## Korte kern

- kiest telkens de beste directe buur
- houdt alleen de huidige positie en het pad bij
- stopt zodra geen betere buur meer bestaat

## Ondersteund concept
- [[Hill Climbing]]

## Doel van deze uitwerking
Deze note toont een kleine Python-implementatie van `Hill Climbing` zodat het verschil met frontier-gebaseerde zoekalgoritmes zichtbaar wordt.

## Context
Gebruik dit wanneer je wil begrijpen hoe een lokale zoekmethode werkt die alleen naar de directe buren van de huidige toestand kijkt.

## Codevoorbeeld
```python
def hill_climbing(graph, heuristic, start, goal):
    path = [start]
    current = start

    while current != goal:
        neighbors = graph.get(current, [])
        if not neighbors:
            return path

        best_neighbor = min(neighbors, key=lambda node: heuristic[node])
        if heuristic[best_neighbor] >= heuristic[current]:
            return path

        path.append(best_neighbor)
        current = best_neighbor

    return path


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": [],
}

heuristic = {
    "A": 6,
    "B": 4,
    "C": 5,
    "D": 6,
    "E": 1,
    "F": 2,
    "G": 0,
}

print(hill_climbing(graph, heuristic, "A", "G"))
```

## Stap-voor-stap uitleg
- `current` houdt de huidige node bij
- enkel de directe buren van `current` worden bekeken
- de buur met de laagste heuristische score wordt gekozen
- zodra geen buur beter is dan de huidige node, stopt het algoritme

## Verwachte output of gedrag
- de functie geeft een pad terug zoals `['A', 'B', 'E', 'G']`
- als het algoritme in een `local optimum` belandt, stopt het zonder globale garantie
- het gedrag hangt sterk af van de heuristische waarden

## Uitwerking
1. Start in de huidige node met haar heuristische score.
2. Vergelijk alleen de directe buren.
3. Ga naar de beste buur als die echt beter is.
4. Stop bij doel of wanneer geen verbetering meer mogelijk is.

## Wat toont dit voorbeeld?
- hoe `Hill Climbing` puur lokaal beslist
- waarom deze aanpak snel is maar gemakkelijk kan vastlopen

## Typische fouten
- een volledige frontier bijhouden en zo onbewust richting `Greedy Best-First Search` gaan
- ook slechtere buren toelaten zonder duidelijke reden
- vergeten dat lokale verbetering geen globale optimaliteit garandeert

## Verwante concepten
- [[Hill Climbing]]
- [[Hill Climbing Worked Example]]
- [[Heuristic]]
- [[h(n)]]

## Begripsafbakening en verbanden
- **Kernonderscheid:** deze implementatie toont lokale buurselectie zonder open lijst; dat is het wezenlijke verschil met frontier-search.
- **Veelvoorkomende misvatting:** denken dat `Hill Climbing` gewoon `Greedy` zonder `Priority Queue` is; de zoekruimte wordt hier fundamenteel anders behandeld.
- **Link met andere concepten:** [[Hill Climbing]], [[Hill Climbing Worked Example]], [[Heuristic]], [[h(n)]], [[Greedy Best-First Search]], [[Hill Climbing vs Greedy Best-First Search]]

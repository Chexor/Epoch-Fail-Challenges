---
type: concept-topic
domain: "artificial-intelligence"
parent: Blind Search
related:
  - Breadth-First Search (BFS)
  - Blind Search
  - Iterative Deepening Search (IDS)
  - DFS Worked Example
theme: "uninformed-search-strategies"
aliases:
  - Depth-First Search (DFS)
---

# Depth-First Search (DFS)
#concept #ai

Depth-First Search (DFS) is een zoekalgoritme dat eerst 1 pad zo diep mogelijk volgt voor het terugkeert naar eerdere vertakkingen.

## Korte kern

- gebruikt een [[Stack]] (`LIFO`) of recursie
- zoekt eerst diep, pas daarna breed
- gebruikt weinig geheugen, maar is niet optimaal

## 1. Wat is het kernprobleem?
Hoe zoek je snel met weinig geheugen door eerst een pad zo diep mogelijk te volgen?

## 2. Intuitieve uitleg
`DFS` kiest een tak en volgt die zo diep mogelijk. Pas wanneer die tak stopt of faalt, keert het terug naar een vorige vertakking.

## 3. Formele structuur
- gebruikt een [[Stack]] (`LIFO`) of recursie
- kiest de diepste open node
- gebruikt weinig geheugen
- is in het algemeen niet compleet
- is niet optimaal

## 4. Snelle vergelijking

- [[Depth-First Search (DFS)]] = volgt 1 tak zo diep mogelijk
- [[Breadth-First Search (BFS)]] = onderzoekt eerst alle ondiepe paden
- [[Iterative Deepening Search (IDS)]] = combineert DFS-achtig geheugengebruik met BFS-achtige veiligheid

## 5. Toepassing
`DFS` is nuttig als geheugen schaars is of als een oplossing mogelijk diep zit en je snel een eerste oplossing wil proberen te vinden.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** `DFS` is geheugenarm, maar geeft geen garantie op de beste of zelfs een tijdige oplossing.
- **Veelvoorkomende misvatting:** denken dat snel een doel bereiken automatisch betekent dat de gevonden oplossing goed is.
- **Link met andere concepten:** [[Search Algorithm]], [[Breadth-First Search (BFS)]], [[Depth-Limited Search (DLS)]], [[Iterative Deepening Search (IDS)]], [[Hill Climbing]], [[Frontier]], [[Explored Set]], [[Stack]], [[BFS vs DFS vs UCS vs Greedy vs A-star|BFS vs DFS vs UCS vs Greedy vs A*]], [[Tree Search vs Graph Search]]
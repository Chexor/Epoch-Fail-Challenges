---
type: concept-topic
domain: "artificial-intelligence"
parent: Heuristic Search
related:
  - Hill Climbing
  - A-star Search
  - Heuristic Search
  - Greedy Best-First Search Worked Example
theme: "heuristic-search"
aliases:
  - Greedy Best-First Search
---

# Greedy Best-First Search
#concept #ai

## 1. Wat is het kernprobleem?
Hoe stuur je search zo snel mogelijk richting doel op basis van een heuristische schatting?

## 2. Intuitieve uitleg
`Greedy Best-First Search` kiest altijd de frontier-node die het dichtst bij het doel lijkt. Het denkt dus vooral: "welke optie ziet er nu het meest veelbelovend uit?"

## 3. Formele structuur
- gebruikt een [[Priority Queue]]
- kiest de laagste `h(n)`
- kijkt niet naar de al gemaakte kost `g(n)`
- is vaak snel
- is niet optimaal
- is niet algemeen betrouwbaar compleet

## 4. Toepassing
Als de heuristiek heel informatief is, kan `Greedy` snel naar een doel leiden. Maar het kan ook misleid worden door een node die dichtbij lijkt, maar via een duur of slecht pad bereikbaar is.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** `Greedy` gebruikt alleen `h(n)` en negeert de reeds gemaakte kost.
- **Veelvoorkomende misvatting:** denken dat een lage `h(n)` automatisch een goed totaal pad betekent.
- **Link met andere concepten:** [[Heuristiek]], [[A-star Search|A* Search]], [[Hill Climbing]], [[Uniform-Cost Search (UCS)]], [[Frontier]], [[Priority Queue]], [[BFS vs DFS vs UCS vs Greedy vs A-star|BFS vs DFS vs UCS vs Greedy vs A*]], [[Hill Climbing vs Greedy Best-First Search]]
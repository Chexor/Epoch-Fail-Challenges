---
type: concept-topic
domain: "artificial-intelligence"
parent: Heuristic Search
related:
  - A-star Search
  - Heuristic Search
  - Iterative Deepening Search (IDS)
theme: "informed-optimal-search"
aliases:
  - IDA* (Iterative Deepening A*)
---

# IDA* (Iterative Deepening A*)
#concept #ai

## 1. Wat is het kernprobleem?
Hoe behoud je de optimaliteit van `A* Search` zonder de grote geheugenkost van een volledige priority queue?

## 2. Intuitieve uitleg
`IDA*` probeert het beste van twee werelden te combineren:

- de slimme evaluatie van [[A-star Search|A* Search]]
- het lage geheugengebruik van [[Depth-First Search (DFS)]]

In plaats van alle frontier-nodes bij te houden, zoekt IDA* depth-first binnen een grens op de `f`-waarde.

## 3. Formele structuur
- gebruikt `f(n) = g(n) + h(n)` zoals [[A-star Search|A* Search]]
- werkt depth-first zoals [[Depth-First Search (DFS)]]
- gebruikt geen dieptelimiet, maar een limiet op [[f(n)]]
- verhoogt die limiet iteratief wanneer geen oplossing gevonden wordt
- gebruikt veel minder geheugen dan A*
- kan wel vaker dezelfde nodes opnieuw bezoeken

## 4. Toepassing
Stel dat de beginlimiet `f = 8` is.

- alle paden met `f <= 8` worden depth-first onderzocht
- een pad met `f = 10` wordt niet verder uitgewerkt
- de kleinste overschrijding, bijvoorbeeld `10`, wordt de nieuwe limiet

Daarna start het algoritme opnieuw met limiet `10`.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** IDA* gebruikt dezelfde evaluatiefunctie als A*, maar niet dezelfde frontier-structuur.
- **Veelvoorkomende misvatting:** denken dat IDA* gewoon `IDS` met heuristiek is, zonder te begrijpen dat de limiet op [[f(n)]] ligt en niet op diepte.
- **Link met andere concepten:** [[A-star Search|A* Search]], [[Iterative Deepening Search (IDS)]], [[Depth-First Search (DFS)]], [[Heuristiek]], [[g(n)]], [[h(n)]], [[f(n)]], [[Admissible Heuristic]], [[Consistent Heuristic]]
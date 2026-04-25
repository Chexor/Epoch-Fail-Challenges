---
type: theory
domain: "artificial-intelligence"
parent: Heuristic Search
related:
  - A-star Search
  - Heuristic Search
  - Iterative Deepening Search (IDS)
  - f(n)
  - IDA-star Python Worked Example
theme: "informed-optimal-search"
aliases:
  - IDA* (Iterative Deepening A*)
---

# IDA* (Iterative Deepening A*)
#concept #ai

IDA* (Iterative Deepening A*) is een zoekalgoritme dat de evaluatiefunctie van `A*` combineert met depth-first zoeken binnen een iteratief stijgende grens op `f(n)`.

## Korte kern

- gebruikt `f(n) = g(n) + h(n)` zoals `A*`
- zoekt depth-first zoals `DFS`
- verlaagt geheugengebruik door een `f`-grens iteratief te verhogen

## Probleem

Hoe behoud je de optimaliteit van `A* Search` zonder de grote geheugenkost van een volledige priority queue?

## Intuïtie

`IDA*` probeert het beste van twee werelden te combineren:

- de slimme evaluatie van [[A-star Search]]
- het lage geheugengebruik van [[Depth-First Search (DFS)]]

In plaats van alle frontier-nodes bij te houden, zoekt IDA* depth-first binnen een grens op de `f`-waarde.

## Toepassing

Stel dat de beginlimiet `f = 8` is.

- alle paden met `f <= 8` worden depth-first onderzocht
- een pad met `f = 10` wordt niet verder uitgewerkt
- de kleinste overschrijding, bijvoorbeeld `10`, wordt de nieuwe limiet

Daarna start het algoritme opnieuw met limiet `10`.

Kort Python-voorbeeld met een gewogen adjacency dict:

```python
def ida_star_threshold(cost, heuristic_value):
    return cost + heuristic_value
```

Voor een grotere code-uitwerking, zie [[IDA-star Python Worked Example]].

## Formeel

- gebruikt `f(n) = g(n) + h(n)` zoals [[A-star Search]]
- werkt depth-first zoals [[Depth-First Search (DFS)]]
- gebruikt geen dieptelimiet, maar een limiet op [[f(n)]]
- verhoogt die limiet iteratief wanneer geen oplossing gevonden wordt
- gebruikt veel minder geheugen dan A*
- kan wel vaker dezelfde nodes opnieuw bezoeken

## Verbanden

> **Valkuil:** denken dat IDA* gewoon `IDS` met heuristiek is, zonder te begrijpen dat de limiet op [[f(n)]] ligt en niet op diepte.

- [[A-star Search]]
- [[Iterative Deepening Search (IDS)]]
- [[Depth-First Search (DFS)]]
- [[Heuristic]]
- [[g(n)]]

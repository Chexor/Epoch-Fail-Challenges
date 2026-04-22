---
type: theory
domain: "artificial-intelligence"
parent:
  - "[[Heuristic Search Algorithms]]"
  - "[[Optimal Search Algorithms]]"
related:
  - Greedy Best-First Search
  - Uniform-Cost Search (UCS)
  - Heuristic Search
  - Search Evaluation Functions
  - A-star Worked Example
  - A-star Python Worked Example
theme: "informed-optimal-search"
aliases:
  - A* Search
---

# A* Search
#concept #ai

A* Search is een heuristisch zoekalgoritme dat de echte kost tot nu toe combineert met een schatting van de resterende kost om het meest veelbelovende pad te kiezen.

## Korte kern

- gebruikt [[f(n)]] met `f(n) = g(n) + h(n)`
- combineert voorzichtig zoeken en doelgericht zoeken
- kan optimaal zijn als de heuristiek goed gekozen is

## Probleem

Hoe vind je een pad dat tegelijk doelgericht zoekt en toch de goedkoopste oplossing kan garanderen?

## Intuïtie

`A* Search` combineert twee soorten informatie:

- wat het al gekost heeft om hier te geraken
- wat nog geschat wordt tot aan het doel

Daardoor zoekt A* niet blind, maar ook niet roekeloos. Het kiest telkens het pad dat er in totaal het meest veelbelovend uitziet.

## Toepassing

Stel dat je van stad `A` naar stad `G` zoekt.

- Een pad naar `B` heeft `g=3` en `h=4`, dus `f=7`.
- Een pad naar `C` heeft `g=5` en `h=1`, dus `f=6`.

A* kiest dan eerst het pad naar `C`, omdat de totale verwachte kost lager is.

Kort Python-voorbeeld met een gewogen adjacency dict:

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
```

Voor een volledige Python-uitwerking, zie [[A-star Python Worked Example]].

## Formeel

- gebruikt een [[Priority Queue]]
- kiest de frontier-node met laagste [[f(n)]]
- [[f(n)]] wordt berekend als `g(n) + h(n)`
- [[g(n)]] = echte kost vanaf de start
- [[h(n)]] = geschatte resterende kost tot het doel
- is optimaal als de heuristiek [[Admissible Heuristic|admissible]] is
- bij `graph search` is [[Consistent Heuristic|consistentie]] belangrijk

## Verbanden

> **Valkuil:** denken dat A* hetzelfde is als `Greedy`, terwijl `Greedy` alleen [[h(n)]] gebruikt.

- [[Search Algorithm]]
- [[Frontier]]
- [[Explored Set]]
- [[Priority Queue]]
- [[Uniform-Cost Search (UCS)]]

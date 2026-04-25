---
type: theory
domain: "artificial-intelligence"
parent: Heuristic Properties
related:
  - Consistent Heuristic
  - Heuristic Properties
  - A-star Search
  - Admissible vs Consistent Heuristic
theme: "heuristic-properties-for-a-star"
aliases:
  - Admissible Heuristic
---

# Admissible Heuristic
#concept #ai

Een admissible heuristic is een heuristiek die de echte minimale resterende kost nooit overschat en daardoor de optimaliteit van [[A-star Search]] kan ondersteunen.

## Korte kern

- een admissible heuristiek is altijd **optimistisch**
- ze mag onderschatten, maar niet overschatten
- belangrijk voor optimale oplossingen bij [[A-star Search]]

## Probleem

Wanneer mag je een heuristiek vertrouwen om de optimale oplossing van `A*` niet kapot te maken?

## Intuïtie

Een heuristiek is `admissible` als ze optimistisch blijft. Ze mag de echte resterende kost onderschatten, maar nooit overschatten.

## Toepassing

Bij routeplanning is hemelsbrede afstand vaak `admissible` als je op de echte weg nooit korter kan reizen dan in een rechte lijn.

## Formeel

- Een heuristiek `h(n)` is `admissible` als voor elke node geldt:
  - `h(n) <= h*(n)`
- Hierbij is `h*(n)` de echte minimale kost van `n` naar het doel.
- Deze eigenschap is belangrijk voor de optimaliteit van `A*`.

## Verbanden

> **Valkuil:** denken dat een admissible heuristiek exact moet zijn.

- [[Heuristic]]
- [[A-star Search]]
- [[Consistent Heuristic]]
- [[Admissible vs Consistent Heuristic]]

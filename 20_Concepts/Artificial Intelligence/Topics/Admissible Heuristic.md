---
type: concept-topic
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

Een admissible heuristic is een heuristiek die de echte minimale resterende kost nooit overschat en daardoor de optimaliteit van [[A-star Search|A* Search]] kan ondersteunen.

## Korte kern

- een admissible heuristiek is altijd **optimistisch**
- ze mag onderschatten, maar niet overschatten
- belangrijk voor optimale oplossingen bij [[A-star Search|A* Search]]

## 1. Wat is het kernprobleem?
Wanneer mag je een heuristiek vertrouwen om de optimale oplossing van `A*` niet kapot te maken?

## 2. Intuitieve uitleg
Een heuristiek is `admissible` als ze optimistisch blijft. Ze mag de echte resterende kost onderschatten, maar nooit overschatten.

## 3. Formele structuur
- Een heuristiek `h(n)` is `admissible` als voor elke node geldt:
  - `h(n) <= h*(n)`
- Hierbij is `h*(n)` de echte minimale kost van `n` naar het doel.
- Deze eigenschap is belangrijk voor de optimaliteit van `A*`.

## 4. Snelle vergelijking

- [[Admissible Heuristic]] = overschat nooit de echte resterende kost
- [[Consistent Heuristic]] = respecteert ook lokale samenhang tussen verbonden nodes
- consistent impliceert admissible, maar niet omgekeerd

## 5. Toepassing
Bij routeplanning is hemelsbrede afstand vaak `admissible` als je op de echte weg nooit korter kan reizen dan in een rechte lijn.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** een `admissible` heuristiek mag onderschatten, maar nooit overschatten.
- **Veelvoorkomende misvatting:** denken dat een admissible heuristiek exact moet zijn.
- **Link met andere concepten:** [[Heuristiek]], [[A-star Search|A* Search]], [[Consistent Heuristic]], [[Admissible vs Consistent Heuristic]]
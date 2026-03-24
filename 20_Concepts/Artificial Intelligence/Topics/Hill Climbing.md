---
type: concept-topic
domain: "artificial-intelligence"
parent: Heuristic Search
related:
  - Greedy Best-First Search
  - Heuristic Search
  - Hill Climbing Worked Example
theme: "heuristic-search"
aliases:
  - Hill Climbing
---

# Hill Climbing
#concept #ai

## 1. Wat is het kernprobleem?
Hoe verbeter je snel een huidige toestand op basis van lokale informatie, zonder de volledige zoekruimte open te houden?

## 2. Intuitieve uitleg
`Hill Climbing` kijkt alleen naar de huidige node en haar directe buren. Het kiest telkens de buur die er volgens de heuristiek het best uitziet.

## 3. Formele structuur
- gebruikt een `heuristiek`
- bewaart meestal alleen de huidige toestand en haar buren
- kiest lokaal de beste buur
- is niet compleet
- is niet optimaal
- kan vastlopen in een `local optimum`, `plateau` of `ridge`

## 4. Toepassing
Bij een optimalisatieprobleem kan `Hill Climbing` snel een redelijke oplossing vinden, maar niet noodzakelijk de globale beste.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** `Hill Climbing` is lokale optimalisatie, geen volwaardige frontier-search.
- **Veelvoorkomende misvatting:** `Hill Climbing` verwarren met `Greedy Best-First Search` omdat beide een heuristiek gebruiken.
- **Link met andere concepten:** [[Heuristiek]], [[Greedy Best-First Search]], [[A-star Search|A* Search]], [[Hill Climbing vs Greedy Best-First Search]]
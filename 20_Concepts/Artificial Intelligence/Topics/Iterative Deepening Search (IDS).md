---
type: concept-topic
domain: "artificial-intelligence"
parent: Blind Search
related:
  - Depth-First Search (DFS)
  - Depth-Limited Search (DLS)
  - Blind Search
  - IDS Worked Example
theme: "uninformed-search-strategies"
aliases:
  - Iterative Deepening Search (IDS)
---

# Iterative Deepening Search (IDS)
#concept #ai

Iterative Deepening Search (IDS) is een zoekalgoritme dat herhaaldelijk depth-limited search uitvoert met steeds grotere dieptelimiet tot een oplossing gevonden wordt.

## Korte kern

- herhaalt [[Depth-Limited Search (DLS)]] met limieten `0, 1, 2, ...`
- combineert weinig geheugengebruik met systematisch zoeken
- optimaal bij gelijke stapkosten

## 1. Wat is het kernprobleem?
Hoe combineer je het lage geheugengebruik van `DFS` met de volledigheid van `BFS`?

## 2. Intuitieve uitleg
`IDS` voert meerdere rondes van `DLS` uit. Eerst zoek je tot diepte `0`, dan `1`, dan `2`, enzovoort, tot een oplossing gevonden wordt.

## 3. Formele structuur
- herhaalt `Depth-Limited Search`
- verhoogt de limiet stapsgewijs
- is compleet
- is optimaal bij gelijke stapkosten
- gebruikt weinig geheugen

## 4. Snelle vergelijking

- [[Iterative Deepening Search (IDS)]] = DFS in herhaalde rondes met grotere limiet
- [[Depth-First Search (DFS)]] = 1 dieptezoektocht zonder systematische limietverhoging
- [[Breadth-First Search (BFS)]] = laag per laag met hoger geheugengebruik

## 5. Toepassing
`IDS` is nuttig wanneer je niet weet hoe diep de oplossing zit, maar wel de ondiepste oplossing wil vinden zonder het geheugenverbruik van `BFS`.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** `IDS` combineert dieptegebaseerd zoeken met systematische uitbreiding per limiet.
- **Veelvoorkomende misvatting:** denken dat het herhalen van bovenste niveaus altijd onaanvaardbaar duur is.
- **Link met andere concepten:** [[Depth-First Search (DFS)]], [[Depth-Limited Search (DLS)]], [[Breadth-First Search (BFS)]], [[Search Algorithm]]
---
type: atlas
domain: "artificial-intelligence"
parent: [[00_Overzicht Artificial Intelligence]]
related:
  - State Space
  - Search Algorithm
theme: "ai-search"
aliases:
  - Atlas Zoekalgoritmen
---

# Atlas - Zoekalgoritmen
#concept #ai

Atlas-note voor het domein van zoekalgoritmen binnen AI.

> Deze note ordent zoekalgoritmen als conceptfamilie en helpt de structuur en onderlinge verbanden tussen blind, heuristisch en optimaal zoeken te begrijpen.

## Korte kern

- ordent zoekalgoritmen (Blind, Heuristisch, Optimaal)
- helpt de structuur en onderlinge verbanden te begrijpen
- dient als navigatiepunt voor alle zoekalgoritme-gerelateerde notes

## Waarom bestaat deze conceptgroep?
Zoekalgoritmen vormen de kern van klassieke AI: het systematisch doorzoeken van een toestandruimte om een doeltoestand te vinden onder specifieke restricties (kosten, tijd, geheugen).

## Groot plaatje
Zoeken is de fundamentele methode om problemen te abstraheren tot toestanden en overgangen, waarbij we vervolgens methodisch navigeren van start naar doel.

## Kernonderdelen

### Zoekfamilies
- [[Blind Search Algorithms]]
- [[Heuristic Search Algorithms]]
- [[Optimal Search Algorithms]]

### Algoritmen per Familie

- **Blind Search:**
    - [[Breadth-First Search (BFS)]]
    - [[Depth-First Search (DFS)]]
    - [[Depth-Limited Search (DLS)]]
    - [[Iterative Deepening Search (IDS)]]
    - [[Non-deterministic Search]]
- **Heuristic Search:**
    - [[Greedy Search]]
        - [[Greedy Best-First Search]]
    - [[Hill Climbing]]
    - [[Beam Search]]
- **Optimal Search:**
    - [[Uniform-Cost Search (UCS)]]
    - [[A-star Search]]

### Conceptuele bouwstenen
- [[State Space]]
- [[Search Algorithm]]
- [[Frontier]]
- [[Explored Set]]
- [[Heuristic]]
- [[Admissible Heuristic]]
- [[Consistent Heuristic]]

## Hoe hangen deze samen?
De opbouw verloopt van ongeïnformeerd zoeken (blind) naar geïnformeerd zoeken (heuristisch), met toenemende complexiteit in hoe kosten en heuristieken worden meegewogen (g(n) vs h(n) vs f(n)).

## Aanbevolen leerpad
1.  **De basis:** [[State Space]] & [[Search Algorithm]]
2.  **Blind zoeken:** [[Blind Search Algorithms]]
    -   Start met [[Breadth-First Search (BFS)]] en [[Depth-First Search (DFS)]] om de basis te begrijpen.
    -   Begrijp de verbeteringen met [[Iterative Deepening Search (IDS)]].
3.  **Heuristisch zoeken:** [[Heuristic Search Algorithms]]
    -   Snap het kernidee met [[Greedy Search]].
    -   Zie de toepassing in [[Greedy Best-First Search]].
4.  **Optimaal zoeken:** [[Optimal Search Algorithms]]
    -   Start met [[Uniform-Cost Search (UCS)]] om kosten te begrijpen.
    -   Combineer alles met [[A-star Search]].

## Verwante concepten
- [[00_Overzicht Machine Learning Concepten]] (de andere grote tak in deze AI-module)

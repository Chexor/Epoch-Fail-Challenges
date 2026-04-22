---
type: theory
domain: "artificial-intelligence"
parent:
  - "[[Search Algorithm]]"
related:
  - "[[Depth-First Search (DFS)]]"
  - "[[Breadth-First Search (BFS)]]"
  - "[[Non-deterministic Search]]"
  - "[[Iterative Deepening Search (IDS)]]"
theme: "ai-search"
aliases:
  - Blind Search
  - Uninformed Search
---

# Blind Search Algorithms
#concept #ai

Blind Search Algorithms (ook wel Uninformed Search) zijn een klasse van zoekalgoritmes die geen enkele domeinspecifieke kennis gebruiken om de zoekruimte te verkennen; ze volgen een vooraf bepaalde strategie zonder te weten hoe "dicht" een state bij het doel is.

## Korte kern

-   Gebruikt geen informatie over de "kwaliteit" van een state.
-   Verkennen de state space op een systematische, maar "domme" manier.
-   Fundamenteel voor het begrijpen van meer geavanceerde zoekmethodes.
-   Voorbeelden: BFS, DFS, DLS, IDS.

## Probleem

Hoe kun je een doel vinden in een state space als je geen enkele informatie hebt over waar het doel zich zou kunnen bevinden?

## Intuïtie

Stel je voor dat je in een doolhof bent en geen kaart hebt. Je kunt geen "goede" of "slechte" paden inschatten. Je enige optie is om een simpele regel te volgen, zoals "houd altijd je rechterhand tegen de muur" (analoog aan DFS) of "verken eerst alle gangen die één stap ver zijn, dan twee stappen, etc." (analoog aan BFS). Dit is de essentie van blind zoeken: systematisch en onwetend.

## Formeel

Blind search algoritmes onderscheiden zich enkel door de volgorde waarin ze nodes uit de [[Frontier]] expanderen.

-   **Strategie:** De keuze van de datastructuur voor de frontier bepaalt het algoritme (FIFO Queue voor BFS, LIFO Stack voor DFS).
-   **Informatie:** Gebruikt alleen de informatie uit de probleemdefinitie zelf (states, actions, initial state, goal test).
-   **Performance Metrics:** Geëvalueerd op basis van volledigheid (vindt het altijd een oplossing?), optimaliteit (vindt het de beste oplossing?), tijdcomplexiteit en ruimtecomplexiteit.

## Specifieke Algoritmes

-   **[[Breadth-First Search (BFS)]]:** Verkent de state space laag voor laag. Gebruikt een FIFO queue.
-   **[[Depth-First Search (DFS)]]:** Verkent een pad zo diep mogelijk voordat het terugkeert (backtracking). Gebruikt een LIFO stack.
-   **[[Depth-Limited Search (DLS)]]:** Een variant van DFS met een vooraf bepaalde dieptelimiet.
-   **[[Iterative Deepening Search (IDS)]]:** Combineert de voordelen van BFS en DFS door herhaaldelijk DLS uit te voeren met een toenemende dieptelimiet.
-   **[[Non-deterministic Search]]**: Verkent paden in een omgeving waar de uitkomst van een actie niet vastligt.

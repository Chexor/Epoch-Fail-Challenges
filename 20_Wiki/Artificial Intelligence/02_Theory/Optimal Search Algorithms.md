---
type: theory
domain: "artificial-intelligence"
parent:
  - "[[Search Algorithm]]"
related:
  - "[[Uniform-Cost Search (UCS)]]"
  - "[[A-star Search]]"
theme: "ai-search"
aliases:
  - Optimal Search
---

# Optimal Search Algorithms
#concept #ai

Optimal Search Algorithms zijn een klasse van zoekalgoritmes die garanderen dat ze de best mogelijke oplossing (meestal het pad met de laagste kost) vinden, mits een oplossing bestaat.

## Korte kern

-   Garandeert het vinden van de goedkoopste oplossing.
-   Houdt rekening met de cumulatieve kost van een pad.
-   Voorbeelden: Uniform-Cost Search (UCS), A* Search.

## Probleem

Hoe vind je niet zomaar *een* oplossing, maar gegarandeerd de *beste* oplossing, bijvoorbeeld de kortste route op een kaart of de goedkoopste manier om een taak uit te voeren?

## Intuïtie

Als je een route plant van A naar B, wil je niet de route met de minste bochten (wat een blind algoritme zou kunnen doen) of de route die het snelst in de juiste richting lijkt te gaan (wat een puur heuristisch algoritme zou doen). Je wilt de route die in totaal de minste kilometers heeft. Een optimaal algoritme weegt systematisch alle opties af op basis van hun totale kost en kiest nooit een pad dat duurder is dan een ander bekend pad, totdat het zeker weet dat de gevonden oplossing de goedkoopste is.

## Formeel

Optimale algoritmes houden de cumulatieve padkost `g(n)` bij. De strategie is om altijd de node in de [[Frontier]] te expanderen die de laagste `g(n)` heeft (of `f(n)` in het geval van A*).

-   **[[Uniform-Cost Search (UCS)]]:** Is optimaal door altijd de node met de laagste padkost `g(n)` te kiezen. Het is in feite Dijkstra's algoritme. `f(n) = g(n)`.
-   **[[A-star Search]]:** Is optimaal als de gebruikte heuristiek `h(n)` [[Admissible Heuristic|admissible]] is (nooit de werkelijke kost overschat). Het combineert de zekerheid van UCS met de snelheid van een heuristiek. `f(n) = g(n) + h(n)`.

## Relatie met andere zoektypes

-   **Blind Search:** Algoritmes zoals [[Breadth-First Search (BFS)]] zijn optimaal als alle stapkosten gelijk zijn, maar falen als de kosten variëren.
-   **Heuristic Search:** Algoritmes zoals [[Greedy Search]] zijn doorgaans niet optimaal omdat ze de padkost `g(n)` negeren.

De sleutel tot optimaliteit is het balanceren van de reeds gemaakte investering (`g(n)`) met de potentie voor de toekomst (`h(n)`), of, bij afwezigheid van een heuristiek, het rigoureus prioriteren van de laagste investering.

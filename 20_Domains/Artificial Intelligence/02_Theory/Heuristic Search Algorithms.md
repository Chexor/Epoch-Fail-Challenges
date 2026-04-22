---
type: theory
domain: "artificial-intelligence"
parent:
  - "[[Search Algorithm]]"
related:
  - "[[Hill Climbing]]"
  - "[[Beam Search]]"
  - "[[Greedy Search]]"
  - "[[A-star Search]]"
theme: "ai-search"
aliases:
  - Heuristic Search
  - Informed Search
---

# Heuristic Search Algorithms
#concept #ai

Heuristic Search Algorithms (ook wel Informed Search) zijn een klasse van zoekalgoritmes die domeinspecifieke kennis in de vorm van een heuristiek gebruiken om de zoektocht efficiënt naar veelbelovende gebieden van de state space te sturen.

## Korte kern

-   Gebruikt een [[Heuristic]] (h(n)) om de "afstand" tot het doel te schatten.
-   Stuurt de zoektocht naar nodes die dichter bij het doel lijken te zijn.
-   Is over het algemeen veel efficiënter dan [[Blind Search Algorithms]].
-   Voorbeelden: Greedy Search, A* Search, Hill Climbing.

## Probleem

Hoe kunnen we de zoektocht in een grote state space versnellen door gebruik te maken van een "educated guess" of "vuistregel"?

## Intuïtie

Stel je voor dat je de weg zoekt naar een hoge toren die je in de verte kunt zien. In plaats van willekeurig straten in te slaan (blind search), kies je bij elke kruising de straat die je gevoelsmatig het dichtst bij de toren brengt. Die "gevoelsmatige inschatting" is je heuristiek. Het is niet altijd perfect—een straat kan een doodlopende weg zijn—maar het is veel slimmer dan blind gokken.

## Formeel

Heuristische algoritmes gebruiken een evaluatiefunctie `f(n)` om de nodes in de [[Frontier]] te ordenen. De samenstelling van deze functie bepaalt het specifieke algoritme. De kerncomponent is de heuristische functie `h(n)`.

-   **Heuristische Functie (h(n)):** Een schatting van de kost van de goedkoopste weg van node `n` naar het doel.
-   **Strategie:** De [[Priority Queue]] wordt meestal gebruikt voor de frontier, geordend op basis van de evaluatiefunctie.

## Specifieke Algoritmes

-   **[[Greedy Search]] (specifiek [[Greedy Best-First Search]]):** Kiest de node met de laagste `h(n)`. Is snel, maar negeert de reeds afgelegde kost en is daardoor niet optimaal. `f(n) = h(n)`.
-   **[[A-star Search]]:** Combineert de afgelegde kost `g(n)` met de heuristische schatting `h(n)`. Is optimaal als de heuristiek [[Admissible Heuristic|admissible]] is. `f(n) = g(n) + h(n)`.
-   **[[Hill Climbing]]:** Een lokale zoektechniek die geen pad onthoudt, maar telkens de buur kiest die de beste verbetering biedt. Kan vastlopen in lokale optima.
-   **[[Beam Search]]:** Een variant van Best-First search die op elk niveau slechts een beperkt aantal (`k`) beste kandidaten onthoudt om geheugengebruik te beperken.

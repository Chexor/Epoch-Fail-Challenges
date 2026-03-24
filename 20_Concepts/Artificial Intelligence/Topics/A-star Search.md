---
type: concept-topic
domain: "artificial-intelligence"
parent: Heuristic Search
related:
  - Greedy Best-First Search
  - Uniform-Cost Search (UCS)
  - Heuristic Search
  - Search Evaluation Functions
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

## 1. Wat is het kernprobleem?
Hoe vind je een pad dat tegelijk doelgericht zoekt en toch de goedkoopste oplossing kan garanderen?

## 2. Intuitieve uitleg
`A* Search` combineert twee soorten informatie:

- wat het al gekost heeft om hier te geraken
- wat nog geschat wordt tot aan het doel

Daardoor zoekt A* niet blind, maar ook niet roekeloos. Het kiest telkens het pad dat er in totaal het meest veelbelovend uitziet.

## 3. Formele structuur
- gebruikt een [[Priority Queue]]
- kiest de frontier-node met laagste [[f(n)]]
- [[f(n)]] wordt berekend als `g(n) + h(n)`
- [[g(n)]] = echte kost vanaf de start
- [[h(n)]] = geschatte resterende kost tot het doel
- is optimaal als de heuristiek [[Admissible Heuristic|admissible]] is
- bij `graph search` is [[Consistent Heuristic|consistentie]] belangrijk

## 4. Snelle vergelijking

- [[Uniform-Cost Search (UCS)]] = kiest alleen op [[g(n)]]
- [[Greedy Best-First Search]] = kiest alleen op [[h(n)]]
- [[A-star Search|A* Search]] = kiest op [[g(n)]] + [[h(n)]] via [[f(n)]]

## 5. Toepassing
Stel dat je van stad `A` naar stad `G` zoekt.

- Een pad naar `B` heeft `g=3` en `h=4`, dus `f=7`.
- Een pad naar `C` heeft `g=5` en `h=1`, dus `f=6`.

A* kiest dan eerst het pad naar `C`, omdat de totale verwachte kost lager is.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** A* gebruikt zowel de reeds gemaakte kost als de geschatte resterende kost.
- **Veelvoorkomende misvatting:** denken dat A* hetzelfde is als `Greedy`, terwijl `Greedy` alleen [[h(n)]] gebruikt.
- **Link met andere concepten:** [[Search Algorithm]], [[Frontier]], [[Explored Set]], [[Priority Queue]], [[Uniform-Cost Search (UCS)]], [[Greedy Best-First Search]], [[Heuristiek]], [[g(n)]], [[h(n)]], [[f(n)]], [[Admissible Heuristic]], [[Consistent Heuristic]], [[Tree Search vs Graph Search]], [[Admissible vs Consistent Heuristic]]

---
type: theory
domain: "artificial-intelligence"
parent: Artificial Intelligence (AI)
related:
  - Artificial Intelligence (AI)
  - State Space
  - AI Search Techniques
  - Frontier
  - Blind Search
  - Cost-Based Search
  - Heuristic Search
theme: "ai-basics-and-search"
aliases:
  - Search Algorithm
---

# Search Algorithm
#concept #ai

Een search algorithm is een procedure die stap voor stap beslist welke toestand of welk pad vervolgens onderzocht wordt binnen een state space.

## Korte kern

- een search algorithm bepaalt de zoekvolgorde in een probleemruimte
- de keuzeregel en datastructuur bepalen snelheid, geheugen en kwaliteit
- verschillende algoritmes zoeken in dezelfde state space, maar gedragen zich anders

## Probleem

Hoe vind je systematisch een oplossing in een probleemruimte zonder zomaar willekeurig mogelijkheden uit te proberen?

## Intuïtie

Een `search algorithm` is een zoekstrategie die stap voor stap beslist welke toestand het daarna onderzoekt. Het algoritme doorloopt dus niet zomaar de volledige `state space`, maar volgt een bepaalde regel om gericht te zoeken.

Die regel bepaalt:

- welke node eerst bekeken wordt
- welke nodes nog wachten in de `frontier`
- of het algoritme snel een oplossing vindt
- of het ook de beste oplossing vindt

## Toepassing

Bij een routeprobleem van stad `A` naar stad `G` kan je verschillende zoekalgoritmes gebruiken.

- `BFS` zoekt eerst alle routes met 1 stap, dan 2 stappen, enzovoort.
- `UCS` kiest altijd eerst de route met de laagste totale afstand tot nu toe.
- `A*` gebruikt zowel de al afgelegde afstand als een schatting van de resterende afstand.

Het probleem blijft hetzelfde, maar het gekozen `search algorithm` bepaalt hoe efficiënt en hoe goed de oplossing is.

## Formeel

- Een `search algorithm` werkt op een `state space`.
- Het vertrekt van een `initial state`.
- Het houdt een verzameling bij van nog te onderzoeken nodes: de `frontier`.
- Het breidt telkens een gekozen node uit en genereert opvolgers.
- Het stopt wanneer een `goal state` gevonden is of wanneer er geen nodes meer over zijn.

Belangrijke onderdelen zijn:

- **[[Frontier]]**: nodes die ontdekt zijn maar nog niet geëxpandeerd
- **expansie**: het genereren van opvolgers van een node
- **keuzeregel**: de regel die bepaalt welke node uit de frontier genomen wordt
- **datastructuur**: vaak [[Queue]], [[Stack]] of [[Priority Queue]]

Typische zoekalgoritmes zijn:

- `BFS`: kiest op kleinste diepte
- `DFS`: kiest de diepste open node
- `UCS`: kiest laagste padkost `g(n)`
- `Greedy`: kiest laagste heuristiek `h(n)`
- `A*`: kiest laagste `f(n) = g(n) + h(n)`

Belangrijke eigenschappen om zoekalgoritmes te vergelijken:

- **compleetheid**: vindt het een oplossing als er een bestaat?
- **optimaliteit**: vindt het de beste oplossing?
- **tijdsefficientie**: hoeveel werk moet het doen?
- **geheugengebruik**: hoeveel nodes moet het onthouden?

## Verbanden

> **Valkuil:** denken dat alle zoekalgoritmes ongeveer hetzelfde werken omdat ze allemaal "een pad zoeken".

- [[State Space]]
- [[Artificial Intelligence (AI)]]
- [[Heuristic]]
- [[Graaf]]
- [[Frontier]]

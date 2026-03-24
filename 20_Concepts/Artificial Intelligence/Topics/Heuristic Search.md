---
type: concept-topic
domain: "artificial-intelligence"
parent: AI Search Techniques
related:
  - Blind Search
  - Cost-Based Search
  - Heuristiek
theme: "heuristic-search"
aliases:
  - Heuristic Search
---

# Heuristic Search
#concept #ai

Heuristic Search is een familie van zoekalgoritmes die heuristische schattingen gebruiken om gerichter naar een oplossing te zoeken.

## Korte kern

- gebruikt een [[Heuristiek]] om zoekkeuzes te sturen
- probeert efficiënter te zoeken dan blind search
- omvat onder meer [[Hill Climbing]], [[Greedy Best-First Search]] en [[A-star Search|A* Search]]

## 1. Wat is het kernprobleem?
Hoe kan je sneller door een zoekruimte bewegen wanneer je een bruikbare schatting van de resterende kost hebt?

## 2. Intuitieve uitleg
In plaats van alle mogelijkheden blind te bekijken, gebruikt heuristic search een extra aanwijzing over welke nodes waarschijnlijk dichter bij het doel liggen.

Die aanwijzing is niet perfect, maar helpt vaak om minder nutteloze paden te onderzoeken.

## 3. Formele structuur
Heuristic search gebruikt meestal een functie zoals [[h(n)]] of een combinatie zoals [[f(n)]].

Belangrijke algoritmes in deze familie:

- [[Hill Climbing]]
- [[Greedy Best-First Search]]
- [[A-star Search|A* Search]]
- [[IDA-star (Iterative Deepening A-star)|IDA* (Iterative Deepening A*)]]

Verwante subthema's zijn:

- [[Search Evaluation Functions]]
- [[Heuristic Properties]]

## 4. Snelle vergelijking

- [[Blind Search]] = geen heuristische schatting
- [[Cost-Based Search]] = echte kost staat centraal
- [[Heuristic Search]] = gebruikt schatting of combinatie van kost en schatting

## 5. Toepassing
Als je in een routeprobleem niet alleen de al gemaakte kost kent, maar ook een nuttige schatting naar het doel hebt, dan gebruik je de logica van heuristic search om sneller een goede oplossing te vinden.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** heuristic search gebruikt extra informatie over het doel om de zoektocht te sturen.
- **Veelvoorkomende misvatting:** denken dat elke heuristische methode automatisch optimaal is. Dat hangt af van het algoritme en de eigenschappen van de heuristiek.
- **Link met andere concepten:** [[AI Search Techniques]], [[Heuristiek]], [[Hill Climbing]], [[Greedy Best-First Search]], [[A-star Search|A* Search]], [[IDA-star (Iterative Deepening A-star)|IDA* (Iterative Deepening A*)]], [[Heuristic Properties]], [[Search Evaluation Functions]]

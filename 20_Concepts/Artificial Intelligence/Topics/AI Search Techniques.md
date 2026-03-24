---
type: concept-topic
domain: "artificial-intelligence"
parent: Search Algorithm
related:
  - Blind Search
  - Cost-Based Search
  - Heuristic Search
theme: "ai-basics-and-search"
aliases:
  - AI Search Techniques
---

# AI Search Techniques
#concept #ai

AI Search Techniques zijn de grote families van zoekmethodes waarmee een algoritme beslist welke node het daarna onderzoekt in een state space.

## Korte kern

- groepeert de belangrijkste zoekfamilies binnen AI
- helpt het verschil zien tussen blind, kost-gebaseerd en heuristisch zoeken
- vormt een inhoudelijke kapstok voor concrete zoekalgoritmes

## 1. Wat is het kernprobleem?
Hoe orden je verschillende zoekalgoritmes op een zinvolle manier zodat hun logica, sterktes en beperkingen duidelijk worden?

## 2. Intuitieve uitleg
Niet elk zoekalgoritme zoekt op dezelfde manier. Sommige zoeken blind en systematisch, andere houden rekening met kosten, en nog andere gebruiken heuristieken om gerichter naar het doel te zoeken.

`AI Search Techniques` is dus geen enkel algoritme, maar een overkoepelende noemer voor meerdere zoekstrategieën.

## 3. Formele structuur
Binnen deze familie vallen vooral drie belangrijke subgroepen:

- [[Blind Search]]
- [[Cost-Based Search]]
- [[Heuristic Search]]

Concrete algoritmes die daaronder vallen zijn onder andere:

- [[Breadth-First Search (BFS)]]
- [[Depth-First Search (DFS)]]
- [[Uniform-Cost Search (UCS)]]
- [[Greedy Best-First Search]]
- [[A-star Search|A* Search]]

## 4. Snelle vergelijking

- [[Blind Search]] = geen heuristische voorkennis
- [[Cost-Based Search]] = kiest op echte kost
- [[Heuristic Search]] = gebruikt een schatting om gerichter te zoeken

## 5. Toepassing
Wanneer je in een cursus meerdere zoekalgoritmes naast elkaar studeert, helpt deze note om ze eerst in families te plaatsen. Daardoor wordt sneller duidelijk waarom `BFS`, `UCS` en `A*` niet gewoon kleine varianten van elkaar zijn, maar echt een andere beslislogica volgen.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** dit is een paraplunote voor zoekfamilies, geen concreet zoekalgoritme.
- **Veelvoorkomende misvatting:** denken dat alle zoekalgoritmes gewoon losse technieken zijn zonder duidelijke familiebanden.
- **Link met andere concepten:** [[Search Algorithm]], [[Blind Search]], [[Cost-Based Search]], [[Heuristic Search]], [[BFS vs DFS vs UCS vs Greedy vs A-star|BFS vs DFS vs UCS vs Greedy vs A*]]

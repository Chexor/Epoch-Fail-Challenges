---
type: concept-map
domain: "artificial-intelligence"
parent:
related:
  - State Space
  - Search Algorithm
  - Machine Learning
theme: "ai-basics-and-search"
aliases:
  - Overzicht Artificial Intelligence
  - Artificial Intelligence
---

# Overzicht Artificial Intelligence
#concept #ai

## Doel van dit overzicht

Deze note groepeert de basisconcepten van AI als duurzame kenniskaart, met nadruk op `search`, heuristieken en de brug naar `machine learning`.

## Groot plaatje

In deze cursus vallen de AI-concepten in twee grote blokken uiteen:

- problemen modelleren en oplossingen zoeken in een `state space`
- patronen leren uit data via `machine learning`

Deze twee blokken delen eenzelfde ambitie: niet zomaar data verwerken, maar doelgericht intelligent gedrag modelleren.

## Centrale vragen

- Hoe stel je een probleem voor als een verzameling toestanden en overgangen?
- Hoe beslist een zoekalgoritme welke node het daarna onderzoekt?
- Wanneer gebruik je kosten, wanneer heuristieken, en wanneer beide?
- Hoe verschilt symbolisch probleemoplossen van leren uit data?

## 1. Basis van AI

- [[Artificial Intelligence (AI)]]
- [[State Space]]
- [[Search Algorithm]]
- [[AI Search Techniques]]
- [[Branching Factor]]
- [[Path Cost]]
- [[Frontier]]
- [[Explored Set]]

## 1.5 Zoekfamilies

- [[Blind Search]]
- [[Cost-Based Search]]
- [[Heuristic Search]]
- [[Search Evaluation Functions]]
- [[Heuristic Properties]]

## 2. Blind search

- [[Breadth-First Search (BFS)]]
- [[Depth-First Search (DFS)]]
- [[Uniform-Cost Search (UCS)]]
- [[Depth-Limited Search (DLS)]]
- [[Iterative Deepening Search (IDS)]]
- [[Bi-directional Search]]

## 3. Heuristic search

- [[Heuristiek]]
- [[g(n)]]
- [[h(n)]]
- [[f(n)]]
- [[Hill Climbing]]
- [[Greedy Best-First Search]]
- [[A-star Search|A* Search]]
- [[IDA-star (Iterative Deepening A-star)|IDA* (Iterative Deepening A*)]]
- [[Admissible Heuristic]]
- [[Consistent Heuristic]]

Binnen dit blok is er een duidelijke opbouw:

- [[Hill Climbing]] = puur lokaal zoeken
- [[Greedy Best-First Search]] = kiezen op basis van `h(n)`
- [[A-star Search|A* Search]] = kiezen op basis van `g(n) + h(n)`
- [[IDA-star (Iterative Deepening A-star)|IDA* (Iterative Deepening A*)]] = A* logica met veel lager geheugengebruik

## 3.5 Vergelijkingen

- [[BFS vs DFS vs UCS vs Greedy vs A-star|BFS vs DFS vs UCS vs Greedy vs A*]]
- [[Admissible vs Consistent Heuristic]]
- [[Hill Climbing vs Greedy Best-First Search]]
- [[BFS vs UCS]]
- [[Tree Search vs Graph Search]]

## 3.7 Uitgewerkte toepassingen

- [[BFS Worked Example]]
- [[DFS Worked Example]]
- [[UCS Worked Example]]
- [[Hill Climbing Worked Example]]
- [[Greedy Best-First Search Worked Example]]
- [[A-star Worked Example]]
- [[IDS Worked Example]]

Deze execution-notes tonen hoe je de algoritmes stap voor stap uitschrijft op een graaf, met focus op frontier, keuzeregel en eindpad.

## 4. Brug naar data-gedreven AI

- [[Machine Learning]]
- [[Deep Learning]]
- [[Neural Network]]
- [[Convolutional Neural Network (CNN)]]

## Hoe hangen deze groepen samen?

- [[State Space]] legt uit *wat* het probleemmodel is.
- [[Search Algorithm]] legt uit *hoe* je door dat model beweegt.
- [[Heuristiek]] legt uit *hoe* je die beweging gerichter maakt.
- [[A-star Search|A* Search]] toont hoe kosten en heuristiek gecombineerd worden.
- [[IDA-star (Iterative Deepening A-star)|IDA* (Iterative Deepening A*)]] toont hoe je diezelfde logica ruimte-efficiënter kunt maken.
- [[Machine Learning]] verschuift van expliciete zoekregels naar patroonleren uit data.
- [[Neural Network]] en [[Convolutional Neural Network (CNN)]] zijn gespecialiseerde modellen binnen die tweede familie.

## Verwante kennisdomeinen

- [[Graaf]] als structurele voorstelling van nodes en verbindingen
- [[00_Overzicht Machine Learning Concepten]] voor de data-gedreven tak

## Aanbevolen leerpad

1. [[Artificial Intelligence (AI)]]
2. [[State Space]]
3. [[Search Algorithm]]
4. [[Breadth-First Search (BFS)]] en [[Depth-First Search (DFS)]]
5. [[Uniform-Cost Search (UCS)]]
6. [[Heuristiek]], [[Greedy Best-First Search]], [[A-star Search|A* Search]]
7. [[IDA-star (Iterative Deepening A-star)|IDA* (Iterative Deepening A*)]], [[Admissible Heuristic]] en [[Consistent Heuristic]]
8. [[Machine Learning]], [[Neural Network]], [[Convolutional Neural Network (CNN)]]

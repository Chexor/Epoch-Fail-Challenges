---
type: concept-topic
domain: "artificial-intelligence"
parent: Blind Search
related:
  - Blind Search
  - Breadth-First Search (BFS)
  - State Space
theme: "uninformed-search-strategies"
aliases:
  - Bi-directional Search
---

# Bi-directional Search
#concept #ai

## 1. Wat is het kernprobleem?
Hoe verklein je de zoekdiepte door zowel vanuit de start als vanuit het doel te zoeken?

## 2. Intuitieve uitleg
In plaats van de volledige afstand van start naar doel in één richting af te leggen, laat je twee zoekfronten naar elkaar toe groeien. Ze ontmoeten elkaar hopelijk ongeveer in het midden.

## 3. Formele structuur
- gebruikt twee zoekprocessen
- één zoekt vooruit vanaf de start
- één zoekt achteruit vanaf het doel
- stopt wanneer beide frontiers elkaar raken
- kan de complexiteit reduceren van ongeveer `O(b^d)` naar `O(b^(d/2))`

## 4. Toepassing
Bij routeproblemen waarbij start en doel expliciet gekend zijn, kan `Bi-directional Search` veel sneller zijn dan een klassieke eenrichtingszoektocht.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** `Bi-directional Search` vermindert zoekdiepte door twee frontiers naar elkaar toe te laten werken.
- **Veelvoorkomende misvatting:** vergeten dat achterwaarts zoeken of een omgekeerde probleemrepresentatie mogelijk moet zijn.
- **Link met andere concepten:** [[Branching Factor]], [[State Space]], [[Search Algorithm]]
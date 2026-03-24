---
type: concept-topic
domain: "artificial-intelligence"
parent: AI Search Techniques
related:
  - Cost-Based Search
  - Heuristic Search
theme: "uninformed-search-strategies"
aliases:
  - Blind Search
---

# Blind Search
#concept #ai

Blind Search is een familie van zoekalgoritmes die geen heuristische voorkennis over het doel gebruiken en dus alleen de structuur van de zoekruimte volgen.

## Korte kern

- gebruikt geen heuristiek
- zoekt op basis van diepte, structuur of systematische uitbreiding
- omvat klassiek `BFS`, `DFS`, `DLS`, `IDS` en vaak `Bi-directional Search`

## 1. Wat is het kernprobleem?
Hoe zoek je systematisch door een probleemruimte wanneer je geen extra schatting of slimme richtinginformatie hebt?

## 2. Intuitieve uitleg
Bij blind search weet het algoritme niet welke nodes veelbelovend zijn. Het volgt dus gewoon een vaste zoekregel, bijvoorbeeld eerst breed of eerst diep.

Dat maakt deze algoritmes eenvoudig en algemeen inzetbaar, maar vaak minder efficiënt dan heuristische methodes.

## 3. Formele structuur
Blind search gebruikt geen [[Heuristiek]] `h(n)`.

Typische algoritmes zijn:

- [[Breadth-First Search (BFS)]]
- [[Depth-First Search (DFS)]]
- [[Depth-Limited Search (DLS)]]
- [[Iterative Deepening Search (IDS)]]
- [[Bi-directional Search]]

Ze verschillen vooral in:

- gebruikte datastructuur
- expansievolgorde
- compleetheid en optimaliteit

## 4. Snelle vergelijking

- [[Blind Search]] = geen schatting van doelafstand
- [[Cost-Based Search]] = kiest op echte kost
- [[Heuristic Search]] = kiest mee op basis van schatting

## 5. Toepassing
Als je een graaf hebt zonder heuristische waarden en je wil verschillende systematische zoekstrategieën vergelijken, dan zit je in het domein van blind search.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** blind search gebruikt geen heuristische voorkennis.
- **Veelvoorkomende misvatting:** denken dat `UCS` ook blind search is in exact dezelfde zin als `BFS` en `DFS`, terwijl kostinformatie daar expliciet de keuze stuurt.
- **Link met andere concepten:** [[AI Search Techniques]], [[Breadth-First Search (BFS)]], [[Depth-First Search (DFS)]], [[Depth-Limited Search (DLS)]], [[Iterative Deepening Search (IDS)]], [[Bi-directional Search]], [[Heuristic Search]]

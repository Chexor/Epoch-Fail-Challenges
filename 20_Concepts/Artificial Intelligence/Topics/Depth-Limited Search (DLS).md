---
type: concept-topic
domain: "artificial-intelligence"
parent: Blind Search
related:
  - Blind Search
  - Depth-First Search (DFS)
  - Iterative Deepening Search (IDS)
theme: "uninformed-search-strategies"
aliases:
  - Depth-Limited Search (DLS)
---

# Depth-Limited Search (DLS)
#concept #ai

## 1. Wat is het kernprobleem?
Hoe beperk je `DFS` zodat het niet oneindig diep blijft zoeken?

## 2. Intuitieve uitleg
`DLS` is `DFS` met een harde grens. Zodra de ingestelde diepte bereikt is, stopt het algoritme met verder afdalen in die tak.

## 3. Formele structuur
- gebruikt de logica van `DFS`
- voegt een dieptelimiet `l` toe
- voorkomt oneindig diep zoeken
- is niet volledig als de oplossing dieper zit dan de limiet
- is niet optimaal

## 4. Toepassing
Als je weet dat een oplossing waarschijnlijk niet dieper dan bijvoorbeeld `5` stappen zit, kan `DLS` nuttig zijn om nutteloze diepe exploratie te vermijden.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** `DLS` beperkt de diepte van `DFS`, maar maakt het algoritme daardoor niet automatisch volledig.
- **Veelvoorkomende misvatting:** denken dat een dieptelimiet altijd een veilige verbetering is.
- **Link met andere concepten:** [[Depth-First Search (DFS)]], [[Iterative Deepening Search (IDS)]], [[Search Algorithm]]
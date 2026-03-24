---
type: concept-topic
domain: "artificial-intelligence"
parent: Search Algorithm
related:
  - Explored Set
  - Search Algorithm
  - Queue
  - Priority Queue
theme: "ai-basics-and-search"
aliases:
  - Frontier
---

# Frontier
#concept #ai

De frontier is de verzameling van ontdekte maar nog niet onderzochte nodes of paden waaruit een zoekalgoritme zijn volgende keuze maakt.

## Korte kern

- bevat wat al ontdekt is, maar nog niet geëxpandeerd
- bepaalt mee het gedrag van het zoekalgoritme
- wordt vaak geïmplementeerd als [[Queue]], [[Stack]] of [[Priority Queue]]

## 1. Wat is het kernprobleem?
Hoe hou je bij welke nodes al ontdekt zijn, maar nog onderzocht moeten worden?

## 2. Intuitieve uitleg
De `frontier` is de rand van het zoekproces. Het zijn de nodes of paden die je al kent, maar nog niet hebt uitgebreid.

Je kan de frontier zien als de verzameling "kandidaten" waaruit het zoekalgoritme telkens de volgende keuze maakt.

## 3. Formele structuur
- De `frontier` bevat ontdekte maar nog niet geëxpandeerde nodes of paden.
- De precieze organisatie van de frontier hangt af van het zoekalgoritme.
- Typische implementaties zijn:
  - [[Queue]] voor `BFS`
  - [[Stack]] voor `DFS`
- [[Priority Queue]] voor `UCS`, `Greedy` en `A*`
- De keuzeregel van een zoekalgoritme bepaalt welk element uit de frontier als volgende gekozen wordt.

## 4. Snelle vergelijking

- [[Frontier]] = wat nog onderzocht moet worden
- [[Explored Set]] = wat al onderzocht en afgewerkt is
- [[State Space]] = alle mogelijke toestanden en overgangen van het probleem

## 5. Toepassing
Bij `BFS` bevat de frontier alle paden die al ontdekt zijn, geordend volgens aankomstvolgorde. Bij `A*` bevat de frontier de nog open paden, geordend volgens hun `f(n)`-score.

De frontier is dus niet zomaar opslag, maar het mechanisme dat het gedrag van het zoekalgoritme mee bepaalt.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** de `frontier` bevat wat nog onderzocht moet worden; een [[Explored Set]] bevat wat al afgewerkt is.
- **Veelvoorkomende misvatting:** de frontier verwarren met alle nodes van de volledige `state space`.
- **Link met andere concepten:** [[Search Algorithm]], [[State Space]], [[Breadth-First Search (BFS)]], [[Depth-First Search (DFS)]], [[Uniform-Cost Search (UCS)]], [[Greedy Best-First Search]], [[A-star Search|A* Search]], [[Explored Set]], [[Queue]], [[Stack]], [[Priority Queue]], [[Tree Search vs Graph Search]]
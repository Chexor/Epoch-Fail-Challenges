---
type: concept-topic
domain: "artificial-intelligence"
parent: Blind Search
related:
  - Depth-First Search (DFS)
  - Blind Search
  - Uniform-Cost Search (UCS)
  - BFS Worked Example
theme: "uninformed-search-strategies"
aliases:
  - Breadth-First Search (BFS)
---

# Breadth-First Search (BFS)
#concept #ai

Breadth-First Search (BFS) is een zoekalgoritme dat systematisch alle paden op kleinere diepte onderzoekt voor het diepere paden bekijkt.

## Korte kern

- gebruikt een [[Queue]] (`FIFO`)
- zoekt laag per laag vanuit de startnode
- optimaal bij gelijke stapkosten

## 1. Wat is het kernprobleem?
Hoe vind je systematisch een oplossing door eerst alle ondiepe paden te onderzoeken?

## 2. Intuitieve uitleg
`BFS` zoekt in lagen. Eerst bekijkt het alles op diepte `1`, dan alles op diepte `2`, enzovoort. Het verspreidt zich als een golf vanuit de startnode.

## 3. Formele structuur
- gebruikt een [[Queue]] (`FIFO`)
- kiest altijd de node met de kleinste diepte
- is **compleet** bij eindige branching factor
- is **optimaal** als alle stapkosten gelijk zijn
- gebruikt veel geheugen omdat volledige niveaus in de frontier kunnen blijven staan

## 4. Snelle vergelijking

- [[Breadth-First Search (BFS)]] = kiest op kleinste diepte
- [[Depth-First Search (DFS)]] = kiest de diepste open tak
- [[Uniform-Cost Search (UCS)]] = kiest laagste padkost in plaats van laagste diepte

## 5. Toepassing
In een ongewogen doolhof is `BFS` geschikt als je de oplossing met het kleinste aantal stappen zoekt.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** `BFS` optimaliseert diepte, niet algemene padkost.
- **Veelvoorkomende misvatting:** denken dat `BFS` altijd de goedkoopste oplossing vindt. Dat geldt alleen bij gelijke stapkosten.
- **Link met andere concepten:** [[Search Algorithm]], [[State Space]], [[Depth-First Search (DFS)]], [[Uniform-Cost Search (UCS)]], [[Iterative Deepening Search (IDS)]], [[Frontier]], [[Explored Set]], [[Queue]], [[BFS vs DFS vs UCS vs Greedy vs A-star|BFS vs DFS vs UCS vs Greedy vs A*]], [[BFS vs UCS]], [[Tree Search vs Graph Search]]
---
type: atom
domain: "artificial-intelligence"
parent: Search Algorithm
related:
  - Frontier
  - Search Algorithm
  - Tree Search vs Graph Search
theme: "ai-basics-and-search"
aliases:
  - Explored Set
---

# Explored Set
#concept #ai

Een explored set is de verzameling van nodes die een zoekalgoritme al volledig geëxpandeerd heeft en daardoor niet opnieuw op dezelfde manier wil behandelen.

## Korte kern

- houdt bij wat al afgewerkt onderzocht is
- helpt lussen en dubbel werk vermijden
- is vooral belangrijk in graph search

## 1. Wat is het kernprobleem?
Hoe voorkom je dat een zoekalgoritme dezelfde nodes telkens opnieuw blijft onderzoeken?

## 2. Intuitieve uitleg
De `explored set` is de verzameling van nodes die al volledig onderzocht zijn. Zodra een node eruit bestaat, weet het algoritme: "deze heb ik al uitgebreid, hier moet ik niet opnieuw op dezelfde manier terugkomen".

Dat helpt om lussen te vermijden en onnodig herhalen te verminderen.

## 3. Formele structuur
- De `explored set` bevat nodes die al geëxpandeerd zijn.
- Ze wordt vooral gebruikt in `graph search`.
- Voor een nieuw gegenereerde node controleer je vaak:
  - zit deze al in de `frontier`?
  - zit deze al in de `explored set`?
- Als dat zo is, kan je dubbele verwerking vermijden of alleen een beter pad behouden.

Belangrijk onderscheid:

- [[Frontier]] = ontdekt maar nog niet geëxpandeerd
- `explored set` = al geëxpandeerd

## 4. Snelle vergelijking

- [[Explored Set]] = wat al afgewerkt onderzocht is
- [[Frontier]] = wat nog onderzocht moet worden
- [[Tree Search vs Graph Search]] = vergelijking waarin dit onderscheid cruciaal wordt

## 5. Toepassing
Stel dat je in een graaf van `A` naar `B` en terug naar `A` kan bewegen. Zonder `explored set` kan een algoritme blijven heen en weer springen.

Met een `explored set` markeer je `A` als al onderzocht zodra het uitgebreid is. Wanneer `A` later opnieuw opduikt via een andere route, kan je die herhaling herkennen.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** de `explored set` bevat afgewerkte nodes; de [[Frontier]] bevat open nodes die nog aan de beurt moeten komen.
- **Veelvoorkomende misvatting:** `explored set` en `frontier` door elkaar halen of denken dat ze hetzelfde doel dienen.
- **Link met andere concepten:** [[Frontier]], [[Search Algorithm]], [[State Space]], [[Breadth-First Search (BFS)]], [[Depth-First Search (DFS)]], [[Uniform-Cost Search (UCS)]], [[A-star Search]], [[Tree Search vs Graph Search]]

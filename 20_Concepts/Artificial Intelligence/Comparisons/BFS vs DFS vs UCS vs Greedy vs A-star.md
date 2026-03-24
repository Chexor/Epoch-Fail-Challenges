---
type: concept-comparison
domain: "artificial-intelligence"
parent: AI Search Techniques
related:
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - Uniform-Cost Search (UCS)
  - Greedy Best-First Search
  - A* Search
theme: "how-search-strategy-changes-behavior"
aliases:
  - BFS vs DFS vs UCS vs Greedy vs A*
---

# BFS vs DFS vs UCS vs Greedy vs A*
#concept #ai

## Wat wordt hier vergeleken?
- [[Breadth-First Search (BFS)]]
- [[Depth-First Search (DFS)]]
- [[Uniform-Cost Search (UCS)]]
- [[Greedy Best-First Search]]
- [[A-star Search|A* Search]]

## Kernverschil
Deze algoritmes verschillen vooral in 1 beslissing: **welke node wordt als volgende uit de frontier gekozen?** Dat ene verschil bepaalt hun gedrag, hun geheugengebruik en of ze een optimale oplossing kunnen garanderen.

## Vergelijking

| Aspect | BFS | DFS | UCS | Greedy | A* |
| --- | --- | --- | --- | --- | --- |
| Keuzeregel | kleinste diepte | diepste node | laagste `g(n)` | laagste `h(n)` | laagste `f(n) = g(n)+h(n)` |
| Datastructuur | [[Queue]] | [[Stack]] | [[Priority Queue]] | [[Priority Queue]] | [[Priority Queue]] |
| Gebruikt echte kost? | alleen impliciet bij gelijke stappen | nee | ja | nee | ja |
| Gebruikt heuristiek? | nee | nee | nee | ja | ja |
| Compleet | ja | niet algemeen | ja, bij positieve kosten | niet gegarandeerd | ja, onder voorwaarden |
| Optimaal | ja, bij gelijke kosten | nee | ja | nee | ja, met goede heuristiek |
| Geheugen | hoog | laag | hoog | vaak hoog | vaak hoog |
| Typische fout | diepte verwarren met kost | denken dat snelle oplossing goede oplossing is | behandelen als BFS met labels | verwarren met A* | verwarren met Greedy |

## Wanneer gebruik je wat?
- **BFS:** als elke stap dezelfde kost heeft en je de oplossing met het kleinste aantal stappen zoekt.
- **DFS:** als geheugen schaars is en je snel een mogelijke oplossing wil vinden.
- **UCS:** als verbindingen verschillende kosten hebben en je zeker het goedkoopste pad wil.
- **Greedy:** als je snel richting doel wil zoeken op basis van een heuristiek, zonder optimaliteitsgarantie.
- **A*:** als je een sterke heuristiek hebt en tegelijk efficiëntie en optimaliteit wil combineren.

## Besluitlogica in 1 zin per algoritme
- **BFS:** "Ik neem wat het langst wacht in de queue."
- **DFS:** "Ik volg eerst de meest recente tak zo diep mogelijk."
- **UCS:** "Ik neem eerst het goedkoopste pad tot nu toe."
- **Greedy:** "Ik neem wat het dichtst bij het doel lijkt."
- **A*:** "Ik neem wat in totaal het meest veelbelovend is."

## Waarom is dit onderscheid belangrijk?
Veel examenvragen lijken op elkaar, maar testen precies dit onderscheid:

- kiest het algoritme op basis van **diepte**?
- op basis van **kost**?
- op basis van **heuristiek**?
- of op basis van een **combinatie van kost en heuristiek**?

Als je dat verschil scherp ziet, kan je snel herkennen welk algoritme geschikt is en hoe je de frontier correct moet uitschrijven.

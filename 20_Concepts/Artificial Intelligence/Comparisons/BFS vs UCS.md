---
type: concept-comparison
domain: "artificial-intelligence"
parent: AI Search Techniques
related:
  - Breadth-First Search (BFS)
  - Uniform-Cost Search (UCS)
theme: "depth-vs-cost-based-search"
aliases:
  - BFS vs UCS
---

# BFS vs UCS
#concept #ai

## Wat wordt hier vergeleken?
- [[Breadth-First Search (BFS)]]
- [[Uniform-Cost Search (UCS)]]

## Kernverschil
`BFS` kiest op basis van diepte, `UCS` kiest op basis van totale padkost. Als alle stapkosten gelijk zijn, vallen ze samen; anders niet.

## Vergelijking

| Aspect | BFS | UCS |
| --- | --- | --- |
| Keuzeregel | kleinste diepte | laagste `g(n)` |
| Datastructuur | queue | priority queue |
| Houdt rekening met kosten? | alleen impliciet via aantal stappen | expliciet |
| Compleet | ja | ja, bij positieve kosten |
| Optimaal | ja, bij gelijke kosten | ja |
| Typische fout | denken dat kortste pad altijd goedkoopste is | behandelen alsof het gewoon BFS met labels is |

## Wanneer gebruik je wat?
- **BFS:** als elke stap dezelfde kost heeft en het aantal stappen centraal staat.
- **UCS:** als verbindingen verschillende kosten kunnen hebben en de goedkoopste oplossing nodig is.

## Waarom is dit onderscheid belangrijk?
Veel verwarring ontstaat omdat diepte en kost gemakkelijk door elkaar gehaald worden. Dat verschil bepaalt precies waarom `UCS` nodig is naast `BFS`.

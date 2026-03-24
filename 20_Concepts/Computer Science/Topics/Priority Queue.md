---
type: concept-topic
domain: "computer-science"
parent: "Ordered Processing and Selection"
related:
  - Ordered Processing and Selection
  - Queue
  - Stack
  - Frontier
theme: "ordered-processing-and-selection"
aliases:
  - Priority Queue
---

# Priority Queue
#concept #cs

## 1. Wat is het kernprobleem?
Hoe kies je telkens het element met de hoogste prioriteit in plaats van gewoon het oudste of recentste element?

## 2. Intuitieve uitleg
Een `priority queue` is een wachtrij waarin niet de volgorde van aankomst telt, maar een score of prioriteit. Het "belangrijkste" element komt eerst aan de beurt.

## 3. Formele structuur
- In een `priority queue` heeft elk element een prioriteitswaarde.
- Het element met de beste prioriteit wordt eerst verwijderd.
- Wat "beste" betekent hangt af van het probleem:
  - laagste `g(n)` bij [[Uniform-Cost Search (UCS)]]
  - laagste `h(n)` bij [[Greedy Best-First Search]]
  - laagste `f(n)` bij [[A-star Search|A* Search]]

## 4. Toepassing
In zoekalgoritmes laat een `priority queue` toe om open nodes te ordenen volgens kost of heuristische score, in plaats van volgens aankomstvolgorde.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** een `priority queue` ordent op basis van prioriteit, niet op basis van aankomstvolgorde of recentheid.
- **Veelvoorkomende misvatting:** denken dat een `priority queue` gewoon een gewone queue is met extra metadata.
- **Link met andere concepten:** [[Uniform-Cost Search (UCS)]], [[Greedy Best-First Search]], [[A-star Search|A* Search]], [[Frontier]], [[Queue]], [[Stack]]

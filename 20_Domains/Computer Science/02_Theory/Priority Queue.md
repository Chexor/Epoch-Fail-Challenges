---
type: theory
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

Een priority queue is een datastructuur die telkens het element met de beste prioriteit kiest, in plaats van gewoon het oudste of recentste element.

## Korte kern

- kiest op basis van prioriteit, niet op basis van volgorde van aankomst
- wordt vaak efficient geimplementeerd met een `heap`
- is cruciaal in [[Uniform-Cost Search (UCS)]], [[Greedy Best-First Search]] en [[A-star Search]]

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
  - laagste `f(n)` bij [[A-star Search]]

## 4. Snelle vergelijking

- [[Priority Queue]] = kiest op beste score of prioriteit
- [[Queue]] = kiest het oudste element eerst
- [[Stack]] = kiest het recentste element eerst

## 5. Toepassing
In zoekalgoritmes laat een `priority queue` toe om open nodes te ordenen volgens kost of heuristische score, in plaats van volgens aankomstvolgorde.

### Op het examen (Frontier uitschrijven)
Wanneer je algoritmes zoals UCS, Greedy of A* op papier uitschrijft, stelt de **Frontier** de Priority Queue voor.
- Na **elke expansie** (het toevoegen van nieuwe buur-nodes aan de frontier) moet je de frontier **opnieuw sorteren** op basis van de prioriteitswaarde (resp. $g(n)$, $h(n)$ of $f(n)$).
- Het element met de *laagste waarde* staat telkens vooraan en wordt als volgende geëxpandeerd.
- Bij gelijke waarden bepaalt de alfabetische volgorde (of een specifieke tie-breaker regel uit de opgave) welk element eerst komt.

Kort Python-voorbeeld (met `heapq` dat automatisch sorteert):

```python
import heapq


frontier = []
heapq.heappush(frontier, (3, "C"))
heapq.heappush(frontier, (1, "A"))
heapq.heappush(frontier, (2, "B"))

best_item = heapq.heappop(frontier)
```

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** een `priority queue` ordent op basis van prioriteit, niet op basis van aankomstvolgorde of recentheid.
- **Veelvoorkomende misvatting:** denken dat een `priority queue` gewoon een gewone queue is met extra metadata.
- **Link met andere concepten:** [[Uniform-Cost Search (UCS)]], [[Greedy Best-First Search]], [[A-star Search]], [[Frontier]], [[Queue]], [[Stack]]

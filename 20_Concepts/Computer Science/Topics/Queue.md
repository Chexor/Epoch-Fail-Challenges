---
type: concept-topic
domain: "computer-science"
parent: "Ordered Processing and Selection"
related:
  - Ordered Processing and Selection
  - Stack
  - Priority Queue
  - Frontier
theme: "ordered-processing-and-selection"
aliases:
  - Queue
---

# Queue
#concept #cs

Een queue is een datastructuur die elementen verwerkt in dezelfde volgorde als waarin ze binnenkomen: `First In, First Out`.

## Korte kern

- werkt volgens `FIFO`
- toevoegen gebeurt achteraan, verwijderen vooraan
- belangrijk in [[Breadth-First Search (BFS)]]

## 1. Wat is het kernprobleem?
Hoe verwerk je elementen in dezelfde volgorde als waarin ze aankomen?

## 2. Intuitieve uitleg
Een `queue` werkt zoals aanschuiven in een rij. Wie eerst aankomt, wordt eerst geholpen.

## 3. Formele structuur
- Een `queue` is een `FIFO`-datastructuur: `First In, First Out`.
- Typische operaties zijn:
  - `enqueue`: voeg achteraan toe
  - `dequeue`: neem vooraan weg
  - `peek/front`: bekijk het voorste element zonder het te verwijderen

## 4. Snelle vergelijking

- [[Queue]] = oudste element eerst
- [[Stack]] = recentste element eerst
- [[Priority Queue]] = element met hoogste of laagste prioriteit eerst

## 5. Toepassing
Bij [[Breadth-First Search (BFS)]] gebruik je een `queue` zodat oudere, ondiepere nodes eerst verwerkt worden. Daardoor zoekt `BFS` niveau per niveau.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** een `queue` verwerkt elementen in aankomstvolgorde, niet volgens prioriteit of recentheid.
- **Veelvoorkomende misvatting:** een `queue` verwarren met een [[Stack]] of [[Priority Queue]].
- **Link met andere concepten:** [[Breadth-First Search (BFS)]], [[Frontier]], [[Stack]], [[Priority Queue]]

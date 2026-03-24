---
type: concept-topic
domain: "computer-science"
parent: "Ordered Processing and Selection"
related:
  - Ordered Processing and Selection
  - Queue
  - Priority Queue
  - Frontier
theme: "ordered-processing-and-selection"
aliases:
  - Stack
---

# Stack
#concept #cs

Een stack is een datastructuur die het meest recent toegevoegde element als eerste teruggeeft: `Last In, First Out`.

## Korte kern

- werkt volgens `LIFO`
- toevoegen en verwijderen gebeuren bovenaan
- belangrijk in [[Depth-First Search (DFS)]]

## 1. Wat is het kernprobleem?
Hoe verwerk je elementen zodanig dat het meest recent toegevoegde element eerst terugkomt?

## 2. Intuitieve uitleg
Een `stack` werkt als een stapel borden. Je neemt eerst het bord weg dat je het laatst hebt neergelegd.

## 3. Formele structuur
- Een `stack` is een `LIFO`-datastructuur: `Last In, First Out`.
- Typische operaties zijn:
  - `push`: voeg bovenaan toe
  - `pop`: neem het bovenste element weg
  - `peek/top`: bekijk het bovenste element zonder het te verwijderen

## 4. Snelle vergelijking

- [[Stack]] = recentste element eerst
- [[Queue]] = oudste element eerst
- [[Priority Queue]] = element met hoogste of laagste prioriteit eerst

## 5. Toepassing
Bij [[Depth-First Search (DFS)]] gebruik je een `stack` zodat het meest recent ontdekte pad eerst verder verkend wordt. Daardoor ga je snel dieper in een zoekboom.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** een `stack` geeft voorrang aan het recentste element, niet aan het oudste of het belangrijkste.
- **Veelvoorkomende misvatting:** een `stack` verwarren met een [[Queue]] of [[Priority Queue]].
- **Link met andere concepten:** [[Depth-First Search (DFS)]], [[Frontier]], [[Queue]], [[Priority Queue]]

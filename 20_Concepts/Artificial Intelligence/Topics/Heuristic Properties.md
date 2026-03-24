---
type: concept-topic
domain: "artificial-intelligence"
parent: Heuristic Search
related:
  - Admissible Heuristic
  - Consistent Heuristic
theme: "heuristic-properties-for-a-star"
aliases:
  - Heuristic Properties
---

# Heuristic Properties
#concept #ai

Heuristic Properties groepeert de formele eigenschappen die bepalen hoe betrouwbaar een heuristiek is in algoritmes zoals `A*`.

## Korte kern

- gaat over kwaliteitseigenschappen van heuristieken
- helpt verklaren wanneer `A*` optimaal blijft
- vormt de kapstok voor admissibility en consistency

## 1. Wat is het kernprobleem?
Aan welke voorwaarden moet een heuristiek voldoen zodat een zoekalgoritme correct en optimaal blijft werken?

## 2. Intuitieve uitleg
Niet elke heuristiek is even goed. Sommige schattingen zijn te agressief of intern niet consistent. Daarom bestudeer je formele eigenschappen die zeggen wanneer een heuristiek veilig gebruikt kan worden.

## 3. Formele structuur
De twee belangrijkste eigenschappen in deze cursus zijn:

- [[Admissible Heuristic]]
- [[Consistent Heuristic]]

Deze eigenschappen zijn vooral belangrijk voor:

- [[A-star Search|A* Search]]
- [[Heuristiek]]

## 4. Snelle vergelijking

- [[Admissible Heuristic]] = overschat de echte resterende kost nooit
- [[Consistent Heuristic]] = respecteert bovendien lokale samenhang tussen verbonden nodes

## 5. Toepassing
Als je moet uitleggen waarom een heuristiek veilig is voor `A*`, dan gebruik je de taal van heuristic properties.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** deze note groepeert eigenschappen van heuristieken, niet de heuristieken zelf.
- **Veelvoorkomende misvatting:** admissibility en consistency als volledig losse termen studeren zonder hun gemeenschappelijke rol binnen heuristic search te zien.
- **Link met andere concepten:** [[Heuristic Search]], [[Heuristiek]], [[Admissible Heuristic]], [[Consistent Heuristic]], [[Admissible vs Consistent Heuristic]], [[A-star Search|A* Search]]

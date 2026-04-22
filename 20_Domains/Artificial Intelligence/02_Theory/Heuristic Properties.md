---
type: theory
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

## Probleem

Aan welke voorwaarden moet een heuristiek voldoen zodat een zoekalgoritme correct en optimaal blijft werken?

## Intuïtie

Niet elke heuristiek is even goed. Sommige schattingen zijn te agressief of intern niet consistent. Daarom bestudeer je formele eigenschappen die zeggen wanneer een heuristiek veilig gebruikt kan worden.

## Toepassing

Als je moet uitleggen waarom een heuristiek veilig is voor `A*`, dan gebruik je de taal van heuristic properties.

## Formeel

De twee belangrijkste eigenschappen in deze cursus zijn:

- [[Admissible Heuristic]]
- [[Consistent Heuristic]]

Deze eigenschappen zijn vooral belangrijk voor:

- [[A-star Search]]
- [[Heuristic]]

## Verbanden

> **Valkuil:** admissibility en consistency als volledig losse termen studeren zonder hun gemeenschappelijke rol binnen heuristic search te zien.

- [[Heuristic Search]]
- [[Heuristic]]
- [[Admissible Heuristic]]
- [[Consistent Heuristic]]
- [[Admissible vs Consistent Heuristic]]

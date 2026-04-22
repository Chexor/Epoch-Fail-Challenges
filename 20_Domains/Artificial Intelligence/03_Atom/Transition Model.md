---
type: atom
domain: "artificial-intelligence"
parent: State Space
related:
  - State Space
  - Search Algorithm
  - Goal Test
theme: "ai-basics-and-search"
aliases:
  - Transition Model
  - Transition Function
---

# Transition Model
#concept #ai

Een transition model beschrijft hoe een actie een huidige toestand omzet naar een volgende toestand in een probleemruimte.

## Korte kern

- legt de dynamiek van het probleem formeel vast
- bepaalt welke overgangen mogelijk zijn vanuit een toestand
- is essentieel voor planning, search en simulatie

## Probleem

Hoe bepaal je systematisch wat het effect van een actie is op de toestand van het systeem?

## Intuïtie

Je kan het transition model zien als de spelregels van de omgeving: voor elke toestand en actie zegt het model wat er daarna gebeurt. Zonder dit model kan een agent geen betrouwbare volgende stappen plannen.

## Toepassing

In een grid world bepaalt het transition model bijvoorbeeld dat de actie `move-right` de kolom met 1 verhoogt, behalve als er een muur staat. In robotnavigatie kan het model ook onzekerheid meenemen, zoals sensorrandruis of slip.

## Formeel

- Deterministische vorm: `Result(s, a) -> s'`.
- Niet-deterministische of stochastische vorm: `P(s' | s, a)`.
- Het model ondersteunt:
  - genereren van opvolgtoestanden
  - evalueren van haalbaarheid van plannen
  - koppeling tussen acties, kosten en doelcontrole

## Verbanden

- [[State Space]]
- [[Search Algorithm]]
- [[Goal Test]]

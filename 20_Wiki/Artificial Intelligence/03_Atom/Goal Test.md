---
type: atom
domain: "artificial-intelligence"
parent: Search Algorithm
related:
  - State Space
  - Search Algorithm
  - Path Cost
theme: "ai-basics-and-search"
aliases:
  - Goal Test
---

# Goal Test
#concept #ai

Een goal test is de controle die bepaalt of een huidige toestand voldoet aan de doelconditie van het zoekprobleem.

## Korte kern

- beslist of een gevonden toestand effectief een oplossing is
- wordt toegepast bij het expanderen of selecteren van nodes
- definieert samen met toestanden en acties de probleemformulering

## Probleem

Hoe weet een zoekalgoritme precies wanneer het mag stoppen met zoeken?

## Intuïtie

Een goal test werkt als een heldere stopregel: bij elke relevante toestand check je of het doel bereikt is. Zonder die check weet je niet of je al een geldige oplossing hebt.

## Toepassing

In routeplanning is de goal test vaak: "is huidige locatie de bestemming?" In puzzels kan het zijn: "staat elk element in de gewenste eindpositie?"

## Formeel

- Gegeven een toestandsruimte `S` en doelverzameling `G`, test de functie of `s in G`.
- Uitkomst is booleaans: `true` (doel bereikt) of `false` (verder zoeken).
- Correcte definitie van de goal test is cruciaal voor:
  - validiteit van oplossingen
  - stopconditie van het algoritme
  - evaluatie van zoekresultaten

## Verbanden

- [[Search Algorithm]]
- [[State Space]]
- [[Path Cost]]

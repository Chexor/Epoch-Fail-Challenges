---
type: concept-topic
domain: "artificial-intelligence"
parent: AI Search Techniques
related:
  - Blind Search
  - Heuristic Search
theme: "cost-based-search"
aliases:
  - Cost-Based Search
---

# Cost-Based Search
#concept #ai

Cost-Based Search is een zoekfamilie waarin de keuze van de volgende node gestuurd wordt door de echte padkost die al opgebouwd is.

## Korte kern

- gebruikt echte kostinformatie
- kijkt niet alleen naar diepte, maar naar cumulatieve kost
- belangrijkste voorbeeld is [[Uniform-Cost Search (UCS)]]

## 1. Wat is het kernprobleem?
Hoe vind je een oplossing wanneer verbindingen niet allemaal dezelfde kost hebben?

## 2. Intuitieve uitleg
Sommige paden zijn kort in aantal stappen, maar duur in totale kost. Dan volstaat een dieptegebaseerde strategie zoals `BFS` niet meer. Een cost-based aanpak kijkt daarom naar wat het pad echt gekost heeft.

## 3. Formele structuur
De centrale grootheid is [[g(n)]], de cumulatieve kost van de start tot node `n`.

Belangrijk algoritme:

- [[Uniform-Cost Search (UCS)]]

Deze familie vormt ook een brug naar algoritmes zoals [[A-star Search|A* Search]], waar kost en heuristiek gecombineerd worden.

## 4. Snelle vergelijking

- [[Blind Search]] = kiest zonder heuristiek of expliciete kostensturing
- [[Cost-Based Search]] = kiest op echte kost
- [[Heuristic Search]] = gebruikt een schatting om te sturen

## 5. Toepassing
Bij routeplanning met verschillende afstanden of reistijden moet het algoritme de werkelijke kost meenemen. Daar is cost-based search de juiste familie.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** cost-based search kijkt naar de echte opgebouwde kost, niet enkel naar diepte of schatting.
- **Veelvoorkomende misvatting:** denken dat `BFS` en `UCS` hetzelfde doen zolang ze allebei systematisch zoeken.
- **Link met andere concepten:** [[AI Search Techniques]], [[Uniform-Cost Search (UCS)]], [[g(n)]], [[Path Cost]], [[BFS vs UCS]], [[Heuristic Search]]

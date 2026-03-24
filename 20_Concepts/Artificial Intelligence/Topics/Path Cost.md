---
type: concept-topic
domain: "artificial-intelligence"
parent: Search Algorithm
related:
  - g(n)
  - Search Evaluation Functions
  - Uniform-Cost Search (UCS)
theme: "search-cost-accounting"
aliases:
  - Path Cost
---

# Path Cost
#concept #ai

## 1. Wat is het kernprobleem?
Hoe druk je uit hoe duur een volledig pad door een probleemruimte is?

## 2. Intuitieve uitleg
`Path cost` is de totale kost van de stappen die je al gezet hebt. Het gaat dus niet over hoeveel rekenwerk het algoritme nodig heeft, maar over de kost binnen het probleem zelf.

Die kost kan verschillende betekenissen hebben, afhankelijk van het probleem:

- afstand
- tijd
- brandstof
- geld
- risico
- aantal stappen

## 3. Formele structuur
- Een pad bestaat uit een opeenvolging van toestanden of acties.
- Elke overgang kan een stapkost hebben.
- De `path cost` is de som van die stapkosten over het volledige pad.
- In zoekalgoritmes wordt die kost vaak genoteerd als `g(n)`:
  - `g(n)` = totale kost van start tot node `n`

Belangrijk onderscheid:

- **path cost**: kost in het probleemmodel
- **computational cost**: tijd of geheugen dat het algoritme zelf nodig heeft

## 4. Toepassing
Bij een routeprobleem:

- `A -> B` kost `5 km`
- `B -> G` kost `3 km`

Dan is de `path cost` van `A -> B -> G` gelijk aan `8 km`.

`Uniform-Cost Search (UCS)` kiest dan het pad met de laagste huidige `path cost`.
`A* Search` gebruikt die kost ook, samen met een heuristische schatting van wat nog rest.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** `path cost` gaat over de kost van een oplossingstraject in het probleem, niet over CPU-tijd of geheugengebruik.
- **Veelvoorkomende misvatting:** denken dat "kost" automatisch over computationele kost gaat.
- **Link met andere concepten:** [[State Space]], [[Search Algorithm]], [[Uniform-Cost Search (UCS)]], [[A-star Search|A* Search]], [[Heuristiek]], [[Priority Queue]]
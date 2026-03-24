---
type: concept-topic
domain: "artificial-intelligence"
parent: Search Evaluation Functions
related:
  - h(n)
  - f(n)
  - Search Evaluation Functions
  - Uniform-Cost Search (UCS)
theme: "search-cost-accounting"
aliases:
  - g(n)
---

# g(n)
#concept #ai

`g(n)` is de echte cumulatieve kost van de startnode tot node `n`. Het zegt dus hoeveel het pad **tot nu toe** al gekost heeft.

## Korte kern

- kijkt naar het **verleden** van het pad
- gebruikt echte kosten, geen schatting
- centraal in [[Uniform-Cost Search (UCS)]] en [[A-star Search|A* Search]]

## 1. Wat is het kernprobleem?
Hoe druk je uit wat een pad tot de huidige node al echt gekost heeft?

## 2. Intuitieve uitleg
`g(n)` is de kost die je al betaald hebt om van de start naar node `n` te geraken. Het kijkt dus naar het verleden van het pad, niet naar wat nog komt.

## 3. Formele structuur
- `g(n)` = cumulatieve kost van start tot node `n`
- `g(n)` is een vorm van [[Path Cost]]
- bij [[Uniform-Cost Search (UCS)]] bepaalt `g(n)` rechtstreeks de prioriteit
- bij [[A-star Search|A* Search]] vormt `g(n)` samen met [[h(n)]] de score [[f(n)]]

## 4. Snelle vergelijking

- [[g(n)]] = echte kost tot nu toe
- [[h(n)]] = geschatte resterende kost
- [[f(n)]] = totale geschatte kost via `n`

## 5. Toepassing
Als het pad `A -> B -> C` respectievelijk kosten `2` en `3` heeft, dan is `g(C) = 5`.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** `g(n)` kijkt naar de echte kost tot nu toe; [[h(n)]] kijkt naar een schatting van wat nog rest.
- **Veelvoorkomende misvatting:** `g(n)` verwarren met de totale verwachte kost van een oplossing.
- **Link met andere concepten:** [[Path Cost]], [[Uniform-Cost Search (UCS)]], [[A-star Search|A* Search]], [[h(n)]], [[f(n)]]
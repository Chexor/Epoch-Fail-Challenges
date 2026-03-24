---
type: concept-topic
domain: "artificial-intelligence"
parent: Search Evaluation Functions
related:
  - g(n)
  - h(n)
  - Search Evaluation Functions
  - A-star Search
theme: "search-cost-accounting"
aliases:
  - f(n)
---

# f(n)
#concept #ai

`f(n)` is de totale geschatte kost van een oplossing via node `n`. Het combineert wat het pad **al gekost heeft** met wat het **nog ongeveer zal kosten**.

## Korte kern

- `f(n) = g(n) + h(n)`
- combineert **echte kost** en **heuristische schatting**
- centraal in [[A-star Search|A* Search]]

## 1. Wat is het kernprobleem?
Hoe combineer je wat een pad al gekost heeft met wat het nog ongeveer zal kosten?

## 2. Intuitieve uitleg
`f(n)` is de totale schatting van een oplossing via node `n`. Het combineert het verleden van het pad met een inschatting van de toekomst.

## 3. Formele structuur
- `f(n) = g(n) + h(n)`
- `g(n)` = echte kost tot nu toe
- `h(n)` = geschatte resterende kost
- `f(n)` wordt vooral gebruikt in [[A-star Search|A* Search]]

## 4. Snelle vergelijking

- [[g(n)]] = wat al echt betaald is
- [[h(n)]] = wat nog geschat wordt
- [[f(n)]] = de totale evaluatiescore via `n`

## 5. Toepassing
Als `g(n) = 7` en `h(n) = 3`, dan is `f(n) = 10`. Een algoritme zoals [[A-star Search|A* Search]] vergelijkt dan nodes op basis van die totale score.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** `f(n)` is geen zuiver gemeten kost en ook geen zuivere schatting, maar een combinatie van beide.
- **Veelvoorkomende misvatting:** `f(n)` verwarren met alleen [[g(n)]] of alleen [[h(n)]].
- **Link met andere concepten:** [[A-star Search|A* Search]], [[g(n)]], [[h(n)]], [[Path Cost]], [[Heuristiek]]
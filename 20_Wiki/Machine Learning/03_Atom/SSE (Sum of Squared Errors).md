---
type: atom
domain: "machine-learning"
parent: "Model Evaluation"
related:
  - Model Evaluation
  - Loss Function
  - MSE (Mean Squared Error)
theme: "model-evaluation"
aliases:
  - SSE (Sum of Squared Errors)
---

# SSE (Sum of Squared Errors)
#concept #ml

SSE (Sum of Squared Errors) kort uitgelegd: wat het is, waarom het telt en wanneer je het gebruikt.
## Korte kern

- kernidee van dit concept
- belangrijkste rol binnen de ML-flow
- link met verwante concepten

## 1. Wat is het kernprobleem?
Hoe meet je de totale fout van een model wanneer grote fouten extra zwaar moeten doorwegen?

## 2. Intuitieve uitleg
Voor elk datapunt neem je de fout tussen echt en voorspeld. Daarna kwadrateer je die fout en tel je alles op.

## 3. Formele structuur
- `SSE = sum((y_i - y_hat_i)^2)`
- Positieve en negatieve fouten heffen elkaar niet op
- Grote fouten tellen zwaarder mee door het kwadraat

## 4. Snelle vergelijking

- Plaats dit concept kort tegenover 1-2 verwante concepten uit deze map.

## 5. Toepassing
Voorbeeld:
- echte waarden: `[3, 5, 7]`
- voorspellingen: `[2, 5, 9]`
- fouten: `[1, 0, -2]`
- gekwadrateerde fouten: `[1, 0, 4]`
- `SSE = 5`

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** `SSE` telt gekwadrateerde fouten op en straft grote afwijkingen extra zwaar.
- **Veelvoorkomende misvatting:** vergeten te kwadrateren of de foutterm verkeerd interpreteren.
- **Link met andere concepten:** [[MSE (Mean Squared Error)]], [[Loss Function]]

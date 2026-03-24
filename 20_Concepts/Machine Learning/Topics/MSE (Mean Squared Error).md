---
type: concept-topic
domain: "machine-learning"
parent: "Model Evaluation"
related:
  - Model Evaluation
  - MAE (Mean Absolute Error)
  - RMSE (Root Mean Squared Error)
  - MAE vs MSE vs RMSE
theme: "model-evaluation"
aliases:
  - MSE (Mean Squared Error)
---

# MSE (Mean Squared Error)
#concept #ml

## 1. Wat is het kernprobleem?
Je wil de gemiddelde gekwadrateerde fout per datapunt kennen, zodat modellen eerlijk vergeleken kunnen worden.

## 2. Intuitieve uitleg
MSE is SSE gedeeld door het aantal datapunten. Daardoor maakt de grootte van de dataset minder uit bij het vergelijken.

## 3. Formele structuur
- `MSE = (1/n) * sum((y_i - y_hat_i)^2)`
- MSE straft grote fouten relatief zwaar
- De eenheid is het kwadraat van de target-eenheid

## 4. Toepassing
Voorbeeld:
- `SSE = 20`
- `n = 5`
- `MSE = 20 / 5 = 4`

Als 1 voorspelling sterk fout zit, stijgt de MSE snel door het kwadraat.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** `MSE` gebruikt kwadraten en reageert daardoor sterker op outliers dan `MAE`.
- **Veelvoorkomende misvatting:** denken dat `MSE` in dezelfde eenheid als de target staat.
- **Link met andere concepten:** [[SSE (Sum of Squared Errors)]], [[RMSE (Root Mean Squared Error)]], [[MAE (Mean Absolute Error)]]

## Context in het domein
- Overzicht: [[00_Overzicht Machine Learning Concepten]]
- Vergelijking: [[MAE vs MSE vs RMSE]]

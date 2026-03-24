---
type: concept-topic
domain: "machine-learning"
parent: "Model Evaluation"
related:
  - Model Evaluation
  - MSE (Mean Squared Error)
  - RMSE (Root Mean Squared Error)
  - MAE vs MSE vs RMSE
theme: "model-evaluation"
aliases:
  - MAE (Mean Absolute Error)
---

# MAE (Mean Absolute Error)
#concept #ml

## 1. Wat is het kernprobleem?
Je wil een foutmaat die gemakkelijk leesbaar is en minder gevoelig is voor uitschieters dan MSE.

## 2. Intuitieve uitleg
MAE kijkt naar hoe ver je voorspelling gemiddeld van de echte waarde ligt, zonder plus- en minfouten elkaar te laten opheffen.

## 3. Formele structuur
- `MAE = (1/n) * sum(|y_i - y_hat_i|)`
- Elke fout telt lineair mee
- Eenheid is dezelfde als de target-eenheid

## 4. Toepassing
Als je voorspellingen gemiddeld 120 euro naast de echte prijs zitten, dan is `MAE = 120 euro`.
Dat maakt MAE vaak makkelijker uit te leggen dan MSE.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** `MAE` meet gemiddelde absolute afwijking en blijft daardoor goed interpreteerbaar.
- **Veelvoorkomende misvatting:** vergeten absolute waarde te nemen.
- **Link met andere concepten:** [[MSE (Mean Squared Error)]], [[RMSE (Root Mean Squared Error)]]

## Context in het domein
- Overzicht: [[00_Overzicht Machine Learning Concepten]]
- Vergelijking: [[MAE vs MSE vs RMSE]]

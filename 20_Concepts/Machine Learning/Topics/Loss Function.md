---
type: concept-topic
domain: "machine-learning"
parent: "Model Evaluation"
related:
  - Model Evaluation
  - MAE (Mean Absolute Error)
  - MSE (Mean Squared Error)
  - Gradient Descent
theme: "model-evaluation"
aliases:
  - Loss Function
---

# Loss Function
#concept #ml

## 1. Wat is het kernprobleem?
Tijdens training heb je een objectieve maat nodig die zegt hoe fout het model momenteel is.

## 2. Intuitieve uitleg
Een loss function vat alle voorspelfouten samen in 1 getal. Hoe lager die loss, hoe beter het model meestal aansluit bij de trainingsdata.

## 3. Formele structuur
- Bij regressie gebruik je vaak `SSE`, `MSE` of `MAE`
- Trainen betekent: parameters aanpassen zodat de loss daalt
- De optimizer gebruikt de loss om te weten hoe hij moet updaten

## 4. Toepassing
Bij regressie met `MSE`:
1. het model maakt voorspellingen `y_hat`
2. je vergelijkt die met de echte waarden `y`
3. je berekent de MSE
4. je past de parameters aan zodat de MSE kleiner wordt

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** een `loss function` stuurt het leerproces tijdens training aan.
- **Veelvoorkomende misvatting:** loss en evaluatiemetric als volledig hetzelfde beschouwen zonder context.
- **Link met andere concepten:** [[MSE (Mean Squared Error)]], [[Gradient Descent]]

## Context in het domein
- Overzicht: [[00_Overzicht Machine Learning Concepten]]
- Vergelijking: [[MAE vs MSE vs RMSE]]

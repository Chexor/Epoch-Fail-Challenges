---
type: atom
domain: "machine-learning"
parent: "Model Evaluation"
related:
  - Model Evaluation
  - MAE (Mean Absolute Error)
  - MSE (Mean Squared Error)
  - Binary Crossentropy
  - Gradient Descent
  - Optimization and Training
  - Loss Function
theme: "model-evaluation"
aliases:
  - Loss Function
---

# Loss Function
#concept #ml

Een loss function is een formule die tijdens training samenvat hoe fout de huidige modelvoorspellingen zijn.

## Korte kern

- zet voorspelfouten om in 1 trainingssignaal
- lagere loss betekent meestal betere fit op trainingsdata
- stuurt parameterupdates tijdens training aan

## 1. Wat is het kernprobleem?
Tijdens training heb je een objectieve maat nodig die zegt hoe fout het model momenteel is.

## 2. Intuitieve uitleg
Een loss function vat alle voorspelfouten samen in 1 getal. Hoe lager die loss, hoe beter het model meestal aansluit bij de trainingsdata.

## 3. Formele structuur
- Bij regressie gebruik je vaak `SSE`, `MSE` of `MAE`
- Bij binaire classificatie gebruik je vaak [[Binary Crossentropy]]
- Trainen betekent: parameters aanpassen zodat de loss daalt
- De optimizer gebruikt de loss om te weten hoe hij moet updaten

## 4. Snelle vergelijking

- [[Loss Function]] = foutmaat die training aanstuurt
- [[Model Evaluation]] = bredere interpretatie en vergelijking van prestaties
- [[MSE (Mean Squared Error)]] = specifieke loss of metric voor regressie
- [[Binary Crossentropy]] = specifieke loss voor binaire classificatie

## 5. Toepassing
Bij regressie met `MSE`:
1. het model maakt voorspellingen `y_hat`
2. je vergelijkt die met de echte waarden `y`
3. je berekent de MSE
4. je past de parameters aan zodat de MSE kleiner wordt

Kort Python-voorbeeld:

```python
def squared_error(y_true, y_pred):
    return (y_true - y_pred) ** 2


loss_value = squared_error(10, 8)
```

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** een `loss function` stuurt het leerproces tijdens training aan.
- **Veelvoorkomende misvatting:** loss en evaluatiemetric als volledig hetzelfde beschouwen zonder context.
- **Link met andere concepten:** [[Model Evaluation]], [[MSE (Mean Squared Error)]], [[MAE (Mean Absolute Error)]], [[Binary Crossentropy]], [[Gradient Descent]], [[Optimization and Training]]

## Context in het domein
- Overzicht: [[00_Overzicht Machine Learning Concepten]]
- Vergelijking: [[MAE vs MSE vs RMSE]]

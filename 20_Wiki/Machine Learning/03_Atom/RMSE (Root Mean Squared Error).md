---
type: atom
domain: "machine-learning"
parent: "Model Evaluation"
related:
  - Model Evaluation
  - MAE (Mean Absolute Error)
  - MSE (Mean Squared Error)
  - MAE vs MSE vs RMSE
theme: "model-evaluation"
aliases:
  - RMSE (Root Mean Squared Error)
---

# RMSE (Root Mean Squared Error)
#concept #ml

RMSE (Root Mean Squared Error) kort uitgelegd: wat het is, waarom het telt en wanneer je het gebruikt.
## Korte kern

- kernidee van dit concept
- belangrijkste rol binnen de ML-flow
- link met verwante concepten

## 1. Wat is het kernprobleem?
MSE is nuttig, maar moeilijk te interpreteren omdat de eenheid gekwadrateerd is.

## 2. Intuitieve uitleg
RMSE neemt de wortel van de MSE en brengt de fout zo terug naar dezelfde eenheid als de target.

## 3. Formele structuur
- `RMSE = sqrt(MSE)`
- Gebruikt dezelfde foutlogica als MSE
- Zelfde eenheid als de target

## 4. Snelle vergelijking

- Plaats dit concept kort tegenover 1-2 verwante concepten uit deze map.

## 5. Toepassing
Als de target huisprijs in euro is, dan is RMSE ook in euro. Dat maakt de foutmaat bruikbaar om aan mensen uit te leggen.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** `RMSE` ligt opnieuw in dezelfde eenheid als de target en blijft tegelijk gevoelig voor grotere fouten.
- **Veelvoorkomende misvatting:** `RMSE` verwarren met `MAE`; `RMSE` straft grote fouten zwaarder.
- **Link met andere concepten:** [[MSE (Mean Squared Error)]], [[MAE (Mean Absolute Error)]]

## Context in het domein
- Overzicht: [[00_Overzicht Machine Learning Concepten]]
- Vergelijking: [[MAE vs MSE vs RMSE]]

---
type: concept-topic
domain: "machine-learning"
parent: "Model Evaluation"
related:
  - Model Evaluation
  - Linear Regression
  - Loss Function
theme: "model-evaluation"
aliases:
  - R2 en R
---

# R2 en R
#concept #ml

## 1. Wat is het kernprobleem?
Je wil de kwaliteit van een lineair model samenvatten met compacte maten.

## 2. Intuitieve uitleg
`R` beschrijft richting en sterkte van een lineair verband. `R2` zegt hoeveel variantie in de target door het model verklaard wordt.

## 3. Formele structuur
- `R` ligt tussen `-1` en `1`
- `R2` is bij een goede fit vaak dicht bij `1`
- `R2` kan ook `0` of zelfs negatief zijn als het model erg slecht is
- Hoge `R` of `R2` betekent geen causaliteit

## 4. Toepassing
Als `R2 = 0.80`, verklaart het model ongeveer 80% van de variantie in de target.
Als `R` negatief is, wijst dat op een dalend lineair verband.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** `R` beschrijft correlatie; `R2` drukt uit hoeveel variantie door het model verklaard wordt.
- **Veelvoorkomende misvatting:** denken dat `R2` altijd tussen `0` en `1` moet liggen in elke situatie.
- **Link met andere concepten:** [[MAE (Mean Absolute Error)]], [[MSE (Mean Squared Error)]], [[Linear Regression]]

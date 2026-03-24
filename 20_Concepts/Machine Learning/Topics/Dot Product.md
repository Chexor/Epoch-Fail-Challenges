---
type: concept-topic
domain: "machine-learning"
parent: "Linear Modeling"
related:
  - Linear Modeling
  - Slope en Intercept
  - Neural Network
theme: "linear-modeling"
aliases:
  - Dot Product
---

# Dot Product
#concept #ml

## 1. Wat is het kernprobleem?
Hoe combineer je meerdere features en hun gewichten tot 1 voorspelling?

## 2. Intuitieve uitleg
Elk feature krijgt een gewicht. Je vermenigvuldigt feature en gewicht per component en telt alles op. Zo laat je sommige features sterker meetellen dan andere.

## 3. Formele structuur
- `a . b = a1*b1 + a2*b2 + ... + an*bn`
- De vectoren moeten dezelfde lengte hebben
- In regressie: `y_hat = w . x + b`

## 4. Toepassing
Voorbeeld:
- `w = [2, 3]`
- `x = [4, 5]`
- `w . x = 2*4 + 3*5 = 8 + 15 = 23`
- met bias `b = 1` krijg je `y_hat = 24`

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** het `dot product` combineert overeenkomstige componenten uit twee vectoren tot één scalair resultaat.
- **Veelvoorkomende misvatting:** vectoren van verschillende lengte willen combineren.
- **Link met andere concepten:** [[Linear Regression]]

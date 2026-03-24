---
type: concept-topic
domain: "machine-learning"
parent: "Linear Modeling"
related:
  - Linear Modeling
  - OLS (Ordinary Least Squares)
  - Gradient Descent
  - Linear Regression
theme: "linear-modeling"
aliases:
  - Linear Regression
---

# Linear Regression
#concept #ml

## 1. Wat is het kernprobleem?
Hoe voorspel je een numerieke target wanneer je veronderstelt dat input en output ongeveer lineair samenhangen?

## 2. Intuitieve uitleg
Linear regression zoekt de rechte die gemiddeld zo dicht mogelijk bij alle datapunten ligt. Het model probeert dus niet elk punt exact te raken, maar wel een goede algemene trend te vinden.

## 3. Formele structuur
- Simple linear regression: `y_hat = a*x + b`
- Multiple linear regression: `y_hat = a0 + a1*x1 + ... + an*xn`
- `a`, `a1`, `a2`, ... zijn gewichten
- `b` of `a0` is de intercept of bias

## 4. Toepassing
Voor huizenprijzen:
- feature `x` = aantal kamers
- target `y` = prijs
- model: `prijs = a * kamers + b`

Als `a = 50000`, dan stijgt de voorspelde prijs met 50000 euro per extra kamer.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** `linear regression` modelleert samenhang, maar bewijst geen causaliteit.
- **Veelvoorkomende misvatting:** een goed lineair model verwarren met een causale verklaring.
- **Link met andere concepten:** [[Slope en Intercept]], [[OLS (Ordinary Least Squares)]], [[Gradient Descent]]

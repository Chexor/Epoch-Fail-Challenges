---
type: theory
domain: "machine-learning"
parent: "Linear Modeling"
related:
  - Linear Modeling
  - OLS (Ordinary Least Squares)
  - Gradient Descent
  - Machine Learning
  - Linear Regression Python Worked Example
  - Scatter Plot
  - Logistic Regression
theme: "linear-modeling"
aliases:
  - Linear Regression
---

# Linear Regression
#concept #ml

Linear Regression is een model dat een numerieke target voorspelt via een lineaire combinatie van een of meer features.

## Korte kern

- voorspelt een continue waarde
- gebruikt een rechte of hypervlak als model
- is een basisvoorbeeld van `supervised learning` voor regressie

## 1. Wat is het kernprobleem?
Hoe voorspel je een numerieke target wanneer je veronderstelt dat input en output ongeveer lineair samenhangen?

## 2. Intuitieve uitleg
Linear regression zoekt de rechte die gemiddeld zo dicht mogelijk bij alle datapunten ligt. Het model probeert dus niet elk punt exact te raken, maar wel een goede algemene trend te vinden.

## 3. Formele structuur
- Simple linear regression: `y_hat = a*x + b`
- Multiple linear regression: `y_hat = a0 + a1*x1 + ... + an*xn`
- `a`, `a1`, `a2`, ... zijn gewichten
- `b` of `a0` is de intercept of bias

## 4. Snelle vergelijking

- [[Linear Regression]] = voorspelt een continue waarde met een lineair model
- [[Logistic Regression]] = gebruikt een lineaire score voor classificatiekansen
- [[K-Nearest Neighbors (KNN)]] = voorspelt op basis van gelijkaardige voorbeelden
- [[K-Means]] = groepeert zonder labels en voorspelt geen targetwaarde

## 5. Toepassing
Voor huizenprijzen:
- feature `x` = aantal kamers
- target `y` = prijs
- model: `prijs = a * kamers + b`

Als `a = 50000`, dan stijgt de voorspelde prijs met 50000 euro per extra kamer.

Kort Python-voorbeeld:

```python
def predict_price(rooms, slope, intercept):
    return slope * rooms + intercept


predicted_price = predict_price(4, 50000, 120000)
```

Voor een volledige Python-uitwerking, zie [[Linear Regression Python Worked Example]].

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** `linear regression` modelleert samenhang, maar bewijst geen causaliteit.
- **Veelvoorkomende misvatting:** een goed lineair model verwarren met een causale verklaring.
 - **Link met andere concepten:** [[Machine Learning]], [[Supervised Learning]], [[Classification vs Regression]], [[Linear Modeling]], [[Linear Model Terms]], [[Slope]], [[Intercept]], [[Scatter Plot]], [[OLS (Ordinary Least Squares)]], [[Gradient Descent]], [[Logistic Regression]], [[Linear Regression Python Worked Example]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

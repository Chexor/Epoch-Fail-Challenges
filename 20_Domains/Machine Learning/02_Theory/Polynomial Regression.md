---
type: theory
domain: "machine-learning"
parent: "Linear Modeling"
related:
  - Linear Modeling
  - Linear Regression
  - OLS (Ordinary Least Squares)
theme: "linear-modeling"
aliases:
  - Polynomial Regression
---

# Polynomial Regression
#concept #ml

Polynomial Regression kort uitgelegd: wat het is, waarom het telt en wanneer je het gebruikt.
## Korte kern

- kernidee van dit concept
- belangrijkste rol binnen de ML-flow
- link met verwante concepten

## 1. Wat is het kernprobleem?
Hoe modelleer je een niet-lineair patroon tussen input en target zonder direct naar complexe niet-lineaire modellen te gaan?

## 2. Intuitieve uitleg
Polynomial regression maakt extra versies van dezelfde feature (`x^2`, `x^3`, ...), zodat een lineair model een kromme kan fitten.

Je kan het zien als:
- zelfde "motor" als linear regression
- rijkere inputrepresentatie

## 3. Formele structuur
- Model met 1 feature en graad `d`: `y_hat = b0 + b1*x + b2*x^2 + ... + bd*x^d`
- Het model is niet-lineair in `x`, maar lineair in parameters `b0..bd`
- Degree is een hyperparameter die je moet kiezen op validatie/test, niet op train alleen

## 4. Snelle vergelijking

- Plaats dit concept kort tegenover 1-2 verwante concepten uit deze map.

## 5. Toepassing
In `scikit-learn` gebruik je typisch:
1. `PolynomialFeatures(degree=d)`
2. `LinearRegression()`
3. Evaluatie met `MAE`, `RMSE`, `R2`

Praktisch doel: de laagste degree vinden die het patroon capteert en goed generaliseert.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** `polynomial regression` blijft lineair in zijn parameters, ook al is de curve niet-lineair in `x`.
- **Veelvoorkomende misvatting:** een hoge degree verwarren met automatisch betere generalisatie.
- **Link met andere concepten:** [[Linear Regression]], [[Parameters vs Hyperparameters]], [[MSE (Mean Squared Error)]], [[Grid Search]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

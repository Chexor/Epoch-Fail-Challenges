---
type: theory
domain: "machine-learning"
parent: "Linear Modeling"
related:
  - Linear Modeling
  - Linear Regression
  - Gradient Descent
theme: "linear-modeling"
aliases:
  - OLS (Ordinary Least Squares)
---

# OLS (Ordinary Least Squares)
#concept #ml

OLS (Ordinary Least Squares) kort uitgelegd: wat het is, waarom het telt en wanneer je het gebruikt.
## Korte kern

- kernidee van dit concept
- belangrijkste rol binnen de ML-flow
- link met verwante concepten

## 1. Wat is het kernprobleem?
Je wil de parameters van lineaire regressie exact berekenen zonder iteratieve zoekmethode.

## 2. Intuitieve uitleg
OLS kiest de rechte waarvoor de totale gekwadrateerde fout zo klein mogelijk is. Het is de klassieke, directe oplossing voor lineaire regressie.

## 3. Formele structuur
- Doel: minimaliseer `sum((y_i - y_hat_i)^2)`
- OLS geeft een analytische oplossing voor lineaire regressie
- In scikit-learn gebruikt `LinearRegression` standaard OLS

## 4. Snelle vergelijking

- Plaats dit concept kort tegenover 1-2 verwante concepten uit deze map.

## 5. Toepassing
Bij een eenvoudige regressie hoef je niet stap voor stap te updaten zoals bij gradient descent. OLS berekent meteen de best passende lijn.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** `OLS` geeft een directe analytische oplossing, terwijl `gradient descent` iteratief optimaliseert.
- **Veelvoorkomende misvatting:** denken dat `OLS` voor elk modeltype beschikbaar is.
- **Link met andere concepten:** [[Linear Regression]], [[Gradient Descent]], [[SSE (Sum of Squared Errors)]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

---
type: theory
domain: "machine-learning"
parent: "ML Tooling and Frameworks"
related:
  - ML Tooling and Frameworks
  - K-Nearest Neighbors (KNN)
  - Grid Search
theme: "ml-tooling-and-frameworks"
aliases:
  - Scikit-learn
---

# Scikit-learn
#concept #ml

Scikit-learn kort uitgelegd: wat het is, waarom het telt en wanneer je het gebruikt.
## Korte kern

- kernidee van dit concept
- belangrijkste rol binnen de ML-flow
- link met verwante concepten

## 1. Wat is het kernprobleem?
Je wil klassieke ML-modellen snel gebruiken zonder alles zelf te programmeren.

## 2. Intuitieve uitleg
Scikit-learn is een praktische Python-bibliotheek met een consistente werkwijze. Je maakt een model, traint het met `fit()`, voorspelt met `predict()` en evalueert met metrics.

## 3. Formele structuur
- Typische workflow: `model.fit(X, y)` -> `model.predict(X_new)`
- Voor lineaire regressie gebruik je vaak `LinearRegression`
- Voor tuning gebruik je bv. `GridSearchCV`

## 4. Snelle vergelijking

- Plaats dit concept kort tegenover 1-2 verwante concepten uit deze map.

## 5. Toepassing
Workflow:
1. splits data in features en target
2. train `LinearRegression()`
3. maak voorspellingen
4. bereken bv. `MAE`, `MSE` of `R2`

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** `Scikit-learn` biedt een consistente workflow voor klassieke ML-modellen.
- **Veelvoorkomende misvatting:** `X` als 1D doorgeven terwijl `scikit-learn` vaak een 2D feature-matrix verwacht.
- **Link met andere concepten:** [[Linear Regression]], [[OLS (Ordinary Least Squares)]], [[Grid Search]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

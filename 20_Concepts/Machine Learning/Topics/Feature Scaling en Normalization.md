---
type: concept-topic
domain: "machine-learning"
parent: "Data Preparation"
related:
  - Data Preparation
  - K-Nearest Neighbors (KNN)
  - Gradient Descent
theme: "data-preparation"
aliases:
  - Feature Scaling en Normalization
---

# Feature Scaling en Normalization
#concept #ml

## 1. Wat is het kernprobleem?
Features met heel verschillende groottes kunnen training met gradient descent traag of instabiel maken.

## 2. Intuitieve uitleg
Als 1 feature waarden rond 2 heeft en een ander rond 200000, dan trekt dat grote getal sneller aan het model. Door te schalen zet je features op een vergelijkbare schaal.

## 3. Formele structuur
- Min-max scaling: `(x - min(x)) / (max(x) - min(x))`
- Standardization: `(x - mean(x)) / std(x)`
- `Normalization` wordt soms breed gebruikt voor schalen, maar betekent niet altijd exact hetzelfde als standardization

## 4. Toepassing
Bij huizenprijzen kunnen `aantal kamers` en `oppervlakte in m2` nog redelijk samen liggen, maar `prijs` en `postnummer` niet. Na scaling convergeren GD en SGD vaak sneller.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** schaling verandert de schaal van features en maakt training of afstandsvergelijkingen vaak stabieler.
- **Veelvoorkomende misvatting:** een schaaltransformatie apart op train en test fitten in plaats van enkel op train.
- **Link met andere concepten:** [[Gradient Descent]], [[SGD (Stochastic Gradient Descent)]]

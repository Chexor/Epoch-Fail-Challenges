---
type: concept-topic
domain: "machine-learning"
parent: "ML Problem Framing"
related:
  - ML Problem Framing
  - Classification vs Regression
  - Machine Learning
theme: "ml-problem-framing"
aliases:
  - Data, Example, Feature, Target
---

# Data, Example, Feature, Target
#concept #ml

## 1. Wat is het kernprobleem?
Zonder deze basiswoorden raak je snel in de war over wat het model als input krijgt en wat het moet voorspellen.

## 2. Intuitieve uitleg
Zie een dataset als een tabel.
- `data` = de volledige tabel
- `example` of `sample` = 1 rij
- `feature` = een invoerkolom
- `target` = de kolom die je wil voorspellen

## 3. Formele structuur
- Dataset `D = {(x_i, y_i)}`
- `x_i` = feature-vector van sample `i`
- `y_i` = target van sample `i`
- 1 example is dus 1 paar `(x_i, y_i)`

## 4. Toepassing
Huizenvoorbeeld:
- 1 rij = 1 huis
- features = aantal kamers, oppervlakte, bouwjaar
- target = prijs

Als je de target als feature gebruikt, geef je het model informatie die het in de praktijk niet mag kennen.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** een `feature` is modelinput; een `target` is de grootheid die voorspeld moet worden.
- **Veelvoorkomende misvatting:** de `target` per ongeluk meegeven als input.
- **Link met andere concepten:** [[Linear Regression]], [[Classification vs Regression]]

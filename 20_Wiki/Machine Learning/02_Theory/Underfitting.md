---
type: theory
domain: "machine-learning"
parent: "Model Fitting"
related:
  - Model Fitting
  - Overfitting
  - Linear Regression
  - Polynomial Regression
theme: "generalization"
aliases:
  - Underfitting
  - Underfit
---

# Underfitting
#concept #ml

Underfitting is het fenomeen waarbij een model te weinig complexiteit heeft om relevante patronen in de data te leren.

## Korte kern

- model is te simpel voor het probleem
- zowel training- als validatiefout blijven relatief hoog
- los je op met rijker model of betere features

## 1. Wat is het kernprobleem?
Hoe herken je dat een model onvoldoende leervermogen heeft om zelfs de trainingsdata goed te benaderen?

## 2. Intuitieve uitleg
Een underfit model lijkt op een liniaal die je probeert te leggen op een sterk gebogen curve. Het globale idee klopt misschien, maar details van het patroon gaan verloren.

## 3. Formele structuur
- typisch patroon: hoge fout op training en vergelijkbaar hoge fout op validatie
- mogelijke oorzaken:
  - modelcomplexiteit te laag
  - te weinig relevante features
  - te sterke regularisatie
- gevolg: zwakke prestaties op zowel bekende als nieuwe data

## 4. Snelle vergelijking
- [[Underfitting]] = model te simpel
- [[Overfitting]] = model te complex
- [[Model Fitting]] = balans zoeken tussen beide

## 5. Toepassing
Als een lineair model systematisch een krom verband mist, kan overschakelen naar [[Polynomial Regression]] of betere feature engineering underfitting verminderen.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** underfitting betekent dat het model te weinig leert, niet dat de data per se slecht is.
- **Veelvoorkomende misvatting:** underfitting en overfitting verwarren omdat beide slechte resultaten kunnen geven.
- **Link met andere concepten:** [[Model Fitting]], [[Overfitting]], [[Linear Regression]], [[Polynomial Regression]], [[Regularization]], [[Train Validation Test Split]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

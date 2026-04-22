---
type: theory
domain: "machine-learning"
parent: "Optimization and Training"
related:
  - Optimization and Training
  - Model Training
  - Regularization
  - Validation
theme: "parameter-optimization"
aliases:
  - Model Fitting
  - Fitting
---

# Model Fitting
#concept #ml

Model Fitting beschrijft hoe een model zich aanpast aan patronen in data, en of die aanpassing te zwak, passend of te sterk is.

## Korte kern

- gaat over hoe goed een model de data volgt
- hangt samen met underfitting en overfitting
- goede fitting balanceert patroonleren en generalisatie

## 1. Wat is het kernprobleem?
Hoe weet je of een model de juiste hoeveelheid structuur uit data leert?

## 2. Intuitieve uitleg
Een model kan te simpel zijn en belangrijke patronen missen, of te complex zijn en zelfs ruis meepakken. Goede fitting zit tussen die twee uitersten.

## 3. Formele structuur
- underfitting = model te simpel
- goede fitting = model leert relevante structuur
- overfitting = model past zich te sterk aan trainingsdetails aan
- fitting beoordeel je best via [[Validation]] of [[Cross-Validation]]

## 4. Snelle vergelijking
- [[Model Fitting]] = mate van aanpassing aan data
- [[Model Training]] = proces dat tot fitting leidt
- [[Regularization]] = hulpmiddel om overfitting af te remmen

## 5. Toepassing
Een SVM met te grote `C` of een te complexe kernel kan overfitten. Een beter afgestemde regularisatie geeft dan een geschiktere fitting.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** fitting gaat over de kwaliteit van de aanpassing; training is het proces dat die aanpassing veroorzaakt.
- **Veelvoorkomende misvatting:** denken dat een perfecte fit op trainingsdata hetzelfde is als goede generalisatie.
- **Link met andere concepten:** [[Model Training]], [[Regularization]], [[Validation]], [[Cross-Validation]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

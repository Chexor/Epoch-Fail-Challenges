---
type: theory
domain: "machine-learning"
parent: "Optimization and Training"
related:
  - Optimization and Training
  - Cross-Validation
  - Grid Search
theme: "model-selection-and-tuning"
aliases:
  - Validation
  - Validation Set
---

# Validation
#concept #ml

Validation is het beoordelen van een model op aparte data die niet gebruikt werd om de parameters te leren.

## Korte kern

- helpt modelkeuzes eerlijker maken
- zit tussen training en test in
- wordt vaak gebruikt voor hyperparametertuning

## 1. Wat is het kernprobleem?
Hoe controleer je modelkeuzes zonder de testset al te "lekken" in je beslissingen?

## 2. Intuitieve uitleg
Je traint op trainingsdata, maar kijkt naar validatiedata om te zien welke instellingen het best generaliseren. Zo hou je de testset achter de hand voor een eerlijk eindoordeel.

## 3. Formele structuur
- train set = parameters leren
- validation set = hyperparameters of modelkeuzes beoordelen
- test set = finale onafhankelijke evaluatie

## 4. Snelle vergelijking
- [[Validation]] = modelkeuzes beoordelen op aparte data
- [[Cross-Validation]] = herhaalde validatie via meerdere splits
- [[Grid Search]] = systematische hyperparameterzoektocht op validatiescores

## 5. Toepassing
Bij SVM kan je verschillende waarden van `C` of `gamma` vergelijken op validatiedata om te zien welke combinatie het best generaliseert.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** validatie dient voor modelselectie; testdata dient voor finale beoordeling.
- **Veelvoorkomende misvatting:** de testset gebruiken om hyperparameters te kiezen.
- **Link met andere concepten:** [[Cross-Validation]], [[Grid Search]], [[Parameters vs Hyperparameters]], [[Model Evaluation]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

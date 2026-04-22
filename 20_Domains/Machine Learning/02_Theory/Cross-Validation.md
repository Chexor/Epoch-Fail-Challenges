---
type: theory
domain: "machine-learning"
parent: "Validation"
related:
  - Validation
  - Grid Search
  - Accuracy
theme: "model-selection-and-tuning"
aliases:
  - Cross-Validation
  - Cross validation
  - K-fold Cross-Validation
---

# Cross-Validation
#concept #ml

Cross-Validation is een validatiemethode waarbij je de data meerdere keren anders splitst om modelprestaties stabieler te schatten.

## Korte kern

- hergebruikt data slim voor meerdere validaties
- geeft robuustere schattingen dan 1 enkele split
- wordt vaak gecombineerd met [[Grid Search]]

## 1. Wat is het kernprobleem?
Hoe verminder je de toevalsinvloed van 1 enkele train-validation-split?

## 2. Intuitieve uitleg
In plaats van 1 keer te splitsen, draai je meerdere rondes. Elke keer is een ander stuk data validatieset. Daarna neem je het gemiddelde van de resultaten.

## 3. Formele structuur
- bij `k-fold cross-validation` split je data in `k` delen
- elke fold wordt 1 keer validatieset
- de andere `k-1` delen vormen dan de trainingset
- finale score is vaak het gemiddelde over alle folds

## 4. Snelle vergelijking
- [[Cross-Validation]] = meerdere validatierondes
- [[Validation]] = algemene validatiegedachte
- [[Grid Search]] = zoekt hyperparameters vaak met cross-validation

## 5. Toepassing
Bij een kleine tot middelgrote dataset kan `5-fold` of `10-fold cross-validation` een betrouwbaardere schatting geven van SVM- of logistic-regressionprestaties.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** cross-validation is een methode om validatie stabieler te maken, geen apart model.
- **Veelvoorkomende misvatting:** denken dat cross-validation de testset vervangt.
- **Link met andere concepten:** [[Validation]], [[Grid Search]], [[Accuracy]], [[Model Evaluation]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

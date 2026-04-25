---
type: atlas
domain: "machine-learning"
parent: [[00_Overzicht Concepten]]
related:
  - Modellen en Algoritmen
theme: "ml-training-eval"
aliases:
  - Atlas Training en Evaluatie
---

# Atlas - Training en Evaluatie
#concept #ml

Atlas-note voor training en evaluatie in Machine Learning.

> Deze note ordent concepten rond modeloptimalisatie, verliesfuncties, validatie en prestatiemeting.

## Korte kern

- ordent optimalisatie (gradient descent) en evaluatie
- linkt verliesfuncties aan modelprestaties
- hub voor concept notes over het trainen en tunen van modellen

## Waarom bestaat deze conceptgroep?
Een model trainen is slechts de helft van het werk. Het begrijpen *hoe* het leert en *hoe goed* het presteert, is cruciaal voor betrouwbare ML.

## Groot plaatje
Training is het iteratief aanpassen van parameters om de fout te minimaliseren; evaluatie bepaalt of die fout voldoende laag is voor de praktijk.

## Kernonderdelen

### Optimalisatie
- [[Optimization and Training]]
- [[Gradient Descent]]
- [[Learning Rate]]
- [[Epoch]]

### Evaluatie & Loss
- [[Loss Function]]
- [[Model Evaluation]]
- [[Accuracy]]
- [[MSE (Mean Squared Error)]]
- [[MAE (Mean Absolute Error)]]
- [[RMSE (Root Mean Squared Error)]]
- [[R2 en R]]

### Validatie
- [[Train Validation Test Split]]
- [[Validation]]
- [[Cross-Validation]]
- [[Overfitting]]
- [[Underfitting]]
- [[Regularization]]
- [[Grid Search]]

## Hoe hangen deze samen?
Optimalisatie (bijv. [[Gradient Descent]]) probeert de [[Loss Function]] te minimaliseren tijdens de training. Evaluatie ([[Model Evaluation]]) op een gesplitste dataset ([[Train Validation Test Split]]) detecteert of het model [[Overfitting]] of [[Underfitting]] vertoont.

## Aanbevolen leerpad
1. [[Model Evaluation]]
2. [[Loss Function]]
3. [[Train Validation Test Split]]
4. [[Optimization and Training]]
5. [[Gradient Descent]]
6. [[Overfitting]] / [[Underfitting]]
7. [[Regularization]]
8. [[Grid Search]]

## Verwante concepten
- [[Atlas - Modellen en Algoritmen]] (deze bepalen *wat* getraind wordt)

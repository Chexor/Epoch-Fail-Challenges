---
type: theory
domain: "machine-learning"
parent: "Optimization and Training"
related:
  - Optimization and Training
  - Soft Margin Classification
  - Grid Search
theme: "model-selection-and-tuning"
aliases:
  - Regularization
  - Penalty
---

# Regularization
#concept #ml

Regularization is het bewust beperken van modelcomplexiteit zodat een model minder snel overfit op trainingsdata.

## Korte kern

- helpt overfitting tegengaan
- straft te complexe modellen af
- hangt vaak samen met hyperparameters zoals `C` of `lambda`

## 1. Wat is het kernprobleem?
Hoe voorkom je dat een model trainingsdata te letterlijk leert en daardoor slechter generaliseert?

## 2. Intuitieve uitleg
Zonder regularisatie mag een model zich soms te sterk aanpassen aan details, ruis of outliers. Regularisatie dwingt het model om eenvoudiger of stabieler te blijven.

## 3. Formele structuur
- regularisatie voegt typisch een strafterm toe voor grote gewichten of complexe grenzen
- in SVM speelt `C` de rol van trade-off tussen marge en fouten
- kleinere `C` betekent in SVM meestal sterkere regularisatie

## 4. Snelle vergelijking
- [[Regularization]] = modelcomplexiteit afremmen
- [[Soft Margin Classification]] = regularisatie binnen SVM-classificatie
- [[Grid Search]] = typische manier om regularisatiesterkte te tunen

## 5. Toepassing
Bij SVM kan een te grote `C` leiden tot een grillige grens die te veel trainingspunten wil respecteren. Een kleinere `C` regulariseert sterker en geeft vaak een robuustere grens.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** regularisatie gaat over generalisatie, niet gewoon over trainingaccuracy maximaliseren.
- **Veelvoorkomende misvatting:** denken dat minder trainingsfouten altijd beter is.
- **Link met andere concepten:** [[Soft Margin Classification]], [[Support Vector Machine]], [[Grid Search]], [[Parameters vs Hyperparameters]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

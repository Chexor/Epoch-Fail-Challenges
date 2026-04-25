---
type: theory
domain: "machine-learning"
parent: "Data Preparation"
related:
  - Data Preparation
  - Model Training
  - Validation
  - Cross-Validation
  - Model Evaluation
theme: "evaluation-workflow"
aliases:
  - Train Validation Test Split
  - Dataset Split
  - Training Validation Test Split
---

# Train Validation Test Split
#concept #ml

Train Validation Test Split is het opdelen van data in aparte subsets om training, modelkeuze en finale evaluatie eerlijk te scheiden.

## Korte kern

- `train` voor parameterleren
- `validation` voor hyperparametertuning en modelkeuze
- `test` voor finale, ongekleurde evaluatie

## 1. Wat is het kernprobleem?
Hoe evalueer je een model eerlijk zonder dat keuzes tijdens ontwikkeling onbewust informatie lekken uit de evaluatiedata?

## 2. Intuitieve uitleg
Zie het als studeren met oefenvragen en een apart examen. Je leert op het oefenmateriaal, test varianten tussendoor, en gebruikt het echte examen pas helemaal op het einde.

## 3. Formele structuur
- `train set`: gebruikt door het algoritme om parameters te leren
- `validation set`: gebruikt om hyperparameters en modelcomplexiteit te kiezen
- `test set`: enkel voor finale evaluatie van generalisatie
- best practices:
  - random split (eventueel gestratificeerd bij classificatie)
  - geen preprocessing fitten op testset
  - testset exact 1 keer gebruiken voor finale check

## 4. Snelle vergelijking
- [[Train Validation Test Split]] = eenvoudige hold-outstrategie met 3 delen
- [[Cross-Validation]] = herhaalde validatie op verschillende folds
- [[Validation]] = algemene stap waarin je modelkeuzes beoordeelt

## 5. Toepassing
Bij polynomial regression train je meerdere graden op de trainingsset, kiest de beste graad via validatiescore, en rapporteert daarna 1 definitieve score op de testset.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** dit gaat over eerlijke evaluatie-opzet, niet over het modelalgoritme zelf.
- **Veelvoorkomende misvatting:** de testset gebruiken tijdens tuning, waardoor de finale score te optimistisch wordt.
- **Link met andere concepten:** [[Data Preparation]], [[Model Training]], [[Validation]], [[Cross-Validation]], [[Model Evaluation]], [[Overfitting]], [[Underfitting]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

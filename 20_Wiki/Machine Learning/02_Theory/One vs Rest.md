---
type: theory
domain: "machine-learning"
parent: "Multinomial Classification"
related:
  - Multinomial Classification
  - Logistic Regression
theme: "classification-foundations"
aliases:
  - One vs Rest
  - One-versus-Rest
  - OvR
---

# One vs Rest
#concept #ml

One vs Rest is een multiclass-strategie waarbij je voor `K` klassen telkens 1 binaire classifier traint tegen alle andere klassen samen.

## Korte kern

- traint `K` binaire classifiers
- elke classifier herkent 1 klasse versus de rest
- de hoogste score of kans wint

## 1. Wat is het kernprobleem?
Hoe maak je van een binair classificatiemodel een aanpak voor meerdere klassen?

## 2. Intuitieve uitleg
Voor elke klasse stel je de vraag: "Is dit klasse A of niet?" Daarna doe je hetzelfde voor klasse B, C, enzovoort. Op het einde kies je de classifier die het sterkst reageert.

## 3. Formele structuur
- voor `K` klassen train je `K` aparte binaire modellen
- model `i` leert klasse `i` tegen alle andere klassen
- voorspelling gebeurt via `argmax` van score of kans

## 4. Snelle vergelijking
- [[One vs Rest]] = multiclass via meerdere binaire modellen
- [[Multinomial Classification]] = breder probleemkader
- [[Logistic Regression]] = vaak basismodel dat binnen OvR gebruikt wordt

## 5. Toepassing
Bij 3 klassen train je 3 classifiers: `A vs rest`, `B vs rest` en `C vs rest`. Het datapunt krijgt de klasse met de hoogste voorspelde waarschijnlijkheid of score.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** OvR is een strategie rond een model, geen apart modeltype.
- **Veelvoorkomende misvatting:** denken dat multiclass altijd een volledig ander algoritme vereist.
- **Link met andere concepten:** [[Multinomial Classification]], [[Logistic Regression]], [[Classification vs Regression]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

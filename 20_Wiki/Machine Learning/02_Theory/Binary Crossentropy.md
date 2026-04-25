---
type: theory
domain: "machine-learning"
parent: "Loss Function"
related:
  - Loss Function
  - Logistic Regression
  - Sigmoid Function
theme: "model-evaluation"
aliases:
  - Binary Crossentropy
  - Binary Cross-Entropy
  - Binary Cross-entropy
  - Log Loss
---

# Binary Crossentropy
#concept #ml

Binary Crossentropy is een loss function voor binaire classificatie die sterke straf geeft aan zelfzekere maar foute kansvoorspellingen.

## Korte kern

- gebruikt voorspelde kansen voor klasse `0` of `1`
- is standaard bij veel binaire classifiers
- past goed bij output via de [[Sigmoid Function]]

## 1. Wat is het kernprobleem?
Hoe meet je bij binaire classificatie hoe fout een voorspelde kans is?

## 2. Intuitieve uitleg
Als het model zegt "99 procent zeker" en toch fout zit, dan moet dat zwaarder bestraft worden dan een onzekere voorspelling. Binary crossentropy doet exact dat.

## 3. Formele structuur
- voor 1 voorbeeld: `L = -(y*log(p) + (1-y)*log(1-p))`
- `y` is het echte label (`0` of `1`)
- `p` is de voorspelde kans op klasse `1`
- als `p` dicht ligt bij het echte label, dan is de loss laag

## 4. Snelle vergelijking
- [[Binary Crossentropy]] = loss voor binaire classificatiekansen
- [[Loss Function]] = brede familie van trainingsfouten
- [[MSE (Mean Squared Error)]] = typische loss voor regressie

## 5. Toepassing
Bij spamdetectie met `y = 1` en voorspelde kans `p = 0.95` is de loss klein. Bij `p = 0.05` is de loss groot, omdat het model zelfzeker de verkeerde kant kiest.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** binary crossentropy is bedoeld voor binaire classificatie, niet voor continue regressietargets.
- **Veelvoorkomende misvatting:** BCE behandelen alsof het gewoon een andere schrijfwijze van MSE is.
- **Link met andere concepten:** [[Loss Function]], [[Logistic Regression]], [[Sigmoid Function]], [[Neural Network]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

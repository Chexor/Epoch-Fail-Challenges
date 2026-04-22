---
type: theory
domain: "machine-learning"
parent: "ML Problem Framing"
related:
  - Classification vs Regression
  - One vs Rest
  - Logistic Regression
theme: "classification-foundations"
aliases:
  - Multinomial Classification
  - Multiclass Classification
---

# Multinomial Classification
#concept #ml

Multinomial Classification is classificatie waarbij een model moet kiezen uit meer dan twee mogelijke klassen.

## Korte kern

- gaat over `K > 2` klassen
- is breder dan binaire classificatie
- kan aangepakt worden via [[One vs Rest]] of multinomiale logistic regression

## 1. Wat is het kernprobleem?
Hoe voorspel je 1 klasse wanneer er meer dan twee mogelijke uitkomsten zijn?

## 2. Intuitieve uitleg
In plaats van alleen `ja/nee` moet het model kiezen uit meerdere labels, zoals `setosa`, `versicolor` of `virginica`.

## 3. Formele structuur
- target heeft meer dan 2 klassen
- output kan gebeuren via meerdere binaire classifiers of via een directe multiclass-output
- vaak gebruik je softmax of strategieen zoals [[One vs Rest]]

## 4. Snelle vergelijking
- [[Multinomial Classification]] = meer dan 2 klassen
- [[Logistic Regression]] = vaak eerst binair uitgelegd
- [[One vs Rest]] = strategie om multiclass via binaire classifiers op te lossen

## 5. Toepassing
De Iris-dataset is een typisch voorbeeld: 1 datapunt moet aan precies 1 van 3 bloemklassen gekoppeld worden.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** multiclass betekent 1 keuze uit meerdere klassen; multi-label betekent meerdere labels tegelijk.
- **Veelvoorkomende misvatting:** multiclass en multi-label door elkaar halen.
- **Link met andere concepten:** [[Classification vs Regression]], [[One vs Rest]], [[Logistic Regression]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

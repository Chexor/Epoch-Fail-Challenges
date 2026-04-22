---
type: theory
domain: "machine-learning"
parent: "Neural Network Models"
related:
  - Neural Network Models
  - Perceptron
  - Step Function
  - Sigmoid Function
  - ReLU
theme: "neural-network-models"
aliases:
  - Activation Functions
  - Activatiefuncties
---

# Activation Functions
#concept #ml

Activation Functions zijn functies die bepalen hoe de gewogen som in een neuron wordt omgezet naar een outputsignaal.

## Korte kern

- voegen niet-lineariteit toe aan neurale netwerken
- bepalen hoe sterk een neuron reageert
- typische voorbeelden zijn [[Step Function]], [[Sigmoid Function]] en [[ReLU]]

## 1. Wat is het kernprobleem?
Hoe zorg je dat een neuraal netwerk meer kan leren dan alleen een lineaire combinatie van inputs?

## 2. Intuitieve uitleg
Na de gewogen som beslist de activatiefunctie wat er "doorgelaten" wordt. Je kan het zien als een regel die bepaalt of een neuron zwak, sterk, binair of gradueel activeert.

## 3. Formele structuur
- input aan een neuron: `z = w1*x1 + ... + wn*xn + b`
- output van het neuron: `a = f(z)`
- zonder activatiefunctie blijven meerdere lagen samen nog steeds lineair
- de keuze van `f` bepaalt mee leerbaarheid, interpretatie en outputbereik

## 4. Snelle vergelijking
- [[Activation Functions]] = overkoepelende familie van activatiefuncties
- [[Step Function]] = harde 0/1-beslissing
- [[Sigmoid Function]] = gladde output tussen `0` en `1`
- [[ReLU]] = laat positieve waarden door en kapt negatieve af

## 5. Toepassing
In een classifier kan een hidden neuron eerst een gewogen som berekenen en daarna `sigmoid` of `ReLU` toepassen, zodat het netwerk niet-lineaire patronen kan leren.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** een activatiefunctie is een onderdeel van een neuron, geen volledig model.
- **Veelvoorkomende misvatting:** denken dat extra lagen zonder activatiefuncties automatisch complexere patronen leren.
- **Link met andere concepten:** [[Neural Network]], [[Perceptron]], [[Step Function]], [[Sigmoid Function]], [[ReLU]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

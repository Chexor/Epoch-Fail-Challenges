---
type: atom
domain: "machine-learning"
parent: "Activation Functions"
related:
  - Activation Functions
  - Logistic Regression
  - Step Function
  - Binary Crossentropy
theme: "neural-network-models"
aliases:
  - Sigmoid Function
  - Sigmoid
  - Logistic Function
---

# Sigmoid Function
#concept #ml

De sigmoid function is een activatiefunctie die elke input omzet naar een waarde tussen `0` en `1`.

## Korte kern

- geeft een gladde output tussen `0` en `1`
- wordt vaak gelezen als kansachtige output
- is belangrijk in [[Logistic Regression]] en binaire classificatie

## 1. Wat is het kernprobleem?
Hoe zet je een lineaire score om naar een zachte, continue output die je als kans kan interpreteren?

## 2. Intuitieve uitleg
De sigmoid duwt heel negatieve waarden dicht bij `0` en heel positieve waarden dicht bij `1`. Waarden rond `0` komen in het midden uit.

## 3. Formele structuur
- definitie: `sigma(z) = 1 / (1 + e^-z)`
- outputbereik: `(0, 1)`
- grote positieve `z` geven output dicht bij `1`
- grote negatieve `z` geven output dicht bij `0`

## 4. Snelle vergelijking
- [[Sigmoid Function]] = gladde output tussen `0` en `1`
- [[Step Function]] = harde binaire output
- [[ReLU]] = niet begrensd aan de positieve kant

## 5. Toepassing
Bij [[Logistic Regression]] wordt eerst een lineaire score `z` berekend. Daarna zet de sigmoid die score om naar een voorspelde kans op de positieve klasse.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** sigmoid geeft een continue output; de uiteindelijke klassebeslissing vraagt vaak nog een drempel.
- **Veelvoorkomende misvatting:** de sigmoidoutput verwarren met een definitief label in plaats van een kans.
- **Link met andere concepten:** [[Logistic Regression]], [[Activation Functions]], [[Step Function]], [[Binary Crossentropy]], [[Neural Network]]

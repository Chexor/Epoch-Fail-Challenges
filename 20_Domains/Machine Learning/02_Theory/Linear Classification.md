---
type: theory
domain: "machine-learning"
parent: "ML Problem Framing"
related:
  - Classification vs Regression
  - Logistic Regression
  - Perceptron
  - Support Vector Machine
theme: "classification-foundations"
aliases:
  - Linear Classification
---

# Linear Classification
#concept #ml

Linear Classification is classificatie waarbij een model klassen scheidt met een lineaire beslissingsgrens zoals een rechte, vlak of hypervlak.

## Korte kern

- gebruikt een lineaire score in de inputruimte
- scheidt klassen met een decision boundary
- typische modellen zijn [[Perceptron]], [[Logistic Regression]] en [[Support Vector Machine]]

## 1. Wat is het kernprobleem?
Hoe beslis je tot welke klasse een datapunt behoort wanneer je een rechte scheidingsgrens wil gebruiken?

## 2. Intuitieve uitleg
Bij lineaire classificatie trek je een scheidingslijn tussen klassen. Aan de ene kant ligt klasse `0`, aan de andere klasse `1`. In hogere dimensies wordt die lijn een vlak of hypervlak.

## 3. Formele structuur
- scorefunctie: `z = b + w1*x1 + ... + wn*xn`
- decision boundary: `z = 0`
- 1 feature: boundary is een punt of threshold
- 2 features: boundary is een rechte
- n features: boundary is een hypervlak

## 4. Snelle vergelijking
- [[Linear Classification]] = classificatie met lineaire scheidingsgrens
- [[Logistic Regression]] = lineaire classifier met kansoutput
- [[Support Vector Machine]] = lineaire of niet-lineaire classifier met marges

## 5. Toepassing
Voor een simpele dataset met `x1` en `x2` kan een model een rechte leren die `spam` en `geen spam` of `aan/uit` van elkaar scheidt.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** lineaire classificatie zegt iets over de vorm van de scheidingsgrens, niet per se over het specifieke algoritme.
- **Veelvoorkomende misvatting:** denken dat classificatie altijd niet-lineair of complex moet zijn.
- **Link met andere concepten:** [[Classification vs Regression]], [[Perceptron]], [[Logistic Regression]], [[Support Vector Machine]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

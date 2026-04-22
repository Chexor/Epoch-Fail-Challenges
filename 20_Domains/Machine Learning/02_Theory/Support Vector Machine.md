---
type: theory
domain: "machine-learning"
parent: "Linear Modeling"
related:
  - Linear Classification
  - Support Vectors
  - Hard Margin Classification
  - Soft Margin Classification
  - Hinge Loss
theme: "linear-modeling"
aliases:
  - Support Vector Machine
  - Support Vector Machines
  - SVM
---

# Support Vector Machine
#concept #ml

Een Support Vector Machine is een supervised model dat een decision boundary zoekt met zo groot mogelijke marge tussen de klassen.

## Korte kern

- afgekort als `SVM`
- zoekt een brede marge rond de scheidingsgrens
- werkt voor lineaire en niet-lineaire problemen

## 1. Wat is het kernprobleem?
Hoe vind je niet zomaar een scheidingslijn, maar een scheidingslijn die ook goed generaliseert op nieuwe data?

## 2. Intuitieve uitleg
Een SVM zoekt niet gewoon een lijn tussen de klassen. Het probeert de "straat" tussen de klassen zo breed mogelijk te maken. Dat maakt het model vaak robuuster voor nieuwe voorbeelden.

## 3. Formele structuur
- decision boundary is een hypervlak
- de marge wordt bepaald door de dichtste punten bij de grens
- die punten heten [[Support Vectors]]
- lineaire SVM gebruikt vaak [[Hinge Loss]]
- met kernels kan SVM ook niet-lineaire grenzen leren

## 4. Snelle vergelijking
- [[Support Vector Machine]] = maximaliseert marge rond de grens
- [[Perceptron]] = eenvoudige lineaire classifier met foutupdates
- [[Logistic Regression]] = lineaire classifier met kansoutput

## 5. Toepassing
Bij een kleine tot middelgrote classificatiedataset kan een SVM vaak een sterke decision boundary vinden, zeker wanneer de klassen redelijk goed gescheiden zijn.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** SVM optimaliseert op marge, niet op kansvoorspellingen.
- **Veelvoorkomende misvatting:** denken dat SVM altijd lineair is; met kernels kan het ook niet-lineair werken.
- **Link met andere concepten:** [[Linear Classification]], [[Support Vectors]], [[Hard Margin Classification]], [[Soft Margin Classification]], [[Hinge Loss]], [[Scaling]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

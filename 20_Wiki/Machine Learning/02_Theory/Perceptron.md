---
type: theory
domain: "machine-learning"
parent: "Neural Network Models"
related:
  - Neural Network Models
  - Neural Network
  - Activation Functions
  - Step Function
  - Logistic Regression
theme: "neural-network-models"
aliases:
  - Perceptron
---

# Perceptron
#concept #ml

Een perceptron is het eenvoudigste neurale classificatiemodel dat een gewogen som van inputs gebruikt en daar een binaire beslissing op toepast.

## Korte kern

- is een vroege bouwsteen van neurale netwerken
- maakt een lineaire scheidingsbeslissing
- gebruikt klassiek een [[Step Function]] als activatie

## 1. Wat is het kernprobleem?
Hoe laat je een eenvoudig model beslissen tussen twee klassen op basis van meerdere inputfeatures?

## 2. Intuitieve uitleg
Een perceptron telt de inputs niet gewoon op, maar geeft elke input een gewicht. Daarna kijkt het of de totale score boven of onder een drempel valt. Zo krijg je een ja/nee-beslissing.

## 3. Formele structuur
- gewogen som: `z = w1*x1 + ... + wn*xn + b`
- output: `y_hat = step(z)`
- een perceptron kan alleen lineair scheidbare problemen correct oplossen
- meerdere perceptrons samen vormen de basis van grotere [[Neural Network|neurale netwerken]]

## 4. Snelle vergelijking
- [[Perceptron]] = eenvoudig binair beslismodel met harde activatie
- [[Logistic Regression]] = gebruikt ook een lineaire score, maar zet die om naar een kans
- [[Neural Network]] = bredere architectuur met meerdere neuronen en lagen

## 5. Toepassing
Voor een simpele classifier met twee features kan een perceptron beslissen of een datapunt aan de ene of andere kant van een scheidingslijn ligt.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** een perceptron geeft typisch een harde klasse-uitkomst en geen kans.
- **Veelvoorkomende misvatting:** denken dat een enkel perceptron complexe niet-lineaire patronen kan leren.
- **Link met andere concepten:** [[Neural Network]], [[Activation Functions]], [[Step Function]], [[Sigmoid Function]], [[Logistic Regression]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

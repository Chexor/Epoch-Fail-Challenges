---
type: concept-topic
domain: "machine-learning"
parent: "ML Tooling and Frameworks"
related:
  - ML Tooling and Frameworks
  - Neural Network
  - Deep Learning
theme: "ml-tooling-and-frameworks"
aliases:
  - Keras
---

# Keras
#concept #ml

## 1. Wat is het kernprobleem?
Je wil neurale netwerken bouwen zonder veel lage-niveaucode te schrijven.

## 2. Intuitieve uitleg
Keras is een gebruiksvriendelijke API bovenop TensorFlow. Je bouwt een model uit lagen, kiest een loss en optimizer, en traint daarna met `fit()`.

## 3. Formele structuur
- Model opbouwen: `Sequential()` of functionele API
- Compileren: kies loss en optimizer
- Trainen: `model.fit(...)`
- Voorspellen: `model.predict(...)`

## 4. Toepassing
Voor een eenvoudige regressietaak kan je 1 output-neuron gebruiken met loss `MSE` en optimizer `SGD` of `adam`.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** `Keras` is een hoog-niveau API voor modelbouw en training, geen afzonderlijk leeralgoritme.
- **Veelvoorkomende misvatting:** vergeten dat keuzes zoals loss, optimizer en learning rate het leerproces mee bepalen.
- **Link met andere concepten:** [[Sequential Neural Net]], [[SGD (Stochastic Gradient Descent)]], [[MSE (Mean Squared Error)]]

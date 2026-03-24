---
type: concept-topic
domain: "machine-learning"
parent: "Neural Network Models"
related:
  - Neural Network Models
  - Neural Network
  - Keras
theme: "neural-network-models"
aliases:
  - Sequential Neural Net
---

# Sequential Neural Net
#concept #ml

## 1. Wat is het kernprobleem?
Je wil een eenvoudig neuraal netwerk waarbij data laag voor laag vooruit stroomt.

## 2. Intuitieve uitleg
Bij een sequential model staat elke laag netjes achter de vorige. De output van laag 1 gaat naar laag 2, enzovoort, tot je een voorspelling krijgt.

## 3. Formele structuur
- Typische volgorde: input -> hidden layer(s) -> output
- In Keras: `Sequential()` met `Dense(...)` lagen
- Geen vertakkingen of meerdere parallelle paden

## 4. Toepassing
Voor een eenvoudige regressietaak kan je werken met:
- invoerlaag voor je features
- 1 hidden layer
- outputlaag met 1 neuron

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** een `Sequential`-model is een specifieke netwerkstructuur, niet de algemene vorm van elk neuraal netwerk.
- **Veelvoorkomende misvatting:** denken dat alle neurale netwerken sequential zijn.
- **Link met andere concepten:** [[Keras]], [[Neural Network]], [[Deep Learning]], [[Convolutional Neural Network (CNN)]]

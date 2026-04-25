---
type: theory
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

Sequential Neural Net kort uitgelegd: wat het is, waarom het telt en wanneer je het gebruikt.
## Korte kern

- kernidee van dit concept
- belangrijkste rol binnen de ML-flow
- link met verwante concepten

## 1. Wat is het kernprobleem?
Je wil een eenvoudig neuraal netwerk waarbij data laag voor laag vooruit stroomt.

## 2. Intuitieve uitleg
Bij een sequential model staat elke laag netjes achter de vorige. De output van laag 1 gaat naar laag 2, enzovoort, tot je een voorspelling krijgt.

## 3. Formele structuur
- Typische volgorde: input -> hidden layer(s) -> output
- In Keras: `Sequential()` met `Dense(...)` lagen
- Geen vertakkingen of meerdere parallelle paden

## 4. Snelle vergelijking

- Plaats dit concept kort tegenover 1-2 verwante concepten uit deze map.

## 5. Toepassing
Voor een eenvoudige regressietaak kan je werken met:
- invoerlaag voor je features
- 1 hidden layer
- outputlaag met 1 neuron

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** een `Sequential`-model is een specifieke netwerkstructuur, niet de algemene vorm van elk neuraal netwerk.
- **Veelvoorkomende misvatting:** denken dat alle neurale netwerken sequential zijn.
- **Link met andere concepten:** [[Keras]], [[Neural Network]], [[Deep Learning]], [[Convolutional Neural Network (CNN)]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

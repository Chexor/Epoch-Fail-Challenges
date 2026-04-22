---
type: theory
domain: "machine-learning"
parent: "Optimization and Training"
related:
  - Optimization and Training
  - Gradient Descent
  - SGD (Stochastic Gradient Descent)
theme: "parameter-optimization"
aliases:
  - Mini-batch Gradient Descent
---

# Mini-batch Gradient Descent
#concept #ml

Mini-batch Gradient Descent kort uitgelegd: wat het is, waarom het telt en wanneer je het gebruikt.
## Korte kern

- kernidee van dit concept
- belangrijkste rol binnen de ML-flow
- link met verwante concepten

## 1. Wat is het kernprobleem?
Je zoekt een compromis tussen trage batch-updates en ruizige SGD-updates.

## 2. Intuitieve uitleg
In plaats van 1 datapunt of de volledige dataset te gebruiken, neem je een kleine groep, bv. 32 of 64 samples. Dat geeft meestal een goede balans tussen snelheid en stabiliteit.

## 3. Formele structuur
- `1 < batch size < n`
- Update gebeurt na elke mini-batch
- Veel gebruikt in neurale netwerken

## 4. Snelle vergelijking

- Plaats dit concept kort tegenover 1-2 verwante concepten uit deze map.

## 5. Toepassing
Bij `batch size = 32` en 320 samples krijg je 10 updates per epoch.
Dat is meestal efficiënter dan 320 losse SGD-updates en lichter dan 1 grote batch-update.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** `mini-batch gradient descent` zit tussen batch training en `SGD` in.
- **Veelvoorkomende misvatting:** `batch size` verwarren met een modelparameter die geleerd wordt.
- **Link met andere concepten:** [[SGD (Stochastic Gradient Descent)]], [[Learning Rate]], [[Epoch]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

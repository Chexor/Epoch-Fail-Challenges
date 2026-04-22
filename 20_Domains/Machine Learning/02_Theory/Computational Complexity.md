---
type: theory
domain: "machine-learning"
parent: "Optimization and Training"
related:
  - Optimization and Training
  - SGD (Stochastic Gradient Descent)
  - Support Vector Machine
theme: "model-selection-and-tuning"
aliases:
  - Computational Complexity
  - Time Complexity
  - Complexity
  - Big O
---

# Computational Complexity
#concept #ml

Computational Complexity beschrijft hoeveel tijd of middelen een algoritme nodig heeft als de dataset of het probleem groter wordt.

## Korte kern

- helpt modellen praktisch vergelijken
- wordt vaak uitgedrukt in `Big O`
- beïnvloedt welke methode haalbaar is op grote data

## 1. Wat is het kernprobleem?
Hoe schat je in of een algoritme nog praktisch bruikbaar blijft wanneer het aantal samples of features groeit?

## 2. Intuitieve uitleg
Sommige methodes werken prima op kleine datasets, maar worden te traag op grote datasets. Complexity helpt je op voorhand inschatten waar de bottlenecks zitten.

## 3. Formele structuur
- `time complexity` beschrijft hoe rekentijd schaalt
- `Big O` noteert groeigedrag, zoals `O(n)` of `O(n^2)`
- in ML kijk je vaak naar afhankelijkheid van aantal samples `m` en features `n`

## 4. Snelle vergelijking
- [[Computational Complexity]] = rekentijd en schaalbaarheid begrijpen
- [[SGD (Stochastic Gradient Descent)]] = vaak interessant voor grote datasets
- [[Support Vector Machine]] = kan zwaar worden afhankelijk van solver en kernel

## 5. Toepassing
Bij lineaire SVM of SGD is training vaak beter schaalbaar dan bij kernel-SVM's op grote datasets. Complexity helpt dan kiezen welke aanpak realistisch is.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** complexity gaat over schaalbaarheid van computation, niet direct over modelkwaliteit.
- **Veelvoorkomende misvatting:** het beste model puur op accuracy kiezen zonder rekentijd mee te nemen.
- **Link met andere concepten:** [[Support Vector Machine]], [[SGD (Stochastic Gradient Descent)]], [[Grid Search]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

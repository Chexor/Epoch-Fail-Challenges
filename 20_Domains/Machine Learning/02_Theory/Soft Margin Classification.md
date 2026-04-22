---
type: theory
domain: "machine-learning"
parent: "Support Vector Machine"
related:
  - Support Vector Machine
  - Hard Margin Classification
  - Hinge Loss
theme: "linear-modeling"
aliases:
  - Soft Margin Classification
---

# Soft Margin Classification
#concept #ml

Soft Margin Classification is een SVM-benadering die een compromis zoekt tussen een brede marge en een beperkt aantal fouten of marge-overtredingen.

## Korte kern

- realistischer dan hard margin
- laat sommige overtredingen toe
- gebruikt de hyperparameter `C` om de trade-off te sturen

## 1. Wat is het kernprobleem?
Hoe hou je een decision boundary robuust wanneer de data niet perfect lineair scheidbaar is?

## 2. Intuitieve uitleg
In echte data zitten vaak outliers of overlap. Daarom mag een SVM soms punten binnen de marge of zelfs aan de verkeerde kant toelaten, zolang de totale scheiding nog sterk blijft.

## 3. Formele structuur
- zoekt balans tussen grote marge en weinig classificatiefouten
- `C` bepaalt hoe zwaar overtredingen bestraft worden
- kleinere `C` betekent typisch meer regularisatie en bredere marge

## 4. Snelle vergelijking
- [[Soft Margin Classification]] = marge plus toegelaten overtredingen
- [[Hard Margin Classification]] = geen overtredingen toegelaten
- [[Hinge Loss]] = typische loss die bij deze trade-off past

## 5. Toepassing
Bij een dataset met outliers kan soft margin een stabielere grens leren dan hard margin, omdat het model niet alles forceert om perfect gescheiden te zijn.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** soft margin regulariseert expliciet de scheiding in plaats van perfecte trainingaccuracy te forceren.
- **Veelvoorkomende misvatting:** denken dat een grotere `C` altijd beter is omdat het minder trainingsfouten geeft.
- **Link met andere concepten:** [[Support Vector Machine]], [[Hard Margin Classification]], [[Hinge Loss]], [[Regularization]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

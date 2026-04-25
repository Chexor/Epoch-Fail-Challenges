---
type: theory
domain: "machine-learning"
parent: "Machine Learning"
related:
  - Classification vs Regression
  - Overfitting
  - Underfitting
  - Random Forest
theme: "tree-based-models"
aliases:
  - Decision Trees
  - Decision Tree
  - Beslissingsboom
---

# Decision Trees
#concept #ml

Decision Trees zijn modellen die voorspellingen maken via opeenvolgende if-then splitsingen in een boomstructuur.

## Korte kern

- splitst data stap voor stap op basis van feature-vragen
- werkt voor zowel classificatie als regressie
- is interpreteerbaar maar gevoelig voor overfitting

## 1. Wat is het kernprobleem?
Hoe maak je beslissingen op basis van data via duidelijke, stapsgewijze regels?

## 2. Intuitieve uitleg
Een decision tree lijkt op een beslisdiagram: bij elk knooppunt stel je een vraag (bijv. `feature <= drempel?`), en via de takken kom je uit bij een voorspelling.

## 3. Formele structuur
- opbouw:
  - `root node`: eerste split
  - `internal nodes`: bijkomende splits
  - `leaf nodes`: finale voorspelling
- taken:
  - classificatie: voorspelt klasse
  - regressie: voorspelt numerieke waarde
- complexiteit groeit met diepte en aantal bladeren

## 4. Snelle vergelijking
- [[Decision Trees]] = enkelvoudig boommodel
- [[Random Forest]] = ensemble van veel bomen
- [[Linear Regression]] = lineair model zonder boomstructuur

## 5. Toepassing
Voor kredietbeslissingen kan een tree regels leren zoals: inkomen boven drempel, schuldgraad onder limiet, en dan lening goedkeuren of weigeren.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** een tree leert hierarchische regels, geen lineaire formule.
- **Veelvoorkomende misvatting:** denken dat dieper altijd beter is; te diepe bomen overfitten vaak.
- **Link met andere concepten:** [[Machine Learning]], [[Classification vs Regression]], [[Random Forest]], [[Overfitting]], [[Underfitting]], [[Regularization]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

---
type: theory
domain: "machine-learning"
parent: "Decision Trees"
related:
  - Decision Trees
  - Classification vs Regression
  - Overfitting
theme: "tree-based-models"
aliases:
  - Random Forest
  - Random Forests
---

# Random Forest
#concept #ml

Random Forest is een ensemblemethode die veel decision trees combineert om robuustere voorspellingen te maken.

## Korte kern

- traint meerdere bomen op verschillende data-samples
- combineert voorspellingen via voting of averaging
- vermindert variantie en overfitting t.o.v. 1 losse tree

## 1. Wat is het kernprobleem?
Hoe maak je boommodellen stabieler zodat ze minder gevoelig zijn voor toevallige patronen in 1 trainingsset?

## 2. Intuitieve uitleg
In plaats van 1 expert te vertrouwen, vraag je de mening van veel experts met verschillende invalshoeken. Het gemiddelde oordeel is meestal betrouwbaarder.

## 3. Formele structuur
- elke boom krijgt een bootstrap-sample van de trainingsdata
- per split wordt vaak een willekeurige subset van features bekeken
- output:
  - classificatie: majority vote
  - regressie: gemiddelde van boomoutputs

## 4. Snelle vergelijking
- [[Decision Trees]] = 1 boom, vaak goed interpreteerbaar maar instabieler
- [[Random Forest]] = veel bomen, doorgaans stabieler en accurater
- [[Gradient Descent]] = optimalisatiemethode, geen boom-ensemble

## 5. Toepassing
Bij churn-voorspelling geeft een random forest vaak betere generalisatie dan 1 enkele decision tree, vooral wanneer data ruis bevat.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** random forest is een ensemble bovenop decision trees, geen volledig ander type basisboom.
- **Veelvoorkomende misvatting:** denken dat random forest automatisch interpreteerbaar is zoals 1 kleine tree.
- **Link met andere concepten:** [[Decision Trees]], [[Classification vs Regression]], [[Overfitting]], [[Model Evaluation]], [[Cross-Validation]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

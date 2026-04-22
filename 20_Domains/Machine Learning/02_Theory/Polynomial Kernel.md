---
type: theory
domain: "machine-learning"
parent: "Support Vector Machine"
related:
  - Support Vector Machine
  - Kernel Trick
  - Polynomial Regression
theme: "linear-modeling"
aliases:
  - Polynomial Kernel
---

# Polynomial Kernel
#concept #ml

De Polynomial Kernel is een kernel voor SVM's die niet-lineaire grenzen mogelijk maakt door impliciet polynomiale featurecombinaties mee te nemen.

## Korte kern

- werkt alsof extra machten en combinaties van features toegevoegd worden
- gebruikt de [[Kernel Trick]]
- heeft hyperparameters zoals `degree` en `coef0`

## 1. Wat is het kernprobleem?
Hoe modelleer je polynomiale niet-lineariteit zonder alle extra features expliciet toe te voegen?

## 2. Intuitieve uitleg
Net zoals bij [[Polynomial Regression]] kan je denken aan termen zoals `x^2`, `x^3` en combinaties van features. De polynomial kernel doet dat impliciet binnen de SVM-berekening.

## 3. Formele structuur
- polynomiale kernels hangen typisch af van `degree`
- `coef0` stuurt de balans tussen lage en hoge machten
- hogere `degree` kan flexibeler zijn, maar verhoogt risico op overfitting

## 4. Snelle vergelijking
- [[Polynomial Kernel]] = polynomiale niet-lineariteit via kernels
- [[Gaussian RBF Kernel]] = lokale, afstandsgebaseerde niet-lineariteit
- [[Polynomial Regression]] = expliciete polynomiale feature-uitbreiding in regressie

## 5. Toepassing
Voor een dataset die met een rechte niet scheidbaar is, kan een polynomial kernel een gebogen grens leren zonder alle polynomiale features apart te construeren.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** polynomial kernel gebruikt impliciete feature-uitbreiding, niet expliciete kolomtoevoeging.
- **Veelvoorkomende misvatting:** denken dat hogere `degree` automatisch betere prestaties geeft.
- **Link met andere concepten:** [[Kernel Trick]], [[Support Vector Machine]], [[Polynomial Regression]], [[Grid Search]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

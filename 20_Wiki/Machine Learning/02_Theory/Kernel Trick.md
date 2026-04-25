---
type: theory
domain: "machine-learning"
parent: "Support Vector Machine"
related:
  - Support Vector Machine
  - Polynomial Kernel
  - Gaussian RBF Kernel
theme: "linear-modeling"
aliases:
  - Kernel Trick
---

# Kernel Trick
#concept #ml

De Kernel Trick laat een model werken alsof het data naar een hogere-dimensionale feature space projecteert zonder die extra features expliciet te berekenen.

## Korte kern

- maakt niet-lineaire grenzen mogelijk
- vermijdt expliciete feature-expansie
- is vooral bekend bij [[Support Vector Machine|SVM's]]

## 1. Wat is het kernprobleem?
Hoe leer je een niet-lineaire decision boundary zonder een explosie aan expliciete extra features te maken?

## 2. Intuitieve uitleg
Soms wordt data pas scheidbaar als je ze in een rijkere ruimte bekijkt. De kernel trick doet alsof je die rijkere ruimte gebruikt, maar rekent slimmer zodat je die ruimte niet echt hoeft uit te schrijven.

## 3. Formele structuur
- een kernel meet impliciet gelijkenis in een hogere-dimensionale ruimte
- typische kernels zijn [[Polynomial Kernel]] en [[Gaussian RBF Kernel]]
- hierdoor kan een lineair algoritme in feature space een niet-lineaire grens geven in de originele ruimte

## 4. Snelle vergelijking
- [[Kernel Trick]] = impliciete feature-transformatie
- [[Polynomial Kernel]] = kernel voor polynomiale relaties
- [[Gaussian RBF Kernel]] = kernel op basis van afstand en lokale gelijkenis

## 5. Toepassing
Bij een niet-lineair scheidbare dataset kan een SVM met kernel trick toch een gebogen decision boundary leren zonder alle polynomiale of similarity features expliciet toe te voegen.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** de kernel trick is een rekenidee, geen apart model.
- **Veelvoorkomende misvatting:** denken dat kernels altijd beter zijn dan lineaire modellen.
- **Link met andere concepten:** [[Support Vector Machine]], [[Polynomial Kernel]], [[Gaussian RBF Kernel]], [[Scaling]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

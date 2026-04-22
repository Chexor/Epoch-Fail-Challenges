---
type: practice
domain: "machine-learning"
parent: "Gradient Descent"
related:
  - Gradient
  - Learning Rate
  - Linear Regression
theme: "parameter-optimization"
aliases:
  - Gradient Descent Worked Example
  - Gradient Descent
---

# Gradient Descent Worked Example
#concept #ml

Gradient Descent Worked Example kort uitgelegd: wat het is, waarom het telt en wanneer je het gebruikt.
## Ondersteund concept
- [[Gradient Descent]]

## Doel van deze uitwerking
Deze note toont stap voor stap hoe gradient descent een parameter bijstuurt op basis van de fout. Het doel is niet alleen de formule zien, maar ook voelen hoe elke update een model dichter bij een beter antwoord brengt.

## Context
Gebruik dit voorbeeld wanneer je wil begrijpen hoe een model leert uit foutinformatie, bijvoorbeeld bij lineaire regressie.

## Uitwerking
1. Stel dat een model start met parameter `theta = 8`.
2. De berekende gradient is `3`, wat betekent dat de fout stijgt in die richting.
3. Kies een learning rate `alpha = 0.1`.
4. Update de parameter met `theta = theta - alpha * gradient`.
5. Nieuwe waarde: `theta = 8 - 0.1 * 3 = 7.7`.
6. Herhaal dit proces tot de updates klein worden en de fout nauwelijks nog daalt.

## Wat toont dit voorbeeld?
- gradient descent verandert parameters niet willekeurig, maar in de richting die de fout verlaagt
- de learning rate bepaalt hoe groot elke stap is en heeft dus veel invloed op convergentie

## Typische fouten
- een te grote learning rate kiezen waardoor het model overspringt of divergeert
- de gradient interpreteren als de nieuwe parameter zelf in plaats van als stuursignaal

## Verwante concepten
- [[Gradient]]
- [[Learning Rate]]
- [[Linear Regression]]

## Wat studeer je hierna?
- [[Gradient Descent]]
- [[SGD (Stochastic Gradient Descent)]]
- [[00_Overzicht Machine Learning Concepten]]

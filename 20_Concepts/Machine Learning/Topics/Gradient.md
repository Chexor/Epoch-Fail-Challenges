---
type: concept-topic
domain: "machine-learning"
parent: "Optimization and Training"
related:
  - Optimization and Training
  - Derivative (Afgeleide)
  - Gradient Descent
theme: "calculus-and-optimization"
aliases:
  - Gradient
---

# Gradient
#concept #ml

## 1. Wat is het kernprobleem?
Bij functies met meerdere variabelen heb je meer nodig dan 1 afgeleide om de steilste richting te kennen.

## 2. Intuitieve uitleg
De gradient is een pijl die wijst naar de richting van de snelste stijging van een functie. Wil je een minimum vinden, dan beweeg je in de omgekeerde richting.

## 3. Formele structuur
- `nabla f = [df/dx1, df/dx2, ..., df/dxn]`
- Grootte van de gradient zegt hoe steil de functie verandert
- Richting `-nabla f` gebruik je voor daling

## 4. Toepassing
Bij een loss function met meerdere parameters gebruik je de gradient om te bepalen hoe elk gewicht moet worden aangepast.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** de `gradient` wijst naar de snelste stijging; voor daling gebruik je `-gradient`.
- **Veelvoorkomende misvatting:** zeggen dat de gradient zelf naar het minimum wijst.
- **Link met andere concepten:** [[Derivative (Afgeleide)]], [[Gradient Descent]]

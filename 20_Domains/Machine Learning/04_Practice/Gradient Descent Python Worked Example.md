---
type: practice
domain: "machine-learning"
parent: "Gradient Descent"
related:
  - Gradient Descent
  - Gradient Descent Worked Example
  - Gradient
  - Learning Rate
theme: "python-ml-implementations"
aliases:
  - Gradient Descent Python Worked Example
  - Gradient Descent Python Example
---

# Gradient Descent Python Worked Example
#concept #ml

Gradient Descent Python Worked Example toont hoe 1 update-stap een parameter verlaagt op basis van learning rate en gradient.

## Korte kern

- gebruikt `theta = theta - alpha * gradient`
- toont 1 update-stap in pure Python
- maakt de rol van `learning rate` expliciet zichtbaar

## Ondersteund concept
- [[Gradient Descent]]

## Doel van deze uitwerking
Deze note toont de kleinste leesbare Python-vorm van `gradient descent`, zodat de parameterupdate direct begrijpbaar wordt.

## Context
Gebruik dit wanneer je de overgang wil zien van formule naar code zonder extra ML-library.

## Codevoorbeeld
```python
def gradient_descent_step(theta, learning_rate, gradient):
    return theta - learning_rate * gradient


theta = 5.0
gradient = 2.0
learning_rate = 0.1

print(gradient_descent_step(theta, learning_rate, gradient))
```

## Stap-voor-stap uitleg
- `theta` is de huidige parameterwaarde
- `gradient` zegt in welke richting de fout stijgt
- de update gaat in de tegengestelde richting van die gradient
- `learning_rate` bepaalt hoe groot de stap is

## Verwachte output of gedrag
- de nieuwe parameter wordt hier `4.8`
- grotere gradients of learning rates geven grotere updates

## Uitwerking
1. Start met een parameterwaarde.
2. Bepaal de gradient van de loss.
3. Trek `learning_rate * gradient` af.
4. Herhaal dit iteratief.

## Wat toont dit voorbeeld?
- hoe een leerregel er in code echt uitziet
- waarom te grote stapgroottes instabiel kunnen worden

## Typische fouten
- de verkeerde richting updaten
- learning rate en gradient inhoudelijk door elkaar halen

## Verwante concepten
- [[Gradient Descent]]
- [[Gradient Descent Worked Example]]
- [[Gradient]]
- [[Learning Rate]]

## Begripsafbakening en verbanden
- **Kernonderscheid:** deze note toont 1 enkele update-stap, niet een volledige trainingslus over een dataset.
- **Veelvoorkomende misvatting:** denken dat gradient descent altijd vanzelf convergeert; learning rate en loss-landschap doen ertoe.
- **Link met andere concepten:** [[Gradient Descent]], [[Gradient Descent Worked Example]], [[Gradient]], [[Learning Rate]], [[SGD (Stochastic Gradient Descent)]], [[Linear Regression]]

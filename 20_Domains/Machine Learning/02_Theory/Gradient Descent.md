---
type: theory
domain: "machine-learning"
parent: "Optimization and Training"
related:
  - Optimization and Training
  - Gradient
  - Learning Rate
  - Gradient Descent Worked Example
  - Gradient Descent Python Worked Example
  - Linear Regression
theme: "parameter-optimization"
aliases:
  - Gradient Descent
---

# Gradient Descent
#concept #ml

Gradient Descent is een iteratieve optimalisatiemethode die parameters stap voor stap aanpast in de richting die de loss verlaagt.

## Korte kern

- gebruikt de gradient om de daalrichting te bepalen
- update parameters iteratief
- is een kernmechanisme achter veel ML- en deep-learningtraining

## 1. Wat is het kernprobleem?
Hoe vind je goede parameters wanneer je de loss niet rechtstreeks of niet handig exact kan oplossen?

## 2. Intuitieve uitleg
Stel je een heuvelachtig landschap voor waarbij hoogte gelijk is aan fout. Gradient descent zet telkens een stap naar beneden tot je in een dal terechtkomt.

## 3. Formele structuur
- Update: `theta = theta - alpha * nabla L(theta)`
- `theta` = parameters
- `alpha` = learning rate
- `nabla L(theta)` = gradient van de loss

## 4. Snelle vergelijking

- [[Gradient Descent]] = iteratief optimaliseren via gradiënten
- [[OLS (Ordinary Least Squares)]] = gesloten-formule-oplossing in een specifiek lineair geval
- [[SGD (Stochastic Gradient Descent)]] = stochastic variant van gradient descent

## 5. Toepassing
Procedure:
1. start met beginwaarden voor de parameters
2. bereken voorspellingen en loss
3. bereken de gradient
4. update de parameters
5. herhaal tot de loss weinig nog daalt

Kort Python-voorbeeld:

```python
def gradient_descent_step(theta, learning_rate, gradient):
    return theta - learning_rate * gradient


next_theta = gradient_descent_step(5.0, 0.1, 2.0)
```

Voor een volledige Python-uitwerking, zie [[Gradient Descent Python Worked Example]].

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** `gradient descent` is een iteratieve optimalisatiemethode en geen gesloten-formule-oplossing.
- **Veelvoorkomende misvatting:** een te grote `learning rate` kiezen en daardoor divergerend gedrag niet herkennen.
- **Link met andere concepten:** [[Optimization and Training]], [[Gradient]], [[Learning Rate]], [[SGD (Stochastic Gradient Descent)]], [[Linear Regression]], [[Gradient Descent Worked Example]], [[Gradient Descent Python Worked Example]]

## Context in het domein
- Overzicht: [[00_Overzicht Machine Learning Concepten]]
- Uitwerking: [[Gradient Descent Worked Example]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

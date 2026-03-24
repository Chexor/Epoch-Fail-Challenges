---
type: concept-topic
domain: "machine-learning"
parent: "Optimization and Training"
related:
  - Optimization and Training
  - Gradient
  - Learning Rate
  - Gradient Descent Worked Example
theme: "parameter-optimization"
aliases:
  - Gradient Descent
---

# Gradient Descent
#concept #ml

## 1. Wat is het kernprobleem?
Hoe vind je goede parameters wanneer je de loss niet rechtstreeks of niet handig exact kan oplossen?

## 2. Intuitieve uitleg
Stel je een heuvelachtig landschap voor waarbij hoogte gelijk is aan fout. Gradient descent zet telkens een stap naar beneden tot je in een dal terechtkomt.

## 3. Formele structuur
- Update: `theta = theta - alpha * nabla L(theta)`
- `theta` = parameters
- `alpha` = learning rate
- `nabla L(theta)` = gradient van de loss

## 4. Toepassing
Procedure:
1. start met beginwaarden voor de parameters
2. bereken voorspellingen en loss
3. bereken de gradient
4. update de parameters
5. herhaal tot de loss weinig nog daalt

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** `gradient descent` is een iteratieve optimalisatiemethode en geen gesloten-formule-oplossing.
- **Veelvoorkomende misvatting:** een te grote `learning rate` kiezen en daardoor divergerend gedrag niet herkennen.
- **Link met andere concepten:** [[Gradient]], [[Learning Rate]], [[SGD (Stochastic Gradient Descent)]]

## Context in het domein
- Overzicht: [[00_Overzicht Machine Learning Concepten]]
- Uitwerking: [[Gradient Descent Worked Example]]

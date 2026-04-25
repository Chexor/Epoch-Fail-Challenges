---
type: atom
domain: "machine-learning"
parent: "Optimization and Training"
related:
  - Optimization and Training
  - Gradient Descent
  - Epoch
  - Gradient
  - Learning Rate
theme: "parameter-optimization"
aliases:
  - Learning Rate
---

# Learning Rate
#concept #ml

Learning Rate is de stapgrootte waarmee een optimalisatie-algoritme parameters aanpast tijdens training.

## Korte kern

- bepaalt hoe groot elke update-stap is
- te groot geeft instabiel gedrag
- te klein geeft traag leren

## 1. Wat is het kernprobleem?
Hoe groot mag een update-stap zijn zonder het minimum voorbij te springen of te traag te leren?

## 2. Intuitieve uitleg
De learning rate is de stapgrootte van je leerproces. Ze bepaalt hoe agressief of voorzichtig je model zijn parameters aanpast.

## 3. Formele structuur
- In gradient descent is `alpha` de learning rate
- Grote `alpha`: sneller, maar risico op overshoot
- Kleine `alpha`: stabieler, maar trager

## 4. Snelle vergelijking

- [[Learning Rate]] = grootte van de update-stap
- [[Gradient]] = richting en steilte van verandering
- [[Epoch]] = 1 volledige doorgang door de trainingsdata

## 5. Toepassing
Bij `alpha = 0.1` kan het model heen en weer springen rond het minimum.
Bij `alpha = 0.001` kan het model wel dalen, maar erg langzaam.

Kort Python-voorbeeld:

```python
def update_parameter(theta, learning_rate, gradient):
    return theta - learning_rate * gradient


new_theta = update_parameter(5.0, 0.01, 2.0)
```

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** de `learning rate` bepaalt hoe groot elke parameterupdate is.
- **Veelvoorkomende misvatting:** denken dat één learning rate altijd voor elk probleem geschikt is.
- **Link met andere concepten:** [[Optimization and Training]], [[Gradient Descent]], [[Gradient]], [[SGD (Stochastic Gradient Descent)]], [[Epoch]]

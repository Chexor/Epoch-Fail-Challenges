---
type: concept-topic
domain: "machine-learning"
parent: "Optimization and Training"
related:
  - Optimization and Training
  - Gradient Descent
  - Epoch
theme: "parameter-optimization"
aliases:
  - Learning Rate
---

# Learning Rate
#concept #ml

## 1. Wat is het kernprobleem?
Hoe groot mag een update-stap zijn zonder het minimum voorbij te springen of te traag te leren?

## 2. Intuitieve uitleg
De learning rate is de stapgrootte van je leerproces. Ze bepaalt hoe agressief of voorzichtig je model zijn parameters aanpast.

## 3. Formele structuur
- In gradient descent is `alpha` de learning rate
- Grote `alpha`: sneller, maar risico op overshoot
- Kleine `alpha`: stabieler, maar trager

## 4. Toepassing
Bij `alpha = 0.1` kan het model heen en weer springen rond het minimum.
Bij `alpha = 0.001` kan het model wel dalen, maar erg langzaam.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** de `learning rate` bepaalt hoe groot elke parameterupdate is.
- **Veelvoorkomende misvatting:** denken dat één learning rate altijd voor elk probleem geschikt is.
- **Link met andere concepten:** [[Gradient Descent]], [[SGD (Stochastic Gradient Descent)]]

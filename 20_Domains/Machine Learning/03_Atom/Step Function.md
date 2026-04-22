---
type: atom
domain: "machine-learning"
parent: "Activation Functions"
related:
  - Activation Functions
  - Perceptron
  - Sigmoid Function
theme: "neural-network-models"
aliases:
  - Step Function
  - Threshold Function
---

# Step Function
#concept #ml

Een step function is een activatiefunctie die de output abrupt naar `0` of `1` zet afhankelijk van of een drempel wel of niet gehaald wordt.

## Korte kern

- maakt een harde binaire beslissing
- wordt klassiek gebruikt in een [[Perceptron]]
- is niet glad en daardoor onhandig voor moderne gradient-based training

## 1. Wat is het kernprobleem?
Hoe vertaal je een numerieke score naar een eenvoudige ja/nee-beslissing?

## 2. Intuitieve uitleg
De step function werkt als een schakelaar. Onder de drempel is de output `0`, erboven `1`. Er is dus geen geleidelijke overgang.

## 3. Formele structuur
- voorbeeldvorm: `f(z) = 1` als `z >= 0`, anders `0`
- output is discreet en binair
- de functie heeft geen bruikbare gladde afgeleide rond de sprong

## 4. Snelle vergelijking
- [[Step Function]] = harde sprong naar `0` of `1`
- [[Sigmoid Function]] = zachte overgang tussen `0` en `1`
- [[ReLU]] = laat positieve waarden lineair door en kapt negatieve af

## 5. Toepassing
In een klassiek perceptron wordt de gewogen som vergeleken met een drempel. De step function beslist dan onmiddellijk of de outputklasse `0` of `1` wordt.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** de step function geeft een harde beslissing, terwijl sigmoid een continue kansachtige output geeft.
- **Veelvoorkomende misvatting:** denken dat een harde binaire functie altijd beter is voor classificatie in neurale netwerken.
- **Link met andere concepten:** [[Perceptron]], [[Activation Functions]], [[Sigmoid Function]]

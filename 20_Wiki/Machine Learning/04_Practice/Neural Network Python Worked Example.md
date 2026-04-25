---
type: practice
domain: "machine-learning"
parent: "Neural Network"
related:
  - Neural Network
  - Deep Learning
  - ReLU
  - Sequential Neural Net
theme: "python-ml-implementations"
aliases:
  - Neural Network Python Worked Example
  - Neural Network Python Example
---

# Neural Network Python Worked Example
#concept #ml

Neural Network Python Worked Example toont hoe een enkele neuron een gewogen som berekent en daarna een activatiefunctie toepast.

## Korte kern

- gebruikt gewichten en bias
- toont een eenvoudige `ReLU`-activatie
- maakt de stap van wiskunde naar code concreet

## Ondersteund concept
- [[Neural Network]]

## Doel van deze uitwerking
Deze note toont een minimale Python-schets van een neuron, zodat duidelijk wordt wat een netwerklaag operationeel doet.

## Context
Gebruik dit wanneer je de basiswerking van neurale netwerken wil begrijpen zonder meteen een volledige framework-implementatie nodig te hebben.

## Codevoorbeeld
```python
def neuron_output(x1, x2, w1, w2, bias):
    weighted_sum = x1 * w1 + x2 * w2 + bias
    return max(0, weighted_sum)


print(neuron_output(2.0, 1.0, 0.4, 0.7, -0.5))
```

## Stap-voor-stap uitleg
- elke input wordt met een gewicht vermenigvuldigd
- bias verschuift de gewogen som
- `max(0, ...)` werkt hier als eenvoudige `ReLU`

## Verwachte output of gedrag
- de output is een geactiveerde neuronwaarde
- als de gewogen som negatief is, wordt de output hier `0`

## Uitwerking
1. Neem inputwaarden.
2. Bereken de gewogen som.
3. Voeg bias toe.
4. Pas de activatiefunctie toe.

## Wat toont dit voorbeeld?
- hoe een neuron informatie combineert
- waarom activatiefuncties nodig zijn om niet-lineariteit toe te voegen

## Typische fouten
- denken dat een neuron gewoon een lineaire formule blijft zonder activatie
- vergeten dat echte netwerken uit veel neuronen en lagen bestaan

## Verwante concepten
- [[Neural Network]]
- [[Deep Learning]]
- [[ReLU]]
- [[Sequential Neural Net]]

## Begripsafbakening en verbanden
- **Kernonderscheid:** deze note toont één eenvoudige neuronstap, niet de volledige training van een diep netwerk.
- **Veelvoorkomende misvatting:** denken dat dit al een volledig neural network is; in realiteit heb je meerdere neuronen, lagen en trainingsstappen nodig.
- **Link met andere concepten:** [[Neural Network]], [[Deep Learning]], [[ReLU]], [[Sequential Neural Net]], [[Transformer]]

---
type: theory
domain: "machine-learning"
parent: "Neural Network Models"
related:
  - Neural Network Models
  - Deep Learning
  - Sequential Neural Net
  - Keras
  - Perceptron
  - Activation Functions
  - Sigmoid Function
  - ReLU
  - Neural Network Python Worked Example
theme: "neural-network-models"
aliases:
  - Neural Network
  - Artificial Neural Networks
---

# Neural Network
#concept #ml

Een neural network is een model met opeenvolgende lagen van gewogen verbindingen en activatiefuncties dat complexe, niet-lineaire patronen uit data leert.

## Korte kern

- bestaat uit input-, hidden- en outputlagen
- leert via aanpassing van gewichten
- vormt de basis van veel deep-learningmodellen

## 1. Wat is het kernprobleem?
Hoe kan een model complexe, niet-lineaire verbanden leren uit data?

## 2. Intuitieve uitleg
Een `neural network` bestaat uit veel eenvoudige rekeneenheden die samen een complexe functie leren. Elke laag transformeert de input een beetje verder, zodat het model steeds rijkere patronen kan herkennen.

## 3. Formele structuur
- typisch opgebouwd uit:
  - `input layer`
  - een of meer `hidden layers`
  - `output layer`
- verbindingen hebben gewichten
- neuronen passen een activatiefunctie toe zoals [[Sigmoid Function]] of [[ReLU]]
- tijdens training worden gewichten aangepast om de fout te verkleinen

## 4. Snelle vergelijking

- [[Neural Network]] = algemeen model met gewichten en activaties
- [[Perceptron]] = eenvoudigste neuronachtige classifier
- [[Linear Regression]] = veel eenvoudiger lineair model zonder hidden layers
- [[Deep Learning]] = gebruik van grotere of diepere neurale netwerken

## 5. Toepassing
Een neuraal netwerk kan gebruikt worden om cijfers te classificeren, prijzen te voorspellen of patronen in tabulaire data te leren.

Kort Python-voorbeeld:

```python
def neuron_output(x1, x2, w1, w2, bias):
    weighted_sum = x1 * w1 + x2 * w2 + bias
    return max(0, weighted_sum)


output = neuron_output(2.0, 1.0, 0.4, 0.7, -0.5)
```

Voor een volledige Python-uitwerking, zie [[Neural Network Python Worked Example]].

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** een `neural network` is een rekenmodel geïnspireerd door biologische neuronen, geen letterlijke kopie ervan.
- **Veelvoorkomende misvatting:** denken dat een neuron biologisch realistisch gemodelleerd wordt.
- **Link met andere concepten:** [[Machine Learning]], [[Deep Learning]], [[Perceptron]], [[Activation Functions]], [[Sequential Neural Net]], [[Convolutional Neural Network (CNN)]], [[Sigmoid Function]], [[ReLU]], [[Keras]], [[Neural Network Python Worked Example]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

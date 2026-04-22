---
type: atom
domain: "machine-learning"
parent: "Neural Network Models"
related:
  - Neural Network
  - Deep Learning
  - Sequential Neural Net
  - Keras
  - Neural Network Models
  - ReLU Python Worked Example
theme: "neural-network-models"
aliases:
  - Rectified Linear Unit
---

# ReLU
#concept #ml

ReLU is een activatiefunctie in neurale netwerken die negatieve input omzet naar `0` en positieve input ongewijzigd doorlaat.

## Korte kern

- `ReLU(x) = max(0, x)`
- introduceert niet-lineariteit in een neuraal netwerk
- is eenvoudig, snel en veelgebruikt in deep learning

## 1. Wat is het kernprobleem?

Hoe geef je een neuraal netwerk een eenvoudige niet-lineaire activatiefunctie zodat het meer kan leren dan alleen lineaire verbanden?

## 2. Intuitieve uitleg

Een neuron met `ReLU` werkt als een soort poort:

- negatieve signalen worden tegengehouden
- positieve signalen mogen door

Daardoor kan een netwerk selectief reageren op bepaalde patronen, zonder de activatiefunctie nodeloos complex te maken.

## 3. Formele structuur

- definitie: `ReLU(x) = max(0, x)`
- voor `x < 0` is de output `0`
- voor `x >= 0` is de output `x`
- `ReLU` wordt typisch gebruikt in hidden layers van [[Neural Network|neurale netwerken]]

## 4. Snelle vergelijking

- `ReLU` = negatieve waarden afkappen, positieve doorlaten
- `sigmoid` = output tussen `0` en `1`
- `tanh` = output tussen `-1` en `1`

## 5. Toepassing

In een deep learning-model krijgt elk neuron eerst een gewogen som als input. Daarna past het netwerk `ReLU` toe, zodat alleen voldoende sterke positieve activaties verder doorstromen.

Kort Python-voorbeeld:

```python
def relu(x):
    return max(0, x)


activated = relu(-3.5)
```

Voor een volledige Python-uitwerking, zie [[ReLU Python Worked Example]].

## 6. Begripsafbakening en verbanden

- **Kernonderscheid:** `ReLU` is een activatiefunctie, geen volledig model of leeralgoritme.
- **Veelvoorkomende misvatting:** denken dat een neuraal netwerk automatisch slim is zonder niet-lineariteit zoals `ReLU`.
- **Link met andere concepten:** [[Neural Network]], [[Deep Learning]], [[Sequential Neural Net]], [[Keras]], [[Neural Network Models]], [[Neural Network Python Worked Example]], [[ReLU Python Worked Example]]

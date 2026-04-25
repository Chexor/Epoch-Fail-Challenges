---
type: practice
domain: "machine-learning"
parent: "ReLU"
related:
  - ReLU
  - Neural Network
  - Deep Learning
  - Neural Network Python Worked Example
theme: "python-ml-implementations"
aliases:
  - ReLU Python Worked Example
  - ReLU Python Example
---

# ReLU Python Worked Example
#concept #ml

ReLU Python Worked Example toont hoe de activatiefunctie `max(0, x)` in code negatieve waarden afkapt en positieve doorlaat.

## Korte kern

- implementatie is zeer eenvoudig
- maakt niet-lineariteit zichtbaar in 1 regel code
- toont waarom negatieve activaties naar `0` gaan

## Ondersteund concept
- [[ReLU]]

## Doel van deze uitwerking
Deze note toont de meest directe Python-vorm van `ReLU`, zodat de activatiefunctie niet abstract blijft.

## Context
Gebruik dit wanneer je activatiefuncties leert en snel wil zien wat `ReLU` operationeel doet.

## Codevoorbeeld
```python
def relu(x):
    return max(0, x)


print(relu(-3.5))
print(relu(2.1))
```

## Stap-voor-stap uitleg
- voor negatieve input geeft `ReLU` `0`
- voor positieve input geeft `ReLU` dezelfde waarde terug
- zo ontstaat een eenvoudige niet-lineaire poort

## Verwachte output of gedrag
- de outputs zijn hier `0` en `2.1`
- de functie is dus lineair voor positieve input, maar kapt negatieve waarden af

## Uitwerking
1. Neem een inputwaarde.
2. Vergelijk die met `0`.
3. Geef de grootste van beide terug.
4. Gebruik dit resultaat als activatie van het neuron.

## Wat toont dit voorbeeld?
- waarom `ReLU` praktisch zo populair is
- hoe weinig code nodig is om een belangrijke activatiefunctie te beschrijven

## Typische fouten
- denken dat `ReLU` negatieve waarden omdraait in plaats van afkapt
- vergeten dat activatiefuncties nodig zijn voor niet-lineariteit

## Verwante concepten
- [[ReLU]]
- [[Neural Network]]
- [[Deep Learning]]
- [[Neural Network Python Worked Example]]

## Begripsafbakening en verbanden
- **Kernonderscheid:** deze note toont alleen de activatiefunctie zelf, niet een volledig netwerk.
- **Veelvoorkomende misvatting:** denken dat `ReLU` op zich al een leeralgoritme is; het is enkel een activatiefunctie.
- **Link met andere concepten:** [[ReLU]], [[Neural Network]], [[Deep Learning]], [[Neural Network Python Worked Example]], [[Transformer]]

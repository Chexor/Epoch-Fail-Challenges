---
type: practice
domain: "machine-learning"
parent: "Linear Regression"
related:
  - Linear Regression
  - OLS (Ordinary Least Squares)
  - Gradient Descent
  - Classification vs Regression
theme: "python-ml-implementations"
aliases:
  - Linear Regression Python Worked Example
  - Linear Regression Python Example
---

# Linear Regression Python Worked Example
#concept #ml

Linear Regression Python Worked Example toont hoe je met een kleine formule en een paar parameters een numerieke voorspelling maakt.

## Korte kern

- gebruikt `y_hat = a*x + b`
- laat de rol van `slope` en `intercept` zien
- houdt de code bewust klein en leesbaar

## Ondersteund concept
- [[Linear Regression]]

## Doel van deze uitwerking
Deze note toont de eenvoudigste Python-vorm van `linear regression`, zodat de stap van formule naar code direct zichtbaar wordt.

## Context
Gebruik dit wanneer je wil zien hoe een lineair model concreet een numerieke waarde voorspelt.

## Codevoorbeeld
```python
def predict_price(rooms, slope, intercept):
    return slope * rooms + intercept


slope = 50000
intercept = 120000

print(predict_price(4, slope, intercept))
```

## Stap-voor-stap uitleg
- `slope` bepaalt hoeveel de voorspelling verandert per extra feature-eenheid
- `intercept` is de basiswaarde wanneer de input `0` is
- de functie berekent rechtstreeks de lineaire formule

## Verwachte output of gedrag
- de output is een numerieke voorspelling zoals `320000`
- elke extra kamer verhoogt de voorspelde prijs met `50000`

## Uitwerking
1. Kies waarden voor `slope` en `intercept`.
2. Vul de inputfeature in.
3. Bereken de lineaire voorspelling.
4. Interpreteer de output in de context van het probleem.

## Wat toont dit voorbeeld?
- hoe lineaire regressie in code vaak neerkomt op een eenvoudige formule
- waarom interpretatie van parameters hier relatief transparant is

## Typische fouten
- classificatie en regressie door elkaar halen
- de output interpreteren als zeker of causaal in plaats van als voorspelling

## Verwante concepten
- [[Linear Regression]]
- [[OLS (Ordinary Least Squares)]]
- [[Gradient Descent]]
- [[Classification vs Regression]]

## Begripsafbakening en verbanden
- **Kernonderscheid:** deze note toont de inferentie van een lineair model, niet hoe de parameters getraind worden.
- **Veelvoorkomende misvatting:** denken dat dit al het volledige leerproces van linear regression is; hier zie je alleen de voorspelfase.
- **Link met andere concepten:** [[Linear Regression]], [[OLS (Ordinary Least Squares)]], [[Gradient Descent]], [[Classification vs Regression]], [[Slope en Intercept]]

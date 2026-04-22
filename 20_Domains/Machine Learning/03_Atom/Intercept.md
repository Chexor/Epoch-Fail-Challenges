---
type: atom
domain: "machine-learning"
parent: "Linear Model Terms"
related:
  - Linear Model Terms
  - Slope
  - Linear Regression
theme: "linear-modeling"
aliases:
  - Intercept
  - Bias
  - y-intercept
---

# Intercept
#concept #ml

Intercept is de modelwaarde van `y` wanneer `x = 0` en bepaalt dus waar een lineaire functie de y-as snijdt.

## Korte kern

- is het startniveau van de rechte
- is in `y = a*x + b` de parameter `b`
- is niet altijd inhoudelijk realistisch

## 1. Wat is het kernprobleem?
Hoe beschrijf je het basisniveau van een lineair model nog voor de invloed van `x` meetelt?

## 2. Intuitieve uitleg
De intercept is de waarde waarmee je start op de y-as. Van daaruit zorgt de [[Slope]] ervoor dat de lijn stijgt of daalt.

## 3. Formele structuur
- in `y = a*x + b` is `b` de intercept
- `b` is de waarde van `y` wanneer `x = 0`
- de intercept verschuift de volledige lijn omhoog of omlaag

## 4. Snelle vergelijking
- [[Intercept]] = startwaarde van de lijn
- [[Slope]] = verandering per stap in `x`
- [[Linear Regression]] = model waarin beide samen de rechte bepalen

## 5. Toepassing
Bij `prijs = 100 + 50*x` is de intercept `100`. Dat is de voorspelde prijs wanneer `x = 0`.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** intercept gaat over het niveau bij `x = 0`, niet over hoe snel de lijn verandert.
- **Veelvoorkomende misvatting:** de intercept altijd letterlijk interpreteren, ook wanneer `x = 0` buiten het relevante domein ligt.
- **Link met andere concepten:** [[Slope]], [[Linear Regression]], [[Linear Model Terms]]

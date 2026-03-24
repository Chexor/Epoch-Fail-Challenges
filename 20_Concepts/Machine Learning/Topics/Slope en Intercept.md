---
type: concept-topic
domain: "machine-learning"
parent: "Linear Modeling"
related:
  - Linear Modeling
  - Linear Regression
  - Dot Product
theme: "linear-modeling"
aliases:
  - Slope en Intercept
---

# Slope en Intercept
#concept #ml

## 1. Wat is het kernprobleem?
Je moet de parameters van een rechte correct kunnen interpreteren in woorden.

## 2. Intuitieve uitleg
De slope vertelt hoe sterk `y` verandert als `x` 1 eenheid stijgt. De intercept is de startwaarde van de lijn op de y-as.

## 3. Formele structuur
- In `y = a*x + b` is `a` de slope
- In `y = a*x + b` is `b` de intercept
- `a = delta y / delta x`
- `b` is de waarde van `y` wanneer `x = 0`

## 4. Toepassing
Bij `y = 100 + 50x`:
- slope `a = 50`
- intercept `b = 100`
- als `x` van 3 naar 4 stijgt, stijgt `y` met 50

De intercept is niet altijd realistisch in de echte wereld, maar hoort wel bij het model.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** de `slope` beschrijft verandering per extra eenheid `x`, de `intercept` het modelniveau bij `x = 0`.
- **Veelvoorkomende misvatting:** de intercept altijd letterlijk interpreteren, ook buiten het relevante datadomein.
- **Link met andere concepten:** [[Linear Regression]], [[Derivative (Afgeleide)]]

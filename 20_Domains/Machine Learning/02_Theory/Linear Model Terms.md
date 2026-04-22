---
type: theory
domain: "machine-learning"
parent: "Linear Modeling"
related:
  - Linear Modeling
  - Linear Regression
  - Slope
  - Intercept
  - Scaling
theme: "linear-modeling"
aliases:
  - Linear Model Terms
  - Slope en Intercept
  - Slope, Intercept en Scaling
---

# Linear Model Terms
#concept #ml

Linear Model Terms groepeert basisbegrippen zoals [[Slope]], [[Intercept]] en [[Scaling]] die vaak samen opduiken bij lineaire modellen en hun interpretatie.

## Korte kern

- slope en intercept beschrijven een rechte
- scaling maakt features numeriek beter hanteerbaar
- samen helpen ze lineaire modellen correct lezen en trainen

## 1. Wat is het kernprobleem?
Welke basisbegrippen moet je beheersen om lineaire modellen correct te interpreteren en praktisch bruikbaar te maken?

## 2. Intuitieve uitleg
Bij een lineair model wil je zowel begrijpen wat de lijn betekent als hoe je inputwaarden worden voorbereid. `Slope` en `intercept` leggen de betekenis van de lijn uit. `Scaling` helpt ervoor zorgen dat training en interpretatie niet scheefgetrokken worden door heel verschillende groottes van features.

## 3. Formele structuur
- [[Slope]] = verandering in `y` per extra eenheid `x`
- [[Intercept]] = modelwaarde van `y` wanneer `x = 0`
- [[Scaling]] = features herschalen naar een bruikbare of vergelijkbare schaal
- in `y = a*x + b` zijn `a` en `b` de kernparameters van de rechte

## 4. Snelle vergelijking

- Plaats dit concept kort tegenover 1-2 verwante concepten uit deze map.

## 5. Toepassing
Bij `y = 100 + 50x`:
- [[Slope]] = `50`
- [[Intercept]] = `100`
- als `x` van 3 naar 4 stijgt, stijgt `y` met 50

Als een feature waarden rond `1` heeft en een andere rond `100000`, dan kan [[Scaling]] nodig zijn om training met gradient descent stabieler te maken.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** `slope` en `intercept` beschrijven de vorm van het model; [[Scaling]] beschrijft hoe inputvariabelen voorbereid worden.
- **Veelvoorkomende misvatting:** denken dat scaling de relatie in de data verandert in plaats van alleen de schaalvoorstelling.
- **Link met andere concepten:** [[Linear Regression]], [[Gradient Descent]], [[Feature Scaling en Normalization]], [[Derivative (Afgeleide)]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

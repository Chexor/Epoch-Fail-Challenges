---
type: atom
domain: "machine-learning"
parent: "Linear Model Terms"
related:
  - Linear Model Terms
  - Intercept
  - Linear Regression
theme: "linear-modeling"
aliases:
  - Slope
  - Helling
---

# Slope
#concept #ml

Slope is de parameter die aangeeft hoeveel de voorspelde output verandert wanneer de input `x` met 1 eenheid stijgt.

## Korte kern

- bepaalt de steilheid van een rechte
- geeft richting en grootte van verandering
- is in `y = a*x + b` de parameter `a`

## 1. Wat is het kernprobleem?
Hoe beschrijf je exact hoe sterk `y` verandert als `x` verandert?

## 2. Intuitieve uitleg
De slope zegt hoeveel de lijn omhoog of omlaag gaat per stap van 1 op de x-as. Een positieve slope betekent stijgen, een negatieve slope betekent dalen.

## 3. Formele structuur
- in `y = a*x + b` is `a` de slope
- `a = delta y / delta x`
- `a > 0` betekent stijgende relatie
- `a < 0` betekent dalende relatie
- `a = 0` betekent horizontale lijn

## 4. Snelle vergelijking
- [[Slope]] = verandering per extra eenheid `x`
- [[Intercept]] = startwaarde van de lijn bij `x = 0`
- [[Derivative (Afgeleide)]] = algemener idee van lokale verandering

## 5. Toepassing
Bij `prijs = 100 + 50*x` is de slope `50`. Voor elke extra kamer stijgt de voorspelde prijs dus met 50.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** slope gaat over verandering, niet over het startpunt van de lijn.
- **Veelvoorkomende misvatting:** slope verwarren met de totale waarde van `y` in plaats van de verandering in `y`.
- **Link met andere concepten:** [[Intercept]], [[Linear Regression]], [[Linear Model Terms]], [[Derivative (Afgeleide)]]

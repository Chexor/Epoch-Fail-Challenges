---
type: practice
domain: "statistics"
parent: "Z-score"
related:
  - Normale verdeling
  - Variantie en Standaardafwijking
  - Gemiddelde
theme: "standardization"
aliases:
  - Z-score Worked Example
  - Z-score
---

# Z-score Worked Example
#concept #statistiek

## Ondersteund concept
- [[Z-score]]

## Doel van deze uitwerking
Deze note toont stap voor stap hoe je een ruwe waarde omzet naar een z-score en interpreteert binnen een normale verdeling.

## Context
Gebruik dit wanneer je wil begrijpen hoe standaardisatie werkt of wanneer je kansen uit een normale verdeling moet berekenen.

## Uitwerking
1. Stel dat `X ~ N(130, sigma)` en dat `P(X < 125) = 0.04`.
2. Schrijf de standaardisatie uit: `Z = (X - mu) / sigma`.
3. Zet de kans om: `P(Z < (125 - 130) / sigma) = 0.04`.
4. Zoek in de Z-tabel: `z_0.04 ≈ -1.75`.
5. Los op: `-5 / sigma = -1.75`, dus `sigma = 5 / 1.75 ≈ 2.857`.

## Wat toont dit voorbeeld?
- een z-score is de brug tussen een ruwe waarde en de standaardnormale verdeling
- standaardisatie maakt kansvragen hanteerbaar via de Z-tabel

## Typische fouten
- het teken van de teller verkeerd nemen
- `mu` en `sigma` omwisselen
- vergeten dat je eerst moet standaardiseren voor je de Z-tabel gebruikt

## Verwante concepten
- [[Normale verdeling]]
- [[Z-score]]
- [[Variantie en Standaardafwijking]]

## Wat studeer je hierna?
- [[Z-score]]
- [[Normale verdeling]]
- [[00_Overzicht Statistics]]

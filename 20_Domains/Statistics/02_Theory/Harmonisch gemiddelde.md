---
type: theory
domain: "statistics"
parent: "Descriptive Statistics"
related:
  - Descriptive Statistics
  - Gemiddelde
  - Mediaan
  - Gemiddelde vs Mediaan vs Modus
  - Variantie en Standaardafwijking
theme: "descriptive-statistics"
aliases:
  - Harmonisch gemiddelde
  - Harmonic mean
  - Harmonic average
---

# Harmonisch gemiddelde
#concept #statistiek

Het harmonisch gemiddelde (Harmonic mean) is geschikt om een gemiddelde te nemen van snelheden, ratio's en rates met een vaste teller.

## Korte kern

- Het gebruikt reciproken: eerst `1/x`, dan terug omkeren.
- Lage waarden wegen zwaarder door dan hoge waarden.
- Het is vaak beter dan het rekenkundig gemiddelde bij rates.

## Probleem

Hoe bereken je een eerlijke centrummaat voor grootheden zoals km/u, prijs per eenheid of andere rates, waar een gewoon gemiddelde kan misleiden?

## Intuïtie

Bij rates bepaalt de traagste of kleinste waarde vaak de totale prestatie sterker. Het harmonisch gemiddelde corrigeert daarvoor door met reciproken te werken, waardoor kleine noemers meer impact krijgen.

## Toepassing

Je rijdt twee gelijke afstanden: de ene helft aan `30 km/u`, de andere helft aan `60 km/u`.

- Rekenkundig gemiddelde: `(30 + 60) / 2 = 45 km/u` (misleidend)
- Harmonisch gemiddelde: `2 / (1/30 + 1/60) = 40 km/u`

`40 km/u` is de correcte gemiddelde snelheid voor gelijke afstanden.

## Formeel

Voor positieve waarden `x_1, ..., x_n`:

- `H = \frac{n}{\sum_{i=1}^{n} (1/x_i)}`
- Voor gewogen vorm: `H_w = \frac{\sum w_i}{\sum (w_i / x_i)}`
- Vereist `x_i > 0` in de standaardvorm.

## Verbanden

- [[Descriptive Statistics]]
- [[Gemiddelde]]
- [[Mediaan]]
- [[Gemiddelde vs Mediaan vs Modus]]
- [[Variantie en Standaardafwijking]]

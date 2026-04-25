---
type: theory
domain: "machine-learning"
parent: "Support Vector Machine"
related:
  - Support Vector Machine
  - Soft Margin Classification
  - Support Vectors
theme: "linear-modeling"
aliases:
  - Hard Margin Classification
---

# Hard Margin Classification
#concept #ml

Hard Margin Classification is een SVM-instelling waarbij alle punten perfect buiten de marge moeten liggen zonder fouten of overtredingen.

## Korte kern

- vereist lineair scheidbare data
- laat geen marge-overtredingen toe
- is gevoelig voor outliers

## 1. Wat is het kernprobleem?
Hoe scheid je twee klassen perfect wanneer de data volledig lineair scheidbaar is?

## 2. Intuitieve uitleg
Bij hard margin is de regel streng: elk punt moet correct gescheiden zijn en buiten de "straat" blijven. Dat werkt alleen als de data heel proper scheidbaar is.

## 3. Formele structuur
- alle punten moeten aan de juiste kant van de marge liggen
- geen slack variables of toegelaten overtredingen
- niet bruikbaar als er overlapping of ruis is

## 4. Snelle vergelijking
- [[Hard Margin Classification]] = perfecte scheiding zonder fouten
- [[Soft Margin Classification]] = laat beperkte fouten of marge-overtredingen toe
- [[Support Vector Machine]] = bredere modelklasse

## 5. Toepassing
In theorie is hard margin mooi voor zuiver lineair scheidbare data, maar in echte datasets is het vaak te streng door ruis en outliers.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** hard margin is een strikt speciaal geval van SVM-classificatie.
- **Veelvoorkomende misvatting:** denken dat perfecte trainingseparatie automatisch de beste generalisatie geeft.
- **Link met andere concepten:** [[Support Vector Machine]], [[Soft Margin Classification]], [[Support Vectors]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

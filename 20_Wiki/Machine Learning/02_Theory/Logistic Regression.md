---
type: theory
domain: "machine-learning"
parent: "Linear Modeling"
related:
  - Linear Modeling
  - Classification vs Regression
  - Linear Regression
theme: "linear-modeling"
aliases:
  - Logistic Regression
---

# Logistic Regression
#concept #ml

Logistic Regression is een model voor classificatie dat kansen op een klasse voorspelt via een lineaire combinatie van features gevolgd door een sigmoidfunctie.

## Korte kern

- wordt gebruikt voor classificatie, niet voor regressie
- geeft een kans tussen 0 en 1
- gebruikt een lineaire score in de achtergrond

## 1. Wat is het kernprobleem?
Hoe voorspel je of een voorbeeld tot een bepaalde klasse behoort op basis van invoerfeatures?

## 2. Intuitieve uitleg
Het model berekent eerst een lineaire score zoals bij [[Linear Regression]]. Daarna wordt die score omgezet naar een kans. Op basis van een drempel, bijvoorbeeld `0.5`, beslis je dan tussen klasse `0` en klasse `1`.

## 3. Formele structuur
- lineaire score: `z = a0 + a1*x1 + ... + an*xn`
- sigmoidfunctie: `p = 1 / (1 + e^-z)`
- `p` is de voorspelde kans op de positieve klasse
- classificatie gebeurt vaak met een drempel op `p`

## 4. Snelle vergelijking
- [[Logistic Regression]] = classificatie via kansen en een sigmoid
- [[Linear Regression]] = regressie voor continue waarden
- [[Classification vs Regression]] = helpt kiezen tussen beide probleemtypes

## 5. Toepassing
Voor spamdetectie kan `p = 0.87` betekenen: 87 procent kans dat een e-mail spam is. Met een drempel van `0.5` label je die dan als spam.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** ondanks de naam is logistic regression een classificatiemodel.
- **Veelvoorkomende misvatting:** denken dat de output zelf een label is in plaats van een kans.
- **Link met andere concepten:** [[Classification vs Regression]], [[Supervised Learning]], [[Linear Regression]], [[Linear Modeling]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

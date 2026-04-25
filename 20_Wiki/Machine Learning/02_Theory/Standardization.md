---
type: theory
domain: "machine-learning"
parent: "Feature Scaling en Normalization"
related:
  - Feature Scaling en Normalization
  - Scaling
  - Normalization
theme: "data-preparation"
aliases:
  - Standardization
  - Z-score scaling
---

# Standardization
#concept #ml

Standardization is een techniek waarbij een feature wordt hercentreerd rond het gemiddelde en geschaald met de standaardafwijking.

## Korte kern

- maakt gemiddelde gelijk aan `0`
- gebruikt standaardafwijking als schaal
- is vaak nuttig voor gradient descent en lineaire modellen

## 1. Wat is het kernprobleem?
Hoe maak je features vergelijkbaar zonder ze per se naar een vast bereik zoals `0` tot `1` te brengen?

## 2. Intuitieve uitleg
Standardization herschrijft een feature zodat je werkt in termen van afstand tot het gemiddelde. Daardoor tellen verschillen in een meer gebalanceerde schaal mee.

## 3. Formele structuur
- typische formule: `(x - mean(x)) / std(x)`
- na standardization heeft de getransformeerde feature gemiddelde `0`
- de standaardafwijking wordt typisch `1`

## 4. Snelle vergelijking
- [[Standardization]] = centreren en schalen met standaardafwijking
- [[Normalization]] = naar een vast bereik herschalen
- [[Scaling]] = bredere verzamelterm voor beide benaderingen

## 5. Toepassing
Als `jaarinkomen` en `leeftijd` samen in een model zitten, kan standardization helpen om beide features op een numeriek beter vergelijkbare schaal te zetten zonder vast te zitten aan `[0,1]`.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** standardization gebruikt gemiddelde en standaardafwijking, normalization meestal minimum en maximum.
- **Veelvoorkomende misvatting:** denken dat standaardiseren alleen voor statistiek is en niet voor machine learning.
- **Link met andere concepten:** [[Scaling]], [[Normalization]], [[Feature Scaling en Normalization]], [[Gradient Descent]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

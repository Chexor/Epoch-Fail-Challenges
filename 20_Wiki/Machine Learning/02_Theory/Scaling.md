---
type: theory
domain: "machine-learning"
parent: "Linear Model Terms"
related:
  - Linear Model Terms
  - Feature Scaling en Normalization
  - Normalization
  - Standardization
  - Gradient Descent
theme: "data-preparation"
aliases:
  - Scaling
  - Feature Scaling
---

# Scaling
#concept #ml

Scaling is het herschalen van features zodat hun waarden binnen een vergelijkbare grootteorde liggen en modellen numeriek stabieler kunnen leren.

## Korte kern

- verandert de schaal, niet de onderliggende betekenis
- helpt bij training en afstandsvergelijkingen
- is vooral nuttig bij sterk verschillende groottes van features

## 1. Wat is het kernprobleem?
Hoe voorkom je dat grote numerieke schalen sommige features te dominant maken tijdens training?

## 2. Intuitieve uitleg
Als 1 feature waarden tussen `0` en `1` heeft en een andere tussen `0` en `100000`, dan werkt een model vaak moeilijker met die ruwe combinatie. Scaling zet ze op een beter vergelijkbare schaal.

## 3. Formele structuur
- [[Scaling]] is de brede verzamelterm voor features herschalen
- [[Normalization]] brengt waarden vaak naar een vast bereik zoals `[0,1]`
- [[Standardization]] centreert rond het gemiddelde en schaalt met de standaardafwijking
- scaling wordt vaak toegepast op inputfeatures, niet rechtstreeks op de interpretatie van het probleem
- scaling is belangrijk voor methodes zoals [[Gradient Descent]] en afstandsgebaseerde modellen

## 4. Snelle vergelijking
- [[Scaling]] = features herschalen naar vergelijkbare grootten
- [[Feature Scaling en Normalization]] = bredere note over scaling en standaardisatie
- [[Normalization]] = vaak herschalen naar een vast bereik
- [[Standardization]] = herschalen via gemiddelde en standaardafwijking
- [[Gradient Descent]] = optimalisatiemethode die vaak baat heeft bij scaling

## 5. Toepassing
Bij een dataset met `leeftijd` en `jaarinkomen` kan `jaarinkomen` numeriek veel groter zijn. Na scaling leert een model met gradient descent vaak stabieler en sneller.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** scaling past de numerieke schaal aan, maar verandert niet welk patroon je probeert te leren.
- **Veelvoorkomende misvatting:** denken dat scaling overbodig is omdat het model "dat zelf wel oplost".
- **Link met andere concepten:** [[Feature Scaling en Normalization]], [[Normalization]], [[Standardization]], [[Gradient Descent]], [[Linear Model Terms]], [[Linear Regression]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

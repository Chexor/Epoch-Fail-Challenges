---
type: theory
domain: "machine-learning"
parent: "Data Preparation"
related:
  - Data Preparation
  - Scaling
  - Normalization
  - Standardization
  - K-Nearest Neighbors (KNN)
  - Gradient Descent
theme: "data-preparation"
aliases:
  - Feature Scaling en Normalization
---

# Feature Scaling en Normalization
#concept #ml

Feature Scaling en Normalization groepeert technieken die features herschalen of hercentreren zodat modellen stabieler leren en variabelen beter vergelijkbaar worden.

## Korte kern

- verzamelt kerntechnieken om features op schaal te brengen
- helpt vooral bij gradient descent en afstandsgebaseerde modellen
- omvat onder meer [[Scaling]], [[Normalization]] en [[Standardization]]

## 1. Wat is het kernprobleem?
Features met heel verschillende groottes kunnen training met gradient descent traag of instabiel maken.

## 2. Intuitieve uitleg
Als 1 feature waarden rond 2 heeft en een ander rond 200000, dan trekt dat grote getal sneller aan het model. Door te schalen zet je features op een vergelijkbare schaal.

## 3. Formele structuur
- [[Scaling]] = brede verzamelnaam voor features herschalen
- [[Normalization]] = waarden vaak naar een vast bereik brengen, bijvoorbeeld `0` tot `1`
- [[Standardization]] = centreren rond het gemiddelde en schalen met de standaardafwijking
- terminologie verschilt soms per cursus of library, dus context blijft belangrijk

## 4. Snelle vergelijking

- Plaats dit concept kort tegenover 1-2 verwante concepten uit deze map.

## 5. Toepassing
Bij huizenprijzen kunnen `aantal kamers` en `oppervlakte in m2` nog redelijk samen liggen, maar `jaarinkomen` en `oppervlakte` vaak niet. Na preprocessing met [[Scaling]], [[Normalization]] of [[Standardization]] convergeren GD en SGD vaak sneller.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** schaling verandert de schaal van features en maakt training of afstandsvergelijkingen vaak stabieler.
- **Veelvoorkomende misvatting:** een schaaltransformatie apart op train en test fitten in plaats van enkel op train.
- **Link met andere concepten:** [[Scaling]], [[Normalization]], [[Standardization]], [[Gradient Descent]], [[SGD (Stochastic Gradient Descent)]], [[K-Nearest Neighbors (KNN)]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

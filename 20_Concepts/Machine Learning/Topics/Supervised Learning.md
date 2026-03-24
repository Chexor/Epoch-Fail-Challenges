---
type: concept-topic
domain: "machine-learning"
parent: "Learning Paradigms"
related:
  - Learning Paradigms
  - Unsupervised Learning
  - Reinforcement Learning
  - Supervised vs Unsupervised vs Reinforcement Learning
theme: "learning-paradigms"
aliases:
  - Supervised Learning
---

# Supervised Learning
#concept #ml

## 1. Wat is het kernprobleem?
Hoe leer je een model een juiste output voorspellen wanneer je trainingsvoorbeelden hebt met een correct antwoord erbij?

## 2. Intuitieve uitleg
Bij `Supervised Learning` leert een model uit voorbeelden waarbij zowel de input als het juiste antwoord gekend zijn. Je toont het model dus telkens: "dit is de situatie" en "dit is het juiste resultaat".

Denk aan huizenprijzen voorspellen. Je geeft woningkenmerken zoals oppervlakte en aantal kamers, samen met de echte prijs. Het model leert dan welke patronen meestal tot welke prijs leiden.

## 3. Formele structuur
- trainingsdata bestaat uit input-outputparen `(x, y)`
- `x` bevat de [[Data, Example, Feature, Target|features]]
- `y` is de `target` of het juiste antwoord
- typische taken zijn [[Classification vs Regression|classificatie]] en [[Classification vs Regression|regressie]]
- het model probeert een functie te leren die van `x` naar `y` gaat

Voorbeelden van algoritmes:

- [[Linear Regression]]
- [[K-Nearest Neighbors (KNN)]]
- [[Neural Network]]

## 4. Toepassing
- een e-mail classificeren als spam of geen spam
- de prijs van een huis voorspellen
- een handgeschreven cijfer herkennen

Het centrale idee is altijd hetzelfde: het model krijgt feedback via het juiste antwoord.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** bij `Supervised Learning` zijn labels of targets aanwezig tijdens training.
- **Veelvoorkomende misvatting:** denken dat elk ML-probleem een correct antwoord bevat. Dat is niet zo bij [[Unsupervised Learning]].
- **Link met andere concepten:** [[Machine Learning]], [[Unsupervised Learning]], [[Reinforcement Learning]], [[Classification vs Regression]], [[Data, Example, Feature, Target]], [[Linear Regression]], [[K-Nearest Neighbors (KNN)]], [[Neural Network]], [[Supervised vs Unsupervised vs Reinforcement Learning]]

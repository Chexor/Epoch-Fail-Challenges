---
type: concept-topic
domain: "machine-learning"
parent: "Learning Paradigms"
related:
  - Learning Paradigms
  - Supervised Learning
  - K-Means
  - Supervised vs Unsupervised vs Reinforcement Learning
theme: "learning-paradigms"
aliases:
  - Unsupervised Learning
---

# Unsupervised Learning
#concept #ml

## 1. Wat is het kernprobleem?
Hoe laat je een model structuur of patronen ontdekken wanneer er geen juiste antwoorden of labels aanwezig zijn?

## 2. Intuitieve uitleg
Bij `Unsupervised Learning` krijgt het model alleen de inputdata. Er staat niet bij wat correct of fout is. Het model moet dus zelf proberen structuur te vinden, bijvoorbeeld groepen, gelijkenissen of verborgen patronen.

Denk aan klantendata zonder labels. Het model kan dan zelf proberen klanten te groeperen in segmenten met gelijkaardig gedrag.

## 3. Formele structuur
- trainingsdata bestaat uit `x` zonder `y`
- er zijn geen labels of targets beschikbaar
- typische taken zijn `clustering` en `dimensionality reduction`
- het model zoekt patronen, groepen of latent structuur in de data

Voorbeelden van algoritmes:

- [[K-Means]]

## 4. Toepassing
- klanten segmenteren op basis van koopgedrag
- gelijkaardige documenten of beelden groeperen
- structuur ontdekken in grote datasets zonder vooraf gedefinieerde klassen

Het doel is hier niet om een bestaand antwoord na te bootsen, maar om zelf orde te vinden in de data.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** bij `Unsupervised Learning` ontbreken labels tijdens training.
- **Veelvoorkomende misvatting:** clustering verwarren met classificatie. Bij classificatie zijn de klassen vooraf gekend; bij clustering niet.
- **Link met andere concepten:** [[Machine Learning]], [[Supervised Learning]], [[Reinforcement Learning]], [[K-Means]], [[Data, Example, Feature, Target]], [[Classification vs Regression]], [[Supervised vs Unsupervised vs Reinforcement Learning]]

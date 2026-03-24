---
type: concept-topic
domain: "machine-learning"
parent: "Machine Learning"
related:
  - Machine Learning
  - Classification vs Regression
  - Feature Scaling en Normalization
theme: "instance-based-learning"
aliases:
  - K-Nearest Neighbors (KNN)
---

# K-Nearest Neighbors (KNN)
#concept #ml

## 1. Wat is het kernprobleem?
Hoe maak je een voorspelling op basis van gelijkaardige voorbeelden uit de trainingsdata?

## 2. Intuitieve uitleg
`KNN` kijkt voor een nieuw datapunt naar de `K` meest gelijkaardige voorbeelden die het al kent. Die buren bepalen samen de voorspelling.

## 3. Formele structuur
- is typisch `supervised learning`
- gebruikt een afstandsmaat tussen datapunten
- bij classificatie stemmen de `K` buren over de klasse
- bij regressie neem je vaak een gemiddelde
- is gevoelig aan schaal van features

## 4. Toepassing
Als je een nieuw datapunt hebt met kenmerken van een bloem, kan `KNN` kijken naar de meest gelijkaardige bloemen in de trainingsset om de soort te voorspellen.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** `KNN` leert meestal geen compacte parameterisatie, maar baseert voorspellingen op opgeslagen voorbeelden.
- **Veelvoorkomende misvatting:** `KNN` behandelen alsof het werkt zoals een getraind parametrisch model.
- **Link met andere concepten:** [[Machine Learning]], [[Supervised Learning]], [[Classification vs Regression]], [[Feature Scaling en Normalization]], [[Supervised vs Unsupervised vs Reinforcement Learning]]

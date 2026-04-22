---
type: theory
domain: "machine-learning"
parent: "Machine Learning"
related:
  - Machine Learning
  - Classification vs Regression
  - Feature Scaling en Normalization
  - Supervised Learning
  - KNN Python Worked Example
theme: "instance-based-learning"
aliases:
  - K-Nearest Neighbors (KNN)
---

# K-Nearest Neighbors (KNN)
#concept #ml

K-Nearest Neighbors (KNN) is een algoritme dat een voorspelling maakt door te kijken naar de `K` meest gelijkaardige voorbeelden in de trainingsdata.

## Korte kern

- gebruikt afstand tussen datapunten
- werkt voor classificatie en regressie
- heeft meestal geen expliciete trainingsfase zoals parametrische modellen

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

## 4. Snelle vergelijking

- [[K-Nearest Neighbors (KNN)]] = gebruikt gelijkaardige voorbeelden met labels
- [[K-Means]] = groepeert zonder labels
- [[Linear Regression]] = leert een compacte lineaire relatie in plaats van buurvergelijking

## 5. Toepassing
Als je een nieuw datapunt hebt met kenmerken van een bloem, kan `KNN` kijken naar de meest gelijkaardige bloemen in de trainingsset om de soort te voorspellen.

Kort Python-voorbeeld:

```python
def knn_predict(neighbor_labels):
    return max(set(neighbor_labels), key=neighbor_labels.count)


predicted_label = knn_predict(["setosa", "setosa", "versicolor"])
```

Voor een volledige Python-uitwerking, zie [[KNN Python Worked Example]].

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** `KNN` leert meestal geen compacte parameterisatie, maar baseert voorspellingen op opgeslagen voorbeelden.
- **Veelvoorkomende misvatting:** `KNN` behandelen alsof het werkt zoals een getraind parametrisch model.
- **Link met andere concepten:** [[Machine Learning]], [[Supervised Learning]], [[Classification vs Regression]], [[Feature Scaling en Normalization]], [[K-Means]], [[Linear Regression]], [[Supervised vs Unsupervised vs Reinforcement Learning]], [[KNN Python Worked Example]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

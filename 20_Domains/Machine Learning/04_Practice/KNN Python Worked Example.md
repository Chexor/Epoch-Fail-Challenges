---
type: practice
domain: "machine-learning"
parent: "K-Nearest Neighbors (KNN)"
related:
  - K-Nearest Neighbors (KNN)
  - Supervised Learning
  - Classification vs Regression
  - Feature Scaling en Normalization
theme: "python-ml-implementations"
aliases:
  - KNN Python Worked Example
  - K-Nearest Neighbors Python Example
---

# KNN Python Worked Example
#concept #ml

KNN Python Worked Example toont hoe je een eenvoudige classificatie maakt door de labels van de dichtste buren te laten stemmen.

## Korte kern

- gebruikt afstanden tussen punten
- laat `K` buurpunten stemmen
- is didactisch eenvoudiger dan een volledige library-aanpak

## Ondersteund concept
- [[K-Nearest Neighbors (KNN)]]

## Doel van deze uitwerking
Deze note toont een kleine Python-schets van `KNN` zodat de stemlogica en het belang van gelijkaardige voorbeelden zichtbaar worden.

## Context
Gebruik dit wanneer je wil begrijpen waarom `KNN` voorspelt op basis van buurpunten en niet via getrainde gewichten.

## Codevoorbeeld
```python
def knn_predict(neighbor_labels):
    return max(set(neighbor_labels), key=neighbor_labels.count)


nearest_labels = ["setosa", "setosa", "versicolor"]
print(knn_predict(nearest_labels))
```

## Stap-voor-stap uitleg
- veronderstel dat de `K` dichtste buren al gevonden zijn
- verzamel hun labels in een lijst
- kies het label dat het vaakst voorkomt

## Verwachte output of gedrag
- de output is hier `setosa`
- bij regressie zou je typisch middelen in plaats van stemmen

## Uitwerking
1. Bepaal de dichtste buurpunten.
2. Verzamel hun labels.
3. Laat de labels stemmen.
4. Gebruik het meerderheidslabel als voorspelling.

## Wat toont dit voorbeeld?
- hoe `KNN` op opgeslagen voorbeelden steunt
- waarom de keuze van `K` en de buurselectie belangrijk zijn

## Typische fouten
- vergeten dat features op vergelijkbare schaal moeten staan
- denken dat `KNN` eerst complexe parameters leert zoals een neuraal netwerk

## Verwante concepten
- [[K-Nearest Neighbors (KNN)]]
- [[Supervised Learning]]
- [[Classification vs Regression]]
- [[Feature Scaling en Normalization]]

## Begripsafbakening en verbanden
- **Kernonderscheid:** deze note toont alleen de stemstap van `KNN`, niet de volledige afstandsberekening over een dataset.
- **Veelvoorkomende misvatting:** denken dat `KNN` vooral over training gaat; de kern zit vaak in de predictiefase.
- **Link met andere concepten:** [[K-Nearest Neighbors (KNN)]], [[Supervised Learning]], [[Classification vs Regression]], [[Feature Scaling en Normalization]], [[K-Means]]

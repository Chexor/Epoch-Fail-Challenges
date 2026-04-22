---
type: practice
domain: "machine-learning"
parent: "K-Means"
related:
  - K-Means
  - Unsupervised Learning
  - Classification vs Regression
  - K-Nearest Neighbors (KNN)
theme: "python-ml-implementations"
aliases:
  - K-Means Python Worked Example
  - K-Means Python Example
---

# K-Means Python Worked Example
#concept #ml

K-Means Python Worked Example toont hoe een datapunt aan het dichtste clustercentrum wordt toegewezen.

## Korte kern

- gebruikt afstand tot centroids
- toont de toewijzingsstap van clustering
- houdt de code klein en numeriek eenvoudig

## Ondersteund concept
- [[K-Means]]

## Doel van deze uitwerking
Deze note toont een minimale Python-schets van `K-Means` zodat de kern van centroid-gebaseerde clustering tastbaar wordt.

## Context
Gebruik dit wanneer je wil zien hoe een punt aan een cluster wordt gekoppeld zonder labels te gebruiken.

## Codevoorbeeld
```python
def assign_cluster(point, centroids):
    return min(range(len(centroids)), key=lambda i: abs(point - centroids[i]))


centroids = [2.0, 6.0]
print(assign_cluster(5.2, centroids))
```

## Stap-voor-stap uitleg
- `centroids` bevatten de huidige clustercentra
- voor elk centroid bereken je een afstand
- het dichtste centroid bepaalt het cluster

## Verwachte output of gedrag
- de output is hier `1`, dus het tweede centroid is het dichtst
- in de volledige versie zou je daarna de centroids opnieuw berekenen

## Uitwerking
1. Kies een set initiële centroids.
2. Bereken voor elk punt de afstand tot elk centroid.
3. Wijs het punt toe aan het dichtste centroid.
4. Herhaal later met nieuwe centroidwaarden.

## Wat toont dit voorbeeld?
- hoe `K-Means` zonder labels toch structuur in data zoekt
- waarom clustering draait om herhaalde toewijzing en herberekening

## Typische fouten
- `K-Means` verwarren met classificatie
- vergeten dat de gekozen startcentra het resultaat kunnen beïnvloeden

## Verwante concepten
- [[K-Means]]
- [[Unsupervised Learning]]
- [[Classification vs Regression]]
- [[K-Nearest Neighbors (KNN)]]

## Begripsafbakening en verbanden
- **Kernonderscheid:** deze note toont de toewijzingsstap van `K-Means`, niet de volledige iteratieve trainingslus.
- **Veelvoorkomende misvatting:** denken dat clustering labels voorspelt zoals classificatie; hier ontstaan de groepen juist uit de data zelf.
- **Link met andere concepten:** [[K-Means]], [[Unsupervised Learning]], [[Classification vs Regression]], [[K-Nearest Neighbors (KNN)]], [[Machine Learning]]

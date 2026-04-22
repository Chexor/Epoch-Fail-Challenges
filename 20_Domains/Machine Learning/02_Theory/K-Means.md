---
type: theory
domain: "machine-learning"
parent: "Machine Learning"
related:
  - Machine Learning
  - Unsupervised Learning
  - Classification vs Regression
  - K-Nearest Neighbors (KNN)
  - K-Means Python Worked Example
theme: "clustering-and-unsupervised-learning"
aliases:
  - K-Means
---

# K-Means
#concept #ml

K-Means is een clusteringalgoritme dat ongelabelde datapunten in `K` groepen verdeelt op basis van hun afstand tot clustercentra.

## Korte kern

- is `unsupervised learning`
- wisselt tussen toewijzen en herberekenen van centra
- resultaat hangt af van startpunten en gekozen `K`

## 1. Wat is het kernprobleem?
Hoe kan je ongelabelde data automatisch opdelen in groepen van gelijkaardige punten?

## 2. Intuitieve uitleg
`K-Means` probeert data in `K` clusters te verdelen. Elk datapunt wordt gekoppeld aan het dichtste centrum, en die centra worden telkens herberekend.

## 3. Formele structuur
- is `unsupervised learning`
- kiest vooraf het aantal clusters `K`
- werkt met `centroids`
- herhaalt twee stappen:
  - wijs elk datapunt toe aan het dichtste centrum
  - herbereken de centra
- resultaat hangt af van de startpositie en de gekozen waarde van `K`

## 4. Snelle vergelijking

- [[K-Means]] = groepeert zonder labels
- [[K-Nearest Neighbors (KNN)]] = voorspelt met labels uit buurvoorbeelden
- [[Linear Regression]] = voorspelt een numerieke target en groepeert niet

## 5. Toepassing
Bij klantensegmentatie kan `K-Means` groepen klanten vinden met gelijkaardig koopgedrag, zonder dat er op voorhand labels bestaan.

Kort Python-voorbeeld:

```python
def assign_cluster(point, centroids):
    return min(range(len(centroids)), key=lambda i: abs(point - centroids[i]))


closest_cluster = assign_cluster(5.2, [2.0, 6.0])
```

Voor een volledige Python-uitwerking, zie [[K-Means Python Worked Example]].

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** `K-Means` groepeert zonder labels en hoort dus bij `unsupervised learning`.
- **Veelvoorkomende misvatting:** `K-Means` verwarren met classificatie.
- **Link met andere concepten:** [[Machine Learning]], [[Unsupervised Learning]], [[Classification vs Regression]], [[K-Nearest Neighbors (KNN)]], [[Supervised vs Unsupervised vs Reinforcement Learning]], [[K-Means Python Worked Example]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

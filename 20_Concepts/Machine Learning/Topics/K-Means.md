---
type: concept-topic
domain: "machine-learning"
parent: "Machine Learning"
related:
  - Machine Learning
  - Unsupervised Learning
  - Classification vs Regression
theme: "clustering-and-unsupervised-learning"
aliases:
  - K-Means
---

# K-Means
#concept #ml

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

## 4. Toepassing
Bij klantensegmentatie kan `K-Means` groepen klanten vinden met gelijkaardig koopgedrag, zonder dat er op voorhand labels bestaan.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** `K-Means` groepeert zonder labels en hoort dus bij `unsupervised learning`.
- **Veelvoorkomende misvatting:** `K-Means` verwarren met classificatie.
- **Link met andere concepten:** [[Machine Learning]], [[Unsupervised Learning]], [[Classification vs Regression]], [[Supervised vs Unsupervised vs Reinforcement Learning]]

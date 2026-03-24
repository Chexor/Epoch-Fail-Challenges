---
type: concept-topic
domain: "machine-learning"
parent: "ML Problem Framing"
related:
  - ML Problem Framing
  - Supervised Learning
  - Linear Regression
  - K-Nearest Neighbors (KNN)
theme: "ml-problem-framing"
aliases:
  - Classification vs Regression
---

# Classification vs Regression
#concept #ml

## 1. Wat is het kernprobleem?
Je moet het juiste probleemtype kiezen op basis van wat je wil voorspellen.

## 2. Intuitieve uitleg
Bij classification vraagt het model: "Tot welke klasse hoort dit?" Bij regression vraagt het model: "Welke numerieke waarde hoort hierbij?"

## 3. Formele structuur
- Classification: output is een categorie of label
- Regression: output is een getal
- Voorbeelden labels: `spam`, `geen spam`
- Voorbeelden getallen: prijs, loon, temperatuur

## 4. Toepassing
- spamfilter = classification
- ziekte wel/niet aanwezig = classification
- huisprijs voorspellen = regression

Kijk dus altijd eerst naar het type output, niet naar het algoritme.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** `classification` voorspelt labels of categorieen; `regression` voorspelt numerieke waarden.
- **Veelvoorkomende misvatting:** geordende labels behandelen alsof het gewone getallen zijn.
- **Link met andere concepten:** [[Linear Regression]]

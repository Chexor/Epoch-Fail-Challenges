---
type: atom
domain: "machine-learning"
parent: "Model Evaluation"
related:
  - Model Evaluation
  - Classification vs Regression
  - Validation
theme: "model-evaluation"
aliases:
  - Accuracy
---

# Accuracy
#concept #ml

Accuracy is het aandeel voorspellingen dat exact correct is.

## Korte kern

- eenvoudige metric voor classificatie
- telt correcte voorspellingen op
- kan misleidend zijn bij ongebalanceerde data

## 1. Wat is het kernprobleem?
Hoe meet je snel hoeveel classificatievoorspellingen juist zijn?

## 2. Intuitieve uitleg
Als een model 90 van de 100 labels juist voorspelt, dan is de accuracy 90 procent.

## 3. Formele structuur
- `accuracy = aantal correcte voorspellingen / totaal aantal voorspellingen`
- wordt gebruikt bij classificatie, niet als hoofdmetric voor regressie
- gevoelig voor class imbalance

## 4. Snelle vergelijking
- [[Accuracy]] = fractie correcte labels
- [[Model Evaluation]] = bredere evaluatiecontext
- [[Classification vs Regression]] = helpt zien wanneer accuracy zinvol is

## 5. Toepassing
Bij een balanced dataset met `50%` en `50%` klassen is accuracy vaak een redelijke eerste metric. Bij sterk scheve data kan ze een vals gevoel van kwaliteit geven.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** accuracy zegt hoe vaak je juist zit, maar niet hoe zeker of gebalanceerd je model is.
- **Veelvoorkomende misvatting:** hoge accuracy automatisch gelijkstellen aan een goed model in elke context.
- **Link met andere concepten:** [[Model Evaluation]], [[Validation]], [[Cross-Validation]], [[Classification vs Regression]]

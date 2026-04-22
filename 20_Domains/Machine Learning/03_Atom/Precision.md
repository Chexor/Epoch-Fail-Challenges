---
type: atom
domain: "machine-learning"
parent: "Model Evaluation"
related:
  - Model Evaluation
  - Accuracy
  - Recall
theme: "model-evaluation"
aliases:
  - Precision
---

# Precision
#concept #ml

Precision is het aandeel positieve voorspellingen dat effectief juist positief is.

## Korte kern

- focust op betrouwbaarheid van positieve voorspellingen
- belangrijk wanneer false positives duur zijn
- werkt samen met [[Recall]] als afruil

## 1. Wat is het kernprobleem?
Hoe meet je of een model niet te snel "positief" roept wanneer dat fout zou zijn?

## 2. Intuitieve uitleg
Als een model 20 keer "positief" voorspelt en daarvan zijn er 16 echt positief, dan is de precision `16/20 = 0.80`.

## 3. Formele structuur
- `precision = TP / (TP + FP)`
- `TP` = true positives, `FP` = false positives
- hoge precision betekent weinig valse alarmen binnen positieve voorspellingen

## 4. Snelle vergelijking
- [[Precision]] = hoe betrouwbaar positieve voorspellingen zijn
- [[Recall]] = hoeveel echte positieven je effectief vindt
- [[Accuracy]] = globale fractie correcte voorspellingen

## 5. Toepassing
Bij spamdetectie wil je vaak hoge precision voor de klasse "spam", zodat normale e-mails niet onterecht in spam belanden.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** precision kijkt alleen naar voorspelde positieven, niet naar alle echte positieven.
- **Veelvoorkomende misvatting:** hoge precision betekent niet automatisch dat je veel positieven vindt; je kan nog steeds lage [[Recall]] hebben.
- **Link met andere concepten:** [[Model Evaluation]], [[Recall]], [[Accuracy]], [[Classification]].

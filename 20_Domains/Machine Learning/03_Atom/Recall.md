---
type: atom
domain: "machine-learning"
parent: "Model Evaluation"
related:
  - Model Evaluation
  - Precision
  - Accuracy
theme: "model-evaluation"
aliases:
  - Recall
  - Sensitivity
  - True Positive Rate
---

# Recall
#concept #ml

Recall is het aandeel echte positieve gevallen dat het model correct als positief herkent.

## Korte kern

- focust op hoeveel positieven je niet mist
- belangrijk wanneer false negatives duur zijn
- staat vaak in afruil met [[Precision]]

## 1. Wat is het kernprobleem?
Hoe meet je of een model voldoende echte positieve gevallen detecteert?

## 2. Intuitieve uitleg
Als er 50 echte positieve gevallen zijn en je model vindt er 40, dan is de recall `40/50 = 0.80`.

## 3. Formele structuur
- `recall = TP / (TP + FN)`
- `TP` = true positives, `FN` = false negatives
- hoge recall betekent dat je weinig echte positieven mist

## 4. Snelle vergelijking
- [[Recall]] = hoeveel echte positieven je opvangt
- [[Precision]] = hoe betrouwbaar je positieve voorspellingen zijn
- [[Accuracy]] = globale fractie correcte voorspellingen

## 5. Toepassing
Bij medische screening wil je vaak hoge recall voor de ziekteklasse, zodat zo weinig mogelijk zieke patiënten gemist worden.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** recall kijkt naar alle echte positieven, niet naar alle voorspelde positieven.
- **Veelvoorkomende misvatting:** hoge recall betekent niet automatisch weinig valse alarmen; precision kan tegelijk laag zijn.
- **Link met andere concepten:** [[Model Evaluation]], [[Precision]], [[Accuracy]], [[Classification]].

---
type: concept-topic
domain: "machine-learning"
parent: "Optimization and Training"
related:
  - Optimization and Training
  - Grid Search
  - Learning Rate
theme: "model-selection-and-tuning"
aliases:
  - Parameters vs Hyperparameters
---

# Parameters vs Hyperparameters
#concept #ml

## 1. Wat is het kernprobleem?
Je moet goed onderscheiden wat het model zelf leert en wat jij vooraf kiest.

## 2. Intuitieve uitleg
Parameters zijn de waarden die tijdens training aangepast worden. Hyperparameters zijn instellingen die het leerproces sturen.

## 3. Formele structuur
- Parameters: gewichten, slope, intercept
- Hyperparameters: learning rate, epochs, batch size
- Parameters worden geleerd; hyperparameters worden ingesteld en vaak getuned

## 4. Toepassing
Bij lineaire regressie leert het model bv. `a` en `b`.
Jij kiest vooraf bv. `learning_rate = 0.01` en `epochs = 100`.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** parameters worden geleerd; hyperparameters worden vooraf gekozen of getuned.
- **Veelvoorkomende misvatting:** `batch size` of `learning rate` beschouwen als iets dat het model zelf leert.
- **Link met andere concepten:** [[Grid Search]], [[Learning Rate]], [[Epoch]]

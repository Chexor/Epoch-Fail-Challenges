---
type: concept-topic
domain: "machine-learning"
parent: "Optimization and Training"
related:
  - Optimization and Training
  - Gradient Descent
  - Mini-batch Gradient Descent
theme: "parameter-optimization"
aliases:
  - SGD (Stochastic Gradient Descent)
---

# SGD (Stochastic Gradient Descent)
#concept #ml

## 1. Wat is het kernprobleem?
Volledige batch-updates kunnen traag zijn bij grote datasets.

## 2. Intuitieve uitleg
SGD werkt met heel kleine stukjes data, vaak 1 datapunt per update. Daardoor krijg je snel veel updates, maar ook meer schommelingen in het leerproces.

## 3. Formele structuur
- Batch size = 1
- Parameterupdate na elk individueel sample
- Vaak met willekeurige volgorde per epoch

## 4. Toepassing
Bij een grote dataset hoef je niet te wachten op alle rijen. Na elk sample kan het model al een kleine bijsturing doen.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** `SGD` update parameters na zeer kleine batches en introduceert daardoor meer ruis.
- **Veelvoorkomende misvatting:** schommelende loss meteen interpreteren als mislukte training.
- **Link met andere concepten:** [[Gradient Descent]], [[Mini-batch Gradient Descent]], [[Epoch]]

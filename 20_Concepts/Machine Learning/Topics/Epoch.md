---
type: concept-topic
domain: "machine-learning"
parent: "Optimization and Training"
related:
  - Optimization and Training
  - Gradient Descent
  - Learning Rate
theme: "parameter-optimization"
aliases:
  - Epoch
---

# Epoch
#concept #ml

## 1. Wat is het kernprobleem?
Je moet kunnen benoemen hoeveel keer het model de volledige trainingsset heeft doorlopen.

## 2. Intuitieve uitleg
Een epoch is 1 volledige ronde over alle trainingsdata. Dat betekent niet automatisch 1 update, want dat hangt af van de batch size.

## 3. Formele structuur
- `1 epoch` = alle trainingssamples 1 keer gezien
- Aantal updates per epoch = `n / batch size` als `n` deelbaar is
- Meer epochs betekent vaker bijleren op dezelfde data

## 4. Toepassing
Bij 1000 samples en `batch size = 100` heb je 10 updates per epoch.
Na 5 epochs heeft het model de volledige dataset 5 keer doorlopen.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** een `epoch` is een volledige doorgang door de trainingsset; een iteratie is één update-stap.
- **Veelvoorkomende misvatting:** epoch en iteratie als hetzelfde zien.
- **Link met andere concepten:** [[Mini-batch Gradient Descent]], [[Parameters vs Hyperparameters]]

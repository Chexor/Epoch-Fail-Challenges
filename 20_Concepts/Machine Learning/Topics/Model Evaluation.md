---
type: concept-topic
domain: "machine-learning"
parent: "Machine Learning"
related:
  - Machine Learning
  - Loss Function
  - MAE vs MSE vs RMSE
  - Optimization and Training
theme: "model-evaluation"
aliases:
  - Model Evaluation
---

# Model Evaluation
#concept #ml

Model Evaluation groepeert de concepten waarmee je de fout, kwaliteit en bruikbaarheid van een machine-learningmodel beoordeelt.

## Korte kern

- gaat over foutmaten en evaluatiescores
- helpt modellen vergelijken en interpreteren
- vormt de kapstok voor MAE, MSE, RMSE en R2

## 1. Wat is het kernprobleem?
Hoe bepaal je of een model goed presteert en hoe vergelijk je meerdere modellen op een zinvolle manier?

## 2. Intuitieve uitleg
Een model bouwen is niet genoeg; je moet ook weten hoe goed het werkt. Daarvoor gebruik je foutmaten en evaluatiecriteria die tonen hoe dicht voorspellingen bij de werkelijkheid liggen.

## 3. Formele structuur
Belangrijke concepten binnen deze groep zijn:

- [[Loss Function]]
- [[SSE (Sum of Squared Errors)]]
- [[MAE (Mean Absolute Error)]]
- [[MSE (Mean Squared Error)]]
- [[RMSE (Root Mean Squared Error)]]
- [[R2 en R]]

## 4. Snelle vergelijking

- [[Model Evaluation]] = meten hoe goed een model is
- [[Linear Modeling]] = modelvorm opstellen
- [[Optimization and Training]] = parameters aanpassen om beter te worden

## 5. Toepassing
Als je twee regressiemodellen wil vergelijken, kijk je bijvoorbeeld naar hun `MSE` of `RMSE`. Dat is model evaluation.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** evaluatie meet prestaties; ze traint het model niet zelf.
- **Veelvoorkomende misvatting:** denken dat een lage foutmaat automatisch betekent dat het model inhoudelijk goed begrepen is of generaliseert zonder nuance.
- **Link met andere concepten:** [[Machine Learning]], [[Loss Function]], [[MAE (Mean Absolute Error)]], [[MSE (Mean Squared Error)]], [[RMSE (Root Mean Squared Error)]], [[R2 en R]], [[MAE vs MSE vs RMSE]]

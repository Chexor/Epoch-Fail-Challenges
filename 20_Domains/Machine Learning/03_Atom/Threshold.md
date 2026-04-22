---
type: atom
domain: "machine-learning"
parent: "ML Problem Framing"
related:
  - Linear Classification
  - Step Function
  - Sigmoid Function
  - Logistic Regression
theme: "classification-foundations"
aliases:
  - Threshold
  - Drempel
---

# Threshold
#concept #ml

Een threshold is een drempelwaarde waarboven of waaronder een model van beslissing of klasse verandert.

## Korte kern

- zet een score of kans om naar een klasse
- is cruciaal in binaire classificatie
- komt voor bij perceptron, logistic regression en decision boundaries

## 1. Wat is het kernprobleem?
Hoe maak je van een continue score of kans een concrete ja/nee-beslissing?

## 2. Intuitieve uitleg
Een model kan eerst een score of kans geven. De threshold bepaalt vanaf welk punt je zegt: "dit hoort bij klasse 1" en daaronder bij klasse 0.

## 3. Formele structuur
- bij een perceptron ligt de beslissing rond een harde drempel
- bij logistic regression gebruik je vaak een kansdrempel zoals `0.5`
- de threshold hangt vaak samen met de decision boundary

## 4. Snelle vergelijking
- [[Threshold]] = drempel voor een beslissing
- [[Step Function]] = harde functie die zo'n drempel toepast
- [[Sigmoid Function]] = produceert een continue output waarop je een threshold kan zetten

## 5. Toepassing
Als logistic regression `0.82` voorspelt en je threshold `0.5` is, dan label je het voorbeeld als klasse `1`.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** de threshold beslist over de klasse, niet over hoe de score zelf berekend wordt.
- **Veelvoorkomende misvatting:** denken dat `0.5` altijd de beste threshold is.
- **Link met andere concepten:** [[Linear Classification]], [[Perceptron]], [[Logistic Regression]], [[Step Function]], [[Sigmoid Function]]

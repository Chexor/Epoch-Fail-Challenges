---
type: theory
domain: "machine-learning"
parent: "Loss Function"
related:
  - Loss Function
  - Perceptron
  - Step Function
  - SGD (Stochastic Gradient Descent)
theme: "model-evaluation"
aliases:
  - Perceptron Loss
---

# Perceptron Loss
#concept #ml

Perceptron Loss is een loss function voor perceptrontraining die alleen straf geeft wanneer een datapunt fout geclassificeerd wordt of aan de verkeerde kant van de beslissingsgrens ligt.

## Korte kern

- focust op fout geclassificeerde voorbeelden
- geeft geen straf aan correct geclassificeerde punten met marge
- past bij lineaire binaire classificatie

## 1. Wat is het kernprobleem?
Hoe stuur je een perceptron bij wanneer een voorbeeld aan de verkeerde kant van de scheidingsgrens valt?

## 2. Intuitieve uitleg
Een perceptron hoeft niet elk correct punt verder te belonen. Het kijkt vooral naar de voorbeelden die fout zitten. Alleen die moeten de gewichten mee veranderen.

## 3. Formele structuur
- voor labels `y` in `{-1, +1}` en score `f(x)` zie je vaak: `L = max(0, -y * f(x))`
- als `y * f(x) > 0`, dan zit het punt aan de juiste kant en is de loss `0`
- als `y * f(x) <= 0`, dan krijgt het model een positieve straf

## 4. Snelle vergelijking
- [[Perceptron Loss]] = focust op fout geclassificeerde lineaire beslissingen
- [[Binary Crossentropy]] = werkt met kansen bij binaire classificatie
- [[Loss Function]] = brede familie van trainingsfouten

## 5. Toepassing
Bij een perceptron met harde klasse-uitkomst worden vooral de fout gelabelde punten gebruikt om de gewichten bij te sturen. Correct geclassificeerde punten veroorzaken geen update.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** perceptron loss werkt op beslissingsscores, niet op kansvoorspellingen.
- **Veelvoorkomende misvatting:** denken dat perceptron loss hetzelfde is als binary crossentropy omdat beide voor binaire classificatie gebruikt worden.
- **Link met andere concepten:** [[Loss Function]], [[Perceptron]], [[Step Function]], [[Binary Crossentropy]], [[SGD (Stochastic Gradient Descent)]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

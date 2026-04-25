---
type: theory
domain: "machine-learning"
parent: "Loss Function"
related:
  - Loss Function
  - Support Vector Machine
  - Soft Margin Classification
theme: "model-evaluation"
aliases:
  - Hinge Loss
---

# Hinge Loss
#concept #ml

Hinge Loss is een loss function voor margin-based classificatie die punten bestraft wanneer ze fout zitten of te dicht bij de scheidingsgrens liggen.

## Korte kern

- typisch voor lineaire SVM-classificatie
- beloont niet alleen correcte labels maar ook voldoende marge
- loss is `0` voor correct geclassificeerde punten met genoeg afstand

## 1. Wat is het kernprobleem?
Hoe bestraf je niet alleen foute classificaties, maar ook correcte classificaties met te kleine veiligheidsmarge?

## 2. Intuitieve uitleg
Een punt mag niet gewoon "nipt juist" zitten. Bij hinge loss wil je dat het punt ook voldoende ver van de grens ligt. Anders krijgt het nog steeds straf.

## 3. Formele structuur
- voor labels `y in {-1, +1}` en score `z`: `L = max(0, 1 - y*z)`
- als `y*z >= 1`, dan is de loss `0`
- als `y*z < 1`, dan krijgt het punt straf

## 4. Snelle vergelijking
- [[Hinge Loss]] = margin-based classificatieloss
- [[Binary Crossentropy]] = kansgebaseerde loss voor binaire classificatie
- [[Perceptron Loss]] = focust op misclassificaties zonder expliciete marge van 1

## 5. Toepassing
Bij lineaire SVM-training helpt hinge loss een grens leren die niet alleen correct classificeert, maar ook een stevige marge tussen klassen houdt.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** hinge loss werkt met scores en marges, niet met kansvoorspellingen.
- **Veelvoorkomende misvatting:** hinge loss behandelen alsof het een probabilistische loss is.
- **Link met andere concepten:** [[Support Vector Machine]], [[Soft Margin Classification]], [[Loss Function]], [[Perceptron Loss]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

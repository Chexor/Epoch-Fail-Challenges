---
type: atom
domain: "machine-learning"
parent: "Support Vector Machine"
related:
  - Support Vector Machine
  - Hard Margin Classification
  - Soft Margin Classification
theme: "linear-modeling"
aliases:
  - Support Vectors
---

# Support Vectors
#concept #ml

Support Vectors zijn de datapunten die het dichtst bij de scheidingsgrens van een SVM liggen en daardoor de grens effectief bepalen.

## Korte kern

- liggen op of dicht bij de marge
- bepalen de decision boundary
- punten verder weg hebben veel minder of geen invloed

## 1. Wat is het kernprobleem?
Welke datapunten zijn echt bepalend voor de optimale SVM-scheidingsgrens?

## 2. Intuitieve uitleg
Je kan de meeste punten een beetje verschuiven zonder de SVM-lijn te veranderen, zolang de kritieke randpunten blijven zitten. Die kritieke randpunten zijn de support vectors.

## 3. Formele structuur
- support vectors liggen op de rand van de marge of binnen de marge
- de optimale hypervlakpositie wordt door deze punten bepaald
- punten ver buiten de marge beïnvloeden de oplossing veel minder

## 4. Snelle vergelijking
- [[Support Vectors]] = kritieke punten voor de SVM-grens
- [[Support Vector Machine]] = model dat die grens leert
- [[Soft Margin Classification]] = laat schendingen toe binnen de marge

## 5. Toepassing
In een 2D-plot zijn de support vectors vaak de punten die net tegen de stippellijnen van de marge liggen. Als je die verandert, verandert de grens mee.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** niet elk datapunt is een support vector.
- **Veelvoorkomende misvatting:** denken dat alle trainingspunten even belangrijk zijn voor een SVM.
- **Link met andere concepten:** [[Support Vector Machine]], [[Hard Margin Classification]], [[Soft Margin Classification]]

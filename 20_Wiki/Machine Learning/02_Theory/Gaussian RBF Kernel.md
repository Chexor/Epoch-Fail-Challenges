---
type: theory
domain: "machine-learning"
parent: "Support Vector Machine"
related:
  - Support Vector Machine
  - Kernel Trick
  - Scaling
theme: "linear-modeling"
aliases:
  - Gaussian RBF Kernel
  - RBF Kernel
  - Radial Basis Function Kernel
---

# Gaussian RBF Kernel
#concept #ml

De Gaussian RBF Kernel is een kernel voor SVM's die gelijkenis tussen punten modelleert via afstand en zo flexibele niet-lineaire decision boundaries mogelijk maakt.

## Korte kern

- gebruikt afstand tussen punten
- kan sterk gebogen grenzen leren
- hyperparameters `gamma` en `C` zijn cruciaal

## 1. Wat is het kernprobleem?
Hoe laat je een SVM lokale, niet-lineaire patronen leren in plaats van alleen globale rechte grenzen?

## 2. Intuitieve uitleg
De RBF-kernel kijkt hoe dicht punten bij elkaar liggen. Dichte punten worden als meer gelijkaardig behandeld. Daardoor kan het model rond lokale clusters buigen.

## 3. Formele structuur
- `gamma` bepaalt hoe lokaal of breed het effect van een punt is
- grotere `gamma` geeft smallere belvormen en grilligere grenzen
- `C` bepaalt opnieuw de regularisatie
- feature scaling is hier extra belangrijk omdat afstand centraal staat

## 4. Snelle vergelijking
- [[Gaussian RBF Kernel]] = lokale afstandsgebaseerde niet-lineariteit
- [[Polynomial Kernel]] = polynomiale niet-lineariteit
- [[Kernel Trick]] = bredere techniek die beide mogelijk maakt

## 5. Toepassing
Bij een halve-maan-dataset kan een RBF-kernel vaak een veel natuurlijkere grens leren dan een lineaire classifier.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** RBF werkt via afstandsgelijkenis en is daardoor gevoelig aan schaalverschillen tussen features.
- **Veelvoorkomende misvatting:** `gamma` en `C` onafhankelijk zien van feature scaling.
- **Link met andere concepten:** [[Kernel Trick]], [[Support Vector Machine]], [[Scaling]], [[Grid Search]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

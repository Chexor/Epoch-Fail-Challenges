---
type: theory
domain: "machine-learning"
parent: "Model Fitting"
related:
  - Model Fitting
  - Underfitting
  - Validation
  - Cross-Validation
  - Regularization
theme: "generalization"
aliases:
  - Overfitting
  - Overfit
---

# Overfitting
#concept #ml

Overfitting is het fenomeen waarbij een model te sterk afstemt op trainingsdata en daardoor slechter generaliseert naar nieuwe data.

## Korte kern

- model leert ook ruis en toevallige details
- trainingprestatie lijkt sterk, validatieprestatie valt tegen
- wordt vaak beperkt met regularisatie en goede validatie

## 1. Wat is het kernprobleem?
Hoe herken je dat een model niet echt het onderliggende patroon leert, maar vooral de trainingsset uit het hoofd leert?

## 2. Intuitieve uitleg
Een overfit model lijkt op een student die alleen exacte voorbeeldvragen memoriseert. Op bekende vragen scoort hij top, maar op nieuwe varianten zakt hij door de mand.

## 3. Formele structuur
- typisch patroon: lage fout op training, duidelijk hogere fout op validatie/test
- oorzaak: modelcomplexiteit te hoog voor de beschikbare data of te weinig regularisatie
- signalen:
  - groot verschil tussen training- en validatiescore
  - prestaties dalen op unseen data

## 4. Snelle vergelijking
- [[Overfitting]] = model te complex, slechte generalisatie
- [[Underfitting]] = model te simpel, zwakke prestaties op zowel training als validatie
- [[Model Fitting]] = overkoepelend kader voor goede fit vs under/overfitting

## 5. Toepassing
Bij polynomial regression kan een te hoge graad de trainingspunten bijna perfect volgen, terwijl de fout op de validatieset stijgt. Dan kies je beter een eenvoudiger model of voeg je [[Regularization]] toe.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** overfitting gaat over generalisatieproblemen, niet over het trainingsproces op zich.
- **Veelvoorkomende misvatting:** denken dat een bijna perfecte trainingsscore automatisch een goed model betekent.
- **Link met andere concepten:** [[Model Fitting]], [[Underfitting]], [[Validation]], [[Cross-Validation]], [[Regularization]], [[Train Validation Test Split]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

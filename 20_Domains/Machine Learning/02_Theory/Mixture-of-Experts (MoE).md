---
type: theory
domain: "machine-learning"
parent: "Neural Network Models"
related:
  - Neural Network Models
  - Deep Learning
  - Transformer
  - Engram
  - Machine Learning
theme: "neural-network-models"
aliases:
  - Mixture of Experts
  - MoE
---

# Mixture-of-Experts (MoE)
#concept #ml

Mixture-of-Experts (MoE) is een modelarchitectuur waarbij een gating-mechanisme per input slechts een deel van meerdere gespecialiseerde experts activeert, zodat modelcapaciteit kan schalen zonder telkens alle berekening uit te voeren.

## Korte kern

- een `MoE`-model bevat meerdere experts maar gebruikt er per token meestal maar enkele
- een gate of router beslist welke experts geactiveerd worden
- het doel is meer capaciteit met minder actieve compute per stap

## 1. Wat is het kernprobleem?

Hoe maak je een model veel groter en rijker in capaciteit zonder dat elke inference stap alle parameters volledig moet gebruiken?

## 2. Intuitieve uitleg

Denk aan een team van specialisten. Niet elke vraag moet door iedereen tegelijk opgelost worden. Een router kiest eerst welke specialisten relevant zijn, en alleen die leveren actief werk.

Zo krijg je:

- veel totale modelcapaciteit
- minder actieve berekening per input
- experts die zich kunnen specialiseren in bepaalde patronen of subproblemen

## 3. Formele structuur

Een klassiek `MoE`-systeem bevat:

- meerdere experts
- een gating- of routingfunctie
- een combinatie- of selectiemechanisme

In moderne deep learning gebeurt vaak het volgende:

- een token of hidden state gaat eerst naar een router
- de router kiest de `top-k` meest relevante experts
- alleen die experts worden actief uitgevoerd
- hun outputs worden gewogen samengevoegd

Belangrijke aandachtspunten:

- `load balancing`: vermijden dat altijd dezelfde experts gekozen worden
- `routing`: bepalen welke experts bij welke input passen
- `capacity factor`: limiteren hoeveel tokens een expert per batch aankan

In moderne taalmodellen wordt `MoE` vaak ingebouwd in transformerblokken om de totale parametercapaciteit sterk te verhogen zonder dezelfde groei in actieve compute.

## 4. Snelle vergelijking

- `Mixture-of-Experts (MoE)` = conditionele compute via selectie van experts
- [[Transformer]] = basisarchitectuur waarin zo'n `MoE`-laag vaak geïntegreerd wordt
- [[Engram]] = conditioneel geheugen voor lookup, niet gewoon extra expertcompute

Belangrijk onderscheid met [[Engram]]:

- `MoE` schaalt vooral `neural computation`
- `Engram` voegt expliciet `static memory` toe

## 5. Toepassing

In een groot taalmodel kan een token eerst door attention verwerkt worden, waarna een router beslist welke experts voor dat token geactiveerd worden in de feedforwardfase.

Daardoor kan het model veel meer totale kennis en capaciteit bevatten dan een dense model met dezelfde actieve compute per stap.

## 6. Begripsafbakening en verbanden

- **Kernonderscheid:** `MoE` gaat over conditionele activatie van experts, niet gewoon over een ensemble dat alles parallel laat meestemmen.
- **Veelvoorkomende misvatting:** denken dat alle experts altijd actief zijn; moderne `MoE` draait net om sparse activatie van een kleine subset.
- **Link met andere concepten:** [[Machine Learning]], [[Neural Network Models]], [[Deep Learning]], [[Transformer]], [[Engram]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

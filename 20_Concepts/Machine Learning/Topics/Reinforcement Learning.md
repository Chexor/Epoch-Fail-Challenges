---
type: concept-topic
domain: "machine-learning"
parent: "Learning Paradigms"
related:
  - Learning Paradigms
  - Supervised Learning
  - Unsupervised Learning
  - Supervised vs Unsupervised vs Reinforcement Learning
theme: "learning-paradigms"
aliases:
  - Reinforcement Learning
---

# Reinforcement Learning
#concept #ml

## 1. Wat is het kernprobleem?
Hoe leert een agent goed handelen in een omgeving wanneer hij geen directe juiste antwoorden krijgt, maar alleen beloningen of straffen?

## 2. Intuitieve uitleg
Bij `Reinforcement Learning` leert een systeem door te proberen, fouten te maken en feedback te krijgen in de vorm van een beloning of straf. Het model krijgt dus niet telkens het juiste antwoord, maar moet zelf ontdekken welke acties op lange termijn het meeste opleveren.

Denk aan een spelletje spelen: een agent probeert zetten uit, ziet welke zet punten oplevert, en leert zo geleidelijk een betere strategie.

## 3. Formele structuur
- er is een `agent` die acties uitvoert
- de agent bevindt zich in een `omgeving`
- na een actie krijgt de agent een `reward` of straf
- het doel is een strategie te leren die de totale toekomstige beloning maximaliseert
- leren gebeurt dus via `trial and error`

Belangrijke bouwstenen:

- toestand (`state`)
- actie (`action`)
- beloning (`reward`)
- beleid (`policy`)

## 4. Toepassing
- een agent die leert schaken of een videogame spelen
- een robot die leert navigeren
- systemen die beslissingen leren nemen over meerdere stappen in de tijd

Hier is de feedback vertraagd: een actie kan pas later goed of slecht blijken.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** `Reinforcement Learning` leert via beloningen en interactie, niet via vaste labels.
- **Veelvoorkomende misvatting:** denken dat dit gewoon een variant is van supervised learning. Bij reinforcement learning moet de agent zelf een strategie ontdekken via opeenvolgende beslissingen.
- **Link met andere concepten:** [[Machine Learning]], [[Supervised Learning]], [[Unsupervised Learning]], [[Artificial Intelligence (AI)]], [[Supervised vs Unsupervised vs Reinforcement Learning]]

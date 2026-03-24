---
type: concept-comparison
domain: "machine-learning"
parent: "Learning Paradigms"
related:
  - Supervised Learning
  - Unsupervised Learning
  - Reinforcement Learning
theme: "three-main-learning-paradigms"
aliases:
  - Supervised vs Unsupervised vs Reinforcement Learning
---

# Supervised vs Unsupervised vs Reinforcement Learning
#concept #ml

## Wat wordt hier vergeleken?
- [[Supervised Learning]]
- [[Unsupervised Learning]]
- [[Reinforcement Learning]]

## Kernverschil
Deze drie leerparadigma's verschillen vooral in **welke feedback het model krijgt tijdens het leren**.

- `Supervised Learning`: juiste antwoorden zijn beschikbaar
- `Unsupervised Learning`: geen juiste antwoorden beschikbaar
- `Reinforcement Learning`: feedback komt via beloningen en straffen over de tijd

## Vergelijking

| Aspect | Supervised | Unsupervised | Reinforcement |
| --- | --- | --- | --- |
| Trainingsdata | `(x, y)` | `x` zonder labels | interacties met omgeving |
| Feedback | direct juist antwoord | geen expliciet antwoord | reward of straf |
| Doel | voorspellen | structuur vinden | strategie leren |
| Typische taken | classificatie, regressie | clustering | sequential decision making |
| Voorbeelden | [[Linear Regression]], [[K-Nearest Neighbors (KNN)]], [[Neural Network]] | [[K-Means]] | game agents, robotnavigatie |
| Centrale vraag | wat is de juiste output? | welke structuur zit in de data? | welke actie levert op lange termijn het meeste op? |
| Typische fout | denken dat elk ML-probleem labels heeft | clustering verwarren met classificatie | reinforcement zien als supervised learning met extra stappen |

## Wanneer gebruik je wat?
- **Supervised Learning:** als je voorbeelden hebt met een correct antwoord of target.
- **Unsupervised Learning:** als je alleen data hebt en zelf groepen of patronen wil ontdekken.
- **Reinforcement Learning:** als een agent moet leren handelen via opeenvolgende beslissingen en beloningen.

## Waarom is dit onderscheid belangrijk?
Dit onderscheid helpt je bijna altijd het juiste probleemtype herkennen. Zodra je weet welke feedback beschikbaar is, wordt het veel duidelijker welk type model of algoritme logisch is.

---
type: examen-focus
vak: Introduction to AI
status: actief
---

# Focus voor vrijdag

> [!info]- Inhoudsopgave
> - [[#Korte kern]]
> - [[#1. Absolute topprioriteit]]
> - [[#2. Zoekalgoritmes die je echt moet kunnen]]
> 	- [[#Eerst volledig beheersen]]
> 	- [[#Daarna stevig kennen]]
> 	- [[#Wat je per algoritme moet kunnen zeggen]]
> - [[#3. Wat je moet kunnen uitschrijven op een graaf]]
> 	- [[#Op papier altijd tonen]]
> - [[#4. Klassieke vergelijkingen die je moet kennen]]
> - [[#5. Examenvallen]]
> - [[#6. Machine Learning: compacter blokken]]
> 	- [[#Wat je mondeling moet kunnen uitleggen]]
> - [[#7. Slimste blokvolgorde voor de komende dagen]]
> - [[#8. Hoofdnota's voor het examen]]
> - [[#9. Beste Base voor vrijdag]]

Dit is de kortste en belangrijkste focuslijst voor het examen `Introduction to AI` komende vrijdag.

## Korte kern

- focus eerst op **search algorithms**
- zorg dat je `BFS`, `DFS`, `UCS`, `Hill Climbing`, `Greedy` en `A*` echt kan **uitschrijven op papier**
- leer ML compacter: vooral de **grote verschillen** en **basisintuïtie**

## 1. Absolute topprioriteit

Deze concepten moet je zeker kennen:

- [[State Space]]
- [[Search Algorithm]]
- [[Frontier]]
- [[Explored Set]]
- [[Path Cost]]
- [[Branching Factor]]
- [[Heuristic]]
- [[g(n)]], [[h(n)]], [[f(n)]]
- [[Admissible Heuristic]]
- [[Consistent Heuristic]]

Bijbehorende cursustopics:

- `Topic 3 - State-spaced Representation`
- `Topic 4 - Blind Search`
- `Topic 5a - Vergelijking van Algoritmen`
- `Topic 5b - Blind Search 2`
- `Topic 6 - Heuristic Search`
- `Topic 7 - Optimal Search`
- `Topic 3_7 - Overview Search Algorithms`

## 2. Zoekalgoritmes die je echt moet kunnen

### Eerst volledig beheersen

- [[Breadth-First Search (BFS)]]
- [[Depth-First Search (DFS)]]
- [[Uniform-Cost Search (UCS)]]
- [[Hill Climbing]]
- [[Greedy Best-First Search]]
- [[A-star Search]]

### Daarna stevig kennen

- [[Depth-Limited Search (DLS)]]
- [[Iterative Deepening Search (IDS)]]
- [[Bi-directional Search]]
- [[IDA-star (Iterative Deepening A-star)]]

### Wat je per algoritme moet kunnen zeggen

- gebruikte datastructuur
- keuzeregel
- compleet of niet
- optimaal of niet
- grootste sterkte
- grootste zwakte

## 3. Wat je moet kunnen uitschrijven op een graaf

Voor het examendeel met een graaf moet je vooral heel vlot kunnen:

- [[BFS Worked Example]]
- [[DFS Worked Example]]
- [[UCS Worked Example]]
- [[Hill Climbing Worked Example]]
- [[Greedy Best-First Search Worked Example]]
- [[A-star Worked Example]]
- [[IDS Worked Example]]

### Op papier altijd tonen

- de frontier na elke stap
- welke node gekozen wordt
- waarom die gekozen wordt
- het gevonden pad
- bij `UCS` en `A*`: de totale kost

Handige hulpmiddelen:

- [[04_Frontier correct uitschrijven op papier|04_Frontier correct uitschrijven op papier]]

## 4. Klassieke vergelijkingen die je moet kennen

- [[BFS vs UCS]]
- [[BFS vs DFS vs UCS vs Greedy vs A-star|BFS vs DFS vs UCS vs Greedy vs A*]]
- [[Hill Climbing vs Greedy Best-First Search]]
- [[Admissible vs Consistent Heuristic]]
- [[Tree Search vs Graph Search]]

## 5. Examenvallen

- `BFS` is alleen optimaal bij gelijke stapkosten
- `UCS` kijkt naar kost, niet naar diepte
- `Greedy` gebruikt alleen `h(n)`
- `A*` gebruikt `g(n) + h(n)`
- `Hill Climbing` kiest alleen uit directe buren
- een doelnode is pas echt relevant wanneer ze gekozen wordt, niet alleen gegenereerd

## 6. Machine Learning: compacter blokken

Dit deel lijkt minder zwaar door te wegen, dus focus op het verschil tussen de kernideeën:

- [[Machine Learning]]
- [[Supervised Learning]]
- [[Unsupervised Learning]]
- [[Reinforcement Learning]]
- [[Supervised vs Unsupervised vs Reinforcement Learning]]
- [[Machine Learning vs Deep Learning]]
- [[Classification vs Regression]]
- [[Linear Regression]]
- [[K-Nearest Neighbors (KNN)]]
- [[K-Means]]
- [[Neural Network]]
- [[Deep Learning]]
- [[Convolutional Neural Network (CNN)]]

### Wat je mondeling moet kunnen uitleggen

- verschil tussen supervised, unsupervised en reinforcement learning
- verschil tussen classification, regression en clustering
- basisidee van linear regression, KNN en K-means
- basisopbouw van een neural network
- waarom CNN goed werkt voor beelden

## 7. Slimste blokvolgorde voor de komende dagen

1. `State Space` + `Search Algorithm`
2. `BFS`, `DFS`, `UCS`
3. `Heuristiek`, `g(n)`, `h(n)`, `f(n)`
4. `Hill Climbing`, `Greedy`, `A*`
5. `Admissible`, `Consistent`, `Tree vs Graph Search`
6. graafoefeningen uitschrijven
7. compact ML herhalen

## 8. Hoofdnota's voor het examen

- [[00_Centrale examensamenvatting|00_Centrale examensamenvatting]]
- [[02_Workflow met Bases|02_Workflow met Bases]]
- [[03_Algoritmes herkennen aan code|03_Algoritmes herkennen aan code]]
- [[04_Frontier correct uitschrijven op papier|04_Frontier correct uitschrijven op papier]]
- [[Samenvatting - Topic 3_7 - Overview Search Algorithms|Samenvatting Topic 3_7 - Overview Search Algorithms]]
- [[Samenvatting - Topic 4 - Blind Search|Samenvatting Topic 4 - Blind Search]]
- [[Samenvatting - Topic 6 - Heuristic Search|Samenvatting Topic 6 - Heuristic Search]]
- [[Samenvatting - Topic 7 - Optimal Search|Samenvatting Topic 7 - Optimal Search]]

## 9. Beste Base voor vrijdag

- [[Base - AI Examen Cockpit.base|Base - AI Examen Cockpit]]

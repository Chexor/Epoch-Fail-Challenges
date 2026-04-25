---
type: practice
domain: "artificial-intelligence"
parent: "Greedy Best-First Search"
related:
  - Priority Queue
  - h(n)
  - Frontier
theme: "step-by-step-search-execution"
aliases:
  - Greedy Best-First Search Worked Example
  - Greedy Best-First Search
---

# Greedy Best-First Search Worked Example
#concept #ai

Greedy Best-First Search Worked Example kort uitgelegd: wat het is, waarom het telt en wanneer je het gebruikt.
## Ondersteund concept
- [[Greedy Best-First Search]]

## Doel van deze uitwerking
Deze note toont hoe `Greedy` uit de volledige frontier kiest op basis van de laagste heuristische waarde `h(n)`.

## Context
Gebruik dit wanneer je op examen de `priority queue` moet uitschrijven voor een heuristische zoekopdracht.

## Voorbeeldgraaf
- start: `A`
- doel: `G`
- heuristieken: `h(A)=6`, `h(B)=4`, `h(C)=5`, `h(D)=6`, `h(E)=1`, `h(F)=2`, `h(G)=0`

![[Greedy Best-First Search Diagram.png]]
## Uitwerking
1. Start met `PQ: [A (h=6)]`.
2. Expandeer `A`: `PQ: [A-B (4), A-C (5)]`.
3. Expandeer `A-B`: `PQ: [A-B-E (1), A-C (5), A-B-D (6)]`.
4. Expandeer `A-B-E`: `PQ: [A-B-E-G (0), A-C (5), A-B-D (6)]`.
5. Kies `A-B-E-G`: doel gevonden.

## Wat toont dit voorbeeld?
- `Greedy` kiest de node die het dichtst bij het doel **lijkt** te liggen
- het gebruikt een volledige [[Frontier]], in tegenstelling tot [[Hill Climbing]]
- het kijkt niet naar reeds gemaakte kost

## Typische fouten
- `Greedy` verwarren met `A*`
- vergeten dat `h(n)` geen garantie geeft op een goedkoop totaal pad
- de `priority queue` noteren zonder heuristische waarde

## Verwante concepten
- [[Greedy Best-First Search]]
- [[Priority Queue]]
- [[h(n)]]
- [[Hill Climbing vs Greedy Best-First Search]]

## Wat studeer je hierna?
- [[A-star Search]]
- [[Heuristic]]
- [[BFS vs DFS vs UCS vs Greedy vs A-star|BFS vs DFS vs UCS vs Greedy vs A*]]

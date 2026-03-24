---
type: concept-execution
domain: "artificial-intelligence"
parent: "Depth-First Search (DFS)"
related:
  - Frontier
  - Stack
  - State Space
theme: "step-by-step-search-execution"
aliases:
  - DFS Worked Example
  - DFS
---

# DFS Worked Example
#concept #ai

## Ondersteund concept
- [[Depth-First Search (DFS)]]

## Doel van deze uitwerking
Deze note toont hoe `DFS` stap voor stap een tak volgt en waarom het zo weinig geheugen gebruikt.

## Context
Gebruik dit wanneer je op examen moet tonen hoe `DFS` via een `stack` werkt en waarom het snel diep in een tak duikt.

## Voorbeeldgraaf
- start: `A`
- doel: `G`
- buren: `A -> B, C`, `B -> D, E`, `C -> F`, `D -> G`

![[DFS Diagram.png]]
## Uitwerking
1. Start met `Stack: [A]`.
2. Expandeer `A` en zet opvolgers zo dat `B` eerst genomen wordt: `Stack: [A-C, A-B]`.
3. Neem `A-B` en voeg `A-B-D`, `A-B-E` toe: `Stack: [A-C, A-B-E, A-B-D]`.
4. Neem `A-B-D` en voeg `A-B-D-G` toe: `Stack: [A-C, A-B-E, A-B-D-G]`.
5. Neem `A-B-D-G`: doel gevonden.

## Wat toont dit voorbeeld?
- `DFS` kiest steeds de laatst toegevoegde node
- de `stack` duwt het algoritme diep in 1 tak
- het eerste doel is niet noodzakelijk het beste doel

## Typische fouten
- kinderen in de verkeerde volgorde op de stack zetten
- `DFS` verwarren met `BFS`
- aannemen dat een snelle oplossing automatisch optimaal is

## Verwante concepten
- [[Depth-First Search (DFS)]]
- [[Stack]]
- [[Frontier]]
- [[Iterative Deepening Search (IDS)]]

## Wat studeer je hierna?
- [[Depth-Limited Search (DLS)]]
- [[Iterative Deepening Search (IDS)]]
- [[BFS vs DFS vs UCS vs Greedy vs A-star|BFS vs DFS vs UCS vs Greedy vs A*]]

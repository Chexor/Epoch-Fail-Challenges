---
type: practice
domain: "graph-theory"
parent: "Padlengte via Matrixmachten"
related:
  - Verbindingsmatrix
  - Graaf
  - Markov-matrix
theme: "path-counting"
aliases:
  - Paden Tellen met A^k Worked Example
  - Paden Tellen met A^k
---

# Paden Tellen met A^k Worked Example
#concept #grafen

## Ondersteund concept
- [[Padlengte via Matrixmachten]]

## Doel van deze uitwerking
Deze note toont hoe je een verbindingsmatrix machtsverheft en daarna een specifiek element interpreteert als aantal paden van lengte `k`.

## Context
Gebruik dit wanneer je een netwerkvraag wilt omzetten naar een matrixvraag, bijvoorbeeld: “Hoeveel manieren zijn er om in 3 stappen van knoop 1 naar knoop 4 te gaan?”

## Uitwerking
1. Stel de verbindingsmatrix `A` van de graaf op.
2. Bereken `A^3`.
3. Zoek het element op positie `(1,4)` in `A^3`.
4. Interpreteer dat getal als het aantal paden van lengte 3 van knoop 1 naar knoop 4.

## Wat toont dit voorbeeld?
- matrixmachten zijn niet alleen algebraische bewerkingen, maar dragen directe netwerkbetekenis
- het `(i,j)`-element van `A^k` is de brug tussen rekenen en interpreteren

## Typische fouten
- wel `A^k` berekenen maar vergeten wat het gezochte element precies betekent
- knoopindexen of matrixposities door elkaar halen

## Verwante concepten
- [[Verbindingsmatrix]]
- [[Padlengte via Matrixmachten]]
- [[Markov-matrix]]

## Wat studeer je hierna?
- [[Padlengte via Matrixmachten]]
- [[Markov-matrix]]
- [[00_Overzicht Graph Theory]]

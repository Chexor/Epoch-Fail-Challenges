---
type: concept-execution
domain: "linear-algebra"
parent: "Gauss-Jordan Eliminatie (rref)"
related:
  - Inverse matrix
  - Eenheidsmatrix
  - Matrix notatie en dimensies
theme: "row-reduction"
aliases:
  - Gauss-Jordan Worked Example
  - Gauss-Jordan
---

# Gauss-Jordan Worked Example
#concept #linal

## Ondersteund concept
- [[Gauss-Jordan Eliminatie (rref)]]

## Doel van deze uitwerking
Deze note toont stap voor stap hoe je een matrix met elementaire rijoperaties naar rref brengt. Het doel is de procedure tastbaar maken en te tonen hoe rijreductie structuur zichtbaar maakt.

## Context
Gebruik dit wanneer je een stelsel wil oplossen of wil begrijpen hoe rijoperaties een matrix vereenvoudigen.

## Uitwerking
1. Start met de matrix `[[1, 2], [3, 4]]`.
2. Trek `3 * rij 1` af van `rij 2` zodat de eerste kolom onder de pivot nul wordt.
3. Normaliseer de nieuwe tweede rij zodat de pivot `1` wordt.
4. Gebruik de tweede rij om de waarde boven die pivot nul te maken.
5. Je eindigt in rref, waar de pivots duidelijk zichtbaar zijn.

## Wat toont dit voorbeeld?
- Gauss-Jordan is een systematische manier om structuur uit een matrix te halen
- de volgorde van rijoperaties is doelgericht: pivots maken, normaliseren, wegwerken

## Typische fouten
- rijoperaties uitvoeren zonder duidelijk pivotdoel
- vergeten een pivotrij te normaliseren voor je andere waarden elimineert

## Verwante concepten
- [[Inverse matrix]]
- [[Eenheidsmatrix]]
- [[Matrix notatie en dimensies]]

## Wat studeer je hierna?
- [[Gauss-Jordan Eliminatie (rref)]]
- [[Inverse matrix]]
- [[00_Overzicht Linear Algebra]]

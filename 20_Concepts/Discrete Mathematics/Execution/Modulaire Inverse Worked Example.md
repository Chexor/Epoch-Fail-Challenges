---
type: concept-execution
domain: "discrete-mathematics"
parent: "Modulaire inverse"
related:
  - Modulorekenen
  - Euler phi-functie
  - Recurrente betrekking
theme: "discrete-procedure-solving"
aliases:
  - Modulaire Inverse Worked Example
  - Modulaire Inverse
---

# Modulaire Inverse Worked Example
#concept #discrete

## Ondersteund concept
- [[Modulaire inverse]]

## Doel van deze uitwerking
Deze note toont hoe je een modulaire inverse berekent via een concreet stappenplan, zodat “delen modulo” niet abstract blijft.

## Context
Gebruik dit wanneer je een inverse van `a` modulo `n` nodig hebt, bijvoorbeeld in cryptografie of codeertheorie.

## Uitwerking
1. Neem bijvoorbeeld `5x ≡ 1 (mod 17)`.
2. Controleer eerst dat `ggd(5,17) = 1`.
3. Zoek een getal `x` zodat `5x` rest 1 geeft modulo 17.
4. Je vindt `x = 7`, want `5 * 7 = 35 ≡ 1 (mod 17)`.
5. Dus de modulaire inverse van 5 modulo 17 is 7.

## Wat toont dit voorbeeld?
- een inverse bestaat niet altijd, maar alleen bij relatieve priemheid
- een discrete rekenregel kan toch heel operationeel toegepast worden
- voor grotere getallen is het uitgebreid algoritme van Euclides meestal de standaardprocedure

## Typische fouten
- geen gcd-check doen voor je naar een inverse zoekt
- gewone deling verwarren met modulo-inversie

## Verwante concepten
- [[Modulorekenen]]
- [[Modulaire inverse]]
- [[Euler phi-functie]]

## Wat studeer je hierna?
- [[Modulaire inverse]]
- [[Euler phi-functie]]
- [[00_Overzicht Discrete Mathematics]]

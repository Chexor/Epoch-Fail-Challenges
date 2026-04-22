---
type: practice
domain: "computer-science"
parent: "Datatypes"
related:
  - uint8
  - float32
  - float64
theme: "data-representation-and-computation"
aliases:
  - Datatypekeuze Worked Example
  - Datatypekeuze
---

# Datatypekeuze Worked Example
#concept #cs

## Ondersteund concept
- [[Datatypes]]

## Doel van deze uitwerking
Deze note toont hoe je een datatype kiest op basis van bereik, precisie en geheugenbeperkingen.

## Context
Gebruik dit wanneer je moet beslissen of een waarde beter in een integer, een compact kommagetaltype of een preciezer kommagetaltype past.

## Uitwerking
1. Stel dat je grijswaarden van een afbeelding opslaat.
2. De waarden lopen van `0` tot `255`.
3. Negatieve waarden zijn niet nodig.
4. `uint8` is dan een goede keuze, omdat 8 bits exact 256 mogelijke waarden geven.
5. Voor grote numerieke arrays in machine learning kan `float32` beter zijn dan `float64` als geheugenbesparing en snelheid belangrijk zijn.

## Wat toont dit voorbeeld?
- datatypekeuze is een praktische ontwerpbeslissing, geen puur theoretische naamkeuze
- bereik, teken en precisie bepalen samen de beste keuze

## Typische fouten
- een te groot datatype kiezen zonder noodzaak
- een te klein datatype kiezen waardoor overflow of precisieverlies ontstaat

## Verwante concepten
- [[Datatypes]]
- [[uint8]]
- [[float32 vs float64]]

## Wat studeer je hierna?
- [[Datatypes]]
- [[float32 vs float64]]
- [[00_Overzicht Computer Science]]

---
type: concept-map
domain: "computer-science"
parent:
related:
  - uint8
  - float32
  - float64
theme: "data-representation-and-computation"
aliases:
  - Datatypes
---

# Datatypes
#concept #cs

## Waarom bestaat deze conceptgroep?

Een computer moet weten hoe hij een waarde moet interpreteren: als geheel getal, als kommagetal, als teken, als bits, enzovoort. Datatypes maken die interpretatie expliciet.

## Groot plaatje

Datatypes bepalen:
- welk soort waarde je kunt opslaan
- hoeveel geheugen daarvoor nodig is
- welk bereik mogelijk is
- hoeveel precisie behouden blijft

Ze vormen dus de brug tussen abstracte data en concrete opslag in geheugen.

## Kernonderdelen
- [[uint8]]
- [[float32]]
- [[float64]]

## Hoe hangen deze samen?
- `uint8` is compact en geschikt voor kleine niet-negatieve gehele waarden
- `float32` en `float64` zijn kommagetaltypes met verschillende precisie en geheugenverbruik
- datatypekeuze is altijd een afweging tussen bereik, precisie en efficiëntie

## Aanbevolen leerpad
1. [[Bit en Byte]]
2. [[Signed vs Unsigned]]
3. [[uint8]]
4. [[float32]]
5. [[float64]]
6. [[float32 vs float64]]

## Toepassingen
- beeldrepresentatie
- numerieke berekeningen
- embedded systems
- machine learning arrays en tensors

## Verwante concepten
- [[float32 vs float64]]
- [[Datatypekeuze Worked Example]]
- [[00_Overzicht Computer Science]]

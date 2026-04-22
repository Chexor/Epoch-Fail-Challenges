---
type: theory
domain: "computer-science"
parent:
related:
  - Ordered Processing and Selection
theme: "data-representation-and-computation"
aliases:
  - Data Representation
---

# Data Representation
#concept #cs

Data Representation groepeert de concepten die uitleggen hoe een computer waarden intern voorstelt in bits, bytes en datatypes.

## Korte kern

- vormt de kapstok voor bits, bytes en numerieke datatypes
- helpt bereik, precisie en geheugenverbruik begrijpen
- is fundamenteel voor correcte berekeningen en datatypekeuzes

## 1. Wat is het kernprobleem?
Hoe wordt informatie intern voorgesteld zodat een computer ze kan opslaan, interpreteren en verwerken?

## 2. Intuitieve uitleg
Een computer ziet geen "getallen" of "teksten" zoals wij die zien. Alles moet vertaald worden naar patronen van bits. Data representation legt uit hoe die vertaling werkt.

## 3. Formele structuur
Belangrijke deelconcepten zijn:

- [[Bit en Byte]]
- [[Signed vs Unsigned]]
- [[uint8]]
- [[float32]]
- [[float64]]

Verwante vergelijkingen en toepassingen:

- [[float32 vs float64]]
- [[Datatypekeuze Worked Example]]

## 4. Snelle vergelijking

- [[Data Representation]] = hoe waarden intern worden voorgesteld
- [[Ordered Processing and Selection]] = hoe data in structuren geordend en gekozen wordt
- [[Communication Protocols]] = hoe systemen data uitwisselen

## 5. Toepassing
Wanneer je moet kiezen tussen `uint8`, `float32` en `float64`, werk je in feite met data representation: hoeveel bits zijn beschikbaar, wat is het bereik en hoeveel precisie heb je nodig?

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** deze note gaat over interne representatie van waarden, niet over algoritmes of communicatieprotocollen.
- **Veelvoorkomende misvatting:** datatypekeuze zien als puur syntactische programmeerkeuze in plaats van als representatieprobleem.
- **Link met andere concepten:** [[Bit en Byte]], [[Signed vs Unsigned]], [[uint8]], [[float32]], [[float64]], [[Datatypes]], [[float32 vs float64]]

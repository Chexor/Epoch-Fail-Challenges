---
type: theory
domain: "computer-science"
parent: "Data Representation"
related:
  - Data Representation
  - Bit en Byte
  - uint8
theme: "data-representation-and-computation"
aliases:
  - Signed vs Unsigned
---

# Signed vs Unsigned
#concept #cs

## 1. Wat is het kernprobleem?
Hoe verandert het mogelijke bereik van een datatype wanneer je al dan niet negatieve waarden wilt toelaten?

## 2. Intuïtieve uitleg
Bij unsigned gebruik je alle bitpatronen voor niet-negatieve waarden. Bij signed reserveer je een deel van de representatie om ook negatieve waarden mogelijk te maken.

## 3. Formele structuur
- unsigned types hebben geen negatieve waarden
- signed types laten zowel negatieve als positieve waarden toe
- hetzelfde aantal bits geeft dus een ander bereik naargelang signed of unsigned

## 4. Toepassing
Een `uint8` gebruikt 8 bits voor waarden van `0` tot `255`. Een signed 8-bit integer gebruikt hetzelfde geheugen, maar moet ook negatieve waarden kunnen voorstellen en heeft dus een ander bereik.

## 5. Examengerichte vertaling
- **Typische vraag:** Waarom heeft een unsigned type een groter niet-negatief bereik dan een signed type met evenveel bits?
- **Vaak gemaakte fout:** denken dat signed en unsigned alleen een naamverschil zijn zonder impact op representatie.
- **Link met andere concepten:** [[Datatypes]], [[uint8]], [[Bit en Byte]]

## Context in het domein
- Overzicht: [[00_Overzicht Computer Science]]
- Umbrella: [[Datatypes]]

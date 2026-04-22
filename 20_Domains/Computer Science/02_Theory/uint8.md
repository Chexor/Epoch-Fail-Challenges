---
type: theory
domain: "computer-science"
parent: "Data Representation"
related:
  - Data Representation
  - Bit en Byte
  - Signed vs Unsigned
  - float32
theme: "data-representation-and-computation"
aliases:
  - uint8
---

# uint8
#concept #cs

## 1. Wat is het kernprobleem?
Je moet weten hoe kleine niet-negatieve gehele waarden compact opgeslagen worden.

## 2. Intuitieve uitleg
`uint8` is een datatype voor gehele getallen zonder teken van `0` tot `255`. Het is compact en geschikt voor waarden die nooit negatief zijn.

## 3. Formele structuur
- `u` = unsigned
- `int` = geheel getal
- `8` = 8 bits = 1 byte
- Bereik: `0` t.e.m. `255`

## 4. Toepassing
Pixelwaarden in afbeeldingen worden vaak als `uint8` opgeslagen:
- `0` = zwart
- `255` = wit

## 5. Examengerichte vertaling
- **Typische vraag:** Waarom kan `uint8` geen negatieve waarden bevatten?
- **Vaak gemaakte fout:** Denken dat `uint8` hetzelfde is als een gewone signed integer.
- **Link met andere concepten:** [[float32]], [[float64]]

## Context in het domein
- Overzicht: [[00_Overzicht Computer Science]]
- Umbrella: [[Datatypes]]
- Vergelijking: [[float32 vs float64]]

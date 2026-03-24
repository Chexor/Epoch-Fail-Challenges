---
type: concept-topic
domain: "computer-science"
parent: "Data Representation"
related:
  - Data Representation
  - Signed vs Unsigned
  - uint8
  - Datatypes
theme: "data-representation-and-computation"
aliases:
  - Bit en Byte
---

# Bit en Byte
#concept #cs

## 1. Wat is het kernprobleem?
Hoe bouw je digitale representatie op uit de kleinste opslagseenheden van een computer?

## 2. Intuïtieve uitleg
Een bit is de kleinste keuze-eenheid: 0 of 1. Een byte bundelt typisch 8 bits en vormt zo een praktisch opslagpakket voor data.

## 3. Formele structuur
- 1 bit kan 2 waarden voorstellen
- 1 byte = 8 bits
- met meer bits groeit het aantal mogelijke combinaties exponentieel

## 4. Toepassing
Met 8 bits kun je `2^8 = 256` verschillende patronen opslaan. Daarom kan een type zoals `uint8` waarden van 0 tot 255 voorstellen.

## 5. Examengerichte vertaling
- **Typische vraag:** Hoeveel verschillende waarden kun je voorstellen met `n` bits?
- **Vaak gemaakte fout:** bits en bytes door elkaar halen of vergeten dat 8 bits 256 combinaties geven.
- **Link met andere concepten:** [[Datatypes]], [[uint8]], [[Signed vs Unsigned]]

## Context in het domein
- Overzicht: [[00_Overzicht Computer Science]]
- Umbrella: [[Datatypes]]

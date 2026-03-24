---
type: concept-topic
domain: "computer-science"
parent:
related:
  - Ordered Processing and Selection
theme: "embedded-communication"
aliases:
  - Communication Protocols
---

# Communication Protocols
#concept #cs

Communication Protocols groepeert de regels en standaarden waarmee hardwarecomponenten of systemen gegevens met elkaar uitwisselen.

## Korte kern

- vormt de kapstok voor communicatiebussen zoals `SPI`
- helpt begrijpen hoe toestellen data uitwisselen
- is belangrijk in embedded systems en hardware-interfacing

## 1. Wat is het kernprobleem?
Hoe laat je verschillende componenten gestructureerd en betrouwbaar met elkaar communiceren?

## 2. Intuitieve uitleg
Als twee systemen gegevens willen uitwisselen, moeten ze afspreken in welk tempo, via welke lijnen en volgens welke regels dat gebeurt. Die afspraken vormen samen een communicatieprotocol.

## 3. Formele structuur
Belangrijke concepten in deze groep zijn:

- [[SPI (Serial Peripheral Interface)|SPI]]
- [[IO-expander]]

Vaak zijn zulke protocollen relevant voor:

- microcontrollers
- sensoren
- uitbreidingschips

## 4. Snelle vergelijking

- [[Communication Protocols]] = regels voor gegevensuitwisseling
- [[Data Representation]] = hoe waarden intern voorgesteld zijn
- [[Ordered Processing and Selection]] = hoe gegevens verwerkt of geselecteerd worden

## 5. Toepassing
Wanneer een microcontroller met een sensor of IO-uitbreidingschip praat via een seriële bus, zit je in het domein van communication protocols.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** communicatieprotocollen gaan over gegevensuitwisseling tussen systemen, niet over de interne representatie van waarden.
- **Veelvoorkomende misvatting:** een protocol verwarren met een datatype of met een fysiek component zelf.
- **Link met andere concepten:** [[SPI (Serial Peripheral Interface)|SPI]], [[IO-expander]], [[Data Representation]]

---
type: theory
domain: "iot"
parent: Internet of Things (IoT)
related:
  - SPI (Serial Peripheral Interface)
  - IO-expander
  - USART en UART
theme: "embedded-communication"
aliases:
  - I2C
  - Inter-Integrated Circuit
---

# I2C
#concept #iot #embedded #communication


I2C is een seriële, synchrone tweedraadsbus waarmee meerdere chips op hetzelfde communicatienetwerk kunnen praten.

## Korte kern

- gebruikt `SCL` en `SDA` met adressering per device
- ondersteunt meerdere slaves op één bus met minimale bedrading
- is zeer geschikt voor sensoren en configuratieverkeer

## Probleem

Hoe verbind je meerdere peripherals efficiënt zonder voor elk device aparte datalijnen te voorzien?

## Intuïtie

I2C werkt als een gedeelde bus: master en slaves hangen op dezelfde twee draden. De master start communicatie en kiest een target via adres, waarna data in beide richtingen kan stromen.

## Toepassing

Een microcontroller leest via I2C periodiek data van een temperatuursensor en configureert tegelijk een tweede peripheral op dezelfde bus via een ander adres.

## Formeel

- Lijnen: `SCL` (clock), `SDA` (data), met pull-up weerstanden.
- Transacties: startconditie, 7/10-bit adres, read/write bit, data bytes, ACK/NACK, stopconditie.
- Eigenschappen: half-duplex, multi-device bus, lagere pin-kost dan point-to-point varianten.

## Verbanden

- [[Communication Protocols]]
- [[SPI (Serial Peripheral Interface)|SPI]]
- [[IO-expander]]
- [[USART en UART]]

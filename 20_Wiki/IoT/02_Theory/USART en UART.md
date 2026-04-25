---
type: theory
domain: "iot"
parent: Internet of Things (IoT)
related:
  - I2C
  - SPI (Serial Peripheral Interface)
  - MQTT
theme: "embedded-communication"
aliases:
  - USART en UART
  - UART
  - USART
---

# USART en UART
#concept #iot #embedded #communication


USART en UART beschrijven asynchrone seriële datacommunicatie tussen systemen via transmit- en receive-lijnen.

## Korte kern

- UART communiceert asynchroon met afgesproken baudrate en frame
- USART kan daarnaast ook synchrone modus ondersteunen
- in embedded systemen is dit een standaard kanaal voor debug en device-links

## Probleem

Hoe wissel je betrouwbaar bytes uit tussen componenten met minimale bekabeling en eenvoudige hardware?

## Intuïtie

Twee toestellen spreken af aan welk tempo bits passeren en hoe elk byte verpakt is. Omdat er geen aparte kloklijn is in UART-modus, moet timing aan beide kanten goed overeenkomen.

## Toepassing

Een microcontroller stuurt meetwaarden naar een pc-terminal via TX/RX. Een tweede toepassing is commando-invoer waarbij binnenkomende bytes acties in de firmware triggeren.

## Formeel

- Basislijnen: `TX`, `RX`, optioneel `GND` gedeeld.
- Frame bevat meestal: startbit, databits, optionele parity, stopbit(ten).
- Kritische parameters: baudrate, woordlengte, parity, stopbits.
- Verwerking kan via polling, interrupt of DMA.

## Verbanden

- [[Communication Protocols]]
- [[I2C]]
- [[SPI (Serial Peripheral Interface)|SPI]]
- [[MQTT]]

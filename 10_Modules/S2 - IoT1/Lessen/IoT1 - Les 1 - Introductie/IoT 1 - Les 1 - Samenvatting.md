# IoT 1 - Les 1 - Samenvatting

Les 1 zet het kader: wat is IoT, waarom microcontrollers, met welke hardware/software we werken (Nucleo + µVision), en de basisbegrippen die je nodig hebt om te starten.

## Waarom IoT + microcontrollers?

- Microcontrollers zitten overal (huistoestellen, auto, domotica, wearables, ...).
- Als zo'n embedded systeem ook online hangt, spreken we van een IoT-device.
- Doel van dit vak: de brug slaan tussen hardware en software en van idee naar werkend prototype gaan.

## Demo's (waar we naartoe kunnen)

- IoT CO2-meter: sensor + WiFi + microcontroller + visualisatie via website (real-time grafiek).
- IoT Train: opstelling met sensoren/actuatoren en MQTT-communicatie (JS-client).
- I2C H-brug: motorsturing met MOSFET's (robot-voorbeeld).
- Mini-drone: flight controller met gyroscoop + accelerometer (schema -> PCB -> 3D-frame).
- (BLDC) motor controller: real-time monitoring/parameter-tuning via Bluetooth.

## Hardware: Nucleo-F091RC + Extension Shield (NES)

- Vives voorziet een `Nucleo-F091RC` met `STM32F091RC` (32-bit ARM Cortex-M0).
- On-board `ST-Link`: programmer + debugger op hetzelfde bord.
- Nucleo alleen heeft typisch 1 LED + 1 drukknop; daarom gebruiken we een `Nucleo Extension Shield (NES)`.
- NES bevat: 4 drukknoppen, 8 LED's, een trimmer (analoge ingang) en een 10-pin box header; compatibel met Arduino Uno R3 headers.

## Software: µVision (Keil) + basis-workflow

- Firmware schrijven we in C en bouwen/flashen/debuggen we in `µVision`.
- Installatie: via Keil website; extra demo/PDF/video + startbestanden staan op Toledo.
- Voor de demo-projectstart: download minstens `main.*`, `leds.*`, `buttons.*`, `ad.*`, `usart2.*` (C + headers).

## Wat is een microcontroller (vs microprocessor)?

- Microprocessor: sterk in rekenkracht, maar meestal niet "stand-alone" (mist o.a. ingebouwd flash/IO); typisch in pc/laptop.
- Microcontroller: heeft "alles" aan boord voor embedded toepassingen: geheugen, IO, timers, AD/DA, communicatie (UART/SPI/I2C/CAN/ethernet, ...).

## Bouwstenen in een microcontroller (conceptueel)

- CPU, oscillator/klok, bussen
- Flash/ROM (firmware-opslag) en RAM (werkgeheugen)
- Timers, interrupt controller
- IO (digitale in/uit)
- Watchdog timer

## Indelen + C datatypes (waarom `stdint.h` belangrijk is)

- Microcontrollers worden o.a. ingedeeld op architectuur, woordbreedte (8/16/32/64-bit) en instructieset (CISC/RISC).
- Wij programmeren in C; voor voorspelbare geheugengrootte gebruik je "exact-width integers" uit `stdint.h`.
- Denk in ranges:
  - 0 .. 53753 -> `uint16_t`
  - -230 .. 153 -> `int16_t`
  - 0 .. 6234547 -> `uint32_t`

## Arduino: wat is het, en waarom niet in dit vak?

- Arduino = open-source prototyping platform (bord + software), snel resultaat via bootloader/USB en veel shields.
- Nadelen als leerplatform: minder directe controle/IO, vaste vormfactor, beperkte debug-ervaring; risico dat je "te veel magie" gebruikt i.p.v. echt embedded te leren.

## Programmeertalen (embedded context)

- Assembly: heel dicht bij hardware; vooral nuttig als je exacte instructie-flow wil forceren/analyseren.
- C: standaardtaal voor embedded; compileert naar microcontroller-instructies; dit is de focus in IoT 1.
- C++: veel gebruikt in embedded, maar staat gemiddeld iets verder van de hardware (meer abstractie).

## 'Onze' STM32F091RC (waarom deze?)

- Keuzecriteria: prijs, bordruimte, snelheid, stroomverbruik, spanning, aantal IO's, interfaces, beschikbaarheid, ...; er bestaat geen "perfecte" MCU.
- STM32F091RC is een sterk instapmodel met voldoende rekenkracht.
- Belangrijkste specs (hoog niveau): Cortex-M0, 32-bit, 256KB flash, 32KB SRAM, tot 48MHz, 3V3 (met enkele 5V-tolerante IO), 12-bit ADC, meerdere timers, UART/SPI/I2C/CAN.

## Your turn (checklist)

1. Installeer µVision.
2. Maak een nieuw project zoals in de demo (Toledo video/PDF).
3. Compileer en flash naar de Nucleo via ST-Link.
4. Pas de firmware aan zodat je minstens 1 aan/uit-schakeling realiseert (bv. LED togglen met knop).

## Mini-oefening (snelle toepassing)

- Kies het kleinste gepaste type:
  - temperatuurdelta in [-40, 125]
  - teller die tot 1 000 000 kan gaan
- Ontwerp in woorden een simpele state machine voor "LED aan/uit" met 1 drukknop (denk aan: druk = toggle, niet "ingedrukt houden").

## Actieve recall (checkvragen)

1. Wanneer noem je een embedded systeem een IoT-device?
2. Geef 3 redenen waarom een microcontroller "stand-alone" kan werken en een microprocessor vaak niet.
3. Wat doet de ST-Link op het Nucleo-bord precies?
4. Waarom zijn `uint16_t`/`int16_t`/`uint32_t` handiger dan `int` in embedded code?
5. Wat zijn 2 voordelen en 2 nadelen van Arduino als leerplatform voor embedded?
6. Noem 5 bouwstenen die je in (bijna) elke microcontroller terugvindt.

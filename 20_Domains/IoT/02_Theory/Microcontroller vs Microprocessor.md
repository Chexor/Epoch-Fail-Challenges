---
type: theory
domain: "iot"
parent: Internet of Things (IoT)
related:
  - GPIO
  - ADC (Analog-to-Digital Converter)
  - Interrupt
theme: "embedded-systems"
aliases:
  - Microcontroller vs Microprocessor
---

# Microcontroller vs Microprocessor
#concept #iot #embedded

Microcontroller vs microprocessor vergelijkt twee chiptypes op integratie, gebruiksdoel en systeemeisen.

## Korte kern

- een microcontroller integreert CPU, geheugen en peripherals op een chip
- een microprocessor focust op CPU-rekenkracht en gebruikt vaker externe componenten
- de keuze hangt af van realtime vereisten, kost, energie en complexiteit

## Probleem

Wanneer kies je voor een microcontroller en wanneer voor een microprocessor in een embedded of IoT-ontwerp?

## Intuïtie

Denk aan een microcontroller als een compacte alles-in-een module voor gerichte taken, en aan een microprocessor als een krachtigere rekenkern die in een groter ecosysteem werkt met extern RAM, opslag en vaak een volwaardig besturingssysteem.

## Toepassing

Een thermostaat, sensor node of simpele motorsturing draait typisch op een microcontroller. Een systeem dat zware GUI, multitasking en complexe netwerkstacks nodig heeft, gebruikt vaker een microprocessor.

## Formeel

- **Microcontroller (MCU):** CPU + RAM + flash + I/O + timers + communicatieblokken in een geïntegreerde chip.
- **Microprocessor (MPU):** vooral CPU-kern; vereist meestal externe RAM/flash en extra peripheral chips.
- Typische verschillen:
  - MCU: laag energieverbruik, deterministischer timing, lagere BOM-kost.
  - MPU: hogere compute-capaciteit, rijkere softwarestack, hogere systeemeisen.

## Verbanden

- [[GPIO]]
- [[ADC (Analog-to-Digital Converter)]]
- [[Interrupt]]
- [[Hardware Timer]]

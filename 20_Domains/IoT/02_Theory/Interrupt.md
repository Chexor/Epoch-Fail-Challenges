---
type: theory
domain: "iot"
parent: Microcontroller vs Microprocessor
related:
  - Debouncing
  - Hardware Timer
  - Watchdog Timer
theme: "embedded-systems"
aliases:
  - Interrupt
---

# Interrupt
#concept #iot #embedded


Een interrupt onderbreekt de normale program flow zodat een systeem onmiddellijk op een gebeurtenis kan reageren.

## Korte kern

- interrupts maken event-driven gedrag mogelijk zonder continue polling
- een handler voert korte, gerichte logica uit bij een trigger
- prioriteiten regelen welke gebeurtenis eerst bediend wordt

## Probleem

Hoe reageer je snel op asynchrone events zonder CPU-tijd te verspillen aan constante controles?

## Intuïtie

In plaats van de hele tijd te vragen "is er iets gebeurd?", laat je hardware zelf een seintje geven wanneer actie nodig is. De CPU springt dan tijdelijk naar een service routine en keert nadien terug.

## Toepassing

Bij een knopdruk, timer-overflow of inkomend seriëel byte kan een interrupt direct de relevante routine starten, waardoor latency laag blijft en de hoofdlus eenvoudiger wordt.

## Formeel

- Triggerbron zet een interrupt pending.
- Interrupt controller beslist op basis van masking en prioriteit.
- CPU voert een ISR/handler uit.
- ISR wist flags en beëindigt correct zodat normale flow verder kan.

## Verbanden

- [[Microcontroller vs Microprocessor]]
- [[Debouncing]]
- [[Hardware Timer]]
- [[Watchdog Timer]]

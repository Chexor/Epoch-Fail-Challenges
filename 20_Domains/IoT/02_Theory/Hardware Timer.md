---
type: theory
domain: "iot"
parent: Microcontroller vs Microprocessor
related:
  - Interrupt
  - ADC (Analog-to-Digital Converter)
  - Watchdog Timer
theme: "embedded-systems"
aliases:
  - Hardware Timer
  - Timer (PSC, ARR, CNT)
---

# Hardware Timer
#concept #iot #embedded


Een hardware timer is een perifere teller die op basis van klokpulsen nauwkeurige tijdsintervallen en events genereert.

## Korte kern

- timers leveren precieze timing zonder blocking delays
- `PSC`, `ARR` en `CNT` bepalen periode en frequentie
- timer-events kunnen polling vervangen via interrupts

## Probleem

Hoe maak je betrouwbare timing in embedded software zonder CPU te blokkeren met wachtlussen?

## Intuïtie

Een timer telt autonoom op de achtergrond. Door de telling slim te schalen en begrenzen laat je hardware op vaste momenten een event geven, terwijl de CPU andere taken doet.

## Toepassing

Voor periodiek LED-toggle, sampling of regel-lussen configureer je de timer op een vaste updatefrequentie en laat je bij elke update een ISR uitvoeren.

## Formeel

- **PSC (prescaler):** deelt timerklok.
- **ARR (auto-reload):** topwaarde waarop teller reset.
- **CNT (counter):** actuele telwaarde.
- Typische relatie: `f_timer = f_clk / ((PSC + 1) * (ARR + 1))`.

## Verbanden

- [[Microcontroller vs Microprocessor]]
- [[Interrupt]]
- [[ADC (Analog-to-Digital Converter)]]
- [[Watchdog Timer]]

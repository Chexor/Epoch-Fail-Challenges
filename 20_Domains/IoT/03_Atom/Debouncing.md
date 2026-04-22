---
type: atom
domain: "iot"
parent: Interrupt
related:
  - GPIO
  - Hardware Timer
  - Interrupt
theme: "embedded-systems"
aliases:
  - Debouncing
  - Debounce
---

# Debouncing
#concept #iot #embedded


Debouncing is het onderdrukken van snelle ongewenste schakelpulsen door mechanische contactdender bij knoppen of schakelaars.

## Korte kern

- voorkomt dat één fysieke druk als meerdere events gelezen wordt
- kan in software (tijdvenster/filter) of hardware uitgevoerd worden
- is essentieel voor betrouwbare inputdetectie

## Probleem

Hoe vermijd je foutieve meervoudige detectie bij één enkele knopactie?

## Intuïtie

Een mechanisch contact stuitert kort bij omschakeling. Zonder debounce ziet de software meerdere snelle flanken in plaats van één intentievolle druk.

## Toepassing

Na de eerste geldige flank negeert de firmware gedurende een korte debounce-tijd bijkomende flanken en accepteert pas daarna een nieuwe input.

## Formeel

- Contactbounce veroorzaakt een reeks korte puls-overgangen.
- Debounce-strategieën:
  - vaste lockout-tijd
  - sample-based stabiliteitscontrole
  - RC + Schmitt-trigger in hardware

## Verbanden

- [[Interrupt]]
- [[GPIO]]
- [[Hardware Timer]]

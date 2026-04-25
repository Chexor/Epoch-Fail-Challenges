---
type: theory
domain: "iot"
parent: Microcontroller vs Microprocessor
related:
  - ADC (Analog-to-Digital Converter)
  - Interrupt
  - IO-expander
theme: "embedded-systems"
aliases:
  - GPIO
  - General Purpose Input/Output
---

# GPIO
#concept #iot #embedded


GPIO zijn programmeerbare digitale pinnen waarmee een systeem externe signalen kan lezen of sturen.

## Korte kern

- elke GPIO-pin kan meestal als input of output werken
- GPIO vormt de basislaag voor knop-, led- en signaalinteractie
- pinmodus en gedrag worden bepaald via hardware-registers

## Probleem

Hoe laat je software veilig en controleerbaar communiceren met fysieke digitale signalen?

## Intuïtie

GPIO is de standaard "contactdoos" tussen code en hardware: als input lees je toestand van buitenaf, als output stuur je actief een logische waarde naar een component.

## Toepassing

Een knop wordt via input-pin ingelezen; een led wordt via output-pin aangestuurd. Met meerdere GPIO-lijnen kan je ook componenten selecteren of eenvoudige protocollen opbouwen.

## Formeel

- **Input mode:** pin leest extern logisch niveau.
- **Output mode:** pin forceert logisch niveau naar buiten.
- Veelgebruikte configuraties:
  - pull-up/pull-down
  - push-pull/open-drain
  - alternate function voor perifere modules

## Verbanden

- [[Microcontroller vs Microprocessor]]
- [[ADC (Analog-to-Digital Converter)]]
- [[Interrupt]]
- [[IO-expander]]

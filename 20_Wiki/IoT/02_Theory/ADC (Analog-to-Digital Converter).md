---
type: theory
domain: "iot"
parent: Microcontroller vs Microprocessor
related:
  - GPIO
  - Hardware Timer
  - Data Representation
theme: "embedded-systems"
aliases:
  - ADC (Analog-to-Digital Converter)
  - ADC
---

# ADC (Analog-to-Digital Converter)
#concept #iot #embedded


Een ADC zet een analoge spanning om naar een digitale waarde zodat software die meetinformatie kan verwerken.

## Korte kern

- ADC maakt de brug tussen continue signalen en digitale verwerking
- resolutie bepaalt het aantal mogelijke outputniveaus
- sampling en referentiespanning bepalen mee de meetkwaliteit

## Probleem

Hoe vertaal je een analoog sensorsignaal naar een bruikbare discrete waarde voor softwarelogica?

## Intuïtie

De ADC neemt snapshots van een spanning en geeft per snapshot een getal terug binnen een vast bereik. Hoe fijner dat bereik is, hoe nauwkeuriger je kleine verschillen kan onderscheiden.

## Toepassing

Een potentiometer of temperatuursensor levert een spanning. De ADC converteert die naar bijvoorbeeld een 12-bit waarde (0-4095) die je kan tonen, filteren of gebruiken in regelalgoritmes.

## Formeel

- Kernparameters:
  - **Resolutie:** `N` bits, met `2^N` niveaus
  - **Referentiespanning:** bepaalt omzettingsbereik
  - **Sampling:** tempo waarop metingen gebeuren
- Voor 12-bit ADC geldt typisch: `digitale_waarde in [0, 4095]`.

## Verbanden

- [[Microcontroller vs Microprocessor]]
- [[GPIO]]
- [[Hardware Timer]]
- [[Data Representation]]

# Labo 7 - Overzicht

## Oefeningen
- [[Labo7_ex03-01]] - vaste kleur op APA102C/NS107S LED-strip.
- [[Labo7_ex03-02]] - state machine spoorwegovergang op LED-strip.
- [[Labo7_ex03-03]] - looplicht met kleurkeuze via AD-converter.

## Concepten in dit labo
- SPI1 initialiseren met `InitSpi1()`.
- Addressable LEDs aansturen met `UpdateAPA102CLeds(...)`.
- Werken met `APA102C` struct (`brightness`, `red`, `green`, `blue`).
- Mapping van logica naar specifieke LED-posities op de strip.
- AD-converter uitlezen met `GetAdValue()`.
- ADC-bereik opdelen in kleurzones.

## Kernidee
In dit labo verschuift de focus van gewone board-LEDs naar een addressable RGB-strip.
Je gebruikt SPI om kleuren te sturen en combineert dat met state machines en analoge input.

## Kort codevoorbeeld
```c
adValue = GetAdValue();
colorIndex = (uint8_t)((adValue * 8U) / 4096U);
```

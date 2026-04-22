# Labo 2 - Overzicht

## Oefeningen
- [[Labo2_ex01-05]] - looplicht van LED1 naar LED8 en terug.
- [[Labo2_ex01-06]] - leds rechtstreeks sturen met vier knoppen.
- [[Labo2_ex01-07]] - toggelen per druk met wachten tot loslaten.
- [[Labo2_ex01-08]] - ADC-waarde op leds tonen.

## Concepten in dit labo
- Bewegende LED-patronen en looplichten.
- Polling van knoppen voor directe bediening.
- Wachten tot een knop losgelaten is om 1 actie per druk te krijgen.
- `GetAdValue()` gebruiken om de potentiometer te meten.
- Een 12-bit ADC-waarde schalen naar 8 leds.
- Verschil tussen een ruwe binaire voorstelling en een gebruiksvriendelijke weergave.

## Kernidee
Dit labo verbindt eenvoudige LED-logica met echte invoer van knoppen en potentiometer.

## Kort codevoorbeeld
```c
while (1)
{
    uint8_t ledValue = (uint8_t)(GetAdValue() >> 4);
    ByteToLeds(ledValue);
    WaitForMs(50);
}
```

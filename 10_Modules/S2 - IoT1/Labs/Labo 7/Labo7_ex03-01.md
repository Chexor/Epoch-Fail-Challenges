# Labo7 ex03-01

## Opgave
Gebruik een stukje addressable LED-strip (minstens 5 LEDs) en zet alle LEDs op een zelfgekozen kleur met de bestaande SPI/APA102C-bibliotheken.

## Oplossing
- `spi1.c/.h` en `apa102c.c/.h` toevoegen aan het project.
- `NUMBER_OF_APA102C_LEDS` op `5` zetten.
- `InitSpi1()` oproepen.
- Alle LEDs in een lus dezelfde RGB-waarde geven.
- Eenmalig `UpdateAPA102CLeds(leds);` sturen.

## Codevoorbeeld
```c
for(i = 0; i < NUMBER_OF_APA102C_LEDS; i++)
{
    leds[i].brightness = DEFAULT_LED_BRIGHTNESS;
    leds[i].red = LED_R;
    leds[i].green = LED_G;
    leds[i].blue = LED_B;
}

UpdateAPA102CLeds(leds);
```

## Korte uitleg
Je configureert SPI1, vult voor elke LED dezelfde kleur in, en stuurt het volledige frame naar de strip.
Kleur wijzigen doe je enkel door RGB-waarden aan te passen en opnieuw te builden/flashes.

## Concepten uit Labo 7
- SPI1 basis
- APA102C frame-update
- RGB-kleurinstelling
- vaste kleur op volledige strip

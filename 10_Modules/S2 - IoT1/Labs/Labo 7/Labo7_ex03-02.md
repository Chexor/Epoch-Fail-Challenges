# Labo7 ex03-02

## Opgave
Hermaak de state machine van de spoorwegovergang, maar toon de lampen op de addressable LED-strip.

## Oplossing
- Start van de bestaande "State Machine Railway" oplossing.
- Vervang `ByteToLeds(...)`-uitgangen door stripaansturing.
- Gebruik 5-LED mapping:
  - `LED 0` = rode lamp links
  - `LED 2` = witte lamp midden
  - `LED 4` = rode lamp rechts
- Hou states identiek: `idle`, `white`, `redOne`, `redTwo`.

## Codevoorbeeld
```c
case white:
    for(i = 0; i < NUMBER_OF_APA102C_LEDS; i++)
    {
        stripLeds[i].red = 0;
        stripLeds[i].green = 0;
        stripLeds[i].blue = 0;
    }
    stripLeds[2].red = 255;
    stripLeds[2].green = 255;
    stripLeds[2].blue = 255;
    UpdateAPA102CLeds(stripLeds);
    break;
```

## Korte uitleg
De state machine blijft hetzelfde, alleen de fysieke output verandert.
Elke state zet eerst de strip leeg en activeert daarna de juiste LED(s) voor die toestand.

## Concepten uit Labo 7
- state machine behouden
- output-mapping naar stripindices
- rood/wit-railwaypatroon
- SW1/SW4 gedrag behouden

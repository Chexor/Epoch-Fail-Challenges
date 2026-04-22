# Labo7 ex03-03

## Opgave
Maak een looplicht op de addressable LED-strip en kies de kleur via de AD-converter over het volledige trimmerbereik.

## Oplossing
- Lees de trimmer met `GetAdValue()` (0..4095).
- Deel het bereik in 8 gelijke zones.
- Koppel elke zone aan een kleur:
  - 0: uit
  - 1: rood
  - 2: groen
  - 3: blauw
  - 4: cyaan
  - 5: magenta
  - 6: geel
  - 7: wit
- Laat telkens 1 LED actief zijn en schuif de positie door voor het looplicht.

## Codevoorbeeld
```c
adValue = GetAdValue();
colorIndex = (uint8_t)((adValue * 8U) / 4096U);

switch(colorIndex)
{
    case 0: red = 0;   green = 0;   blue = 0;   break;
    case 1: red = 255; green = 0;   blue = 0;   break;
    case 2: red = 0;   green = 255; blue = 0;   break;
    case 3: red = 0;   green = 0;   blue = 255; break;
    case 4: red = 0;   green = 255; blue = 255; break;
    case 5: red = 255; green = 0;   blue = 255; break;
    case 6: red = 255; green = 255; blue = 0;   break;
    default:red = 255; green = 255; blue = 255; break;
}
```

## Korte uitleg
Door de ADC-waarde in zones te verdelen, doorloop je netjes alle gevraagde kleuren.
Tegenwijzerzin (lage ADC-waarden) geeft `uit`; wijzerzin evolueert richting `wit`.

## Concepten uit Labo 7
- ADC uitlezen
- bereikkwantisatie
- kleurkeuze op basis van analoge input
- looplicht op RGB-strip

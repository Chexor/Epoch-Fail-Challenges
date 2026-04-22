# Labo3 ex01-10

## Opgave
Maak een bargraph van de ADC-waarde en hou de piekwaarde nog even zichtbaar.

## Oplossing
- Zet de ADC-waarde om naar een niveau van `0` tot `8`.
- Bouw een bargraph op met meerdere actieve leds.
- Bewaar ook een piekniveau en het tijdstip ervan.
- Laat de piek pas na ongeveer `1 s` terug zakken.

## Codevoorbeeld
```c
uint8_t level = (uint8_t)((GetAdValue() * 9U) / 4096U);

if (level > peakLevel)
{
    peakLevel = level;
    peakTick = ticks;
}

if ((ticks - peakTick) > 1000)
{
    peakLevel = level;
}

ByteToLeds(barPattern[level] | peakPattern[peakLevel]);
```

## Korte uitleg
De bargraph toont het actuele niveau, terwijl de piek nog even blijft staan. Daardoor lijkt de weergave op een eenvoudige VU-meter.

## Concepten uit Labo 3
- bargraph
- peak-hold
- tijdstempel met `ticks`
- samengestelde LED-weergave

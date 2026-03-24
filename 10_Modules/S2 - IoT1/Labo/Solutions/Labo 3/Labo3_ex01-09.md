# Labo3 ex01-09

## Opgave
Zet de potentiometerstand om naar een positie-indicator op de leds.

## Oplossing
- Lees en schaal de ADC-waarde naar 8 bit.
- Zet alle leds uit bij waarde `0`.
- Zet `LED8` aan bij waarde `255`.
- Verdeel de tussenwaarden over `LED1` tot `LED7`.

## Codevoorbeeld
```c
uint8_t adcValue8 = (uint8_t)(GetAdValue() >> 4);
uint8_t ledPattern = 0;

if (adcValue8 == 0)
{
    ledPattern = 0x00;
}
else if (adcValue8 == 255)
{
    ledPattern = 0x80;
}
else
{
    uint8_t ledIndex = (adcValue8 - 1) / 36;
    ledPattern = (1 << ledIndex);
}

ByteToLeds(ledPattern);
```

## Korte uitleg
De code deelt het ADC-bereik op in zones en koppelt elke zone aan precies 1 led. Zo krijg je een positie-indicator in plaats van een ruwe binaire weergave.

## Concepten uit Labo 3
- zone-indeling
- niveauweergave
- ADC-schaal
- enkel actieve led

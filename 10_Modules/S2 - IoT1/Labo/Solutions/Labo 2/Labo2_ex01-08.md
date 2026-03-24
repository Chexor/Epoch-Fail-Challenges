# Labo2 ex01-08

## Opgave
Lees de potentiometer via de ADC en toon de gemeten waarde op de leds.

## Oplossing
- Lees de ADC-waarde met `GetAdValue()`.
- Schaal van 12 bit naar 8 bit met `>> 4`.
- Toon die 8-bit waarde met `ByteToLeds(...)`.
- Stuur ook debugtekst via `printf`.

## Codevoorbeeld
```c
while (1)
{
    uint16_t adcValue = GetAdValue();
    uint8_t ledValue = (uint8_t)(adcValue >> 4);

    ByteToLeds(ledValue);
    printf("ADC: %u\r\n", adcValue);
    WaitForMs(50);
}
```

## Korte uitleg
De ADC levert een waarde tussen `0` en `4095`. Door die te verkleinen naar 8 bit kan je ze rechtstreeks op de 8 leds afbeelden.

## Concepten uit Labo 2
- ADC
- potentiometer
- schalen van 12 bit naar 8 bit
- seriele debug

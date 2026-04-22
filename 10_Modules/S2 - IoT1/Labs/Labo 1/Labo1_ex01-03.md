# Labo1 ex01-03

## Opgave
Toon een oplopende 8-bit teller op de leds.

## Oplossing
- Bewaar de teller in een `uint8_t`.
- Stuur de teller naar de leds met `ByteToLeds(count)`.
- Verhoog de teller met `count++`.
- Wacht `100 ms` tussen twee stappen.

## Codevoorbeeld
```c
uint8_t count = 0;

while (1)
{
    ByteToLeds(count);
    count++;
    WaitForMs(100);
}
```

## Korte uitleg
Elke tellerwaarde wordt als bitpatroon op de 8 leds gezet, zodat je de binaire teller direct ziet.

## Concepten uit Labo 1
- `uint8_t`
- binaire teller
- `ByteToLeds(...)`
- periodieke update

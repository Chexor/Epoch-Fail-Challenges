# Labo2 ex01-06

## Opgave
Gebruik vier knoppen om LED1 en LED8 rechtstreeks aan en uit te zetten.

## Oplossing
- Poll alle knoppen continu.
- `SW1` zet `LED1` aan.
- `SW2` zet `LED1` uit.
- `SW3` zet `LED8` aan en `SW4` zet `LED8` uit.

## Codevoorbeeld
```c
while (1)
{
    if (SW1Active()) SetLed(1);
    if (SW2Active()) ClearLed(1);
    if (SW3Active()) SetLed(8);
    if (SW4Active()) ClearLed(8);
}
```

## Korte uitleg
Elke knop is gekoppeld aan een vaste actie. Daardoor reageert de ledtoestand onmiddellijk op de ingedrukte knop.

## Concepten uit Labo 2
- directe besturing
- polling
- `SetLed(...)`
- `ClearLed(...)`

# Labo2 ex01-05

## Opgave
Maak een looplicht dat van LED1 naar LED8 loopt en daarna terugkeert.

## Oplossing
- Gebruik een lus van links naar rechts.
- Gebruik daarna een lus van rechts naar links.
- Zet per stap telkens een enkel LED-patroon.
- Wacht `100 ms` per stap.

## Codevoorbeeld
```c
while (1)
{
    for (int i = 0; i < 8; i++)
    {
        ByteToLeds(1 << i);
        WaitForMs(100);
    }

    for (int i = 6; i > 0; i--)
    {
        ByteToLeds(1 << i);
        WaitForMs(100);
    }
}
```

## Korte uitleg
Omdat er telkens maar 1 bit actief is en dat bit opschuift, zie je een lopend licht over de 8 leds.

## Concepten uit Labo 2
- looplicht
- `for`-lus
- bitpatroon
- richting

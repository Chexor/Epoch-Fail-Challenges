# Labo1 ex01-04

## Opgave
Toon opnieuw een 8-bit teller, maar laat de snelheid afhangen van de drukknoppen.

## Oplossing
- Poll `SW1` tot `SW4` in de hoofdlus.
- Kies op basis van de knop een wachttijd van `400`, `200`, `100` of `10 ms`.
- Toon de huidige tellerwaarde met `ByteToLeds(count)`.
- Verhoog de teller na elke stap.

## Codevoorbeeld
```c
while (1)
{
    if (SW1Active())
    {
        ByteToLeds(count);
        count++;
        WaitForMs(400);
    }
    else if (SW2Active())
    {
        ByteToLeds(count);
        count++;
        WaitForMs(200);
    }
    else if (SW3Active())
    {
        ByteToLeds(count);
        count++;
        WaitForMs(100);
    }
    else if (SW4Active())
    {
        ByteToLeds(count);
        count++;
        WaitForMs(10);
    }
}
```

## Korte uitleg
De actieve knop bepaalt hoe lang het programma wacht tussen twee tellerstappen. Zonder knop blijft de laatste tellerwaarde staan.

## Concepten uit Labo 1
- polling
- `if` en `else if`
- variabele snelheid
- knopinvoer

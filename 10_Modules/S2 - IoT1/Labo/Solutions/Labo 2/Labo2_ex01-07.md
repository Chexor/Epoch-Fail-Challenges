# Labo2 ex01-07

## Opgave
Laat SW1 LED1 toggelen en SW4 LED8 toggelen, maar slechts 1 keer per druk.

## Oplossing
- Detecteer of een knop actief is.
- Wacht in een lus tot die knop terug losgelaten is.
- Toggle daarna de bijhorende led.
- Voeg nog een korte wachttijd toe.

## Codevoorbeeld
```c
while (1)
{
    if (SW1Active())
    {
        while (SW1Active());
        ToggleLed(1);
        WaitForMs(50);
    }

    if (SW4Active())
    {
        while (SW4Active());
        ToggleLed(8);
        WaitForMs(50);
    }
}
```

## Korte uitleg
Door pas na het loslaten te toggelen, vermijd je dat 1 lange druk meerdere toggles veroorzaakt.

## Concepten uit Labo 2
- toggelen
- wachten tot loslaten
- eenvoudige debounce-aanpak
- knoplogica

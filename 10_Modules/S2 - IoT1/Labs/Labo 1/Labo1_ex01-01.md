# Labo1 ex01-01

## Opgave
Laat LED1 blijven knipperen met een zichtbare periode.

## Oplossing
- Initialiseer klok, leds en SysTick.
- Toggle `LED1` in de hoofdlus.
- Wacht telkens `500 ms` met `WaitForMs(500)`.

## Codevoorbeeld
```c
while (1)
{
    ToggleLed(1);
    WaitForMs(500);
}
```

## Korte uitleg
Door LED1 elke 500 ms om te schakelen, krijg je een volledige aan/uit-cyclus van ongeveer 1 seconde.

## Concepten uit Labo 1
- `while(1)`
- `SysTick`
- blocking delay
- LED-output

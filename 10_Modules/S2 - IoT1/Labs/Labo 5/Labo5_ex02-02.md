# Labo5 ex02-02

## Opgave
Verstuur elke 5 seconden de tekst `IoT Devices` naar de pc.

## Oplossing
- Initialiseer `USART2`.
- Verstuur `IoT Devices\r\n`.
- Wacht `5000 ms`.
- Herhaal dit in een oneindige lus.

## Codevoorbeeld
```c
while (1)
{
    StringToUsart2("IoT Devices\r\n");
    WaitForMs(5000);
}
```

## Korte uitleg
De hoofdlus stuurt steeds dezelfde tekst door en wacht dan 5 seconden. Daardoor verschijnt periodiek dezelfde regel in de terminal.

## Concepten uit Labo 5
- string versturen
- `\r\n`
- periodieke output
- seriele terminal

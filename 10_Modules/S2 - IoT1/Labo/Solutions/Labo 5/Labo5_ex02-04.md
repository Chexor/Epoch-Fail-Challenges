# Labo5 ex02-04

## Opgave
Stuur de interne tijd sinds het opstarten in milliseconden naar de pc.

## Oplossing
- Lees `ticks` uit in de hoofdlus.
- Formatteer de waarde als tekst, bijvoorbeeld `1234 ms`.
- Verstuur die tekst via `USART2`.
- Wacht ongeveer `1 s` tussen twee berichten.

## Codevoorbeeld
```c
while (1)
{
    sprintf(buffer, "%u ms\r\n", (unsigned int)ticks);
    StringToUsart2(buffer);
    WaitForMs(1000);
}
```

## Korte uitleg
Omdat `ticks` elke milliseconde verhoogt, vormt die variabele een eenvoudige uptime-teller die je rechtstreeks kan rapporteren.

## Concepten uit Labo 5
- `ticks`
- SysTick-tijdsbasis
- formatteren van integers
- periodieke rapportering

# Labo6 ex02-05

## Opgave
Ontvang een byte via polling, toon die op de leds en stuur nuttige info terug naar de pc.

## Oplossing
- Zet de receiver aan met `RE`.
- Poll op `USART_ISR_RXNE`.
- Lees de byte uit `USART2->RDR`.
- Toon de byte op de leds en stuur `CHAR`, `ASCII` en `BIN` terug.

## Codevoorbeeld
```c
if ((USART2->ISR & USART_ISR_RXNE) == USART_ISR_RXNE)
{
    rx.ascii = (uint8_t)USART2->RDR;
    ByteToLeds(rx.ascii);
    sprintf(rx.bericht, "CHAR: %c ASCII: %u\r\n", rx.ascii, rx.ascii);
    StringToUsart2(rx.bericht);
}
```

## Korte uitleg
`RXNE` meldt dat er een ontvangen byte klaarstaat. Zodra die gelezen is, kan de code dezelfde informatie zowel op leds als in seriele tekst tonen.

## Concepten uit Labo 6
- USART2 ontvangen
- polling
- `RXNE`
- `RDR`

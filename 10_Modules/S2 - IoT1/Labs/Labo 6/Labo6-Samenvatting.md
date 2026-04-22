# Labo 6 - Overzicht

## Oefeningen
- [[Labo6_ex02-05]] - byte ontvangen via polling.
- [[Labo6_ex02-06]] - byte ontvangen via interrupt.
- [[Labo6_ex02-07]] - seriele `S` start een looplicht.
- [[Labo6_ex02-08]] - `S` start en `P` stopt het looplicht.

## Concepten in dit labo
- USART2 receiver activeren met `RE`.
- Ontvangst pollen via `RXNE` of afhandelen via `RXNEIE`.
- Bytes uitlezen uit `USART2->RDR`.
- Verschil tussen polling en interrupts bij seriele ontvangst.
- Seriele data interpreteren als commando.
- `volatile` gebruiken voor gedeelde toestand tussen main en ISR.

## Kernidee
Dit labo toont hoe ontvangen seriele data niet alleen informatie kan zijn, maar ook het gedrag van het programma kan sturen.

## Kort codevoorbeeld
```c
void USART2_IRQHandler(void)
{
    uint8_t data = (uint8_t)USART2->RDR;
    if (data == 'S') gestart = true;
    if (data == 'P') gestart = false;
}
```

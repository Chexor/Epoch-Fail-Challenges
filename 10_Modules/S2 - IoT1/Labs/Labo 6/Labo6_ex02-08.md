# Labo6 ex02-08

## Opgave
Breid ex02-07 uit zodat `S` het looplicht start en `P` het stopt.

## Oplossing
- Verwerk ontvangen bytes in de USART-interrupt.
- Zet `gestart = true` bij `S`.
- Zet `gestart = false` bij `P`.
- Laat de hoofdlus het looplicht alleen uitvoeren wanneer `gestart` waar is.

## Codevoorbeeld
```c
void USART2_IRQHandler(void)
{
    uint8_t data = (uint8_t)USART2->RDR;

    if (data == 'S') gestart = true;
    if (data == 'P') gestart = false;
}

while (1)
{
    if (gestart)
    {
        ByteToLeds(1 << i);
        WaitForMs(100);
    }
}
```

## Korte uitleg
De seriele poort stuurt hier niet alleen data door, maar bestuurt rechtstreeks de toestand van het programma met eenvoudige commando's.

## Concepten uit Labo 6
- start/stop via commando
- `volatile` toestand
- seriele protocolbasis
- looplicht aansturen

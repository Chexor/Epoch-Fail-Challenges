# Labo6 ex02-07

## Opgave
Gebruik een ontvangen seriele byte als commando: `S` moet een looplicht starten.

## Oplossing
- Lees de byte in de USART-interrupt.
- Zet `gestart = true` wanneer de byte `S` is.
- Laat de hoofdlus alleen dan het looplicht uitvoeren.
- Stuur een bevestiging terug naar de pc.

## Codevoorbeeld
```c
void USART2_IRQHandler(void)
{
    if ((uint8_t)USART2->RDR == 'S')
    {
        gestart = true;
        StringToUsart2("Start\r\n");
    }
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
De interrupt beslist enkel of het systeem gestart is. De hoofdlus voert daarna het eigenlijke looplicht uit zolang die toestand actief blijft.

## Concepten uit Labo 6
- commandoherkenning
- toestandsvlag
- ISR + hoofdloop samenwerken
- seriele besturing

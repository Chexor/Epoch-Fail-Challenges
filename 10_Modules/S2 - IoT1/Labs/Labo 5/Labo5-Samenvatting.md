# Labo 5 - Overzicht

## Oefeningen
- [[Labo5_ex02-01]] - karakter versturen bij knopdruk.
- [[Labo5_ex02-02]] - periodiek tekst versturen.
- [[Labo5_ex02-03]] - potmeterspanning via USART2 rapporteren.
- [[Labo5_ex02-04]] - uptime in milliseconden versturen.

## Concepten in dit labo
- USART2 initialiseren op `9600 baud`.
- Een byte of string via de seriele poort verzenden.
- `\r\n` gebruiken voor nette terminaloutput.
- Flankdetectie om 1 actie per knopdruk te krijgen.
- `sprintf(...)` gebruiken om meetwaarden te formatteren.
- ADC- en tijdsgegevens leesbaar naar de pc sturen.

## Kernidee
Dit labo maakt de stap van lokale LED-weergave naar communicatie met een pc via USART2.

## Kort codevoorbeeld
```c
sprintf(buffer, "%u ms\r\n", (unsigned int)ticks);
StringToUsart2(buffer);
```

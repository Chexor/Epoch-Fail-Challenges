# Labo5 ex02-01

## Opgave
Verstuur de letter `V` via `USART2` wanneer SW2 net ingedrukt wordt.

## Oplossing
- Bewaar de huidige en vorige toestand van SW2.
- Detecteer de flank `niet ingedrukt -> ingedrukt`.
- Verstuur `V` met `StringToUsart2("V")`.
- Herhaal dit in de hoofdlus.

## Codevoorbeeld
```c
bool current = SW2Active();

if (current && !previous)
{
    StringToUsart2("V");
}

previous = current;
```

## Korte uitleg
Flankdetectie zorgt ervoor dat je per druk maar 1 verzending krijgt, ook als de knop langer ingedrukt blijft.

## Concepten uit Labo 5
- USART2 zenden
- flankdetectie
- knoptoestand onthouden
- ASCII-karakter verzenden

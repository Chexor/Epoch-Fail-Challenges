# Labo3 ex01-12

## Opgave
Gebruik een knopinterrupt om een teller te verhogen en toon die teller op de leds.

## Oplossing
- Laat `InitButtons()` de interrupt op SW1 instellen.
- Verhoog `count` in `EXTI0_1_IRQHandler()`.
- Toon in de hoofdlus constant `ByteToLeds(count)`.
- Gebruik een `uint8_t` zodat de teller vanzelf rondloopt.

## Codevoorbeeld
```c
void EXTI0_1_IRQHandler(void)
{
    EXTI->PR = EXTI_PR_PR1;
    count++;
}

while (1)
{
    ByteToLeds(count);
}
```

## Korte uitleg
Elke interrupt verhoogt de teller met 1. De hoofdlus leest die teller uit en zet hem als bitpatroon op de leds.

## Concepten uit Labo 3
- knopinterrupt
- teller in ISR
- hoofdloop als weergave
- dender zichtbaar maken

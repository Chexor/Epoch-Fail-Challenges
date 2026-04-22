# Labo 3 - Overzicht

## Oefeningen
- [[Labo3_ex01-09]] - ADC omzetten naar een positie op de leds.
- [[Labo3_ex01-10]] - bargraph met piekgeheugen.
- [[Labo3_ex01-11]] - teller stoppen via EXTI-interrupt.
- [[Labo3_ex01-12]] - knopdrukken tellen via interrupt.

## Concepten in dit labo
- ADC-waarden omzetten naar niveaus of zones.
- Bargraph-weergave en peak-hold.
- EXTI-interrupts op knopdrukken.
- Pending flags correct wissen in een handler.
- `volatile` voor variabelen die in main en interrupt gebruikt worden.
- Verschil tussen polling en event-driven werken.
- Dender als praktisch probleem bij mechanische knoppen.

## Kernidee
Dit labo verschuift van gewone polling naar reageren op hardwaregebeurtenissen met interrupts.

## Kort codevoorbeeld
```c
void EXTI0_1_IRQHandler(void)
{
    EXTI->PR = EXTI_PR_PR1;
    count++;
}
```

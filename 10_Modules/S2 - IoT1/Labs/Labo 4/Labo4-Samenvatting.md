# Labo 4 - Overzicht

## Oefeningen
- [[Labo4_ex01-13]] - twee knoppen via interrupt.
- [[Labo4_ex01-14]] - LED1 periodiek toggelen met Timer7.
- [[Labo4_ex01-15]] - reactietijd meten met timerinterrupts.
- [[Labo4_ex01-16]] - blokgolf maken op een GPIO-pin.

## Concepten in dit labo
- EXTI op meerdere lijnen configureren.
- Timer7 instellen met `PSC` en `ARR`.
- Periodieke interrupts gebruiken in plaats van software delays.
- Tijdsmetingen opbouwen met vaste interruptstappen.
- Reactietijd meten met start- en stoplogica.
- Een uitgangspin periodiek toggelen voor een blokgolf.

## Kernidee
Dit labo toont hoe timers zorgen voor stabiele, herhaalbare timing in embedded systemen.

## Kort codevoorbeeld
```c
void TIM7_IRQHandler(void)
{
    TIM7->SR &= ~TIM_SR_UIF;
    ToggleLed(1);
}
```

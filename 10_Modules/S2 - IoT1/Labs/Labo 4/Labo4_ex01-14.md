# Labo4 ex01-14

## Opgave
Laat LED1 automatisch toggelen om de `0,5 s` met Timer7.

## Oplossing
- Schakel de klok van `TIM7` in.
- Kies `PSC` zodat de timer op `1 ms` telt.
- Zet `ARR` op `499`.
- Toggle `LED1` in de timerinterrupt.

## Codevoorbeeld
```c
TIM7->PSC = 47999;
TIM7->ARR = 499;
TIM7->DIER |= TIM_DIER_UIE;
TIM7->CR1 |= TIM_CR1_CEN;

void TIM7_IRQHandler(void)
{
    TIM7->SR &= ~TIM_SR_UIF;
    ToggleLed(1);
}
```

## Korte uitleg
Na 500 timerstappen ontstaat een update-interrupt. In die handler wordt LED1 omgeschakeld, dus knippert hij stabiel met een halve seconde per toggle.

## Concepten uit Labo 4
- `TIM7`
- `PSC`
- `ARR`
- periodieke interrupt

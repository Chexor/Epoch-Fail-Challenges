# Labo4 ex01-15

## Opgave
Maak een reactietijdmeter die start na een willekeurige wachttijd en stopt bij een tweede knop.

## Oplossing
- Start de meting met `SW1`.
- Wacht eerst een pseudo-willekeurige tijd.
- Laat Timer7 elke `20 ms` een teller verhogen.
- Stop de teller met `SW2` en toon de waarde op de leds.

## Codevoorbeeld
```c
if (SW1Active())
{
    WaitForMs(randomDelay);
    count = 0;
    meten = true;
    TIM7->CR1 |= TIM_CR1_CEN;
}

void TIM7_IRQHandler(void)
{
    TIM7->SR &= ~TIM_SR_UIF;
    if (meten)
    {
        count++;
    }
}
```

## Korte uitleg
De timer levert vaste tijdsstappen. Door bij elke interrupt de teller te verhogen, meet je reactietijd in blokjes van 20 ms.

## Concepten uit Labo 4
- reactietijdmeting
- timer als tijdsbasis
- start/stop-toestand
- pseudo-random delay

# Labo4 ex01-13

## Opgave
Gebruik twee knopinterrupts: SW1 moet alle leds aanzetten en SW2 moet alle leds uitzetten.

## Oplossing
- Configureer EXTI voor `PA1` en `PA4`.
- Activeer falling-edge detectie.
- Schakel de juiste NVIC-interrupts in.
- Zet in de handlers `ByteToLeds(255)` of `ByteToLeds(0)`.

## Codevoorbeeld
```c
void EXTI0_1_IRQHandler(void)
{
    EXTI->PR = EXTI_PR_PR1;
    ByteToLeds(255);
}

void EXTI4_15_IRQHandler(void)
{
    EXTI->PR = EXTI_PR_PR4;
    ByteToLeds(0);
}
```

## Korte uitleg
Elke knop heeft zijn eigen EXTI-lijn. Daardoor kan de microcontroller meteen de juiste actie uitvoeren zonder polling in de hoofdlus.

## Concepten uit Labo 4
- meerdere EXTI-lijnen
- falling edge
- NVIC
- interruptgestuurde actie

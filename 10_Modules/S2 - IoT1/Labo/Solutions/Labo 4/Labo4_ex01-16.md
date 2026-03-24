# Labo4 ex01-16

## Opgave
Genereer een blokgolf op een GPIO-pin met behulp van Timer7.

## Oplossing
- Configureer `PA9` als uitgang.
- Stel Timer7 in op een update om de `20 ms`.
- Toggle `GPIOA->ODR` bit 9 in de interrupt.
- Meet het resultaat op de pin met een oscilloscoop.

## Codevoorbeeld
```c
void TIM7_IRQHandler(void)
{
    TIM7->SR &= ~TIM_SR_UIF;
    GPIOA->ODR ^= GPIO_ODR_9;
}
```

## Korte uitleg
Elke interrupt wisselt de pin tussen hoog en laag. Omdat dat om de 20 ms gebeurt, krijg je een blokgolf met een periode van ongeveer 40 ms.

## Concepten uit Labo 4
- GPIO-output
- blokgolf
- periodiek toggelen
- timing meten

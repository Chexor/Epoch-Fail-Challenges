# Labo3 ex01-11

## Opgave
Laat de teller lopen zoals in ex01-04, maar stop alles via een interrupt op SW1.

## Oplossing
- Gebruik polling om de telsnelheid te kiezen.
- Configureer een EXTI-interrupt op `SW1`.
- Wis in de handler de pending flag.
- Zet alle leds aan en zet een stopvlag op `true`.

## Codevoorbeeld
```c
void EXTI0_1_IRQHandler(void)
{
    EXTI->PR = EXTI_PR_PR1;
    ByteToLeds(0xFF);
    gestopt = true;
}

while (!gestopt)
{
    ByteToLeds(count);
    count++;
    WaitForMs(100);
}
```

## Korte uitleg
De interrupt onderbreekt de hoofdlus meteen. De handler zet het systeem in een eindtoestand: teller gestopt en alle leds aan.

## Concepten uit Labo 3
- EXTI
- interrupt handler
- pending flag wissen
- `volatile` stopvlag

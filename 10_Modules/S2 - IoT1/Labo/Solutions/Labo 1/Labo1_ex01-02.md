# Labo1 ex01-02

## Opgave
Toon na de startup-sequentie een eenvoudig LED-patroon met LED1 en LED8.

## Oplossing
- Voer eerst de startup-sequentie uit.
- Toggle daarna `LED1` twee keer na elkaar.
- Wacht `100 ms`.
- Toggle vervolgens `LED1` en `LED8` en wacht opnieuw `100 ms`.

## Codevoorbeeld
```c
while (1)
{
    ToggleLed(1);
    ToggleLed(1);
    WaitForMs(100);

    ToggleLed(1);
    ToggleLed(8);
    WaitForMs(100);
}
```

## Korte uitleg
De code wisselt in de praktijk tussen alle leds uit en het patroon met LED1 en LED8 aan. De dubbele toggle op LED1 heft zichzelf op.

## Concepten uit Labo 1
- startup-sequentie
- `ToggleLed(...)`
- patroonvorming
- tijdsvertragingen

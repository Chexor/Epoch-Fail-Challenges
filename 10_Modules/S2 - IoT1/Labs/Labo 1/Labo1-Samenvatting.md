# Labo 1 - Overzicht

## Oefeningen
- [[Labo1_ex01-01]] - 1 led laten knipperen.
- [[Labo1_ex01-02]] - een eenvoudig patroon met LED1 en LED8.
- [[Labo1_ex01-03]] - een 8-bit teller tonen op de leds.
- [[Labo1_ex01-04]] - de telsnelheid kiezen met knoppen.

## Concepten in dit labo
- `while(1)` als oneindige hoofdlus.
- `SysTick_Handler()` en `ticks` als milliseconde-teller.
- `WaitForMs(...)` voor blocking delays.
- `SetLed(...)`, `ClearLed(...)`, `ToggleLed(...)` en `ByteToLeds(...)`.
- Polling van drukknoppen met `SW1Active()` tot `SW4Active()`.
- Een binaire teller weergeven op 8 leds.

## Kernidee
Dit labo legt de basis van embedded programmeren: uitgangen aansturen, ingangen lezen, tijd gebruiken en eenvoudige logica herhalen.

## Kort codevoorbeeld
```c
while (1)
{
    ByteToLeds(count);
    count++;
    WaitForMs(100);
}
```

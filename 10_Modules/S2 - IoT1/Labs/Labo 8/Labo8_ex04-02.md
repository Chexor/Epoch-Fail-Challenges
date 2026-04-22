# Labo8 ex04-02

## Opgave
Toon de waarde van `ticks` op het OLED-scherm, update elke seconde op lijn 4. De rest van het scherm blijft leeg.

## Oplossing
- Vertrokken van ex04-01 (werkende I2C/OLED-template).
- Lijn 4 is page `3` (0-based pages).
- `ticks` formatteren met `snprintf`.
- Update elke 1000 ms via verschilmeting `now - lastUpdate`.

## Waarom deze aanpak
- `ticks` wordt elke 1 ms verhoogd in `SysTick_Handler`, dus die variabele is een betrouwbare softwareklok.
- Door `now - lastUpdate` te gebruiken, krijg je stabiele timing zonder blokkerende `WaitForMs(1000)`.
- Met `fillWithBlanks = true` blijft de lijn proper, ook als het aantal cijfers verandert.

## Werkwijze
1. OLED één keer wissen met `OLED_FillScreen(0)`.
2. Startwaarde meteen tonen (niet wachten op 1 seconde).
3. In de `while(1)` om de 1000 ms nieuwe tekst maken en op page `3` schrijven.
4. Rest van het scherm niet meer aanraken.

## Codevoorbeeld
```c
uint32_t lastUpdate = ticks;
char oledText[22];

OLED_FillScreen(0);
snprintf(oledText, sizeof(oledText), "ticks: %lu", (unsigned long)ticks);
OLED_StringToPage(oledText, 3, true);

while(1)
{
    uint32_t now = ticks;
    if((now - lastUpdate) >= 1000U)
    {
        lastUpdate = now;
        snprintf(oledText, sizeof(oledText), "ticks: %lu", (unsigned long)now);
        OLED_StringToPage(oledText, 3, true);
    }
}
```

## Snel testen
- Na flashen zie je op lijn 4 een teller (`ticks: ...`).
- Waarde moet ongeveer elke seconde verspringen.
- Andere lijnen blijven leeg.

## Veelgemaakte fouten
- Page verkeerd gekozen (lijn 4 moet page `3` zijn).
- Te kleine tekstbuffer gebruiken in `snprintf`.
- `lastUpdate` niet updaten na het schrijven.

# Labo8 ex04-01

## Opgave
Gebruik een OLED-scherm via I2C. Zet je voornaam op lijn 2 en je achternaam op lijn 3. De rest van het scherm blijft leeg.

## Oplossing
- `i2c1.c/.h`, `oled.c/.h` en `font6x8.h` toegevoegd aan het project.
- I2C en OLED initialiseren met:
  - `InitI2C1();`
  - `OLED_Init();`
- Scherm wissen met `OLED_FillScreen(0);`.
- Naam tonen met:
  - `OLED_StringToPage((char*)voornaam, 1, true);`
  - `OLED_StringToPage((char*)achternaam, 2, true);`

## Waarom deze aanpak
- De OLED-library werkt met pages (0-based): page `1` = lijn 2, page `2` = lijn 3.
- `fillWithBlanks = true` zorgt dat oude tekens op die lijn weggewerkt worden.
- Door eerst `OLED_FillScreen(0)` te doen, start je met een volledig leeg scherm zoals de opgave vraagt.

## Stappenplan in `main`
1. Basis init (`SystemClock_Config`, buttons/leds/usart/ad).
2. `InitI2C1();` en daarna `OLED_Init();`.
3. Eventuele startup-sequentie afronden.
4. `OLED_FillScreen(0);` uitvoeren.
5. Voornaam op page 1, achternaam op page 2 schrijven.
6. In `while(1)` niets extra doen voor oef 4.1.

## Codevoorbeeld
```c
static const char voornaam[] = "Tim";
static const char achternaam[] = "Kindt";

OLED_FillScreen(0);
OLED_StringToPage((char*)voornaam, 1, true);
OLED_StringToPage((char*)achternaam, 2, true);
```

## Snel testen
- Build en flash.
- Verwacht resultaat:
  - lijn 2 = voornaam
  - lijn 3 = achternaam
  - alle andere lijnen leeg

## Veelgemaakte fouten
- `InitI2C1()` vergeten (OLED toont niets).
- Verkeerde line/page-index gebruikt (bijv. `2` en `3` i.p.v. `1` en `2`).
- `font6x8.h` ontbreekt terwijl `oled.c` die header include't.

# Labo 8 - Overzicht

## Oefeningen
- [[Labo8_ex04-01]] - voornaam/achternaam op OLED via I2C
- [[Labo8_ex04-02]] - `ticks` elke seconde op lijn 4
- [[Labo8_ex04-03]] - progress bar op lijn 5 via trimmer (ADC)

## Concepten
- I2C1 initialiseren met `InitI2C1()`
- OLED initialiseren met `OLED_Init()`
- Tekst tonen met `OLED_StringToPage(...)`
- Pixeldata per page tonen met `OLED_ArrayToPage(...)`
- Timing op basis van `ticks` (`now - lastUpdate`)
- ADC uitlezen met `GetAdValue()` en schalen naar schermbreedte

## Page-mapping OLED
- Page `0` = lijn 1
- Page `1` = lijn 2
- Page `2` = lijn 3
- Page `3` = lijn 4
- Page `4` = lijn 5

Deze mapping verklaart waarom ex04-01 pages `1/2` gebruikt, ex04-02 page `3`, en ex04-03 page `4`.

## Samenvatting per oefening
- **ex04-01**: vaste tekst op OLED (naam), focus op correcte init en page-adressering.
- **ex04-02**: periodieke tekstupdate (ticks) met niet-blokkerende timing.
- **ex04-03**: analoge input naar grafische output (ADC -> progress bar).

## Kernidee
Labo 8 combineert I2C-communicatie, OLED-weergave en ADC-metingen om zowel tekst als een dynamische grafische bar op het scherm te tonen.

# Labo8 ex04-03

## Opgave
Gebruik de onboard trimmer (ADC) om op lijn 5 van het OLED een progress bar te tonen. AD-omzetting ongeveer elke 200 ms.

## Oplossing
- Vertrokken van ex04-01 (werkende I2C/OLED-template).
- AD-waarde lezen met `GetAdValue()`.
- Schalen van `0..4095` naar `0..128` kolommen.
- Buffer opbouwen met `0xFF` (gevuld) en `0x00` (leeg).
- Balk naar page `4` sturen met `OLED_ArrayToPage(...)`.

## Waarom deze aanpak
- `GetAdValue()` geeft een 12-bit waarde (`0..4095`).
- Het OLED is `128` pixels breed (`OLED_WIDTH`), dus schaling naar kolommen is logisch.
- Een byte-array op page-niveau is efficient en geeft een strakke grafische bar.
- Update om de 200 ms is vlot genoeg zonder overbodige I2C-traffic.

## Werkwijze
1. Scherm bij opstart wissen met `OLED_FillScreen(0)`.
2. In de lus elke 200 ms ADC lezen.
3. `filledColumns` berekenen via lineaire schaling.
4. Buffer vullen (`0xFF` tot de grens, daarna `0x00`).
5. Buffer op page `4` schrijven met `OLED_ArrayToPage(...)`.

## Codevoorbeeld
```c
uint8_t progressBar[OLED_WIDTH];

while(1)
{
    uint32_t now = ticks;
    if((now - lastUpdate) >= 200U)
    {
        uint16_t adValue = GetAdValue();
        uint16_t filledColumns = (uint16_t)(((uint32_t)adValue * OLED_WIDTH) / 4095U);

        for(uint8_t i = 0; i < OLED_WIDTH; i++)
            progressBar[i] = (i < filledColumns) ? 0xFF : 0x00;

        OLED_ArrayToPage(progressBar, OLED_WIDTH, 4);
        lastUpdate = now;
    }
}
```

## Snel testen
- Trimmer volledig tegenwijzerzin: bar bijna/volledig leeg.
- Trimmer volledig wijzerzin: bar bijna/volledig vol.
- Balk verandert ongeveer 5 keer per seconde.

## Veelgemaakte fouten
- Verkeerde page gebruiken (lijn 5 = page `4`).
- Schaling met `4096` of foute cast waardoor laatste kolom nooit vol raakt.
- Richting omgekeerd door mechanische montage van de trimmer.

Als de richting omgekeerd is, kan je dit gebruiken:
```c
filledColumns = OLED_WIDTH - filledColumns;
```

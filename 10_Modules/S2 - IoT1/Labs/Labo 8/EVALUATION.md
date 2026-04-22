# Evaluation ex04-01_to_ex04-03

## 1) Waarvoor zorgt de `PE` bit in het `I2C1->CR1` register?

`PE` is de **Peripheral Enable** bit van I2C1.

- `PE = 0`: I2C1 staat uit.
- `PE = 1`: I2C1 staat aan en kan I2C-communicatie uitvoeren.

In `InitI2C1()` gebeurt dat op het einde met:
```c
I2C1->CR1 |= I2C_CR1_PE;
```

Praktisch in de debugger:
- Zet een breakpoint net voor deze instructie en lees `I2C1->CR1` uit.
- Stap 1 regel verder (Step Over).
- Je ziet dan dat bit `PE` omschakelt van `0` naar `1`.
- Dat is het moment waarop de peripheral effectief geactiveerd wordt.

## 2) Als JP1 voor I2C1 gebruikt wordt: op welke pin wordt de klok gegenereerd?

Op **PB8** (I2C1 SCL).

Onderbouwing:
- In `InitI2C1()` staat expliciet:
  - `PB8 => SCL-pin`
  - `PB9 => SDA-pin`
- PB8 wordt geconfigureerd als alternate function voor I2C1, dus dat is de kloklijn die op de JP1-koppeling gebruikt wordt.

Kort:
- `PB8` = klok (`SCL`)
- `PB9` = data (`SDA`)

## 3) Signatuur van `OLED_StringToPage` in `oled.c`

Definitie:
```c
void OLED_StringToPage(char* text, uint8_t pageNumber, bool fillWithBlanks)
```

Parameters:
- `text`: pointer naar de string die getoond moet worden.
- `pageNumber`: pagina/lijn op het OLED-scherm (0 t.e.m. 7).
- `fillWithBlanks`: als `true`, wordt de rest van de lijn opgevuld met spaties.

Typisch gebruik:
- `OLED_StringToPage("Hello", 3, true);`
- Dit zet tekst op lijn 4 (page 3) en wist achterblijvende karakters op dezelfde lijn.

Return:
- `void` (de functie geeft geen waarde terug).

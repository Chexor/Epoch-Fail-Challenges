# IoT 1 - Les 2 - Samenvatting

Les 2 focust op de meest elementaire vorm van interactie met de buitenwereld: digitale input/output en het inlezen van analoge signalen via de AD-converter.

## 1. GPIO (General Purpose Input/Output)

De pinnen op de Nucleo (STM32F091RC) kunnen voor verschillende doeleinden gebruikt worden. In deze les kijken we naar de basis: digitale in- en uitgangen.

### Registers
Om een pin aan te sturen of uit te lezen, werken we met specifieke registers:
- **MODER (GPIOx_MODER)**: Bepaalt de modus van de pin (Input, Output, Alternate Function of Analoog).
- **ODR (GPIOx_ODR)**: Output Data Register. Hier schrijf je een '1' of '0' naar toe om een LED aan of uit te zetten.
- **IDR (GPIOx_IDR)**: Input Data Register. Hier lees je de status van een pin (bv. een drukknop) uit.

### Hardware op het NES (Nucleo Extension Shield)
- **8 LED's**: Verbonden met specifieke pinnen (meestal geconfigureerd als digitale output).
- **4 Drukknoppen**: Verbonden met pinnen geconfigureerd als digitale input.

## 2. ADC (Analog-to-Digital Converter)

Een microcontroller werkt digitaal (0 of 1), maar de wereld is analoog. De ADC slaat de brug.

### Eigenschappen van de STM32 ADC
- **Resolutie**: 12-bit. Dit betekent dat een analoge spanning wordt omgezet in een getal tussen **0 en 4095** ($2^{12} - 1$).
- **Spanningsbereik**: Meestal tussen 0V en 3.3V.

### De Trimmer (Potentiometer)
Op het NES-shield zit een trimmer. Door hieraan te draaien, verander je de spanning op een specifieke analoge inputpin.
- **Toepassing**: De ingelezen waarde (0-4095) kan gebruikt worden om variabelen in je code aan te passen, zoals de snelheid van een knipperende LED of een drempelwaarde.

## 3. Software & Datatypes

In deze les wordt ook het belang van de juiste datatypes herhaald:
- Gebruik `uint16_t` voor ADC-waarden (omdat 4095 niet in een `uint8_t` past).
- Gebruik bit-shifting (`>>` of `<<`) om waarden te schalen (bv. een 12-bit ADC waarde omzetten naar een 8-bit waarde voor de 8 LED's).

## Actieve recall (checkvragen)
1. Welk register gebruik je om een pin als output in te stellen?
2. Wat is de maximale waarde die een 12-bit ADC kan teruggeven?
3. Waarom gebruiken we `uint16_t` voor het opslaan van een ADC-waarde?
4. Hoe vertaal je een waarde van 0-4095 naar een weergave op 8 LED's?

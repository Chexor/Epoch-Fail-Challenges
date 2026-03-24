---
type: module-overzicht
vak: IoT1
docent: Ruben Buysschaert
lesuren: Dinsdag 08:45 - 12:00
examendatum:
onderwijsvorm: dagonderwijs
status: lopend semester
semester: 2
---

# Module Overzicht: IoT1

## Modulefiche

- **Docent**: Ruben Buysschaert
- **Lesuren**: Dinsdag 08:45 - 12:00
- **Examendatum**: _Nog in te vullen_
- **Onderwijsvorm**: Dagonderwijs
- **Status**: Lopend semester

## Documentatie & Lessen

Hieronder vind je een overzicht van de beschikbare lesnotities en samenvattingen:

- [[IoT 1 - Les 1 - Samenvatting|Les 1 - Introductie tot IoT & Microcontrollers]]
- [[IoT 1 - Les 2 - Samenvatting|Les 2 - Input, Output & AD-converter]]
- [[IoT 1 - Les 3 - Samenvatting|Les 3 - Klok, Watchdog, Debugger & Interrupts]]
- [[IoT 1 - Les 4 - Samenvatting|Les 4 - Timers & Slinger]]
- [[IoT1 - Les 5 - Samenvatting|Les 5 - Structs, Pointers, Alternate Functions & USART]]
- [[IoT1 - Les 6 - Samenvatting|Les 6 - SBUS, SPI, Audio & IO-expander]]

## Hardware & Software

### Hardware
- **Nucleo-F091RC**: Gebaseerd op de `STM32F091RC` (32-bit ARM Cortex-M0).
- **Nucleo Extension Shield (NES)**: Bevat 4 drukknoppen, 8 LED's, een trimmer en een 10-pin box header.
- **Specifieke Componenten**:
	- **SBUS Inverter**: Voor RC-communicatie.
	- **PGA2311**: Digitale audio volumeregeling.
	- **APA102C**: Adresseerbare RGB LED's.
	- **MCP23S17**: 16-bit IO-expander via SPI.

### Software
- **µVision (Keil)**: IDE voor ontwikkeling, compileren en debuggen.
- **ST-Link**: On-board programmer en debugger.
- **C-taal**: Focus op embedded C met gebruik van `stdint.h` voor voorspelbare datatypes.

## Concepten per les

| Les | Belangrijkste Concepten |
| :--- | :--- |
| **Les 1** | MCU vs MPU, C datatypes (`uint8_t`, etc.), µVision workflow, Nucleo Architectuur. |
| **Les 2** | GPIO Registers (MODER/ODR/IDR), 12-bit ADC, Schalen van analoge input naar 8 LED's. |
| **Les 3** | Clock Tree (HSI/PLL/48MHz), Independent Watchdog (IWDG), NVIC (Interrupts), Debugging. |
| **Les 4** | Hardware Timers (TIMx), Prescaler (PSC), Auto-reload (ARR), Slinger-project. |
| **Les 5** | `structs`, `pointers`, Alternate Functions (AF), USART (Baudrate, TX/RX, Polling/Interrupt/DMA). |
| **Les 6** | SBUS (100k baud, inverted), SPI (SCLK/MOSI/MISO/CS), Zero Crossing (PGA2311), IO-expansion. |

## Taken

```tasks
not done
path includes 10_Modules/S2 - IoT1
sort by priority
sort by due
```

## Snelle links

- Info: [[Info]]
- Lessen: [[Lessen]]
- Oefeningen: [[Oefeningen]]
- Oplossingen: [GitHub Repo](https://github.com/Chexor/IoT1)

---
type: theory
domain: "computer-science"
parent: "Communication Protocols"
related:
  - SPI (Serial Peripheral Interface)
theme: "embedded-communication"
aliases:
  - IO-expander
---

# IO-expander
#concept #electronics #embedded

## 1. Wat is het kernprobleem?
Microcontrollers have a limited number of physical GPIO pins. When a project requires more inputs or outputs than available, an **IO-expander** allows adding more pins using only a few communication lines (like I2C or SPI).

## 2. Intuitieve uitleg
Stel je voor dat je een stekkerdoos gebruikt om één stopcontact uit te breiden naar zes. Een IO-expander doet hetzelfde voor de "pootjes" (pinnen) van je computerchip. Je praat tegen de expander via een snelle "briefwisseling" (seriële bus), en de expander zet die commando's om in het aan- of uitzetten van zijn eigen pinnen.

## 3. Formele structuur
An IO-expander is an integrated circuit (IC) that communicates with a host microcontroller via a serial protocol.

### Key Specifications:
- **Interface**: Usually **I2C** (e.g., PCF8574) or **SPI** (e.g., MCP23S17).
- **Bit-width**: Typically 8-bit or 16-bit, providing that many additional GPIOs.
- **Addressing**: Multiple expanders can often be placed on the same bus by configuring hardware address pins (A0, A1, A2).
- **Registers**: Controlled via internal registers:
  - `IODIR`: Sets pin direction (Input/Output).
  - `GPIO` / `OLAT`: Sets or reads the logic level.
  - `GPPU`: Enables internal pull-up resistors.

## 4. Toepassing
Using an **MCP23S17** (16-bit SPI expander) to drive 16 LEDs:
1. Connect MOSI, MISO, SCK, and CS to the MCU.
2. Send SPI command to set `IODIR` register to `0x00` (all outputs).
3. Send SPI command to `GPIO` register with value `0xFFFF` to turn all LEDs on.

## 5. Examengerichte vertaling
- **Typische vraag:** "Hoeveel extra pinnen kun je aansturen met een PCF8574 en hoe verbind je deze?"
- **Vaak gemaakte fout:** Vergeten de adres-pinnen fysiek te verbinden (hoog of laag), waardoor de I2C-adressering niet klopt.
- **Link met andere concepten:** [[SPI]], [[I2C]], [[GPIO]].

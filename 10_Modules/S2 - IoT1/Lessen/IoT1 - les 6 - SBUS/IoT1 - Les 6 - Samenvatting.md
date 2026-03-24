# Samenvatting les 6

Deze les gaat over:
- `SBUS` protocol
- `[[SPI]]` bus
- `PGA2311` (volumeregeling)
- `APA102C` (adresseerbare LED's)
- `[[IO-expander]]` (MCP23S17)

## 1. SBUS Protocol

**SBUS** is een serieel protocol dat veel gebruikt wordt in de RC-wereld (afstandsbedieningen).

- **Type**: Serieel (UART-gebaseerd), maar **geïnverteerd**.
- **Snelheid**: 100.000 baud.
- **Data**: Kan tot 16 kanalen aan stuurinformatie doorgeven via één enkele draad.
- **Hardware**: Omdat het signaal geïnverteerd is, heb je vaak een transistor of inverter-chip nodig om het te kunnen lezen met een standaard UART-poort.

## 2. SPI (Serial Peripheral Interface)

**[[SPI]]** is een snelle, synchrone bus om chips met elkaar te laten praten.

Belangrijke pinnen:
- **SCLK** (Serial Clock): De klok die de snelheid bepaalt (gegeven door de master).
- **MOSI** (Master Out Slave In): Data van de MCU naar de chip.
- **MISO** (Master In Slave Out): Data van de chip terug naar de MCU.
- **CS / NSS** (Chip Select): Hiermee kies je met welke chip je wilt praten.

## 3. PGA2311 (Audio Volume Control)

De **PGA2311** is een chip om het volume van een audiosignaal digitaal te regelen.

- **Werking**: Je stuurt via SPI een waarde door, en de chip past de versterking aan.
- **Zero Crossing Detection**: Een belangrijke feature die zorgt dat het volume pas verandert als het audiosignaal de 0V passeert. Dit voorkomt irritante "tikjes" in het geluid.

## 4. APA102C (RGB LED's)

Dit zijn adresseerbare LED's (vergelijkbaar met NeoPixels/WS2812), maar met een belangrijk verschil.

- **Interface**: Gebruikt een aparte Data- en Clock-lijn (SPI-stijl).
- **Voordeel**: Omdat er een kloklijn is, is de timing veel minder kritisch dan bij WS2812. Je kunt ze veel sneller aansturen.

## 5. IO-expander (MCP23S17)

Een **[[IO-expander]]** gebruik je als de pinnen van je microcontroller op zijn.

- **Type**: In deze les gebruiken we de **MCP23S17** (SPI-versie).
- **Functie**: Voegt 16 extra digitale pinnen toe aan je systeem via de SPI-bus.
- **Registers**: Je moet de chip configureren via registers (bijv. `IODIR` om te kiezen tussen input of output).

## Belangrijkste kernideeen

- **SBUS** is handig voor afstandsbedieningen maar vereist een inverter en een specifieke baudrate (100k).
- **[[SPI]]** is een full-duplex bus waarbij de **Chip Select** bepaalt welke component actief is.
- De **PGA2311** gebruikt **Zero Crossing** voor zuivere audio-overgangen.
- De **MCP23S17** breidt je aantal pinnen uit via SPI-commando's.

## Kort onthouden

- **SBUS** = 100k baud, inverted UART, 16 kanalen.
- **SPI** = SCLK, MOSI, MISO, CS.
- **Zero Crossing** = Volume aanpassen zonder bijgeluiden.
- **IO-expander** = Meer pinnen via een seriële bus.

---
type: lesnotitie
vak: IoT1
les: "8"
datum: 2026-03-31
docent: Ruben Buysschaert
status: actief
parent: "[[10_Modules/S2 - IoT1/00_Module_Overzicht|IoT1]]"
related: []
---

# IoT1 - Les 8 - Wifi & MQTT
#iot1 #lesnotitie

## Lescontext
- **Datum:** 2026-03-31
- **Thema:** Wifi & MQTT
- **Docent:** Ruben Buysschaert
- **Status:** live capture
- **Bronnen:**

## Snelle capture

### Doelen van deze les
-

### Live notities
- We gaan uitsluitend QoS0
- We gebruiken MQTT Explorer om topics en JSON-berichten te monitoren
- MQTT-broker is centrale punt

### Kernbegrippen
- MQTT (Message Queue Telemetry Transport)
- Publish/Subscribe-communicatiemodel
- MQTT-broker (bv. Mosquitto, test.mosquitto.org, mqtt.rubu.be)
- MQTT-client (publishen en subscriben)
- MQTT Explorer als praktische MQTT-client voor testen en debugging
- Topic-structuur (bv. `achternaamvoornaam/leds`, `achternaamvoornaam/buttonsadleds`)
- QoS-niveaus (QoS 0, QoS 1, QoS 2) - in deze les focus op QoS 0
- ESP32-C3 met AT-firmware
- USART1-koppeling tussen Nucleo en ESP32-C3
- Circulair buffer (`readIndex`, `writeIndex`, `numberOfStringsInBuffer`)
- JSON-payloads voor I/O-data (buttons, AD, leds)
- Watchdog timer om reset te forceren bij geblokkeerde hoofdlus

### Voorbeelden en demo's
-

### Vragen tijdens de les
- [ ]

### Acties / taken
- [ ]

---

## Uitwerking na de les

### 1. Groot plaatje
*Welk probleem of welk groter onderwerp staat centraal in deze les?*

### 2. Intuitie
*Leg de kernideeen eerst eenvoudig uit, nog zonder te veel detail.*

### 3. Formele structuur
*Definities, syntax, formules, stappenplannen, architectuur of technische details.*

### 4. Toepassing
*Voorbeelden, demo's, oefeningen, code, of concrete use-cases uit de les.*

### 5. Examenfocus
- **Te kennen:**
- **Typische valkuilen:**
- **Mogelijke examenvraag:**

## Links
- **Module:** [[10_Modules/S2 - IoT1/00_Module_Overzicht|IoT1]]
- **Leslog:**
- **Samenvatting:** [[IoT1-Les8-Wifi_MQTT#Samenvatting|Samenvatting Les 8]]
- **Oefeningen:**
- **Concepten:**

---

## Samenvatting Les 8: Wifi & MQTT

Deze les introduceert **MQTT**, een lichtgewicht communicatieprotocol ideaal voor IoT. De kern is een **publish/subscribe-model**, waarbij een centrale **MQTT-broker** berichten verdeelt. IoT-devices (clients) publiceren berichten naar specifieke **topics** (bv. `student/leds`) of abonneren zich op topics om berichten te ontvangen.

In de praktijk koppelen we een Nucleo-bord via **USART1** aan een **ESP32-C3** (met AT-firmware) om Wifi-connectiviteit te krijgen. De communicatie tussen deze twee wordt efficiënt beheerd met een **circulair buffer**.

De data zelf, zoals de status van knoppen of ADC-waarden, wordt verpakt in een **JSON-payload** en verstuurd. We gebruiken de tool **MQTT Explorer** om de communicatie op de broker te monitoren en te debuggen. De focus ligt op **QoS 0**, de snelste maar minst gegarandeerde manier van berichtlevering. Tot slot wordt een **watchdog timer** gebruikt als veiligheidsmechanisme om de microcontroller te resetten als de hoofd-loop vastloopt.

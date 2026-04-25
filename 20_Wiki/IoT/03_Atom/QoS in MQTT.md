---
type: atom
domain: "iot"
parent: MQTT
related:
  - MQTT
  - Communication Protocols
  - Watchdog Timer
theme: "networked-systems"
aliases:
  - QoS in MQTT
  - MQTT QoS
---

# QoS in MQTT
#concept #iot #communication

QoS in MQTT definieert hoeveel leveringsgarantie een bericht krijgt tussen client en broker.

## Korte kern

- `QoS 0`: at most once, snelst maar zonder bevestiging
- `QoS 1`: at least once, met kans op duplicaten
- `QoS 2`: exactly once, hoogste zekerheid met meeste overhead

## Probleem

Hoe kies je de juiste balans tussen betrouwbaarheid, latentie en netwerkbelasting voor MQTT-berichten?

## Intuïtie

Hoe hoger het QoS-niveau, hoe meer controleberichten en dus overhead. Je kiest dus niet standaard het hoogste niveau, maar wat functioneel nodig is voor de use case.

## Toepassing

Telemetrie met hoge frequentie gebruikt vaak `QoS 0`; kritische commando's zoals "deur sluiten" kiezen eerder `QoS 1` of `QoS 2` afhankelijk van duplicate-tolerantie.

## Formeel

- QoS wordt per publish/subscription ingesteld.
- Niveau bepaalt ack-flow tussen client en broker.
- Keuze hangt af van foutkost, bandbreedte en realtime-vereisten.

## Verbanden

- [[MQTT]]
- [[Communication Protocols]]
- [[Watchdog Timer]]

---
type: theory
domain: "iot"
parent: Internet of Things (IoT)
related:
  - QoS in MQTT
  - USART en UART
  - Watchdog Timer
theme: "networked-systems"
aliases:
  - MQTT
  - Message Queue Telemetry Transport
---

# MQTT
#concept #iot #communication


MQTT is een lichtgewicht publish/subscribe-protocol waarbij clients via een broker berichten uitwisselen op topics.

## Korte kern

- ontkoppelt zenders en ontvangers via topic-gebaseerde broker-routing
- is ontworpen voor beperkte bandbreedte en resource-arme devices
- wordt breed gebruikt in IoT-telemetrie en remote besturing

## Probleem

Hoe laat je veel IoT-devices efficiënt communiceren zonder directe point-to-point koppelingen tussen alle partijen?

## Intuïtie

Een client publiceert data op een topic. Andere clients die op dat topic subscriben krijgen die data via de broker. Daardoor kennen publisher en subscriber elkaar niet rechtstreeks.

## Toepassing

Een sensor node publiceert temperatuur op `gebouw/ruimte1/temp`; dashboard en alarmservice subscriben op dat topic en reageren onafhankelijk.

## Formeel

- Rollen: broker, publisher, subscriber.
- Kernacties: connect, publish, subscribe, unsubscribe.
- Topicstructuur bepaalt routering en schaalbaarheid.
- Betrouwbaarheidsgedrag wordt vastgelegd via QoS-niveaus.

## Verbanden

- [[Communication Protocols]]
- [[QoS in MQTT]]
- [[USART en UART]]
- [[Watchdog Timer]]

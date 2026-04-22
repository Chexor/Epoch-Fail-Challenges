---
type: theory
domain: "iot"
parent: Microcontroller vs Microprocessor
related:
  - Interrupt
  - Hardware Timer
  - MQTT
theme: "embedded-systems"
aliases:
  - Watchdog Timer
  - Watchdog
---

# Watchdog Timer
#concept #iot #embedded


Een watchdog timer bewaakt of software nog correct loopt en forceert een reset als de toepassing vastloopt.

## Korte kern

- watchdog verhoogt robuustheid van autonome systemen
- software moet periodiek de watchdog verversen
- uitblijven van refresh wijst op blokkering of foutpad

## Probleem

Hoe herstel je een embedded systeem automatisch wanneer de hoofdlogica onverwacht hangt?

## Intuïtie

De watchdog is een onafhankelijke timer met een deadline. Zolang de software gezond is, reset ze die timer op tijd. Bij een hang of deadlock gebeurt dat niet en dwingt de watchdog een herstart af.

## Toepassing

In IoT-nodes voorkomt een watchdog langdurige uitval bij netwerk- of state-machinefouten. Het systeem kan na reset opnieuw initialiseren en terug online komen.

## Formeel

- Stel prescaler/reload in volgens gewenste timeout.
- Activeer watchdog en refresh binnen tijdsvenster.
- Bij timeout zonder refresh volgt hardware reset.
- Best practice: refresh alleen in bewezen gezonde control flow.

## Verbanden

- [[Microcontroller vs Microprocessor]]
- [[Interrupt]]
- [[Hardware Timer]]
- [[MQTT]]

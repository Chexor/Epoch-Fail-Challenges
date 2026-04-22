---
type: theory
domain: "artificial-intelligence"
parent: Heuristic Properties
related:
  - Admissible Heuristic
  - Heuristic Properties
  - A-star Search
  - Admissible vs Consistent Heuristic
theme: "heuristic-properties-for-a-star"
aliases:
  - Consistent Heuristic
---

# Consistent Heuristic
#concept #ai

Een consistent heuristic is een heuristiek die lokaal coherent blijft over opeenvolgende nodes, zodat haar schattingen niet sneller dalen dan de echte stapkosten toelaten.

## Korte kern

- een consistente heuristiek respecteert een lokale driehoeksvoorwaarde
- ze is sterker dan admissibility
- bij [[A-star Search]] maakt ze graph search netter en stabieler

## Probleem

Wanneer gedraagt een heuristiek zich lokaal logisch over opeenvolgende nodes heen?

## Intuïtie

Een heuristiek is `consistent` als ze niet te abrupt daalt tussen twee verbonden nodes. De geschatte resterende kost moet in lijn blijven met de echte stapkost.

## Toepassing

Als je van stad `A` naar buurstad `B` rijdt met kost `3`, dan mag een consistente heuristiek niet suggereren dat je resterende kost plots met meer dan `3` zakt door enkel die stap te zetten.

## Formeel

- Een heuristiek is `consistent` als voor elke overgang van `n` naar `n'` geldt:
  - `h(n) <= c(n,n') + h(n')`
- Dit is een vorm van driehoeksvoorwaarde.
- Consistentie impliceert admissibility.
- Bij `graph search` maakt consistentie `A*` netter en voorkomt ze problematische heropeningen van nodes.

## Verbanden

> **Valkuil:** `admissible` en `consistent` als synoniemen behandelen.

- [[Heuristic]]
- [[Admissible Heuristic]]
- [[A-star Search]]
- [[Admissible vs Consistent Heuristic]]

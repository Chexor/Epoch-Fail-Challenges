---
type: concept-topic
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

## 1. Wat is het kernprobleem?
Wanneer gedraagt een heuristiek zich lokaal logisch over opeenvolgende nodes heen?

## 2. Intuitieve uitleg
Een heuristiek is `consistent` als ze niet te abrupt daalt tussen twee verbonden nodes. De geschatte resterende kost moet in lijn blijven met de echte stapkost.

## 3. Formele structuur
- Een heuristiek is `consistent` als voor elke overgang van `n` naar `n'` geldt:
  - `h(n) <= c(n,n') + h(n')`
- Dit is een vorm van driehoeksvoorwaarde.
- Consistentie impliceert admissibility.
- Bij `graph search` maakt consistentie `A*` netter en voorkomt ze problematische heropeningen van nodes.

## 4. Toepassing
Als je van stad `A` naar buurstad `B` rijdt met kost `3`, dan mag een consistente heuristiek niet suggereren dat je resterende kost plots met meer dan `3` zakt door enkel die stap te zetten.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** `consistentie` legt een lokale voorwaarde op tussen verbonden nodes en is sterker dan `admissibility`.
- **Veelvoorkomende misvatting:** `admissible` en `consistent` als synoniemen behandelen.
- **Link met andere concepten:** [[Heuristiek]], [[Admissible Heuristic]], [[A-star Search|A* Search]], [[Admissible vs Consistent Heuristic]]
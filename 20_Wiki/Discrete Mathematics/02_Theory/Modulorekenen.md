---
type: theory
domain: "discrete-mathematics"
parent: "Discrete Number Operations"
related:
  - Discrete Number Operations
  - Modulaire inverse
  - Euler phi-functie
  - Staartdeling (Long Division)
theme: "discrete-structures-and-stepwise-reasoning"
aliases:
  - Modulorekenen
---

# Modulorekenen
#concept #discrete

## 1. Wat is het kernprobleem?
Hoe reken je wanneer alleen de rest na deling telt, in plaats van de volledige grootte van een getal?

## 2. Intuïtieve uitleg
Modulorekenen is klokrekenen. Op een klok is 15 uur hetzelfde als 3 uur wanneer je modulo 12 rekent.

## 3. Formele structuur
- `a ≡ b (mod n)` betekent dat `a` en `b` dezelfde rest hebben bij deling door `n`
- optellen, aftrekken en vermenigvuldigen blijven geldig binnen dezelfde restklasse
- delen kan niet altijd zomaar; daarvoor heb je soms een modulaire inverse nodig

## 4. Toepassing
Controlegetallen, cryptografie en klokproblemen gebruiken allemaal modulorekenen om met restklassen te werken in plaats van met gewone gehele getallen.

## 5. Examengerichte vertaling
- **Typische vraag:** Vereenvoudig deze uitdrukking modulo `n`.
- **Vaak gemaakte fout:** doen alsof delen modulo altijd automatisch kan.
- **Link met andere concepten:** [[Modulaire inverse]], [[Euler phi-functie]]

## Context in het domein
- Overzicht: [[00_Overzicht Discrete Mathematics]]
- Uitwerking: [[Modulaire Inverse Worked Example]]

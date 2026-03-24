---
type: concept-topic
domain: "discrete-mathematics"
parent: "Discrete Number Operations"
related:
  - Discrete Number Operations
  - Modulorekenen
  - Euler phi-functie
  - Modulaire Inverse Worked Example
theme: "discrete-structures-and-stepwise-reasoning"
aliases:
  - Modulaire inverse
---

# Modulaire inverse
#concept #discrete

## 1. Wat is het kernprobleem?
Hoe “deel” je modulo `n`, terwijl gewoon delen daar niet altijd betekenisvol is?

## 2. Intuïtieve uitleg
De modulaire inverse van `a` modulo `n` is een getal dat `a` terug naar 1 brengt in dat systeem. Het speelt dus de rol van een omgekeerde, maar alleen binnen het modulo-kader.

## 3. Formele structuur
- `x` is een inverse van `a` modulo `n` als `a * x ≡ 1 (mod n)`
- zo'n inverse bestaat alleen als `ggd(a, n) = 1`
- je vindt die vaak via het algoritme van Euclides

## 4. Toepassing
In RSA wordt de privésleutel berekend als modulaire inverse van een exponent modulo `phi(n)`.

## 5. Examengerichte vertaling
- **Typische vraag:** Bereken de inverse van `a` modulo `n`.
- **Vaak gemaakte fout:** proberen een inverse te zoeken terwijl `a` en `n` niet relatief priem zijn.
- **Link met andere concepten:** [[Modulorekenen]], [[Euler phi-functie]], [[Modulaire Inverse Worked Example]]

## Context in het domein
- Overzicht: [[00_Overzicht Discrete Mathematics]]
- Uitwerking: [[Modulaire Inverse Worked Example]]

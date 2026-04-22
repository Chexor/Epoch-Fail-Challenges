---
type: theory
domain: "discrete-mathematics"
parent: "Discrete Number Operations"
related:
  - Discrete Number Operations
  - Modulorekenen
  - Modulaire inverse
theme: "discrete-structures-and-stepwise-reasoning"
aliases:
  - Euler phi-functie
---

# Euler phi-functie
#concept #discrete

## 1. Wat is het kernprobleem?
Hoe tel je hoeveel getallen kleiner dan `n` relatief priem zijn met `n`?

## 2. Intuïtieve uitleg
De phi-functie meet hoeveel getallen binnen `1` tot `n-1` nog “goed samenwerken” met `n` voor inverse en modulorekenen.

## 3. Formele structuur
- `phi(n)` telt het aantal getallen kleiner dan `n` die relatief priem zijn met `n`
- deze functie speelt een centrale rol in Euler's stelling en RSA
- als `ggd(a, n) = 1`, dan geldt `a^phi(n) ≡ 1 (mod n)`

## 4. Toepassing
Bij RSA gebruik je `phi(n)` om de publieke en private exponenten met elkaar te verbinden.

## 5. Examengerichte vertaling
- **Typische vraag:** Bereken `phi(n)` of gebruik Euler's stelling in een modulo-vraagstuk.
- **Vaak gemaakte fout:** `phi(n)` verwarren met `n-1` in gevallen waar `n` niet priem is.
- **Link met andere concepten:** [[Modulorekenen]], [[Modulaire inverse]]

## Context in het domein
- Overzicht: [[00_Overzicht Discrete Mathematics]]

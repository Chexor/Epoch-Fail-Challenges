---
type: atom
domain: "machine-learning"
parent: [[Data]]
related:
  - Data
  - Feature
  - Target
theme: "ml-foundations"
aliases:
  - Example
  - Sample
---

# Example
#concept #ml

Een `example` (of `sample`) is één concreet datapunt binnen een dataset, bestaande uit de input-data (features) en optioneel de te voorspellen waarde (target).

## Korte kern

- 1 rij in een tabel
- 1 observatie met features en optioneel target

## Waarom is dit belangrijk?
Het is de fundamentele eenheid waarmee een model traint of test.

## Formele structuur
- 1 example = 1 paar `(x_i, y_i)`
- `x_i` = feature-vector van sample `i`
- `y_i` = target van sample `i`

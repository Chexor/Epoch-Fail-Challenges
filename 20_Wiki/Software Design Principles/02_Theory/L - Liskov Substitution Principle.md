---
type: theory
domain: "software-design-principles"
parent: "Object-Oriented Design Principles"
related:
  - Object-Oriented Design Principles
  - O - Open-Closed Principle
  - S - Single Responsibility Principle
theme: "maintainable-object-oriented-design"
aliases:
  - L - Liskov Substitution Principle
---

# L - Liskov Substitution Principle
#concept #design

## 1. Wat is het kernprobleem?
Wanneer mag een subtype echt de plaats innemen van zijn supertype zonder dat het gedrag van het programma stukgaat?

## 2. Intuïtieve uitleg
Als iets een subtype van iets anders noemt, dan moet het zich ook zo gedragen. Anders lijkt de erfelijkheid logisch op papier, maar breekt de verwachting van de gebruiker van de code.

## 3. Formele structuur
- een subtype moet inzetbaar zijn waar het supertype verwacht wordt
- precondities mogen niet strenger worden
- postcondities mogen niet zwakker worden
- invarianten moeten behouden blijven

## 4. Toepassing
Een subklasse die een contract van het supertype breekt, schendt LSP ook al compileert de code nog steeds.

## 5. Examengerichte vertaling
- **Typische vraag:** Leg uit waarom deze subklasse het LSP schendt.
- **Vaak gemaakte fout:** denken dat correcte compilatie genoeg is om substitueerbaarheid te garanderen.
- **Link met andere concepten:** [[O - Open-Closed Principle]], [[D - Dependency Inversion Principle]]

## Context in het domein
- Overzicht: [[SOLID Principes]]

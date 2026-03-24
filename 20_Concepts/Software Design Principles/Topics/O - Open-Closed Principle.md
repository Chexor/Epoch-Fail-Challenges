---
type: concept-topic
domain: "software-design-principles"
parent: "Object-Oriented Design Principles"
related:
  - Object-Oriented Design Principles
  - S - Single Responsibility Principle
  - SRP vs OCP
theme: "maintainable-object-oriented-design"
aliases:
  - O - Open-Closed Principle
---

# O - Open-Closed Principle
#concept #design

**Kernidee:** Een klasse moet open for extension zijn, maar closed for modification.

## 1. Wat is het kernprobleem?

Hoe kun je nieuw gedrag toevoegen aan een klasse zonder de bestaande, werkende broncode te moeten wijzigen?

## 2. Intuïtieve uitleg

Vergelijk het met een laptop. De laptop is gesloten aan de binnenkant, maar open voor uitbreiding via poorten. In software bereik je dit met abstracties, interfaces en patterns.

## 3. Formele structuur

- nieuw gedrag voeg je toe via uitbreiding, niet via wijziging van bestaande kerncode
- abstracties vormen de stabiele laag
- concrete uitbreidingen hangen onder die abstracties

## 4. Toepassing

In Strategy, Decorator of Factory Method voeg je nieuw gedrag toe door nieuwe klassen te maken in plaats van bestaande logica aan te passen.

## 5. Examengerichte vertaling
- **Typische vraag:** Refactor code die OCP schendt, bijvoorbeeld grote `if/else`-structuren op type.
- **Vaak gemaakte fout:** overal abstracties toevoegen zonder dat er echt verwachte variatie is.
- **Link met andere concepten:** [[S - Single Responsibility Principle]], [[D - Dependency Inversion Principle]], [[SRP vs OCP]]

## Context in het domein
- Overzicht: [[SOLID Principes]]
- Vergelijking: [[SRP vs OCP]]

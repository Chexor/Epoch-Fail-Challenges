---
type: theory
domain: "software-design-principles"
parent: "Object-Oriented Design Principles"
related:
  - Object-Oriented Design Principles
  - I - Interface Segregation Principle
  - SRP vs OCP
theme: "maintainable-object-oriented-design"
aliases:
  - D - Dependency Inversion Principle
---

# D - Dependency Inversion Principle
#concept #design

## 1. Wat is het kernprobleem?
Hoe zorg je dat belangrijke code niet vastzit aan concrete implementaties die moeilijk te vervangen of testen zijn?

## 2. Intuïtieve uitleg
Als high-level code rechtstreeks afhangt van concrete details, wordt elke wijziging onderaan gevaarlijk. DIP zegt dat beide beter afhangen van abstracties.

## 3. Formele structuur
- high-level modules mogen niet afhangen van low-level modules
- beide moeten afhangen van abstracties
- details horen af te hangen van abstracties, niet omgekeerd

## 4. Toepassing
Een service die rechtstreeks een specifieke databaseklasse aanmaakt is sterk gekoppeld. Met een interface kun je die database vervangen zonder high-level logica te herschrijven.

## 5. Examengerichte vertaling
- **Typische vraag:** Toon hoe dit ontwerp afhankelijkheden omkeert via een interface of abstracte klasse.
- **Vaak gemaakte fout:** denken dat dependency injection op zich al DIP garandeert zonder goede abstracties.
- **Link met andere concepten:** [[O - Open-Closed Principle]], [[I - Interface Segregation Principle]], [[L - Liskov Substitution Principle]]

## Context in het domein
- Overzicht: [[SOLID Principes]]

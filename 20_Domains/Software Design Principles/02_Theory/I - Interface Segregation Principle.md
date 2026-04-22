---
type: theory
domain: "software-design-principles"
parent: "Object-Oriented Design Principles"
related:
  - Object-Oriented Design Principles
  - D - Dependency Inversion Principle
  - S - Single Responsibility Principle
theme: "maintainable-object-oriented-design"
aliases:
  - I - Interface Segregation Principle
---

# I - Interface Segregation Principle
#concept #design

## 1. Wat is het kernprobleem?
Hoe vermijd je dat klassen afhankelijk worden van methodes die ze eigenlijk niet nodig hebben?

## 2. Intuïtieve uitleg
Een te brede interface is als een formulier waar je vijf pagina's moet invullen voor één eenvoudige aanvraag. ISP zegt dat je beter meerdere kleine, gerichte interfaces maakt.

## 3. Formele structuur
- clients mogen niet gedwongen worden te hangen aan methodes die ze niet gebruiken
- meerdere kleine interfaces zijn vaak beter dan één brede interface
- ISP vermindert onnodige koppeling

## 4. Toepassing
Een interface die zowel printen, scannen als faxen bevat, is problematisch als een client alleen wil printen.

## 5. Examengerichte vertaling
- **Typische vraag:** Waarom schendt deze interface het ISP?
- **Vaak gemaakte fout:** een brede interface handig vinden terwijl ze clients onnodig belast.
- **Link met andere concepten:** [[D - Dependency Inversion Principle]], [[S - Single Responsibility Principle]]

## Context in het domein
- Overzicht: [[SOLID Principes]]

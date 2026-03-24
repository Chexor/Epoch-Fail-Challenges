---
type: concept-topic
domain: "software-design-principles"
parent: "Object-Oriented Design Principles"
related:
  - Object-Oriented Design Principles
  - O - Open-Closed Principle
  - SRP Refactoring Worked Example
  - SRP vs OCP
theme: "maintainable-object-oriented-design"
aliases:
  - S - Single Responsibility Principle
---

# S - Single Responsibility Principle
#concept #design

**Kernidee:** Elke klasse moet één, en niet meer dan één, reden hebben om gewijzigd te worden.

- **Alias:** Hoge cohesie
- **Summary:** Een klasse moet slechts één duidelijke, samenhangende verantwoordelijkheid hebben.

## 1. Wat is het kernprobleem?

Wanneer een klasse te veel verantwoordelijkheden heeft, wordt code moeilijk te begrijpen en te onderhouden. Een wijziging in één verantwoordelijkheid kan onbedoelde neveneffecten hebben op de andere.

## 2. Intuïtieve uitleg

Vergelijk het met een Zwitsers zakmes. Het is handig, maar als je enkel een schroef wilt aandraaien, sleep je ook een blikopener, een schaar en een kurkentrekker mee.

SRP stelt dat je beter aparte gereedschappen hebt met elk één duidelijke taak. In software betekent dit dat elke klasse een specialist moet zijn in één ding.

## 3. Formele structuur

- een klasse hoort één conceptuele verantwoordelijkheid te dragen
- meerdere ongerelateerde redenen om te wijzigen wijzen op SRP-schending
- SRP stuurt naar hoge cohesie

## 4. Toepassing

Een klasse `SuperDashboard` combineert UI-logica en versiebeheer.

- reden 1 om te wijzigen: de UI verandert
- reden 2 om te wijzigen: de versie-informatie verandert

De oplossing is de klasse opsplitsen in bv. `DashboardView` en `VersionManager`.

## 5. Examengerichte vertaling
- **Typische vraag:** Toon waarom deze klasse SRP schendt en hoe je ze refactort.
- **Vaak gemaakte fout:** denken dat SRP betekent dat een klasse maar één methode mag hebben.
- **Link met andere concepten:** [[O - Open-Closed Principle]], [[SRP vs OCP]]

## Context in het domein
- Overzicht: [[SOLID Principes]]
- Vergelijking: [[SRP vs OCP]]
- Uitwerking: [[SRP Refactoring Worked Example]]

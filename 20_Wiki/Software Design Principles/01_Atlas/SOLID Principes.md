---
type: atlas
domain: "software-design-principles"
parent: 00_Overzicht Software Design Principles
related:
  - S - Single Responsibility Principle
  - O - Open-Closed Principle
  - D - Dependency Inversion Principle
theme: "maintainable-object-oriented-design"
aliases:
  - SOLID Principes
---

# SOLID Principes
#concept #design

## Doel van dit overzicht

Deze note groepeert de SOLID-principes zodat je sneller ziet hoe ze samen software onderhoudsvriendelijk, uitbreidbaar en begrijpelijk maken.

## Groot plaatje

SOLID is geen losse lijst van vijf slogans, maar een samenhangend denkkader voor objectgeoriënteerd ontwerp. De principes helpen je beslissen:
- hoe je verantwoordelijkheden splitst
- hoe je nieuw gedrag toevoegt zonder bestaande code te breken
- hoe afhankelijkheden beheersbaar blijven
- hoe interfaces en abstraheringen ontwerpkeuzes sturen

Deze map-note is dus een leerkaart van hoe de vijf principes samen een ontwerpfilosofie vormen.

## 1. Verantwoordelijkheid en cohesie

- [[S - Single Responsibility Principle]]

Dit principe helpt je begrijpen:
- waarom een klasse niet meerdere ongerelateerde redenen mag hebben om te wijzigen
- hoe hoge cohesie onderhoudbaarheid ondersteunt

## 2. Uitbreidbaarheid zonder breuk

- [[O - Open-Closed Principle]]

Deze groep gaat over:
- hoe je nieuw gedrag toevoegt zonder bestaande code aan te passen
- waarom abstracties en patterns belangrijk worden bij schaalbare software

## 3. Vervangbaarheid en contracten

- [[L - Liskov Substitution Principle]]

Dit principe gaat over:
- wanneer een subtype echt een geldig subtype is
- waarom erfelijkheid risico's meebrengt als contracten breken

## 4. Interface-ontwerp

- [[I - Interface Segregation Principle]]

Deze groep helpt je begrijpen:
- waarom te brede interfaces clients onnodig koppelen aan gedrag dat ze niet nodig hebben

## 5. Afhankelijkheden en abstractie

- [[D - Dependency Inversion Principle]]

Deze groep gaat over:
- waarom high-level code beter afhangt van abstracties dan van concrete implementaties
- hoe dit samenwerkt met OCP en testbaarheid

## 6. Vergelijking en uitvoering

- [[SRP vs OCP]]
- [[SRP Refactoring Worked Example]]

Deze notes helpen je:
- principes niet als losse definities te leren
- maar te zien hoe ze in ontwerpbeslissingen en refactorings terugkomen

## 7. Aanbevolen leerpad

1. [[S - Single Responsibility Principle]]
2. [[SRP Refactoring Worked Example]]
3. [[O - Open-Closed Principle]]
4. [[SRP vs OCP]]
5. [[L - Liskov Substitution Principle]]
6. [[I - Interface Segregation Principle]]
7. [[D - Dependency Inversion Principle]]

## 8. Link met de les

Deze concepten ondersteunen softwareontwerp, design patterns en examenvragen waarin je code moet beoordelen of refactoren volgens SOLID.

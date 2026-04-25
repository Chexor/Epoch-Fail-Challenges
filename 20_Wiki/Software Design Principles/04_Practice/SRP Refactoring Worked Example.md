---
type: practice
domain: "software-design-principles"
parent: "S - Single Responsibility Principle"
related:
  - O - Open-Closed Principle
  - D - Dependency Inversion Principle
theme: "maintainable-object-oriented-design"
aliases:
  - SRP Refactoring Worked Example
  - SRP Refactoring
---

# SRP Refactoring Worked Example
#concept #design

## Ondersteund concept
- [[S - Single Responsibility Principle]]

## Doel van deze uitwerking
Deze note toont hoe je een klasse met meerdere verantwoordelijkheden opsplitst in kleinere, meer coherente onderdelen.

## Context
Gebruik dit wanneer je een codevoorbeeld krijgt waarin UI-logica, metadata of businesslogica in dezelfde klasse samenkomen.

## Uitwerking
1. Identificeer de verschillende redenen waarom de klasse zou kunnen wijzigen.
2. Groepeer methodes en data per verantwoordelijkheid.
3. Splits de klasse op in aparte klassen met elk één duidelijke rol.
4. Controleer of elke nieuwe klasse nog een samenhangende taak heeft.

## Voor en na

```java
// Voor: 1 klasse met meerdere verantwoordelijkheden
class SuperDashboard {
  void renderUi() { }
  String getVersion() { return "1.0"; }
}

// Na: verantwoordelijkheden opgesplitst
class DashboardView {
  void renderUi() { }
}

class VersionInfo {
  String getVersion() { return "1.0"; }
}
```

## Wat toont dit voorbeeld?
- SRP is geen slogan, maar een concrete refactoringstrategie
- onderhoudbaarheid stijgt wanneer wijzigingsredenen uit elkaar gehaald worden

## Typische fouten
- te ver opsplitsen tot triviale klassen zonder duidelijke samenhang
- alleen methodes verplaatsen zonder de achterliggende verantwoordelijkheden scherp te analyseren

## Verwante concepten
- [[S - Single Responsibility Principle]]
- [[SRP vs OCP]]
- [[O - Open-Closed Principle]]

## Wat studeer je hierna?
- [[S - Single Responsibility Principle]]
- [[O - Open-Closed Principle]]
- [[SOLID Principes]]

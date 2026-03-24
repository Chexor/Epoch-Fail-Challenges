---
type: concept-comparison
domain: "software-design-principles"
parent: "SOLID Principes"
related:
  - S - Single Responsibility Principle
  - O - Open-Closed Principle
theme: "maintainable-object-oriented-design"
aliases:
  - SRP vs OCP
---

# SRP vs OCP
#concept #design

## Wat wordt hier vergeleken?
- [[S - Single Responsibility Principle]]
- [[O - Open-Closed Principle]]

## Kernverschil
SRP gaat over hoeveel verantwoordelijkheden een klasse draagt. OCP gaat over hoe je nieuw gedrag toevoegt zonder bestaande code te wijzigen. Het ene principe stuurt interne focus, het andere externe uitbreidbaarheid.

## Vergelijking

| Aspect | SRP | OCP |
| --- | --- | --- |
| Centrale vraag | heeft deze klasse 1 reden om te wijzigen? | kan ik gedrag uitbreiden zonder bestaande code te wijzigen? |
| Focus | cohesie | uitbreidbaarheid |
| Typisch probleem | te veel verantwoordelijkheden in 1 klasse | if/else of switch die blijft groeien |
| Typische oplossing | splitsen in gespecialiseerde klassen | abstraheren via interfaces/patterns |
| Typische fout | over-splitsen in triviale klassen | overal abstractie forceren zonder reden |

## Wanneer gebruik je wat?
- **SRP:** als code moeilijk te begrijpen is omdat één klasse te veel rollen combineert.
- **OCP:** als code regelmatig aangepast moet worden om nieuwe gevallen of gedrag toe te voegen.

## Waarom is dit onderscheid belangrijk?
Beide principes gaan over onderhoudbaarheid, maar op een ander niveau. Als je ze door elkaar haalt, refactor je code vaak in de verkeerde richting.

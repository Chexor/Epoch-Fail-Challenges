---
type: practice
domain: "artificial-intelligence"
parent: "IDA-star (Iterative Deepening A-star)"
related:
  - IDA-star (Iterative Deepening A-star)
  - A-star Search
  - Iterative Deepening Search (IDS)
  - f(n)
theme: "python-search-implementations"
aliases:
  - IDA-star Python Worked Example
  - IDA* Python Worked Example
---

# IDA-star Python Worked Example
#concept #ai

IDA-star Python Worked Example toont hoe je de kernintuïtie van `IDA*` implementeert met een iteratief stijgende `f`-grens.

## Korte kern

- combineert `f(n)` met depth-first uitbreiding
- bewaart geen volledige priority queue zoals `A*`
- verhoogt de grens op basis van de kleinste overschrijding

## Ondersteund concept
- [[IDA-star (Iterative Deepening A-star)]]

## Doel van deze uitwerking
Deze note toont een compacte Python-schets van `IDA*` zodat het verschil met `A*` en `IDS` beter zichtbaar wordt.

## Context
Gebruik dit als geheugensteun voor de kernmechaniek van `IDA*`, niet als productieklare implementatie.

## Codevoorbeeld
```python
def ida_threshold(path_cost, heuristic_value):
    return path_cost + heuristic_value


def next_ida_limit(exceeded_values):
    return min(exceeded_values) if exceeded_values else None
```

## Stap-voor-stap uitleg
- `f = g + h` bepaalt of een pad nog binnen de huidige grens valt
- paden boven de grens worden niet verder uitgebreid
- de kleinste overschrijding wordt de volgende grens
- daarna start een nieuwe depth-first ronde

## Verwachte output of gedrag
- deze schets toont vooral het limietidee, niet het volledige algoritme
- de essentie is dat `IDA*` op `f` limiteert, niet op diepte

## Uitwerking
1. Kies een beginlimiet op basis van de starttoestand.
2. Doorzoek depth-first alle paden met `f <= limiet`.
3. Verzamel overschrijdingen van die limiet.
4. Gebruik de kleinste overschrijding als nieuwe limiet.

## Wat toont dit voorbeeld?
- hoe `IDA*` tegelijk op geheugen bespaart en heuristische evaluatie behoudt
- waarom herhaling van nodes hier de prijs is voor lagere ruimtecomplexiteit

## Typische fouten
- `IDA*` behandelen alsof het gewoon `A*` met minder opslag is zonder limietlogica uit te schrijven
- denken dat de limiet over diepte gaat in plaats van over `f`

## Verwante concepten
- [[IDA-star (Iterative Deepening A-star)]]
- [[A-star Search]]
- [[Iterative Deepening Search (IDS)]]
- [[f(n)]]

## Begripsafbakening en verbanden
- **Kernonderscheid:** deze note geeft een didactische Python-schets van `IDA*`, niet een volledige optimale implementatie.
- **Veelvoorkomende misvatting:** denken dat `IDA*` vooral over diepte-limieten gaat; de echte grens ligt op `f(n)`.
- **Link met andere concepten:** [[IDA-star (Iterative Deepening A-star)]], [[A-star Search]], [[Iterative Deepening Search (IDS)]], [[f(n)]], [[g(n)]], [[h(n)]]

---
type: theory
domain: "computer-science"
parent:
related:
  - Data Representation
theme: "ordered-processing-and-selection"
aliases:
  - Ordered Processing and Selection
---

# Ordered Processing and Selection
#concept #cs

Ordered Processing and Selection groepeert datastructuren die bepalen in welke volgorde elementen verwerkt of geselecteerd worden.

## Korte kern

- vormt de kapstok voor `Queue`, `Stack` en `Priority Queue`
- legt uit hoe verwerkingsvolgorde gedrag bepaalt
- is belangrijk voor algoritmes die een frontier of wachtrij beheren

## 1. Wat is het kernprobleem?
Hoe bepaal je formeel welke informatie eerst verwerkt wordt wanneer meerdere elementen op verwerking wachten?

## 2. Intuitieve uitleg
Soms wil je het oudste element eerst nemen, soms het recentste, en soms het element met de hoogste prioriteit. De gekozen datastructuur bepaalt dus direct het gedrag van je algoritme.

## 3. Formele structuur
Belangrijke structuren in deze groep zijn:

- [[Queue]]
- [[Stack]]
- [[Priority Queue]]

Ze worden vaak gebruikt in algoritmes zoals:

- [[Breadth-First Search (BFS)]]
- [[Depth-First Search (DFS)]]
- [[Uniform-Cost Search (UCS)]]

## 4. Snelle vergelijking

- [[Queue]] = oudste element eerst
- [[Stack]] = recentste element eerst
- [[Priority Queue]] = element met beste prioriteit eerst

## 5. Toepassing
Bij zoekalgoritmes bepaalt precies deze keuze van datastructuur of je laag per laag, diep per diep, of kostgestuurd door een probleemruimte beweegt.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** deze note groepeert structuren op basis van verwerkingsvolgorde, niet op basis van datatype of geheugenrepresentatie.
- **Veelvoorkomende misvatting:** datastructuren beschouwen als neutrale opslag in plaats van als actieve keuzemechanismen.
- **Link met andere concepten:** [[Queue]], [[Stack]], [[Priority Queue]], [[Frontier]], [[Breadth-First Search (BFS)]], [[Depth-First Search (DFS)]], [[Uniform-Cost Search (UCS)]]

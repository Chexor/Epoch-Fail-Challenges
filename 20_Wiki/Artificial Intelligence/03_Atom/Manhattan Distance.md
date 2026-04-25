---
type: atom
domain: "artificial-intelligence"
parent: Heuristiek
related:
  - Heuristiek
  - Euclidean Distance
  - A-star Search
theme: "heuristic-types"
aliases:
  - Manhattan Distance
  - Manhattan afstand
---

# Manhattan Distance
#concept #ai #math

De Manhattan Distance (L1-norm) is een afstandsmaat die de som van de absolute verschillen van de cartesiaanse coördinaten berekent. Het meet de afstand tussen twee punten alsof je door een rechthoekig stratenpatroon (zoals in Manhattan) navigeert.

## Korte kern
- telt uitsluitend horizontale en verticale stappen
- formule: $|x_2 - x_1| + |y_2 - y_1|$
- is een perfecte **Admissible Heuristic** voor grid-problemen waar diagonaal bewegen niet is toegestaan

## 1. Wat is het kernprobleem?
Hoe schat je accuraat de afstand tussen twee punten in een rooster (grid) in, wanneer je alleen in rechte hoeken (Up, Down, Left, Right) mag bewegen?

## 2. Intuïtieve uitleg
Stel je bevindt je in New York City (Manhattan). Je staat op een kruispunt en moet naar een gebouw 3 blokken verder naar het noorden en 4 blokken verder naar het oosten. Je kunt niet dwars door de wolkenkrabbers steken (diagonale lijn). Je moet de straten volgen. De minimale afstand die je moet wandelen is dus 3 + 4 = 7 blokken. Dat is de Manhattan afstand.

## 3. Formele structuur
Voor twee punten $P = (x_1, y_1)$ en $Q = (x_2, y_2)$:
$$ d_{manhattan}(P,Q) = |x_2 - x_1| + |y_2 - y_1| $$

**Eigenschappen in AI (als heuristiek $h(n)$):**
- **Admissible:** In een grid waar obstakels kunnen staan, geeft deze formule de *absoluut kortst mogelijke weg* zonder obstakels. Zodra er een muur in de weg staat, wordt de werkelijke pad-kost groter. De formule zal de werkelijke kost dus **nooit overschatten**.
- **Consistent:** Een stap in eender welke toegelaten richting in het grid verandert de Manhattan afstand met exact 1. Dit betekent dat de schatting netjes meebeweegt met de werkelijke stapkosten ($c = 1$), waardoor de heuristiek monotoon is.

## 4. Toepassing in de praktijk
- **Pathfinding in Games / Doolhoven:** Als een unit in een grid-based map van start tot doel moet geraken en geen diagonalen mag gebruiken, wordt Manhattan distance gebruikt als $h(n)$ in het **A* algoritme**.
- **Sliding Puzzle (15-puzzle):** De heuristiek "som van de Manhattan-afstanden van alle tegels naar hun doelpositie" is de meest efficiënte heuristiek om dergelijke puzzels met A* op te lossen.
- **Machine Learning:** Wordt soms gebruikt als afstandsmetriek in algoritmes zoals **K-Nearest Neighbors (KNN)** wanneer de data robuuster moet zijn tegen outliers.

**Python implementatie:**
```python
def manhattan_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)
```

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** Manhattan staat geen diagonale stappen toe, Euclidean wel.
- **Veelvoorkomende misvatting:** Manhattan afstand gebruiken op een grid waar je wél schuin mag lopen; in dat geval overschat de Manhattan heuristiek de echte kost en is hij niet langer *admissible*!
- **Link met andere concepten:** [[Heuristic]], [[Euclidean Distance]], [[Admissible Heuristic]], [[A-star Search]], [[K-Nearest Neighbors (KNN)]]
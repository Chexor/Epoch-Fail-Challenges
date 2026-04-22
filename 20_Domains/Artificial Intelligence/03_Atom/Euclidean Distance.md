---
type: atom
domain: "artificial-intelligence"
parent: Heuristiek
related:
  - Heuristiek
  - Manhattan Distance
  - A-star Search
  - K-Nearest Neighbors (KNN)
theme: "heuristic-types"
aliases:
  - Euclidean Distance
  - Euclidische afstand
---

# Euclidean Distance
#concept #ai #math

De Euclidean Distance (L2-norm) is de "vogelvlucht"-afstand tussen twee punten. Het is de lengte van een rechte, directe lijn die twee coördinaten met elkaar verbindt.

## Korte kern
- meet de directe, kortst mogelijke afstand in rechte lijn ("hemelsbreed")
- formule: $\sqrt{(x_2 - x1)^2 + (y_2 - y_1)^2}$
- is altijd een **Admissible Heuristic** voor reizen tussen fysieke locaties, omdat de fysieke weg (over straten/paden) altijd minstens even lang of langer is

## 1. Wat is het kernprobleem?
Wat is de absoluut wiskundig minimale afstand tussen twee punten, ongeacht obstakels, wegen of grid-patronen?

## 2. Intuïtieve uitleg
Stel je moet van Brussel naar Antwerpen. Je kunt over de snelweg rijden met kronkels en afritten (werkelijke kost $g$). Maar je kunt ook de stelling van Pythagoras gebruiken en een perfect rechte lijn tekenen op een landkaart. De lengte van die rechte lijn over het papier, in theorie te vliegen door een vogel, is de Euclidische afstand.

In AI gebruiken we dit als heuristiek ($h$): als de vogelvlucht-afstand 40 kilometer is, zal je werkelijke reis via de kronkelende weg met de auto nooit korter zijn dan 40 km. Dus: de vogelvlucht onderschat de werkelijke kost veilig en is daardoor **Admissible**.

## 3. Formele structuur
Voor twee punten $P = (x_1, y_1)$ en $Q = (x_2, y_2)$ in een 2D vlak:
$$ d_{euclidean}(P,Q) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} $$

Voor $n$-dimensionale data:
$$ d_{euclidean}(P,Q) = \sqrt{\sum_{i=1}^{n} (x_{2i} - x_{1i})^2} $$

**Eigenschappen in AI (als heuristiek $h(n)$):**
- **Admissible:** Omdat een schuine lijn (hypotenusa) tussen twee punten de kortst denkbare verbinding is, zal $h(n)$ nooit de reële grafen-afstand $h^*(n)$ overschrijden. Zelfs als er wegen zijn in elke mogelijke hoek, zal je minimaal de Euclidische afstand afleggen.
- **Consistent:** Zelfs als je een andere stad langs de route aandoet, garandeert de driehoeksongelijkheid (driehoeksvoorwaarde) dat $d_{A,C} \le d_{A,B} + d_{B,C}$. 

## 4. Toepassing in de praktijk
- **Routeplanning / Pathfinding in continue ruimte:** In games waar characters vrij in elke hoek (360 graden) mogen bewegen of waar het pad een werkelijke landkaart is, is Euclidean de ideale heuristiek voor het **A* algoritme**.
- **Machine Learning (Clustering):** In **K-Means** clustering is het de standaard afstandsmeting om te zien welk datapunt tot welke 'centroid' behoort.
- **Machine Learning (Classificatie):** Bij **K-Nearest Neighbors (KNN)** is Euclidean distance de meest voorkomende metriek om "dichtbij" te definiëren voor continue variabelen (features).

**Python implementatie:**
```python
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
```

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** Euclidean is de stelling van Pythagoras (rechte schuine lijn), Manhattan is navigeren langs een hoekig blokpatroon (haakse hoeken).
- **Relatie tot elkaar:** De Euclidean distance is **altijd $\le$** aan de Manhattan distance tussen dezelfde twee punten. Daardoor is Euclidean altijd "veiliger" (admissible), maar vaak minder informatief (het geeft een lagere $h(n)$) als je eigenlijk verplicht bent langs assen te bewegen.
- **Link met andere concepten:** [[Heuristic]], [[Manhattan Distance]], [[Admissible Heuristic]], [[A-star Search]], [[K-Nearest Neighbors (KNN)]], [[K-Means]]
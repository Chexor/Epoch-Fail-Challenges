# Samenvatting Topic 6: Heuristic Search (Geactualiseerd)

In dit topic stappen we over van "blind" zoeken naar "geïnformeerd" zoeken door gebruik te maken van domeinkennis.

## 1. Het Kernprobleem (Big Picture)
De zoekruimte voor veel problemen is te groot om volledig te doorzoeken (combinatorische explosie). Hoe kunnen we domeinkennis gebruiken om de zoektocht te sturen, zodat we directer op ons doel afgaan?

## 2. De Intuïtie
- **Zonder Heuristiek**: Je zoekt in een donkere kamer naar de deur door willekeurig rond te tasten.
- **Met Heuristiek**: Je ziet een klein streepje licht onder de deur. Dat licht is je **heuristiek**. Je loopt in de richting van het licht, ook al ken je de exacte weg nog niet.

## 3. Formele Structuur: De Heuristische Functie $h(n)$
Een heuristiek $h(n)$ is een schatting van de kosten van de huidige node $n$ naar het doel.
- $h(n) = 0$ bij het doel.
- **Greedy Best-First Search**: Kiest de node met de laagste $h(n)$. Is snel maar niet altijd optimaal.
- **A* Search**: Combineert de kosten tot nu toe ($g(n)$) met de schatting ($h(n)$): **$f(n) = g(n) + h(n)$**.

## 4. Praktische Toepassingen (Maze & Puzzel)
In de notebooks (zie `topic 6 - maze_heuristic_search.ipynb`):
- **Manhattan Distance**: De som van horizontale en verticale afstanden naar het doel. Ideaal voor grids waar je alleen in 4 richtingen mag bewegen.
- **Euclidean Distance**: De vogelvluchtafstand (rechte lijn).
- **Misplaced Tiles**: Bij de 8-puzzel, het aantal tegels dat niet op de juiste positie ligt.

### Waarom Heuristieken werken in de Maze:
In plaats van elke gang in het doolhof in te gaan (zoals BFS/DFS), geeft de heuristiek prioriteit aan gangen die fysiek dichter bij de uitgang liggen. Dit vermindert het aantal nodes dat het algoritme moet verkennen aanzienlijk.

## 5. Examengerichte Focus
- **Admissibility (Toelaatbaarheid)**: Een heuristiek is admissible als hij de werkelijke kosten *nooit overschat*. Dit is cruciaal voor de optimaliteit van A*.
- **Consistency**: De schatting mag niet sneller dalen dan de werkelijke stapkosten.
- **Dominantie**: Als $h_2(n) \ge h_1(n)$ voor alle $n$, dan is $h_2$ efficiënter (dominant) omdat het de zoekruimte sterker inperkt.

---
*Samenvatting geactualiseerd op basis van de praktische implementaties van Manhattan en Euclidean afstanden.*

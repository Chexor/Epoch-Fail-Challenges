# Samenvatting Topic 4: Blind Search (Geactualiseerd)

Dit topic behandelt zoekstrategieën die geen domeinkennis gebruiken om het doel te vinden (Uninformed Search).

## 1. Het Kernprobleem (Big Picture)
Hoe vinden we een pad naar het doel als we alleen weten wat de mogelijke acties zijn, maar niet hoe ver we nog van het doel verwijderd zijn? Het probleem is hoe we de zoekruimte systematisch kunnen verkennen zonder in lussen te raken of oneindig door te zoeken.

## 2. De Intuïtie
- **BFS (Breadth-First)**: Zoeken in "lagen". Je bekijkt eerst alle directe buren, dan de buren van buren, enzovoort. Denk aan een rimpel in het water die zich verspreidt.
- **DFS (Depth-First)**: Zoeken in "gangen". Je kiest één pad en volgt dat tot je niet verder kunt, dan keer je terug (backtracking) en probeert een ander pad. Denk aan een ontdekkingsreiziger in een grot.

## 3. Formele Structuur: De Algoritmen

### A. Breadth-First Search (BFS)
- **Data Structuur**: Gebruikt een **Queue** (FIFO: First-In, First-Out).
- **Eigenschappen**: Vindt altijd het pad met de *minste stappen* (optimaal als alle stappen dezelfde kosten hebben).
- **Nadeel**: Gebruikt veel geheugen om alle nodes op het huidige niveau te onthouden.

### B. Depth-First Search (DFS)
- **Data Structuur**: Gebruikt een **Stack** (LIFO: Last-In, First-Out).
- **Eigenschappen**: Ruimte-efficiënt (onthoudt alleen het huidige pad).
- **Nadeel**: Kan vastlopen in oneindige paden en vindt niet noodzakelijk het kortste pad.

### C. Uniform Cost Search (UCS)
- **Data Structuur**: Gebruikt een **Priority Queue**.
- **Eigenschappen**: Breidt de node uit met de laagste cumulatieve padkosten ($g(n)$). Optimaal voor variabele stapkosten.

## 4. Praktische Toepassing: De Maze Notebook
In de praktijk (zie `topic 4 - maze_DFS_BFS.ipynb`):
- **BFS in de Maze**: De rimpel-aanpak zorgt ervoor dat we altijd de kortste weg uit het doolhof vinden.
- **DFS in de Maze**: De verkenner-aanpak kan een heel lange omweg maken, maar gebruikt minder geheugen.
- **Loop Detection**: Het is essentieel om bij te houden welke locaties al in het huidige pad zitten (via de `Path` klasse) om te voorkomen dat het algoritme rondjes blijft draaien.

## 5. Examengerichte Focus
- **Compleetheid**: BFS is compleet (vindt altijd een oplossing als die bestaat); DFS is alleen compleet in eindige ruimtes zonder lussen.
- **Optimaliteit**: BFS is optimaal voor ongewogen grafen; UCS voor gewogen grafen.
- **Tijd- en Ruimtecomplexiteit**: Begrijp de exponentiële groei $O(b^d)$ en waarom geheugen vaak de beperkende factor is voor BFS.

---
*Samenvatting geactualiseerd op basis van de praktische Maze-simulaties.*

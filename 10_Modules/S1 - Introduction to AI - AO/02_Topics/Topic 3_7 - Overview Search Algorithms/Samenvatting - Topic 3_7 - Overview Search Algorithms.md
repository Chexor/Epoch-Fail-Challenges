# Samenvatting Topic 3-7: Overview Search Algorithms

Dit topic biedt een overkoepelend overzicht en vergelijking van de verschillende zoekalgoritmen die in de voorgaande hoofdstukken zijn behandeld.

## 1. Het Kernprobleem (Big Picture)
Er bestaat geen "one size fits all" algoritme voor zoekproblemen. De uitdaging is om het juiste algoritme te kiezen op basis van de eigenschappen van het probleem: is de zoekruimte groot of klein? Zijn de stapkosten gelijk of variabel? Hebben we een goede heuristiek beschikbaar?

## 2. De Intuïtie (De "Zoek-Hiërarchie")
- **Blind (Uninformed)**: Je hebt geen kaart en geen kompas (BFS, DFS, UCS).
- **Heuristisch (Informed)**: Je hebt een kompas dat wijst naar het doel (Greedy, A*).
- **Optimaal**: Je hebt de garantie dat je niet alleen het doel vindt, maar ook de goedkoopste route (UCS, A* met admissible heuristiek).

## 3. Formele Vergelijkingstabel

| Algoritme | Strategie | Compleet? | Optimaal? | Tijd | Ruimte |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **BFS** | Lagen (Queue) | Ja | Ja* | $O(b^d)$ | $O(b^d)$ |
| **DFS** | Diepte (Stack) | Nee** | Nee | $O(b^m)$ | $O(bm)$ |
| **UCS** | Kosten ($g$) | Ja | Ja | $O(b^{C^*/\epsilon})$ | $O(b^{C^*/\epsilon})$ |
| **Greedy** | Schatting ($h$) | Nee | Nee | $O(b^m)$ | $O(b^m)$ |
| **A\*** | $g + h$ | Ja | Ja | Exponentieel | Exponentieel |

*\*Optimaal als alle stapkosten gelijk zijn.*
*\*\*Alleen compleet in eindige ruimtes zonder lussen.*

## 4. Belangrijke Concepten voor de Keuze
- **Backtracking**: Gebruikt in DFS om terug te keren van doodlopende wegen.
- **Iterative Deepening (IDS)**: Combineert de voordelen van BFS (optimaliteit) en DFS (ruimte-efficiëntie).
- **Heuristische Kwaliteit**: Hoe dichter $h(n)$ bij de werkelijke kosten komt, hoe minder nodes A* hoeft te verkennen.

## 5. Examengerichte Focus
- **Algoritme Herkenning**: Gegeven een scenario, welk algoritme is het meest geschikt?
- **Eigenschappen**: Ken de tabel uit je hoofd (Compleet/Optimaal).
- **Trade-offs**: Begrijp de afweging tussen rekentijd en geheugengebruik.

---
*Dit overzicht vormt de synthese van de leerstof over zoekalgoritmen uit de eerste helft van de cursus.*

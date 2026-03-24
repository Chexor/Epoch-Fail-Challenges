---
type: concept-comparison
domain: Artificial Intelligence
parent: "[[10_Modules/S1 - Introduction to AI - AO/00_Module_Overzicht|Introduction to AI]]"
related: ["[[Samenvatting - Topic 4 - Blind Search]]"]
big_picture: "Het vergelijken van verschillende 'blind search' (uninformed) algoritmen om te bepalen welk algoritme het meest geschikt is voor een specifiek probleem op basis van compleetheid, optimaliteit en complexiteit."
---

# Samenvatting - Topic 5a - Vergelijking van Algoritmen
#concept #AI #SearchAlgorithms

## 1. Big Picture / Probleem
Bij het oplossen van problemen via zoekalgoritmen zonder domeinkennis (blind search) is het cruciaal om te weten welk algoritme de oplossing vindt, of die oplossing de beste is, en hoeveel middelen (tijd en geheugen) dit kost. Er is vaak een trade-off tussen **geheugengebruik** en **optimaliteit**.

## 2. Intuïtie
Stel je voor dat je een sleutel zoekt in een groot hotel:
- **BFS:** Je controleert elke kamer op de eerste verdieping, dan de tweede, enzovoort (je vindt de dichtstbijzijnde sleutel, maar moet veel onthouden).
- **DFS:** Je kiest één gang en blijft deuren openen tot je niet verder kunt (je onthoudt weinig, maar kunt in een eindeloze gang verdwalen).
- **IDS:** Je kiest een gang tot 1 verdieping diep, dan tot 2, enzovoort (je combineert de veiligheid van BFS met de efficiëntie van DFS).

## 3. Formele Structuur (Vergelijkingstabel)

| Algoritme | Compleet? | Optimaal? | Tijdcomplexiteit | Ruimtecomplexiteit |
| :--- | :--- | :--- | :--- | :--- |
| **BFS** | Ja¹ | Ja² | $O(b^d)$ | $O(b^d)$ |
| **DFS** | Nee³ | Nee | $O(b^m)$ | $O(bm)$ |
| **UCS** | Ja⁴ | Ja | $O(b^{1 + \lfloor C^*/\epsilon \rfloor})$ | $O(b^{1 + \lfloor C^*/\epsilon \rfloor})$ |
| **DLS** | Nee⁵ | Nee | $O(b^l)$ | $O(bl)$ |
| **IDS** | Ja¹ | Ja² | $O(b^d)$ | $O(bd)$ |

*Legenda:*
- $b$: Branching factor (aantal vertakkingen per node).
- $d$: Diepte van de ondiepste oplossing.
- $m$: Maximale diepte van de zoekruimte.
- $l$: Dieptelimiet (bij DLS).
- ¹ Mits $b$ eindig is.
- ² Mits alle stapkosten gelijk zijn.
- ³ Faalt in oneindige ruimtes of bij lussen.
- ⁴ Mits stapkosten > 0.
- ⁵ Alleen compleet als $l \ge d$.

## 4. Praktische Toepassing: Wanneer gebruik je wat?

### **Breadth-First Search (BFS)**
- **Gebruik:** Als de oplossing ondiep is en geheugen geen probleem vormt.
- **Nadeel:** Het geheugenverbruik groeit exponentieel ($O(b^d)$), wat vaak de beperkende factor is.

### **Depth-First Search (DFS)**
- **Gebruik:** Als de zoekruimte erg diep is en je heel weinig geheugen hebt.
- **Nadeel:** Kan vastlopen in oneindige paden en vindt niet noodzakelijk de kortste route.

### **Uniform-Cost Search (UCS)**
- **Gebruik:** Wanneer padkosten variëren (bijv. Google Maps met verschillende snelheden per weg).
- **Kenmerk:** Breidt altijd de node met de laagste cumulatieve kosten uit.

### **Iterative Deepening Search (IDS)**
- **Gebruik:** De **gouden standaard** voor blind search in grote zoekruimtes.
- **Voordeel:** Heeft de geheugenefficiëntie van DFS ($O(bd)$) en de compleetheid/optimaliteit van BFS. De extra tijd om bovenliggende nodes opnieuw te genereren is verwaarloosbaar.

## 5. Examengerichte Focus
- Begrijp waarom BFS een groter probleem heeft met **geheugen** dan met tijd.
- Begrijp waarom IDS ondanks het 'dubbele werk' toch efficiënt is (de meeste nodes zitten in de onderste laag).
- Kunnen bepalen welk algoritme optimaal is in een specifieke graaf met variërende kosten (UCS).

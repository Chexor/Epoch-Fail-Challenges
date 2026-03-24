---
type: concept
domain: Artificial Intelligence
parent: "[[10_Modules/S1 - Introduction to AI - AO/00_Module_Overzicht|Introduction to AI]]"
related: ["[[Samenvatting - Topic 4 - Blind Search]]", "[[Samenvatting - Topic 5a - Vergelijking van Algoritmen]]"]
big_picture: "Het optimaliseren van blind search door redundante paden te vermijden (Graph Search) en de zoekruimte van twee kanten tegelijk te verkennen (Bi-directional Search)."
---

# Samenvatting - Topic 5b - Blind Search 2
#concept #AI #SearchAlgorithms #GraphSearch

## 1. Big Picture / Probleem
Zelfs de beste blind search algoritmen (zoals IDS) kunnen falen in complexe omgevingen door twee grote problemen:
1. **Herhaalde statussen (Repeated States):** In een graaf kun je via verschillende paden in dezelfde status terechtkomen of zelfs in lussen (cycles) belanden.
2. **Exponentiële groei:** Bij een grote diepte $d$ wordt de zoekboom te groot voor BFS of UCS.

## 2. Intuïtie
- **Graph Search:** Stel je voor dat je een doolhof verkent en met krijt een kruis zet op elke splitsing waar je al bent geweest. Je gaat nooit een gang in die al gemarkeerd is. Dit voorkomt dat je rondjes blijft lopen.
- **Bi-directional Search:** Stel je voor dat twee mensen elkaar zoeken in een stad. In plaats van dat één persoon de hele stad afzoekt, vertrekken ze beiden (één vanaf start, één vanaf het doel) en lopen ze naar elkaar toe. Ze ontmoeten elkaar in het midden, wat veel minder stappen kost.

## 3. Formele Structuur

### A. Graph Search vs. Tree Search
Het kernverschil is het bijhouden van bezochte statussen.

- **Tree Search:** Verkent elke tak, ook als die naar een bekende status leidt.
- **Graph Search:** Gebruikt een **Explored Set** (of *Closed List*).
    1. Voeg de `initial state` toe aan de `frontier`.
    2. Kies een node uit de `frontier` om uit te breiden.
    3. **Check:** Is de status al in de `explored set`?
        - **Ja:** Negeer de node.
        - **Nee:** Breid uit en voeg de status toe aan de `explored set`.

### B. Bi-directional Search
Zoekt gelijktijdig vanaf de **Start ($S$)** en het **Doel ($G$)**.

- **Terminatie:** De zoektocht stopt wanneer de fronten (grenzen) van beide zoektochten elkaar raken.
- **Complexiteit:** 
    - **Tijd:** $O(b^{d/2})$ (In plaats van $O(b^d)$). Dit is een enorme tijdwinst!
    - **Ruimte:** $O(b^{d/2})$ (Minstens één front moet in het geheugen blijven voor de intersection check).

| Kenmerk | Tree Search | Graph Search | Bi-directional |
| :--- | :--- | :--- | :--- |
| **Geheugen** | Laag | Hoog (Explored Set) | Medium ($O(b^{d/2})$) |
| **Lussen** | Kan oneindig lopen | Veilig | Veilig (indien BFS) |
| **Efficiëntie** | Laag | Hoog | Zeer Hoog |

## 4. Praktische Toepassing & Beperkingen

### Wanneer Bi-directional Search lastig is:
1. **Meerdere doelen:** Als het doel niet één specifieke status is (bijv. "elke status waar de koningin veilig is"), is het lastig om 'achteruit' te zoeken.
2. **Omkeerbaarheid:** De acties moeten omkeerbaar zijn ($Predecessors$ berekenen). In schaken is dit makkelijk, in andere problemen soms onmogelijk.
3. **Intersection Check:** Het constant vergelijken of een nieuwe node in de andere frontier zit, vereist snelle datastructuren (Hashtables).

## 5. Examengerichte Focus
- Kunnen uitleggen waarom **Graph Search** essentieel is om oneindige lussen te voorkomen in DFS.
- Het concept van de **Explored Set** kunnen toepassen in een handmatige trace van een algoritme.
- Begrijpen waarom de tijdcomplexiteit van Bi-directional search $O(b^{d/2})$ is (de exponent wordt gehalveerd).
- De nadelen van Bi-directional search kennen (moeilijk bij onduidelijke doelen).

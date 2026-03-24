# Samenvatting Topic 3: State-spaced Representation (Geactualiseerd)

Dit topic behandelt de abstracte modellering van problemen zodat ze door zoekalgoritmen opgelost kunnen worden.

## 1. Het Kernprobleem (Big Picture)
Hoe vertalen we een complex probleem in de echte wereld (zoals een doolhof of een puzzel) naar een wiskundige vorm die een computer kan begrijpen? We hebben een gestructureerde manier nodig om de "toestand" van de wereld en de toegestane "acties" te beschrijven.

## 2. De Intuïtie
Stel je een schaakbord voor.
- De **State** is de huidige positie van alle stukken op het bord.
- De **Initial State** is de beginopstelling.
- De **Actions** (Production Rules) zijn de regels die bepalen hoe elk stuk mag bewegen.
- De **Goal Test** is de vraag: "Staat de koning schaakmat?"

## 3. Formele Structuur: De 5 Componenten
Een zoekprobleem bestaat uit:
1.  **Initial State**: Waar beginnen we? (Bijv. coördinaat (2,2) in een doolhof).
2.  **Actions**: Welke zetten zijn mogelijk? (Bijv. `Left`, `Right`, `Up`, `Down`).
3.  **Transition Model**: Wat is het resultaat van een actie? (Huidige positie + zet = nieuwe positie).
4.  **Goal Test**: Is de huidige state de gewenste eindtoestand?
5.  **Path Cost**: Wat "kost" het om daar te komen? (Bijv. aantal stappen of afgelegde afstand).

## 4. Praktische Implementatie (Python OO-model)
In de notebooks wordt een Object-Oriented (OO) model gebruikt:
- **`Position` klasse**: Slaat coördinaten op `(irow, icol)`.
- **`Path` klasse**: Houdt een lijst van posities bij die reeds bezocht zijn.
- **`Maze` klasse**: Definieert het grid met muren (`#`), vrije paden (`.`), start (`*`) en doel (`o`).
- **`State` klasse**: De kern van het model. Bevat de methoden:
    - `calculate_moves()`: Berekent welke zetten geldig zijn (niet door muren, niet terug op het eigen pad).
    - `apply_move()`: Creëert een nieuwe state na een zet.
    - `is_goal()`: Checkt of we bij `o` zijn aangekomen.

### Voorbeelden:
- **Maze (Doolhof)**: Navigeren van start naar doel zonder muren te raken.
- **Sliding Puzzle (8-puzzle)**: Tegels schuiven naar een specifieke doelconfiguratie.
- **Ganzenbord**: Een pion verplaatsen op basis van dobbelsteenworpen (production rules), rekening houdend met putten (pitfalls).

## 5. Examengerichte Focus
- **Abstractie**: Kunnen uitleggen waarom we details weglaten (bijv. de kleur van de muren in een doolhof doet er niet toe voor het zoekalgoritme).
- **State Space Graph vs. Search Tree**: Een graaf toont alle mogelijke toestanden en hun verbindingen; een boom toont de paden die een algoritme verkent.
- **Validiteit**: Begrijpen waarom een zet soms ongeldig is (bijv. buiten het bord gaan of tegen een muur lopen).

---
*Deze samenvatting is geactualiseerd op basis van de praktische implementaties in Python.*

---
type: theory
domain: "artificial-intelligence"
parent:
  - "[[Heuristic Search Algorithms]]"
related:
  - "[[Greedy Best-First Search]]"
  - "[[Hill Climbing]]"
theme: "ai-search"
aliases:
  - Greedy Search
---

# Greedy Search
#concept #ai

Greedy Search is een algemene aanpak binnen heuristische zoekalgoritmes die op elk punt in het zoekproces de lokaal meest optimale of veelbelovende keuze maakt, in de hoop dat een reeks van lokale optima tot een globaal goede oplossing leidt.

## Korte kern

-   Maakt op elk moment de keuze die er *nu* het best uitziet.
-   Gebruikt een heuristiek om "het beste" te bepalen.
-   Is vaak snel en efficiënt, maar niet gegarandeerd optimaal.

## Probleem

Hoe kunnen we snel een oplossing vinden voor een complex probleem door het op te splitsen in een reeks van simpele, kortzichtige beslissingen?

## Intuïtie

Stel je voor dat je op een berg staat en zo snel mogelijk naar beneden wilt. Bij elke stap kies je de richting die het steilst naar beneden gaat. Dit is een "greedy" aanpak. Het brengt je snel omlaag, maar je kunt vast komen te zitten in een dalletje (een lokaal minimum) dat niet het laagste punt van het hele gebied is. Je hebt de lokale beste keuze gemaakt, maar daarmee de globaal beste route misschien uitgesloten.

## Toepassing

-   **Padvinding:** [[Greedy Best-First Search]] voor snelle, maar niet-optimale routes.
-   **Optimalisatie:** Het "Change-making problem" (wisselgeld teruggeven met zo min mogelijk munten).
-   **Graaf-algoritmes:** Dijkstra's, Prim's, Kruskal's algoritme.

## Formeel

Greedy search is een strategie, geen enkel specifiek algoritme, maar het wordt het vaakst geïmplementeerd in padvind-algoritmes en optimalisatieproblemen.

-   **Heuristiek:** De kern van de greedy aanpak is de heuristische functie die bepaalt welke keuze "lokaal optimaal" is.
-   **Implementaties:**
    -   **[[Greedy Best-First Search]]:** De meest bekende implementatie in het kader van padvinding. Het gebruikt `h(n)` (geschatte afstand tot doel) als de enige maatstaf om de frontier te doorzoeken. `f(n) = h(n)`.
    -   **[[Hill Climbing]]:** Een lokale zoekvariant die geen geheugen van vorige stappen bijhoudt. Het kijkt alleen naar de directe buren en kiest de beste.
    -   **Klassieke algoritmes:** Algoritmes zoals Dijkstra's (voor kortste paden) en Prim's (voor minimum spanning trees) hebben een "greedy" karakter omdat ze bij elke stap de lokaal beste rand of node toevoegen. In deze gevallen leidt de greedy strategie toevallig wél tot een globaal optimum.

## Eigenschappen

-   **Snelheid:** Omdat er geen complexe afwegingen worden gemaakt over de toekomst of het verleden, zijn greedy algoritmes vaak erg snel.
-   **Optimaliteit:** Greedy algoritmes zijn zelden globaal optimaal. De uitzonderingen (zoals Dijkstra) zijn problemen met een specifieke wiskundige structuur (de "greedy choice property" en "optimal substructure").
-   **Kortzichtigheid:** De belangrijkste zwakte. Een keuze die nu goed lijkt, kan later tot een doodlopend spoor of een suboptimale oplossing leiden.

---
type: theory
domain: "artificial-intelligence"
parent:
  - "[[Heuristic Search Algorithms]]"
related:
  - "[[Greedy Best-First Search]]"
  - "[[Breadth-First Search (BFS)]]"
theme: "ai-search"
aliases:
  - Beam Search
---

# Beam Search
#concept #ai

Beam Search is een heuristisch zoekalgoritme dat een geoptimaliseerde variant is van Best-First Search, waarbij op elk niveau van de zoekboom slechts een beperkt aantal (`k`) van de meest veelbelovende kandidaten wordt behouden om de geheugencomplexiteit te reduceren.

## Korte kern

-   Een variant van [[Greedy Best-First Search]] met een limiet.
-   Behoudt op elk niveau een vaste `beam width` (`k`) van de beste nodes.
-   Is niet compleet en niet optimaal, maar geheugen-efficiënt.

## Probleem

Traditionele Best-First search algoritmes kunnen een [[Frontier]] hebben die exponentieel groeit, wat leidt tot een hoog geheugenverbruik. Hoe kunnen we de zoektocht sturen en tegelijkertijd het geheugenverbruik onder controle houden?

## Intuïtie

Stel je voor dat je meedoet aan een talentenjacht. In de eerste ronde treden 1000 kandidaten op. In plaats van ze allemaal door te laten gaan naar de volgende ronde (zoals BFS zou doen met een groeiende frontier), selecteert de jury alleen de top 10 (de "beam width" k=10). In de volgende ronde worden alleen de optredens van deze 10 kandidaten geëvalueerd, en opnieuw gaan alleen de beste 10 door. Dit proces herhaalt zich. Het risico is dat een kandidaat die in het begin zwak presteerde maar later briljant zou zijn, vroegtijdig wordt geëlimineerd.

## Toepassing

Beam Search wordt vaak gebruikt in systemen waar de zoekruimte extreem groot is en een "goede" oplossing voldoende is, ook al is deze niet perfect.
-   **Natural Language Processing (NLP):** Bij machine translation of speech recognition om de meest waarschijnlijke zinnen te genereren zonder alle mogelijke woordcombinaties te moeten exploreren.
-   **Computer Vision:** Bij object tracking.

## Formeel

Beam Search is een vorm van Best-First Search, maar met een aangepast frontier management.

-   **Beam Width (k):** De belangrijkste parameter. Dit is het maximale aantal nodes dat op elk niveau wordt bewaard.
-   **Process:**
    1.  Start met de initiële state.
    2.  Genereer alle opvolgers van de huidige set kandidaten.
    3.  Evalueer alle gegenereerde opvolgers met een heuristiek `h(n)`.
    4.  Selecteer de `k` beste opvolgers. De rest wordt permanent verworpen.
    5.  Herhaal vanaf stap 2 met de nieuwe set van `k` kandidaten, totdat een doel is gevonden of er geen kandidaten meer zijn.

-   **Eigenschappen:**
    -   **Niet compleet:** Als de oplossing buiten de "beam" valt, wordt deze nooit gevonden.
    -   **Niet optimaal:** Een suboptimaal pad kan er in het begin veelbelovender uitzien en de optimale weg uit de beam duwen.
    -   **Geheugen:** De frontier-grootte is beperkt, wat het grootste voordeel is.

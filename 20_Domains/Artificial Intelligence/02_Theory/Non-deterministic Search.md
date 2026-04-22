---
type: theory
domain: "artificial-intelligence"
parent:
  - "[[Blind Search Algorithms]]"
related:
  - "[[State Space]]"
theme: "ai-search"
aliases:
  - Nondeterministic Search
---

# Non-deterministic Search
#concept #ai

Non-deterministic Search behandelt zoekproblemen in omgevingen waar acties onvoorspelbare uitkomsten kunnen hebben, waardoor een pad geen vaste sequentie van states meer is, maar een strategie of plan om met eventualiteiten om te gaan.

## Korte kern

-   Acties kunnen leiden tot meerdere mogelijke uitkomsten.
-   Het doel is niet een pad, maar een *plan* dat werkt voor *elke* mogelijke uitkomst.
-   De state space wordt een AND-OR graaf.

## Probleem

Hoe vind je een pad naar een doel als je niet zeker weet wat het resultaat van je acties zal zijn? Denk aan een robot die een glad object probeert op te pakken; het kan lukken, of het object kan vallen.

## Intuïtie

Stel je voor dat je een game speelt waarin een dobbelsteen wordt geworpen elke keer als je een deur opent. Je kunt niet plannen "ga links, dan rechts, dan rechtdoor". In plaats daarvan moet je een plan hebben zoals: "Probeer de linker deur. *Als* er een monster is, ga terug en neem de rechter deur. *Als* de kamer leeg is, ga rechtdoor." Je zoekt naar een strategie die je naar het doel leidt, ongeacht de worp van de dobbelsteen.

## Toepassing

-   **Robotica:** Een robotarm die een object moet grijpen dat kan wegglippen.
-   **Spellen:** Spellen met een kans-element, zoals het gooien van een dobbelsteen.
-   **Internet:** Communiceren over een onbetrouwbaar netwerk waar pakketjes verloren kunnen gaan.

## Formeel

In een deterministische wereld ga je van state naar state. In een non-deterministische wereld ga je van een state naar een *set* van mogelijke states.

-   **State Space:** De zoekruimte is geen simpele graaf meer, maar een **AND-OR graaf**.
    -   **OR-nodes:** Staan voor de keuzes die de agent kan maken (bv. kies actie A of actie B).
    -   **AND-nodes:** Staan voor de oncontroleerbare uitkomsten van een actie (bv. actie A leidt tot state X *en* Y *en* Z, en je moet een plan hebben voor allemaal).
-   **Oplossing:** Een oplossing is een subgraaf van de AND-OR graaf die voor elke mogelijke eventualiteit een pad naar het doel bevat. Dit wordt ook wel een *contingent plan* of *strategie* genoemd.
-   **Algoritme:** Een typisch algoritme doorzoekt de AND-OR graaf recursief. Een node is oplosbaar als:
    -   Het een doelstate is.
    -   Het een OR-node is met minstens één oplosbare opvolger.
    -   Het een AND-node is waarvan *alle* opvolgers oplosbaar zijn.

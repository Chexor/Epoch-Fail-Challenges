# H7 - Recurrente betrekkingen

[[Problem Solving 2 - Overzicht]]

## A. Wat is het kernprobleem?

Sommige processen laten zich het best beschrijven door een "stap-voor-stap" formule: de volgende toestand hangt af van de vorige. Denk aan de groei van een konijnenpopulatie (Fibonacci), of de afbetaling van een lening. Zo'n stap-voor-stap formule heet een **recurrente betrekking** (of differentievergelijking).

Het probleem is dat zo'n recursieve formule onhandig is. Om de 100ste term te kennen, moet je eerst alle 99 voorgaande termen uitrekenen. Het doel is om een **directe, expliciete formule** te vinden waarmee je de `n`-de term kan berekenen zonder de vorige te kennen.

## B. Intuïtieve uitleg

Je hebt een recept dat zegt: "Neem wat je gisteren had, en doe er 2 bij". Als je op dag 0 met 10 begon, weet je:
-   Dag 1: 12
-   Dag 2: 14
-   Dag 3: 16

Dit is de **recursieve** manier. Het is makkelijk om de volgende stap te zetten, maar vervelend als ik wil weten wat je op dag 200 hebt.

De **expliciete** formule is wat je zoekt. In dit geval is dat simpel: `Waarde(n) = 10 + 2*n`. Nu kan je direct de waarde op dag 200 berekenen: `10 + 2*200 = 410`.

Dit hoofdstuk geeft je een methode om van die eerste, recursieve vorm naar de tweede, directe vorm te gaan voor een specifieke klasse van problemen.

## C. Formele structuur

We focussen enkel op **lineaire recurrente betrekkingen van orde 2 met constante coëfficiënten**. Dit is de standaardvorm:
`an = c1 * a(n-1) + c2 * a(n-2)`

Voorbeeld (Fibonacci): `F(n) = 1 * F(n-1) + 1 * F(n-2)`.

### Het stappenplan om de expliciete formule te vinden:

1.  **Stel de Karakteristieke Vergelijking op.**
    Dit is de sleutel. Vervang `an` door `r²`, `a(n-1)` door `r`, en `a(n-2)` door `1`.
    `r² = c1*r + c2`  ofwel  **`r² - c1*r - c2 = 0`**.

2.  **Los de Karakteristieke Vergelijking op.**
    Dit is een gewone vierkantsvergelijking. Zoek de wortels `r1` en `r2`. Er zijn drie mogelijkheden:

    *   **Case 1: Twee verschillende reële wortels (D > 0)**
        De algemene oplossing is:
        `an = α1 * (r1)^n + α2 * (r2)^n`

    *   **Case 2: Eén dubbele reële wortel (D = 0)**
        De algemene oplossing is:
        `an = α1 * r^n + α2 * n * r^n` (Let op de extra `n` in de tweede term!)

    *   **Case 3: Twee complexe wortels (D < 0)**
        Dit geval wordt in de syllabus enkel kort vermeld en is minder belangrijk voor de oefeningen.

3.  **Vind de constanten α1 en α2.**
    De "algemene oplossing" heeft nog twee onbekende constanten, `α1` en `α2`. Om die te vinden, heb je **twee beginvoorwaarden** nodig (bv. `a0 = ...` en `a1 = ...`).
    -   Vul `n=0` in de algemene formule en stel het resultaat gelijk aan de waarde van `a0`.
    -   Vul `n=1` in de algemene formule en stel het resultaat gelijk aan de waarde van `a1`.
    -   Je krijgt nu een **stelsel van 2 vergelijkingen met 2 onbekenden** (`α1` en `α2`). Los dit op!

4.  **Schrijf de finale expliciete formule.**
    Vul de gevonden waarden voor `α1` en `α2` in in de algemene oplossing. Nu heb je de directe formule.

### Niet-homogene betrekkingen

Soms staat er nog een extra term in de betrekking: `an = c1*a(n-1) + c2*a(n-2) + f(n)`.
-   De aanpak is gelijkaardig, maar complexer. De algemene oplossing is dan `A(algemeen) = A(homogeen) + A(particulier)`.
-   `A(homogeen)` is de oplossing die we hierboven vonden.
-   `A(particulier)` is een "gok" die lijkt op de vorm van `f(n)`.

## D. Toepassing: De Torens van Hanoi

Een klassieke puzzel: verplaats `n` schijven van de ene naar de andere stok onder bepaalde regels. Het minimum aantal zetten `Hn` wordt beschreven door de recurrente betrekking:
`Hn = 2 * H(n-1) + 1` (met `H1 = 1`).
Via de methodes uit dit hoofdstuk kan je de directe formule vinden: `Hn = 2^n - 1`.

## E. Examengerichte vertaling

-   **Focus:** Het **stappenplan** voor het oplossen van homogene lineaire recurrente betrekkingen van orde 2 is de kern. Je moet dit kunnen dromen.
-   **Typische Vragen:**
    -   "Gegeven de betrekking `an = ...` en de beginvoorwaarden `a0=...` en `a1=...`, bepaal de expliciete formule voor `an`."
    -   "Bereken de 20ste term van de rij." (Eerst expliciete formule vinden, dan `n=20` invullen).
    -   Een vraagstuk (zoals renteberekening, populatiegroei) dat je eerst zelf moet vertalen naar een recurrente betrekking, en dan moet oplossen.
-   **Software (`wxMaxima`):** `wxMaxima` kan je helpen met de twee belangrijkste rekenstappen in het proces. Je moet het stappenplan wel zelf kennen en aansturen.

    -   **Stap 1: Wortels vinden:**
        -   `solve(r^2 - c1*r - c2 = 0, r);`
        -   Gebruik dit commando om de wortels `r1` en `r2` van de karakteristieke vergelijking snel en foutloos te vinden.

    -   **Stap 2: Constanten (α1, α2) vinden:**
        -   Stel de twee vergelijkingen op basis van je beginvoorwaarden manueel op.
        -   `solve([vergelijking1, vergelijking2], [a1, a2]);` (gebruik `a1` en `a2` voor `α1` en `α2`).
        -   Dit commando lost het stelsel voor je op en geeft je de waarden voor de constanten.

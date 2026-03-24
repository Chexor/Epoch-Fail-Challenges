# H3 - Stelsels van lineaire vergelijkingen

[[Problem Solving 2 - Overzicht]]

## A. Wat is het kernprobleem?

Hoe los je een set van meerdere vergelijkingen met meerdere onbekenden op een systematische en efficiënte manier op? Denk aan 3 vergelijkingen met 3 onbekenden (x, y, z), of zelfs 100 met 100. Manuele substitutie wordt dan onmogelijk.

Matrices bieden een krachtige, algoritmische methode om dit aan te pakken.

## B. Intuïtieve uitleg

Elke lineaire vergelijking kan je zien als een meetkundig object.
-   `ax + by = c` (2 onbekenden) is een **rechte**.
-   `ax + by + cz = d` (3 onbekenden) is een **vlak**.

Een stelsel oplossen betekent dat je op zoek gaat naar het **gemeenschappelijke snijpunt** van al die objecten.
-   **Twee rechten:** snijden meestal in één punt (unieke oplossing). Soms lopen ze parallel (geen oplossing) of liggen ze op elkaar (oneindig veel oplossingen).
-   **Drie vlakken:** snijden meestal in één punt. Maar ze kunnen ook snijden in een lijn (oneindig veel oplossingen), of twee aan twee parallel lopen (geen oplossing).

De methodes hieronder zijn manieren om dat snijpunt systematisch te vinden.

## C. Formele structuur

Elk stelsel kunnen we schrijven in de matrixvorm: **`A * X = B`**
-   **A:** De **coëfficiëntenmatrix**. Hierin staan alle getallen die voor de onbekenden (x, y, z) staan.
-   **X:** De **kolommatrix van de onbekenden**.
-   **B:** De **kolommatrix van de rechterleden** (de getallen na het '=' teken).

### Methode 1: Methode van de inverse matrix (Beperkt nuttig)

-   **Idee:** Als `A * X = B`, dan is `X = A⁻¹ * B`.
-   **Procedure:**
    1.  Stel matrix `A` en `B` op.
    2.  Bereken de inverse `A⁻¹`.
    3.  Vermenigvuldig `A⁻¹` met `B`. Het resultaat is de oplossing `X`.
-   **Nadelen:**
    -   Werkt **enkel** voor vierkante stelsels (evenveel vergelijkingen als onbekenden).
    -   Werkt **enkel** als de inverse bestaat (`det(A) ≠ 0`).
    -   Geeft dus **enkel** unieke oplossingen en kan niet omgaan met "geen" of "oneindig veel" oplossingen.

### Methode 2: Eliminatiemethode van Gauss-Jordan (DE STANDAARDMETHODE)

Dit is de meest robuuste en belangrijkste methode. Het werkt altijd.

-   **Idee:** We herschrijven het stelsel stap voor stap naar een extreem simpele vorm waar je de oplossing gewoon kan aflezen, zonder de betekenis ervan te veranderen.
-   **Procedure:**
    1.  **De Gerande Matrix:** We maken één grote matrix `[A | B]`, de coëfficiëntenmatrix met de kolom van de rechterleden er gewoon aan geplakt.
    2.  **Rij-operaties:** We gebruiken de elementaire rij-operaties (rijen wisselen, rij * getal, rij + veelvoud * andere rij) om de `A`-kant van de matrix om te vormen naar de **eenheidsmatrix**.
    3.  **Doel (RREF):** Het doel is om de vorm `[I | X]` te bereiken. (Reduced Row Echelon Form).
    4.  **Oplossing aflezen:** Zodra de linkerkant de eenheidsmatrix is, is de rechterkant automatisch de oplossingsmatrix `X`.

### Mogelijke Resultaten van Gauss-Jordan

1.  **Unieke Oplossing:** Je kan de linkerkant perfect omvormen tot de eenheidsmatrix. De oplossing staat rechts.
2.  **Geen Oplossing (Strijdig stelsel):** Tijdens het proces krijg je een rij die eruitziet als `[0 0 0 | c]` (met `c` niet nul). Dit vertaalt zich naar de onmogelijke vergelijking `0*x + 0*y + 0*z = c`. Het stelsel is strijdig.
3.  **Oneindig Veel Oplossingen:** Je krijgt een volledige **nulrij** `[0 0 0 | 0]`. Dit betekent dat één van je vergelijkingen overbodig was (een combinatie van de anderen). Je hebt dan een "vrije variabele" (of parameter) die je zelf mag kiezen, en de andere onbekenden hangen daarvan af. De oplossing is een lijn of een vlak.

## D. Toepassing: Vraagstukken

De moeilijkheid bij vraagstukken is niet het oplossen van het stelsel, maar het **correct opstellen** ervan.

-   **Stap 1: Identificeer de onbekenden.** (bv. `x` = prijs van een computer, `y` = prijs van een printer, ...).
-   **Stap 2: Vertaal elke zin/voorwaarde naar een wiskundige vergelijking.** ("De printer, scanner en DVD-writer kosten samen 250 EUR" → `y + z + w = 250`).
-   **Stap 3: Schrijf het volledige stelsel in de `A*X=B` vorm.**
-   **Stap 4: Los het stelsel op met Gauss-Jordan** (in `wxMaxima`).

## E. Examengerichte vertaling

-   **Focus:** Je **moet** de Gauss-Jordan methode kunnen toepassen met behulp van de gerande matrix.
-   **Typische Vragen:**
    -   "Los volgend stelsel op met een matrix-methode." (Gebruik ALTIJD Gauss-Jordan).
    -   Een vraagstuk waarbij je zelf het stelsel opstelt en oplost.
    -   "Bespreek het stelsel in functie van parameter `m`." (Dit is geavanceerder, maar het komt neer op kijken wanneer je door nul zou delen in het Gauss-Jordan proces).
-   **Software (`wxMaxima`):** De Gauss-Jordan methode is de standaard. Volg deze stappen:
    1.  `stelsel: [...]`: Definieer de vergelijkingen in een lijst.
    2.  `AB_neg: augcoefmatrix(stelsel, [x,y,z]);`: Maakt de gerande matrix `[A | -B]`. **Opgelet:** `augcoefmatrix` geeft een negatief rechterlid!
    3.  `AB: columndiv(AB_neg, 4, -1);`: Corrigeer de laatste kolom (vervang `4` door het juiste kolomnummer).
    4.  `rref(AB);`: Dit is het **belangrijkste commando**. Het past de Gauss-Jordan eliminatie toe en geeft de eindmatrix waar je de oplossing direct uit afleest.
-   **Vaak gemaakte fouten:**
    -   Fouten bij het manueel overschrijven van het stelsel naar de matrix.
    -   Verkeerd interpreteren van een `[0 0 0 | c]` of `[0 0 0 | 0]` rij.
    -   Vergeten dat `augcoefmatrix` een `-B` kolom geeft.

# H1 - Matrices

[[Problem Solving 2 - Overzicht]] | [[H1 - Oefeningen]]

## A. Wat is het kernprobleem?

Hoe kunnen we een verzameling van gerelateerde getallen (zoals de prijzen van producten in verschillende winkels, of de coördinaten van een 3D-object) op een gestructureerde manier voorstellen en ermee rekenen?

Matrices zijn het antwoord. Ze geven ons een raamwerk om met datasets als één geheel te werken, in plaats van met honderden losse getallen.

## B. Intuïtieve uitleg

Stel je een Excel-spreadsheet voor: een rooster van rijen en kolommen. Dat is een matrix. Het is een manier om data te organiseren.

-   Een **rij** kan bijvoorbeeld alle eigenschappen van één object (bv. de voedingswaarden van een appel) voorstellen.
-   Een **kolom** kan één specifieke eigenschap voor alle objecten (bv. de calorieën van alle fruitsoorten) voorstellen.

Het krachtige is dat we regels hebben om met deze "spreadsheets" te rekenen: je kan ze optellen, vermenigvuldigen, en manipuleren om complexe problemen op te lossen.

## C. Formele structuur

### 1. Definitie & Basisbegrippen

-   **Matrix:** Een rechthoekige tabel van getallen, met `m` rijen en `n` kolommen. We noemen dit een `(m x n)`-matrix.
-   **Element:** Elk getal in de matrix. De positie wordt aangeduid met `Aij` (element op rij `i`, kolom `j`).
-   **Vierkante matrix:** Een matrix met evenveel rijen als kolommen (`m = n`).
-   **Nulmatrix:** Een matrix die enkel uit nullen bestaat.
-   **Eenheidsmatrix (I):** Een vierkante matrix met enen op de hoofddiagonaal (van linksboven naar rechtsonder) en verder overal nullen. Dit is de "1" van de matrixwereld.

### 2. Bewerkingen met matrices

De regels zijn strikt. Vooral de afmetingen zijn cruciaal.

#### a. Optellen en Aftrekken
-   **Regel:** Je kan enkel matrices van **exact dezelfde dimensies** optellen of aftrekken.
-   **Hoe?** Tel (of trek) de elementen op dezelfde positie bij elkaar op.
-   `[A] (m x n) + [B] (m x n) = [C] (m x n)`

#### b. Vermenigvuldigen met een getal (scalair)
-   **Regel:** Altijd mogelijk.
-   **Hoe?** Vermenigvuldig **elk element** in de matrix met dat getal.

#### c. Transponeren
-   **Symbool:** `A^T`
-   **Regel:** Altijd mogelijk.
-   **Hoe?** Wissel de rijen en kolommen van plaats. De eerste rij wordt de eerste kolom, de tweede rij de tweede kolom, etc.
-   Een `(m x n)`-matrix wordt een `(n x m)`-matrix.

#### d. Matrices Vermenigvuldigen (BELANGRIJK!)
Dit is de meest complexe, maar ook de meest krachtige bewerking.

-   **Regel:** Het product `A * B` is **enkel mogelijk** als het aantal **kolommen van A** gelijk is aan het aantal **rijen van B**.
    -   `[A] (m x n) * [B] (n x p) = [C] (m x p)`
-   **Resultaat:** De resulterende matrix `C` heeft het aantal **rijen van A** en het aantal **kolommen van B**.
-   **Hoe?** Om het element `Cij` te vinden, neem je de **i-de rij van A** en de **j-de kolom van B**. Vermenigvuldig de corresponderende elementen en tel de resultaten op.
    - `Cij = (rij i van A) • (kolom j van B)`

**Cruciale Eigenschappen:**
-   `A * B` is **NIET** hetzelfde als `B * A`. De volgorde is essentieel! (Niet-commutatief)
-   `(A * B) * C = A * (B * C)` (Associatief)

## D. Toepassing: Winkelmandjes berekenen

Dit voorbeeld komt rechtstreeks uit de syllabus en is een perfecte illustratie van waarom matrixvermenigvuldiging zo nuttig is.

-   **Matrix P (Prijzen):** Rijen zijn supermarkten (X, Y, Z), kolommen zijn producten (water, melk, ...). `Pij` is de prijs van product `j` in winkel `i`. (Dimensie: 3x5)
-   **Matrix L (Lijstjes):** Rijen zijn producten, kolommen zijn studenten (An, Bart, Chris). `Lij` is de hoeveelheid van product `i` die student `j` nodig heeft. (Dimensie: 5x3)

**Probleem:** Bereken de totale kost per student, per supermarkt.

**Oplossing:** `PL = P * L`

-   **Check dimensies:** `(3x5) * (5x3)` → Kan, want 5=5. Het resultaat wordt een `(3x3)` matrix.
-   **Interpretatie resultaat:** De resulterende matrix `PL` heeft supermarkten als rijen en studenten als kolommen. Het element `(PL)ij` geeft de totale kost voor student `j` in supermarkt `i`.

Dit ene product `P * L` vervangt 3 * 3 = 9 aparte, manuele berekeningen. Schaal dit op naar 1000 producten en 500 studenten, en je ziet meteen de kracht.

## E. Examengerichte vertaling

-   **Focus:** Het examen is 100% oefeningen. Zorg dat je de **bewerkingen** (vooral vermenigvuldiging) vlot en foutloos kan uitvoeren, zowel manueel als met `wxMaxima`.
-   **Typische Vragen:**
    -   "Gegeven matrices A en B, bereken `A*B`, `A^T`, `2A + B`..."
    -   Toepassingsvragen zoals het winkelmandjes-voorbeeld. Je moet hier zelf de matrices correct kunnen opstellen en de juiste vermenigvuldiging (`P*L` of `L*P`?) kiezen. De dimensie-check is hier je beste vriend.
    -   "Is `A*B` gedefinieerd? Zo ja, wat zijn de dimensies van het resultaat?"
-   **Vaak gemaakte fouten:**
    -   De volgorde omdraaien (`A*B` in plaats van `B*A`).
    -   De dimensieregel voor vermenigvuldiging negeren.
    -   Fouten in het "rij-punt-kolom" proces. Werk gestructureerd.
-   **Software (`wxMaxima`):** Oefen hiermee! De syllabus toont de commando's. Zorg dat je een matrix kan ingeven en de basisbewerkingen kan uitvoeren. Dit bespaart je enorm veel tijd en rekenfouten op het examen.

    -   `A: matrix([r1], [r2], ...)`: Een matrix definiëren. Bv: `matrix([1,2], [3,4])`.
    -   `A + B`, `A - B`, `k * A`: Optellen, aftrekken en scalair vermenigvuldigen.
    -   `A . B`: Matrixvermenigvuldiging (let op de punt!).
    -   `transpose(A)`: De getransponeerde matrix.
    -   `A^^n`: De matrix tot een macht verheffen (bv. `A^^2`).
    -   `invert(A)` of `A^^(-1)`: De inverse matrix berekenen.

Volgende stap is de oefeningen van Hoofdstuk 1 maken. Ben je er klaar voor?

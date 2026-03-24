# H4 - Grafen modelleren met matrices

[[Problem Solving 2 - Overzicht]]

## A. Wat is het kernprobleem?

Hoe kunnen we een netwerk van verbindingen (steden met wegen, mensen op social media, computers in een netwerk) wiskundig vastleggen zodat we erover kunnen redeneren en berekeningen op kunnen uitvoeren?

We gebruiken hiervoor **grafen** (de visuele voorstelling) en **verbindingsmatrices** (de wiskundige vertaling).

## B. Intuïtieve uitleg

Een **graaf** is niets meer dan een verzameling van **punten** (knopen) die verbonden zijn door **lijnen** (zijden). Denk aan een simplistische metrokaart.

De bijhorende **verbindingsmatrix** (of adjacentiematrix) is een tabel die deze graaf perfect beschrijft. De matrix `A` vertelt je hoeveel directe verbindingen er zijn tussen twee punten.

-   `Aij = 1` betekent: er is een directe verbinding tussen punt `i` en punt `j`.
-   `Aij = 0` betekent: er is géén directe verbinding.
-   `Aij = 2` betekent: er zijn twee verschillende verbindingen tussen `i` en `j`.

De echte magie komt wanneer we machten van deze matrix nemen. `A²` vertelt je plots op hoeveel manieren je in **twee stappen** van punt `i` naar `j` kan reizen! `A³` doet hetzelfde voor **drie stappen**, enzovoort. Dit is een ongelofelijk krachtig concept.

## C. Formele structuur

### 1. Basisbegrippen Grafentheorie

-   **Graaf:** Een verzameling van **knopen** (vertices) en **zijden** (edges).
-   **Graad van een knoop:** Het aantal zijden dat in een knoop toekomt.
-   **Pad:** Een opeenvolging van zijden die je doorloopt van de ene knoop naar de andere.
-   **Niet-gerichte graaf:** De verbindingen werken in beide richtingen (een gewone weg). De verbindingsmatrix is **symmetrisch**.
-   **Gerichte graaf:** De verbindingen zijn eenrichtingsverkeer (aangeduid met een pijl). De verbindingsmatrix is **niet symmetrisch**.

### 2. De Verbindingsmatrix (Adjacency Matrix) `A`

-   Voor een graaf met `n` knopen is `A` een `(n x n)`-matrix.
-   `Aij` = het aantal directe verbindingen van knoop `i` naar knoop `j`.
-   **Eigenschap:** De som van de elementen in rij `i` (of kolom `i`, bij een niet-gerichte graaf) is gelijk aan de graad van knoop `i`.

### 3. Machten van de Verbindingsmatrix

Dit is de kern van de toepassingen.

-   Het element `(A²)ij` geeft het **aantal paden met lengte 2** van knoop `i` naar knoop `j`.
-   Het element `(A³)ij` geeft het **aantal paden met lengte 3** van knoop `i` naar knoop `j`.
-   Het element `(A^k)ij` geeft het **aantal paden met lengte k** van knoop `i` naar knoop `j`.

### 4. Evolutiematrices (Leslie & Markov)

Dit zijn speciale, gerichte grafen die een verandering in de tijd voorstellen.

-   **Leslie-matrix (Populatiemodel):**
    -   Beschrijft de evolutie van een populatie ingedeeld in leeftijdscategorieën.
    -   De matrix toont overlevingskansen en geboortecijfers.
    -   Als je de matrix vermenigvuldigt met een kolomvector die de huidige populatie voorstelt, krijg je de populatie van de volgende generatie.
-   **Markov-matrix (Overgangsmodel):**
    -   Beschrijft de overgang tussen verschillende toestanden (bv. klanten die wisselen tussen computermerken A, B en C).
    -   De elementen zijn kansen. De som van de elementen in elke kolom is 1 (of 100%).
    -   **Stabiele toestand:** Vaak wordt gezocht naar een evenwichtssituatie die na verloop van tijd niet meer verandert. Dit komt neer op het oplossen van het stelsel `M*X = X`, ofwel **`(M - I) * X = 0`**. Dit is een directe link naar Hoofdstuk 3!

## D. Toepassing: Het Königsberg Brugprobleem

Het historische startpunt van de grafentheorie. De vraag was of je een wandeling kon maken waarbij je elke van de 7 bruggen precies één keer overstak. Door de stad voor te stellen als een graaf (4 landmassa's als knopen, 7 bruggen als zijden), kon Euler bewijzen dat dit onmogelijk was omdat de knopen een 'oneven' graad hadden.

## E. Examengerichte vertaling

-   **Focus:** Je moet vlot kunnen schakelen tussen de visuele graaf en de wiskundige matrix. De link met stelsels (bij Markov-processen) is cruciaal.
-   **Typische Vragen:**
    -   Gegeven een graaf, stel de verbindingsmatrix op.
    -   Gegeven een verbindingsmatrix, teken de bijhorende (gerichte of niet-gerichte) graaf.
    -   "Hoeveel manieren zijn er om in 3 stappen van knoop A naar knoop B te gaan?" (Hint: bereken `A³`).
    -   Een vraagstuk over populatie of marktaandeel (Leslie/Markov). Je moet:
        1.  De evolutiematrix correct opstellen.
        2.  De toestand na een paar stappen berekenen (matrixvermenigvuldiging).
        3.  De stabiele toestand/evenwichtssituatie berekenen (het stelsel `(M-I)X=0` oplossen).
-   **Software (`wxMaxima`):**
    -   **Paden tellen:**
        1.  `A: matrix(...)`: Definieer de verbindingsmatrix.
        2.  `A^^k`: Bereken de k-de macht. Het `(i,j)`-element is je antwoord.
    -   **Stabiele toestand (Markov):**
        1.  `M: matrix(...)`: Definieer de Markov-matrix.
        2.  `I: ident(n)`: Maak een eenheidsmatrix van de juiste dimensie `n`.
        3.  `stelsel_matrix = M - I`: Stel de matrix voor het stelsel `(M-I)X=0` op.
        4.  `rref(stelsel_matrix)`: Los het stelsel op om de verhoudingen van de stabiele toestand te vinden. Vergeet niet de extra voorwaarde (bv. `x+y+z=1`) toe te voegen.

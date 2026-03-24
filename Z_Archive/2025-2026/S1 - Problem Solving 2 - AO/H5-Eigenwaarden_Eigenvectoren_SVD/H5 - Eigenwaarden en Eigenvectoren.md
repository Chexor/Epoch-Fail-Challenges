# H5 - Eigenwaarden en Eigenvectoren

[[Problem Solving 2 - Overzicht]]

## A. Wat is het kernprobleem?

Wanneer een matrix een transformatie uitvoert op een vector (bv. een punt in de ruimte), verandert die vector meestal van zowel lengte als richting. De vraag is: zijn er **speciale vectoren** die, na de transformatie, wel van lengte veranderen, maar **exact dezelfde richting** behouden?

Deze speciale vectoren heten **eigenvectoren**, en de factor waarmee hun lengte verandert, heet hun **eigenwaarde**.

## B. Intuïtieve uitleg

Stel je een wereldkaart voor die je uitrekt in de oost-west richting.
-   Een vector die van west naar oost wijst, wordt langer maar blijft perfect horizontaal. Dit is een **eigenvector**. De 'stretch'-factor (bv. 2) is de **eigenwaarde**.
-   Een vector die van zuid naar noord wijst, verandert niet van lengte of richting. Dit is ook een **eigenvector**, met eigenwaarde 1.
-   Een vector die schuin wijst (bv. naar het noordoosten), zal na de transformatie meer naar het oosten wijzen. De richting verandert. Dit is dus **geen** eigenvector.

Eigenvectoren zijn dus de "assen" of de fundamentele richtingen van een transformatie. Ze leggen de diepste structuur van de matrix bloot.

## C. Formele structuur

### 1. Definitie

De definitie die alles samenvat is: `A * v = λ * v`
-   **A:** De vierkante matrix.
-   **v:** De eigenvector (mag niet de nulvector zijn).
-   **λ:** De eigenwaarde (een getal).

Deze vergelijking zegt: "Matrix A toepassen op vector v heeft hetzelfde effect als vector v gewoon vermenigvuldigen met het getal λ".

### 2. Hoe vind je de eigenwaarden (λ)?

1.  Herschrijf de definitie: `A*v - λ*v = 0` → `A*v - λ*I*v = 0` → **`(A - λI) * v = 0`**.
2.  Dit is een stelsel van vergelijkingen (zie H3). We zoeken een oplossing `v` die **niet nul** is.
3.  Een stelsel heeft een niet-nul oplossing als en slechts als de coëfficiëntenmatrix **singulier** is.
4.  Dus, de **determinant** van die matrix moet nul zijn:
    **`det(A - λI) = 0`**
5.  Deze vergelijking heet de **karakteristieke vergelijking**. Los deze op naar `λ` en je hebt de eigenwaarden!

### 3. Hoe vind je de eigenvectoren (v)?

1.  Neem een eigenwaarde `λ` die je net hebt gevonden.
2.  Vul deze waarde in in het stelsel van stap 2: **`(A - λI) * v = 0`**.
3.  Los dit stelsel op voor `v` (de onbekenden x, y, z). Gebruik hiervoor de **Gauss-Jordan methode** uit Hoofdstuk 3.
4.  Omdat `det(A - λI)` per definitie 0 is, zal je altijd **oneindig veel oplossingen** vinden (met minstens één parameter). Elke van deze oplossingen (behalve de nulvector) is een geldige eigenvector.

### 4. Singuliere Waarden Decompositie (SVD)

SVD is een meer geavanceerde techniek die het idee van eigenwaarden en eigenvectoren veralgemeent naar **niet-vierkante matrices**. Het ontbindt een matrix `A` in drie andere matrices: `A = U * S * W^T`.
-   **S:** Een diagonaalmatrix met de "singuliere waarden". Dit is de tegenhanger van de eigenwaarden.
-   **U en W:** Matrices die de "richtingen" bevatten, vergelijkbaar met de eigenvectoren.

## D. Toepassing: Machtsverheffing van een matrix

Een van de meest krachtige toepassingen is het razendsnel berekenen van een hoge macht van een matrix (bv. `A^50`). Dit is cruciaal voor het voorspellen van systemen op lange termijn (zie Markov-ketens in H4).

-   **Procedure (Diagonalisatie):**
    1.  Vind de eigenwaarden `λ1, λ2, ...` en de bijhorende eigenvectoren `v1, v2, ...`.
    2.  Maak een matrix `P` met de eigenvectoren als kolommen.
    3.  Maak een diagonaalmatrix `D` met de eigenwaarden op de diagonaal.
    4.  Dan geldt: `A = P * D * P⁻¹`.
    5.  En de magie: **`A^m = P * D^m * P⁻¹`**.
-   Het berekenen van `D^m` is super eenvoudig: verhef gewoon de getallen op de diagonaal tot de macht `m`. De rest blijft 0.

Hiermee kan je `A^50` berekenen met slechts twee matrixvermenigvuldigingen, in plaats van 49.

## E. Examengerichte vertaling

-   **Focus:** Je moet het **stappenplan** voor het vinden van eigenwaarden en eigenvectoren perfect beheersen. De link met determinanten (H2) en stelsels (H3) is 100% expliciet.
-   **Typische Vragen:**
    -   "Bepaal de eigenwaarden en de bijhorende eigenvectoren van matrix A."
    -   "Bereken `A^20` met behulp van diagonalisatie."
-   **Software (`wxMaxima`):** Gebruik de ingebouwde functies. Ze doen al het zware rekenwerk voor jou.

    -   `eigenvalues(A)`: Geeft een lijst met de eigenwaarden.
    -   `eigenvectors(A)`: Geeft de volledige informatie in een specifiek formaat.
        -   **Output:** `[[[λ1, λ2, ...], [mult1, mult2, ...]], [v1], [v2], ...]`
        -   **Betekenis:**
            -   De eerste lijst bevat de eigenwaarden (`λ`) en hun multipliciteit.
            -   Daarna volgen de bijhorende eigenvectoren (`v1`, `v2`, ...), elk als een aparte lijst.
        -   **Toepassing:** Gebruik deze output om direct je diagonaalmatrix `D` (met de eigenwaarden) en je matrix `P` (met de eigenvectoren als kolommen) op te stellen voor diagonalisatie.
-   **Vaak gemaakte fouten:**
    -   Een rekenfout in de determinant `det(A - λI) = 0`, waardoor je foute eigenwaarden vindt.
    -   Slordigheidsfouten bij het oplossen van het stelsel `(A - λI)v = 0` om de eigenvectoren te vinden. Controleer je werk met `wxMaxima`!

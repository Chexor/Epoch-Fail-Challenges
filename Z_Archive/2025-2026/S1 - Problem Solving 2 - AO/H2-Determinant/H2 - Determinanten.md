# H2 - Determinanten

[[Problem Solving 2 - Overzicht]]

## A. Wat is het kernprobleem?

Hoe kunnen we met één enkel getal de "essentie" van een **vierkante** matrix samenvatten? We hebben een getal nodig dat ons iets vertelt over de unieke eigenschappen van de matrix, bijvoorbeeld of we een matrix-vergelijking wel kunnen oplossen.

De **determinant** is dat magische getal.

## B. Intuïtieve uitleg

Stel je voor dat een matrix een transformatie is in de ruimte. Bijvoorbeeld, een matrix kan een vierkantje uitrekken, draaien of samendrukken.

De determinant vertelt je **hoeveel de oppervlakte (of het volume in 3D) verandert** door die transformatie.

-   `det(A) = 3` → De oppervlakte wordt 3 keer zo groot.
-   `det(A) = 0.5` → De oppervlakte wordt gehalveerd.
-   `det(A) = -1` → De oppervlakte blijft gelijk, maar de oriëntatie is gespiegeld (zoals in een spiegel).

En de belangrijkste:
-   **`det(A) = 0`** → De transformatie plet het figuur tot een lijn of een punt. De oppervlakte wordt nul. Dit betekent dat de matrix "informatie verliest". Een matrix met determinant 0 is speciaal en onhandelbaar, en je kan er niet mee "terugrekenen".

## C. Formele structuur

### 1. Hoe bereken je de determinant?

De methode hangt af van de grootte van de matrix.

#### a. Voor een (2x2)-matrix
Dit is de basis. Voor een matrix `[[a, b], [c, d]]`:
`det(A) = ad - bc`
(Product van de hoofddiagonaal min het product van de andere diagonaal).

#### b. Voor een (3x3)-matrix: Regel van Sarrus
Dit is een visueel trucje dat **enkel voor 3x3** werkt!

1.  Schrijf de eerste twee kolommen van de matrix er rechts naast.
2.  Je hebt nu 3 volledige diagonalen van linksboven naar rechtsonder, en 3 van rechtsboven naar linksonder.
3.  **Tel op:** De producten van de 3 diagonalen (linksboven → rechtsonder).
4.  **Trek af:** De producten van de 3 andere diagonalen (rechtsboven → linksonder).

Dit is een standaardprocedure voor manuele berekeningen op het examen.

### 2. Belangrijkste Eigenschappen

Dit is **cruciale leerstof**. Deze regels helpen je om determinanten sneller te berekenen of om vragen op te lossen zonder veel rekenwerk.

-   **Inverse Matrix:** Een matrix `A` heeft een inverse `A⁻¹` **ALS EN SLECHTS ALS** `det(A) ≠ 0`. Dit is de allerbelangrijkste eigenschap.
-   **Productregel:** `det(A * B) = det(A) * det(B)`. Super handig!
-   **Transponeren:** `det(A) = det(A^T)`. Rijen en kolommen hebben dezelfde eigenschappen.
-   **Nulrij/kolom:** Als een matrix een volledige rij of kolom met nullen heeft, is de determinant `0`.
-   **Gelijke rijen/kolommen:** Als een matrix twee identieke rijen of kolommen heeft, is de determinant `0`.
-   **Rij-operaties:**
    -   Twee rijen van plaats wisselen: de determinant **wisselt van teken**.
    -   Een rij vermenigvuldigen met een getal `k`: de determinant wordt ook `* k` vermenigvuldigd.
    -   **BELANGRIJK:** Een veelvoud van een rij bij een andere rij optellen: de determinant **verandert NIET**. Dit is de sleutel om nullen te creëren en de berekening te vereenvoudigen.

## D. Toepassing: Bestaat de inverse?

De meest directe en belangrijkste toepassing van de determinant is de vraag: "Is deze matrix inverteerbaar?". Dit betekent: "Kunnen we een 'deel door' operatie uitvoeren voor deze matrix?".

-   Als `det(A) ≠ 0`, is de matrix **regulier** (of inverteerbaar). Er bestaat een unieke `A⁻¹`.
-   Als `det(A) = 0`, is de matrix **singulier** (niet inverteerbaar). Er is geen `A⁻¹`.

Deze vraag is fundamenteel voor het oplossen van stelsels van vergelijkingen in het volgende hoofdstuk.

## E. Examengerichte vertaling

-   **Focus:** Je moet vlot een 2x2 en 3x3 determinant kunnen berekenen (manueel met Sarrus, en met `wxMaxima`).
-   **Typische Vragen:**
    -   "Bereken de determinant van matrix A."
    -   "Voor welke waarde(n) van parameter `m` is de matrix A singulier?" (Hint: stel de determinant gelijk aan 0 en los op naar `m`).
    -   "Heeft matrix A een inverse? Waarom wel/niet?" (Hint: bereken de determinant).
    -   "Gebruik de eigenschappen van determinanten om aan te tonen dat `det(A) = 0` zonder de volledige berekening te maken." (Hint: zoek naar gelijke rijen, een rij die een veelvoud is van een andere, etc.).
-   **Software (`wxMaxima`):** Gebruik `wxMaxima` om je manuele berekeningen (Regel van Sarrus) te controleren en om snel te werken op het examen.

    -   `determinant(A)`: Berekent de determinant van matrix A.
    -   `solve(determinant(A) = 0, m)`: Een krachtige combinatie om te vinden voor welke waarde van een parameter `m` een matrix singulier wordt.

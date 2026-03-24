# H5 - wxMaxima Handleiding

[[H5 - Eigenwaarden en Eigenvectoren]]

Deze nota toont de `wxMaxima` commando's voor de berekeningen uit Hoofdstuk 5. `wxMaxima` heeft krachtige, ingebouwde functies die dit complexe onderwerp sterk vereenvoudigen.

## 1. De Karakteristieke Vergelijking

Je kan `wxMaxima` gebruiken om de vergelijking `det(A - λI) = 0` op te stellen.

```maxima
/* Definieer je matrix A */
A: matrix([4, -1, -1], [-1, 4, -1], [-1, -1, 4]);

/* Definieer de eenheidsmatrix */
I3: ident(3);

/* De karakteristieke matrix (A - λI).
   Let op: wxMaxima gebruikt vaak %lambda voor de Griekse letter. */
kar_matrix: A - %lambda * I3;

/* Bereken de determinant om de karakteristieke vergelijking te krijgen */
kar_vgl: determinant(kar_matrix) = 0;

/* Je kan de vergelijking vereenvoudigen met expand() of factor() */
factor(kar_vgl);
```

## 2. Eigenwaarden en Eigenvectoren Vinden

Dit is waar `wxMaxima` echt uitblinkt. In plaats van het volledige stappenplan manueel te doen, kan je directe commando's gebruiken.

-   `eigenvalues(A)`: Geeft een lijst met de eigenwaarden en hun multipliciteit.
-   `eigenvectors(A)`: Geeft een compleet overzicht:
    -   Een lijst met de eigenwaarden en hun multipliciteit.
    -   Een lijst met de bijhorende eigenvectoren.

```maxima
A: matrix([2, 1, 1], [2, 3, 2], [3, 3, 4]);

/* Vraag de eigenwaarden op */
ev_A: eigenvalues(A);
/* Output: [[1, 7], [2, 1]]
   Betekenis: Eigenwaarde 1 heeft multipliciteit 2, eigenwaarde 7 heeft multipliciteit 1. */

/* Vraag de eigenwaarden én eigenvectoren op */
evc_A: eigenvectors(A);
/* Output: [[[1, 7], [2, 1]], [[[-1, 0, 1], [-1, 1, 0]], [[1, 2, 3]]]]
   Betekenis:
   - [[-1, 0, 1], [-1, 1, 0]] zijn de twee eigenvectoren bij eigenwaarde 1.
   - [[1, 2, 3]] is de eigenvector bij eigenwaarde 7.
*/
```
**Opgelet:** De eigenvectoren die `wxMaxima` geeft, zijn niet uniek. Ze kunnen een veelvoud zijn van wat je manueel zou berekenen. Dit is niet fout.

## 3. Diagonalisatie en Machtsverheffing

Voor het berekenen van `A^m` via diagonalisatie (`A^m = P * D^m * P⁻¹`) gebruik je `wxMaxima` om `P`, `D` en `P⁻¹` te vinden en de finale vermenigvuldiging te doen.

```maxima
/* Stel, we willen A^10 berekenen voor de matrix A hierboven */
A: matrix([2, 1, 1], [2, 3, 2], [3, 3, 4]);

/* 1. Vind de eigenvectoren om P te vormen.
      P is de matrix met de eigenvectoren als kolommen. */
P: matrix( [-1, -1, 1], [0, 1, 2], [1, 0, 3] );
/* Let op: je moet de vectoren manueel uit de output van eigenvectors()
   omzetten naar de kolommen van een matrix. */
P: transpose(P); /* Makkelijker: typ ze als rijen en transponeer. */

/* 2. Maak de diagonaalmatrix D met de eigenwaarden */
D: matrix( [1, 0, 0], [0, 1, 0], [0, 0, 7] );

/* 3. Bereken P-inverse */
P_inv: P^^-1;

/* 4. Bereken D^10 */
D10: D^^10;

/* 5. Bereken het eindresultaat */
A10: P . D10 . P_inv;
```
Dit is een lang proces, maar veel sneller dan `A^^10` rechtstreeks berekenen voor grote matrices en hoge machten.

# H1 - wxMaxima Handleiding

[[H1 - Matrices]]

Deze nota toont de essentiële `wxMaxima` commando's voor de berekeningen met matrices uit Hoofdstuk 1.

## 1. Een Matrix Invoeren

Er zijn twee manieren, maar de `matrix()` functie is het handigst.

-   **Syntax:** `Variabele: matrix( [rij1], [rij2], ... );`
-   Elke rij staat tussen vierkante haken `[]`.
-   Elementen in een rij worden gescheiden door komma's.

```maxima
/* Voorbeeld: Een 2x3 matrix A aanmaken */
A: matrix( [1, 2, 3], [4, 5, 6] );
```

## 2. Optellen, Aftrekken en Scalair Vermenigvuldigen

Dit werkt intuïtief met de gewone `+`, `-` en `*` operatoren.

```maxima
/* Definieer twee matrices van dezelfde grootte */
A: matrix( [1, 2], [3, 4] );
B: matrix( [5, 6], [7, 8] );

/* Optellen */
C: A + B;

/* Aftrekken */
D: B - A;

/* Scalaire vermenigvuldiging (met een getal) */
E: 3 * A;
```

## 3. Matrixvermenigvuldiging (BELANGRIJK!)

Dit is de meest gemaakte fout. Voor een matrixproduct gebruik je **geen `*` maar een punt `.`**

-   `A * B` → **FOUT!** Dit doet element-per-element vermenigvuldiging.
-   `A . B` → **CORRECT!** Dit doet de wiskundige "rij maal kolom" vermenigvuldiging.

```maxima
/* Definieer twee matrices met correcte afmetingen */
/* A is 2x3, B is 3x2 */
A: matrix( [1, 2, 3], [4, 5, 6] );
B: matrix( [7, 8], [9, 10], [11, 12] );

/* Bereken het product A.B (resultaat is een 2x2 matrix) */
C: A . B;
```

## 4. Transponeren

Gebruik de `transpose()` functie.

```maxima
A: matrix( [1, 2, 3], [4, 5, 6] );

/* Bereken de getransponeerde (resultaat is een 3x2 matrix) */
At: transpose(A);
```

## 5. Machtsverheffing (BELANGRIJK!)

Net als bij de vermenigvuldiging is hier een speciaal symbool voor nodig. Gebruik **twee `^` tekens**.

-   `A^2` → **FOUT!** Dit kwadrateert elk element apart.
-   `A^^2` → **CORRECT!** Dit berekent `A . A`.

```maxima
/* Definieer een vierkante matrix */
M: matrix( [1, 2], [3, 4] );

/* Bereken M tot de derde macht */
M3: M^^3;
```

## 6. Speciale Matrices

-   **Eenheidsmatrix:** `ident(n)` maakt een `n x n` eenheidsmatrix.
-   **Nulmatrix:** Er is geen direct commando, maar je kan `zeromatrix(m, n)` gebruiken.

```maxima
/* Maak een 3x3 eenheidsmatrix */
I3: ident(3);
```

## Compleet Voorbeeld

Laten we de vergelijking `X = 3B - A` uit oefening 5 oplossen in wxMaxima.

```maxima
/* Oefening 5 in wxMaxima */

/* 1. Definieer de matrices A en B */
A: matrix([4, -2], [0, 0], [1, -6]);
B: matrix([-1, 0], [0, -2], [1, -2]);

/* 2. Voer de berekening uit in één keer */
X: (3*B - A)/2;

/* Het resultaat voor X wordt nu getoond */
```

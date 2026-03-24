# H2 - wxMaxima Handleiding

[[H2 - Determinanten]]

Deze nota toont de `wxMaxima` commando's voor de berekeningen uit Hoofdstuk 2, met name determinanten en de inverse matrix.

## 1. De Determinant Berekenen

Het berekenen van een determinant is heel eenvoudig met de `determinant()` functie.

```maxima
/* Definieer een vierkante matrix */
A: matrix( [1, 2, 3], [4, 5, 6], [7, 8, 9] );

/* Bereken de determinant */
d: determinant(A);

/* Resultaat zal 0 zijn, wat betekent dat deze matrix singulier is */
```

## 2. De Inverse Matrix Berekenen

Er zijn twee manieren: de snelle en de stapsgewijze (die de Gauss-Jordan methode nabootst).

### Manier 1: De snelle manier (`A^^-1`)

Net zoals machtsverheffen, kan je de inverse vinden met de `^^` operator.

```maxima
/* Definieer een inverteerbare matrix (determinant is niet 0) */
A: matrix( [1, 2], [3, 5] );

/* Bereken de inverse */
A_inv: A^^-1;
```

### Manier 2: De Gauss-Jordan methode (`rref`)

Dit is de methode die je manueel ook zou gebruiken en die getoond wordt in de syllabus. Het is goed om deze te begrijpen.

1.  Maak de **gerande matrix** `[A | I]` aan. Dit kan met `addcol()`.
2.  Pas de `rref()` (Reduced Row Echelon Form) functie toe op deze nieuwe matrix.
3.  Het resultaat is `[I | A⁻¹]`. Het rechterdeel is je inverse.

```maxima
/* Definieer een 3x3 matrix */
A: matrix( [1, 3, 3], [1, 4, 3], [1, 3, 4] );

/* Maak de 3x3 eenheidsmatrix */
I3: ident(3);

/* Plak ze aan elkaar tot de gerande matrix [A|I] */
AI: addcol(A, I3);

/* Voer de Gauss-Jordan eliminatie uit */
rref_AI: rref(AI);

/* Het rechterdeel van het resultaat is de inverse van A.
   Je kan het manueel aflezen of selecteren met submatrix(). */
```
**Opgelet:** De `rref()` functie is niet standaard ingebouwd in `wxMaxima`. Je moet de definitie ervan uit de syllabus (pagina 34) in je sessie kopiëren en plakken als je ze wil gebruiken.

## Toepassing: Vraagstukken

**Typische vraag:** "Voor welke waarde van `m` is matrix `A` singulier?"
**Aanpak in `wxMaxima`:**
1.  Definieer de matrix `A` met de parameter `m`.
2.  Bereken de determinant van `A`. Je krijgt een formule met `m`.
3.  Gebruik de `solve()` functie om die formule gelijk te stellen aan nul.

```maxima
/* Definieer een matrix met een parameter m */
A: matrix( [m, 1], [4, m-3] );

/* Bereken de determinant in functie van m */
det_A: determinant(A);
/* Resultaat: m*(m-3) - 4 */

/* Los op voor welke m de determinant 0 is */
solve(det_A = 0, m);
/* Resultaat: [m=-1, m=4] */
```
Dit is een enorm krachtige techniek voor het examen.

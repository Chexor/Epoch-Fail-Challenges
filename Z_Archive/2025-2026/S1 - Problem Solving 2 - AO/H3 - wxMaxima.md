# H3 - wxMaxima Handleiding

[[H3 - Stelsels van lineaire vergelijkingen]]

Deze nota toont de `wxMaxima` commando's voor het oplossen van stelsels, de kern van Hoofdstuk 3. Er zijn twee methodes: de `solve` functie en de Gauss-Jordan methode met `rref`. De tweede is de meest robuuste en wordt aangeraden.

## Methode 1: De `solve` functie

Dit is de meest directe manier, maar het geeft de tussenstappen niet weer.

```maxima
/* Definieer de vergelijkingen van het stelsel */
vgl1: 2*x - 3*y + 4*z = -1;
vgl2: 3*y - 2*z = 3;
vgl3: x - 2*y + 2*z = -1/2;

/* Los het stelsel op */
oplossing: solve([vgl1, vgl2, vgl3], [x, y, z]);
```

## Methode 2: De Gauss-Jordan Methode (AANGERADEN)

Dit is de methode die het dichtst aanleunt bij de theorie en die je moet gebruiken op het examen. Het stappenplan is altijd hetzelfde.

**Stap 1: Definieer het stelsel**
Plaats je vergelijkingen in een lijst.

```maxima
stelsel: [2*x+y+2*z+t=6, 6*x-6*y+6*z+12*t=36, 4*x+3*y+3*z-3*t=-1, 2*x+2*y-z+t=10];
```

**Stap 2: Maak de gerande matrix `[A|-B]`**
De functie `augcoefmatrix` doet dit voor jou.
**LET OP:** Deze functie maakt de matrix `[A|-B]`, dus met een negatief rechterlid.

```maxima
AB: augcoefmatrix(stelsel, [x,y,z,t]);
```

**Stap 3: Corrigeer naar `[A|B]`**
We corrigeren het teken van de laatste kolom met het commando `columndiv`.

```maxima
/* Deel de 5e kolom door -1 */
AB: columndiv(AB, 5, -1);
```

**Stap 4: Pas `rref` toe**
Dit commando voert de volledige Gauss-Jordan eliminatie uit en geeft je de eindvorm `[I|X]`, waaruit je de oplossing kan aflezen.

```maxima
oplossing_matrix: rref(AB);
```
Het resultaat is een matrix. De laatste kolom bevat de waarden voor `x, y, z, t`.

**Opgelet:** De `rref()` functie en `columndiv()` functie zijn niet standaard! Je moet de definities uit de syllabus (pagina 47 en 49) in je wxMaxima-sessie kopiëren aan het begin van je examen.

## Compleet Voorbeeld

```maxima
/* ---- KOPIEER DIT AAN HET BEGIN VAN JE EXAMEN ---- */
rref(A):=block([p,q,k],[p,q]:matrix_size(A),A:echelon(A), k:min(p,q), for i thru min(p,q) do (if A[i,i]=0 then (k:i-1,return())), for i:k thru 2 step -1 do (for j from i-1 thru 1 step -1 do A:rowop(A,j,i,A[j,i])), A)$
columndiv(A,i,a):=columnop(A,i,i,1-1/a)$
/* ----------------------------------------------- */

/* Stap 1: Definieer het stelsel */
stelsel: [2*x+y+2*z+t=6, 6*x-6*y+6*z+12*t=36, 4*x+3*y+3*z-3*t=-1, 2*x+2*y-z+t=10];

/* Stap 2: Maak [A|-B] */
AB: augcoefmatrix(stelsel, [x,y,z,t]);

/* Stap 3: Maak [A|B] */
AB: columndiv(AB, 5, -1);

/* Stap 4: Los op met rref */
oplossing: rref(AB);

/* Resultaat is de matrix:
[ 1  0  0  0 | 2 ]
[ 0  1  0  0 | 1 ]
[ 0  0  1  0 | -1]
[ 0  0  0  1 | 3 ]
Je leest af: x=2, y=1, z=-1, t=3
*/
```

# H4 - wxMaxima Handleiding

[[H4 - Grafen modelleren met matrices]]

Deze nota toont de `wxMaxima` commando's voor de berekeningen uit Hoofdstuk 4, die voornamelijk draaien om machten van matrices en het oplossen van stelsels voor stabiele toestanden.

## 1. Verbindingsmatrix en Machten

Er zijn geen speciale functies voor grafen. Je stelt de verbindingsmatrix (adjacency matrix) manueel op zoals elke andere matrix. De belangrijkste operatie is het berekenen van machten om het aantal paden van een bepaalde lengte te vinden.

**Herhaling:** Gebruik `^^` voor machtsverheffing.

```maxima
/* Stel de verbindingsmatrix A van een graaf op */
A: matrix( [0,1,1,0], [1,0,0,1], [1,0,0,1], [0,1,1,0] );

/* Bereken het aantal paden van lengte 3 tussen alle knopen */
A3: A^^3;

/* Het element op rij 1, kolom 4 van A3 geeft het aantal paden
   van lengte 3 tussen knoop 1 en knoop 4. */
```

## 2. Markov-ketens en Stabiele Toestand

Het vinden van de stabiele toestand van een Markov-proces (zoals een veranderend marktaandeel) is een toepassing van het oplossen van stelsels. We zoeken een toestand `X` (een kolomvector) waarvoor geldt: `M * X = X`.

Dit herschrijven we als `(M - I) * X = 0`. Daarnaast voegen we de voorwaarde toe dat de som van de elementen in `X` gelijk moet zijn aan 1 (of 100%).

### Stappenplan in `wxMaxima`

```maxima
/* Voorbeeld: marktaandelen van 3 merken, x+y+z=1 */

/* 1. Definieer de Markov-matrix M */
M: matrix( [0.7, 0.2, 0.1], [0.1, 0.6, 0.2], [0.2, 0.2, 0.7] );

/* 2. Definieer de eenheidsmatrix I */
I: ident(3);

/* 3. Stel het stelsel (M-I)X = 0 op.
   De vergelijkingen zijn de rijen van (M-I), vermenigvuldigd met [x,y,z]
   en gelijkgesteld aan 0. Voeg de extra voorwaarde toe.
*/
stelsel: [
  (0.7-1)*x + 0.2*y + 0.1*z = 0,
  0.1*x + (0.6-1)*y + 0.2*z = 0,
  0.2*x + 0.2*y + (0.7-1)*z = 0,
  x+y+z=1
];

/* 4. Los het stelsel op met de methode uit H3 */
AB: augcoefmatrix(stelsel, [x,y,z]);
/* augcoefmatrix maakt [A|-B], hier is B [0,0,0,1], dus dat werkt prima. */

oplossing: rref(AB);

/* De laatste kolom van de resulterende matrix geeft de stabiele verdeling
   voor x, y, en z. */
```

Dit patroon is heel herkenbaar en een typische examenvraag. Het combineert matrixbewerkingen met het oplossen van stelsels.

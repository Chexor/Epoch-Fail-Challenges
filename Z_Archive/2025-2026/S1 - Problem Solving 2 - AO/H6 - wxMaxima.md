# H6 - wxMaxima Handleiding

[[H6 - Inleiding tot codeertheorie]]

Deze nota toont de `wxMaxima` commando's voor getaltheorie en cryptografie uit Hoofdstuk 6. Deze functies zijn essentieel voor de RSA-oefeningen.

## 1. Basis Getaltheorie

-   **Priemfactorontbinding:** `factor(n)`
-   **Grootste Gemene Deler (ggd):** `gcd(a, b)`
-   **Rest en Quotiënt bij deling:** `divide(a, b)` geeft een lijst `[quotiënt, rest]`.

```maxima
/* Ontbind 120 in priemfactoren */
factor(120); /* Output: 2^3 * 3 * 5 */

/* Bereken de ggd van 48 en 180 */
gcd(48, 180); /* Output: 12 */

/* Bereken quotiënt en rest van 100 / 7 */
divide(100, 7); /* Output: [14, 2] */
```

## 2. Modulorekenen

-   **Berekening:** `mod(a, n)` berekent de rest van `a` na deling door `n`. Dit is de kern van modulorekenen.
-   **Modulaire machtsverheffing:** `power_mod(a, k, n)` berekent `a^k mod n`. Dit is **extreem belangrijk** voor RSA, omdat het met gigantische getallen kan werken die `a^k` nooit volledig zou kunnen uitrekenen.
-   **Modulaire inverse:** `inv_mod(a, n)` berekent de inverse van `a` modulo `n`. Dit is de snelste manier om de privé-sleutel `d` te vinden in RSA.

```maxima
/* Bereken 25 mod 7 */
mod(25, 7); /* Output: 4 */

/* Bereken 5^123 mod 17 (onmogelijk met de hand) */
power_mod(5, 123, 17);

/* Bereken de inverse van 5 modulo 17 */
inv_mod(5, 17); /* Output: 7, want 5*7 = 35, en 35 mod 17 = 1 */
```

## 3. Euler's φ-functie

De `totient()` functie berekent `φ(n)`.

```maxima
/* Bereken phi van 15 */
totient(15); /* Output: 8 */

/* Bereken phi van een priemgetal 17 */
totient(17); /* Output: 16 */
```

## 4. RSA Stappenplan in `wxMaxima`

Hier is een volledig voorbeeld van hoe je een RSA-vraagstuk op het examen zou aanpakken.

**Gegeven:** `p=13`, `q=17`, `e=11`. Versleutel het bericht `B=88`.

```maxima
/* 1. Bereken n en phi(n) */
p: 13;
q: 17;
n: p*q;           /* Output: 221 */
phi_n: (p-1)*(q-1); /* Output: 192 */

/* 2. Bereken de geheime sleutel d.
      d is de inverse van e modulo phi_n. */
e: 11;
d: inv_mod(e, phi_n); /* Output: 35 */
/* Controle: mod(d*e, phi_n) moet 1 zijn. */

/* 3. Versleutel het bericht B=88. C = B^e mod n */
B: 88;
C: power_mod(B, e, n); /* Output: 11 */

/* 4. Ontcijfer het bericht C=11 om B terug te vinden. B = C^d mod n */
B_ontcijferd: power_mod(C, d, n); /* Output: 88. Het werkt! */
```

Deze functies (`power_mod`, `inv_mod`, `gcd`, `totient`) maken de RSA-oefeningen puur een kwestie van het correct toepassen van het stappenplan.

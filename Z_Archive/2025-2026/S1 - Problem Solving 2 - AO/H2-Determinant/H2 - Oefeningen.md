# H2 - Oefeningen Determinanten
#ps2 #oefeningen #wip

[[H2 - Determinanten]]

---

## Oefening 1: Parameter Vinden

### Opgave

Gegeven is de matrix A:
```
A = | 1  -1   2 |
    | m   2   1 |
    | 1   1  -1 |
```
Voor welke waarde(n) van de parameter `m` is deze matrix **singulier**?

### Zelf Oplossen
*Probeer de oefening eerst zelf op te lossen. Gebruik de Regel van Sarrus.*

...

### Uitwerking

**1. Gebruikte Concepten**
- [[Determinant: betekenis + berekening]]
- [[Singulier vs Inverteerbaar]]

**2. Stappenplan**
Een matrix is singulier als haar determinant gelijk is aan 0. We moeten dus de determinant van A berekenen, deze gelijkstellen aan 0, en de vergelijking oplossen voor `m`.

**3. Berekening (Regel van Sarrus)**
- Schrijf de eerste twee kolommen ernaast:
  ```
  | 1  -1   2 | 1  -1
  | m   2   1 | m   2
  | 1   1  -1 | 1   1
  ```
- Bereken de som van de producten van de diagonalen (↘):
  ` (1 * 2 * -1) + (-1 * 1 * 1) + (2 * m * 1) = -2 - 1 + 2m = 2m - 3 `
- Bereken de som van de producten van de anti-diagonalen (↗):
  ` (2 * 2 * 1) + (1 * 1 * 1) + (-1 * m * -1) = 4 + 1 + m = m + 5 `
- Trek de twee van elkaar af:
  ` det(A) = (2m - 3) - (m + 5) = 2m - 3 - m - 5 = m - 8 `

**4. Oplossen**
Stel de determinant gelijk aan 0:
`m - 8 = 0`
`m = 8`

**Conclusie:** De matrix A is singulier als `m = 8`.

### Verificatie met wxMaxima
```maxima
A: matrix( [1, -1, 2], [m, 2, 1], [1, 1, -1] );
det_A: determinant(A); /* Geeft m - 8 */
solve(det_A = 0, m);   /* Geeft [m=8] */
```

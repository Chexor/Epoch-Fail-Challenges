# Formularium-cheatsheet per oefening

## 🧭 Afgeleid (geen SSOT)
- Samenvatting voor snelle oefenkeuze.
- Formules blijven **authoritative** in het officiële formularium.

Doel: per oefening snel de juiste formules pakken uit het formularium.

## Oefening 1 (H1-H2) - Tabel, ogief, kengetallen, spreiding, scheefheid

### Kernformules
- Gegroepeerd gemiddelde: xbar = (sum m_i f_i) / n.
- Som: sum x_i = n * xbar.
- Mediaan (gegroepeerd): Me = l + ((n/2 - c f_(m-1)) / f_m) * b.
- Quartielen: Q1 = l + ((n/4 - c f_(q1-1)) / f_q1) * b, Q3 = l + ((3n/4 - c f_(q3-1)) / f_q3) * b.
- Modus (gegroepeerd): Mo = l + (Delta1 / (Delta1 + Delta2)) * b.
- Standaardafwijking: s = sqrt( (1/n) * sum (x_i - xbar)^2 ) of s = sqrt( X2bar - xbar^2 ).
- Som kwadraten: sum x_i^2 = n (s^2 + xbar^2).
- Scheefheid (Pearson): Sk_P = (xbar - Mo) / s.
- Scheefheid (Bowley): Sk_B = (Q3 + Q1 - 2 Me) / (Q3 - Q1).

### Wanneer gebruiken
- Gegroepeerd gemiddelde en variantie bij klassen.
- Interpolatieformules voor Me, Q1, Q3, Mo.
- Sk_P en Sk_B om scheefheid te duiden.

## Oefening 2 (H2) - Verwijderen min/max

### Kernformules
- sum x_i = n * xbar.
- sum x_i^2 = n (s^2 + xbar^2).
- xbar' = sum' x_i / n'.
- s'^2 = (sum' x_i^2 - n' xbar'^2) / (n' - 1).

### Wanneer gebruiken
- Als data wordt aangepast en je nieuwe xbar en s nodig hebt.

## Oefening 3 (H4) - Kansregels

### Kernformules
- P(A_bar) = 1 - P(A).
- P(A or B) = P(A) + P(B) - P(A and B).
- P(A and B) = P(A) P(B) (onafhankelijk).

### Wanneer gebruiken
- Geen van beide, beide, minstens een, A maar niet B.

## Oefening 4 (H4) - Bayes

### Kernformules
- P(A|B) = P(B|A) P(A) / P(B).
- P(B) = sum P(B|O_i) P(O_i) (wet van totale kans).

### Wanneer gebruiken
- Test/expertoordeel: kans op oorzaak gegeven positief resultaat.

## Oefening 5 (H5) - Joint tabel, X+Y, E en Var

### Kernformules
- E(X) = sum x_i P(X = x_i).
- Var(X) = sum (x_i - E(X))^2 P(X = x_i) = E(X^2) - (E(X))^2.
- E(X + Y) = E(X) + E(Y).
- Var(X + Y) = Var(X) + Var(Y) (als X en Y onafhankelijk).
- Var(X + Y) = Var(X) + Var(Y) + 2 Cov(X, Y) (algemeen).
- Cov(X, Y) = E(XY) - E(X) E(Y).

### Wanneer gebruiken
- Joint tabel om marges te maken, onafhankelijkheid checken en somverdeling opbouwen.

## Oefening 6 (H8) - Betrouwbaarheidsinterval (kleine n)

### Kernformules
- xbar ± t_(alpha/2) * (s / sqrt(n)).
- n = (z_(alpha/2) * sigma / a)^2 of n = (z_(alpha/2) * s / a)^2 (voor sample size).

### Wanneer gebruiken
- Sigma onbekend en n klein -> t-interval.

## Oefening 7 (H7-H9) - Steekproefgemiddelde en verschil

### Kernformules
- Z = (x - mu) / sigma.
- sigma_xbar = sigma / sqrt(n).
- Xbar ~ N(mu, sigma / sqrt(n)).
- Voor verschil: mu_(X-Y) = mu_X - mu_Y.
- sigma_(X-Y) = sqrt(sigma_X^2 + sigma_Y^2).

### Wanneer gebruiken
- Kans op afwijking van xbar of vergelijking van twee normalen.

## Oefening 8 (H6) - Binomiaal en normale benadering

### Kernformules
- Combinaties: C(n, k) = n! / (k! (n-k)!).
- Binomiaal: P(X = k) = C(n, k) p^k q^(n-k).
- Binomiaal parameters: E(X) = n p, sigma = sqrt(n p q).
- Normaal: Z = (X - mu) / sigma.

### Wanneer gebruiken
- Exacte kans met binomiaal; grote n -> normale benadering.

## Oefening 9 (H6) - Normaal en sigma afleiden

### Kernformules
- Z = (X - mu) / sigma.
- P(X < a) = p -> z_p uit tabel.

### Wanneer gebruiken
- Sigma bepalen uit percentiel; daarna kans berekenen.

## Oefening 10 (H10) - Toetsing verschil van gemiddelden

### Kernformules
- Z = (Xbar - mu_0) / (sigma / sqrt(n)).
- t = (Xbar - mu_0) / (s / sqrt(n-1)).
- Z = (Xbar - Ybar) / sqrt(s_x^2 / n_x + s_y^2 / n_y).
- t = (Xbar - Ybar) / sqrt( ((n_x - 1) s_x^2 + (n_y - 1) s_y^2) / (n_x + n_y - 2) * (1/n_x + 1/n_y) ).

### Wanneer gebruiken
- Een of twee steekproeven; kies z bij grote n of sigma bekend, t bij kleine n.

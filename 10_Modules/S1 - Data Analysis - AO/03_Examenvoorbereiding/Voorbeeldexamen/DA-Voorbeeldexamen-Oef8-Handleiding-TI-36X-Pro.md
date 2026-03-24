# Oefening 8 - Handleiding (TI-36X Pro)

Doel: binomiale kans exact (pdf) en een normale benadering met continuiteitscorrectie.

## Opgave

![[DA-Voorbeeldexamen-Oef8.png]]

## (a) Exact met binomiaal

Definieer $X$ = aantal afgekeurde stukken.

- $X\sim B(n=50,p=0.10)$
- Gevraagd: $P(X=5)$

TI:
1. `PRB` (DISTR/PROB)
2. Kies `binompdf(`
3. Vul in: `binompdf(50,0.10,5)`

## (b) Normale benadering voor $P(X\ge 30)$

Gegeven $X\sim B(200,0.10)$.

1. Parameters:
$$
\mu=np=200\cdot 0.10=20
$$
$$
\sigma=\sqrt{np(1-p)}=\sqrt{200\cdot 0.10\cdot 0.90}
$$

2. Continuiteitscorrectie:
$$
P(X\ge 30) \approx P(N\ge 29.5)
$$

TI:
- `normalcdf(29.5, 1E99, 20, sqrt(200*0.1*0.9))`

## Handige links

- [[DA-Voorbeeldexamen-TI-36X-Pro-Manual]]

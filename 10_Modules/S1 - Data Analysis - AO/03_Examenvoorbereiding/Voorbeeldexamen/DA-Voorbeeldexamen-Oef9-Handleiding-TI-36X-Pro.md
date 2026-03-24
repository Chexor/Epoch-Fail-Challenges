# Oefening 9 - Handleiding (TI-36X Pro)

Doel: bij normale verdeling $\sigma$ bepalen met een percentiel (invNorm), en daarna een kans met normalcdf.

## Opgave

![[DA-Voorbeeldexamen-Oef9.png]]

## Gegeven

- $X$ = inhoud (gram)
- $X\sim N(\mu=130,\sigma)$
- $P(X<125)=0.04$

## (a) Bereken $\sigma$

1. Zet om naar z:
$$
P\left(Z<\frac{125-130}{\sigma}\right)=0.04
$$

2. Vind $z$ met TI:
- `z = invNorm(0.04, 0, 1)`

3. Los op:
$$
z=\frac{-5}{\sigma} \Rightarrow \sigma=\frac{-5}{z}
$$

TI:
- `sigma = (-5)/z`

## (b) $P(X>132)$

TI:
- `normalcdf(132, 1E99, 130, sigma)`

## Handige links

- [[DA-Voorbeeldexamen-TI-36X-Pro-Manual]]

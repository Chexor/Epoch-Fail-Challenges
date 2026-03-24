# Oefening 4 - Handleiding (TI-36X Pro)

Doel: Bayes met een boomdiagram (expert zegt “authentiek”). TI gebruik je voor breuken/decimalen.

## Opgave

![[DA-Voorbeeldexamen-Oef4.png]]

## Gegeven

- 12 schilderijen: 10 authentiek, 2 vervalst
- Expert oordeelt in 9/10 gevallen juist

Definieer:
- $A$ = “authentiek”
- $E$ = “expert zegt: authentiek”

Dan:
- $P(A)=10/12$, $P(\bar{A})=2/12$
- $P(E\mid A)=0.9$
- $P(E\mid \bar{A})=0.1$ (expert fout als het vervalst is)

## Gevraagd: $P(A\mid E)$

### 1) Totale kans $P(E)$
$$
P(E)=P(E\mid A)P(A)+P(E\mid \bar{A})P(\bar{A})
$$
Reken op TI:
- `(10/12)*0.9 + (2/12)*0.1` -> 0.766666...

### 2) Bayes
$$
P(A\mid E)=\frac{P(E\mid A)P(A)}{P(E)}
$$
Reken op TI:
- `((10/12)*0.9) / 0.7666666667` -> 0.9783...

Conclusie: $P(A\mid E)\approx 97.83\%$.

## Handige links

- [[DA-Voorbeeldexamen-TI-36X-Pro-Manual]]

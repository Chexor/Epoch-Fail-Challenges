# Oefening 7 - Handleiding (TI-36X Pro)

Doel: kansen met normale verdelingen, steekproefgemiddelde, en verschil van 2 normalen. TI gebruik je voor `normalcdf(` (en eventueel z-werk).

## Opgave

![[DA-Voorbeeldexamen-Oef7.png]]

## (a) Kans dat $\bar{X}$ minstens 5 afwijkt

Gegeven: $X\sim N(38,9)$ en steekproefgrootte $n=6$.

1. Verdeling van het steekproefgemiddelde:
$$
\bar{X}\sim N\left(\mu,\frac{\sigma}{\sqrt{n}}\right)
$$
Dus $\mu_{\bar{X}}=38$ en $\sigma_{\bar{X}}=9/\sqrt{6}$.

2. Gevraagd:
$$
P(|\bar{X}-38|>5)=P(\bar{X}<33)+P(\bar{X}>43)
$$
Door symmetrie:
$$
P(|\bar{X}-38|>5)=2\,P(\bar{X}<33)
$$

TI (rechtstreeks met `normalcdf`):
- `p = normalcdf(-1E99, 33, 38, 9/sqrt(6))`
- antwoord = `2*p`

## (b) Kans dat klant in B langer wacht dan in A

Gegeven: $X\sim N(38,9)$ en $Y\sim N(35,10)$, onafhankelijk.

1. Zet om naar 1 normale:
Neem $D=X-Y$.
$$
D\sim N(\mu_X-\mu_Y,\sqrt{\sigma_X^2+\sigma_Y^2})
$$
Dus $\mu_D=3$ en $\sigma_D=\sqrt{9^2+10^2}=\sqrt{181}$.

2. Gevraagd:
$$
P(Y>X)=P(X-Y<0)=P(D<0)
$$

TI:
- `normalcdf(-1E99, 0, 3, sqrt(181))`

## Handige links

- [[DA-Voorbeeldexamen-TI-36X-Pro-Manual]]

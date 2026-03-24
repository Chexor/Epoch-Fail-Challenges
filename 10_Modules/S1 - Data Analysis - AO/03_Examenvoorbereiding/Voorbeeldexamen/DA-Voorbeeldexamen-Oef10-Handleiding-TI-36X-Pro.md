# Oefening 10 - Handleiding (TI-36X Pro)

Doel: eenzijdige t-toets voor verschil tussen 2 gemiddelden (2 onafhankelijke steekproeven), met grote df (kritieke waarde kan met t-tabel of z-benadering).

## Opgave

![[DA-Voorbeeldexamen-Oef10.png]]

## Gegeven

Landelijk:
- $n_1=70$, $\bar{x}_1=3.7$, $s_1=0.40$

Stedelijk:
- $n_2=85$, $\bar{x}_2=3.5$, $s_2=0.35$

## Stap 1: hypothesen (manueel)

Neem $X$ = landelijk, $Y$ = stedelijk.

- $H_0: \mu_X=\mu_Y$
- $H_1: \mu_X>\mu_Y$ (eenzijdig)

## Stap 2: gepoolde variantie (manueel + TI)

$$
s_p^2=\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}
$$

TI: typ de formule met haakjes.

Vrijheidsgraden:
$$
\nu=n_1+n_2-2=153
$$

## Stap 3: toetsingsgrootheid t

Standaardfout:
$$
SE=\sqrt{s_p^2\left(\frac{1}{n_1}+\frac{1}{n_2}\right)}
$$

Toetsingsgrootheid:
$$
t=\frac{\bar{x}_1-\bar{x}_2}{SE}
$$

TI: reken $SE$ en daarna $t$ uit.

## Stap 4: kritieke waarde en conclusie

Voor $\alpha=0.05$ (eenzijdig): $t_{0.95,153}\approx 1.645$.

Voor $\alpha=0.01$ (eenzijdig): $t_{0.99,153}\approx 2.33$.

Beslissing:
- Verwerp $H_0$ als $t$ groter is dan de kritieke waarde.

Interpretatie (taal in je conclusie):
- verwerpen bij 0.05: significant
- verwerpen bij 0.01: sterk significant

## Handige links

- [[DA-Voorbeeldexamen-TI-36X-Pro-Manual]]

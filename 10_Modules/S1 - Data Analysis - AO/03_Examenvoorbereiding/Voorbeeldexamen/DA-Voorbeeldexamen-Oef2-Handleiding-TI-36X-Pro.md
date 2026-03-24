# Oefening 2 - Handleiding (TI-36X Pro)

Doel: nieuw gemiddelde en nieuwe standaardafwijking na verwijderen van de kleinste en grootste waarde, zonder de volledige data te kennen.

## Opgave

![[DA-Voorbeeldexamen-Oef2.png]]

## Gegeven

- $n = 10$
- $\min = 24.5$, $\max = 64.5$
- $\bar{X} = 42.5$
- $s = 10.0$ (hier met noemer $n$ in de variantieformule)

## Stappen (manueel + TI als rekenmachine)

### 1) Totale som $\sum X_i$
Formule:
$$
\sum X_i = n\bar{X}
$$
Reken op TI:
- `10*42.5` -> 425

### 2) Totale som kwadraten $\sum X_i^2$
Gebruik (met noemer $n$):
$$
s^2 = \frac{1}{n}\sum X_i^2 - \bar{X}^2
\Rightarrow \sum X_i^2 = n(s^2+\bar{X}^2)
$$
Reken op TI:
- `10*(10^2+42.5^2)` -> 19062.5

### 3) Verwijder $\min$ en $\max$

Nieuwe som:
$$
\sum X_i(\text{nieuw}) = 425 - 24.5 - 64.5 = 336
$$

Nieuwe som kwadraten:
$$
\sum X_i^2(\text{nieuw}) = 19062.5 - 24.5^2 - 64.5^2 = 14302
$$

Nieuwe steekproefgrootte: $n_{nieuw}=8$.

### 4) Nieuw gemiddelde en nieuwe s

Nieuw gemiddelde:
$$
\bar{X}_{nieuw} = \frac{336}{8} = 42
$$

Nieuwe standaardafwijking (zelfde noemer-conventie als gegeven):
$$
s_{nieuw} = \sqrt{\frac{14302}{8} - 42^2} = 4.8734
$$

## Handige links

- [[DA-Voorbeeldexamen-Oef2-Samenvatting]]
- [[DA-Voorbeeldexamen-TI-36X-Pro-Manual]]

# Oefening 5 - Handleiding (TI-36X Pro)

Doel: werken met een gezamenlijke kansverdeling (tabel), onafhankelijkheid, verdeling van $S=X+Y$, en dan $E(S)$ en $Var(S)$.

## Opgave

![[DA-Voorbeeldexamen-Oef5.png]]

## Gegeven

- $X\in\{1,2,3\}$
- $Y\in\{1,2\}$
- Gezamenlijke kansverdeling $P(X=x, Y=y)$ in een tabel met rij- en kolomtotaal.

## (a) Tabel vervolledigen (manueel)

Regels:
- Elke rij moet optellen tot zijn rijtotaal.
- Elke kolom moet optellen tot zijn kolomtotaal.
- Groot totaal is 1.

Werkwijze:
1. Vul eerst waar een rij/kolom maar 1 ontbrekende cel heeft.
2. Controleer op het einde dat alles optelt tot 1.

TI: enkel voor optellen/aftrekken.

## (b) Onafhankelijk of niet?

Test:
$$
\text{onafhankelijk} \iff P(X=x,Y=y)=P(X=x)P(Y=y)\ \text{voor alle }x,y
$$

Praktisch:
1. Neem 1 cel (bv. $X=1, Y=1$).
2. Bereken $P(X=1)$ (kolomtotaal) en $P(Y=1)$ (rijtotaal).
3. Vergelijk.

Als 1 vergelijking faalt: afhankelijk.

## (c) Kansverdeling van $S=X+Y$ (manueel)

1. Noteer mogelijke sommen: 2, 3, 4, 5.
2. Voor elke som tel je de cellen op die die som geven.

Voorbeeld:
- $P(S=2)=P(X=1,Y=1)$
- $P(S=3)=P(2,1)+P(1,2)$
- $P(S=4)=P(3,1)+P(2,2)$
- $P(S=5)=P(3,2)$

Teken daarna een staafdiagram: x-as = som, y-as = kans.

## (d) $E(S)$ en $Var(S)$ (TI als rekenmachine)

Formules:
$$
E(S)=\sum s\,P(S=s)
$$
$$
Var(S)=\sum s^2\,P(S=s) - (E(S))^2
$$

TI-tip: typ de sommen rechtstreeks in (met haakjes).

## Handige links

- [[DA-Voorbeeldexamen-TI-36X-Pro-Manual]]

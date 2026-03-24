# Oefening 6 - Handleiding (TI-36X Pro)

Doel: 95%-betrouwbaarheidsinterval voor het gemiddelde bij kleine steekproef ($n=6$). TI gebruik je voor 1-Var Stats en rekenwerk.

## Opgave

![[DA-Voorbeeldexamen-Oef6.png]]

## Gegeven

Metingen (verschil in bloeddruk): 1.7, 3.0, 0.8, 3.4, 2.7, 2.1.

## Stap 1: $\bar{X}$ en standaardafwijking uitrekenen (TI)

1. `DATA`
2. Zet de 6 waarden in L1.
3. `STAT` -> `1-VAR` met Xlist = L1.
4. Lees af:
   - `xbar`
   - `Sx` en `sigma x`

In de voorbeeldoplossing wordt met `sigma x` gewerkt en daarna gedeeld door $\sqrt{n-1}$.

## Stap 2: t-kritieke waarde

- 95% tweezijdig: gebruik $t_{0.975}$ met $\nu=n-1=5$.
- In de oplossing: $t_{0.975}\approx 2.57$.

Als je TI een `invT(` functie heeft: neem kans 0.975 en df 5.

## Stap 3: Betrouwbaarheidsinterval

Consistent met de voorbeeldoplossing:
$$
\bar{X} \pm t_{0.975}\,\frac{\sigma}{\sqrt{n-1}}
$$

Reken op TI:
1. `marge = t * sigma / sqrt(5)`
2. ondergrens = `xbar - marge`
3. bovengrens = `xbar + marge`

## Handige links

- [[DA-Voorbeeldexamen-TI-36X-Pro-Manual]]

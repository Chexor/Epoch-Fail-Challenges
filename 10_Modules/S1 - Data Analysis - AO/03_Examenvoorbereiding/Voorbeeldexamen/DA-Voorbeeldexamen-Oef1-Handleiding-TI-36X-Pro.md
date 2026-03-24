# Oefening 1 - Handleiding (TI-36X Pro)

Doel: stap voor stap Oefening 1 oplossen met duidelijke splitsing:
- wat je manueel doet (tabel, grafieken, interpolatie)
- wat je TI-36X Pro snel kan uitrekenen (xbar, (sigma)x, rekenwerk)

## Opgave

![[DA-Voorbeeldexamen-Oef1.png]]

## Gegeven

- Aantal studenten: $n = 110$.
- Klassen (uren/week): 1-6, 7-12, 13-18, 19-24, 25-30.
- Frequenties: $f_i =$ 22, 39, 28, 15, 6.

## (a) Frequentietabel aanvullen (manueel)

### 1) Intervalgrenzen (continue grenzen)
Omdat er is afgerond op het uur, gebruik je een continuiteitscorrectie van 0.5.

- 1-6  -> 0.5-6.5
- 7-12 -> 6.5-12.5
- 13-18 -> 12.5-18.5
- 19-24 -> 18.5-24.5
- 25-30 -> 24.5-30.5

Klassenbreedte: $h = 6$.

### 2) Intervalmiddelen
Formule: $m_i = \frac{\text{ondergrens} + \text{bovengrens}}{2}$.

- 3.5, 9.5, 15.5, 21.5, 27.5

### 3) Cumulatieve absolute frequenties
Formule: $cf_i = \sum_{k=1}^{i} f_k$.

- 22, 61, 89, 104, 110

### 4) Cumulatieve relatieve frequenties (in %)
Formule: $ch_i = 100 \cdot cf_i / n$.

- 20.00, 55.45, 80.91, 94.55, 100.00

Je TI-36X Pro gebruik je hier vooral voor de delingen (bv. `61/110*100`).

## (b) Histogram tekenen (manueel)

Omdat alle klassen even breed zijn ($h=6$), mag je de staafhoogte gelijk nemen aan $f_i$.

1. Zet op de x-as de intervalgrenzen: 0.5 | 6.5 | 12.5 | 18.5 | 24.5 | 30.5.
2. Teken 5 aaneensluitende rechthoeken met hoogtes: 22, 39, 28, 15, 6.

## (b) Ogief tekenen + kwartielen schatten (manueel)

### 1) Ogief
Gebruik punten (bovengrens, cumulatief) en start met (0.5, 0).

- (0.5, 0)
- (6.5, 22)
- (12.5, 61)
- (18.5, 89)
- (24.5, 104)
- (30.5, 110)

Verbind de punten met rechte lijnstukken of een vloeiende stijgende lijn.

### 2) Q1, Me, Q3 grafisch (ruwe schatting)

- $Q_1$ ligt bij 25%: $0.25n = 27.5$
- $Me$ ligt bij 50%: $0.50n = 55$
- $Q_3$ ligt bij 75%: $0.75n = 82.5$

Op de ogief:
1. Trek horizontaal vanaf 27.5, 55, 82.5 naar de curve.
2. Ga verticaal naar de x-as en lees de x-waarde af.

## (b)/(d) Kwartielen en mediaan via interpolatie (manueel + TI als rekenmachine)

Algemene interpolatieformule (gegroepeerde data):
$$
\text{waarde} = L + \frac{\text{positie} - cf_{\text{voor}}}{f_{\text{klasse}}} \cdot h
$$

Waar:
- $L$ = ondergrens van de klasse
- $h$ = klassenbreedte
- $cf_{\text{voor}}$ = cumulatief aantal voor de klasse
- $f_{\text{klasse}}$ = frequentie van de klasse

Posities:
- $Q_1$: $n/4 = 27.5$ (valt in klasse 6.5-12.5)
- $Me$: $n/2 = 55$ (valt in klasse 6.5-12.5)
- $Q_3$: $3n/4 = 82.5$ (valt in klasse 12.5-18.5)

Voorbeeld (mediaan):
$$
Me = 6.5 + \frac{55 - 22}{39} \cdot 6 = 11.58
$$

## (c) Gemiddelde xbar (TI-36X Pro)

Voor gegroepeerde data gebruik je de intervalmiddelen als representatieve waarden.

Manueel idee:
$$
\bar{X} = \frac{\sum f_i m_i}{n}
$$

Op TI-36X Pro (1-Var Stats met frequenties):
1. `DATA`
2. L1: 3.5, 9.5, 15.5, 21.5, 27.5
3. L2: 22, 39, 28, 15, 6
4. `2nd` `MODE` (QUIT)
5. `STAT` -> `1-VAR`
6. Stel in: Xlist = L1, Freq = L2
7. Lees af: `xbar`

Verwacht: $\bar{X} \approx 12.45$.

## (d) Mediaan Me (manueel + TI voor rekenwerk)

Mediaanpositie: $n/2 = 55$.

Mediaanklasse: 6.5-12.5 (want $cf$ gaat van 22 naar 61).

$$
Me = 6.5 + \frac{55 - 22}{39} \cdot 6 = 11.58
$$

## (e) Modus Mo (manueel + TI voor rekenwerk)

Modale klasse: hoogste frequentie = 6.5-12.5.

- $d_1 = f_{mod} - f_{vorige} = 39 - 22 = 17$
- $d_2 = f_{mod} - f_{volgende} = 39 - 28 = 11$

$$
Mo = 6.5 + \frac{17}{17+11} \cdot 6 = 10.14
$$

## (f) Standaardafwijking (TI-36X Pro)

Gebruik dezelfde invoer als bij (c) (middenpunten + frequenties) en lees af in `1-VAR`:
- `sigma x` (noemer $n$)
- `Sx` (noemer $n-1$)

In dit voorbeeld wordt met noemer $n$ gewerkt, dus neem `sigma x`.

Verwacht: $\sigma \approx 6.708$.

## (g) Pearson scheefheidscoefficient

$$
Sk_p = \frac{\bar{X} - Mo}{\sigma}
$$

Verwacht:
$$
Sk_p \approx \frac{12.45 - 10.14}{6.708} = 0.34
$$

Interpretatie: lichte positieve scheefheid (rechtsscheef). Dat past bij $Mo < Me < \bar{X}$.

## Handige links

- [[DA-Voorbeeldexamen-Oef1-Samenvatting]]
- [[DA-Voorbeeldexamen-TI-36X-Pro-Manual]]

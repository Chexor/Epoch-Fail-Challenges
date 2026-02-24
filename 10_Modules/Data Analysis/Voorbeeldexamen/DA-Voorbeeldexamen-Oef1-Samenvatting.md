# Oefening 1 - Finale samenvatting (zonder voorkennis)

## Opgave

![[Pasted image 20260224163957.png]]
## Gegeven
- Aantal studenten: $n = 110$.
- Klassen: 1-6, 7-12, 13-18, 19-24, 25-30.
- Frequenties: 22, 39, 28, 15, 6.


## (a) Intervalgrenzen, middenpunten en cumulatieven
Omdat er op hele uren is afgerond, neem je grenzen op halve uren.
Zo sluit je de klassen netjes op elkaar aan en kun je lineair interpoleren.
- Grenzen: 0.5-6.5, 6.5-12.5, 12.5-18.5, 18.5-24.5, 24.5-30.5.
- Middenpunten: 3.5, 9.5, 15.5, 21.5, 27.5.
Formule: $X_i = (\text{ondergrens} + \text{bovengrens}) / 2$.

### Cumulatieve frequenties
- Dit is handig omdat je meteen ziet hoeveel studenten onder een grens vallen.
- Cumulatief absoluut: 22, 61, 89, 104, 110.
- Cumulatief relatief (in %): 20.20, 55.45, 80.91, 94.55, 100.00.
Formule: $cf_i = \sum_{k=1}^{i} f_k$, en $ch_i = 100 \cdot cf_i / n$.

## (b) Ogief en kwartielen
Teken de punten met (bovenste grens, cumulatief aantal).
- Punten: (6.5, 22), (12.5, 61), (18.5, 89), (24.5, 104), (30.5, 110).

![[Pasted image 20260224164522.png]]

Kwartielen liggen bij 25%, 50%, 75% van 110:
- 25% = 27.5, 50% = 55, 75% = 82.5.
De ogief is een stijgende lijn; met rechte stukjes tussen punten kun je waarden aflezen.
Ruwe schatting uit de grafiek: $Q_1 \approx 7$, $Me \approx 11.5$, $Q_3 \approx 17$.
Formule: $Q_1 = L + \frac{\frac{n}{4} - cf_{Q1-1}}{f_{Q1}} \cdot h$.
Formule: $Q_3 = L + \frac{\frac{3n}{4} - cf_{Q3-1}}{f_{Q3}} \cdot h$.

### Rekenstappen (b) Q1
- Klasse: 7-12.
- $L = 6.5$, $h = 6$, $cf_{\text{voor}} = 22$, $f = 39$.
- Aandeel $= (27.5 - 22) / 39 = 0.1410$.
- $Q_1 = 6.5 + 0.1410 \cdot 6 = 7.35$.

### Rekenstappen (b) Q3
- Klasse: 13-18.
- $L = 12.5$, $h = 6$, $cf_{\text{voor}} = 61$, $f = 28$.
- Aandeel $= (82.5 - 61) / 28 = 0.7679$.
- $Q_3 = 12.5 + 0.7679 \cdot 6 = 17.11$.

## (c) Gemiddelde
Gebruik de middenpunten als representatieve waarden.
Dat is een schatting, omdat je niet de exacte uren binnen elke klasse kent.
Formule: $\bar{X} = \frac{\sum f_i X_i}{n}$.

### Rekenstappen (c)
- 3.5 * 22 = 77
- 9.5 * 39 = 370.5
- 15.5 * 28 = 434
- 21.5 * 15 = 322.5
- 27.5 * 6 = 165
- Som = 1369
- $\bar{X} = 1369 / 110 = 12.45$

## (d) Mediaan
De mediaan ligt in de klasse waar het cumulatief aantal de 55 overschrijdt.
- Mediaanklasse: 7-12.
Je verdeelt de klasse lineair, alsof de waarden gelijkmatig verdeeld zijn.
Formule: $Me = L + \frac{\frac{n}{2} - cf_{m-1}}{f_m} \cdot h$.

### Rekenstappen (d)
- $L = 6.5$, $h = 6$, $cf_{\text{voor}} = 22$, $f = 39$.
- Aandeel $= (55 - 22) / 39 = 0.8462$.
- $Me = 6.5 + 0.8462 \cdot 6 = 11.58$.

## (e) Modus
De modale klasse heeft de hoogste frequentie.
- Modale klasse: 7-12.
De modus is het meest voorkomende aantal uren, geschat binnen die klasse.
Formule: $Mo = L + \frac{\Delta_1}{\Delta_1 + \Delta_2} \cdot h$.

### Rekenstappen (e)
- $f_1 = 39$, $f_0 = 22$, $f_2 = 28$.
- $L = 6.5$, $h = 6$.
- Teller $= 39 - 22 = 17$.
- Noemer $= 2 \cdot 39 - 22 - 28 = 28$.
- $Mo = 6.5 + (17/28) \cdot 6 = 10.14$.

## (f) Standaardafwijking
Gebruik de formule met $\sum f_i X_i^2$.
Dit geeft aan hoe ver de waarden gemiddeld van het gemiddelde af liggen.
Formule: $s = \sqrt{\frac{1}{n} \sum f_i X_i^2 - \bar{X}^2}$.

### Rekenstappen (f)
- $22 \cdot 3.5^2 = 269.5$
- $39 \cdot 9.5^2 = 3522.75$
- $28 \cdot 15.5^2 = 6727$
- $15 \cdot 21.5^2 = 6933.75$
- $6 \cdot 27.5^2 = 4537.5$
- $\sum f_i X_i^2 = 21990.5$
- $s^2 = 21990.5 / 110 - 12.45^2 = 45.00$
- $s = \sqrt{45.00} = 6.708$

## (g) Scheefheid (Pearson)
Rechts-scheef als gemiddelde > mediaan > modus.
De Pearson-coefficient zet dit om naar één getal om de scheefheid te meten.
Formule: $Sk_p = \frac{\bar{X} - Mo}{s}$.

### Rekenstappen (g)
- $Sk_p = (12.45 - 10.14) / 6.708 = 0.34$.

## Betekenis van symbolen (met voorbeeld)
- $n$: totaal aantal studenten (hier 110).
- $f_i$: frequentie per klasse (bijv. 39).
- $cf$: cumulatieve frequentie (bijv. 61).
- $L$: ondergrens van klasse (bijv. 6.5).
- $h$: klassenbreedte (hier 6).
- $X_i$: middenpunt (bijv. 9.5).
- $\bar{X}$: gemiddelde (12.45).
- $Me$: mediaan (11.58).
- $Mo$: modus (10.14).
- $Q_1$, $Q_3$: kwartielen (7.35 en 17.11).
- $s$: standaardafwijking (6.708).

## Gebruikte formules (uit het formularium)

Rekenkundig gemiddelde:
$$
\bar{X} = \frac{\sum f_i X_i}{n}
$$

Mediaan (gegroepeerde gegevens):
$$
Me = L + \frac{\frac{n}{2} - cf_{m-1}}{f_m} \cdot h
$$

Kwartielen:
$$
Q_1 = L + \frac{\frac{n}{4} - cf_{Q1-1}}{f_{Q1}} \cdot h
$$

$$
Q_3 = L + \frac{\frac{3n}{4} - cf_{Q3-1}}{f_{Q3}} \cdot h
$$

Modus:
$$
Mo = L + \frac{\Delta_1}{\Delta_1 + \Delta_2} \cdot h
$$

Standaardafwijking (alternatief):
$$
s = \sqrt{\frac{1}{n} \sum f_i X_i^2 - \bar{X}^2}
$$

Scheefheid (Pearson):
$$
Sk_p = \frac{\bar{X} - Mo}{s}
$$

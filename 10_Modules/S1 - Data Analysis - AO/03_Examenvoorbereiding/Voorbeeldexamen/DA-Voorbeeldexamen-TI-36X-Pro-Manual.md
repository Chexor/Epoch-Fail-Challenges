# TI-36X Pro - Stappenplan Voorbeeldexamen (Data Analysis)

Gebruik dit als "knoppenrecept" bij:
- [[DA-Voorbeeldexamen-Oef1.png]]
- [[DA-Voorbeeldexamen-Oef2.png]]
- [[DA-Voorbeeldexamen-Oef3.png]]
- [[DA-Voorbeeldexamen-Oef4.png]]
- [[DA-Voorbeeldexamen-Oef5.png]]
- [[DA-Voorbeeldexamen-Oef6.png]]
- [[DA-Voorbeeldexamen-Oef7.png]]
- [[DA-Voorbeeldexamen-Oef8.png]]
- [[DA-Voorbeeldexamen-Oef9.png]]
- [[DA-Voorbeeldexamen-Oef10.png]]

## Voor je start (altijd doen)
1. Werk in decimalen (niet in breuken), tenzij je oefening expliciet breuken wil.
2. Gebruik haakjes. Alles met /, macht, wortel: altijd haakjes rond teller/noemer.
3. Als je met data werkt: maak je lijsten leeg voordat je iets nieuws invoert.
4. Sla tussentijdse resultaten op:
   - Na een berekening: `STO>` -> kies een letter
   - Later: `RCL` -> die letter

## Knoppen/menus die je het meest gebruikt
- `DATA`: waarden (en evt. frequenties) invoeren in lijsten.
- `STAT`: 1-Variabele statistiek (gemiddelde, s, ...).
- `PRB` (of DISTR/PROB menu): kansen en verdelingen.
  - `normalcdf(`, `invNorm(`, `binompdf(`, `binomcdf(` (en soms ook `tcdf(` / `invT(`).
- `2nd`: tweede functie van knoppen.

## Belangrijke keuze: s met n of met (n-1)
Je TI toont vaak twee standaardafwijkingen:
- `Sx` = met (n-1) in de noemer (klassieke steekproef-s)
- `σx` = met n in de noemer (populatie-s)

In dit vak worden soms formules gebruikt met noemer n (je ziet dat in het voorbeeldexamen).
1. Als de oplossing werkt met noemer n: gebruik `σx`.
2. Als de oplossing werkt met noemer (n-1): gebruik `Sx`.

Voor standaardfout (SE) bij betrouwbaarheidsintervallen:
- Werk je met `Sx`: SE = Sx / sqrt(n)
- Werk je met `σx`: SE = σx / sqrt(n-1)
  (dit is gelijkwaardig, zolang je consistent blijft)

---

## Oefening 1 (gegroepeerde data: xbar, Me, Mo, s, ogief, kwartielen, scheefheid)
Doel: uit een frequentietabel snel xbar en s met TI; kwartielen/mediaan/modus doe je met interpolatie.

### 1) Gemiddelde en standaardafwijking (via middenpunten + frequenties)
1. Bereken op papier de middenpunten van elke klasse.
2. `DATA`
3. Vul L1 met de middenpunten (bv. 3.5, 9.5, 15.5, 21.5, 27.5).
4. Vul L2 met de frequenties (bv. 22, 39, 28, 15, 6).
5. `STAT` -> kies `1-VAR`
6. Stel in:
   - Xlist = L1
   - Freq  = L2
7. Lees af:
   - `xbar` (gemiddelde)
   - `σx` (standaardafwijking met noemer n) of `Sx` (met n-1), afhankelijk van je formule.

### 2) Mediaan (Me) en kwartielen (Q1, Q3) via interpolatie
1. Bereken n (totaal) en cumulatieve frequenties (cf).
2. Bepaal positie:
   - Q1 zit bij 0.25 * n
   - Me zit bij 0.50 * n
   - Q3 zit bij 0.75 * n
3. Zoek de klasse waar die positie in valt (via cf).
4. Interpoleer met TI (als rekenmachine):
   - waarde = L + ((positie - cf_voor) / f_klasse) * h
   - L = ondergrens, h = klassenbreedte

### 3) Modus (Mo) in gegroepeerde data
1. Zoek modale klasse (hoogste frequentie).
2. Gebruik modusformule (TI rekent):
   - Mo = L + (Δ1 / (Δ1 + Δ2)) * h
   - Δ1 = f_mod - f_vorige
   - Δ2 = f_mod - f_volgende

### 4) Pearson scheefheid
1. Neem xbar, Mo en s.
2. Skp = (xbar - Mo) / s
3. Interpretatie:
   - Skp > 0: rechtsscheef
   - Skp < 0: linksscheef
   - |Skp| klein (bv. < 0.5): lichte scheefheid

---

## Oefening 2 (nieuw xbar en s na verwijderen kleinste + grootste)
Gegeven: n, xbar, s, min, max. Gevraagd: nieuw xbar en nieuw s.

1. Bereken som:
   - somX = n * xbar
2. Bereken som van kwadraten (als je formule met noemer n gebruikt):
   - somX2 = n * (s^2 + xbar^2)
3. Verwijder min en max:
   - somX_nieuw  = somX  - min - max
   - somX2_nieuw = somX2 - min^2 - max^2
   - n_nieuw = n - 2
4. Nieuw gemiddelde:
   - xbar_nieuw = somX_nieuw / n_nieuw
5. Nieuwe standaardafwijking (noemer n):
   - s_nieuw = sqrt( (somX2_nieuw / n_nieuw) - (xbar_nieuw)^2 )

---

## Oefening 3 (kansen met onafhankelijke gebeurtenissen)
Hier gebruikt je TI vooral als rekenmachine.

1. Complementen:
   - P(niet A) = 1 - P(A)
2. Onafhankelijk:
   - P(A en B) = P(A) * P(B)
3. "Minstens 1":
   - P(A of B) = P(A) + P(B) - P(A en B)
4. "A maar niet B":
   - P(A en niet B) = P(A) * (1 - P(B))

---

## Oefening 4 (Bayes: expert beslist "authentiek")
Definieer:
- A = echt
- E = expert zegt "echt"

1. Zet alle kansen op papier:
   - P(A) en P(niet A)
   - P(E | A) (expert juist bij echt)
   - P(E | niet A) (expert fout bij vals)
2. Totale kans:
   - P(E) = P(E|A)*P(A) + P(E|niet A)*P(niet A)
3. Gevraagde kans:
   - P(A|E) = (P(E|A)*P(A)) / P(E)
4. Alles is: vermenigvuldigen, optellen, delen (TI als rekenmachine).

---

## Oefening 5 (gezamenlijke kansverdeling, onafhankelijkheid, verdeling van X+Y, E en Var)
### (a) Tabel vervolledigen
1. Gebruik rij/kolomtotaal:
   - Rij moet optellen tot rijtotaal.
   - Kolom moet optellen tot kolomtotaal.
   - Groot totaal = 1.

### (b) Onafhankelijk?
1. Neem 1 cel, bv. P(X=1 en Y=1).
2. Bereken marginaal:
   - P(X=1) = rijtotaal
   - P(Y=1) = kolomtotaal
3. Check:
   - Als P(X=1 en Y=1) niet gelijk is aan P(X=1)*P(Y=1) -> afhankelijk.

### (c) Verdeling van S = X + Y
1. Maak een lijst van mogelijke sommen (bv. 2, 3, 4, 5).
2. Voor elke som: tel de bijhorende cellen op uit de tabel.

### (d) E(S) en Var(S)
1. E(S) = som van (s * P(S=s))
2. Var(S) = som van (s^2 * P(S=s)) - (E(S))^2

---

## Oefening 6 (95% betrouwbaarheidsinterval voor gemiddelde, n klein)
1. `DATA`
2. Zet de 6 metingen in L1.
3. `STAT` -> `1-VAR` met Xlist = L1.
4. Noteer:
   - xbar
   - `Sx` en `σx`
5. Kies je formule (consistent):
   - Met `Sx`: SE = Sx / sqrt(n)
   - Met `σx`: SE = σx / sqrt(n-1)
6. Zoek t-kritiek voor 95% en df = n-1 in je t-tabel.
   - Als je TI een `invT(` functie heeft: gebruik die i.p.v. tabel.
7. Interval:
   - onder = xbar - t * SE
   - boven = xbar + t * SE

---

## Oefening 7 (normaal + steekproefgemiddelde + verschil van 2 normalen)
### (a) Kans dat Xbar minstens 5 afwijkt
1. Reken sigma_xbar = sigma / sqrt(n)
2. Gebruik `PRB` -> `normalcdf(`
   - P(Xbar < mu-5) = normalcdf(-1E99, mu-5, mu, sigma_xbar)
   - Door symmetrie: antwoord = 2 * die kans

### (b) Kans dat wachttijd in B groter is dan in A
1. Neem D = X - Y.
2. mu_D = mu_X - mu_Y
3. sigma_D = sqrt(sigma_X^2 + sigma_Y^2) (bij onafhankelijk)
4. Gevraagd P(Y > X) = P(X - Y < 0):
   - normalcdf(-1E99, 0, mu_D, sigma_D)

---

## Oefening 8 (binomiaal + normale benadering)
### (a) Exact P(X = 5) met binomiaal
1. `PRB` -> `binompdf(n, p, x)`
2. Vul n=50, p=0.10, x=5.

### (b) Normale benadering voor P(X >= 30)
1. mu = n*p
2. sigma = sqrt(n*p*(1-p))
3. Continuiteitscorrectie:
   - P(X >= 30) ~ P(N >= 29.5)
4. `PRB` -> `normalcdf(29.5, 1E99, mu, sigma)`

---

## Oefening 9 (normaal: sigma uit percentiel + kans)
### (a) Bepaal sigma uit P(X < 125) = 0.04
1. `PRB` -> `invNorm(0.04, 0, 1)` geeft z.
2. Gebruik: z = (125 - mu) / sigma
3. Oplossen:
   - sigma = (125 - mu) / z

### (b) P(X > 132)
1. `PRB` -> `normalcdf(132, 1E99, mu, sigma)`

---

## Oefening 10 (1-zijdige toets: verschil tussen 2 gemiddelden)
Gegeven: n1, xbar1, s1 en n2, xbar2, s2.

1. Bereken gepoolde variantie:
   - sp2 = ((n1-1)*s1^2 + (n2-1)*s2^2) / (n1 + n2 - 2)
2. Standaardfout:
   - SE = sqrt(sp2 * (1/n1 + 1/n2))
3. Testwaarde:
   - t = (xbar1 - xbar2) / SE
4. Kritieke waarde (1-zijdig):
   - Als je TI `invT(` heeft: gebruik df = n1+n2-2 en kans 1-alpha.
   - Anders: benader met z via `invNorm(1-alpha, 0, 1)` (werkt goed bij grote df).
5. Beslissing:
   - verwerp H0 als t > kritieke waarde
6. Label:
   - alpha 0.05 en verwerpen: "significant"
   - alpha 0.01 en verwerpen: "sterk significant"

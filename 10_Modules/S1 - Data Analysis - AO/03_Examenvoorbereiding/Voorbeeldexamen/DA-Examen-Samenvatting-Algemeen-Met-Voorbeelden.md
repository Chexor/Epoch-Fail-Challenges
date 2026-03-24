# Data Analysis - Algemene samenvatting (met voorbeelden)

Doel: 1 document om snel te herhalen voor het examen.
Ik leg de concepten uit met concrete mini-voorbeelden uit het voorbeeldexamen (vooral oef. 1).

Handig erbij:
- [[DA-Voorbeeldexamen-TI-36X-Pro-Cheat-Sheet]]
- [[DA-Examen-Samenvatting-Laatst]]
- Statistische tabellen (binomiaal, Poisson, Z, t)

## 0) Eerste reflex op examen

- Schrijf eerst: wat is de toevalsvariabele / welke grootheid? (X = ...)
- Is de data gegroepeerd in klassen of zijn het losse waarden?
- Werk je met kansen (0..1) of met percentages (0..100)? Zet het meteen juist.
- Als je een formule kiest: blijf consistent (noemer n of n-1 voor spreiding).

## 1) Beschrijvende statistiek (oef. 1 als voorbeeld)

Voorbeeldcontext: 110 studenten, uren social media per week, gegroepeerd in klassen met frequenties.

### 1.1 Klassen: grenzen en middenpunten

- Als er afgerond is op hele uren: maak klassen “continu” met 0.5-correctie.
  - vb. 1-6 wordt 0.5-6.5
- Middenpunt m van een klasse = (ondergrens + bovengrens) / 2
  - vb. 0.5-6.5 heeft m = 3.5

Waarom? Omdat je binnen een klasse niet alle exacte waarden kent. Je vervangt de hele klasse door 1 representatieve waarde (het middenpunt).

### 1.2 Cumulatieven (voor ogief, mediaan, kwartielen)

- Cumulatief absoluut cf = “totaal tot en met deze klasse”
  - vb. als de frequenties 22, 39, 28, ... zijn: cf wordt 22, 61, 89, ...
- Cumulatief relatief (in %) = 100 * cf / n
  - vb. cf = 61 bij n=110 -> 61/110*100 = 55.45%

### 1.3 Histogram vs ogief

- Histogram (klassen): staaf per klasse.
  - Bij gelijke klassenbreedte mag staafhoogte = frequentie.
- Ogief: stijgende lijn door punten (bovengrens, cumulatief).
  - vb. (6.5, 22), (12.5, 61), ...

### 1.4 Gemiddelde bij gegroepeerde data

Idee: “gewogen gemiddelde” met middenpunten.

- xbar = (som van fi * mi) / n
  - mi = middenpunt van klasse
  - fi = frequentie van klasse

Interpretatie:
- xbar is het langetermijngemiddelde als je heel vaak studenten zou meten.
- Bij gegroepeerde data is het een schatting (want je gebruikt middenpunten).

### 1.5 Mediaan en kwartielen bij gegroepeerde data (interpolatie)

Stapplan:
1) Zoek de positie:
   - Q1-positie = 0.25*n
   - Me-positie = 0.50*n
   - Q3-positie = 0.75*n
2) Zoek de klasse waar die positie in valt via cf.
3) Interpoleer binnen die klasse alsof de data daar gelijkmatig verdeeld is.

Rekenrecept:
- waarde = L + ((positie - cf_voor) / f_klasse) * h
  - L = ondergrens van de klasse
  - cf_voor = cumulatief aantal voor die klasse
  - f_klasse = frequentie van die klasse
  - h = klassenbreedte

Interpretatie:
- Mediaan = “50% zit eronder”.
- Q1 = “25% zit eronder”. Q3 = “75% zit eronder”.

### 1.6 Modus bij gegroepeerde data

Stapplan:
1) Zoek modale klasse: hoogste frequentie.
2) Corrigeer binnen die klasse met de buren.

Rekenrecept:
- Mo = L + (d1 / (d1 + d2)) * h
  - d1 = f_mod - f_vorige
  - d2 = f_mod - f_volgende

Interpretatie:
- Modus = “meest typische / meest voorkomende” (bij klassen: schatting binnen modale klasse).

### 1.7 Spreiding: variantie en standaardafwijking

- Variantie zegt hoe hard waarden rond het gemiddelde schommelen.
- Standaardafwijking is dezelfde info maar in dezelfde eenheid als de data (uren).

Bij gegroepeerde data (met middenpunten) zie je vaak:
- s^2 = (som fi * mi^2)/n - xbar^2
- s = sqrt(s^2)

Interpretatie:
- s is een “typische afstand tot het gemiddelde”.
  - vb. s = 6.7 uur betekent: typische afwijking rond xbar is ~6.7 uur.

### 1.8 Scheefheid (Pearson)

- Skp = (xbar - Mo) / s

Interpretatie:
- Skp > 0: rechtsscheef (staart naar rechts)
- Skp < 0: linksscheef
- |Skp| klein (bv < 0.5): lichte scheefheid

Check-regel die vaak klopt:
- rechtsscheef: Mo < Me < xbar

## 2) Kansrekening basics (oef. 3 als voorbeeld)

Typische bouwstenen:
- complement: P(niet A) = 1 - P(A)
- onafhankelijk: P(A en B) = P(A)*P(B)
- unie: P(A of B) = P(A)+P(B)-P(A en B)
- “minstens 1” = 1 - P(geen)

Interpretatie:
- Je zet zinnen om naar gebeurtenissen (A, B, ...), en rekent dan met deze regels.

## 3) Voorwaardelijke kans en Bayes (oef. 4 als voorbeeld)

Als je hoort “gegeven dat”:
- P(A gegeven B) = P(A en B) / P(B)

Bayes stappen:
1) Definieer gebeurtenissen (A = echt, E = expert zegt echt)
2) Bereken eerst P(E) met totale kans:
   - P(E) = P(E|A)P(A) + P(E|niet A)P(niet A)
3) Dan Bayes:
   - P(A|E) = P(E|A)P(A) / P(E)

Interpretatie:
- Je update je kans op A als je nieuwe info (B) krijgt.

## 4) Discrete verdelingen: binomiaal (oef. 8 als voorbeeld)

Wanneer binomiaal?
- n vaste proeven
- per proef: succes/mislukking
- p blijft constant
- proeven zijn onafhankelijk

Parameters:
- mu = n*p (verwacht aantal successen)
- sigma = sqrt(n*p*(1-p))

Wat doe je op examen?
- Exacte kans P(X = k): TI `binompdf` of Tabel 2.
- Cumulatief P(X <= k): TI `binomcdf` of Tabel 3.

Normale benadering (bij grote n):
- gebruik mu en sigma
- continuiteitscorrectie:
  - P(X >= 30) wordt ongeveer P(N >= 29.5)

## 5) Normale verdeling en Z-tabel (oef. 7/9 als voorbeeld)

Wat is normaal verdeeld?
- klokvormig en symmetrisch rond mu
- sigma bepaalt de breedte

Standaardiseren:
- z = (x - mu) / sigma

Z-tabel (Tabel 8a/8b in jouw tabellen):
- geeft P(Z <= z)
- z > 0: gebruik 8b; z < 0: gebruik 8a
- rechterstaart: P(Z > z) = 1 - P(Z <= z)

## 6) Steekproefgemiddelde (oef. 7a)

Als individuele waarden normaal zijn (of n is groot genoeg):
- het steekproefgemiddelde xbar is (ongeveer) normaal
- centrum blijft mu
- spreiding wordt kleiner: sigma_xbar = sigma / sqrt(n)

Interpretatie:
- gemiddelden van steekproeven “clusteren” dichter rond mu dan individuele waarden.

## 7) Som/verschil van normalen (oef. 7b)

Bij onafhankelijkheid:
- D = X - Y
- mu_D = mu_X - mu_Y
- sigma_D = sqrt(sigma_X^2 + sigma_Y^2)

Dan herleid je de vraag naar een normale kans over D.

## 8) Betrouwbaarheidsinterval voor mu (oef. 6)

Als n klein en sigma onbekend:
- gebruik t-verdeling met v = n-1

Basisvorm:
- interval = xbar ± t * (S / sqrt(n))

Waar haal je t?
- Tabel 9 (t-verdeling): kies de juiste kolom (bv. 0.975 voor 95% tweezijdig)

Interpretatie:
- “95% betrouwbaar” betekent: als je dit heel vaak herhaalt, dan zal ongeveer 95% van de intervallen de echte mu bevatten.

## 9) Toetsen van hypothesen (oef. 10)

Altijd hetzelfde stramien:
1) H0 en H1 opschrijven (eenzijdig of tweezijdig)
2) Kies alpha (0.05 of 0.01)
3) Bereken testgrootheid (bv. t)
4) Kritieke waarde uit t-tabel
5) Beslissing en conclusie in woorden:
   - verwerpen bij 0.05: significant
   - verwerpen bij 0.01: sterk significant

## 10) Mini-checklist voor je uitkomst

- Is je kans tussen 0 en 1 (of 0% en 100%)?
- Is je gemiddelde logisch (tussen min en max)?
- Bij “>=” of “>”: heb je continuiteitscorrectie toegepast (bij normale benadering van binomiaal)?
- Bij t: juiste vrijheidsgraden gekozen?
- Schrijf altijd je conclusie in context (wat betekent het voor de situatie?).

# Voorbeeldexamen - Studeersamenvatting per oefening

## 🧭 Afgeleid (geen SSOT)
- Samenvatting op basis van het voorbeeldexamen.
- Scope blijft in [[data_analysis_leerstof_overzicht_2025_2026]].

Doel: genoeg houvast om elke oefening zelfstandig op te lossen.

## Oefening 1 - Frequentietabel, ogief, kengetallen, spreiding, scheefheid (H1-H2)

### Kernprobleem
Ruwe (gegroepeerde) data omzetten naar een volledige tabel, grafieken en kengetallen.

### Intuitieve uitleg
Je maakt van ruwe data een overzicht: hoeveel komt voor, waar ligt het midden, en hoe verspreid/scheef is de verdeling.

### Formele structuur
- Intervalgrenzen bij afgeronde data: klasse 1-6 wordt 0.5-6.5 (haal 0.5 af van ondergrens, tel 0.5 bij bovengrens).
- Intervalmidden: m_i = (ondergrens + bovengrens) / 2.
- Cumulatieve frequentie: c f_i = som van f_1 t/m f_i.
- Relatieve frequentie: h_i = f_i / n. Cumulatief relatief: c h_i = c f_i / n.
- Gegroepeerd gemiddelde: xbar = (sum m_i f_i) / n.
- Steekproefvariantie: s^2 = (sum (m_i - xbar)^2 f_i) / (n - 1). Standaardafwijking s = sqrt(s^2).
- Mediaan bij klassen: interpolatie in mediaanklasse.
- Modus bij klassen: interpolatie in modusklasse.
- Pearson-scheefheid: Sk = (xbar - Mo) / s.

### Toepassing (procedure)
1. Vul intervalgrenzen en intervalmidden in.
2. Vul f_i, c f_i, h_i (en c h_i indien gevraagd).
3. Teken histogram en ogief.
4. Lees Q1, Me, Q3 uit ogief (grafisch).
5. Bereken xbar, Me (interpolatie), Mo (interpolatie), s.
6. Bereken Sk en interpreteer: Sk > 0 rechts-scheef, Sk < 0 links-scheef.

### Examengerichte vertaling
- Controleer sum f_i = n en sum h_i = 1.
- Gebruik n - 1 in s^2 (steekproef).
- Scheefheid check: bij rechts-scheef vaak Mo < Me < xbar.

## Oefening 2 - Effect van verwijderen min/max op xbar en s (H2)

### Kernprobleem
Nieuwe xbar en s berekenen na verwijderen van kleinste en grootste waarde.

### Intuitieve uitleg
Je corrigeert de totalsommen en herberekent alles op basis van de overblijvende data.

### Formele structuur
- Sum x_i = n * xbar.
- Sum x_i^2 = (n - 1) s^2 + n xbar^2.
- Na verwijderen: n' = n - 2,
  sum' x_i = sum x_i - x_min - x_max,
  sum' x_i^2 = sum x_i^2 - x_min^2 - x_max^2.
- Nieuwe xbar' = sum' x_i / n'.
- Nieuwe s'^2 = (sum' x_i^2 - n' xbar'^2) / (n' - 1).

### Toepassing (procedure)
1. Bereken sum x_i en sum x_i^2 uit xbar en s.
2. Trek min en max af (ook hun kwadraten).
3. Bereken xbar' en s' met n'.

### Examengerichte vertaling
- Foutkans: n - 1 vergeten.
- Controle: s' is meestal kleiner na verwijderen extreme waarden.

## Oefening 3 - Kansregels (H4)

### Kernprobleem
Kansen combineren voor geen, beide, minstens een, A maar niet B.

### Intuitieve uitleg
Gebruik unie, doorsnede en complement om samengestelde kansen te berekenen.

### Formele structuur
- Onafhankelijk: P(A ∩ B) = P(A) P(B).
- Complement: P(A_bar) = 1 - P(A).
- Unie: P(A ∪ B) = P(A) + P(B) - P(A ∩ B).

### Toepassing (procedure)
1. Definieer A en B.
2. Gebruik onafhankelijkheid indien van toepassing.
3. Geen van beide: P(A_bar ∩ B_bar) = P(A_bar) P(B_bar).
4. Beide: P(A ∩ B).
5. Minstens een: 1 - P(A_bar ∩ B_bar) of unie.
6. A maar niet B: P(A ∩ B_bar) = P(A) P(B_bar).

### Examengerichte vertaling
- Unieregel zonder aftrek doorsnede is fout.
- Complement-truc is vaak sneller.

## Oefening 4 - Bayes met betrouwbaarheid (H4)

### Kernprobleem
Kans op echte oorzaak gegeven een positief oordeel/test.

### Intuitieve uitleg
Een positieve test betekent niet automatisch dat de oorzaak waar is; basisfrequentie speelt mee.

### Formele structuur
- Bayes: P(A|B) = P(B|A) P(A) / P(B).
- Totale kans: P(B) = P(B|A) P(A) + P(B|A_bar) P(A_bar).

### Toepassing (procedure)
1. Definieer A (echt) en B (positief oordeel).
2. Bereken P(B) via totale kans.
3. Pas Bayes toe.

### Examengerichte vertaling
- Verwissel P(A|B) niet met P(B|A).
- Boomdiagram helpt fouten vermijden.

## Oefening 5 - Gezamenlijke verdeling, onafhankelijkheid, som (H5)

### Kernprobleem
Joint tabel aanvullen, onafhankelijkheid testen, verdeling van X + Y, E en Var.

### Intuitieve uitleg
Uit een gezamenlijke verdeling kan je alle marges, sommen en verwachtingen afleiden.

### Formele structuur
- Marginale kans: rij/kolomsom.
- Onafhankelijk: P(X = x, Y = y) = P(X = x) P(Y = y) voor alle cellen.
- Verdeling som: P(X + Y = k) = sum van cellen met x + y = k.
- E(X + Y) = E(X) + E(Y).
- Var(X + Y) = Var(X) + Var(Y) (als X en Y onafhankelijk).
- Var(X + Y) = Var(X) + Var(Y) + 2 Cov(X, Y) (algemeen).

### Toepassing (procedure)
1. Vul ontbrekende cellen via rijsommen/kolomsommen.
2. Check onafhankelijkheid met 1-2 cellen.
3. Stel verdeling van X + Y op door combinaties te bundelen.
4. Bereken E en Var.

### Examengerichte vertaling
- Vergeet niet om meerdere combinaties voor dezelfde som op te tellen.
- Als onafhankelijk, dan Var(X + Y) = Var(X) + Var(Y).

## Oefening 6 - 95% betrouwbaarheidsinterval (H8)

### Kernprobleem
Intervalschatting van het populatiegemiddelde bij kleine steekproef.

### Intuitieve uitleg
Je schat het echte gemiddelde met een foutmarge op basis van de steekproef.

### Formele structuur
- Kleine n, sigma onbekend: xbar ± t_(alpha/2, n-1) * (s / sqrt(n)).

### Toepassing (procedure)
1. Bereken xbar en s.
2. Zoek t-waarde met df = n - 1.
3. Bereken marge en intervalgrenzen.

### Examengerichte vertaling
- Gebruik t-tabel, niet z-tabel.
- Vermeld df = n - 1.

## Oefening 7 - Steekproefgemiddelde en verschil van normalen (H7-H9)

### Kernprobleem
Kans op afwijking van het steekproefgemiddelde en vergelijking van twee normaalverdelingen.

### Intuitieve uitleg
Gemiddelden uit steekproeven schommelen minder dan individuele waarden. Het verschil van twee normalen is weer normaal.

### Formele structuur
- Xbar ~ N(mu, sigma / sqrt(n)).
- Voor verschil: mu_(X-Y) = mu_X - mu_Y.
- sigma_(X-Y) = sqrt(sigma_X^2 + sigma_Y^2).

### Toepassing (procedure)
1. Zet Xbar om naar z-score met sigma / sqrt(n).
2. Bij "minstens" gebruik tweezijdige staartkans.
3. Bij vergelijking A en B: werk met X - Y en standaardiseer.

### Examengerichte vertaling
- Standaardfout sigma / sqrt(n) wordt vaak vergeten.
- Bij verschil: varianties optellen, niet aftrekken.

## Oefening 8 - Binomiaal en normale benadering (H6)

### Kernprobleem
Exacte binomiale kans en benadering met normale verdeling.

### Intuitieve uitleg
Bij grote n lijkt binomiaal op normaal; je gebruikt dan z-scores.

### Formele structuur
- Binomiaal: P(X = k) = C(n, k) p^k q^(n-k).
- Binomiaal parameters: E(X) = n p, sigma = sqrt(n p q).
- Normaal: Z = (X - mu) / sigma.
- Continuiteitscorrectie: P(X >= 30) -> P(X >= 29.5).

### Toepassing (procedure)
1. (a) Bereken exact met binomiaal.
2. (b) Benader met normaal: standardiseer en lees uit tabel.

### Examengerichte vertaling
- Gebruik continuiteitscorrectie.
- Check of n p en n q voldoende groot zijn.

## Oefening 9 - Normaal en sigma afleiden (H6)

### Kernprobleem
Bereken sigma uit een percentiel en gebruik die sigma voor een nieuwe kans.

### Intuitieve uitleg
Een percentiel zet een z-waarde vast, die bepaalt de spreiding.

### Formele structuur
- Z = (X - mu) / sigma.
- P(X < a) = p -> z_p uit tabel.

### Toepassing (procedure)
1. Zet de gegeven kans om naar z.
2. Los sigma op.
3. Gebruik sigma voor de tweede kans.

### Examengerichte vertaling
- Let op links/rechts (z-waarde kan negatief zijn).
- Schrijf z expliciet om fout te voorkomen.

## Oefening 10 - Hypothesetoets verschil van gemiddelden (H10)

### Kernprobleem
Beslissen of het verschil tussen twee gemiddelden significant is.

### Intuitieve uitleg
Je vergelijkt het waargenomen verschil met wat je door toeval zou verwachten.

### Formele structuur
- H0: mu_x = mu_y.
- H1 (eenzijdig): mu_x > mu_y.
- z = (Xbar - Ybar) / sqrt(s_x^2 / n_x + s_y^2 / n_y) (grote n of sigma bekend).
- t = (Xbar - Ybar) / sqrt( ((n_x - 1) s_x^2 + (n_y - 1) s_y^2) / (n_x + n_y - 2) * (1/n_x + 1/n_y) ) (kleine n).

### Toepassing (procedure)
1. Formuleer H0 en H1 (eenzijdig of tweezijdig).
2. Bereken z of t.
3. Vergelijk met kritieke waarde(n) voor alpha.
4. Besluit en benoem significant/sterk significant.

### Examengerichte vertaling
- Verkeerde richting (eenzijdig vs tweezijdig) is een klassieke fout.
- Vergelijk met juiste kritieke waarde.

# Betrouwbaarheidsintervallen

**Wat is het?**
Een **intervalschatting** die een bereik van waarschijnlijke waarden geeft voor een onbekende populatieparameter (zoals het gemiddelde `μ`). In plaats van een onzekere puntschatting (bv. `x̄` = 10), geeft het een interval met een bepaald [[Details van Betrouwbaarheidsintervallen|betrouwbaarheidsniveau]].

**Interpretatie:**
Een 95% betrouwbaarheidsinterval betekent dat als we het proces van steekproeftrekking en intervalberekening heel vaak zouden herhalen, 95% van de berekende intervallen de ware populatieparameter zou bevatten.

---

### Algemene Formule & Berekening
De structuur van een betrouwbaarheidsinterval is bijna altijd hetzelfde:

$$ \text{Puntschatting} \pm \text{Foutenmarge} $$

Specifiek voor een populatiegemiddelde `μ`:

$$ \bar{x} \pm (\text{kritieke waarde} \times \text{standaardfout}) $$

-   **`x̄` (Puntschatting):** Het gemiddelde van je steekproef. Dit is je "beste gok".
-   **Kritieke waarde:** Een getal uit de Z- of t-verdeling dat afhangt van het gekozen betrouwbaarheidsniveau (bv. 1.96 voor 95% bij een Z-verdeling).
-   **Standaardfout:** De standaardafwijking van de [[Steekproefverdelingen|steekproefverdeling]]. Het meet de gemiddelde fout die we verwachten te maken met onze puntschatting. Voor een gemiddelde is de standaardfout:
    $$ SE = \frac{s}{\sqrt{n}} $$
    - `s` is de steekproefstandaardafwijking.
    - `n` is de steekproefgrootte.

### Wanneer Z of T gebruiken?
-   **Z-waarde:** Als de populatiestandaardafwijking `σ` bekend is, of als de steekproef heel groot is (n > 30).
-   **t-waarde:** Als `σ` onbekend is en de steekproef klein is (n ≤ 30). De t-verdeling heeft "dikkere staarten" om de extra onzekerheid van het schatten van `σ` met `s` te compenseren.

---

**Waarom is dit belangrijk?**
Het geeft een veel eerlijker en informatiever beeld dan een enkele puntschatting. Het kwantificeert onze (on)zekerheid en geeft een bereik van plausibele waarden, wat essentieel is voor het nemen van onderbouwde beslissingen.
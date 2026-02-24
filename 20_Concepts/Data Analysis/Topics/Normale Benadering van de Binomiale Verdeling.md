# Normale Benadering van de Binomiale Verdeling

**Wat is het?**
Een techniek om een [[Kansverdelingen|Binomiale verdeling]] te benaderen met een [[Kansverdelingen|Normale verdeling]]. Dit is extreem handig omdat het berekenen van binomiale kansen met een grote `n` (aantal herhalingen) zeer intensief is.

**Wanneer mag je dit gebruiken? (De vuistregel)**
Je mag de normale benadering toepassen als zowel het verwachte aantal successen als het verwachte aantal mislukkingen groot genoeg is. Concreet:
- $n \cdot p \ge 5$
- $n \cdot (1-p) \ge 5$
Waarbij `n` het aantal herhalingen is en `p` de kans op succes.

---

### Hoe werkt het? Stappenplan:
1.  **Controleer de voorwaarden:** Ga na of `np` en `n(1-p)` beiden groter of gelijk aan 5 zijn.
2.  **Bereken de parameters voor de Normale verdeling:**
    -   Het gemiddelde `μ` is de verwachtingswaarde van de binomiale verdeling:
        $$ \mu = n \cdot p $$
    -   De standaardafwijking `σ` is de wortel uit de variantie van de binomiale verdeling:
        $$ \sigma = \sqrt{n \cdot p \cdot (1-p)} $$
3.  **Pas de Continuïteitscorrectie toe:**
    Dit is de **meest cruciale stap**. Omdat je een discrete verdeling (binomiale) benadert met een continue verdeling (normale), moet je een correctie van 0.5 toepassen.
    -   $P(X = k) \rightarrow P(k-0.5 \le X \le k+0.5)$
    -   $P(X \ge k) \rightarrow P(X \ge k-0.5)$
    -   $P(X > k) \rightarrow P(X \ge k+0.5)$
    -   $P(X \le k) \rightarrow P(X \le k+0.5)$
    -   $P(X < k) \rightarrow P(X \le k-0.5)$
4.  **Standaardiseer en bereken de kans:**
    Zet de (gecorrigeerde) waarde om naar een Z-score en zoek de kans op in de Z-tabel.
    $$ Z = \frac{x_{\text{gecorrigeerd}} - \mu}{\sigma} $$

---

**Waarom is dit belangrijk?**
Het is een krachtige shortcut die complexe, tijdrovende berekeningen van de binomiale verdeling voor grote steekproeven vereenvoudigt tot een snelle opzoeking in de Z-tabel. Het vormt een brug tussen de discrete en continue kansverdelingen.
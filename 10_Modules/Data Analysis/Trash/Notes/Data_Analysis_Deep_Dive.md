# Data Analysis: The Grand Deep Dive 🌊

## 🧭 Afgeleid (geen SSOT)
- Verdieping en extra uitleg.
- Scope blijft in [[data_analysis_leerstof_overzicht_2025_2026]].

Een compleet overzicht van alle leerstof, gestructureerd van basis tot examen-niveau.

---

## 🏗️ Deel 1: De Fundering (Beschrijvend)
*Doel: Data samenvatten en begrijpen.*

### H1: Frequentieverdelingen
*   **Kern:** Van ruwe data naar tabellen en grafieken.
*   **Must-Know:**
    *   **Histogram:** Oppervlakte = frequentie. (Alleen voor continue data).
    *   **Ogief:** Cumulatief. Handig voor mediaan/kwartielen.
*   **Valkuil:** Open klassen ("> 100") hebben geen midden -> geen gemiddelde mogelijk!

### H2: Parameters
*   **Kern:** Data samenvatten in getallen.
*   **Centrum:** Gemiddelde ($\bar{x}$, gevoelig), Mediaan (Me, resistent), Modus (Mo).
*   **Spreiding:** Variantie ($s^2$), Standaardafwijking ($s$), Range.
    *   **Formule $s^2$:** $\frac{\sum (x_i - \bar{x})^2}{n-1}$. (Deel door $n-1$ bij steekproef!).
*   **Vorm:** Scheefheid (Links/Rechts) en Spitsheid (Kurtosis).

### H3: Regressie (Facultatief)
*   **Kern:** Verband tussen X en Y. (Niet examengericht).

---

## 🎲 Deel 2: Het Gereedschap (Kansrekening)
*Doel: De regels van het toeval leren.*

### H4: Kansverzamelingen
*   **Kern:** Hoe reken je met kansen?
*   **Basis:** Laplace ($P(A) = \frac{\text{gunstig}}{\text{totaal}}$). Alleen bij eerlijke kansen!
*   **Regels:**
    *   **Of (Unie):** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
    *   **En (Doorsnede):** $P(A \cap B) = P(A) \cdot P(B|A)$.
    *   **Onafhankelijk:** Als $P(A \cap B) = P(A) \cdot P(B)$.
*   **Bayes (De Omkeertruc):**
    *   $P(Ziek|Positief) = \frac{P(Positief|Ziek) \cdot P(Ziek)}{P(Positief)}$.
    *   *Gebruik:* Boomdiagrammen!

### H5: Toevalsveranderlijken
*   **Kern:** Van "Kop/Munt" naar getallen ($X=0, X=1$).
*   **Eigenschappen:**
    *   $E(X)$ (Verwachtingswaarde) = "Het gemiddelde op lange termijn".
    *   **Sommen:** $E(X+Y) = E(X) + E(Y)$. (Altijd).
    *   **Variantie:** $Var(X+Y) = Var(X) + Var(Y)$. (**ALLEEN als onafhankelijk!**).

### H6: Kansverdelingen (De Big Three)
1.  **Binomiaal ($n, p$):**
    *   Succes/Mislukking, $n$ keer herhaald. (Met terugleggen).
    *   $E = n \cdot p$, $Var = n \cdot p \cdot (1-p)$.
2.  **Poisson ($\lambda$):**
    *   Zeldzame events in tijd/ruimte (bv. aantal telefoontjes per uur).
    *   $E = \lambda$, $Var = \lambda$.
3.  **Normaal ($\mu, \sigma$):**
    *   De Klokcurve. Alles is continu.
    *   **Standaardiseren:** $z = \frac{x - \mu}{\sigma}$. (Maak er een N(0,1) van).

---

## ⚖️ Deel 3: De Beslissing (Inferentie)
*Doel: Van steekproef naar werkelijkheid.*

### H7: Centrale Limietstelling (De Brug)
*   **Het Wonder:** Als je vaak een steekproef neemt, is het **gemiddelde van die steekproeven** ($\bar{X}$) Normaal verdeeld!
    *   Zelfs als de populatie *niet* normaal is (bij $n > 30$).
*   **De Formule:** $\bar{X} \sim N(\mu, \frac{\sigma}{\sqrt{n}})$.
    *   *Let op:* De spreiding wordt kleiner ($\sqrt{n}$) naarmate je meer meet.

### H8: Betrouwbaarheidsintervallen (Schatten)
*   **Vraag:** "Ik meet 10 en 12. Waar ligt het echte gemiddelde?"
*   **Antwoord:** $\bar{x} \pm \text{Marge}$.
*   **Situatie A: $\sigma$ bekend (Grote n)** -> **Z-tabel**.
    *   $\bar{x} \pm z \cdot \frac{\sigma}{\sqrt{n}}$.
*   **Situatie B: $\sigma$ onbekend (Kleine n)** -> **T-tabel** (Student).
    *   $\bar{x} \pm t_{n-1} \cdot \frac{s}{\sqrt{n}}$.
    *   *Valkuil:* $t$ hangt af van vrijheidsgraden ($df = n-1$).

### H9: Verschillen (A vs B)
*   **Vraag:** "Is A beter dan B?"
*   **Truc:** Maak een nieuwe variabele $D = X - Y$.
    *   $E(X-Y) = \mu_X - \mu_Y$.
    *   $Var(X-Y) = \sigma_X^2 + \sigma_Y^2$. (**Optellen!** Spreiding wordt altijd groter).

### H10: Hypotheses Toetsen (Het Vonnis)
*   **Stappenplan:**
    1.  **Hypotheses:** $H_0$ (Geen verschil) vs $H_1$ (Wel verschil).
    2.  **Kies $\alpha$:** Foutkans (meestal 0.05).
    3.  **Toetsingsgrootheid:** Reken $z$ of $t$ uit.
        *   $z_{obs} = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}$.
    4.  **Besluit:**
        *   Ligt $z_{obs}$ in het **Verwerpingsgebied**? -> Verwerp $H_0$. (Significant verschil).
        *   Ligt $z_{obs}$ in het **Aanvaardingsgebied**? -> Aanvaard $H_0$. (Toeval).
*   **Fouten:**
    *   **Type I ($\alpha$):** Onschuldige veroordelen ($H_0$ is waar, maar je verwerpt).
    *   **Type II ($\beta$):** Schuldige vrijspreken ($H_1$ is waar, maar je aanvaardt $H_0$).

---

## 📝 Examen Cheat Sheet (Must-Knows)

| Wat? | Formule/Regel |
| :--- | :--- |
| **Klassengrens** | Ondergrens + Bovengrens / 2 |
| **Steekproefvariantie** | Deel door **$n-1$** |
| **Onafhankelijkheid** | $P(A \cap B) = P(A) \cdot P(B)$ |
| **Bayes** | $P(A|B) = \frac{P(B|A)P(A)}{P(B)}$ |
| **Standaardfout** | $\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$ |
| **Z-score** | $z = \frac{\text{waarde} - \text{gemiddelde}}{\text{standaardfout}}$ |
| **Betr. Interval (t)** | $\bar{x} \pm t \cdot \frac{s}{\sqrt{n}}$ |
| **Verschil Variantie** | $\sigma_{X-Y}^2 = \sigma_X^2 + \sigma_Y^2$ |

---

### 🔥 Top 3 Valkuilen
1.  **$s$ vs $\sigma$:** Gebruik je de populatie-standaardafwijking ($\sigma$, zelden gekend) of de steekproef-versie ($s$)? Bij $s$ en kleine $n$: **T-tabel**!
2.  **Variantie optellen:** $Var(X-Y)$ is **PLUS** de varianties, niet min! (Onzekerheid + Onzekerheid = Meer Onzekerheid).
3.  **Eenzijdig vs Tweezijdig:**
    *   "$H_1: \mu \neq 50$" -> Tweezijdig ($\alpha$ delen door 2).
    *   "$H_1: \mu > 50$" -> Eenzijdig (Volledige $\alpha$ rechts).

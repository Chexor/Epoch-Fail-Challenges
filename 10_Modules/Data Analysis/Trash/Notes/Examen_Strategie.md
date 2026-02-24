# Data Analysis: Examen Strategie

## 🧭 Afgeleid (geen SSOT)
- Strategie en tips, geen scope-bron.
- Scope blijft in [[data_analysis_leerstof_overzicht_2025_2026]].

## 1. De Drie Grote Blokken
Op basis van het voorbeeldexamen bestaat je examen uit drie soorten vragen. We moeten ze alle drie beheersen om te slagen.

### 🧱 Blok A: De "Rekenmachine" (H1, H2, H3)
*   **Type:** Tabel invullen, gemiddelde/mediaan/modus/kwartielen berekenen, boxplot tekenen.
*   **Valkuil:** Reken- of overschrijffouten. Formules voor *gegroepeerde data* vergeten.
*   **Jouw tactiek:** Snelheid & Precisie. We trainen op "foutloos invullen".
*   **Must-know:** Formules voor $s^2$, $\bar{x}$ en $Me$ (interpolatie!) bij klassen.

### 🎲 Blok B: De "Puzzelaar" (H4, H5, H6)
*   **Type:** Kansrekening, Bayes (Boomdiagram), Kansverdelingen (Binomiaal/Normaal).
*   **Valkuil:** De vraag niet begrijpen ("Is dit nu Binomiaal of Poisson?").
*   **Jouw tactiek:** Vraag-herkenning. "Ah, dit is een 'minstens 1' vraag -> $1 - P(0)$".
*   **Must-know:** Bayes formule, Binomiale tabel, $n \cdot p$ regels.

### ⚖️ Blok C: De "Beslisser" (H7, H8, H9, H10)
*   **Type:** Betrouwbaarheidsintervallen, Hypothesetoetsen.
*   **Valkuil:** Verkeerde toets kiezen (z vs t), eenzijdig/tweezijdig verwisselen.
*   **Jouw tactiek:** Stappenplan. 1. Hypothese, 2. Toetsingsgrootheid, 3. Kritieke waarde, 4. Besluit.
*   **Must-know:** De t-tabel (voor $n < 30$), de z-formule, de $H_0$ formulering.

---

## 2. Onze Focus voor de Komende Dagen
We gaan niet "alles" leren, we gaan leren wat op het examen komt.

*   **Vandaag (zat):** H1 & H2 (Blok A) is af. Dit is je basispunten-pakker. (Vraag 1 op examen).
*   **Morgen (zon):** H4 & H5 (Blok B). Focus op *Bayes* en *Kansbomen*. (Vraag 3 & 4).
*   **Maandag:** H6 & H7 (Blok B/C). *Normale Verdeling* en *Steekproeven*. (Vraag 5 & 7).
*   **Dinsdag:** H8 & H9 (Blok C). *Betrouwbaarheidsintervallen*. (Vraag 6 & 8).
*   **Woensdag:** H10 (Blok C). *Hypotheses*. (Vraag 9 & 10). + **Oefenexamen maken**.

---

## 3. De "Gouden Formules" (Uit het voorbeeldexamen)
Dit zijn de formules die je **blind** moet kunnen toepassen:
1.  **Gegroepeerd Gemiddelde:** $\bar{x} = \frac{\sum m_i f_i}{n}$
2.  **Variantie (Steekproef):** $s^2 = \frac{\sum (m_i - \bar{x})^2 \cdot f_i}{n - 1}$
3.  **Bayes:** $P(A|B) = \frac{P(B|A)P(A)}{P(B)}$
4.  **Betrouwbaarheidsinterval (kleine n):** $\bar{x} \pm t \cdot \frac{s}{\sqrt{n}}$
5.  **Toetsingsgrootheid (z):** $z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}$

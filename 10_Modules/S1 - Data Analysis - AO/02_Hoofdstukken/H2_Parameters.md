# H2: Parameters van een Frequentieverdeling

## ✅ SSOT
- Dit is de **authoritative** hoofdstuknote voor H2.
- Afgeleide samenvattingen moeten hiernaar linken.

## 1. Het Grote Plaatje
### ❓ Kernprobleem
In H1 hebben we data in tabellen en grafieken gezet. Dat geeft een **beeld**, maar geen **getal**.
Als je aan je baas moet rapporteren, kun je niet zeggen: *"Kijk naar deze tekening, de balkjes staan een beetje rechts"*.
Je moet zeggen: *"De gemiddelde verkoop is €500 met een variatie van €50"*.

### 🎯 Doel
De hele berg data samenvatten in **enkele krachtige getallen**:
1.  **Waar ligt het midden?** (Centrummaten)
2.  **Hoe verspreid liggen de cijfers?** (Spreidingsmaten)
3.  **Welke vorm heeft de berg?** (Vormparameters)

---

## 2. Centrummaten (Waar is het midden?)
Zie concept-note: [[Centrummaten]]

### A. Rekenkundig Gemiddelde ($\bar{x}$)
*   **Intuïtie:** Als iedereen evenveel zou hebben, hoeveel heeft dan één persoon? Het "zwaartepunt".
*   **Formule:** $\bar{x} = \frac{1}{n} \sum x_i n_i$ (Som van alles / Aantal).
*   **Nadeel:** **Gevoelig voor uitschieters!** (Als Bill Gates binnenkomt, is iedereen in de kamer miljonair).
    *   *Gebruik:* Enkel bij kwantitatieve (getal) variabelen zonder extreme uitschieters.

### B. Mediaan (Me)
*   **Intuïtie:** De **middelste** persoon als je iedereen op een rij zet van klein naar groot (50% is kleiner, 50% is groter).
*   **Voordeel:** **Resistent!** Trekt zich niets aan van uitschieters.
*   **Berekening:**
    *   *Discreet:* De $(n+1)/2$-de waarneming.
    *   *Continu (Klassen):* Zoek de klasse waar de 50%-grens (cumulatieve freq) wordt overschreden.

### C. Modus (Mo)
*   **Intuïtie:** De populairste. Wat komt het vaakst voor? (De hoogste staaf in het histogram).
*   **Voordeel:** Kan ook bij *kwalitatieve* data (bv. "Kleur: Rood" is de modus).
*   **Multimodaal:** Als er twee pieken zijn (bv. kamelenrug) = 2 modi.

---

## 3. Spreidingsmaten (Hoe breed is de berg?)
Zie concept-note: [[Spreidingsmaten]]
*Waarom nodig?* Twee klassen kunnen allebei gemiddeld 12/20 halen.
*   Klas A: Iedereen heeft 12. (Spreiding = 0).
*   Klas B: De helft heeft 0, de helft heeft 24 (onmogelijk, maar snap je punt). (Enorme spreiding).
*   Gemiddelde is hetzelfde, situatie is totaal anders.

### A. Variatiebreedte (Range)
*   **Formule:** $Max - Min$.
*   **Nadeel:** Kijkt enkel naar extremen, negeert alles ertussen.

### B. Variantie ($s^2$) & Standaardafwijking ($s$)
*   **Intuïtie:** De *gemiddelde afstand* van elk punt tot het gemiddelde.
*   **Formule (Variantie):** $s^2 = \frac{1}{n} \sum (x_i - \bar{x})^2 n_i$
*   **Standaardafwijking ($s$):** $\sqrt{s^2}$ (Wortel van variantie).
    *   *Waarom wortel?* Om terug naar de originele eenheid te gaan (bv. van "vierkante euro's" terug naar "euro's").
*   **Eigenschap:** Hoe groter $s$, hoe platter en breder de berg.

### C. Variatiecoëfficiënt (VC)
*   **Probleem:** Is een spreiding van 10 groot?
    *   Bij lengte van mieren (mm): JA.
    *   Bij afstand naar de zon (km): NEE.
*   **Oplossing:** Relatieve spreiding.
*   **Formule:** $VC = \frac{s}{\bar{x}}$ (Standaardafwijking gedeeld door gemiddelde).

### D. Interkwartielafstand (IQR)
*   **Intuïtie:** De breedte van de "middenmoot" (de doos van de boxplot).
*   **Formule:** $Q3 - Q1$.
*   **Voordeel:** Resistent tegen uitschieters (net als de mediaan).

---

## 4. Vormparameters (Hoe ziet de berg eruit?)

### A. Scheefheid (Skewness)
Is de berg symmetrisch of "leunend"?
*   **Symmetrisch:** $\bar{x} \approx Me \approx Mo$.
*   **Positief scheef (Rechts):** Staart naar **Rechts** (positieve kant). De meeste mensen zitten links (laag), paar uitschieters rechts. ($\bar{x} > Me > Mo$).
*   **Negatief scheef (Links):** Staart naar **Links** (negatieve kant). ($\bar{x} < Me < Mo$).

### B. Spitsheid (Kurtosis)
Is de piek scherp (naald) of plat (heuvel)?
*   *Leptokurtisch:* Spits.
*   *Platykurtisch:* Plat.

---

## 5. Examenvallen ⚠️
1.  **Open klassen:** (" > 100 euro"). Je kunt **GEEN gemiddelde** berekenen (want geen midden), maar **WEL een mediaan**!
2.  **Variantie combineren:** Als je twee groepen samenvoegt, is de nieuwe variantie NIET gewoon de som/gemiddelde. Je hebt de *binnenvariantie* + *tussenvariantie* nodig (Ingewikkelde formule: zie slides p.39).
3.  **Eenheid:** Vergeet de eenheid niet bij $s$ (dezelfde als $x$), maar $s^2$ heeft een kwadraat-eenheid!

---

## ✅ Toepassing (Oefening)
Stel: Cijfers {2, 4, 4, 4, 5, 5, 7, 9}
1.  **Gemiddelde:** $(2+4+4+4+5+5+7+9) / 8 = 40 / 8 = 5$.
2.  **Modus:** 4 (komt 3x voor).
3.  **Mediaan:** (4+5)/2 = 4,5.
4.  **Range:** $9 - 2 = 7$.
5.  **Variantie:**
    *   Afwijkingen: $(2-5)^2=9, (4-5)^2=1...$
    *   Som kwadraten / n.

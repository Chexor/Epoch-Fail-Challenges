# Quiz: H1 & H2 (Beschrijvende Statistiek)

**Doel:** Test of de basisconcepten vastzitten voor we naar Kansrekening (H4) gaan.
**Tijd:** 10-15 minuten.
**Mag:** Rekenmachine.

---

## Deel 1: Conceptuele Vragen (Inzicht)

**Vraag 1 (Meetniveaus)**
Verbind de variabele met het juiste meetniveau:
1.  Je postcode (bv. 8500). => Nominaal
2.  Je tevredenheid over dit vak (Schaal 1-5). => Ordinaal
3.  De temperatuur in Kortrijk vandaag (°C). => Interval
4.  Het aantal pintjes dat je gisteren gedronken hebt. => Ratio

*Opties:* A. Nominaal, B. Ordinaal, C. Interval, D. Ratio.

**Vraag 2 (Centrummaten)**
Welke centrummaat gebruik je best in deze situaties?
1.  De huizenprijzen in Knokke (waar een paar villa's van €20 miljoen staan).
2.  De meest gekozen kleur van een auto.
3.  De gemiddelde lengte van volwassen mannen (normaal verdeeld).

**Vraag 3 (Grafieken)**
Waarom mag je **geen** histogram tekenen voor de variabele "Lievelingsvak"?

---

## Deel 2: Rekenwerk (Toepassing)

**Gegeven de steekproef:** `{ 2, 4, 4, 4, 5, 5, 7, 25 }` ($n=8$)

**Vraag 4**
Bereken de **Modus**, **Mediaan** en het **Gemiddelde**.
*Tip:* Let op de uitschieter (25)!

**Vraag 5**
Bereken de **Range** en de **Interkwartielafstand (IQR)**.
*Tip:* Voor IQR moet je eerst Q1 en Q3 vinden.
*(Q1 = mediaan van de eerste helft, Q3 = mediaan van de tweede helft).*

**Vraag 6 (Valkuil)**
Is het getal **25** een uitschieter volgens de officiële boxplot-regel?
*Regel:* Uitschieter als $X > Q3 + 1,5 \times IQR$.

---

## 🛑 STOP - EERST MAKEN!

*(Scroll pas naar beneden voor de antwoorden als je klaar bent)*

<br>
<br>
<br>
<br>
<br>

---

## Antwoorden & Uitleg

### Deel 1
1.  **1-A (Nominaal), 2-B (Ordinaal), 3-C (Interval), 4-D (Ratio).**
    *   *Let op:* Postcode is een *naam* (etiket), geen rekengetal. Temperatuur heeft geen natuurlijk nulpunt (0°C is koud, maar niet "niks").
2.  **1. Mediaan** (Resistent tegen de dure villa's/uitschieters). **2. Modus** (Enige optie bij categorieën). **3. Gemiddelde** (Bij symmetrische verdelingen is dit de beste).
3.  Omdat "Lievelingsvak" een **kwalitatieve (nominale)** variabele is. Een histogram is voor **continue** (kwantitatieve) data. Hier gebruik je een **Staafdiagram** (met spaties tussen de balken).

### Deel 2
**Data:** 2, 4, 4, 4, 5, 5, 7, 25 (gesorteerd).

4.  **Centrum:**
    *   **Modus:** 4 (komt 3x voor).
    *   **Mediaan:** $(4+5)/2 = 4,5$. (Middelste van 8 getallen is het gemiddelde van het 4e en 5e getal).
    *   **Gemiddelde:** $(2+4+4+4+5+5+7+25) / 8 = 56 / 8 = 7$.
    *   *Zie je het effect?* De mediaan (4,5) negeert de 25. Het gemiddelde (7) wordt omhoog getrokken.

5.  **Spreiding:**
    *   **Range:** $25 - 2 = 23$.
    *   **Q1:** De eerste helft is {2, 4, 4, 4}. Mediaan hiervan is $(4+4)/2 = 4$.
    *   **Q3:** De tweede helft is {5, 5, 7, 25}. Mediaan hiervan is $(5+7)/2 = 6$.
    *   **IQR:** $Q3 - Q1 = 6 - 4 = 2$.

6.  **Uitschieter-test:**
    *   Grens = $Q3 + 1,5 \times IQR$
    *   Grens = $6 + (1,5 \times 2) = 6 + 3 = 9$.
    *   Is $25 > 9$? **JA!**
    *   **Conclusie:** 25 is een statistische uitschieter en krijgt een *sterretje* in de boxplot.

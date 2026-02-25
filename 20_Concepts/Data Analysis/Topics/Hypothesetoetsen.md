# Hypothesetoetsen

## Overzicht
Een formele, statistische procedure om een bewering over een populatie te testen op basis van data uit een steekproef. We wegen het bewijs af tegen een claim (de nulhypothese).

---

## De twee hypothesen
1.  **Nulhypothese (H₀):** De "status quo" of de "geen effect" hypothese. Dit is de claim die we proberen te weerleggen.
    - *Voorbeeld:* $H_0: \mu = 100$ (Het gemiddelde IQ is 100).
2.  **Alternatieve Hypothese (H₁):** Wat we proberen aan te tonen. Deze claim wordt aanvaard als er genoeg bewijs is om H₀ te verwerpen.
    - *Voorbeeld:* $H_1: \mu \neq 100$ (Het gemiddelde IQ is niet 100).

---

## De procedure en berekening
De kern van elke hypothesetoets is de **toetsingsgrootheid** (test statistic). Deze volgt bijna altijd dezelfde logische structuur:

$$ \text{Toetsingsgrootheid} = \frac{(\text{Waargenomen waarde} - \text{Verwachte waarde onder } H_0)}{\text{Standaardfout}} $$

- **Waargenomen waarde:** De statistiek die je in je steekproef berekent (bv. het steekproefgemiddelde `x̄`).
- **Verwachte waarde:** De waarde die de nulhypothese voorspelt (bv. `μ₀`).
- **Standaardfout:** De standaardafwijking van de steekproefverdeling, die de te verwachten variabiliteit door toeval meet.

**Voorbeeld (t-toets voor één gemiddelde):**
$$ t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}} $$
Deze t-waarde drukt uit hoeveel standaardfouten je steekproefgemiddelde (`x̄`) afwijkt van de waarde onder de nulhypothese (`μ₀`).

**De Beslissing:**
1.  Bereken de toetsingsgrootheid (bv. de t-waarde).
2.  Vergelijk deze met een **kritieke waarde** uit de t-verdeling (die afhangt van je [[Details van Hypothesetoetsen|significantieniveau α]]).
3.  Als de berekende waarde extremer is dan de kritieke waarde, is het resultaat **statistisch significant**. We **verwerpen H₀**.

---

## Mogelijke fouten
Het nemen van een beslissing op basis van een steekproef is nooit 100% zeker. Er zijn altijd risico's. Zie: [[Details van Hypothesetoetsen]].

---

**Waarom is dit belangrijk?**
Het geeft ons een objectieve en gestructureerde methode om beslissingen te nemen onder onzekerheid. Het is het fundament van wetenschappelijk onderzoek, A/B-testen, medische studies en kwaliteitscontrole.

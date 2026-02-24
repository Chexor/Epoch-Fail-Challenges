# Spreidingsmaten

**Wat is het?**
Getallen die beschrijven hoe ver de data uit elkaar liggen, of hoe "gespreid" de dataset is.

---

### 1. Variantie
De variantie is de gemiddelde gekwadrateerde afstand van elke waarde tot het gemiddelde. Een grotere variantie betekent meer spreiding.

**Formules & Berekening:**
- **Steekproefvariantie (`s²`):**
  $$ s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1} $$
  - `(xᵢ - x̄)²`: Voor elke waarde, bereken het verschil met het gemiddelde en kwadrateer dit.
  - `Σ`: Tel al deze gekwadrateerde verschillen op.
  - `n-1`: Deel door het aantal waarden min één. We delen door `n-1` (en niet `n`) om een betere, "eerlijkere" schatting te krijgen van de populatievariantie. Dit heet de correctie van Bessel.

- **Populatievariantie (`σ²`):**
  $$ \sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N} $$
  - Hier deel je wel door de totale grootte van de populatie `N`.

### 2. Standaardafwijking (of Standaarddeviatie)
De standaardafwijking is de wortel uit de variantie. Het is de meest gebruikte spreidingsmaat omdat de eenheid dezelfde is als die van de data zelf.

**Formules & Berekening:**
- **Steekproefstandaardafwijking (`s`):**
  $$ s = \sqrt{s^2} = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}} $$

- **Populatiestandaardafwijking (`σ`):**
  $$ \sigma = \sqrt{\sigma^2} = \sqrt{\frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}} $$

### 3. Variatiebreedte (Range)
De eenvoudigste spreidingsmaat: het verschil tussen de hoogste en de laagste waarde in de dataset.
$$ \text{Variatiebreedte} = \max(x) - \min(x) $$
- *Extreem gevoelig voor uitschieters.*

---
### Speciale Formules voor Gegroepeerde Data
- **Standaardafwijking (Gegroepeerd - rekenformule):**
  Een snellere manier om de standaardafwijking voor gegroepeerde data te berekenen.
  $$ s = \sqrt{\frac{\sum f_i \cdot X_i^2}{n} - \bar{x}^2} $$
  - `fᵢ` is de frequentie van een klasse.
  - `Xᵢ` is het **klassenmidden** van die klasse.
  - `n` is het totaal aantal waarnemingen.
  - `x̄` is het (eerder berekende) gegroepeerde gemiddelde.

---

**Waarom is dit belangrijk?**
Spreidingsmaten vertellen je over de consistentie en betrouwbaarheid van je data. Een kleine spreiding betekent dat de waarden dicht bij het gemiddelde liggen en dus voorspelbaarder zijn. De standaardafwijking is een fundamentele bouwsteen voor bijna alle verdere statistische analyses.
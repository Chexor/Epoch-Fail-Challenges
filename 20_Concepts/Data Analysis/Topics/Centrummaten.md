# Centrummaten

**Wat is het?**
Eén getal dat het "midden" of het centrum van je data beschrijft.

---

### 1. Rekenkundig Gemiddelde
De som van alle waarden, gedeeld door het aantal. Het is de meest gebruikte centrummaat, maar is *gevoelig voor uitschieters*.

**Formules & Berekening:**
- **Steekproefgemiddelde (`x̄`):**
  $$ \bar{x} = \frac{\sum_{i=1}^{n} x_i}{n} $$
  - `Σ` (sigma) betekent "som van".
  - `xᵢ` is elke individuele waarde in je steekproef.
  - `n` is het aantal waarden in de steekproef.

- **Populatiegemiddelde (`μ`):**
  $$ \mu = \frac{\sum_{i=1}^{N} x_i}{N} $$
  - `N` is de totale grootte van de populatie.

### 2. Mediaan
De middelste waarde wanneer je alle data van klein naar groot rangschikt. De mediaan is *robuust tegen uitschieters*.

**Berekening:**
1. Sorteer je dataset.
2. Is het aantal waarden (`n`) **oneven**? De mediaan is de middelste waarde.
3. Is het aantal waarden **even**? De mediaan is het gemiddelde van de twee middelste waarden.

### 3. Modus
De waarde of categorie die het vaakst voorkomt in de dataset.

---
### Speciale Formules voor Gegroepeerde Data
Wanneer je data in klassen (intervallen) gegroepeerd zijn, gebruik je specifieke formules om de centrummaten te *schatten*.

- **Gemiddelde (Gegroepeerd):**
  $$ \bar{x} = \frac{\sum f_i \cdot X_i}{n} $$
  - `fᵢ` is de frequentie (aantal) van een klasse.
  - `Xᵢ` is het **klassenmidden** van die klasse.

- **Mediaan (Gegroepeerde lineaire interpolatie):**
  $$ Me = L + \frac{\frac{n}{2} - cf_{voor}}{f_{Me}} \cdot h $$
  - `L`: De ondergrens van de mediaanklasse.
  - `n`: Totaal aantal waarnemingen.
  - `cf_{voor}`: De cumulatieve frequentie van de klasse *voor* de mediaanklasse.
  - `f_{Me}`: De frequentie van de mediaanklasse zelf.
  - `h`: De klassenbreedte.

- **Modus (Gegroepeerd):**
  $$ Mo = L + \frac{\Delta_1}{\Delta_1 + \Delta_2} \cdot h $$
   - `L`: Ondergrens van de modale klasse.
   - `Δ₁`: Verschil in frequentie met de klasse *ervoor*.
   - `Δ₂`: Verschil in frequentie met de klasse *erna*.
   - `h`: Klassenbreedte.
---

**Waarom is dit belangrijk?**
Elke centrummaat vertelt een ander deel van het verhaal. Het gemiddelde geeft een algemeen beeld, de mediaan beschermt tegen extreme waarden, en de modus toont de meest populaire keuze. Samen geven ze een genuanceerd beeld van de "typische" waarde.
# Spreidingsmaten

## Overzicht
Spreidingsmaten zijn kengetallen die beschrijven hoe ver de data uit elkaar liggen (hoe "gespreid" de dataset is). Ze geven context bij een centrummaat: hoe consistent zijn de waarden?

## Variantie
De **variantie** is de gemiddelde gekwadrateerde afstand van elke waarde tot het gemiddelde. Het meet spreiding in gekwadrateerde eenheden.

### Formules
- **Conventie (n vs. n-1):**
  In sommige cursussen (ook in ons formularium) wordt de "beschrijvende" standaardafwijking/variantie met `n` in de noemer geschreven. In veel statistiekboeken gebruikt men `n-1` voor de onbevooroordeelde schatting van de populatievariantie.

- **Variantiesom (beschrijvend, noemer `n`):**
  $$ s_n^2 = \frac{1}{n}\sum_{i=1}^{n} (x_i - \bar{x})^2 $$

- **Onbevooroordeelde steekproefvariantie (noemer `n-1`):**
  $$ s^2 = \frac{1}{n-1}\sum_{i=1}^{n} (x_i - \bar{x})^2 $$

- **Populatievariantie (`σ²`):**
  $$ \sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N} $$

## Standaardafwijking
De **standaardafwijking** is de vierkantswortel van de variantie. Het is de meest gebruikte spreidingsmaat omdat het in dezelfde eenheid is als de data.

### Formules
- **Beschrijvende standaardafwijking (noemer `n`):**
  $$ s_n = \sqrt{\frac{1}{n}\sum_{i=1}^{n} (x_i - \bar{x})^2} $$

- **Onbevooroordeelde variantieschatting (noemer `n-1`):**
  $$ s = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n} (x_i - \bar{x})^2} $$

- **Populatiestandaardafwijking (`σ`):**
  $$ \sigma = \sqrt{\frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}} $$

- **Voor gegroepeerde data (rekenformule):**
  $$ s_n = \sqrt{\frac{\sum f_i \cdot X_i^2}{n} - \bar{x}^2} $$

  (Als je de variantie met `n-1` wil, pas je eerst de variantie-correctie toe: $s^2 = \frac{n}{n-1}s_n^2$.)

## Variatiebreedte (Range)
De **variatiebreedte** is het verschil tussen de hoogste en de laagste waarde.
$$ \text{Variatiebreedte} = \max(x) - \min(x) $$
Hij is extreem gevoelig voor uitschieters.

## Praktische keuze
- Standaardafwijking: meest bruikbaar als "standaard" spreidingsmaat.
- Variantie: vooral handig als tussenstap (bv. in formules).
- Variatiebreedte: snel inzicht, maar fragiel bij outliers.

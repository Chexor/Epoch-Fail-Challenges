# Centrummaten

## Overzicht
Centrummaten zijn kengetallen die het "midden" of het centrum van je data beschrijven. Ze geven een snelle indicatie van een "typische" waarde.

## Gemiddelde
Het **rekenkundig gemiddelde** is de som van alle waarden, gedeeld door het aantal waarden. Het is de meest gebruikte centrummaat, maar is gevoelig voor uitschieters.

### Formules
- **Steekproefgemiddelde (`x̄`):**
  $$ \bar{x} = \frac{\sum_{i=1}^{n} x_i}{n} $$

- **Populatiegemiddelde (`μ`):**
  $$ \mu = \frac{\sum_{i=1}^{N} x_i}{N} $$

- **Voor gegroepeerde data:**
  $$ \bar{x} = \frac{\sum f_i \cdot X_i}{n} $$
  Waarbij `Xᵢ` het klassenmidden is.

## Mediaan
De **mediaan** is de middelste waarde wanneer je alle data van klein naar groot rangschikt. De mediaan is robuust tegen uitschieters.

### Berekening
1.  Sorteer je dataset.
2.  Is het aantal waarden (`n`) oneven? De mediaan is de middelste waarde.
3.  Is het aantal waarden even? De mediaan is het gemiddelde van de twee middelste waarden.

### Voor gegroepeerde data
Voor gegroepeerde data wordt de mediaan geschat via lineaire interpolatie in de mediaanklasse.
$$ Me = L + \frac{\frac{n}{2} - cf_{voor}}{f_{Me}} \cdot h $$
- `L`: Ondergrens van de mediaanklasse.
- `cf_{voor}`: Cumulatieve frequentie van de klasse voor de mediaanklasse.
- `f_{Me}`: Frequentie van de mediaanklasse.
- `h`: Klassenbreedte.

## Modus
De **modus** is de waarde of categorie die het vaakst voorkomt in de dataset. Een dataset kan meerdere modi hebben (bimodaal, multimodaal) of geen.

### Voor gegroepeerde data
Voor gegroepeerde data wordt de modus geschat binnen de modale klasse (de klasse met de hoogste frequentie).
$$ Mo = L + \frac{\Delta_1}{\Delta_1 + \Delta_2} \cdot h $$
- `L`: Ondergrens van de modale klasse.
- `Δ₁`: Verschil in frequentie met de klasse ervoor.
- `Δ₂`: Verschil in frequentie met de klasse erna.
- `h`: Klassenbreedte.

## Wanneer welke?
- Gemiddelde: handig bij (ongeveer) symmetrische data zonder extreme uitschieters.
- Mediaan: beter bij scheve verdelingen of outliers.
- Modus: vooral nuttig bij categorische data of wanneer de meest voorkomende waarde belangrijk is.

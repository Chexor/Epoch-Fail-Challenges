# Oefening 2 - Finale samenvatting (zonder voorkennis)

## Opgave

![[DA-Voorbeeldexamen-Oef2.png]]

## Gegeven
- Aantal data: $n = 10$.
- Kleinste waarde: $24.5$.
- Grootste waarde: $64.5$.
- Gemiddelde: $\bar{X} = 42.5$.
- Standaardafwijking: $s = 10.0$.

## (a) Relevante formules
Formule: $\sum X_i = n \cdot \bar{X}$.

Formule: $s^2 = \frac{1}{n} \sum X_i^2 - \bar{X}^2$.

## (b) Som van de waarden en kwadraten
Gebruik de formules om de totale sommen te vinden.

### Rekenstappen (b)
- $\sum X_i = 10 \cdot 42.5 = 425$.
- $\sum X_i^2 = n(s^2 + \bar{X}^2) = 10(10^2 + 42.5^2) = 19062.5$.

## (c) Verwijder kleinste en grootste waarde
Haal $24.5$ en $64.5$ uit de sommen.

### Rekenstappen (c)
- Nieuwe som: $\sum X_i = 425 - 24.5 - 64.5 = 336$.
- Nieuwe som kwadraten: $\sum X_i^2 = 19062.5 - 24.5^2 - 64.5^2 = 14302$.

## (d) Nieuw gemiddelde en standaardafwijking
Je hebt nu $n = 8$ waarden over.

### Rekenstappen (d)
- Nieuw gemiddelde: $\bar{X} = 336 / 8 = 42$.
- Nieuwe variantie: $s^2 = 14302 / 8 - 42^2$.
- Nieuwe standaardafwijking: $s = \sqrt{14302 / 8 - 42^2} = 4.8734$.

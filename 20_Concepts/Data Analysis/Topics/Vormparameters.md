# Vormparameters

## Overzicht
Vormparameters beschrijven de vorm van je verdeling, voorbij het centrum en de spreiding. Ze helpen inschatten of een verdeling (ongeveer) symmetrisch/normaal is en hoe outlier-gevoelig ze is.

## Scheefheid (Skewness)
**Scheefheid** meet de asymmetrie van een verdeling.
- Positief (rechtsscheef): staart langer rechts, typisch geldt `Gemiddelde > Mediaan`.
- Negatief (linksscheef): staart langer links, typisch geldt `Gemiddelde < Mediaan`.

### Pearson (2 varianten)
Er bestaan twee veelgebruikte Pearson-benaderingen. In het formularium komt de eerste variant voor.

1) **Pearson op basis van modus** (formularium-notatie $Sk_p$):
$$ Sk_p = \frac{\bar{x} - Mo}{s} $$

2) **Pearson op basis van mediaan** (vaak "Pearson's 2nd" genoemd):
$$ \text{Sk} = \frac{3(\bar{x} - Me)}{s} $$

Interpretatie:
- positief: rechtsscheef
- negatief: linksscheef
- dicht bij 0: ongeveer symmetrisch

### Bowley (kwartielen)
Een robuuste maat (minder gevoelig voor outliers):
$$ Sk_B = \frac{(Q_3 - Me) - (Me - Q_1)}{Q_3 - Q_1} $$

## Topheid (Kurtosis)
**Topheid** meet de "gepiektheid" of "platheid" t.o.v. de normale verdeling, en beschrijft vooral het gewicht van de staarten.

- Leptokurtisch (hoge kurtosis): spitser, dikkere staarten, meer kans op extreme uitschieters.
- Platykurtisch (lage kurtosis): platter, dunnere staarten.

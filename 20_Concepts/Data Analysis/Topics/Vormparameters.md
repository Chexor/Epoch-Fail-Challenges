# Vormparameters: Scheefheid & Topheid

**Wat is het?**
Vormparameters beschrijven de vorm van je frequentieverdeling, voorbij het centrum en de spreiding.

1.  **Scheefheid (Skewness):** Meet de asymmetrie van de verdeling.
    -   **Positief Scheef (Rechtsscheef):** De "staart" van de verdeling is langer aan de rechterkant. Het gemiddelde is groter dan de mediaan.
    -   **Negatief Scheef (Linksscheef):** De "staart" is langer aan de linkerkant. Het gemiddelde is kleiner dan de mediaan.

**Formule & Berekening (Pearson's 2nd Skewness Coefficient):**
Een eenvoudige manier om scheefheid te benaderen is door het gemiddelde en de mediaan te vergelijken:
$$ \text{Sk} = \frac{3(\bar{x} - \text{Mediaan})}{s} $$
- `x̄` is het steekproefgemiddelde.
- `s` is de steekproefstandaardafwijking.
- **Interpretatie:**
  - `Sk > 0`: Rechtsscheef (gemiddelde > mediaan).
  - `Sk < 0`: Linksscheef (gemiddelde < mediaan).
  - `Sk ≈ 0`: Ongeveer symmetrisch.

2.  **Topheid (Kurtosis):** Meet de "gepiektheid" of "platheid" van de verdeling in vergelijking met de normale verdeling.
    -   **Leptokurtisch:** Spitser dan normaal (meer data in het centrum en de staarten).
    -   **Platykurtisch:** Platter dan normaal (minder data in het centrum en de staarten).

**Waarom is dit belangrijk?**
Ze geven cruciale informatie over de onderliggende structuur van je data en helpen bepalen of je data (bij benadering) normaal verdeeld zijn, wat een belangrijke aanname is voor veel statistische toetsen.
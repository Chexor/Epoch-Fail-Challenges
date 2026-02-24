# Toevalsvariabelen

**Wat is het?**
Een variabele, vaak genoteerd als `X`, waarvan de waarde een numerieke uitkomst is van een toevalsproces. We weten de waarde niet op voorhand, maar we kunnen wel de kansen van de mogelijke waarden beschrijven.

---

### Twee Soorten

1.  **Discrete Toevalsvariabele:** Kan een eindig, telbaar aantal waarden aannemen.
    -   *Voorbeeld:* Het aantal ogen `X` bij een worp met een dobbelsteen. Mogelijke waarden zijn {1, 2, 3, 4, 5, 6}.
    -   Beschreven door een **[[Functies van Toevalsvariabelen|kansfunctie]]** `P(X=x)`.

2.  **Continue Toevalsvariabele:** Kan elke waarde binnen een bepaald interval aannemen.
    -   *Voorbeeld:* De exacte lengte van een willekeurige student.
    -   Beschreven door een **[[Functies van Toevalsvariabelen|dichtheidsfunctie]]** `f(x)`.

---

### Belangrijke Eigenschappen

1.  **Verwachtingswaarde (E[X] of μ)**
    Het theoretische gemiddelde van de toevalsvariabele, of de waarde die je op lange termijn verwacht. Het is een gewogen gemiddelde van alle mogelijke waarden, gewogen door hun kans.

    **Formules & Berekening:**
    -   **Discreet:**
        $$ E[X] = \sum x \cdot P(X=x) $$
        (Voor elke mogelijke waarde `x`, vermenigvuldig die waarde met zijn kans en tel alles op.)
    -   **Continu:**
        $$ E[X] = \int_{-\infty}^{\infty} x \cdot f(x) \,dx $$
        (De integraal van `x` vermenigvuldigd met de dichtheidsfunctie.)

2.  **Variantie (Var(X) of σ²)**
    De verwachte gekwadrateerde afwijking van het gemiddelde. Het meet de spreiding van de toevalsvariabele.

    **Formules & Berekening:**
    -   **Definitie:**
        $$ \text{Var}(X) = E[(X - \mu)^2] $$
    -   **Praktische Rekenregel:**
        $$ \text{Var}(X) = E[X^2] - (E[X])^2 $$
        (De verwachtingswaarde van het kwadraat, min het kwadraat van de verwachtingswaarde.)

De **standaardafwijking** ($\sigma$) is simpelweg de wortel uit de variantie: $\sigma = \sqrt{\text{Var}(X)}$.

---
### Onafhankelijkheid en Rekenregels voor Som/Verschil
- **Onafhankelijkheid:** Twee toevalsvariabelen `X` en `Y` zijn onafhankelijk als de uitkomst van de een geen invloed heeft op de uitkomst van de ander. Formeel: $P(X=x \cap Y=y) = P(X=x) \cdot P(Y=y)$ voor alle `x` en `y`.

- **Verwachtingswaarde van Som/Verschil:**
  Dit geldt *altijd*, ook als de variabelen niet onafhankelijk zijn.
  $$ E[X \pm Y] = E[X] \pm E[Y] $$

- **Variantie van Som/Verschil:**
  De varianties mag je alleen optellen als de variabelen **onafhankelijk** zijn. Let op: de variantie van een verschil is ook een som! Meer spreiding is meer onzekerheid, en onzekerheid telt altijd op.
  $$ \text{Var}(X \pm Y) = \text{Var}(X) + \text{Var}(Y) \quad (\text{indien onafhankelijk}) $$
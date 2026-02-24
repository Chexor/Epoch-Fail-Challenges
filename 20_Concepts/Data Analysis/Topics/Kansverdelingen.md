# Kansverdelingen

**Wat is het?**
Een theoretisch model dat beschrijft hoe de kansen verdeeld zijn over de mogelijke waarden van een toevalsvariabele. Het is een wiskundige functie die een patroon in toeval beschrijft.

---

### 1. Binomiale Verdeling
Beschrijft het aantal successen (`k`) in een vast aantal onafhankelijke herhalingen (`n`), waarbij elke herhaling slechts twee uitkomsten heeft (succes of mislukking) met een constante kans op succes (`p`).

**Wanneer te gebruiken?**
Vier voorwaarden (acroniem: "Vaste Twee Onafhankelijke Kansen"):
1.  **Vast** aantal herhalingen (`n`).
2.  **Twee** mogelijke uitkomsten per herhaling.
3.  **Onafhankelijke** herhalingen.
4.  Constante **kans** op succes (`p`).

**Formule & Berekening:**
De kans op exact `k` successen in `n` pogingen is:
$$ P(X=k) = \binom{n}{k} p^k (1-p)^{n-k} $$
- $\binom{n}{k}$ is het [[Combinatiegetallen|combinatiegetal]]: het aantal manieren om `k` successen te kiezen uit `n` pogingen.
- $p^k$: de kans op `k` successen.
- $(1-p)^{n-k}$: de kans op `n-k` mislukkingen.

### 2. Normale Verdeling (Gauss-curve)
De belangrijkste continue kansverdeling. Het beschrijft talloze natuurlijke fenomenen en is de hoeksteen van de verklarende statistiek.

**Kenmerken:**
-   Symmetrisch en klokvormig.
-   Het gemiddelde, de mediaan en de modus vallen samen.
-   De vorm wordt volledig bepaald door twee parameters:
    -   **Populatiegemiddelde `μ`**: Bepaalt het centrum van de curve.
    -   **Populatiestandaardafwijking `σ`**: Bepaalt de breedte (spreiding) van de curve.
-   Notatie: $X \sim N(\mu, \sigma)$

**Standaardnormale Verdeling (Z-verdeling):**
Een speciale normale verdeling met een gemiddelde van 0 en een standaardafwijking van 1.
$$ Z \sim N(0, 1) $$
We kunnen elke normale verdeling omzetten naar een Z-verdeling met de **Z-score**:
$$ Z = \frac{X - \mu}{\sigma} $$
De Z-score drukt uit hoeveel standaardafwijkingen een waarde `X` van het gemiddelde `μ` verwijderd is.

---

**Waarom is dit belangrijk?**
Deze verdelingen zijn krachtige modellen. Als we kunnen aannemen dat onze data een bepaalde verdeling volgen, kunnen we met deze formules en de [[Toolbox - Statistische Tabellen|statistische tabellen]] specifieke kansen berekenen en voorspellingen doen. De normale verdeling is de basis voor de [[Centrale Limietstelling]] en dus voor bijna alle [[Hypothesetoetsen]] en [[Betrouwbaarheidsintervallen]].
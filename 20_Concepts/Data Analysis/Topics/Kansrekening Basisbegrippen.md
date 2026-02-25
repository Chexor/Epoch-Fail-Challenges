# Kansrekening: Basisbegrippen

**Wat is het?**
Kansrekening is de wiskunde van toeval. Het geeft ons een formele manier om de waarschijnlijkheid (notatie: `P`) van een bepaalde uitkomst of gebeurtenis te berekenen. Een kans is altijd een getal tussen 0 (onmogelijk) en 1 (zeker).

---

### Kernconcepten
-   **Universum (Ω):** De verzameling van álle mogelijke uitkomsten.
-   **Gebeurtenis (A, B, ...):** Een specifieke uitkomst of een verzameling van uitkomsten. Het is een deelverzameling van het universum.

---

### Fundamentele Rekenregels

#### Basisidee (Laplace + complement)
Als alle uitkomsten in een eindig universum even waarschijnlijk zijn:
$$ P(A) = \frac{\text{aantal gunstige uitkomsten}}{\text{totaal aantal mogelijke uitkomsten}} $$

De kans dat gebeurtenis A *niet* plaatsvindt, is 1 min de kans dat A wel plaatsvindt.
$$ P(A^c) = 1 - P(A) $$

#### Somregels
Als gebeurtenissen A en B elkaar uitsluiten (niet tegelijk kunnen gebeuren):
$$ P(A \cup B) = P(A) + P(B) $$
($\cup$ betekent "of")

Voor twee willekeurige gebeurtenissen A en B:
$$ P(A \cup B) = P(A) + P(B) - P(A \cap B) $$
($\cap$ betekent "en". We trekken de overlap eraf om dubbeltelling te voorkomen.)

#### Productregels
Als het plaatsvinden van A geen invloed heeft op de kans van B:
$$ P(A \cap B) = P(A) \cdot P(B) $$

Volgt direct uit de voorwaardelijke kans, voor twee willekeurige gebeurtenissen:
$$ P(A \cap B) = P(A|B) \cdot P(B) $$

#### Voorwaardelijke kans + Bayes
De kans op A, *gegeven dat* B heeft plaatsgevonden:
$$ P(A|B) = \frac{P(A \cap B)}{P(B)} $$

Draait een voorwaardelijke kans om. Hiermee bereken je $P(B|A)$ als je $P(A|B)$ weet.
$$ P(B|A) = \frac{P(A|B) \cdot P(B)}{P(A)} $$

---

**Waarom is dit belangrijk?**
Deze regels zijn de fundamentele bouwstenen om complexe kansproblemen op te splitsen in kleinere, beheersbare delen. Ze stellen ons in staat om onzekerheid te meten en voorspellingen te doen, van dobbelstenen tot financiële markten.

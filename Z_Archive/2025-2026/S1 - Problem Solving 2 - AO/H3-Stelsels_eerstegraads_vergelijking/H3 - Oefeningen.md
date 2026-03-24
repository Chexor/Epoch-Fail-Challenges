# H3 - Oefeningen

[[H3 - Stelsels van lineaire vergelijkingen]]

## Voorbeeld: Stelsel oplossen in wxMaxima

Hieronder staat de stap-voor-stap procedure om een stelsel op te lossen met de Gauss-Jordan eliminatiemethode, vertaald naar `wxMaxima`. Dit is de standaardprocedure die je op het examen moet volgen.

**Gegeven stelsel:**
```
x + y + 2z = 9
2x + 4y - 3z = 1
3x + 6y - 5z = 0
```

### Stap 1: Definieer de vergelijkingen

Eerst geven we de vergelijkingen in als een lijst.
```wxmx
stelsel: [x + y + 2*z = 9, 2*x + 4*y - 3*z = 1, 3*x + 6*y - 5*z = 0];
```

### Stap 2: Maak de gerande matrix [A | -B]

We gebruiken `augcoefmatrix` om de gerande matrix `[A | -B]` te maken. Let op de `-B` aan de rechterkant!
```wxmx
AB_neg: augcoefmatrix(stelsel, [x, y, z]);
```
**Resultaat:**
```
matrix(
[1, 1, 2, -9],
[2, 4, -3, -1],
[3, 6, -5, 0]
)
```

### Stap 3: Corrigeer naar [A | B]

De laatste kolom moet positief zijn. We vermenigvuldigen de 4e kolom met -1.
```wxmx
AB: columndiv(AB_neg, 4, -1);
```
**Resultaat:**
```
matrix(
[1, 1, 2, 9],
[2, 4, -3, 1],
[3, 6, -5, 0]
)
```

### Stap 4: Pas Gauss-Jordan toe (rref)

Dit is de belangrijkste stap. `rref()` (Reduced Row Echelon Form) voert de volledige eliminatie voor ons uit.
```wxmx
oplossing_matrix: rref(AB);
```
**Resultaat:**
```
matrix(
[1, 0, 0, 1],
[0, 1, 0, 2],
[0, 0, 1, 3]
)
```

### Stap 5: Lees de oplossing af

De linkerkant is nu de eenheidsmatrix. De rechterkolom is de oplossing voor `[x, y, z]`.
-   `x = 1`
-   `y = 2`
-   `z = 3`

---

## ✅ Jouw Oefeningen

Nu is het aan jou. Gebruik bovenstaande methode als sjabloon om de oefeningen uit de PDF's op te lossen in `wxMaxima`.

-   **Bestanden:** `oefn H3 (1).pdf` en `oefn H3 (2 tem 8).pdf`
-   **Doel:**
    1.  Stel voor elke oefening de `A*X=B` vorm op.
    2.  Los op met de `rref()` methode in `wxMaxima`.
    3.  Interpreteer het resultaat: is er een unieke oplossing, geen oplossing, of oneindig veel?

Maak hieronder voor elke oefening een klein verslagje van je oplossing.

---
type: examen-voorbeeld
vak: Introduction to AI
focus: zoekalgoritmes
status: actief
---

# Voorbeelden - Algoritmes uitschrijven op examen

## 1. Groot plaatje

Als je op het examen een graaf krijgt met een `startnode`, `goalnode`, afstanden en heuristische waarden, dan moet je meestal **niet alleen het eindpad geven**.

Je moet tonen:

- welke node telkens gekozen wordt
- hoe de `queue`, `stack` of `priority queue` evolueert
- welk pad op het einde gevonden wordt

De veiligste aanpak is dus altijd: **frontier uitschrijven na elke expansie**.

---

## 2. Afspraken voor de notatie

Gebruik in je uitwerking best altijd dezelfde afspraken:

- links in de frontier = **volgende element dat gekozen wordt**
- bij gelijke prioriteit: werk **alfabetisch** of volgens de gegeven buurvolgorde
- schrijf bij BFS/DFS/UCS/A* best **volledige paden** uit, niet alleen losse nodes
- schrijf bij heuristische algoritmes ook de score erbij

Voorbeeld notatie:

- `Queue: [A-B, A-C]`
- `Priority queue UCS: [A-B (g=2), A-C (g=4)]`
- `Priority queue A*: [A-B (g=2, h=4, f=6), A-C (g=4, h=5, f=9)]`

---

## 3. Voorbeeldgraaf

We gebruiken overal dezelfde graaf.

### Start en doel
- **Start**: `A`
- **Goal**: `G`

### Gewogen verbindingen
- `A-B = 2`
- `A-C = 4`
- `B-D = 2`
- `B-E = 5`
- `C-F = 3`
- `D-G = 7`
- `E-G = 2`
- `F-G = 2`

### Heuristische waarden `h(n)` naar `G`

| Node | h(n) |
| :--- | :--- |
| A | 6 |
| B | 4 |
| C | 5 |
| D | 6 |
| E | 1 |
| F | 2 |
| G | 0 |

### Visueel schema

```text
        A(6)
       /   \
    2 /     \ 4
     B(4)   C(5)
    /   \      \
  2/     \5     \3
  D(6)   E(1)   F(2)
    \      \      \
   7 \      \ 2    \ 2
      G(0)   G(0)   G(0)
```

---

## 4. Breadth-First Search (BFS)

## Idee
BFS kijkt alleen naar het aantal stappen, niet naar de afstanden.

## Datastructuur
- **queue (FIFO)**

## Uitwerking

Start:

- `Queue: [A]`

Expandeer `A`:

- opvolgers: `A-B`, `A-C`
- `Queue: [A-B, A-C]`

Expandeer `A-B`:

- opvolgers: `A-B-D`, `A-B-E`
- `Queue: [A-C, A-B-D, A-B-E]`

Expandeer `A-C`:

- opvolger: `A-C-F`
- `Queue: [A-B-D, A-B-E, A-C-F]`

Expandeer `A-B-D`:

- opvolger: `A-B-D-G`
- `Queue: [A-B-E, A-C-F, A-B-D-G]`

Expandeer `A-B-E`:

- opvolger: `A-B-E-G`
- `Queue: [A-C-F, A-B-D-G, A-B-E-G]`

Expandeer `A-C-F`:

- opvolger: `A-C-F-G`
- `Queue: [A-B-D-G, A-B-E-G, A-C-F-G]`

Neem eerste pad uit de queue:

- `A-B-D-G` eindigt in `G`

## Antwoord
- **gevonden pad**: `A-B-D-G`
- **opmerking**: BFS vindt hier het eerste doel op minimale diepte, maar **houdt geen rekening met gewichten**

---

## 5. Depth-First Search (DFS)

## Idee
DFS gaat zo diep mogelijk in de eerste tak.

## Datastructuur
- **stack (LIFO)**

## Uitwerking

Start:

- `Stack: [A]`

Expandeer `A` en zet opvolgers in omgekeerde volgorde zodat `B` eerst gekozen wordt:

- `Stack: [A-C, A-B]`

Neem `A-B`:

- opvolgers: `A-B-D`, `A-B-E`
- `Stack: [A-C, A-B-E, A-B-D]`

Neem `A-B-D`:

- opvolger: `A-B-D-G`
- `Stack: [A-C, A-B-E, A-B-D-G]`

Neem `A-B-D-G`:

- doel gevonden

## Antwoord
- **gevonden pad**: `A-B-D-G`
- **opmerking**: DFS geeft hier snel een oplossing, maar niet noodzakelijk de beste

---

## 6. Uniform-Cost Search (UCS)

## Idee
UCS kiest altijd het pad met de laagste totale kost `g(n)`.

## Datastructuur
- **priority queue**, gesorteerd op `g`

## Uitwerking

Start:

- `PQ: [A (g=0)]`

Expandeer `A`:

- `A-B (g=2)`
- `A-C (g=4)`
- `PQ: [A-B (2), A-C (4)]`

Expandeer `A-B`:

- `A-B-D (g=4)`
- `A-B-E (g=7)`
- `PQ: [A-C (4), A-B-D (4), A-B-E (7)]`

Bij gelijke kost nemen we alfabetisch `A-B-D` of volgens invoegvolgorde. We kiezen hier `A-B-D`.

Expandeer `A-B-D`:

- `A-B-D-G (g=11)`
- `PQ: [A-C (4), A-B-E (7), A-B-D-G (11)]`

Expandeer `A-C`:

- `A-C-F (g=7)`
- `PQ: [A-B-E (7), A-C-F (7), A-B-D-G (11)]`

Expandeer `A-B-E`:

- `A-B-E-G (g=9)`
- `PQ: [A-C-F (7), A-B-E-G (9), A-B-D-G (11)]`

Expandeer `A-C-F`:

- `A-C-F-G (g=9)`
- `PQ: [A-B-E-G (9), A-C-F-G (9), A-B-D-G (11)]`

Neem eerste doelpad met laagste kost:

- `A-B-E-G (g=9)`

## Antwoord
- **gevonden pad**: `A-B-E-G`
- **totale kost**: `9`
- **opmerking**: UCS houdt wel rekening met afstanden, dus vindt het goedkoopste pad

---

## 7. Hill Climbing

## Idee
Hill Climbing kijkt alleen naar de **huidige node** en kiest de buur met de beste heuristische waarde.

## Datastructuur
- geen volledige frontier zoals BFS/UCS
- enkel huidige node + buurvergelijking

## Uitwerking

Start in `A` met `h(A)=6`.

Vanuit `A`:

- `B` met `h=4`
- `C` met `h=5`
- kies `B`

Pad tot nu toe:

- `A-B`

Vanuit `B`:

- `D` met `h=6`
- `E` met `h=1`
- kies `E`

Pad tot nu toe:

- `A-B-E`

Vanuit `E`:

- `G` met `h=0`
- kies `G`

## Antwoord
- **gevonden pad**: `A-B-E-G`
- **opmerking**: Hill Climbing gebruikt alleen de lokale heuristische verbetering, niet de volledige kost `g(n)`

---

## 8. Greedy Best-First Search

## Idee
Greedy kiest altijd het frontier-pad waarvan de eindnode de kleinste `h(n)` heeft.

## Datastructuur
- **priority queue**, gesorteerd op `h`

## Uitwerking

Start:

- `PQ: [A (h=6)]`

Expandeer `A`:

- `A-B (h=4)`
- `A-C (h=5)`
- `PQ: [A-B (4), A-C (5)]`

Expandeer `A-B`:

- `A-B-D (h=6)`
- `A-B-E (h=1)`
- `PQ: [A-B-E (1), A-C (5), A-B-D (6)]`

Expandeer `A-B-E`:

- `A-B-E-G (h=0)`
- `PQ: [A-B-E-G (0), A-C (5), A-B-D (6)]`

Neem eerste pad:

- `A-B-E-G`

## Antwoord
- **gevonden pad**: `A-B-E-G`
- **totale kost van dat pad**: `9`
- **opmerking**: Greedy gebruikt alleen `h(n)`, niet `g(n)`

---

## 9. A* Search

## Idee
A* kiest het frontier-pad met de laagste `f(n) = g(n) + h(n)`.

## Datastructuur
- **priority queue**, gesorteerd op `f`

## Uitwerking

Start:

- `PQ: [A (g=0, h=6, f=6)]`

Expandeer `A`:

- `A-B: g=2, h=4, f=6`
- `A-C: g=4, h=5, f=9`
- `PQ: [A-B (6), A-C (9)]`

Expandeer `A-B`:

- `A-B-D: g=4, h=6, f=10`
- `A-B-E: g=7, h=1, f=8`
- `PQ: [A-B-E (8), A-C (9), A-B-D (10)]`

Expandeer `A-B-E`:

- `A-B-E-G: g=9, h=0, f=9`
- `PQ: [A-C (9), A-B-E-G (9), A-B-D (10)]`

Bij gelijke `f` nemen we alfabetisch of volgens invoegvolgorde. We nemen hier `A-B-E-G` als doelpad.

## Antwoord
- **gevonden pad**: `A-B-E-G`
- **totale kost**: `9`
- **opmerking**: A* combineert echte kost en heuristiek, daarom is het sterker dan Greedy

---

## 10. IDS kort voorbeeld

Bij `Iterative Deepening Search` schrijf je meestal geen queue uit, maar **opeenvolgende dieptelimieten**.

### Limiet 0
- bezoek: `A`
- geen doel

### Limiet 1
- bezoek: `A, B, C`
- geen doel

### Limiet 2
- bezoek: `A, B, D, E, C, F`
- geen doel

### Limiet 3
- bezoek: `A, B, D, G`
- doel gevonden

## Antwoord
- **gevonden pad**: `A-B-D-G`

---

## 11. Schrijfsjabloon voor het examen

Als je een graaf krijgt, kan je dit stramien letterlijk volgen.

## BFS / DFS

```text
Start: [S]
Expandeer S -> [...]
Expandeer ... -> [...]
...
Doel gevonden: S-...-G
```

## UCS

```text
PQ: [S (g=0)]
Expandeer S -> [...]
PQ: [...]
Expandeer ... -> [...]
PQ: [...]
Doel gevonden: S-...-G met kost ...
```

## Greedy

```text
PQ: [S (h=...)]
Expandeer S -> [...]
PQ: [...]
Doel gevonden: S-...-G
```

## A*

```text
PQ: [S (g=0, h=..., f=...)]
Expandeer S -> [...]
PQ: [...]
Doel gevonden: S-...-G met kost ...
```

## Hill Climbing

```text
Huidige node: S
Buren: ...
Beste buur: ...
Nieuw pad: S-...
...
Doel gevonden: S-...-G
```

---

## 12. Examenfocus

- Schrijf altijd de **frontier na elke stap** uit.
- Maak duidelijk **waarom** een node gekozen wordt:
  - BFS: eerste in queue
  - DFS: bovenste van de stack
  - UCS: laagste `g`
  - Greedy: laagste `h`
  - A*: laagste `f`
- Vermeld bij A* en UCS altijd de **totale kost van het eindpad**.
- Als er heuristische waarden gegeven zijn, noteer ze expliciet bij de relevante algoritmes.
- Als er gelijke waarden zijn, vermeld je best kort je tie-break regel.

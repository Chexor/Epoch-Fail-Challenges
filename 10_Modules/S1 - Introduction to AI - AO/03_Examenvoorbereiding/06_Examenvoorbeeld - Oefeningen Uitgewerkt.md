---
type: examen-voorbeeld
vak: Introduction to AI
status: actief
related:
  - 04_Frontier correct uitschrijven op papier
  - 04_Frontier correct uitschrijven op papier
---

# Examenvoorbeeld: Oefeningen Uitgewerkt

> [!info]- Inhoudsopgave
> - [[#Korte kern]]
> - [[#Deel 1: Grid Search (Opdracht 1 - Basic Search)]]
> 	- [[#Gegeven uit Opdracht 1]]
> 	- [[#Hoe schrijf je dit op het examen? (Voorbeeld: DFS)]]
> - [[#Deel 2: Graph met Heuristiek (Opdracht 2 & 3 - Heuristic/Optimal Search)]]
> 	- [[#Hoe schrijf je dit op het examen? (Voorbeeld: A*)]]
> - [[#Conclusie & Controle]]
> - [[#Deel 3: Volledig Uitgewerkte Referentiegraaf]]
> 	- [[#Afspraken voor de notatie]]
> 	- [[#Voorbeeldgraaf]]
> 	- [[#Start en doel]]
> 	- [[#Gewogen verbindingen]]
> 	- [[#Heuristische waarden `h(n)` naar `G`]]
> 	- [[#Visueel schema]]
> 	- [[#1. Breadth-First Search (BFS)]]
> 	- [[#2. Depth-First Search (DFS)]]
> 	- [[#3. Uniform-Cost Search (UCS)]]
> 	- [[#4. Hill Climbing]]
> 	- [[#5. Greedy Best-First Search]]
> 	- [[#6. A* Search]]
> 	- [[#7. IDS kort voorbeeld]]
> 	- [[#8. Schrijfsjabloon voor het examen]]
> 	- [[#9. Examenfocus]]
> - [[#Deel 4: Neuraal Netwerk (Forward Pass met ReLU)]]
> 	- [[#Voorbeeld Opgave]]
> - [[#Deel 5: State Space Formulering (bv. Water Jugs)]]
> 	- [[#Voorbeeld: The Water Jugs Problem]]

Op het examen krijg je vaak twee soorten oefeningen om zoekalgoritmes op uit te voeren: een **Grid (Raster)** en een **Graaf (Graph)**. Hieronder zie je, gebaseerd op de opdrachten uit `03_Oefeningen`, exact hoe je deze op papier uitschrijft.

## Korte kern
- **Grid Search:** Schrijf de coördinaten (rij, kolom) in je Queue/Stack en vermeld expliciet je vaste zoekrichting (bijv. _Up, Left, Right, Down_).
- **Graph Search:** Vermeld knooppunt-namen en hou altijd $g(n)$, $h(n)$ en $f(n)$ bij in je Priority Queue.

---

## Deel 1: Grid Search (Opdracht 1 - Basic Search)

Bij een Grid Search (zoals een doolhof) krijg je een matrix met een Start (`S`) en een Goal (`G`), plus enkele obstakels. Vaak moet je **Breadth-First Search (BFS)** of **Depth-First Search (DFS)** toepassen.

### Gegeven uit Opdracht 1
- **Start (S):** Coördinaat `(5, 3)` (Rij 5, Kolom 3)
- **Goal (G):** Coördinaat `(2, 2)` (Rij 2, Kolom 2)
- **Regel:** Legal steps in this order: **Up, Left, Right, Down**.

### Hoe schrijf je dit op het examen? (Voorbeeld: DFS)

Bij een Grid worden de paden heel lang om volledig op te schrijven. Tenzij de docent expliciet om het volledige pad vraagt per stap, volstaat het vaak om de **huidige node** en de **nieuwe acties** te noteren in de datastructuur, in de vorm van `(rij, kolom)`. 

**Startnotatie:**
> _"Ik gebruik DFS (Stack). Tie-breaker (volgorde van toevoegen): Up, Left, Right, Down. Om de juiste node bovenaan de stack te krijgen, push ik de buren in **omgekeerde volgorde** (Down, Right, Left, Up)."_

**Uitwerking (eerste paar stappen):**

```text
Stack = [ (5,3) ]

Kies: (5,3)
Genereer geldige buren (niet geblokkeerd/bezocht): 
- Up (4,3)
- Left (5,2) is geblokkeerd ■
- Right (5,4)
- Down (6,3)
Push in omgekeerde volgorde (Down, Right, Up):
Nieuwe Stack = [ (4,3), (5,4), (6,3) ]

Kies: (4,3)  <-- Neem altijd het eerste (bovenste) element!
Genereer buren vanaf (4,3):
- Up (3,3) is geblokkeerd ■
- Left (4,2)
- Right (4,4)
- Down (5,3) is de parent (niet opnieuw toevoegen als je loops vermijdt)
Push in omgekeerde volgorde (Right, Left):
Nieuwe Stack = [ (4,2), (4,4), (5,4), (6,3) ]

Kies: (4,2)
Genereer buren vanaf (4,2):
- Up (3,2) is geblokkeerd ■
- Left (4,1) is geblokkeerd ■
- Right (4,3) was de parent
- Down (5,2) is geblokkeerd ■
Dead-end! Geen nieuwe buren.
Nieuwe Stack = [ (4,4), (5,4), (6,3) ]  <-- (4,2) is gewoon weggenomen.

Kies: (4,4)
... (gaat verder tot Goal (2,2) wordt gekozen uit de stack)
```

**Examen Tip voor Grids:** Teken na elke expansie met potlood in het grid een pijltje of een volgnummer (zoals in de modeloplossing: `1, 2, 3...`) zodat je zelf niet in de war raakt welke nodes al in de "Explored" set zitten!

---

## Deel 2: Graph met Heuristiek (Opdracht 2 & 3 - Heuristic/Optimal Search)

Hier krijg je een netwerk van nodes (bijv. steden `A, B, C...`) met **afstanden op de verbindingen** ($g$) en een **heuristische tabel** ($h$).

### Hoe schrijf je dit op het examen? (Voorbeeld: A*)

Bij een Graph Search schrijf je wél het volledige pad uit in de Frontier, omdat je de cumulatieve kosten ($g$) moet optellen. 

**Startnotatie:**
> _"Ik gebruik A* (Priority Queue). Evaluatiefunctie $f(n) = g(n) + h(n)$. Tie-breaker: Alfabetisch sorteren bij gelijke $f$-waarde."_

**Uitwerking (Conceptueel voorbeeld obv Opdracht 3):**

Stel Start is `S`, Goal is `G`. Heuristiek van `S` = 10.
- `S` -> `A` (kost 3), $h(A) = 6$
- `S` -> `B` (kost 4), $h(B) = 4$

```text
Priority Queue = [ S (g=0, h=10, f=10) ]

Kies: S (f=10)
Genereer buren:
- Pad S-A: kost is 0 + 3 = 3. Dus: g=3, h=6 -> f=9
- Pad S-B: kost is 0 + 4 = 4. Dus: g=4, h=4 -> f=8
Sorteer Priority Queue op f-waarde (laagste eerst):
Nieuwe Priority Queue = [ S-B (f=8), S-A (f=9) ]

Kies: S-B (f=8)
Genereer buren van B: 
- Pad S-B-G: kost is 4 + 4 = 8. Dus: g=8, h=0 -> f=8
- Pad S-B-C: kost is 4 + 2 = 6. Dus: g=6, h=5 -> f=11
Sorteer Priority Queue:
Nieuwe Priority Queue = [ S-B-G (f=8), S-A (f=9), S-B-C (f=11) ]

Kies: S-B-G (f=8)
Dit is de GOAL node! 
Stop het algoritme.
```

**Examen Tip voor Heuristiek:**
Vergeet **nooit** de $g(n)$ op te tellen bij A* en UCS. Een veelgemaakte fout (ook in eerdere examens) is dat men bij A* alleen naar de heuristiek of de laatste link-kost kijkt, in plaats van de _cumulatieve_ kost vanaf het startpunt.

## Conclusie & Controle
Als je deze uitschrijf-methode consequent aanhoudt, laat je aan de docent zien dat je het **mechanisme** van de frontier 100% begrijpt. Dit levert vaak al (deel)punten op, zelfs als je onderweg per ongeluk een klein telfoutje maakt.---

## Deel 3: Volledig Uitgewerkte Referentiegraaf

Als je op het examen een graaf krijgt met een `startnode`, `goalnode`, afstanden en heuristische waarden, dan moet je meestal **niet alleen het eindpad geven**.

Je moet tonen:

- welke node telkens gekozen wordt
- hoe de `queue`, `stack` of `priority queue` evolueert
- welk pad op het einde gevonden wordt

De veiligste aanpak is dus altijd: **frontier uitschrijven na elke expansie**.

---

### Afspraken voor de notatie

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

### Voorbeeldgraaf

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

### 1. Breadth-First Search (BFS)

#### Idee
BFS kijkt alleen naar het aantal stappen, niet naar de afstanden.

#### Datastructuur
- **queue (FIFO)**

#### Uitwerking

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

#### Antwoord
- **gevonden pad**: `A-B-D-G`
- **opmerking**: BFS vindt hier het eerste doel op minimale diepte, maar **houdt geen rekening met gewichten**

---

### 2. Depth-First Search (DFS)

#### Idee
DFS gaat zo diep mogelijk in de eerste tak.

#### Datastructuur
- **stack (LIFO)**

#### Uitwerking

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

#### Antwoord
- **gevonden pad**: `A-B-D-G`
- **opmerking**: DFS geeft hier snel een oplossing, maar niet noodzakelijk de beste

---

### 3. Uniform-Cost Search (UCS)

#### Idee
UCS kiest altijd het pad met de laagste totale kost `g(n)`.

#### Datastructuur
- **priority queue**, gesorteerd op `g`

#### Uitwerking

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

#### Antwoord
- **gevonden pad**: `A-B-E-G`
- **totale kost**: `9`
- **opmerking**: UCS houdt wel rekening met afstanden, dus vindt het goedkoopste pad

---

### 4. Hill Climbing

#### Idee
Hill Climbing kijkt alleen naar de **huidige node** en kiest de buur met de beste heuristische waarde.

#### Datastructuur
- geen volledige frontier zoals BFS/UCS
- enkel huidige node + buurvergelijking

#### Uitwerking

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

#### Antwoord
- **gevonden pad**: `A-B-E-G`
- **opmerking**: Hill Climbing gebruikt alleen de lokale heuristische verbetering, niet de volledige kost `g(n)`

---

### 5. Greedy Best-First Search

#### Idee
Greedy kiest altijd het frontier-pad waarvan de eindnode de kleinste `h(n)` heeft.

#### Datastructuur
- **priority queue**, gesorteerd op `h`

#### Uitwerking

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

#### Antwoord
- **gevonden pad**: `A-B-E-G`
- **totale kost van dat pad**: `9`
- **opmerking**: Greedy gebruikt alleen `h(n)`, niet `g(n)`

---

### 6. A* Search

#### Idee
A* kiest het frontier-pad met de laagste `f(n) = g(n) + h(n)`.

#### Datastructuur
- **priority queue**, gesorteerd op `f`

#### Uitwerking

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

#### Antwoord
- **gevonden pad**: `A-B-E-G`
- **totale kost**: `9`
- **opmerking**: A* combineert echte kost en heuristiek, daarom is het sterker dan Greedy

---

### 7. IDS kort voorbeeld

Bij `Iterative Deepening Search` schrijf je meestal geen queue uit, maar **opeenvolgende dieptelimieten**.

#### Limiet 0
- bezoek: `A`
- geen doel

#### Limiet 1
- bezoek: `A, B, C`
- geen doel

#### Limiet 2
- bezoek: `A, B, D, E, C, F`
- geen doel

#### Limiet 3
- bezoek: `A, B, D, G`
- doel gevonden

#### Antwoord
- **gevonden pad**: `A-B-D-G`

---

### 8. Schrijfsjabloon voor het examen

Als je een graaf krijgt, kan je dit stramien letterlijk volgen.

#### BFS / DFS

```text
Start: [S]
Expandeer S -> [...]
Expandeer ... -> [...]
...
Doel gevonden: S-...-G
```

#### UCS

```text
PQ: [S (g=0)]
Expandeer S -> [...]
PQ: [...]
Expandeer ... -> [...]
PQ: [...]
Doel gevonden: S-...-G met kost ...
```

#### Greedy

```text
PQ: [S (h=...)]
Expandeer S -> [...]
PQ: [...]
Doel gevonden: S-...-G
```

#### A*

```text
PQ: [S (g=0, h=..., f=...)]
Expandeer S -> [...]
PQ: [...]
Doel gevonden: S-...-G met kost ...
```

#### Hill Climbing

```text
Huidige node: S
Buren: ...
Beste buur: ...
Nieuw pad: S-...
...
Doel gevonden: S-...-G
```

---

### 9. Examenfocus

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

## Deel 4: Neuraal Netwerk (Forward Pass met ReLU)
Bij vragen over neurale netwerken wordt vaak gevraagd om een "forward pass" te berekenen. Je berekent de waarde van elke knoop door de som te nemen van (Input × Gewicht). Vervolgens pas je de activatiefunctie (meestal ReLU) toe op die som.

**De ReLU regel (Rectified Linear Unit):** `f(x) = max(0, x)`
- Is de som **negatief**? De output wordt **0**.
- Is de som **positief**? De output blijft **het getal zelf**.

### Voorbeeld Opgave
Een simpel netwerk met 2 inputs ($I_1 = 3$, $I_2 = -2$), twee hidden nodes ($H_1$, $H_2$), en één output node ($O$).
Gewichten naar $H_1$: $w_1 = 1$, $w_2 = 2$
Gewichten naar $H_2$: $w_3 = 2$, $w_4 = -1$
Gewichten naar $O$: $w_5 = 1$, $w_6 = 1$ (Als gewichten naar de output niet gegeven zijn, veronderstel 1).

##### Uitwerking Stappenplan

**Stap 1: Bereken Bovenste Hidden Node ($H_1$)**
1. Som berekenen: $(I_1 \times w_1) + (I_2 \times w_2)$
2. Invullen: $(3 \times 1) + (-2 \times 2) = 3 - 4 = -1$
3. ReLU toepassen: $ReLU(-1) = 0$
4. **Output van $H_1$ is 0.**

**Stap 2: Bereken Onderste Hidden Node ($H_2$)**
1. Som berekenen: $(I_1 \times w_3) + (I_2 \times w_4)$
2. Invullen: $(3 \times 2) + (-2 \times -1) = 6 + 2 = 8$
3. ReLU toepassen: $ReLU(8) = 8$
4. **Output van $H_2$ is 8.**

**Stap 3: Bereken de Output Node ($O$)**
1. Som berekenen: $(H_1 \times w_5) + (H_2 \times w_6)$
2. Invullen: $(0 \times 1) + (8 \times 1) = 0 + 8 = 8$
3. ReLU toepassen (indien gevraagd): $ReLU(8) = 8$
4. **De finale output is 8.**

---
## Deel 5: State Space Formulering (bv. Water Jugs)

Soms krijg je geen visuele graaf of doolhof, maar een **tekstueel probleem** (zoals de bekende _Water Jugs_ oefening uit Opdracht 2). Je moet dan zelf de _State Space_ opstellen.

### Voorbeeld: The Water Jugs Problem
Je hebt een kruik van 4 liter en een kruik van 3 liter. Beide zijn leeg. Je wil exact 2 liter in de 4-liter kruik krijgen. Je mag kruiken volledig vullen, volledig leegmaken, of overgieten tot de ene vol is of de andere leeg.

**Hoe schrijf je dit formeel uit?**

1. **State representation:**
   Een state wordt voorgesteld als `[x, y]` waarbij `x` = inhoud 4L-kruik en `y` = inhoud 3L-kruik.
2. **Initial State:**
   `[0, 0]`
3. **Goal State:**
   `[2, 0]` (of `[2, y]` als het niet uitmaakt wat in de kleine zit).
4. **Operatoren (Rules):**
   - Vul 4L: `[x, y], x < 4  ->  [4, y]`
   - Vul 3L: `[x, y], y < 3  ->  [x, 3]`
   - Leeg 4L: `[x, y], x > 0  ->  [0, y]`
   - Leeg 3L: `[x, y], y > 0  ->  [x, 0]`
   - Giet 3L in 4L: `[x, y], x+y <= 4, y > 0  ->  [x+y, 0]`
   - Giet 4L in 3L: `[x, y], x+y <= 3, x > 0  ->  [0, x+y]`
   - ... (en zo verder voor deellimieten).

**Examen Tip voor State Spaces:**
Als ze vragen om hier **Hill Climbing** of **A*** op toe te passen, zal de docent een specifieke **heuristiek formule** geven, bijvoorbeeld:
$h([x,y]) = f(x) + f(y)$ met een tabel voor de waarden van $f$.
Je rekent dan voor elke geldige regel uit welke nieuwe state `[x, y]` je krijgt, berekent de nieuwe `h`-waarde voor die state, en kiest (bij Hill Climbing) de buur met de laagste (beste) `h`. Je noteert dit simpelweg als een netwerk van nodes: `[0,0] -> [4,0]` etc. Net als een gewone graaf, maar de 'nodes' zijn nu de coördinaten van je kruiken.

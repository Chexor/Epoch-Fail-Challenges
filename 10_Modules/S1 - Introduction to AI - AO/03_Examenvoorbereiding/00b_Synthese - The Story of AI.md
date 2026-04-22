---
type: examen-samenvatting
vak: Introduction to AI
status: uitgebreid
bronnen:
  - "[[00_Centrale examensamenvatting]]"
  - "[[01_Focus voor vrijdag]]"
  - "[[04_Frontier correct uitschrijven op papier]]"
---

# Synthese Examen: Introduction to AI

> [!info]- Inhoudsopgave
> - [[#1. Het Grote Plaatje: Welk Probleem Lossen We Op?]]
> 	- [[#Wat wordt er van je verwacht?]]
> - [[#2. De Intuïtie: Begrip Vóór de Formules]]
> 	- [[#A. De Kern van "Search"]]
> 	- [[#B. Twee Grote Families van Algoritmes]]
> - [[#3. De Formele Structuur: Details & Vergelijking]]
> 	- [[#A. De Datastructuren van de Frontier Uitgelegd]]
> 	- [[#B. Gedetailleerde Werking van Kernalgoritmes]]
> 	- [[#C. Kritische Concepten Verdiept]]
> - [[#4. De Toepassing: Examenstrategie]]
> 	- [[#A. Algoritmes Uitschrijven op een Graaf]]
> 	- [[#B. Machine Learning Hoofdlijnen Verdiept]]
> 	- [[#C. Typische Examenvallen]]

Deze nota bundelt alle kerninformatie voor het examen `Introduction to AI` in een gestructureerd overzicht. De didactische methode "Whole-to-Detail" wordt hier gevolgd.

---

## 1. Het Grote Plaatje: Welk Probleem Lossen We Op?

Het examen test primair je vermogen om **zoekproblemen systematisch op te lossen**. De kernvraag is: "Hoe kan een agent op een intelligente manier een doel bereiken in een gegeven omgeving (de 'State Space')?"

### Wat wordt er van je verwacht?
- **Begrip:** Je snapt de theorie achter de belangrijkste zoekalgoritmes.
- **Toepassing:** Je kan deze algoritmes foutloos en stap voor stap uitvoeren op een graaf.
- **Analyse:** Je kan de algoritmes vergelijken en uitleggen waarom ze bepaalde keuzes maken.
- **Communicatie:** Je kan je redenering helder en beknopt uitleggen, zowel op papier als mondeling.

**Examenvorm:** Een combinatie van meerkeuzevragen, een praktische oefening op een graaf, en open/mondelinge theorievragen. Snelheid en accuraatheid zijn cruciaal.

---

## 2. De Intuïtie: Begrip Vóór de Formules

### A. De Kern van "Search"
Stel je een doolhof voor. Je staat bij de ingang (`initial state`) en je wilt naar de uitgang (`goal state`). Elke stap die je zet is een `operator`. De weg die je aflegt is een `path`. De hele doolhof is de `state space`.

Een zoekalgoritme is simpelweg een **strategie** om dit doolhof te verkennen.

- **De Frontier:** Dit is je "to-do-lijst" van plekken die je hebt ontdekt maar nog niet bezocht. Elk algoritme beheert deze lijst op een andere manier.
- **De Explored Set:** Dit is de lijst van plekken waar je al geweest bent. Dit voorkomt dat je in cirkels loopt.

**De centrale vraag is altijd: Welke plek op mijn to-do-lijst (frontier) kies ik als volgende?**

### B. Twee Grote Families van Algoritmes

1.  **Blind Search (Niet-geïnformeerd zoeken):**
    - **Intuïtie:** Je hebt geen kaart en geen kompas. Je volgt een simpele, vaste regel.
    - **Voorbeelden:**
        - **BFS (Breadth-First Search):** Verken alle paden van 1 stap lang, dan alle paden van 2 stappen, etc. (breedte eerst).
        - **DFS (Depth-First Search):** Volg één pad zo diep mogelijk. Als het doodloopt, keer je terug en probeer je een andere afslag (diepte eerst).
        - **UCS (Uniform-Cost Search):** Kies altijd het pad dat tot nu toe het goedkoopst was (laagste `g(n)`).

2.  **Heuristic Search (Geïnformeerd zoeken):**
    - **Intuïtie:** Stel je voor dat je een muis in het doolhof bent die de kaas (`goal`) kan ruiken. De sterkte van de kaasgeur is je **heuristiek (`h(n)`)**. Het is een *slimme gok* die je vertelt hoe dicht je waarschijnlijk bij de kaas bent. Je volgt de geur in de hoop sneller de kaas te vinden dan wanneer je willekeurig zou rondlopen. Dit "gevoel" voor richting maakt de zoektocht geïnformeerd.
    - **Voorbeelden:**
        - **Greedy Best-First Search:** Wees gulzig. Kies altijd de plek die *lijkt* het dichtst bij de uitgang te zijn (laagste `h(n)`).
        - **A\* Search:** De slimste van de hoop. Combineert de al afgelegde kost (`g(n)`) met de geschatte kost tot het doel (`h(n)`). De totale geschatte kost is `f(n) = g(n) + h(n)`. Kies het pad met de laagste `f(n)`.
        - **Hill Climbing:** Een simpele, lokale zoektocht. Kijk alleen naar je directe buren en stap naar de beste. Stopt als er geen betere buur is.

---

## 3. De Formele Structuur: Details & Vergelijking

### A. De Datastructuren van de Frontier Uitgelegd

De manier waarop de `frontier` (de to-do-lijst) beheerd wordt, bepaalt het gedrag van het algoritme. Dit gebeurt met specifieke datastructuren:

-   **Queue (Wachtrij):**
    -   **Principe:** First-In, First-Out (FIFO). Wie het eerst komt, wordt het eerst geholpen.
    -   **Analogie:** Een rij voor de kassa. Nieuwe mensen sluiten achteraan aan, en de persoon vooraan wordt als eerste geholpen.
    -   **Gebruikt door:** [[Breadth-First Search (BFS)]]. BFS voegt nieuwe nodes achteraan de frontier toe, en kiest altijd de node vooraan. Dit zorgt ervoor dat het laag na laag de graaf verkent.

-   **Stack (Stapel):**
    -   **Principe:** Last-In, First-Out (LIFO). Wat er als laatste opgelegd wordt, wordt als eerste afgehaald.
    -   **Analogie:** Een stapel borden. Je zet een nieuw bord bovenop, en als je een bord nodig hebt, pak je ook het bovenste.
    -   **Gebruikt door:** [[Depth-First Search (DFS)]]. DFS voegt nieuwe nodes "bovenop" de frontier en kiest ook altijd de bovenste. Dit zorgt ervoor dat het algoritme zo snel mogelijk de diepte in duikt.

-   **Priority Queue (Voorrangswachtrij):**
    -   **Principe:** Items worden niet op volgorde van aankomst verwerkt, maar op basis van een **prioriteitsscore**. Het item met de beste score wordt eerst gekozen.
    -   **Analogie:** De boarding gate op een vliegveld. Passagiers in First Class mogen eerst boarden, zelfs als ze later bij de gate aankwamen dan passagiers in Economy. Hun "ticket" geeft hen prioriteit.
    -   **Gebruikt door:** [[Uniform-Cost Search (UCS)]] (prioriteit = laagste `g(n)`), [[Greedy Best-First Search]] (prioriteit = laagste `h(n)`) en [[A-star Search|A* Search]] (prioriteit = laagste `f(n)`).

### B. Gedetailleerde Werking van Kernalgoritmes

-   **BFS:** Verkent systematisch niveau per niveau. Garandeert het vinden van de kortste weg in termen van *aantal stappen*. Het is ideaal als alle stapkosten gelijk zijn.
-   **DFS:** Duikt zo snel mogelijk de diepte in. Het is geheugenefficiënt (hoeft maar één pad te onthouden), maar kan vastlopen in oneindig diepe paden of lussen als er geen `explored set` wordt gebruikt. Het vindt zelden een optimale oplossing.
-   **UCS:** Is de slimmere versie van BFS voor als stapkosten verschillen. Het kiest altijd het pad met de laagste *totale kost vanaf de start* (`g(n)`). Het is een soort Dijkstra's algoritme en garandeert het vinden van de goedkoopste oplossing.
-   **Greedy Search:** Is kortzichtig. Het kijkt enkel naar de geschatte afstand tot het doel (`h(n)`) en negeert de reeds afgelegde weg. Hierdoor kan het een pad kiezen dat initieel veelbelovend lijkt, maar uiteindelijk veel duurder is.
-   **A\* Search:** Is de gouden standaard. Het combineert de sterkte van UCS (kijkt naar de afgelegde kost `g(n)`) met de sterkte van Greedy (gebruikt een schatting `h(n)`). Door de laagste `f(n) = g(n) + h(n)` te kiezen, vindt het een balans tussen wat al afgelegd is en wat nog moet komen.

### C. Kritische Concepten Verdiept
- **g(n):** De *werkelijke* kost van de startnode tot node `n`.
- **h(n):** De *geschatte* kost van node `n` tot de goal.
- **f(n):** De *geschatte totale* kost van een pad via node `n`. `f(n) = g(n) + h(n)`.
- **Admissible Heuristic:** Een "optimistische" heuristiek. Het overschat *nooit* de werkelijke kost. Dit is een harde eis voor A\* om optimaal te zijn. Als je h(n) een te hoge schatting geeft, zou A\* een potentieel optimaal pad kunnen negeren omdat het ten onrechte te duur lijkt.
- **Consistent Heuristic:** Een nog strengere eis. Het zorgt ervoor dat de geschatte kost (`f`) langs een pad nooit daalt. Als een heuristiek consistent is, is ze automatisch ook admissible.

---

## 4. De Toepassing: Examenstrategie

### A. Algoritmes Uitschrijven op een Graaf

Dit is de kern van de praktische proef. Volg deze stappen rigoureus:

**Voorbereiding:**
1.  Identificeer het gevraagde algoritme.
2.  Noteer de juiste datastructuur (Queue, Stack, Priority Queue).
3.  Noteer je tie-break regel (bv. "Bij gelijke scores kies ik alfabetisch").

**Uitvoering (Stap-voor-Stap):**

```text
Stap 0: Frontier = [ (StartNode, score=...) ]

---
Stap 1:
Kies: ... (de beste node uit de frontier)
Genereer: ... (de opvolgers/buren)
Nieuwe Frontier: [ ... ] (voeg de nieuwe nodes toe op de juiste manier)
---
Stap 2:
... (herhaal tot de goal node *gekozen* wordt)
```

**Specifieke Notatie per Algoritme:**

-   **BFS (Queue):** `Frontier = [A, B, C]` (nieuwe nodes achteraan)
-   **DFS (Stack):** `Stack = [C, B, A]` (nieuwe nodes vooraan)
-   **UCS (Priority Queue):** `Frontier = [A(g=5), B(g=7)]`
-   **Greedy (Priority Queue):** `Frontier = [A(h=3), B(h=6)]`
-   **A\* (Priority Queue):** `Frontier = [A(f=8), B(f=10)]` (noteer ook `g` en `h`!)
-   **Hill Climbing:**
    -   `Huidige node: A (h=5)`
    -   `Buren: B(h=3), C(h=6)`
    -   `Kies: B`

**!! BELANGRIJKE REGEL:** Een pad naar de goal is pas de oplossing als de goal-node **uit de frontier wordt gekozen**, niet wanneer deze voor het eerst wordt toegevoegd. Dit is cruciaal voor UCS en A\*.

### B. Machine Learning Hoofdlijnen Verdiept

Dit deel is conceptueler. Focus op de grote verschillen.

-   **Supervised Learning:** Leren van data met **labels** (input en correcte output zijn gekend).
    -   **Classification:** Voorspel een categorie (bv. spam/geen spam).
    -   **Regression:** Voorspel een continue waarde (bv. huisprijs).
-   **Unsupervised Learning:** Leren van data **zonder labels**.
    -   **Clustering:** Vind groepen in de data (bv. klantsegmentatie).
-   **Reinforcement Learning:** Leren door **interactie** met een omgeving en het krijgen van **beloningen** of straffen.

**Belangrijkste Algoritmes om te Kennen:**
- **Linear Regression:** (Supervised) Zoekt de best passende rechte lijn door een set datapunten om een relatie tussen variabelen te modelleren. Wordt gebruikt voor voorspellingen (bv. huizenprijs op basis van oppervlakte).
- **K-Nearest Neighbors (KNN):** (Supervised) Een eenvoudig en intuïtief algoritme. Om een nieuw datapunt te classificeren, kijkt het naar de `k` meest vergelijkbare datapunten uit de trainingsset. De nieuwe datapunten krijgen dan het label dat het meest voorkomt bij hun 'buren'.
- **K-Means:** (Unsupervised) Een clusteringsalgoritme dat probeert data op te delen in `k` groepen. Het doet dit door `k` centroïden (middelpunten) te plaatsen en elke datapunt toe te wijzen aan het dichtstbijzijnde centrum.
- **Neural Networks / Deep Learning:** Geïnspireerd op het menselijk brein. Ze leren complexe, niet-lineaire patronen via onderling verbonden lagen van 'neuronen'. CNNs (Convolutional Neural Networks) zijn een speciaal type dat uitblinkt in het herkennen van patronen in visuele data, zoals randen, vormen en objecten in afbeeldingen.

### C. Typische Examenvallen
- `BFS` is enkel optimaal als alle stapkosten gelijk zijn.
- `UCS` kiest op totale padkost (`g`), niet op het aantal stappen.
- `Greedy` is "dom" en kijkt enkel naar de heuristiek (`h`), negeert de afgelegde weg.
- `A*` combineert beide (`g+h`). Verwar het niet met Greedy.
- `Hill Climbing` is lokaal: het kan vastlopen op een "local maximum" en ziet de globale oplossing niet. Het heeft geen geheugen (frontier).

---
type: examen-samenvatting
vak: Introduction to AI
focus: algoritmes
status: actief
---

# Overzicht - Alle algoritmes

## 1. Groot plaatje

In deze module komen twee grote families van algoritmes terug:

- **Zoekalgoritmes**: zoeken een pad of oplossing in een [[State Space]].
- **Machine Learning algoritmes**: leren patronen uit data om te voorspellen of te groeperen binnen [[Machine Learning]].

Voor het examen ligt de zwaarste focus op de **zoekalgoritmes**. Daar moet je telkens kunnen uitleggen:

- welke **datastructuur** gebruikt wordt
- welke **regel** bepaalt welke node als volgende gekozen wordt
- of het algoritme **compleet** en **optimaal** is
- waarom het veel of weinig **geheugen** gebruikt
- hoe je het **stap voor stap uitschrijft** op een graaf

## Relevante conceptlinks

- AI-overzicht: [[00_Overzicht Artificial Intelligence]]
- Zoekbasis: [[Search Algorithm]], [[State Space]], [[Frontier]], [[Explored Set]], [[Path Cost]], [[Branching Factor]]
- Datastructuren: [[Queue]], [[Stack]], [[Priority Queue]]
- Heuristieken: [[Heuristic]], [[g(n)]], [[h(n)]], [[f(n)]], [[Admissible Heuristic]], [[Consistent Heuristic]]
- Zoekalgoritmes: [[Breadth-First Search (BFS)]], [[Depth-First Search (DFS)]], [[Uniform-Cost Search (UCS)]], [[Depth-Limited Search (DLS)]], [[Iterative Deepening Search (IDS)]], [[Bi-directional Search]], [[Hill Climbing]], [[Greedy Best-First Search]], [[A-star Search]], [[IDA-star (Iterative Deepening A-star)]]
- Vergelijkingen: [[Tree Search vs Graph Search]], [[BFS vs UCS]], [[Hill Climbing vs Greedy Best-First Search]], [[Admissible vs Consistent Heuristic]]
- ML-overzicht: [[00_Overzicht Machine Learning Concepten]], [[Supervised vs Unsupervised vs Reinforcement Learning]], [[Classification vs Regression]]

---

## 2. De kernvraag bij elk zoekalgoritme

Elk zoekalgoritme verschilt in feite op 1 punt:

**Hoe kiest het de volgende node uit de frontier?**

Daaruit volgen bijna alle eigenschappen.

| Algoritme | Kiest volgende node op basis van |
| :--- | :--- |
| BFS | kleinste diepte / eerst in queue |
| DFS | diepste / laatst toegevoegd |
| UCS | laagste padkost `g(n)` |
| DLS | DFS, maar met dieptelimiet |
| IDS | herhaalde DFS met grotere limiet |
| Hill Climbing | beste directe buur volgens `h(n)` |
| Greedy | laagste heuristiek `h(n)` |
| A* | laagste `f(n) = g(n) + h(n)` |
| IDA* | depth-first binnen een `f`-limiet |

---

## 3. Ongeïnformeerd zoeken

Deze algoritmes gebruiken **geen [[Heuristic]]**. Ze kijken alleen naar de structuur van de [[Graaf]] en eventueel naar de echte [[Path Cost|padkosten]].

## Breadth-First Search (BFS)

### Probleem
Hoe vind je systematisch een oplossing zonder domeinkennis, en liefst met zo weinig mogelijk stappen?

### Intuïtie
BFS zoekt **laag per laag**. Eerst alle nodes op diepte 1, dan alle nodes op diepte 2, enzovoort.

### Opbouw
- **datastructuur**: [[Queue]] (`FIFO`)
- **frontier**: bevat alle paden die nog onderzocht moeten worden in de [[Frontier]]
- vaak gecombineerd met een [[Explored Set]] bij `graph search`

### Werking
1. Zet de startnode in de queue.
2. Neem telkens het eerste element uit de queue.
3. Controleer of dit het doel is.
4. Genereer de opvolgers.
5. Zet de opvolgers achteraan in de queue.
6. Herhaal tot het doel gevonden is of de queue leeg is.

### Beslisregel
**Wie het eerst in de queue komt, wordt het eerst uitgebreid.**

### Eigenschappen
- **compleet**: ja
- **optimaal**: ja, als alle stapkosten gelijk zijn
- **sterkte**: vindt het pad met het kleinste aantal stappen
- **zwakte**: groot geheugengebruik

### Examenfocus
- schrijf telkens de **queue** uit
- BFS kijkt naar **diepte**, niet naar kost

## Depth-First Search (DFS)

### Probleem
Hoe zoek je met weinig geheugen in een grote of diepe zoekruimte?

### Intuitie
DFS kiest 1 pad en gaat **zo diep mogelijk**. Pas wanneer het vastloopt, gaat het terug en probeert het een andere tak.

### Opbouw
- **datastructuur**: [[Stack]] (`LIFO`) of recursie
- bewaart vooral het huidige pad
- backtracking is essentieel

### Werking
1. Zet de startnode op de stack.
2. Neem telkens de laatst toegevoegde node.
3. Controleer of dit het doel is.
4. Breid de node uit.
5. Zet de opvolgers bovenaan op de stack.
6. Als een pad vastloopt, ga terug.

### Beslisregel
**De laatst toegevoegde node wordt eerst uitgebreid.**

### Eigenschappen
- **compleet**: niet in het algemeen
- **optimaal**: nee
- **sterkte**: weinig geheugen nodig
- **zwakte**: kan vastlopen in lussen of een slechte diepe tak

### Examenfocus
- schrijf telkens de **stack** uit
- DFS kan snel een oplossing vinden, maar niet noodzakelijk de beste

## Uniform-Cost Search (UCS)

### Probleem
Hoe vind je het goedkoopste pad als verbindingen verschillende kosten hebben?

### Intuitie
UCS is voorzichtig: het werkt eerst alle **goedkope paden** af en breidt pas later duurdere paden uit.

### Opbouw
- **datastructuur**: [[Priority Queue]]
- prioriteit op basis van [[g(n)]]
- [[g(n)]] = echte kost van start tot node `n`

### Werking
1. Zet de startnode in de priority queue met kost `0`.
2. Neem telkens het pad met laagste `g(n)`.
3. Controleer of de eindnode het doel is.
4. Genereer opvolgers en bereken hun nieuwe cumulatieve kost.
5. Voeg die toe aan de priority queue.
6. Herhaal.

### Beslisregel
**Kies altijd het pad met de laagste totale kost `g(n)`.**

### Eigenschappen
- **compleet**: ja, als alle stapkosten positief zijn
- **optimaal**: ja
- **sterkte**: vindt het goedkoopste pad
- **zwakte**: kan veel geheugen vragen

### Examenfocus
- schrijf telkens de **priority queue** uit
- noteer expliciet `g(n)` bij elk pad
- UCS kijkt naar **kost**, niet naar diepte

## Depth-Limited Search (DLS)

### Probleem
Hoe voorkom je dat DFS eindeloos diep blijft zoeken?

### Intuitie
DLS is DFS, maar met een **harde dieptelimiet**.

### Opbouw
- gebruikt DFS-logica
- voegt een limiet `l` toe

### Werking
1. Zoek zoals DFS.
2. Zodra de diepte `l` bereikt is, stop je met uitbreiden.
3. Ga terug en probeer een andere tak.

### Beslisregel
**Zoek depth-first, maar nooit dieper dan de limiet.**

### Eigenschappen
- **compleet**: alleen als de oplossing binnen de limiet ligt
- **optimaal**: nee
- **sterkte**: voorkomt oneindig diep zoeken
- **zwakte**: verkeerde limiet kan oplossingen missen

## Iterative Deepening Search (IDS)

### Probleem
Hoe combineer je de lage geheugenkost van DFS met de volledigheid van BFS?

### Intuitie
IDS voert meerdere DFS-rondes uit met limieten `0, 1, 2, ...`.

### Opbouw
- herhaalde `DLS`
- steeds grotere dieptelimiet

### Werking
1. Voer DLS uit met limiet `0`.
2. Geen oplossing? Verhoog de limiet.
3. Herhaal tot het doel gevonden is.

### Beslisregel
**Voer DFS opnieuw uit met steeds grotere limiet.**

### Eigenschappen
- **compleet**: ja
- **optimaal**: ja, als alle stapkosten gelijk zijn
- **sterkte**: weinig geheugen, maar toch volledig
- **zwakte**: bovenste niveaus worden opnieuw bezocht

## Bi-directional Search

### Probleem
Hoe maak je een heel diepe zoekopdracht sneller?

### Intuitie
In plaats van van 1 kant te zoeken, zoek je tegelijk van **start** en van **doel** tot beide zoekfronten elkaar ontmoeten.

### Opbouw
- twee zoekprocessen
- twee frontiers
- een test om te zien of ze elkaar raken

### Werking
1. Zoek vanaf de start.
2. Zoek tegelijk vanaf het doel.
3. Breid beide frontiers uit.
4. Stop zodra er overlap is.
5. Combineer beide deelpaden.

### Beslisregel
**Werk gelijktijdig vanaf beide kanten.**

### Eigenschappen
- **sterkte**: veel sneller bij grote diepte
- **complexiteit**: ongeveer `O(b^(d/2))`
- **zwakte**: werkt alleen goed als achteruit zoeken mogelijk is

---

## 4. Geinformeerd zoeken

Deze algoritmes gebruiken een [[Heuristic]] `[[h(n)]]`: een schatting van de resterende kost tot het doel.

## Hill Climbing

### Probleem
Hoe raak je snel dichter bij het doel zonder de volledige frontier bij te houden?

### Intuitie
Hill Climbing kijkt enkel naar de **huidige node** en zijn **directe buren**. Het kiest de buur die er het best uitziet.

### Opbouw
- geen volledige frontier zoals BFS of A*
- gebruikt alleen de huidige toestand en de buurtoestanden
- gebruikt een [[Heuristic]] `[[h(n)]]`

### Werking
1. Start in de beginnode.
2. Bekijk de directe buren.
3. Kies de buur met beste heuristische waarde.
4. Ga naar die buur.
5. Herhaal tot doel of tot geen verbetering meer mogelijk is.

### Beslisregel
**Kies lokaal de beste buur volgens [[h(n)]].**

### Eigenschappen
- **compleet**: nee
- **optimaal**: nee
- **sterkte**: snel en geheugenarm
- **zwakte**: kan vastlopen in `local optimum`, `plateau` of `ridge`

### Examenfocus
- verwar dit niet met Greedy
- Hill Climbing kiest **niet uit de hele frontier**, maar enkel uit de directe buren

## Greedy Best-First Search

### Probleem
Hoe zoek je doelgericht richting doel op basis van een schatting?

### Intuitie
Greedy is "bijziend": het kiest altijd de frontier-node die **het dichtst bij het doel lijkt** te liggen.

### Opbouw
- **datastructuur**: [[Priority Queue]]
- prioriteit op basis van [[h(n)]]

### Werking
1. Zet de startnode in de frontier.
2. Neem telkens de node met kleinste `h(n)`.
3. Controleer of dit het doel is.
4. Voeg opvolgers toe met hun heuristische waarde.
5. Herhaal.

### Beslisregel
**Kies de frontier-node met laagste [[h(n)]].**

### Eigenschappen
- **compleet**: niet gegarandeerd
- **optimaal**: nee
- **sterkte**: vaak snel richting doel
- **zwakte**: kan misleid worden door een slechte heuristiek

### Examenfocus
- noteer `h(n)` expliciet
- Greedy negeert de reeds afgelegde kost `g(n)`

## A* Search

### Probleem
Hoe combineer je doelgericht zoeken met garantie op het goedkoopste pad?

### Intuitie
A* combineert het **verleden** en de **toekomst**:

- [[g(n)]] = wat het al gekost heeft
- [[h(n)]] = wat nog geschat wordt
- [[f(n)]] = `g(n) + h(n)` = totale verwachte kost

### Opbouw
- **datastructuur**: [[Priority Queue]]
- kiest op basis van [[f(n)]]

### Werking
1. Zet de startnode in de frontier.
2. Neem telkens de node met laagste `f(n)`.
3. Controleer of dit het doel is.
4. Bereken voor opvolgers hun `g`, `h` en `f`.
5. Voeg betere paden toe aan de frontier.
6. Herhaal.

### Beslisregel
**Kies de frontier-node met laagste [[f(n)]].**

### Eigenschappen
- **compleet**: ja, onder de gebruikelijke voorwaarden
- **optimaal**: ja, als [[h(n)]] [[Admissible Heuristic|admissible]] is; bij `graph search` is [[Consistent Heuristic|consistentie]] belangrijk
- **sterkte**: combineert efficiëntie en optimaliteit
- **zwakte**: kan nog steeds veel geheugen gebruiken

### Examenfocus
- noteer bij elk pad liefst `g`, `h` en `f`
- verwar A* niet met Greedy:
  - Greedy gebruikt alleen `h`
  - A* gebruikt `g + h`

## IDA* (Iterative Deepening A*)

### Probleem
Hoe combineer je de optimaliteit van A* met het lage geheugengebruik van DFS?

### Intuitie
IDA* werkt als iterative deepening, maar gebruikt geen dieptelimiet. Het gebruikt een **`f`-limiet**.

### Opbouw
- depth-first zoekproces
- limiet op basis van [[f(n)]]

### Werking
1. Start met een beginlimiet voor `f`.
2. Zoek depth-first zolang `f(n)` niet te groot wordt.
3. Overschrijdt een node de limiet, dan onthoud je de kleinste overschrijding.
4. Gebruik die als nieuwe limiet.
5. Herhaal tot het doel gevonden is.

### Beslisregel
**Zoek depth-first binnen een stijgende `f`-grens.**

### Eigenschappen
- **sterkte**: veel minder geheugen dan A*
- **zwakte**: bezoekt vaak opnieuw dezelfde knopen

---

## 5. Heuristische bouwstenen

Deze zijn geen algoritmes op zich, maar wel belangrijk voor `Hill Climbing`, `Greedy` en `A*`.

## Manhattan Distance

### Idee
De afstand is het totaal van horizontale en verticale stappen.

### Formule
`abs(r_goal - r) + abs(c_goal - c)`

### Gebruik
- ideaal voor grids waar je alleen omhoog, omlaag, links en rechts mag bewegen

## Euclidean Distance

### Idee
De rechte-lijnafstand tussen 2 punten.

### Gebruik
- geschikt wanneer fysieke of rechte afstand relevant is

## Misplaced Tiles

### Idee
Tel hoeveel tegels niet op de juiste plaats liggen.

### Gebruik
- typische heuristiek voor de sliding puzzle

## Admissible Heuristic

### Definitie
Een heuristiek is **admissible** als ze de werkelijke kost naar het doel **nooit overschat**.

### Belang
- nodig om A* optimaal te maken bij [[Tree Search vs Graph Search|tree search]]

## Consistent Heuristic

### Definitie
Een heuristiek is **consistent** als de geschatte kost niet sneller daalt dan de werkelijke stapkost toelaat.

### Belang
- nodig om A* optimaal te maken bij [[Tree Search vs Graph Search|graph search]]

---

## 6. Machine Learning algoritmes

Deze komen ook in de module voor, maar zijn voor het examen meestal minder centraal dan de zoekalgoritmes. Ze linken wel door naar duurzame concepten in `20_Wiki/Machine Learning`.

## Linear Regression

### Idee
Zoekt een lineair verband tussen input en output in [[Linear Regression]].

### Opbouw
- input: features `X`
- output: continue waarde `y`

### Werking
1. Geef trainingsvoorbeelden `(X, y)`.
2. Het model leert gewichten.
3. Daarna kan het een numerieke waarde voorspellen.

### Belangrijk
- [[Supervised Learning|supervised learning]]
- gebruikt voor [[Classification vs Regression|regressie]]

## K-Nearest Neighbors (KNN)

### Idee
Voorspel op basis van de `K` meest gelijkaardige voorbeelden in [[K-Nearest Neighbors (KNN)]].

### Opbouw
- kies `K`
- gebruik een afstandsmaat
- vergelijk met trainingsvoorbeelden

### Werking
1. Bereken de afstand tot alle trainingspunten.
2. Kies de `K` dichtste buren.
3. Laat die stemmen over de klasse, of neem hun gemiddelde.

### Belangrijk
- [[Supervised Learning|supervised learning]]
- gevoelig aan schaal van features

## K-Means

### Idee
Verdeel ongelabelde data in `K` clusters met [[K-Means]].

### Opbouw
- kies `K`
- elk cluster heeft een `centroid`

### Werking
1. Kies startcentra.
2. Wijs elk punt toe aan het dichtste centrum.
3. Herbereken de centra.
4. Herhaal tot stabiliteit.

### Belangrijk
- [[Unsupervised Learning|unsupervised learning]]
- resultaat hangt af van `K` en de startkeuze

## Artificieel Neuraal Netwerk (ANN)

### Idee
Een netwerk van neuronen leert complexe verbanden uit data in [[Neural Network]] en [[Deep Learning]].

### Opbouw
- `input layer`
- `hidden layers`
- `output layer`
- gewichten en activatiefuncties

### Werking
1. Input gaat door het netwerk.
2. Elke laag berekent nieuwe activaties.
3. De output wordt vergeleken met het juiste antwoord.
4. Tijdens training worden gewichten aangepast.

### Belangrijk
- basis van **Deep Learning**
- sterk voor complexe patroonherkenning

## Convolutional Neural Network (CNN)

### Idee
Een gespecialiseerd neuraal netwerk voor beelden in [[Convolutional Neural Network (CNN)]].

### Opbouw
- `convolutional layers`
- `pooling layers`
- daarna vaak dense lagen

### Werking
1. Filters detecteren kenmerken zoals randen en vormen.
2. Diepere lagen bouwen complexere patronen op.
3. De outputlaag beslist de klasse.

### Belangrijk
- zeer geschikt voor beeldherkenning

---

## 7. Snelle vergelijking van de zoekalgoritmes

| Algoritme | Datastructuur | Gebruikt | Compleet | Optimaal |
| :--- | :--- | :--- | :--- | :--- |
| BFS | Queue | diepte | Ja | Ja, bij gelijke kost |
| DFS | Stack | diepte-first | Nee | Nee |
| UCS | Priority queue | `g(n)` | Ja | Ja |
| DLS | Stack | diepte + limiet | Soms | Nee |
| IDS | Herhaalde DFS | oplopende limiet | Ja | Ja, bij gelijke kost |
| Hill Climbing | Lokale keuze | beste buur via `h(n)` | Nee | Nee |
| Greedy | Priority queue | `h(n)` | Niet gegarandeerd | Nee |
| A* | Priority queue | `g(n) + h(n)` | Ja | Ja, mits goede heuristiek |
| IDA* | DFS + `f`-limiet | `g(n) + h(n)` | Ja, onder voorwaarden | Ja, onder voorwaarden |

---

## 8. Examenfocus

## Wat je altijd moet kunnen
- de **frontier** stap voor stap uitschrijven
- zeggen **waarom** precies die node gekozen wordt
- het verschil uitleggen tussen `g`, `h` en `f`
- het eindpad en, waar relevant, de **totale kost** geven

## Wat je moet noteren tijdens het uitschrijven
- bij `BFS` en `DFS`: queue of stack
- bij `UCS`: `g(n)`
- bij `Greedy`: `h(n)`
- bij `A*`: `g(n)`, `h(n)` en `f(n)`
- bij gelijke waarden: je **tie-break regel** vermelden

## Klassieke verwarringen
- `BFS` vs `UCS`
  - BFS kijkt naar **aantal stappen**
  - UCS kijkt naar **totale kost**
- `Greedy` vs `A*`
  - Greedy gebruikt alleen **`h(n)`**
  - A* gebruikt **`g(n) + h(n)`**
- `Hill Climbing` vs `Greedy`
  - Hill Climbing kijkt alleen naar de **directe buren**
  - Greedy kiest uit de **volledige frontier**

## Conceptlinks
- Overzicht AI: [[00_Overzicht Artificial Intelligence]]
- Basis: [[Search Algorithm]], [[State Space]], [[Frontier]], [[Explored Set]], [[Heuristic]], [[Branching Factor]]
- Datastructuren: [[Queue]], [[Stack]], [[Priority Queue]]
- Heuristieken: [[g(n)]], [[h(n)]], [[f(n)]], [[Admissible Heuristic]], [[Consistent Heuristic]]
- Vergelijkingen: [[Tree Search vs Graph Search]], [[BFS vs UCS]], [[Hill Climbing vs Greedy Best-First Search]], [[Admissible vs Consistent Heuristic]]

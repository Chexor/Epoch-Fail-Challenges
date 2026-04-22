---
type: examen-samenvatting
vak: Introduction to AI
focus: centrale-ssot
status: actief
---

# Centrale examensamenvatting

> [!info]- Inhoudsopgave
> - [[#1. Wat lijkt het examen te testen?]]
> - [[#2. Hoofdprioriteiten voor het examen]]
> 	- [[#Prioriteit 1 - Search en heuristieken]]
> 	- [[#Prioriteit 2 - Zoekalgoritmes]]
> 	- [[#Prioriteit 3 - Machine Learning en neural nets]]
> - [[#3. Wat je van elk zoekalgoritme altijd moet kennen]]
> - [[#4. Kernoverzicht van de zoekalgoritmes]]
> - [[#5. Zoekalgoritmes die je absoluut operationeel moet kunnen uitvoeren]]
> 	- [[#Wat je op papier moet tonen]]
> 	- [[#Wat je per algoritme moet noteren]]
> 	- [[#Als je code krijgt in plaats van een graaf]]
> 	- [[#Veilige examenmethode]]
> - [[#6. Kritieke concepten die je mondeling moet kunnen uitleggen]]
> 	- [[#Search-basis]]
> 	- [[#Algoritme-eigenschappen]]
> 	- [[#Heuristieken]]
> - [[#7. Klassieke examenvallen]]
> - [[#8. Machine Learning - wat je moet kennen, maar compacter]]
> 	- [[#Extra theorie-begrippen]]
> 	- [[#Grote lijnen]]
> 	- [[#Typische probleemtypes]]
> 	- [[#Algoritmes]]
> 	- [[#Wat je mondeling moet kunnen zeggen]]
> - [[#9. Concreet studieplan]]
> 	- [[#Eerst blokkeren]]
> 	- [[#Daarna herhalen]]
> 	- [[#Daarna compact ML herhalen]]
> - [[#10. Mondelinge checklist]]
> - [[#11. Gebruik van de conceptnotes]]

> Dit is de centrale examennota voor `Introduction to AI`.
> Deze note bundelt de kern uit de oudere examendocumenten en verwijst door naar de duurzame conceptnotes in `20_Domains/`.

## 1. Wat lijkt het examen te testen?

Op basis van de officiële exameninformatie (via Teams/ANS):

**Deel 1: Theorie en Oefeningen (45 minuten, in ANS)**
- **20 Meerkeuzevragen (Theorie)** (50% van de punten) - *Tijdslimiet: 25 minuten*
- **Open vragen & Oefeningen Zoekalgoritmen** (50% van de punten) - *Tijdslimiet: 20 minuten*
  - Bestaat uit: open theorievragen (25%) + effectieve oefeningen (25%).
  - Mogelijke opdrachten: het opgeven van de Queue voor een bepaald zoekalgoritme, of het bepalen van het gevolgde zoekpad in een maze/graaf.
  - Python-kennis is *passief*: je moet een fragment Python in de context van zoekalgoritmen kunnen *interpreteren*, je hoeft zelf niet te programmeren.

**Deel 2: Mondeling (ca. 10 minuten, via Teams)**
- Korte mondelinge bespreking ter verdediging/toelichting van je antwoorden.

**Hulpmiddelen & Randvoorwaarden:**
- Open boek: alle cursusmateriaal mag gebruikt worden.
- Echter: door de harde tijdslimieten per onderdeel is uitgebreid opzoeken niet haalbaar. **Begrip + snelheid** zijn cruciaal.
- Leerstof omvat alles, inclusief de inleiding. Slides zijn de leidraad.

---

## 2. Hoofdprioriteiten voor het examen

### Prioriteit 1 - Search en heuristieken

Dit is veruit het belangrijkste deel.

Je moet zeker kennen:

- [[State Space]]
- [[Search Algorithm]]
- [[Frontier]]
- [[Explored Set]]
- [[Path Cost]]
- [[Branching Factor]]
- [[Heuristic]]
- [[g(n)]], [[h(n)]], [[f(n)]]
- [[Admissible Heuristic]]
- [[Consistent Heuristic]]

### Prioriteit 2 - Zoekalgoritmes

Je moet deze algoritmes kunnen herkennen, vergelijken, uitleggen en op papier uitvoeren:

- [[Breadth-First Search (BFS)]]
- [[Depth-First Search (DFS)]]
- [[Uniform-Cost Search (UCS)]]
- [[Depth-Limited Search (DLS)]]
- [[Iterative Deepening Search (IDS)]]
- [[Bi-directional Search]]
- [[Hill Climbing]]
- [[Greedy Best-First Search]]
- [[A-star Search]]
- [[IDA-star (Iterative Deepening A-star)]]

### Prioriteit 3 - Machine Learning en neural nets

Dit is minder operationeel dan search, maar je moet de grote lijnen kennen:

- [[Machine Learning]]
- [[Supervised Learning]]
- [[Unsupervised Learning]]
- [[Reinforcement Learning]]
- [[Classification vs Regression]]
- [[Linear Regression]]
- [[K-Nearest Neighbors (KNN)]]
- [[K-Means]]
- [[Neural Network]]
- [[Deep Learning]]
- [[Convolutional Neural Network (CNN)]]

---

## 3. Wat je van elk zoekalgoritme altijd moet kennen

Van elk algoritme moet je minstens deze 6 dingen kennen:

1. **Welke datastructuur gebruikt het?**
2. **Hoe kiest het de volgende node?**
3. **Gebruikt het diepte, kost, heuristiek of een combinatie?**
4. **Is het compleet?**
5. **Is het optimaal?**
6. **Wat is de grote sterkte en de grote zwakte?**

De kernvraag is altijd:

**Waarom kiest dit algoritme precies die node als volgende uit de frontier?**

---

## 4. Kernoverzicht van de zoekalgoritmes

| Algoritme | Datastructuur | Keuzeregel | Compleet | Optimaal |
| :--- | :--- | :--- | :--- | :--- |
| BFS | [[Queue]] | kleinste diepte | ja | ja, bij gelijke kost |
| DFS | [[Stack]] | diepste / laatst toegevoegd | nee, niet algemeen | nee |
| UCS | [[Priority Queue]] | laagste [[g(n)]] | ja | ja |
| DLS | [[Stack]] | DFS met limiet | soms | nee |
| IDS | herhaalde DFS | stijgende dieptelimiet | ja | ja, bij gelijke kost |
| Hill Climbing | lokale keuze | beste directe buur via [[h(n)]] | nee | nee |
| Greedy | [[Priority Queue]] | laagste [[h(n)]] | niet gegarandeerd | nee |
| A* | [[Priority Queue]] | laagste [[f(n)]] | ja, onder voorwaarden | ja, onder voorwaarden |
| IDA* | DFS + `f`-limiet | depth-first binnen stijgende [[f(n)]]-grens | ja, onder voorwaarden | ja, onder voorwaarden |

Klassieke vergelijkingen:

- [[BFS vs UCS]]
- [[Hill Climbing vs Greedy Best-First Search]]
- [[BFS vs DFS vs UCS vs Greedy vs A-star|BFS vs DFS vs UCS vs Greedy vs A*]]
- [[Admissible vs Consistent Heuristic]]
- [[Tree Search vs Graph Search]]

---

## 5. Zoekalgoritmes die je absoluut operationeel moet kunnen uitvoeren

Op basis van de exameninformatie moet je vooral deze heel vlot kunnen uitschrijven:

- [[Breadth-First Search (BFS)]]
- [[Depth-First Search (DFS)]]
- [[A-star Search]]
- [[Hill Climbing]]

Maar in de praktijk moet je ook klaar zijn voor:

- [[Uniform-Cost Search (UCS)]]
- [[Greedy Best-First Search]]
- [[Iterative Deepening Search (IDS)]]

### Wat je op papier moet tonen

Als je een graaf krijgt met `start`, `goal`, afstanden en eventueel heuristische waarden, dan moet je meestal:

- de **frontier** na elke stap uitschrijven
- tonen **welke node gekozen wordt**
- tonen **waarom** die gekozen wordt
- het **gevonden pad** noteren
- bij `UCS` en `A*` ook de **totale kost** geven

Gebruik hiervoor ook:

- [[10_Modules/S1 - Introduction to AI - AO/03_Examenvoorbereiding/04_Frontier correct uitschrijven op papier|04_Frontier correct uitschrijven op papier]]

### Wat je per algoritme moet noteren

- `BFS`: queue
- `DFS`: stack
- `UCS`: priority queue + `g(n)`
- `Greedy`: priority queue + `h(n)`
- `A*`: priority queue + `g(n)`, `h(n)`, `f(n)`
- `Hill Climbing`: huidige node + directe buren + beste buur

### Als je code krijgt in plaats van een graaf

Gebruik dan ook:

- [[10_Modules/S1 - Introduction to AI - AO/03_Examenvoorbereiding/03_Algoritmes herkennen aan code|03_Algoritmes herkennen aan code]]

### Veilige examenmethode

Gebruik altijd deze aanpak:

1. schrijf de **startfrontier** uit
2. expandeer exact 1 node
3. werk de frontier volledig bij
4. noteer scores (`g`, `h`, `f`) waar relevant
5. vermeld bij gelijke waarden je **tie-break regel**
6. stop pas als het doel echt gekozen wordt, niet alleen gegenereerd

---

## 6. Kritieke concepten die je mondeling moet kunnen uitleggen

### Search-basis

- wat een [[State Space]] is
- verschil tussen `state`, `initial state`, `goal state`, `operator`, `path`
- wat [[Frontier]] en [[Explored Set]] doen
- wat [[Path Cost]] betekent
- waarom [[Branching Factor]] belangrijk is

### Algoritme-eigenschappen

- **compleetheid**
- **optimaliteit**
- **tijdsefficiëntie**
- **geheugengebruik**

### Heuristieken

- wat een [[Heuristic]] is
- verschil tussen [[g(n)]], [[h(n)]], [[f(n)]]
- verschil tussen [[Admissible Heuristic]] en [[Consistent Heuristic]]
- waarom een heuristiek nuttig is
- waarom een slechte heuristiek kan misleiden

---

## 7. Klassieke examenvallen

- `BFS` is **niet altijd** optimaal; alleen bij gelijke stapkosten
- `UCS` kiest op **kost**, niet op diepte
- `Greedy` gebruikt alleen `h`, niet `g`
- `A*` gebruikt `g + h`, niet alleen `h`
- `Hill Climbing` kiest niet uit de hele frontier, maar alleen uit de directe buren
- een doelnode die al gegenereerd is, is nog niet noodzakelijk de uiteindelijke oplossing; belangrijk is **wanneer ze gekozen wordt**

---

## 8. Machine Learning - wat je moet kennen, maar compacter

Dit deel lijkt minder zwaar te wegen dan search, maar moet wel gekend zijn op conceptueel niveau.

### Extra theorie-begrippen

- **ReLU (Rectified Linear Unit):** Activatiefunctie in neurale netwerken. Regel: `f(x) = max(0, x)`. Alles onder nul wordt 0, alles erboven blijft zichzelf.
- **Heuristiek bepalen:** Grid (vakjes) = Manhattan Distance. Vluchten/Lijnen = Euclidean Distance.

### Grote lijnen

- [[Machine Learning]] = modellen leren patronen uit data
- [[Supervised Learning]] = leren met labels
- [[Unsupervised Learning]] = leren zonder labels
- [[Reinforcement Learning]] = leren via beloningen en interactie

Gebruik hiervoor ook:

- [[Supervised vs Unsupervised vs Reinforcement Learning]]
- [[Machine Learning vs Deep Learning]]

### Typische probleemtypes

- [[Classification vs Regression|classification]] = klasse voorspellen
- [[Classification vs Regression|regression]] = continue waarde voorspellen
- `clustering` = groepen zoeken in data

### Algoritmes

- [[Linear Regression]] -> supervised, regression
- [[K-Nearest Neighbors (KNN)]] -> supervised, classificatie/regressie
- [[K-Means]] -> unsupervised, clustering
- [[Neural Network]] / [[Deep Learning]] -> neurale netwerken
- [[Convolutional Neural Network (CNN)]] -> beeldherkenning

### Wat je mondeling moet kunnen zeggen

- verschil tussen supervised en unsupervised learning
- verschil tussen classification, regression en clustering
- verschil tussen [[Machine Learning]] en [[Deep Learning]]
- basisopbouw van een [[Neural Network]]
- waarom een [[Convolutional Neural Network (CNN)]] sterk is voor beelden

---

## 9. Concreet studieplan

### Eerst blokkeren

1. [[State Space]]
2. [[Search Algorithm]]
3. [[Breadth-First Search (BFS)]]
4. [[Depth-First Search (DFS)]]
5. [[Uniform-Cost Search (UCS)]]
6. [[Heuristic]], [[g(n)]], [[h(n)]], [[f(n)]]
7. [[Hill Climbing]], [[Greedy Best-First Search]], [[A-star Search]]
8. [[Admissible Heuristic]] en [[Consistent Heuristic]]
9. [[BFS vs DFS vs UCS vs Greedy vs A-star|BFS vs DFS vs UCS vs Greedy vs A*]]

### Daarna herhalen

- [[Iterative Deepening Search (IDS)]]
- [[Depth-Limited Search (DLS)]]
- [[Bi-directional Search]]
- [[IDA-star (Iterative Deepening A-star)]]

### Daarna compact ML herhalen

- [[Machine Learning]]
- [[Supervised vs Unsupervised vs Reinforcement Learning]]
- [[Classification vs Regression]]
- [[Linear Regression]]
- [[K-Nearest Neighbors (KNN)]]
- [[K-Means]]
- [[Neural Network]]
- [[Deep Learning]]
- [[Convolutional Neural Network (CNN)]]

---

## 10. Mondelinge checklist

- [ ] Ik kan uitleggen wat een [[State Space]] is.
- [ ] Ik kan het verschil uitleggen tussen [[Breadth-First Search (BFS)]] en [[Depth-First Search (DFS)]].
- [ ] Ik kan uitleggen waarom [[Uniform-Cost Search (UCS)]] verschilt van `BFS`.
- [ ] Ik kan [[g(n)]], [[h(n)]] en [[f(n)]] helder definiëren.
- [ ] Ik kan [[Greedy Best-First Search]] en [[A-star Search]] duidelijk onderscheiden.
- [ ] Ik kan [[Admissible Heuristic]] en [[Consistent Heuristic]] uitleggen.
- [ ] Ik kan een frontier stap voor stap uitschrijven op een graaf.
- [ ] Ik kan zeggen waarom [[Hill Climbing]] geen echte frontier-search is.
- [ ] Ik kan het verschil uitleggen tussen [[Supervised Learning]], [[Unsupervised Learning]] en [[Reinforcement Learning]].
- [ ] Ik kan de basis van [[Neural Network]] en [[Convolutional Neural Network (CNN)]] mondeling uitleggen.

---

## 11. Gebruik van de conceptnotes

Deze centrale note is je **examengerichte overzicht**.

Gebruik `20_Domains/` zo:

- overview nodig -> [[00_Overzicht Artificial Intelligence]] of [[00_Overzicht Machine Learning Concepten]]
- 1 algoritme herhalen -> open de specifieke topicnote
- verschil tussen 2 of 3 concepten herhalen -> open een comparison note
- formules of symbolen vergeten -> kijk naar [[g(n)]], [[h(n)]], [[f(n)]], [[Path Cost]]

De bedoeling is dus:

- **deze note kennen voor het examenoverzicht**
- **de conceptnotes gebruiken voor verdieping en actieve herhaling**

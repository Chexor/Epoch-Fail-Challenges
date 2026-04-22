---
type: examen-samenvatting
vak: Introduction to AI
focus: theorie-overzicht
status: actief
related:
  - "[[Info Examenvoorbereiding]]"
  - "[[Overzicht - Alle algoritmes]]"
  - "[[Voorbeelden - Algoritmes uitschrijven op examen]]"
---

# Uitgebreide examensamenvatting

## Groot plaatje

Deze samenvatting bundelt de theorie die je voor het examen van `Introduction to AI` moet kennen.

De kern van het vak is dat AI-systemen problemen oplossen op drie grote manieren:

- door **toestanden en problemen te representeren**
- door **te zoeken** naar oplossingen in een `state space`
- door **te leren uit data** via `machine learning` en `neural networks`

Voor het examen ligt de nadruk vooral op **zoekalgoritmes**, heuristieken en het correct kunnen verklaren waarom een algoritme een bepaald pad kiest.

## Conceptlinks

Gebruik deze conceptnotes voor duurzame verdieping buiten deze examennota:

- Overzicht AI: [[00_Overzicht Artificial Intelligence]]
- Basis: [[Artificial Intelligence (AI)]], [[State Space]], [[Search Algorithm]], [[Branching Factor]]
- Search: [[Breadth-First Search (BFS)]], [[Depth-First Search (DFS)]], [[Uniform-Cost Search (UCS)]], [[Depth-Limited Search (DLS)]], [[Iterative Deepening Search (IDS)]], [[Bi-directional Search]]
- Heuristieken: [[Heuristic]], [[Hill Climbing]], [[Greedy Best-First Search]], [[A-star Search]], [[IDA-star (Iterative Deepening A-star)]], [[Admissible Heuristic]], [[Consistent Heuristic]]
- Vergelijkingen: [[BFS vs DFS vs UCS vs Greedy vs A-star|BFS vs DFS vs UCS vs Greedy vs A*]], [[BFS vs UCS]], [[Hill Climbing vs Greedy Best-First Search]], [[Admissible vs Consistent Heuristic]]
- ML-brug: [[00_Overzicht Machine Learning Concepten]], [[Machine Learning]], [[Neural Network]], [[Deep Learning]], [[Convolutional Neural Network (CNN)]], [[K-Nearest Neighbors (KNN)]], [[K-Means]]

## Examenfocus

- Begrijp de logica achter elk zoekalgoritme.
- Ken de betekenis van `state`, `goal`, `path`, `frontier`, `queue`, `stack` en `priority queue`.
- Ken de verschillen tussen `BFS`, `DFS`, `UCS`, `Greedy`, `A*`, `Hill Climbing`, `IDS`, `DLS`, `Bi-directional Search` en `IDA*`.
- Begrijp `g(n)`, `h(n)`, `f(n)`, `admissible` en `consistent`.
- Ken de basis van `machine learning`, `deep learning`, `ANN` en `CNN`.
- Wees klaar om theorie ook mondeling uit te leggen.

## 1. Wat is AI?

### Intuïtie

Artificial Intelligence gaat over systemen die taken uitvoeren waarvoor menselijke intelligentie nodig lijkt, zoals redeneren, leren, plannen, waarnemen en beslissen.

### Formele kern

- AI probeert problemen op te lossen met computationele methodes.
- AI omvat zowel **symbolische AI** als **data-gedreven AI**.
- Symbolische AI werkt met expliciete kennis, regels en zoekprocedures.
- Data-gedreven AI leert patronen uit voorbeelden via `machine learning`.

### Examenfocus

- Ken het brede doel van AI.
- Begrijp het verschil tussen klassieke zoek-/redeneermethodes en lerende systemen.
- Verdieping: [[Artificial Intelligence (AI)]], [[Machine Learning]]

## 2. Algorithms fundamenten

### Intuïtie

Een algoritme is een systematische manier om van een beginsituatie naar een oplossing te gaan.

### Kernbegrippen

- **correctheid**: geeft het algoritme een juist antwoord?
- **tijds efficiëntie**: hoe snel werkt het?
- **geheugengebruik**: hoeveel geheugen heeft het nodig?
- **compleetheid**: vindt het een oplossing als er een bestaat?
- **optimaliteit**: vindt het de beste oplossing?

### Examenfocus

- Je moet deze eigenschappen kunnen gebruiken om algoritmes te vergelijken.
- Je moet begrijpen waarom de gekozen datastructuur het gedrag van het algoritme bepaalt.
- Verdieping: [[Search Algorithm]], [[BFS vs DFS vs UCS vs Greedy vs A-star|BFS vs DFS vs UCS vs Greedy vs A*]]

## 3. State-space representation

### Groot plaatje

Voor je een probleem kan oplossen met search, moet je het eerst modelleren als een verzameling toestanden en overgangen.

### Kernbegrippen

- **state**: een mogelijke situatie van het probleem
- **initial state**: de starttoestand
- **goal state**: de gewenste eindtoestand
- **operator / action**: een toegelaten overgang tussen toestanden
- **path**: opeenvolging van toestanden of acties
- **path cost**: totale kost van een pad
- **state space**: alle mogelijke toestanden en overgangen

### Intuitie

Een routeplanner, doolhof of puzzel kan je zien als een graaf waarin je van een startnode naar een doelnode probeert te geraken.

### Examenfocus

- Je moet problemen kunnen herkennen als `state-space`-problemen.
- Je moet begrijpen wat nodes, edges, acties en kosten voorstellen.
- Verdieping: [[State Space]], [[Graaf]], [[Branching Factor]]

## 4. Blind search

Blind search gebruikt geen extra kennis over hoe dicht een node bij het doel ligt. Het algoritme kent dus alleen:

- de starttoestand
- de mogelijke acties
- de opvolgers van een node
- eventueel de kost van een stap

Het algoritme weet **niet** welke richting waarschijnlijk beter is. Daardoor verkent het de ruimte op een algemene manier.

### Waarom is dit belangrijk?

Blind search vormt de basis waarop je bijna alle andere zoekalgoritmes begrijpt.

- `BFS` toont wat er gebeurt als je op diepte zoekt
- `DFS` toont wat er gebeurt als je op diepte van een pad focust
- `UCS` toont wat er gebeurt als kost belangrijker is dan diepte
- `IDS` en `DLS` zijn varianten die praktische problemen van DFS proberen op te lossen

### Breadth-First Search (BFS)

#### Intuitie

BFS zoekt in lagen. Het bekijkt eerst alle toestanden die je in `1` stap bereikt, dan alle toestanden op diepte `2`, daarna op diepte `3`, enzovoort.

Als je een doolhof zonder gewichten hebt, dan is BFS alsof je vanuit de start overal tegelijk een golf laat uitzetten.

#### Datastructuur

- gebruikt een `queue (FIFO)`
- wat eerst toegevoegd wordt, komt er eerst uit
- de frontier bevat dus altijd de oudste nog niet geëxpandeerde paden

#### Keuzeregel

BFS kiest altijd het pad waarvan de eindnode de **kleinste diepte** heeft.

#### Staplogica

1. Zet de startnode in de queue.
2. Neem het eerste element uit de queue.
3. Test of dit het doel is.
4. Genereer de opvolgers.
5. Zet die achteraan in de queue.
6. Herhaal tot het doel gevonden is of de queue leeg is.

#### Eigenschappen

- **compleet**: ja, als de branching factor eindig is
- **optimaal**: ja, als alle stapkosten gelijk zijn
- **sterkte**: vindt de oplossing met het kleinste aantal stappen
- **zwakte**: gebruikt veel geheugen, omdat volledige niveaus in de frontier blijven zitten

#### Typische examenvraag

Waarom is BFS optimaal bij gelijke stapkosten?

Antwoordidee: omdat BFS alle oplossingen op kleinere diepte eerst onderzoekt. De eerste gevonden oplossing is dus de oplossing met het kleinste aantal stappen.

### Depth-First Search (DFS)

#### Intuitie

DFS kiest een pad en volgt dat zo diep mogelijk. Pas als dat pad stopt of faalt, keert het terug om een andere tak te proberen.

Bij een doolhof is dit alsof je telkens een gang blijft volgen tot je niet verder kan.

#### Datastructuur

- gebruikt een `stack (LIFO)` of recursie
- de laatst toegevoegde node wordt eerst verder onderzocht

#### Keuzeregel

DFS kiest altijd de **diepste** nog niet afgewerkte node.

#### Staplogica

1. Zet de startnode op de stack.
2. Neem de bovenste node.
3. Controleer of dit het doel is.
4. Breid die node uit.
5. Zet de opvolgers bovenop de stack.
6. Ga verder tot een doel gevonden is of alle takken uitgeput zijn.

#### Eigenschappen

- **compleet**: niet in het algemeen
- **optimaal**: nee
- **sterkte**: weinig geheugen nodig
- **zwakte**: kan vastlopen in diepe of cyclische paden en kan een slechte oplossing vroeg vinden

#### Waarom gebruikt DFS weinig geheugen?

Omdat DFS vooral het huidige pad en een beperkte set alternatieven moet onthouden, niet een volledige laag zoals BFS.

#### Typische examenvraag

Waarom is DFS riskant?

Antwoordidee: omdat het heel diep in een verkeerde tak kan doorgaan en daardoor een oplossing kan missen of pas laat vinden.

### Uniform-Cost Search (UCS)

#### Intuitie

UCS kijkt niet naar het aantal stappen, maar naar de **totale kost** die je al gemaakt hebt. Het goedkoopste pad tot nu toe krijgt altijd prioriteit.

Dat is belangrijk wanneer sommige verbindingen duurder zijn dan andere.

#### Datastructuur

- gebruikt een `priority queue`
- prioriteit op basis van `g(n)`
- `g(n)` is de cumulatieve kost vanaf de startnode

#### Keuzeregel

UCS kiest altijd het frontier-pad met de **laagste huidige padkost**.

#### Staplogica

1. Start met `g(start)=0`.
2. Neem de node met laagste `g(n)` uit de priority queue.
3. Test het doel.
4. Voeg opvolgers toe met hun nieuwe cumulatieve kost.
5. Herhaal totdat een doelnode als goedkoopste gekozen wordt.

#### Eigenschappen

- **compleet**: ja, als alle stapkosten positief zijn
- **optimaal**: ja
- **sterkte**: werkt correct bij ongelijke kosten
- **zwakte**: kan traag worden en veel geheugen vragen

#### BFS versus UCS

- `BFS` kiest laagste diepte
- `UCS` kiest laagste kost
- bij gelijke stapkosten gedragen ze zich hetzelfde
- bij ongelijke stapkosten kan `UCS` een langer pad kiezen als dat goedkoper is

#### Typische examenvraag

Waarom is UCS optimaal?

Antwoordidee: omdat het altijd eerst het goedkoopste pad uitbreidt. Als een doelnode uit de priority queue komt, bestaat er geen goedkoper frontier-pad meer.

### Depth-Limited Search (DLS)

#### Intuitie

DLS is DFS met een veiligheidsrem. Je laat het algoritme maar tot een bepaalde diepte zoeken.

#### Waarom bestaat DLS?

Gewone DFS kan oneindig diep blijven zoeken. DLS voorkomt dat door een harde limiet `l` in te stellen.

#### Eigenschappen

- werkt zoals DFS
- stopt met uitbreiden zodra de limiet bereikt is
- nuttig als je weet dat een oplossing waarschijnlijk niet te diep zit
- niet volledig als de echte oplossing dieper ligt dan de limiet

#### Exameninzicht

DLS lost het oneindig-diep-probleem van DFS op, maar introduceert een nieuw risico: een te lage limiet kan de oplossing afsnijden.

### Iterative Deepening Search (IDS)

#### Intuitie

IDS voert meerdere keren een depth-limited search uit:

- eerst limiet `0`
- dan limiet `1`
- dan limiet `2`
- enzovoort

Zo krijg je de geheugenvoordelen van DFS, maar toch de zekerheid dat je de ondiepste oplossing zal vinden.

#### Waarom werkt dit goed?

In een boom zitten de meeste nodes typisch op de diepste niveaus. Het opnieuw bezoeken van de bovenste niveaus kost daardoor minder dan je intuItief zou denken.

#### Eigenschappen

- **compleet**: ja
- **optimaal**: ja, bij gelijke stapkosten
- **sterkte**: weinig geheugen, toch veilig
- **zwakte**: bezoekt de bovenste delen van de boom meerdere keren opnieuw

#### IDS versus DFS

- beide gebruiken weinig geheugen
- `DFS` kan blijven hangen in een verkeerde tak
- `IDS` zal systematisch diepere niveaus bereiken en is daardoor betrouwbaarder

### Bi-directional Search

#### Intuitie

In plaats van helemaal van start naar doel te zoeken, laat je twee zoekprocessen naar elkaar toe werken:

- een vanaf de start
- een vanaf het doel

Ze proberen elkaar in het midden te ontmoeten.

#### Waarom is dit sneller?

Als een oplossing diepte `d` heeft, dan moet gewone search vaak ongeveer tot `d` zoeken. Bi-directional search splitst dat ruwweg in twee stukken van lengte `d/2`.

Dat geeft een grote winst bij grote branching factor.

#### Beperkingen

- je moet het doel expliciet kennen
- je moet achterwaarts kunnen zoeken
- je moet kunnen detecteren wanneer beide frontiers elkaar raken

### Examenfocus

- Ken van elk algoritme: datastructuur, keuzecriterium, compleetheid, optimaliteit, tijd en geheugen.
- Begrijp vooral deze verschillen:
  - `BFS` kiest op diepte
  - `DFS` kiest op diepte van het huidige pad
  - `UCS` kiest op kost
  - `IDS` is DFS in rondes met stijgende limiet
- Typische mondelinge vraag: waarom zou je `BFS` verkiezen boven `DFS`, of `UCS` boven `BFS`?

## 5. Heuristic search

Heuristic search gebruikt extra kennis om gerichter naar het doel te zoeken. In plaats van blind alle opties af te lopen, gebruikt het algoritme een schatting om betere keuzes te maken.

### Waarom is een heuristiek nuttig?

In veel problemen is de zoekruimte enorm. Zonder extra sturing moet een algoritme heel veel nodes verkennen.

Een heuristiek helpt om sneller te beslissen:

- welke node waarschijnlijk veelbelovend is
- welke paden je beter eerst onderzoekt
- welke opties minder kans maken om snel tot een oplossing te leiden

### Heuristiek

Een `heuristiek` is een schatting van hoe ver een toestand nog van het doel verwijderd is.

- `g(n)`: echte kost van start tot node `n`
- `h(n)`: geschatte resterende kost van `n` tot het doel
- `f(n) = g(n) + h(n)`

### Hill Climbing

#### Intuitie

Hill Climbing kijkt alleen naar de huidige toestand en haar directe buren. Daarna kiest het de buur die er het best uitziet volgens de heuristiek.

Het denkt dus **lokaal**, niet globaal.

#### Keuzeregel

- vergelijk de buurtoestanden
- kies de buur met de beste heuristische waarde
- vervang de huidige node door die buur

#### Eigenschappen

- gebruikt geen volledige frontier
- snel en simpel
- niet compleet
- niet optimaal

#### Typische problemen

- `local optimum`: een toestand die beter is dan de buren, maar niet de globale beste oplossing
- `plateau`: meerdere buren met dezelfde waarde, zodat er geen duidelijke richting is
- `ridge`: een situatie waarin de beste globale richting niet via een directe beste buur zichtbaar is

#### Exameninzicht

Hill Climbing is geen volledig zoekalgoritme zoals BFS of A*. Het is vooral een lokale optimalisatietechniek.

### Greedy Best-First Search

#### Intuitie

Greedy Search kiest altijd de node die volgens de heuristiek het dichtst bij het doel lijkt.

Het idee is: "ga zo snel mogelijk in de richting van het doel".

#### Datastructuur

- gebruikt een `priority queue`
- sorteert op `h(n)`

#### Keuzeregel

Kies de frontier-node met de **laagste heuristische waarde**.

#### Eigenschappen

- kijkt alleen naar `h(n)`
- negeert de kost die al gemaakt is
- vaak snel in de praktijk
- niet optimaal
- niet betrouwbaar compleet in het algemeen

#### Waarom kan Greedy fout zitten?

Omdat een node er heuristisch dichtbij kan uitzien, maar via een duur of slecht pad bereikbaar is. Greedy laat zich dus misleiden als `h(n)` alleen geen goed totaalbeeld geeft.

### A* Search

#### Intuitie

A* probeert het beste van twee werelden te combineren:

- wat het al gekost heeft om hier te geraken
- wat het nog ongeveer zal kosten om het doel te bereiken

Het kiest dus niet de goedkoopste node **tot nu toe** en ook niet gewoon de node die **het dichtst lijkt**, maar de node met de beste totale schatting.

#### Datastructuur

- gebruikt een `priority queue`
- sorteert op `f(n) = g(n) + h(n)`

#### Keuzeregel

Kies de frontier-node met de laagste `f(n)`.

#### Waarom is A* zo sterk?

- `g(n)` voorkomt dat je al gemaakte kost negeert
- `h(n)` helpt om gericht te zoeken
- samen geven ze een evenwicht tussen voorzichtigheid en snelheid

#### Eigenschappen

- compleet onder de gebruikelijke voorwaarden
- optimaal als de heuristiek `admissible` is
- bij `graph search` is `consistentie` extra belangrijk
- meestal veel efficiënter dan blind search als de heuristiek goed is
- kan nog altijd veel geheugen gebruiken

#### Greedy versus A*

- `Greedy`: kiest laagste `h(n)`
- `A*`: kiest laagste `g(n) + h(n)`
- `Greedy` denkt vooral aan "dicht bij doel"
- `A*` denkt aan "goed totaal pad"

Dit is een van de belangrijkste theoretische vergelijkingen voor het examen.

### IDA*

#### Intuitie

IDA* wil de kwaliteit van A* behouden, maar zonder de zware geheugenlast van een grote priority queue.

#### Werking in grote lijnen

- gebruik een grens op `f(n)` in plaats van op diepte
- voer een depth-first zoekproces uit binnen die `f`-grens
- als de grens overschreden wordt, verhoog je ze naar de kleinste te hoge `f` die je tegenkwam

#### Eigenschappen

- veel minder geheugen dan A*
- herhaalt stukken van de zoekboom vaker
- interessant wanneer geheugen de beperkende factor is

### Examenfocus

- Verwar `Hill Climbing`, `Greedy` en `A*` niet.
- `Hill Climbing` kiest lokaal de beste buur.
- `Greedy` kiest in de frontier de laagste `h(n)`.
- `A*` kiest in de frontier de laagste `g(n) + h(n)`.
- Begrijp waarom een goede heuristiek de zoekruimte kleiner maakt.
- Begrijp ook waarom een slechte heuristiek een algoritme kan misleiden.

## 6. Eigenschappen van heuristieken

### Admissible heuristic

Een heuristiek is `admissible` als ze de echte resterende kost nooit overschat.

Belang:

- nodig om de optimaliteit van A* te garanderen

### Consistent heuristic

Een heuristiek is `consistent` als de geschatte kost zich gedraagt volgens de driehoeksvoorwaarde.

Intuitief:

- de heuristische waarde mag niet sneller dalen dan de werkelijke stapkost toelaat

Belang:

- vooral belangrijk bij `graph search`
- zorgt ervoor dat A* nodes niet op een problematische manier moet heropenen

### Voorbeelden van heuristieken

- `Manhattan distance`
- `Euclidean distance`
- `Misplaced tiles`

### Examenfocus

- Ken het verschil tussen `admissible` en `consistent`.
- Begrijp waarom deze eigenschappen belangrijk zijn voor A*.

## 7. Vergelijking van zoekalgoritmes

### Wat je altijd moet kunnen vergelijken

- waarop het algoritme kiest
- welke datastructuur het gebruikt
- of het compleet is
- of het optimaal is
- of het veel tijd kost
- of het veel geheugen gebruikt

### Klassieke vergelijkingen

- `BFS` vs `DFS`: breed versus diep, veel geheugen versus weinig geheugen
- `BFS` vs `UCS`: diepte versus kost
- `Greedy` vs `A*`: alleen schatting versus kost + schatting
- `DFS` vs `IDS`: weinig geheugen in beide, maar IDS is veiliger

### Examenfocus

- Dit soort vergelijkingen zijn typische open vragen.
- Je moet niet alleen weten *wat* het antwoord is, maar ook *waarom*.

## 8. Machine learning

### Groot plaatje

Machine learning laat systemen patronen leren uit data in plaats van alles expliciet te programmeren.

### Basisbegrippen

- **training data**: voorbeelden waarmee het model leert
- **features**: invoervariabelen
- **label**: juist antwoord bij supervised learning
- **prediction**: voorspelling van het model

### Belangrijke types

- **supervised learning**: leren met input-outputvoorbeelden
- **unsupervised learning**: leren zonder labels
- **regression**: continue waarde voorspellen
- **classification**: klasse voorspellen
- **clustering**: data groeperen

### Examenfocus

- Ken het verschil tussen supervised en unsupervised learning.
- Ken het verschil tussen classification, regression en clustering.

## 9. Belangrijke ML-algoritmes

### Linear Regression

- supervised learning
- voorspelt een continue waarde
- zoekt een lineair verband tussen input en output

### K-Nearest Neighbors (KNN)

- supervised learning
- gebruikt de `K` dichtste voorbeelden
- gevoelig aan schaal en afstandsmaat

### K-Means

- unsupervised learning
- verdeelt data in `K` clusters
- gebruikt `centroids`
- resultaat hangt af van startpositie en keuze van `K`

### Examenfocus

- Ken per algoritme het doel en het type learning.
- Weet welk algoritme hoort bij regressie, classificatie of clustering.

## 10. Neural networks en deep learning

### Artificial Neural Network (ANN)

Een `ANN` bestaat uit lagen van neuronen die samen complexe patronen leren.

#### Opbouw

- `input layer`
- een of meer `hidden layers`
- `output layer`
- gewichten op verbindingen
- activatiefuncties

#### Basisidee van training

- input gaat door het netwerk naar voor
- output wordt vergeleken met het juiste antwoord
- gewichten worden aangepast om fouten te verkleinen

### Deep learning

Van `deep learning` spreken we wanneer een neuraal netwerk meerdere hidden layers heeft.

### Convolutional Neural Network (CNN)

- gespecialiseerd voor beelden
- gebruikt `convolutional layers`
- gebruikt vaak `pooling`
- bouwt van simpele naar complexe patroonherkenning

### Examenfocus

- Ken de basisstructuur van een neuraal netwerk.
- Begrijp waarom `CNNs` sterk zijn voor beeldherkenning.
- Je hoeft dit meestal minder operationeel uit te schrijven dan zoekalgoritmes, maar je moet het wel helder kunnen uitleggen.

## 11. Python en tools

### Wat je globaal moet kennen

- `NumPy`: numerieke arrays en matrixbewerkingen
- `Pandas`: werken met tabellen en datasets
- `Scikit-learn`: klassieke machine learning algoritmes
- `Keras`: bouwen en trainen van neurale netwerken

### Examenfocus

- Vooral begrijpen waarvoor deze tools gebruikt worden.
- Minder focus op detailsyntax, meer op hun rol in AI-praktijk.

## 12. Mondelinge theorie die je vlot moet kunnen zeggen

- Waarom `BFS` optimaal is bij gelijke stapkosten.
- Waarom `DFS` weinig geheugen gebruikt maar riskant is.
- Waarom `UCS` verschilt van `BFS`.
- Waarom `Greedy` snel kan zijn maar niet optimaal.
- Waarom `A*` sterker is dan `Greedy`.
- Wat een heuristiek precies doet.
- Wat `admissible` en `consistent` betekenen.
- Verschil tussen `supervised` en `unsupervised learning`.
- Verschil tussen `ANN` en `CNN`.

## 13. Prioriteiten voor blokken

### Prioriteit 1

- `state-space representation`
- `blind search`
- `heuristic search`
- vergelijkingen tussen zoekalgoritmes
- heuristieken en hun eigenschappen

### Prioriteit 2

- basis AI-begrippen
- machine learning fundamenten
- neural networks en CNN

### Prioriteit 3

- Python-tools en toepassingscontext

## 14. Checklist

- [ ] Ik kan uitleggen wat een `state space` is.
- [ ] Ik kan `BFS`, `DFS` en `UCS` theoretisch vergelijken.
- [ ] Ik kan uitleggen wat `g(n)`, `h(n)` en `f(n)` zijn.
- [ ] Ik kan `Greedy` en `A*` duidelijk onderscheiden.
- [ ] Ik kan `admissible` en `consistent` uitleggen.
- [ ] Ik ken het verschil tussen `supervised`, `unsupervised`, `classification`, `regression` en `clustering`.
- [ ] Ik kan de basis van `ANN` en `CNN` uitleggen.
- [ ] Ik kan deze theorie ook mondeling kort en helder verwoorden.

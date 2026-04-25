# Examenvragen - uitgeschreven

Bron: transcriptie van de screenshots uit `Examenvragen.md`.

## Deel 1: Keuzevragen

### 1. Point of singularity
- [ ] Het punt waarop AI volledig autonoom opereert binnen een enkel domein zoals schaken of Go.
- [x] Het punt waarop AI-systemen even intelligent worden beschouwd als de mens.
- [ ] Het moment waarop een AI-systeem voor het eerst een menselijke taal volledig begrijpt en reproduceert.
- [ ] Het moment waarop een AI-systeem voor het eerst een menselijke taal volledig begrijpt en reproduceert.

### 2. Algemeen - Wat is het doel van de Turing test?
- [ ] Om te zien of een computer in staat is om de intentie van menselijke taal correct te analyseren.
- [ ] Om na te gaan of een robot fysiek menselijk gedrag kan nabootsen.
- [ ] Om te bepalen of een machine logisch kan redeneren.
- [x] Om te testen of een machine een conversatie kan voeren zonder dat de gesprekspartner weet dat het geen mens is.

### 3. Algemeen - Gegeven de volgende uitspraken
A. Sommige neurale netwerken zijn expertsystemen

B. We spreken van Deep Learning wanneer een neuraal netwerk langdurig getraind wordt op veel data.

Wat kun je besluiten over volgende uitspraken?
- [ ] Alleen A is waar
- [ ] A en B zijn beide waar
- [x] A en B zijn beide onwaar
- [ ] Alleen B is waar

### 4. Machine learning - Wat is de rol van een centroide in het k-means clustering algoritme?
- [x] Het is het gemiddelde punt van alle data-items in een cluster en bepaalt de nieuwe positie van het clustercentrum.
- [ ] Het is het punt dat willekeurig wordt gekozen om het algoritme te beeindigen.
- [ ] Het is het punt in de dataset dat het dichtst bij het oorsprong ligt.
- [ ] Het is het datapunt met de hoogste waarde in het cluster.

### 5. Machine learning - Welke van de volgende stappen hoort niet thuis in het standaard k-means algoritme?
- [ ] Toewijzen van elk datapunt aan de dichtstbijzijnde centroide
- [ ] Herberekenen van de centroiden als het gemiddelde van de toegewezen punten
- [ ] Willekeurig initialiseren van k centroiden
- [x] Backpropagation gebruiken om de fouten te minimaliseren

### 6. Machine learning - Wat is het doel van backpropagation in een neuraal netwerk?
- [ ] Het normaliseren van de inputdata door bias toe te voegen
- [ ] Het achteraf opslaan van aangepaste data in het geheugen na elke epoch
- [ ] Het bepalen van het aantal benodigde verborgen lagen
- [x] Het trainen van het netwerk door gewichten aan te passen op basis van de fout

### 7. Machine learning - Welke uitspraak is correct?
- [ ] Een algoritme is het eindproduct dat voorspellingen doet; een model is de methode om het algoritme te trainen.
- [ ] Een model is een verzameling van trainingsdata; een algoritme is de formule die voorspellingen maakt.
- [x] Een algoritme is het leerproces dat gebruikt wordt om op basis van data een model te bouwen; het model is het getrainde resultaat dat voorspellingen kan doen.
- [ ] Een model bepaalt de keuze van het algoritme in supervised learning; het algoritme is slechts een opslagstructuur voor parameters.

### 8. Topic 2 - Welk machine learning model heeft de hoogste interpreteerbaarheid?
- [x] decision tree ✅ 2026-03-28
- [ ] clustering model
- [ ] regressie model
- [ ] neuraal netwerk

### 9. State-space representation
Je ontwerpt een AI-agent om het probleem van de 8-puzzle op te lossen. Hierbij stel je elke mogelijke configuratie van de puzzel (plaatsing van de tegels) voor als een toestand. De agent kan van een ene toestand naar de volgende gaan door een tegel te schuiven.

Welk van onderstaande antwoorden geeft best aan wat de state-space representatie is in deze context?
- [ ] De visuele weergave van het bord op een scherm.
- [ ] Voorstellingen van de mogelijke toestanden en de spelregels
- [x] Een lijst van alle mogelijke zetten die je in de puzzel kunt maken.
- [ ] Een verzameling regels om te bepalen welke tegel je moet schuiven.

### 10. State-space representation - Wat kun je niet met production rules?
- [ ] berekenen welke zetten mogelijk zijn in een bepaalde situatie
- [x] leren efficient een pad te vinden naar de oplossing
- [ ] de branching factor inschatten
- [ ] de zoekboom opstellen, gegeven een startsituatie

### 11. Supervised - unsupervised - Welke uitspraak is correct?
- [ ] Supervised learning kan alleen gebruikt worden voor tekstdata, unsupervised voor getallen.
- [ ] Supervised learning maakt gebruik van neurale netwerken, unsupervised learning niet.
- [x] Sommige unsupervised algoritmen vereisen vooraf een keuze van het aantal groepen, wat subjectieve keuzes inhoudt.
- [ ] Unsupervised learning kan geen nieuwe informatie opleveren, enkel herhalen wat in de data zit.

### 12. Neurale Netwerken: Bereken de output (v1)
Gegeven: bovenstaand eenvoudig neuraal netwerk. De activatiefunctie is de ReLU in elke node van de Hidden layer.

Hoeveel is de output?

Antwoord ingevuld: `8`

### 13. Neurale netwerken - Wat is niet van toepassing voor neurale netwerken?
- [ ] De feature-extractie gebeurt automatisch
- [ ] De neuronen in alle hidden layers kunnen elk een eigen bias hebben
- [ ] Een activatiefunctie is een niet-lineaire functie
- [x] Enkel bij elke input kan een bias meegegeven worden

### 14. Neurale netwerken - overfitting - Welke uitspraak over overfitting is correct?
- [x] Overfitting wordt gekenmerkt door hoge nauwkeurigheid op de trainingsdata en lage nauwkeurigheid op de testdata
- [ ] Overfitting kan verminderen wanneer het model meer parameters bevat, omdat het dan beter kan generaliseren.
- [ ] Overfitting treedt op wanneer het model te veel bias heeft en daardoor de trainingsdata slecht benadert.
- [ ] Overfitting betekent dat het model niet in staat is om de trainingsdata correct te voorspellen en altijd overschat.

### 15. Zoekalgoritmen - Wat kun je stellen over de snelheid/rekentijd van diepte-eerst en breedte-eerst
- [ ] Over het algemeen is breedte-eerst trager dan diepte-eerst, maar de effectieve snelheid van een algoritme hangt van de zoekboom af
- [ ] Breedte-eerst is altijd sneller dan diepte-eerst
- [x] Over het algemeen is diepte-eerst trager dan breedte-eerst, maar de effectieve snelheid van een algoritme hangt van de zoekboom af
- [ ] Diepte-eerst is altijd sneller dan breedte-eerst

### 16. Zoekalgoritmen
Stel je hebt een zoekalgoritme dat werkt op een oneindige zoekruimte met mogelijke oplossingen. Onder welke voorwaarde kan dit algoritme als compleet worden beschouwd?
- [ ] Het garandeert het vinden van een optimale oplossing, zelfs als de zoekruimte oneindig is.
- [ ] Het bezoekt de complete boom, dus alle knopen, zelfs al vond het eerder een oplossing, om zeker ook het optimale pad te kunnen vinden
- [ ] Het maakt gebruik van heuristieken die altijd de exacte afstand tot het doel berekenen.
- [x] Het vindt gegarandeerd een oplossing als er ten minste een bestaat en als het algoritme niet vastloopt in oneindige paden.

### 17. Zoekalgoritmen
Met efficient in de volgende vraag bedoelen we zowel rekentijd als geheugengebruik.

Welke uitspraak over A* is de juiste?
- [x] A* is belangrijk om efficienter het kortste pad naar de doelnode te vinden
- [ ] A* is belangrijk om met zekerheid het kortste pad naar de doelnode te kunnen vinden.
- [ ] A* verschilt niet veel met estimate-extended uniform cost en dus is de impact bij uitvoering eerder beperkt.
- [ ] A* is belangrijk om efficienter de doelnode te vinden.

### 18. Zoekalgoritmes zijn ALTIJD compleet? (meerdere antwoorden mogelijk)
- [ ] Diepte-eerst
- [x] Breedte-eerst
- [x] Iterative deepening
- [ ] Non-deterministic search

### 19. Zoekalgoritmen - Een zoekalgoritme is compleet als
- [x] het eindigt als er een oplossing bestaat
- [ ] het een lus (loop) bevat
- [ ] het start met een oplossing
- [ ] het alle oplossingen in de zoekboom vindt

### 20. Zoekalgoritmen - Wat is waar ivm de sortering van de queue bij Greedy Search?
- [x] Alle nieuwe knopen worden gesorteerd op hun heuristische waarde
- [ ] De nieuwe knopen worden gesorteerd op hun totale pakkosten
- [ ] Alle knopen worden gesorteerd op hun totale padkosten,
- [ ] Alle knopen worden gesorteerd op hun heuristische waarde

## Deel 2: Open vragen

### 1. Oefening zoekalgoritmen

In het zwart: de kost (afstand) tussen buren, in het rood: afstand in vogelvlucht tot Hasselt.

Ik wil reizen van Roeselare naar Hasselt.

We gebruiken onderstaande zoekalgoritmes om deze reis te maken.

Voer telkens het algoritme strikt uit en hou geen rekening met of iets in de realiteit ook op die manier zou kunnen via de weg of het spoor tussen de steden.
Hou ook rekening met het juiste stopcriterium.

Kies, indien relevant voor een algoritme, een bij deze context passende heuristische functie.
Indien de volgorde relevant is (cfr links naar rechts), kiezen we hier de alfabetische volgorde.

Geef hieronder elke toestand van de QUEUE weer vanaf de start in Hasselt

Elke nieuwe toestand van de volledige queue komt telkens op een nieuwe lijn. Gebruik van elke stad de eerste letter en gebruik als scheidingsteken een spatie, bijvoorbeeld:

```text
H
HL
HLA HLG HLB ...
... enz...
```

#### 1a. Geef hieronder de queue weer met Breadth First Search

Ingevuld antwoord:

```text
H
L
A B G
B G O
G O
O A B L R
A B L R
B L R
L R
R
```

#### 1b. Geef hieronder de queue weer met Hill Climbing

Ingevuld antwoord:

```text
H
L
B
G
R
```

#### 1c. Geef hieronder de queue weer met A*

Ingevuld antwoord:

```text
R
G O
B A L O
A L O
L O
H O
H
```

### 2. Vergelijking zoekalgoritmen
Bespreek de voor- en nadelen van Greedy Search t.o.v. Uniform Cost.

Bespreek de voor- en nadelen van Iterative Deepening t.o.v. Breadth First Search.

Behandel hierbij ook de criteria die in de cursus besproken worden.

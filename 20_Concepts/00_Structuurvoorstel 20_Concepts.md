---
related:
  - 00_Overzicht Concepten
  - 00_Voorstel Eerste Bases
type: concept-map
domain: "concept-root"
theme: "concept-vault-structure"
aliases:
  - Structuurvoorstel voor 20_Concepts
---

# Structuurvoorstel voor 20_Concepts

## Doel

- `10_Modules/` blijft cursus- en semestergebonden
- `20_Concepts/` blijft de duurzame, vakoverschrijdende kennisbank
- concepten worden geordend op **kennisdomein**, niet op cursusnaam
- de structuur moet **stabiel, schaalbaar en onderhoudbaar** blijven
- Obsidian moet zowel **didactisch** als **operationeel** goed bruikbaar zijn

---

## Huidige realiteit

De huidige `20_Concepts/`-structuur is vandaag:

```text
20_Concepts/
├─ Artificial Intelligence/
├─ Computer Science/
├─ Discrete Mathematics/
├─ Graph Theory/
├─ Linear Algebra/
├─ Machine Learning/
├─ Software Design Principles/
├─ Statistics/
├─ Concepts-canvas.canvas
└─ 00_Structuurvoorstel 20_Concepts.md
```

Deze structuur werkt al redelijk goed, maar bevat nog enkele historische inconsistenties:

- sommige mappen zijn duidelijke **kennisdomeinen** (`Machine Learning`, `Statistics`)
- andere zijn eerder **subdomeinen** (`Graph Theory`)
- andere zijn **thematische verzamelmappen** (`Software Design Principles`)
- de ooit bedachte superstructuur met `Mathematics/` en `Data & AI/` is inhoudelijk logisch, maar nog niet geïmplementeerd

Conclusie: dit document moet geen theoretisch eindbeeld meer zijn, maar een **realistisch werkdocument voor de huidige vault**.

---

## Aanbevolen richting

### Kernprincipe

Behoud voorlopig de huidige domeinmappen, en migreer alleen waar de winst duidelijk is.

Dat betekent:

- **geen big-bang herstructurering**
- wel stelselmatig inconsistenties wegwerken
- domeinmappen behouden als stabiele inhoudelijke thuisbasis
- `Maps` gebruiken als didactische navigatie
- `Bases` gebruiken als dynamische indexlaag

### Praktische doelstructuur op korte termijn

```text
20_Concepts/
├─ Artificial Intelligence/
│  ├─ Maps/
│  ├─ Topics/
│  ├─ Comparisons/
│  └─ Execution/
├─ Machine Learning/
│  ├─ Maps/
│  ├─ Topics/
│  ├─ Comparisons/
│  └─ Execution/
├─ Computer Science/
│  ├─ Maps/
│  ├─ Topics/
│  ├─ Comparisons/
│  └─ Execution/
├─ Discrete Mathematics/
│  ├─ Maps/
│  ├─ Topics/
│  ├─ Comparisons/
│  └─ Execution/
├─ Linear Algebra/
│  ├─ Maps/
│  ├─ Topics/
│  ├─ Comparisons/
│  └─ Execution/
├─ Statistics/
│  ├─ Maps/
│  ├─ Topics/
│  ├─ Comparisons/
│  └─ Execution/
├─ Graph Theory/
│  ├─ Maps/
│  ├─ Topics/
│  ├─ Comparisons/
│  └─ Execution/
└─ Software Design Principles/
   ├─ Maps/
   ├─ Topics/
   ├─ Comparisons/
   └─ Execution/
```

Dit sluit aan op wat nu effectief bestaat en vraagt geen zware herbouw.

---

## Waarom deze richting beter is dan het oude voorstel?

Het oude voorstel met `Mathematics/`, `Data & AI/` en `Interdisciplinary/` is inhoudelijk logisch, maar momenteel te groot als migratiestap.

De nadelen daarvan zijn:

- veel padwijzigingen in 1 keer
- veel backlinks die mee aangepast moeten worden
- meer risico op tijdelijke chaos in Obsidian
- weinig directe winst zolang de huidige domeinen al goed werken

De huidige richting is beter omdat ze:

- aansluit op de **echte vault**
- kleine, veilige migraties mogelijk maakt
- domeinen herkenbaar houdt
- future-proof blijft voor latere verfijning
- goed combineert met een extra indexlaag via **Obsidian Bases**

---

## Plaatsingsregels

### Artificial Intelligence

Voor search, heuristieken, state spaces en klassieke AI-probleemvoorstellingen.

Voorbeelden:
- `Breadth-First Search (BFS)`
- `A* Search`
- `Heuristiek`
- `State Space`

### Machine Learning

Voor modellen die leren uit data, leerparadigma's, evaluatie, training en deep-learninggerelateerde concepten.

Voorbeelden:
- `Linear Regression`
- `Gradient Descent`
- `MSE`
- `Keras`
- `Deep Learning`

### Computer Science

Voor programmeer-, datatype-, systeem- en abstracte informaticaconcepten.

Voorbeelden:
- `uint8`
- `float32`
- `Priority Queue`
- `Stack`

### Discrete Mathematics

Voor getaltheorie, modulorekenen, recursies en discrete rekenprocedures.

Voorbeelden:
- `Modulorekenen`
- `Euler phi-functie`
- `Modulaire inverse`
- `Staartdeling (Long Division)`

### Linear Algebra

Voor matrices, determinant, inverses en rijoperaties.

### Statistics

Voor beschrijvende statistiek, verdelingen en standaardmaten.

### Graph Theory

Voor puur grafentheoretische concepten.

Voorbeelden:
- `Graaf`
- `Verbindingsmatrix`
- `Padlengte via Matrixmachten`

### Software Design Principles

Voor ontwerpprincipes zoals `SOLID`.

Opmerking:
- inhoudelijk zou dit op termijn onder `Computer Science/` kunnen vallen
- voorlopig mag deze map blijven bestaan zolang de structuur intern consistent is

---

## Concrete evaluatie van huidige mappen

### Goed zoals het nu is

- `Artificial Intelligence/`
- `Machine Learning/`
- `Linear Algebra/`
- `Statistics/`
- `Discrete Mathematics/`

Deze mappen zijn duidelijk, herkenbaar en al functioneel opgebouwd met `Maps`, `Topics`, `Comparisons` en `Execution`.

### Mag voorlopig blijven, maar vraagt later heroverweging

- `Graph Theory/`
  - inhoudelijk grenst dit aan `Discrete Mathematics`
  - voorlopig apart houden is verdedigbaar zolang het domein voldoende inhoud krijgt
- `Software Design Principles/`
  - inhoudelijk eerder een subdomein van `Computer Science`
  - naam is bruikbaar, maar minder algemeen schaalbaar

### Reeds uitgevoerde correcte plaatsingen

- `Staartdeling (Long Division)` is verhuisd naar `Discrete Mathematics/Topics/`
- AI- en ML-domeinen zijn verder uitgebouwd met `Maps`, `Topics`, `Comparisons` en `Execution`

---

## Mapping van huidige mappen naar aanbevolen status

- `Artificial Intelligence/` -> behouden
- `Machine Learning/` -> behouden
- `Computer Science/` -> behouden
- `Discrete Mathematics/` -> behouden
- `Linear Algebra/` -> behouden
- `Statistics/` -> behouden
- `Graph Theory/` -> voorlopig behouden, later evalueren voor merge met `Discrete Mathematics/`
- `Software Design Principles/` -> voorlopig behouden, later evalueren voor opname in `Computer Science/`

---

## Concrete plaatsing van types notes

### Topic notes

Gebruik `Topics/` voor echte kernconcepten.

Voorbeelden:
- `Machine Learning`
- `A* Search`
- `Queue`
- `Modulorekenen`

### Comparison notes

Gebruik `Comparisons/` voor notities met expliciet vergelijkingsdoel.

Voorbeelden:
- `Machine Learning vs Deep Learning`
- `BFS vs UCS`
- `Admissible vs Consistent Heuristic`

Regel:
- als een note hoofdzakelijk het onderscheid tussen meerdere concepten uitlegt, hoort die in `Comparisons/`

### Execution notes

Gebruik `Execution/` voor worked examples, procedures en uitgewerkte toepassingen.

Voorbeelden:
- `Gradient Descent Worked Example`
- `Gauss-Jordan Worked Example`
- `BFS Worked Example`

### Maps

Gebruik `Maps/` voor overzichtsnotes en navigatiehubs.

Voorbeelden:
- `00_Overzicht Artificial Intelligence`
- `00_Overzicht Machine Learning Concepten`

---

## Nieuwe standaard voor conceptnotes

Een `Topic`-note volgt idealiter deze structuur:

1. titel + tags
2. 1 korte openingszin direct onder de titel
3. `Korte kern`
4. `Wat is het kernprobleem?`
5. `Intuitieve uitleg`
6. `Formele structuur`
7. `Snelle vergelijking` (optioneel)
8. `Toepassing`
9. `Begripsafbakening en verbanden`

Waarom?

- de korte openingszin maakt backlink pop-ups veel bruikbaarder
- `Korte kern` maakt snelle herhaling mogelijk
- de deeper sections blijven geschikt voor echte studie
- `Execution/` blijft apart voor grotere worked examples

---

## Metadata-standaard

Om de vault goed te laten werken met links, overzichtsnotes en Obsidian Bases, moet metadata consistent zijn.

### Minimumset voor conceptnotes

- `type`
- `domain`
- `parent`
- `related`
- `theme`
- `aliases`

### Waarom deze velden nuttig zijn

- `type` maakt onderscheid tussen `topic`, `comparison`, `execution`, `map`
- `domain` maakt filteren per kennisdomein mogelijk
- `parent` helpt bij hiërarchie en navigatie
- `related` helpt bij semantische verbindingen
- `theme` helpt om het overkoepelende thema van een note te begrijpen
- `aliases` helpen bij leesbare links en alternatieve benamingen

Belangrijk:

- liever 6 consistente velden dan 15 half ingevulde velden
- metadata moet een hulpmiddel zijn, geen administratieve last

### Parent-first model

Voor hiërarchie gebruiken we voortaan een **parent-first model**:

- `parent` wordt expliciet ingevuld als primaire inhoudelijke kapstok
- `siblings` worden **niet** apart opgeslagen; die zijn afleidbaar als notes met dezelfde `parent`
- `children` worden **niet** apart opgeslagen; die zijn afleidbaar als notes die naar dezelfde umbrella-note verwijzen als `parent`

Waarom?

- minder dubbele administratie
- minder kans op inconsistentie
- beter bruikbaar in Bases
- duidelijkere semantische boomstructuur

Voorbeeld:

- `Blind Search` -> parent: `AI Search Techniques`
- `Heuristic Search` -> parent: `AI Search Techniques`
- `Breadth-First Search (BFS)` -> parent: `Blind Search`
- `Depth-First Search (DFS)` -> parent: `Blind Search`

Zo zijn:

- `Blind Search` en `Heuristic Search` automatisch siblings
- `BFS` en `DFS` automatisch children van `Blind Search`

---

## Maps en Obsidian Bases

### Maps

`Maps/` blijven de **didactische navigatielaag**.

Ze zijn bedoeld om:

- concepten inhoudelijk te groeperen
- leerpaden voor te stellen
- verbanden uit te leggen in mensentaal
- als startpunt te dienen bij studeren

Een map-note is dus een **leerkaart**, geen database.

### Obsidian Bases

`Obsidian Bases` zijn de **operationele indexlaag** bovenop de notestructuur.

Ze zijn bedoeld om:

- notes dynamisch te filteren en sorteren
- metadata snel te inspecteren
- ontbrekende velden of inconsistenties te vinden
- per domein snelle dashboards te maken

Belangrijk principe:

- `Maps` vervangen **niet** door `Bases`
- `Bases` vervangen **niet** de inhoudelijke kennisstructuur
- beide vullen elkaar aan

Kort:

- `Maps` = didactisch, handgemaakt, inhoudelijk
- `Bases` = dynamisch, querybaar, onderhoudsgericht

---

## Aanbevolen Bases

### 1. Alle conceptnotes

Doel:
- totaaloverzicht van alle notes in `20_Concepts/`

Nuttige kolommen:
- `type`
- `domain`
- `parent`
- `theme`
- `aliases`

### 2. Domeinspecifieke Bases

Voorbeelden:
- `AI Topics`
- `Machine Learning Topics`
- `Discrete Mathematics Topics`

Filter op:
- `domain`
- `type = concept-topic`

### 3. Comparison notes

Doel:
- snel alle vergelijkingsnotes terugvinden

Filter op:
- `type = concept-comparison`

### 4. Execution notes

Doel:
- worked examples en procedures snel terugvinden

Filter op:
- `type = concept-execution`

### 5. Notes met ontbrekende metadata

Doel:
- onderhoud en kwaliteitscontrole

Filter op notes waar 1 of meer van deze velden leeg zijn:
- `domain`
- `type`
- `related`
- `theme`

---

## Hoe Bases passen in de vault

De beste aanpak is:

- domeinmappen blijven de inhoudelijke thuisbasis
- `Maps/` blijven de hoofdnavigatie voor studeren
- `Bases` worden dashboards voor onderhoud en snelle filtering

Een goede toekomstige root-note zoals `00_Overzicht Concepten.md` kan dan bevatten:

- handgemaakte links naar de domeinen
- embedded `Bases` voor recente notes, comparisons en execution notes

---

## Richtlijnen

- organiseer `20_Concepts/` volgens kennisstructuur, niet volgens vaknamen
- kies altijd de **meest stabiele inhoudelijke thuisbasis**
- gebruik `Comparisons/` alleen voor echte vergelijkingsnotes
- gebruik `Execution/` alleen voor worked examples en procedures
- houd `Maps/` handgemaakt en didactisch
- gebruik `Bases` als extra indexlaag, niet als hoofdstructuur
- zorg dat elke conceptnote een backlink-vriendelijke openingszin heeft
- vermijd dubbele notes met bijna dezelfde functie
- vermijd massale herstructurering in 1 keer
- update map-notes wanneer een domein inhoudelijk groeit
- gebruik Windows-veilige bestandsnamen als nodig, maar hou links leesbaar in Obsidian

---

## Aanbevolen migratie in fasen

1. Huidige domeinen behouden als basis.
2. Nieuwe notes meteen correct in `Topics`, `Comparisons`, `Execution` of `Maps` plaatsen.
3. Bestaande `Topic`-notes stelselmatig normaliseren naar de nieuwe template.
4. Metadata standaardiseren (`type`, `domain`, `parent`, `related`, `theme`, `aliases`).
5. Een globale root-map voorzien voor `20_Concepts/`.
6. Daarna 2-3 kern-Bases opzetten als dashboardlaag.
7. Pas daarna grotere domeinmigraties evalueren (`Graph Theory`, `Software Design Principles`).
8. Overview-notes en backlinks mee bijwerken.

---

## Status

Dit document is een **bijgewerkt werkdocument** voor de huidige vault.

Huidige conclusie:

- de bestaande domeinstructuur is werkbaar
- kleine gerichte migraties zijn wenselijk
- een volledige superstructuur met `Mathematics/` en `Data & AI/` is voorlopig **niet nodig**
- `Maps` en `Obsidian Bases` samen vormen de beste combinatie voor navigatie en onderhoud

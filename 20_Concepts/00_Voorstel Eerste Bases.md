---
related:
  - 00_Overzicht Concepten
  - 00_Structuurvoorstel 20_Concepts
  - Base - Alle conceptnotes
  - Base - Metadata Check
type: concept-map
domain: "concept-root"
theme: "concept-vault-indexing"
aliases:
  - Voorstel Eerste Bases
---

# Voorstel Eerste Bases

Dit document stelt de eerste 3 `Obsidian Bases` voor die de meeste directe winst geven voor jouw vault. Het doel is niet om alles meteen te databasen, maar om met een kleine set nuttige dashboards te starten.

## Korte kern

- begin met 3 eenvoudige, hoog-nuttige Bases
- gebruik Bases als indexlaag, niet als vervanging van `Maps`
- focus eerst op overzicht, filteren en onderhoud

## 1. Wat is het kernprobleem?

Welke `Bases` geven het snelst meerwaarde in een groeiende conceptvault zonder extra complexiteit te veroorzaken?

## 2. Intuitieve uitleg

De beste eerste Bases zijn niet de meest complexe, maar degene die meteen helpen bij dagelijkse navigatie en onderhoud.

Daarom starten we best met 3 soorten overzicht:

- een **globaal overzicht** van alle conceptnotes
- een **inhoudelijke focusbasis** voor AI en ML-studie
- een **onderhoudsbasis** voor ontbrekende of inconsistente metadata

Zo krijg je tegelijk:

- beter zicht op je knowledge base
- sneller toegang tot relevante notes
- een praktisch hulpmiddel om kwaliteit op peil te houden

## 3. Formele structuur

De eerste 3 Bases steunen best op deze metadata:

- `type`
- `domain`
- `parent`
- `related`
- `theme`
- `aliases`

Zonder consistente metadata verliezen Bases veel van hun nut. Daarom zijn dit niet alleen zoekvensters, maar ook kwaliteitsinstrumenten.

Belangrijk binnen dit model:

- `parent` wordt expliciet opgeslagen
- `siblings` en `children` worden afgeleid via de Base-logica en niet als aparte properties beheerd

## 4. Snelle vergelijking

- `Base 1` = breed overzicht
- `Base 2` = snelle inhoudelijke studie-ingang
- `Base 3` = onderhoud en kwaliteitscontrole

Samen vormen ze een minimale maar sterke indexlaag.

## 5. Voorstel van de eerste 3 Bases

## Base 1 - Alle conceptnotes

### Doel

Een centraal overzicht van alle notes in `20_Concepts`, ongeacht domein.

### Waarom eerst?

Dit is je algemene catalogus. Als je niet weet waar iets staat, begin je hier.

### Aanbevolen kolommen

- `file.name`
- `type`
- `domain`
- `parent`
- `theme`

### Nuttige sortering

- eerst op `domain`
- daarna op `type`
- daarna alfabetisch op naam

### Typische use cases

- snel zien of een concept al bestaat
- snel springen tussen domeinen
- makkelijk controleren of een note een `Topic`, `Comparison`, `Execution` of `Map` is

### Concrete setup

Maak deze Base in de root van `20_Concepts/` met als scope alle markdown-notes onder `20_Concepts/`.

**Aanbevolen naam:** `Base - Alle conceptnotes`

**Bron / scope:**
- map: `20_Concepts/`
- bestandstype: markdown notes

**Aanbevolen zichtbare kolommen:**
- `file.name`
- `type`
- `domain`
- `parent`
- `theme`

**Aanbevolen verborgen of secundaire kolommen:**
- `related`
- `aliases`
- `file.path`

**Aanbevolen standaard sortering:**
1. `domain` oplopend
2. `type` oplopend
3. `file.name` oplopend

**Aanbevolen eerste filters:**
- toon alleen notes waarvan `type` bestaat

**Optionele views binnen dezelfde Base:**
- `Alles`
- `Alle Topics`
- `Alle Comparisons`
- `Alle Execution`
- `Alle Maps`

**Filterlogica per view:**
- `Alle Topics` -> `type = concept-topic`
- `Alle Comparisons` -> `type = concept-comparison`
- `Alle Execution` -> `type = concept-execution`
- `Alle Maps` -> `type = concept-map`

**Waarom deze config goed is:**
- eenvoudig genoeg om meteen bruikbaar te zijn
- breed genoeg om de hele vault te overzien
- sterk genoeg om dubbele of verkeerd geplaatste notes snel te spotten

## Base 2 - Studiebasis AI en ML

### Doel

Een focusbasis voor de domeinen die je het meest actief gebruikt voor je studies: `Artificial Intelligence` en `Machine Learning`.

### Waarom als tweede?

Dit geeft je meteen dagelijkse studie-waarde. In plaats van door mappen te klikken, kan je filteren op domein en note-type.

### Aanbevolen filters

- `domain = artificial-intelligence` OF `domain = machine-learning`

### Aanbevolen kolommen

- `file.name`
- `domain`
- `type`
- `parent`
- `related`

### Slimme views binnen dezelfde Base

- `AI Topics`
- `AI Comparisons`
- `AI Execution`
- `ML Topics`
- `ML Comparisons`
- `ML Execution`

### Typische use cases

- snel alle zoekalgoritmes zien
- snel alle worked examples zien
- snel alle ML-vergelijkingen terugvinden

## Base 3 - Metadata Check

### Doel

Een onderhoudsbasis die notes toont met ontbrekende, zwakke of inconsistente metadata.

### Waarom als derde?

Zodra je meer notes hebt, wordt consistentie moeilijker. Deze Base helpt je vault gezond houden.

### Aanbevolen controles

- ontbrekende `type`
- ontbrekende `domain`
- ontbrekende `parent` waar een note normaal een kapstok zou moeten hebben
- lege `related`
- lege `theme`
- ontbrekende `aliases` waar die nuttig zouden zijn

### Aanbevolen kolommen

- `file.name`
- `type`
- `domain`
- `related`
- `theme`
- `aliases`

### Typische use cases

- snel zien welke notes nog genormaliseerd moeten worden
- nieuwe notes direct afwerken
- structurele kwaliteit van de vault bewaren

## 6. Aanbevolen volgorde van implementatie

1. Maak `Base 1 - Alle conceptnotes`.
2. Maak `Base 2 - Studiebasis AI en ML`.
3. Maak `Base 3 - Metadata Check`.

Waarom deze volgorde?

- eerst overzicht
- dan inhoudelijke snelheid
- dan onderhoud

## 7. Praktische richtlijnen

- hou de eerste versie van elke Base simpel
- begin met weinig kolommen
- voeg pas extra views toe als je ze echt gebruikt
- gebruik `Maps` voor leren en verbanden
- gebruik `Bases` voor filteren, terugvinden en onderhouden

## 8. Begripsafbakening en verbanden

- **Kernonderscheid:** een Base is een dynamisch overzicht op basis van metadata; een Map is een handgemaakte didactische navigatienote.
- **Veelvoorkomende misvatting:** denken dat je eerst perfecte metadata op alle notes nodig hebt. Je kan klein starten en daarna verbeteren.
- **Link met andere concepten:** [[00_Structuurvoorstel 20_Concepts]], [[00_Overzicht Concepten]], [[00_Overzicht Artificial Intelligence]], [[00_Overzicht Machine Learning Concepten]]

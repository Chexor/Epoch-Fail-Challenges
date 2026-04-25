---
type: theory
domain: "software-engineering"
parent: [[00_Overzicht Software Engineering]]
related:
  - [[00_Overzicht Software Engineering]]
theme: "software-development-lifecycle"
aliases:
  - V-model
  - V model
---

# V-model
#concept #se

Het V-model is een softwareontwikkelingsmodel dat ontwikkelfasen links koppelt aan bijpassende testfasen rechts, zodat verificatie en validatie van bij het begin mee ingepland worden.

## Korte kern

- bouwt verder op de lineaire logica van het watervaldenken
- koppelt elke ontwerpfase aan een passende testfase
- benadrukt dat testen niet pas op het einde begint

## 1. Wat is het kernprobleem?

Hoe zorg je ervoor dat analyse, ontwerp en implementatie systematisch gecontroleerd worden, in plaats van pas helemaal op het einde te ontdekken dat het systeem niet klopt?

## 2. Intuitieve uitleg

Het model ziet eruit als een `V`. Links werk je steeds concreter naar beneden: van vereisten naar analyse, ontwerp en implementatie. Rechts klim je weer naar boven via testfasen die controleren of wat links bedacht werd ook echt correct gerealiseerd is.

De kernintuïtie is dus: voor elke stap waarin je iets specificeert of ontwerpt, moet er later een test zijn die nagaat of dat stuk ook correct is uitgewerkt.

## 3. Formele structuur

Een typische invulling is:

- links: gebruikersvereisten -> systeemontwerp -> detailontwerp -> implementatie
- rechts: unit test -> integratietest -> systeemtest -> acceptatietest

De koppeling is belangrijker dan de exacte benaming van de lagen:

- vereisten hangen samen met acceptatietesten
- systeemontwerp hangt samen met systeemtesten
- detailontwerp hangt samen met integratietesten
- code of componenten hangen samen met unit testen

## 4. Diagram

> Ruimte om later een V-modeldiagram toe te voegen.

```text
[diagram hier later toevoegen]
```

## 5. Snelle vergelijking

- watervalmodel = lineair fasemodel zonder expliciete testkoppeling per laag
- `V-model` = lineair fasemodel met expliciete koppeling tussen ontwikkel- en testfasen
- iteratieve of agile aanpak = werkt in kortere cycli en minder strikt sequentieel

## 6. Toepassing

Bij een examenvraag over het `V-model` moet je meestal kunnen tonen dat testen niet los staat van analyse en ontwerp. Je tekent dan links de ontwikkelstappen, onderaan de implementatie, en rechts de teststappen die elk niveau controleren.

## 7. Begripsafbakening en verbanden

- **Kernonderscheid:** het `V-model` is geen puur testmodel, maar een ontwikkelmodel waarin testen structureel gekoppeld wordt aan eerdere ontwikkelkeuzes.
- **Veelvoorkomende misvatting:** denken dat alle testen pas na implementatie bedacht worden. In het `V-model` worden ze conceptueel al mee voorzien tijdens analyse en ontwerp.
- **Link met andere concepten:** [[00_Overzicht Software Engineering]]

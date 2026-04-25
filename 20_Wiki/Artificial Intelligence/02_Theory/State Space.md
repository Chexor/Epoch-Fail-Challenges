---
type: theory
domain: "artificial-intelligence"
parent: Artificial Intelligence (AI)
related:
  - Artificial Intelligence (AI)
  - Search Algorithm
  - Branching Factor
  - Graaf
theme: "ai-basics-and-search"
aliases:
  - State Space
---

# State Space
#concept #ai

Een state space is de volledige verzameling van mogelijke toestanden en toegelaten overgangen waarin een zoekalgoritme een oplossing probeert te vinden.

## Korte kern

- een state space is het probleemmodel waarop search werkt
- states zijn mogelijke situaties; overgangen stellen acties voor
- zonder goede state-spacevoorstelling kan een zoekalgoritme niet systematisch zoeken

## Probleem

Hoe stel je een probleem zo voor dat een algoritme systematisch naar een oplossing kan zoeken?

## Toepassing

Stel dat je een routeprobleem hebt:

- `initial state`: je staat in stad `A`
- `goal state`: je wil in stad `G` raken
- `actions`: kies een weg naar een aangrenzende stad
- `path cost`: de totale afstand van de gekozen route

Dan bestaat de `state space` uit alle steden die je kan bereiken en alle toegelaten verbindingen tussen die steden. Zoekalgoritmes zoals `BFS`, `UCS` en `A*` werken op zo'n voorstelling.

## Formeel

- Een `state` is een mogelijke configuratie van het probleem.
- De `initial state` is de starttoestand.
- Een `goal state` is een toestand die voldoet aan de oplossingseis.
- Een `operator` of `action` zet een toestand om in een andere toestand.
- Een `path` is een opeenvolging van toestanden of acties.
- De `path cost` is de totale kost van een pad.
- De `state space` is de verzameling van alle mogelijke toestanden en overgangen.

Een zoekalgoritme werkt dus typisch op een graaf- of boomvoorstelling van een probleem:

- knopen stellen toestanden voor
- verbindingen stellen acties of overgangen voor
- gewichten kunnen kosten voorstellen

## Intuïtieve uitleg

Een `state space` is de volledige speelruimte van een probleem. Elke `state` is een mogelijke situatie waarin je je kan bevinden. Vanuit zo'n toestand kan je via toegelaten acties naar andere toestanden gaan.

Bij een doolhof is elke positie een toestand. De mogelijke bewegingen zijn de acties. Het doel is dan een pad vinden van de startpositie naar de uitgang.

## Verbanden

> **Valkuil:** de `state space` verwarren met alleen het gevonden pad.

- [[Artificial Intelligence (AI)]]
- [[Graaf]]
- [[Search Algorithm]]
- [[Heuristic]]
- [[Branching Factor]]

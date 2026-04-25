---
type: theory
domain: "machine-learning"
parent: "Machine Learning"
related:
  - "Supervised Learning"
  - "Unsupervised Learning"
  - "Supervised vs Unsupervised vs Reinforcement Learning"
theme: "learning-paradigm"
aliases:
  - bestraffend leren
  - bekrachtiging leren
---

# Reinforcement Learning
#concept #ml

**Reinforcement Learning (RL)** is een paradigma binnen [[Machine Learning]] waarbij een 'agent' leert beslissingen te nemen door interactie met een omgeving. De agent ontvangt beloningen (`rewards`) voor goede acties en straffen (`penalties`) voor slechte acties, en probeert zijn gedrag te optimaliseren om de cumulatieve beloning te maximaliseren.

## Korte kern
Reinforcement learning is als **het trainen van een hond**. De hond (`agent`) voert acties uit in zijn omgeving (bv. de woonkamer). Als hij een trucje goed doet ('zit'), krijgt hij een beloning (een koekje). Als hij iets verkeerd doet (op de bank kauwen), krijgt hij een 'straf' (een "nee!"). Na verloop van tijd leert de hond welk gedrag tot de meeste koekjes leidt.

## 1. Wat is het kernprobleem?
Hoe kan een agent een optimale strategie leren in een complexe, onbekende omgeving, waarbij de feedback over zijn acties pas met vertraging en in de vorm van een simpele beloning of straf komt?

## 2. Intuitieve uitleg
RL draait om leren door te proberen (`trial and error`). In tegenstelling tot supervised learning, waar het juiste antwoord wordt gegeven, moet een RL-agent zelf ontdekken welk gedrag het beste is. Het is een continu proces van actie, feedback (beloning/straf), en het aanpassen van de strategie (`policy`) om in de toekomst betere beloningen te krijgen.

## 3. Formele structuur
De kerncomponenten van een RL-systeem zijn:
- **Agent:** Het lerende component dat beslissingen neemt.
- **Environment:** De wereld waarin de agent opereert.
- **State (`s`):** Een snapshot van de omgeving op een bepaald moment.
- **Action (`a`):** Een van de mogelijke zetten die de agent kan doen.
- **Reward (`r`):** De feedback die de agent ontvangt na een actie in een bepaalde state.
- **Policy (`π`):** De strategie van de agent die bepaalt welke actie te kiezen in een bepaalde state.

De agent doorloopt een cyclus: observeer de state, kies een actie, ontvang een reward, ga naar een nieuwe state, en pas de policy aan.

## 4. Snelle vergelijking
- **[[Reinforcement Learning]]**: Leert van interactieve feedback (beloningen/straffen).
- **[[Supervised Learning]]**: Leert van statische data met correcte labels.
- **[[Unsupervised Learning]]**: Vindt patronen in data zonder labels of feedback.

## 5. Toepassing
- **Spelcomputers:** Het trainen van AI om spellen zoals schaken, Go (AlphaGo) of complexe videogames te spelen.
- **Robotica:** Robots leren om taken uit te voeren in de fysieke wereld, zoals het oppakken van objecten.
- **Zelfrijdende auto's:** Beslissingsmodellen trainen voor sturen, versnellen en remmen.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** De feedback is een schaars signaal (een beloning), niet een expliciet 'juist antwoord'. Het leren gebeurt over een reeks van beslissingen, niet op basis van een enkel datapunt.
- **Veelvoorkomende misvatting:** RL wordt soms verward met een simpel "if-this-then-that" systeem. De kracht van RL is juist dat het een strategie kan leren in omgevingen die te complex zijn voor handgeschreven regels.
- **Link met andere concepten:** Een van de drie grote paradigma's van [[Machine Learning]]. Het heeft sterke banden met [[Artificial Intelligence (AI)]] op het gebied van besluitvorming en planning.

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

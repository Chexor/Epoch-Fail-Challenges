---
type: theory
domain: "machine-learning"
parent: "Machine Learning"
related:
  - "Supervised Learning"
  - "Reinforcement Learning"
  - "Supervised vs Unsupervised vs Reinforcement Learning"
  - "Clustering"
  - "K-Means"
theme: "learning-paradigm"
aliases:
  - niet-gesuperviseerd leren
---

# Unsupervised Learning
#concept #ml

**Unsupervised Learning** is een paradigma binnen [[Machine Learning]] waarbij een model leert van een dataset die geen gelabelde outputs bevat. Het algoritme moet zelfstandig patronen, structuren of relaties in de data ontdekken.

## Korte kern
Unsupervised learning is als **het sorteren van een doos gemengde LEGO-blokken zonder instructies**. Het model krijgt alleen de data (`de blokken`) en moet zelf uitzoeken welke blokken bij elkaar horen op basis van kenmerken zoals kleur, vorm en grootte. Het doel is om de verborgen structuur in de data te vinden.

## 1. Wat is het kernprobleem?
Hoe kan een model betekenisvolle inzichten of patronen uit data halen als er geen 'juiste antwoorden' zijn om van te leren?

## 2. Intuitieve uitleg
In tegenstelling tot supervised learning, is er bij unsupervised learning geen leraar die de antwoorden geeft. Het model wordt losgelaten op de data en moet zelf op zoek naar interessante structuren. Het is alsof je naar een menigte mensen kijkt en probeert te ontdekken welke subgroepen er zijn op basis van kledingstijl, gedrag of hoe dicht ze bij elkaar staan, zonder dat iemand je vertelt welke groepen er zouden moeten zijn.

## 3. Formele structuur
- **Trainingsdata:** Bestaat enkel uit input-features, `X`. Er zijn geen `y`-labels.
- **Doel:** De onderliggende structuur of distributie in de data modelleren.
- **Twee hoofdtaken:**
    1.  **[[Clustering]]**: Data groeperen in clusters op basis van gelijkenis.
    2.  **Dimensionality Reduction**: Het aantal variabelen verminderen met behoud van de belangrijkste informatie.

## 4. Snelle vergelijking
- **[[Unsupervised Learning]]**: Ontdekt patronen in ongelabelde data.
- **[[Supervised Learning]]**: Leert een mapping van input naar output op basis van gelabelde data.

## 5. Toepassing
- **Klantsegmentatie:** Klanten groeperen voor gerichte marketing.
- **Anomaliedetectie:** Ongewone datapunten identificeren die niet in een cluster passen (bv. fraude).
- **Topic Modeling:** Automatisch de belangrijkste onderwerpen in een verzameling documenten ontdekken.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** De afwezigheid van labels in de trainingsdata. Het doel is ontdekking, niet voorspelling van een gekend target.
- **Veelvoorkomende misvatting:** Clustering wordt vaak verward met classificatie. Classificatie vereist vooraf bekende klassen, terwijl clustering deze klassen zelf probeert te vinden.
- **Link met andere concepten:** Een van de drie grote paradigma's in [[Machine Learning]]. [[Clustering]] is de meest prominente taak, met [[K-Means]] als een bekend algoritme.

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

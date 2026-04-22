---
type: theory
domain: "machine-learning"
parent: "Neural Network Models"
related:
  - Neural Network Models
  - Deep Learning
  - Neural Network
  - Transformer
  - Mixture-of-Experts (MoE)
  - Machine Learning
theme: "neural-network-models"
aliases:
  - Conditional Memory
  - DeepSeek Engram
---

# Engram
#concept #ml

Engram is een `conditional memory`-module van DeepSeek die statische patroonkennis via `O(1)` lookup toevoegt aan een taalmodel, zodat minder GPU-compute verspild wordt aan zaken die eerder op opzoeken lijken dan op redeneren.

## Korte kern

- Engram vult een transformer aan met een aparte geheugenlaag voor snelle statische lookup
- het probeert `memory` en `reasoning` gedeeltelijk van elkaar los te trekken
- het is een architecturale bouwsteen binnen grote taalmodellen, geen externe tool zoals `RAG`

## 1. Wat is het kernprobleem?

Transformers zijn sterk in flexibele berekening, maar zwak in expliciete lookup van vaste kennis of vaak terugkerende tokenpatronen.

Daardoor gebruiken ze dure neurale berekening voor dingen die conceptueel dichter bij opzoeken liggen, zoals vaste uitdrukkingen, namen of lokale patrooncombinaties. Engram probeert dat inefficiente stuk apart te behandelen.

## 2. Intuitieve uitleg

Denk aan een klassiek taalmodel als een systeem dat telkens opnieuw moet "uitrekenen" wat het al heel vaak gezien heeft. Engram voegt daar een tweede spoor aan toe:

- het gewone model doet de dynamische interpretatie en redenering
- Engram doet snelle geheugenlookup voor statische of vaak terugkerende patronen

De kernintuïtie is dus niet "groter model = beter", maar eerder:

- sommige taken vragen echte berekening
- sommige taken vragen vooral snelle herinnering

Volgens DeepSeek werkt een hybride combinatie van beide beter dan alles via dezelfde transformerlagen te forceren.

## 3. Formele structuur

Engram komt uit de DeepSeek-paper *Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models*.

Belangrijke ideeën:

- het moduleert `conditional memory` als extra sparsity-as naast `Mixture-of-Experts (MoE)`
- het moderniseert klassieke `N-gram embeddings` tot een geheugenmechanisme met `O(1)` lookup
- het gebruikt deterministische adressering op basis van de input-tokenreeks
- opgehaalde geheugensignalen worden samengevoegd met de dynamische hidden states van het model
- een gating-mechanisme filtert irrelevante of botsende geheugenhits weg

Belangrijke implicaties uit de paper:

- een deel van de modelcapaciteit verschuift van compute naar geheugen
- vroege lagen moeten minder statische reconstructie doen, waardoor meer effectieve diepte overblijft voor moeilijkere redenering
- doordat lookup deterministisch is, kan geheugen uit host RAM geprefetcht worden met lage overhead

DeepSeek beschrijft dit als een nieuwe afweging tussen:

- `neural computation`
- `static memory`

Hun experimenten suggereren dat niet alle sparse capaciteit naar compute moet gaan; een gemengde verdeling kan beter werken.

## 4. Snelle vergelijking

- `Engram` = interne geheugenmodule binnen het model voor snelle statische lookup
- [[Mixture-of-Experts (MoE)]] = conditionele compute via selectie van experts
- [[Transformer]] = de basisarchitectuur die door Engram aangevuld kan worden
- [[Deep Learning]] = brede modelfamilie van diepe neurale netwerken
- [[Neural Network]] = algemene netwerkstructuur, zonder dat daar automatisch zo'n apart geheugenmechanisme in zit

Belangrijk onderscheid:

- `Engram` is geen klassieke `RAG`, want de lookup gebeurt binnen de modelarchitectuur zelf en niet via een externe documentretriever
- `Engram` is ook geen episodisch agentgeheugen met chatgeschiedenis of gebruikersvoorkeuren

## 5. Toepassing

Een taalmodel dat vaak vaste technische termen, namen of bekende tokencombinaties tegenkomt, kan zulke patronen via Engram sneller ophalen in plaats van ze telkens opnieuw via meerdere transformerlagen te reconstrueren.

Volgens de DeepSeek-resultaten helpt dat niet alleen bij kennisvragen, maar ook bij redeneer-, codeer- en lange-contexttaken, omdat het gewone model meer capaciteit overhoudt voor moeilijkere verwerking.

## 6. Begripsafbakening en verbanden

- **Kernonderscheid:** Engram is een architecturale geheugencomponent voor grote taalmodellen, geen losse applicatielaag rond een model.
- **Veelvoorkomende misvatting:** denken dat Engram gewoon "meer geheugen" betekent; het gaat specifieker om deterministische lookup van statische patronen als aanvulling op neurale berekening.
- **Link met andere concepten:** [[Machine Learning]], [[Neural Network Models]], [[Neural Network]], [[Deep Learning]], [[Transformer]], [[Mixture-of-Experts (MoE)]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

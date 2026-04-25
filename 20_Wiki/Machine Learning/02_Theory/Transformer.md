---
type: theory
domain: "machine-learning"
parent: "Neural Network Models"
related:
  - Neural Network Models
  - Neural Network
  - Deep Learning
  - Attention
  - Self-Attention
  - Mixture-of-Experts (MoE)
  - Engram
  - Machine Learning
  - Transformer Python Worked Example
theme: "neural-network-models"
aliases:
  - Transformer Architecture
  - Transformer Model
---

# Transformer
#concept #ml

Transformer is een deep-learningarchitectuur die `self-attention` gebruikt om relaties tussen tokens parallel te modelleren, en vormt de kern van veel moderne `LLMs`.

## Korte kern

- een transformer verwerkt tokens vooral via [[Self-Attention]] in plaats van recurrency
- hij laat sterke parallelisatie toe en schaalde daardoor goed naar grote taalmodellen
- Engram probeert net zo'n transformer aan te vullen met explicietere geheugenlookup

## 1. Wat is het kernprobleem?

Hoe verwerk je een volledige sequentie zodat het model zowel lokale als verre verbanden tussen tokens kan meenemen, zonder alles stap voor stap zoals bij een `RNN` te moeten aflopen?

## 2. Intuitieve uitleg

Bij een transformer kijkt elk token als het ware naar andere relevante tokens in dezelfde context en beslist het hoeveel aandacht elk token verdient.

Daardoor kan het model sneller verbanden leggen zoals:

- welk woord bij welk onderwerp hoort
- welke eerdere passage belangrijk is voor de huidige voorspelling
- welke delen van de context genegeerd mogen worden

De grote winst is dat dit veel beter te paralleliseren is dan klassieke recurrente netwerken.

## 3. Formele structuur

Een transformer bestaat typisch uit:

- token- en positie-embeddings
- herhaalde blokken met `self-attention`
- feedforward-lagen
- normalisatie en residual verbindingen

Belangrijke eigenschappen:

- tokens worden omgezet naar vectorrepresentaties
- [[Self-Attention]] laat tokens informatie uitwisselen binnen een contextvenster
- [[Attention]] in meerdere heads laat het model verschillende soorten relaties tegelijk volgen
- moderne varianten worden vaak gebruikt als `encoder-only`, `decoder-only` of `encoder-decoder`

Waarom dit belangrijk was:

- minder sequentiele bottleneck dan bij `RNN` of `LSTM`
- sterk schaalbaar naar grote datasets en modellen
- vormt de architecturale basis van systemen zoals `GPT` en vele andere `LLMs`

## 4. Snelle vergelijking

- `Transformer` = algemene architectuur voor sequentiemodellering met [[Attention]]
- [[Neural Network]] = breder begrip voor neurale netwerkmodellen in het algemeen
- [[Deep Learning]] = bredere modelfamilie waar transformers een deel van zijn
- [[Attention]] = algemeen mechanisme om context dynamisch te wegen
- [[Self-Attention]] = aandacht binnen dezelfde sequentie
- [[Engram]] = extra geheugenmodule die een transformer kan aanvullen

## 5. Toepassing

Bij tekstgeneratie krijgt een transformer een reeks tokens als context en gebruikt hij [[Self-Attention]] om te bepalen welke eerdere tokens het belangrijkst zijn voor het voorspellen van het volgende token.

Dat maakt transformers zeer geschikt voor taalmodellen, samenvattingen, vertaling en andere taken waarbij contextrelaties cruciaal zijn.

Kort Python-voorbeeld:

```python
def weighted_sum(values, weights):
    return sum(value * weight for value, weight in zip(values, weights))


context_value = weighted_sum([1.2, 0.4, 2.0], [0.2, 0.3, 0.5])
```

Voor een volledige Python-uitwerking, zie [[Transformer Python Worked Example]].

## 6. Begripsafbakening en verbanden

- **Kernonderscheid:** een transformer is een basisarchitectuur; hij beschrijft hoe informatie verwerkt wordt, niet automatisch hoe geheugen of routing georganiseerd is.
- **Veelvoorkomende misvatting:** denken dat een transformer per definitie hetzelfde is als een `LLM`; een `LLM` is meestal een grote toepassing van transformerideeën, niet het basisconcept zelf.
- **Link met andere concepten:** [[Machine Learning]], [[Neural Network Models]], [[Neural Network]], [[Deep Learning]], [[Attention]], [[Self-Attention]], [[Engram]], [[Mixture-of-Experts (MoE)]], [[Transformer Python Worked Example]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

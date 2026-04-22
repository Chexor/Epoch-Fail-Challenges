---
type: theory
domain: "machine-learning"
parent: "Attention"
related:
  - Attention
  - Transformer
  - Neural Network Models
  - Deep Learning
  - Machine Learning
theme: "neural-network-models"
aliases:
  - Self Attention
  - Scaled Dot-Product Self-Attention
---

# Self-Attention
#concept #ml

Self-Attention is een vorm van attention waarbij elk token gewichten berekent ten opzichte van andere tokens in dezelfde sequentie, zodat contextafhankelijke representaties ontstaan.

## Korte kern

- elk token kan rechtstreeks naar andere tokens in dezelfde input kijken
- zo worden verre afhankelijkheden beter zichtbaar zonder recurrency
- dit is de kernbouwsteen van moderne transformers

## 1. Wat is het kernprobleem?

Hoe laat je elk element in een sequentie context uit diezelfde sequentie gebruiken om zijn eigen representatie te verfijnen?

## 2. Intuitieve uitleg

Bij `self-attention` stelt elk token als het ware de vraag: "naar welke andere tokens moet ik nu luisteren om mezelf goed te begrijpen?"

Daardoor kan een woord zoals `bank` meer gewicht geven aan woorden zoals `geld` of `rivier`, afhankelijk van de context.

Het grote voordeel is dat elk token niet alleen van zijn nabije buren leert, maar meteen van relevante stukken elders in de sequentie.

## 3. Formele structuur

Bij `self-attention` komen `query`, `key` en `value` allemaal uit dezelfde inputrepresentaties.

Typisch verloopt het zo:

- elke tokenembedding wordt geprojecteerd naar een `query`
- dezelfde input levert ook `keys`
- dezelfde input levert ook `values`
- elke `query` krijgt scores tegenover alle `keys`
- de gewogen som van de `values` vormt de nieuwe contextuele representatie

Belangrijke eigenschappen:

- directe koppeling tussen alle tokens binnen het contextvenster
- sterk paralleliseerbaar
- vaak gebruikt in meerdere heads tegelijk via `multi-head attention`
- vormt de kern van `decoder-only`, `encoder-only` en `encoder-decoder` transformers

## 4. Snelle vergelijking

- [[Attention]] = algemene familie van aandachtmechanismen
- `Self-Attention` = aandacht binnen dezelfde sequentie
- [[Transformer]] = architectuur die self-attention systematisch gebruikt

## 5. Toepassing

In een taalmodel kan het token `het` via self-attention sterker linken naar een eerder zelfstandig naamwoord waarop het terugwijst, zodat de representatie van `het` rijker en contextgevoeliger wordt.

Dat is een van de redenen waarom transformers taalrelaties zo krachtig kunnen modelleren.

## 6. Begripsafbakening en verbanden

- **Kernonderscheid:** self-attention is een specifieke vorm van attention waarbij bron en doel uit dezelfde sequentie komen.
- **Veelvoorkomende misvatting:** denken dat self-attention gewoon "kijken naar alles" betekent; in werkelijkheid leert het model gewogen, contextafhankelijke relaties.
- **Link met andere concepten:** [[Machine Learning]], [[Neural Network Models]], [[Deep Learning]], [[Attention]], [[Transformer]], [[Engram]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

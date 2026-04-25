---
type: theory
domain: "artificial-intelligence"
parent: Artificial Intelligence (AI)
related:
  - Rational Agent
  - Search Algorithm
  - Machine Learning
theme: "ai-basics-and-search"
aliases:
  - Expert Systems
  - Expertensystemen
---

# Expert Systems
#concept #ai

Expert systems zijn AI-systemen die domeinkennis en regels expliciet modelleren om beslissingen of diagnoses te ondersteunen.

## Korte kern

- een expert system redeneert via kennisbanken en inference rules
- de kracht zit in uitlegbaarheid en domeinspecifieke precisie
- ze werken vooral goed in stabiele domeinen met duidelijke regels

## Probleem

Hoe leg je specialistische menselijke expertise vast zodat een systeem consequent advies kan geven zonder telkens een menselijke expert nodig te hebben?

## Intuïtie

Denk aan een digitale checklist met redenering: op basis van feiten en regels leidt het systeem af welke conclusie het meest logisch is. In plaats van te leren uit grote hoeveelheden data, gebruikt het expliciete kennis van experten.

## Toepassing

In medische triage kan een expert system symptomen, risicofactoren en beslisregels combineren om een eerste differentiaaldiagnose voor te stellen. In technische support kan het foutcodes en symptomen koppelen aan waarschijnlijke oorzaken en acties.

## Formeel

- Een expert system bevat typisch:
  - een **knowledge base** met feiten en regels
  - een **inference engine** die regels toepast op beschikbare feiten
  - een interface voor input en uitleg van conclusies
- Redenering verloopt vaak via:
  - **forward chaining** (van feiten naar conclusies)
  - **backward chaining** (van hypothese naar noodzakelijke feiten)
- Sterke punten: transparantie, reproduceerbaarheid, domeinspecifieke consistentie.
- Beperkingen: kennisacquisitie is duur, onderhoud van regels schaalt moeilijk, minder robuust bij onzekere of snel veranderende contexten.

## Verbanden

- [[Artificial Intelligence (AI)]]
- [[Rational Agent]]
- [[Search Algorithm]]
- [[Machine Learning]]

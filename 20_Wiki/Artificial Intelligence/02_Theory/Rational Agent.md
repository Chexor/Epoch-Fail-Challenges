---
type: theory
domain: "artificial-intelligence"
parent: Artificial Intelligence (AI)
related:
  - Search Algorithm
  - State Space
  - Machine Learning
theme: "ai-basics-and-search"
aliases:
  - Rational Agent
---

# Rational Agent
#concept #ai

Een rational agent is een systeem dat in elke situatie de actie kiest die zijn verwachte doelbereiking maximaliseert op basis van wat het weet en kan waarnemen.

## Korte kern

- een rational agent kiest doelgericht in plaats van willekeurig te handelen
- rationaliteit betekent niet perfectie, maar de beste keuze gegeven beperkte informatie
- het concept is de moderne kern om AI-systemen te definiëren en te vergelijken

## Probleem

Hoe beschrijf je "intelligent gedrag" op een manier die toetsbaar en bruikbaar is voor het ontwerpen van AI-systemen?

## Intuïtie

Zie een rational agent als een goede navigator: die weet niet alles, maar kiest telkens de meest verstandige volgende stap met de informatie die op dat moment beschikbaar is. De agent hoeft dus niet onfeilbaar te zijn; hij moet consequent keuzes maken die het doel het best dienen binnen de context.

## Toepassing

Bij robotnavigatie kiest een rational agent niet zomaar de kortste lijn, maar de actie met de hoogste verwachte opbrengst gegeven obstakels, sensorrandruis en resterende batterij. In een zoekprobleem doet een algoritme als `A*` iets gelijkaardigs: het kiest de volgende stap op basis van een evaluatie van huidige kost en geschatte resterende kost.

## Formeel

- Een **agent** neemt percepties waar uit een omgeving en kiest acties.
- Een **performance measure** definieert wat "goed" gedrag is.
- Een agent is **rationeel** als hij, voor elke perceptiegeschiedenis, de actie kiest die de verwachte waarde van die performance measure maximaliseert.
- Rationaliteit hangt af van:
  - beschikbare percepties
  - aanwezige voorkennis
  - mogelijke acties
  - beschikbare rekentijd en middelen
- Rationaliteit is dus contextgebonden en verschilt van alwetendheid.

## Verbanden

- [[Artificial Intelligence (AI)]]
- [[Search Algorithm]]
- [[State Space]]
- [[Machine Learning]]

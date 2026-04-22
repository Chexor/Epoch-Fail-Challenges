---
type: practice
domain: "machine-learning"
parent: "Attention"
related:
  - Attention
  - Self-Attention
  - Transformer
  - Transformer Python Worked Example
theme: "python-ml-implementations"
aliases:
  - Attention Python Worked Example
  - Attention Python Example
---

# Attention Python Worked Example
#concept #ml

Attention Python Worked Example toont hoe ruwe scores eerst naar gewichten worden genormaliseerd en daarna gebruikt worden om context te wegen.

## Korte kern

- zet scores om naar gewichten
- maakt zichtbaar dat aandacht een verdeling over context is
- vormt een brug naar `Self-Attention` en `Transformer`

## Ondersteund concept
- [[Attention]]

## Doel van deze uitwerking
Deze note toont een kleine Python-schets van attention zonder zware matrixnotatie, zodat het kernidee helder blijft.

## Context
Gebruik dit wanneer je de basisintuïtie van attention wil begrijpen voor je naar self-attention en transformers gaat.

## Codevoorbeeld
```python
def normalize(scores):
    total = sum(scores)
    return [score / total for score in scores]


scores = [2.0, 3.0, 5.0]
weights = normalize(scores)
print(weights)
```

## Stap-voor-stap uitleg
- `scores` drukken ruwe relevantie uit
- normalisatie maakt er vergelijkbare gewichten van
- die gewichten kunnen daarna gebruikt worden om contextwaarden te combineren

## Verwachte output of gedrag
- de output is hier een lijst gewichten die samen `1.0` vormen
- grotere scores krijgen een groter aandeel in de aandacht

## Uitwerking
1. Start met ruwe aandachtsscores.
2. Tel alle scores op.
3. Deel elke score door het totaal.
4. Gebruik de gewichten om contextwaarden te combineren.

## Wat toont dit voorbeeld?
- waarom attention niet gewoon "kijken" is, maar gewogen contextverdeling
- hoe score naar gewicht een cruciale stap vormt

## Typische fouten
- denken dat ruwe scores al direct gewichten zijn
- vergeten dat attention een mechanisme is en geen volledig model

## Verwante concepten
- [[Attention]]
- [[Self-Attention]]
- [[Transformer]]
- [[Transformer Python Worked Example]]

## Begripsafbakening en verbanden
- **Kernonderscheid:** deze note toont de wegingintuïtie van attention, niet de volledige query-key-value-formule.
- **Veelvoorkomende misvatting:** denken dat attention en transformer synoniemen zijn; attention is een bouwsteen binnen een bredere architectuur.
- **Link met andere concepten:** [[Attention]], [[Self-Attention]], [[Transformer]], [[Transformer Python Worked Example]], [[Neural Network]]

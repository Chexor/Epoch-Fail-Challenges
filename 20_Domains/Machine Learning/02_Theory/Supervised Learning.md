---
type: theory
domain: "machine-learning"
parent: "Machine Learning"
related:
  - "Unsupervised Learning"
  - "Reinforcement Learning"
  - "Supervised vs Unsupervised vs Reinforcement Learning"
  - "Classification"
  - "Regression"
theme: "learning-paradigm"
aliases:
  - gesuperviseerd leren
---

# Supervised Learning
#concept #ml

**Supervised Learning** is een paradigma binnen [[Machine Learning]] waarbij een model leert van een dataset die gelabelde voorbeelden bevat. Elk voorbeeld bestaat uit een input en een corresponderende, correcte output.

## Korte kern
Supervised learning is als **leren met een antwoordenboek**. Het model krijgt een reeks vragen (`input`) en de bijbehorende juiste antwoorden (`output labels`). Het doel is om het patroon tussen de vragen en antwoorden te leren, zodat het later zelfstandig nieuwe, onbekende vragen kan beantwoorden.

## 1. Wat is het kernprobleem?
Hoe kan een model leren om correcte voorspellingen te doen wanneer het toegang heeft tot een dataset met historische voorbeelden en de bijbehorende juiste uitkomsten?

## 2. Intuitieve uitleg
Stel, je leert een kind verschillende dieren herkennen. Je toont een foto van een kat (de input) en zegt "dit is een kat" (het label). Na vele voorbeelden van verschillende dieren leert het kind een patroon. Als je dan een nieuwe, onbekende foto van een kat toont, kan het kind zelfstandig zeggen: "dat is een kat". Dit is de essentie van supervised learning.

## 3. Formele structuur
- **Trainingsdata:** Bestaat uit paren van input-features en output-labels, `(X, y)`.
- **Doel:** Het leren van een mapping-functie `f` die de relatie tussen `X` en `y` zo goed mogelijk benadert, `y ≈ f(X)`.
- **Twee hoofdtaken:**
    1.  **[[Classification]]**: Het label `y` is een categorie (bv. "spam", "kat").
    2.  **[[Regression]]**: Het label `y` is een continue waarde (bv. 25.5, 150.000).

## 4. Snelle vergelijking
- **[[Supervised Learning]]**: Leert van gelabelde data (input + correcte output).
- **[[Unsupervised Learning]]**: Leert van ongelabelde data (enkel input).
- **[[Reinforcement Learning]]**: Leert door middel van beloningen en straffen.

## 5. Toepassing
- Voorspellen of een creditcardtransactie frauduleus is ([[Classification]]).
- De prijs van een huis voorspellen op basis van kenmerken ([[Regression]]).
- Handgeschreven cijfers herkennen ([[Classification]]).

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** De aanwezigheid van expliciete, correcte output-labels in de trainingsdata is wat dit paradigma definieert.
- **Link met andere concepten:** Het is een van de drie grote paradigma's in [[Machine Learning]]. Het omvat de meest voorkomende taken zoals [[Classification]] en [[Regression]].

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

---
type: atom
domain: "artificial-intelligence"
parent: Search Evaluation Functions
related:
  - g(n)
  - f(n)
  - Heuristiek
  - Search Evaluation Functions
theme: "search-cost-accounting"
aliases:
  - h(n)
---

# h(n)
#concept #ai

`h(n)` is een heuristische schatting van de kost van node `n` naar het doel. Het zegt dus niet wat het pad al gekost heeft, maar wat er **nog zou kunnen resten**.

## Korte kern

- kijkt naar de **toekomst** van het pad
- is een **schatting**, geen echte kost
- centraal in [[Heuristic]], [[Greedy Best-First Search]] en [[A-star Search]]

## 1. Wat is het kernprobleem?
Hoe druk je uit hoe veelbelovend een node lijkt met het oog op het doel?

## 2. Intuitieve uitleg
`h(n)` is een schatting van wat het nog zou kosten om van node `n` naar het doel te gaan. Het is dus geen gemeten kost, maar een heuristische inschatting.

## 3. Formele structuur
- `h(n)` = geschatte resterende kost van `n` tot het doel
- `h(n)` is de centrale score in [[Heuristic]]
- bij [[Greedy Best-First Search]] bepaalt `h(n)` rechtstreeks de prioriteit
- bij [[A-star Search]] wordt `h(n)` gecombineerd met [[g(n)]] tot [[f(n)]]

## 4. Snelle vergelijking

- [[g(n)]] = echte kost tot nu toe
- [[h(n)]] = geschatte resterende kost
- [[f(n)]] = combinatie van beide

## 5. Toepassing
In een routeprobleem kan hemelsbrede afstand dienen als `h(n)`: ze is niet exact, maar geeft wel aan welke steden dichter bij het doel lijken te liggen.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** `h(n)` is een schatting, geen echte padkost.
- **Veelvoorkomende misvatting:** denken dat `h(n)` exact moet zijn om nuttig te zijn.
- **Link met andere concepten:** [[Heuristic]], [[Greedy Best-First Search]], [[A-star Search]], [[Admissible Heuristic]], [[Consistent Heuristic]], [[g(n)]], [[f(n)]]
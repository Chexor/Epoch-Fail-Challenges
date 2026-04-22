---
type: theory
domain: "artificial-intelligence"
parent: AI Search Techniques
related:
  - g(n)
  - h(n)
  - f(n)
theme: "search-cost-accounting"
aliases:
  - Search Evaluation Functions
---

# Search Evaluation Functions
#concept #ai

Search Evaluation Functions zijn de grootheden waarmee een zoekalgoritme de kwaliteit of prioriteit van een node evalueert tijdens het zoeken.

## Korte kern

- groepeert de belangrijkste evaluatiefuncties in search
- helpt het verschil zien tussen echte kost, schatting en gecombineerde score
- vormt de kapstok voor [[g(n)]], [[h(n)]] en [[f(n)]]

## Probleem

Hoe druk je formeel uit welke node een zoekalgoritme als meest veelbelovend beschouwt?

## Intuïtie

Een zoekalgoritme heeft vaak een score nodig om nodes te rangschikken. Soms is dat de echte kost tot nu toe, soms een schatting van de toekomst, en soms een combinatie van beide.

## Toepassing

Wanneer je op examen een priority queue van `UCS`, `Greedy` of `A*` moet uitschrijven, werk je in feite met search evaluation functions.

## Formeel

De belangrijkste evaluatiefuncties zijn:

- [[g(n)]] = echte kost tot nu toe
- [[h(n)]] = geschatte resterende kost
- [[f(n)]] = gecombineerde evaluatiescore via `g(n) + h(n)`

Ze worden gebruikt in verschillende algoritmes:

- [[Uniform-Cost Search (UCS)]] gebruikt vooral [[g(n)]]
- [[Greedy Best-First Search]] gebruikt vooral [[h(n)]]
- [[A-star Search]] gebruikt vooral [[f(n)]]

## Verbanden

> **Valkuil:** `g(n)`, `h(n)` en `f(n)` als losse symbolen kennen zonder hun gemeenschappelijke rol te zien.

- [[AI Search Techniques]]
- [[g(n)]]
- [[h(n)]]
- [[f(n)]]
- [[Uniform-Cost Search (UCS)]]

---
type: concept-topic
domain: "artificial-intelligence"
parent: Heuristic Search
related:
  - Heuristic Search
  - g(n)
  - h(n)
  - f(n)
theme: "heuristic-search"
aliases:
  - Heuristiek
---

# Heuristiek
#concept #ai

## 1. Wat is het kernprobleem?
Hoe kan je een zoekalgoritme sneller naar een oplossing sturen zonder alle mogelijkheden blind te moeten doorlopen?

## 2. Intuïtieve uitleg
Een `heuristiek` is een slimme schatting. Ze zegt niet exact hoe ver je nog van het doel verwijderd bent, maar geeft een nuttige indicatie van welke richting waarschijnlijk beter is.

Bij routeplanning is de hemelsbrede afstand naar de bestemming bijvoorbeeld een heuristiek. Die afstand is niet noodzakelijk de echte wegafstand, maar helpt wel om te beslissen welke stad er veelbelovend uitziet.

## 3. Formele structuur
- Een `heuristiek` is een functie `h(n)`.
- `h(n)` schat de kost van node `n` tot het doel.
- Een heuristiek wordt gebruikt om nodes in de `frontier` te rangschikken.
- Ze komt vooral voor in `heuristic search` zoals `Greedy` en `A*`.

Belangrijke verwante grootheden:

- [[g(n)]]: de echte kost van start tot node `n`
- [[h(n)]]: de geschatte resterende kost van `n` tot het doel
- [[f(n)]] = `g(n) + h(n)`: de geschatte totale kost van een oplossing via `n`

Belangrijke eigenschappen van heuristieken:

- **admissible**: de heuristiek overschat de echte resterende kost nooit
- **consistent**: de heuristiek respecteert de driehoeksvoorwaarde en daalt niet sneller dan de werkelijke stapkost toelaat

Voorbeelden van heuristieken:

- `Manhattan distance`
- `Euclidean distance`
- `Misplaced tiles`

## 4. Toepassing
Bij `Greedy Best-First Search` wordt alleen `h(n)` gebruikt. Het algoritme kiest dus de node die het dichtst bij het doel lijkt.

Bij `A*` wordt niet alleen naar de schatting gekeken, maar ook naar de al gemaakte kost:

- `A*` gebruikt `f(n) = g(n) + h(n)`

Daardoor is `A*` meestal betrouwbaarder dan `Greedy`, omdat het niet alleen op gevoel richting doel loopt, maar ook rekening houdt met de kost van het pad tot nu toe.

## 5. Begripsafbakening en verbanden
- **Kernonderscheid:** een heuristiek is een schatting, geen exacte resterende kost.
- **Veelvoorkomende misvatting:** denken dat een heuristiek alleen nuttig is als ze perfect exact is.
- **Link met andere concepten:** [[Search Algorithm]], [[State Space]], [[Artificial Intelligence (AI)]], [[Graaf]], [[Greedy Best-First Search]], [[A-star Search|A* Search]], [[Admissible Heuristic]], [[Consistent Heuristic]], [[g(n)]], [[h(n)]], [[f(n)]]
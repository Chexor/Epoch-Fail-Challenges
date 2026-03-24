# Samenvatting Topic 7: Optimal Search

In dit topic verdiepen we ons in de wiskundige garanties van zoekalgoritmen. We kijken niet alleen naar het vinden van *een* oplossing, maar naar het vinden van de *beste* (goedkoopste) oplossing.

## 1. Het Kernprobleem (Big Picture)
Bij complexe problemen is het niet genoeg om een doel te bereiken; de route ernaartoe bepaalt de efficiëntie en kosten. Het kernprobleem is: **Hoe kunnen we garanderen dat een algoritme het optimale pad vindt zonder de hele zoekruimte te moeten doorzoeken?** Dit vereist strikte voorwaarden voor onze heuristieken.

## 2. De Intuïtie
Stel je voor dat je een GPS gebruikt.
- Een "goede" GPS stuurt je niet zomaar naar het doel, maar berekent de route met de minste kilometers of tijd.
- Om dit te doen zonder elke mogelijke zijstraat in heel Europa te checken, gebruikt de GPS een schatting (heuristiek). Als die schatting de afstand naar het doel *nooit* te hoog inschat, zal de GPS nooit een kortere route over het hoofd zien.

## 3. Formele Structuur

### A. Admissibility (Toelaatbaarheid) - Voor Tree Search
Een heuristiek $h(n)$ is **admissible** als hij de kosten naar het doel nooit overschat:
$$0 \le h(n) \le h^*(n)$$
waarbij $h^*(n)$ de werkelijke minimale kosten zijn.
*   **Gevolg**: Als $h(n)$ admissible is, is A* optimaal voor **Tree Search**.

### B. Consistency (Consistentie / Monotoniciteit) - Voor Graph Search
Een heuristiek is **consistent** als voor elke node $n$ en elke opvolger $n'$ die bereikt wordt via actie $a$:
$$h(n) \le c(n, a, n') + h(n')$$
Dit betekent dat de geschatting naar het doel niet meer mag afnemen dan de werkelijke kosten van de stap die je net hebt gezet.
*   **Gevolg**: Elke consistente heuristiek is ook admissible. Consistentie is vereist om A* optimaal te maken voor **Graph Search** (waarbij we nodes in een `Explored Set` bijhouden).

### C. De rol van de f-waarde
In een optimaal zoekproces met een consistente heuristiek zijn de $f$-waarden ($f(n) = g(n) + h(n)$) langs elk pad **niet-dalend**. Dit zorgt ervoor dat we de zoekruimte in "contouren" van oplopende kosten verkennen.

## 4. Algoritme Verfijning: IDA*
**Iterative Deepening A* (IDA*)** combineert de ruimte-efficiëntie van DFS met de optimaliteit van A*. In plaats van een dieptelimiet (zoals bij IDS), gebruikt IDA* een **f-cost limiet**.

## 5. Examengerichte Focus
*   **Bewijs van Optimaliteit**: Kunnen uitleggen waarom A* een suboptimale node $G_2$ niet zal kiezen als er nog een optimale node $G$ op de frontier staat (mits $h$ admissible is).
*   **Consistentie Check**: Gegeven een graaf met $h$-waarden, kunnen bepalen of de heuristiek consistent is.
*   **Tree vs Graph Search**: Begrijpen waarom admissibility volstaat voor bomen, maar consistentie nodig is voor grafen met lussen.
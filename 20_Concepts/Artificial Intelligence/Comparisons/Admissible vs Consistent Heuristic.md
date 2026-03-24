---
type: concept-comparison
domain: "artificial-intelligence"
parent: Heuristic Properties
related:
  - Admissible Heuristic
  - Consistent Heuristic
  - A* Search
theme: "heuristic-properties-for-a-star"
aliases:
  - Admissible vs Consistent Heuristic
---

# Admissible vs Consistent Heuristic
#concept #ai

## Wat wordt hier vergeleken?
- [[Admissible Heuristic]]
- [[Consistent Heuristic]]

## Kernverschil
`Admissible` gaat over globale veiligheid: nooit de echte resterende kost overschatten. `Consistent` gaat over lokale samenhang: tussen twee verbonden nodes moet de heuristiek zich logisch gedragen.

## Vergelijking

| Aspect | Admissible | Consistent |
| --- | --- | --- |
| Kernidee | nooit overschatten | respecteert driehoeksvoorwaarde |
| Formule | `h(n) <= h*(n)` | `h(n) <= c(n,n') + h(n')` |
| Type eigenschap | globale ondergrens | lokale samenhang tussen buren |
| Belang voor A* | nodig voor optimaliteit | maakt `graph search` properder en sterker |
| Relatie | kan bestaan zonder consistentie | impliceert admissibility |
| Typische fout | denken dat de heuristiek exact moet zijn | denken dat consistent gewoon een synoniem is van admissible |

## Wanneer gebruik je wat?
- **Admissible:** als je wil aantonen dat `A*` de optimale oplossing kan vinden.
- **Consistent:** als je ook wil garanderen dat de heuristiek zich netjes gedraagt over overgangen in een graaf.

## Waarom is dit onderscheid belangrijk?
Deze twee eigenschappen liggen dicht bij elkaar, maar verklaren een ander aspect van `A*`: admissibility garandeert optimale eindoplossingen, terwijl consistentie het zoekproces zelf stabieler maakt.

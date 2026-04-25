---
type: examen-hulpmiddel
vak: Introduction to AI
status: actief
related:
  - 00_Centrale examensamenvatting
  - 01_Focus voor vrijdag
  - 02_Workflow met Bases
---

# Algoritmes herkennen aan code

> [!info]- Inhoudsopgave
> - [[#Korte kern]]
> - [[#1. Snelste herkenningsregel]]
> - [[#2. Herkenningsmatrix]]
> - [[#3. Compacte examtabel]]
> - [[#4. BFS herkennen]]
> - [[#5. DFS herkennen]]
> - [[#6. UCS herkennen]]
> - [[#7. Greedy herkennen]]
> - [[#8. A* herkennen]]
> - [[#9. Hill Climbing herkennen]]
> - [[#10. Meest gemaakte verwarringen]]
> - [[#11. Zeer korte herkenningssignalen]]
> - [[#12. Examensnelregel]]
> - [[#13. Handige vervolgnote]]

> **Examennuance:** Tijdens het examen wordt **Python alleen passief** ondervraagd. Je moet een fragment Python in de context van zoekalgoritmen kunnen interpreteren, maar je hoeft zelf geen programmeeroefening te schrijven. De codevragen testen je inzicht in de werking van het algoritme (zoals het beheer van de frontier), niet je schrijfvaardigheid.

Deze note helpt je snel herkennen welk zoekalgoritme je voor je hebt wanneer je Python-code, pseudocode of een korte implementatie ziet.

## Korte kern

- kijk eerst naar de gebruikte datastructuur
- kijk daarna naar de keuzeregel: diepte, `g(n)`, `h(n)` of `g(n)+h(n)`
- let op of het algoritme een volledige frontier bewaart of alleen de huidige node

## 1. Snelste herkenningsregel

Vraag altijd in deze volgorde:

1. Welke datastructuur zie ik?
2. Wordt er gekozen op `diepte`, `g`, `h` of `f = g + h`?
3. Houdt de code een volledige frontier bij of alleen een huidige toestand?

Als je die 3 dingen ziet, kan je meestal het algoritme meteen benoemen.

## 2. Herkenningsmatrix

| Wat je in code ziet | Waarschijnlijk algoritme |
| :--- | :--- |
| `deque`, `popleft()`, FIFO | [[Breadth-First Search (BFS)]] |
| lijst met `pop()` achteraan, LIFO | [[Depth-First Search (DFS)]] |
| `heapq` of priority queue op cumulatieve kost | [[Uniform-Cost Search (UCS)]] |
| `heapq` op alleen heuristische score | [[Greedy Best-First Search]] |
| `heapq` op `g + h` | [[A-star Search]] |
| alleen huidige node + beste buur | [[Hill Climbing]] |

## 3. Compacte examtabel

| Datastructuur / patroon | Score of keuzeregel | Algoritme | Typische val |
| :--- | :--- | :--- | :--- |
| `queue`, `deque`, `popleft()` | oudste open pad eerst | [[Breadth-First Search (BFS)]] | verwarren met goedkoopste pad bij ongelijke kosten |
| `stack`, lijst + `pop()` | laatst toegevoegd pad eerst | [[Depth-First Search (DFS)]] | denken dat eerste oplossing ook goed of optimaal is |
| `priority queue`, `heapq` | laagste `g(n)` | [[Uniform-Cost Search (UCS)]] | verwarren met BFS of te vroeg stoppen bij gegenereerd doel |
| `priority queue`, `heapq` | laagste `h(n)` | [[Greedy Best-First Search]] | denken dat doelgericht ook automatisch goedkoop betekent |
| `priority queue`, `heapq` | laagste `g(n) + h(n)` | [[A-star Search]] | `Greedy` verwarren met `A*` omdat beide heuristieken gebruiken |
| geen frontier, alleen `current` en buren | beste directe buur | [[Hill Climbing]] | denken dat dit gewoon `Greedy` zonder heap is |

## 4. BFS herkennen

Typische signalen:

- `deque`
- `popleft()`
- nieuwe paden of nodes worden achteraan toegevoegd
- geen prioriteit op kost of heuristiek

Typisch codepatroon:

```python
frontier = deque([[start]])
path = frontier.popleft()
frontier.append(path + [neighbor])
```

Kernidee:

- oudste open pad eerst
- dus zoeken in lagen

## 5. DFS herkennen

Typische signalen:

- gewone lijst als `stack`
- `pop()` zonder index
- nieuwe paden worden achteraan toegevoegd en ook achteraan weer genomen

Typisch codepatroon:

```python
stack = [[start]]
path = stack.pop()
stack.append(path + [neighbor])
```

Kernidee:

- laatst toegevoegd pad eerst
- dus snel diep in 1 tak

## 6. UCS herkennen

Typische signalen:

- `heapq` of `priority queue`
- tuples zoals `(cost, path)`
- `new_cost = cost + step_cost`
- keuze gebeurt op laagste cumulatieve kost

Typisch codepatroon:

```python
frontier = [(0, [start])]
cost, path = heapq.heappop(frontier)
new_cost = cost + step_cost
heapq.heappush(frontier, (new_cost, path + [neighbor]))
```

Kernidee:

- kiest op [[g(n)]]
- niet op diepte en niet op heuristiek

## 7. Greedy herkennen

Typische signalen:

- `heapq` of `priority queue`
- prioriteit is alleen `heuristic[node]`
- al gemaakte kost wordt niet opgeteld in de keuze

Typisch codepatroon:

```python
frontier = [(heuristic[start], [start])]
heapq.heappush(frontier, (heuristic[neighbor], path + [neighbor]))
```

Kernidee:

- kiest op [[h(n)]]
- doelgericht, maar niet voorzichtig

## 8. A* herkennen

Typische signalen:

- `heapq` of `priority queue`
- zowel echte kost als heuristiek zitten in de code
- prioriteit wordt berekend als `new_cost + heuristic[neighbor]`

Typisch codepatroon:

```python
new_cost = cost + step_cost
priority = new_cost + heuristic[neighbor]
heapq.heappush(frontier, (priority, new_cost, path + [neighbor]))
```

Kernidee:

- kiest op [[f(n)]] = [[g(n)]] + [[h(n)]]

## 9. Hill Climbing herkennen

Typische signalen:

- geen volledige frontier
- alleen `current` en `neighbors`
- kiest `best_neighbor`
- stopt als geen buur beter is

Typisch codepatroon:

```python
current = start
neighbors = graph.get(current, [])
best_neighbor = min(neighbors, key=lambda node: heuristic[node])
if heuristic[best_neighbor] >= heuristic[current]:
    return path
```

Kernidee:

- alleen lokale buurkeuze
- geen globale open lijst

## 10. Meest gemaakte verwarringen

- **BFS vs DFS:** kijk naar `queue` versus `stack`
- **UCS vs Greedy:** kijk of de code kiest op `g` of op `h`
- **Greedy vs A*:** kijk of `g` mee in de prioriteit zit
- **Greedy vs Hill Climbing:** kijk of er een volledige frontier is of alleen een huidige node met directe buren

## 11. Zeer korte herkenningssignalen

- **BFS:** `deque` + `popleft()`
- **DFS:** lijst + `pop()`
- **UCS:** `heapq` + `new_cost`
- **Greedy:** `heapq` + `heuristic[neighbor]`
- **A*:** `new_cost + heuristic[neighbor]`
- **Hill Climbing:** `current`, `neighbors`, `best_neighbor`

## 12. Examensnelregel

Als je twijfelt, schrijf letterlijk dit op kladpapier:

- `queue -> BFS`
- `stack -> DFS`
- `priority on g -> UCS`
- `priority on h -> Greedy`
- `priority on g+h -> A*`
- `current + best neighbor only -> Hill Climbing`

Dat is meestal genoeg om snel juist te zitten.

## 13. Handige vervolgnote

- [[Base - AI Examen Cockpit.base|Base - AI Examen Cockpit]]
- [[Breadth-First Search (BFS)]]
- [[Depth-First Search (DFS)]]
- [[Uniform-Cost Search (UCS)]]
- [[Greedy Best-First Search]]
- [[A-star Search]]
- [[Hill Climbing]]
- [[04_Frontier correct uitschrijven op papier|04_Frontier correct uitschrijven op papier]]

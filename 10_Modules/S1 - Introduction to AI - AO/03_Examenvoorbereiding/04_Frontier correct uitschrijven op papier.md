---
type: examen-hulpmiddel
vak: Introduction to AI
status: actief
related:
  - 00_Centrale examensamenvatting
  - 01_Focus voor vrijdag
  - 02_Workflow met Bases
  - 03_Algoritmes herkennen aan code
---

# Frontier correct uitschrijven op papier

> [!info]- Inhoudsopgave
> - [[#Korte kern]]
> - [[#1. Wat moet je altijd tonen?]]
> - [[#2. Veilige standaardvorm]]
> - [[#3. Breadth-First Search (BFS)]]
> - [[#4. Depth-First Search (DFS)]]
> - [[#5. Uniform-Cost Search (UCS)]]
> - [[#6. Greedy Best-First Search]]
> - [[#7. A* Search (A-Star)]]
> - [[#8. Hill Climbing (Lokale Search)]]
> - [[#9. Examen Tips (Tie-Breakers & Stoppen)]]
> - [[#10. Mini-checklist voor je antwoord]]
> - [[#11. Handige vervolgnote]]

Deze note toont hoe je op examen je frontier stap voor stap correct uitschrijft, en welke datastructuur elk algoritme daarvoor gebruikt. Door deze regels te volgen verlies je geen punten op procedurefouten.

## Korte kern
- **BFS:** Queue (FIFO) - toevoegen achteraan, nemen vooraan.
- **DFS:** Stack (LIFO) - toevoegen bovenaan, nemen bovenaan.
- **UCS, Greedy, A*:** Priority Queue - lijst steeds sorteren op prioriteit.
- **Actie:** Schrijf altijd exact 1 expansiestap per regel uit!

## 1. Wat moet je altijd tonen?

Bij frontier-gebaseerde algoritmes schrijf je best altijd:
1. de huidige frontier
2. welke node of welk pad gekozen wordt
3. welke opvolgers gegenereerd worden
4. hoe de frontier er na de update uitziet
5. welke score telt: diepte, `g`, `h` of `f`

Voor `Hill Climbing` schrijf je geen volledige frontier uit, maar wel:
- huidige node
- directe buren met heuristiek
- beste buur
- reden van keuze

## 2. Veilige standaardvorm

Gebruik op papier telkens dit patroon:

```text
Stap 0: Frontier = [...]
Kies: ...
Genereer: ...
Nieuwe frontier = [...]
```

## 3. Breadth-First Search (BFS)
- **Datastructuur:** [[Queue]] (First In, First Out)
- **Selectieregel:** Oudste element eerst (vooraan de lijst).
- **Toevoegen:** Nieuwe buren komen **achteraan** in de lijst. De lijst wordt _nooit_ gesorteerd.

**Typisch patroon:**
```text
Queue = [A]
Kies: A (neem vooraan)
Genereer: B, C (voeg achteraan toe)
Nieuwe Queue = [A-B, A-C]
```
_Fout die vaak gebeurt:_ de nieuwe nodes vooraan zetten in plaats van achteraan.

## 4. Depth-First Search (DFS)
- **Datastructuur:** [[Stack]] (Last In, First Out)
- **Selectieregel:** Meest recente element eerst (vooraan de lijst / bovenaan de stapel).
- **Toevoegen:** Nieuwe buren komen **vooraan** in de lijst. Vaak voeg je ze in omgekeerde volgorde (bijv. C, dan B) toe zodat de gewenste (B) bovenaan ligt. De lijst wordt _nooit_ gesorteerd.

**Typisch patroon:**
```text
Stack = [A]
Kies: A (neem bovenaan)
Genereer: B, C (push C, dan push B)
Nieuwe Stack = [A-B, A-C]
```
_Fout die vaak gebeurt:_ de buurvolgorde niet vermelden en daardoor later een andere tak volgen dan je eerst bedoelde.

## 5. Uniform-Cost Search (UCS)
- **Datastructuur:** [[Priority Queue]]
- **Selectieregel:** Laagste actuele kost ($g(n)$).
- **Toevoegen:** Nieuwe buren toevoegen en direct **sorteren** op basis van $g(n)$. Laagste waarde komt vooraan.

**Typisch patroon:**
```text
Priority Queue = [A (g=0)]
Kies: A (g=0)
Genereer: B (g=2), C (g=5)
Nieuwe Priority Queue = [A-B (g=2), A-C (g=5)] 
```
_Fout die vaak gebeurt:_ frontier tekenen alsof ze op diepte geordend is in plaats van op kost.

## 6. Greedy Best-First Search
- **Datastructuur:** [[Priority Queue]]
- **Selectieregel:** Laagste heuristische schatting ($h(n)$).
- **Toevoegen:** Nieuwe buren toevoegen en direct **sorteren** op basis van $h(n)$. De actuele kost ($g(n)$) speelt _geen_ rol.

**Typisch patroon:**
```text
Priority Queue = [A (h=6)]
Kies: A (h=6)
Genereer: B (h=4), C (h=1)
Nieuwe Priority Queue = [A-C (h=1), A-B (h=4)]  <- Let op: C staat nu vooraan!
```
_Fout die vaak gebeurt:_ stiekem `g(n)` laten meespelen terwijl dat niet hoort.

## 7. A* Search (A-Star)
- **Datastructuur:** [[Priority Queue]]
- **Selectieregel:** Laagste totale geschatte kost ($f(n) = g(n) + h(n)$).
- **Toevoegen:** Nieuwe buren toevoegen en direct **sorteren** op basis van $f(n)$. Vermeld best altijd $g$, $h$ en $f$ om rekenfouten te voorkomen.

**Typisch patroon:**
```text
Priority Queue = [A (g=0, h=6, f=6)]
Kies: A (f=6)
Genereer: B (g=2, h=4, f=6), C (g=5, h=1, f=6)
Nieuwe Priority Queue = [A-B (f=6), A-C (f=6)]
```
_Fout die vaak gebeurt:_ alleen `h` noteren en zo per ongeluk `Greedy` uitvoeren.

## 8. Hill Climbing (Lokale Search)
- **Datastructuur:** Geen (werkt alleen met de huidige node en zijn directe buren).
- **Selectieregel:** Buur met de beste heuristische score ($h(n)$) die _beter_ is dan de huidige node.
- **Toevoegen:** Geen lijst om bij te houden. Lokaal de beste buur kiezen en direct doorgaan.

**Typisch patroon:**
```text
Huidig = A (h=6)
Buren = B (h=4), C (h=5)
Kies: B (h=4 is beter dan h=6)
Nieuwe huidige node = B
```
_Fout die vaak gebeurt:_ een volledige frontier construeren, terwijl Hill Climbing alleen lokaal kiest.

## 9. Examen Tips (Tie-Breakers & Stoppen)

1. **Wanneer stoppen?**
   - Een veelgemaakte fout op het examen is te vroeg stoppen. Het algoritme stopt pas wanneer de doelknoop (Goal) **gekozen/verwijderd** wordt uit de Frontier, **niet** wanneer hij er voor het eerst aan wordt toegevoegd (gegenereerd). Dit is extreem belangrijk bij UCS, Greedy en A*.

2. **Tie-Breakers**
   - Als elementen in een Queue, Stack of Priority Queue een **gelijke prioriteit** (of gelijke waarden) hebben, vermeld dan altijd je **Tie-Breaker** regel bovenaan je blad.
   - Voorbeeld: *"Tie-break: bij gelijke waarden / opties kies ik alfabetisch."*
   - Maak dit zichtbaar in je uitwerking als de situatie zich voordoet.

3. **Consistentie**
   - Schrijf altijd exact 1 expansiestap per regel/blokje uit.
   - Maak duidelijk welke specifieke node je kiest en welke buren dat oplevert.

## 10. Mini-checklist voor je antwoord

Voor je doorschuift naar de volgende stap, check:
- [ ] staat de frontier correct geordend?
- [ ] heb ik exact 1 keuze gemaakt?
- [ ] heb ik alle nieuwe kandidaten toegevoegd?
- [ ] heb ik `g`, `h` of `f` genoteerd waar nodig?
- [ ] heb ik nog niet te vroeg gestopt?

## 11. Handige vervolgnote
- [[03_Algoritmes herkennen aan code|03_Algoritmes herkennen aan code]]
- [[Breadth-First Search (BFS)]]
- [[Depth-First Search (DFS)]]
- [[Uniform-Cost Search (UCS)]]
- [[Greedy Best-First Search]]
- [[A-star Search]]
- [[Hill Climbing]]

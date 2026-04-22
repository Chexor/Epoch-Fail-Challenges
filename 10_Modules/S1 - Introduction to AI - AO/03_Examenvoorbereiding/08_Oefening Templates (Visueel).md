---
type: examen-template
vak: Introduction to AI
status: actief
---
# Visuele Oefening Templates

> [!info]- Inhoudsopgave
> - [[#Template 1: Grid Search (Doofhof, BFS/DFS)]]
> - [[#Template 2: Graph Search met Gewichten (UCS / Greedy / A*)]]
> - [[#Template 3: State Space Formulering (bv. Water Jugs)]]
> - [[#Template 4: Hoe je het Finale Antwoord Noteert op het Examen]]

Teken tijdens je examen dit soort schema's op je kladpapier voor maximale overzichtelijkheid en foutreductie bij het uitvoeren van zoekalgoritmen.

## Template 1: Grid Search (Doofhof, BFS/DFS)
Bij Grid Searches (waar nodes coördinaten zijn zoals `(5,3)`) worden de rijen vaak te lang als je het hele pad uitschrijft. Gebruik deze compacte tabel:

| Stap | Gekozen Node (Pop) | Buren Genereren (Volgens richting) | Nieuwe Queue/Stack |
| :--- | :--- | :--- | :--- |
| 0 | - | Start: `(5,3)` | `[(5,3)]` |
| 1 | `(5,3)` | Up:`(4,3)`, Right:`(5,4)`, Down:`(6,3)` | `[(4,3), (5,4), (6,3)]` |
| 2 | `(4,3)` | Left:`(4,2)`, Right:`(4,4)` | `[(4,2), (4,4), (5,4), (6,3)]` |

*Let op: In een Queue voeg je buren rechts toe (FIFO). In een Stack voeg je buren links toe (LIFO) in **omgekeerde volgorde** van je richtingsregels!*

---

## Template 2: Graph Search met Gewichten (UCS / Greedy / A*)
Bij grafen met heuristieken ($h$) en stapkosten ($g$) is het cruciaal dat je het hele pad in je Priority Queue (PQ) bewaart, anders vergeet je cumulatieve kosten.

| Huidige PQ (gesorteerd) | Gekozen Pad (Pop) | Genereer Buren (Nieuwe Paden) | Berekening Score (g, h, f) |
| :--- | :--- | :--- | :--- |
| `[ A (f=6) ]` | `A` | `A-B` <br> `A-C` | `g=2, h=4 -> f=6` <br> `g=4, h=5 -> f=9` |
| `[ A-B (f=6), A-C (f=9) ]` | `A-B` | `A-B-D` <br> `A-B-E` | `g(2+2=4), h=6 -> f=10` <br> `g(2+5=7), h=1 -> f=8` |
| `[ A-B-E (f=8), A-C (f=9), A-B-D (f=10) ]` | `A-B-E` | `A-B-E-G` | `g(7+2=9), h=0 -> f=9` |
| `[ A-C (f=9), A-B-E-G (f=9), A-B-D (f=10) ]`| `A-B-E-G` (DOEL!) | STOP! | Eindkost: 9 |

*Sorteer na élke stap je PQ op de relevante waarde (`g` voor UCS, `h` voor Greedy, `f` voor A*). Alfabetisch bij gelijke score!*

---

## Template 3: State Space Formulering (bv. Water Jugs)
Soms moet je zelf de structuur uitschrijven voor een raadsel:

1. **State:** Definieer wat een "node" is (bijv. `[inhoud 4L, inhoud 3L]`).
2. **Start State:** Bijv. `[0, 0]`
3. **Goal State:** Bijv. `[2, y]`
4. **Regels (Operators):**
   - R1: Vul kruik 1 (Als leeg -> 4L)
   - R2: Leeg kruik 2 (Als vol -> 0L)
   - R3: Giet kruik 2 in kruik 1 (Als ruimte -> bereken som)
5. **Algoritme toepassen:** Gebruik de nodes `[0,0]` in Template 1 of 2 alsof het gewone letters waren in een graaf.

---
## Template 4: Hoe je het Finale Antwoord Noteert op het Examen

Naast het uitschrijven van je Frontier/Queue, moet je vaak een expliciet antwoord geven. Docenten zoeken naar specifieke elementen. Gebruik dit stramien om geen domme punten te verliezen:

**Vraag: Geef het pad dat algoritme X vindt van S naar G.**

**Mijn Antwoord:**
1. **Gevonden Pad:** `S -> A -> B -> G`
2. **Totale Kost (indien relevant voor UCS/A*):** `14`
3. **Aantal Geëxpandeerde Nodes:** `4` (S, A, B en G)
4. **Korte Verantwoording (Optioneel maar veilig):** "Gekozen via A* omdat $f(G) = 14$ de laagste waarde in de Priority Queue was op het moment van expansie."

*Let op: "Geëxpandeerde nodes" zijn de nodes die je daadwerkelijk uit je Queue hebt gehaald (ge-popt) om hun buren te bekijken, NIET alle nodes die ooit in je Queue hebben gestaan!*

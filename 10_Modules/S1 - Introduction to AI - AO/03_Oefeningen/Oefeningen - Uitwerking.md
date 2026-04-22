# Opdracht 1: Basic Search

Given the following figure, find a path from the square labeled with S to the square labeled with G, without passing through the black squares.
Legal steps (in this order): **up, left, right, down** (each to an adjacent square).
## Depth first

|       |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |
| :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| **0** | 18  | 17  | 16  | 15  | 14  | 13  | 12  | 11  |
| **1** | 20  | 19  | 21  |     |     |     |     | 10  |
| **2** |     |     |  G (22)  |     |     |     |     |  9  |
| **3** |     |     |  ■  |  ■  |  ■  |  ■  |  ■  |  8  |
| **4** |     |  ■  |  3  |  2  |  4  |  5  |  6  |  7  |
| **5** |     |     |  ■  |  S (1)  |     |     |  ■  |     |
| **6** |     |     |     |     |     |     |     |     |
| **7** |     |     |     |     |     |     |     |     |

## Breadth First

|       |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |
| :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| **0** |     |     |     |     |     |     |     |     |
| **1** |     |     |  ↓  |  ←  |  ←  |  ←  |  ←  |  ←  |
| **2** |     |     |  G  |     |     |     |     |  ↑  |
| **3** |     |     |  ■  |  ■  |  ■  |  ■  |  ■  |  ↑  |
| **4** |     |  ■  |     |  →  |  →  |  →  |  →  |  ↑  |
| **5** |     |     |  ■  |  ↑  |     |     |  ■  |     |
| **6** |     |     |     |     |     |     |     |     |
| **7** |     |     |     |     |     |     |     |     |

<table>
  <tr><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td></td><td style="background: green;">G</td><td></td><td></td><td></td></tr>
  <tr><td></td><td style="background: black;"></td><td style="background: black;"></td><td style="background: black;"></td><td></td></tr>
  <tr><td></td><td></td><td style="background: blue; color: white;">S</td><td></td><td></td></tr>
</table>
## Opdracht 2: Heuristic Search

## Opdracht 3: Optimal Search


# H4: Kansberekening

## ✅ SSOT
- Dit is de **authoritative** hoofdstuknote voor H4.
- Afgeleide samenvattingen moeten hiernaar linken.

## 1. Basisbegrippen
- **Universum $U$:** verzameling van alle mogelijke uitkomsten.
- **Gebeurtenis $A$:** deelverzameling van $U$.
- **Zekere gebeurtenis:** $U$.
- **Lege gebeurtenis:** $\varnothing$.
- **Elementaire gebeurtenis:** één uitkomst (singleton).

### Soorten universa
- **Eindig:** telbaar aantal uitkomsten.
- **Aftelbaar oneindig:** uitkomsten zijn te ordenen (bv. $\mathbb{N}$).
- **Overaftelbaar:** niet te ordenen (bv. $[0,1]$).

## 2. Bewerkingen met gebeurtenissen
- **Unie:** $A \cup B$ (A of B).
- **Doorsnede:** $A \cap B$ (A en B).
- **Verschil:** $A \setminus B$ (A maar niet B).
- **Complement:** $A^c$ (niet A).
- **Disjunct:** $A \cap B = \varnothing$.

### De Morgan
- $(A \cup B)^c = A^c \cap B^c$.
- $(A \cap B)^c = A^c \cup B^c$.

## 3. Frequenties en kans
- **Absolute frequentie:** $f(A)$ = aantal keer dat $A$ optreedt.
- **Relatieve frequentie:** $h(A) = \frac{f(A)}{n}$.

### Eigenschappen relatieve frequentie
- $0 \le h(A) \le 1$.
- $h(U)=1$.
- Als $A \cap B=\varnothing$: $h(A \cup B)=h(A)+h(B)$.

### Statistische stabiliteit
- Als $n$ stijgt, stabiliseert $h(A)$ rond een vaste waarde $P(A)$.

## 4. Kansen en axioma's
- **Axioma 1:** $P(A) \ge 0$.
- **Axioma 2:** $P(U)=1$.
- **Axioma 3:** als $A \cap B=\varnothing$ dan $P(A \cup B)=P(A)+P(B)$.

### Uniforme kansverdeling
- Alle elementaire gebeurtenissen hebben dezelfde kans.
- In een eindig uniform universum met $n$ uitkomsten: $P(\{u\})=\frac{1}{n}$.

### Regel van Laplace (eindig en uniform)
- Als $A$ $k$ elementen heeft in $U$ met $n$ elementen:
  - $P(A)=\frac{k}{n}$.
- Let op: dit geldt **niet** bij een niet-uniforme uitkomstenverzameling.

## 5. Kansregels
- **Complementregel:** $P(A^c)=1-P(A)$.
- **Verschilregel:** $P(A\setminus B)=P(A)-P(A \cap B)$.
- **Somregel:** $P(A \cup B)=P(A)+P(B)-P(A \cap B)$.

### Productregel (onafhankelijk)
- $A$ en $B$ onafhankelijk $=> P(A \cap B)=P(A)P(B)$.

## 6. Voorwaardelijke kansen
- **Definitie:** $P(B|A)=\frac{P(A \cap B)}{P(A)}$ (als $P(A)>0$).
- **Algemene productregel:** $P(A \cap B)=P(A)P(B|A)$.

### Totale kans
- Als $\{O_i\}$ een verdeling van $U$ is:
  - $P(A)=\sum_i P(O_i)P(A|O_i)$.

### Formule van Bayes
- $P(O_k|A)=\frac{P(O_k)P(A|O_k)}{\sum_i P(O_i)P(A|O_i)}$.

## 7. Veelgemaakte fouten
- **Uniformiteit vergeten:** Laplace werkt alleen bij gelijke kansen.
- **Kans \u2260 relatieve frequentie:** kans is theoretisch, frequentie is empirisch.
- **Afhankelijkheid negeren:** $P(A \cap B) != P(A)P(B)$ als gebeurtenissen afhangen.

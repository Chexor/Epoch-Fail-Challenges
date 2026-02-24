# H1: Frequentieverdelingen & Grafische Voorstelling

## ✅ SSOT
- Dit is de **authoritative** hoofdstuknote voor H1.
- Afgeleide samenvattingen moeten hiernaar linken.

## 1. Basisbegrippen
- **Populatie:** De volledige groep (personen, dieren, objecten) waarover je iets wil weten. Zie [[Populatie vs Steekproef]].
- **Steekproef:** Een (kleine) deelverzameling van de populatie.
- **Representativiteit:** Een steekproef is representatief *als en slechts als* elk element van de populatie dezelfde kans heeft om geselecteerd te worden.
  - *Random:* Willekeurige selectie.
  - *Gestratificeerd:* Opdelen in subgroepen (bv. m/v) en verhoudingsgewijs trekken.
  - *Getrapt:* Subpopulaties -> kleinere delen (bv. provincie -> gemeente -> straat).
  - *Systematisch:* Elk n-de element (bv. aan de lopende band).

## 2. Statistische Variabelen
Het correct classificeren van variabelen is cruciaal voor de keuze van je analyse/grafiek. Zie [[Meetniveaus]].

| Hoofdtype | Subtype | Kenmerk | Voorbeeld |
| :--- | :--- | :--- | :--- |
| **Kwalitatief** (Eigenschap) | **Nominaal** | Geen logische volgorde | Kleur, Land, Geslacht |
| | **Ordinaal** | Wel logische volgorde | Hotelsterren, Opleidingsniveau (Lager/Sec/Hoger) |
| **Kwantitatief** (Getal) | **Discreet** | Tellen (gehele getallen) | Aantal kinderen, Aantal fouten |
| | **Continu** | Meten (reële getallen) | Lengte, Gewicht, Tijd |

*> Extra onderscheid bij Kwantitatief:*
- **Ratio:** Natuurlijk nulpunt (0 betekent "niets"). Bv. Lengte (0m bestaat niet/is niets).
- **Interval:** Geen natuurlijk nulpunt. Bv. Temperatuur (0°C is niet "geen temperatuur").

## 3. Frequentieverdelingen

### A. Discrete Verdeling
- **Tabel:** Lijst van waarden ($x_i$) met hun absolute frequentie ($n_i$) of relatieve frequentie ($f_i$).
- **Grafiek:** **Staafdiagram** (staven staan los van elkaar).

### B. Continue Verdeling (Klassen)
- **Klassen:** Groeperen van waarden in intervallen $[a, b[$.
- **Klassenbreedte:** Verschil tussen boven- en ondergrens.
- **Klassenmidden ($m_i$):** $(Ondergrens + Bovengrens) / 2$.
  - *Let op:* Open klassen (bv. "> 100") hebben geen midden!

## 4. Grafische Voorstellingen (Continu)

### **Histogram**
- Aaneensluitende blokken.
- **Breedte:** Klassebreedte.
- **Oppervlakte:** Totaal aantal waarnemingen ($n$ of $1$).

### **Frequentiepolygoon**
- Lijn die de **klassenmiddens** verbindt.
- **Belangrijk:** Start en eindig met "staartjes" naar de x-as (zodat de oppervlakte gesloten is).
- Oppervlakte onder de lijn = Oppervlakte histogram.

### **Ogief (Sompolygoon)**
- Voor **cumulatieve** frequenties (niet gewone!).
- Toont "hoeveel procent is kleiner dan x?".
- **Startpunt:** Ondergrens van de eerste klasse (0%).
- **Eindpunt:** Bovengrens van de laatste klasse (100%).
- Handig om **kwartielen** af te lezen.

### **Boxplot** (Zie [[Boxplot]])
Visuele samenvatting van 5 getallen:
1.  **Min** (of grens voor uitschieters)
2.  **Q1** (25%)
3.  **Mediaan** (50%)
4.  **Q3** (75%)
5.  **Max** (of grens voor uitschieters)

---
type: concept-topic
domain: "discrete-mathematics"
parent: "Discrete Number Operations"
related:
  - Discrete Number Operations
  - Modulorekenen
  - Modulaire inverse
theme: "discrete-structures-and-stepwise-reasoning"
aliases:
  - Staartdeling (Long Division)
---

# Staartdeling (Long Division)
#concept #wiskunde

## 1. Wat is het kernprobleem?
Een staartdeling beantwoordt de vraag: "Hoe kan ik een groot getal systematisch delen door een kleiner getal, op een manier die altijd werkt, zelfs als je het niet uit je hoofd kunt?" Het breekt een complexe deling op in kleine, herhaalbare stappen.

## 2. Intuïtieve uitleg
Stel je voor dat je 125 snoepjes hebt en je wilt ze eerlijk verdelen over 4 vrienden.

1.  Je kijkt eerst naar het eerste cijfer: '1'. Kun je 1 snoepje verdelen over 4 vrienden? Nee.
2.  Je neemt het volgende cijfer erbij: '12'. Kun je 12 snoepjes verdelen? Ja. Elke vriend krijgt 3 snoepjes (3 x 4 = 12). Je hebt nu 0 snoepjes over van die 12.
3.  Nu kijk je naar de snoepjes die je nog niet hebt bekeken: de '5'. Je hebt nog 5 snoepjes.
4.  Kun je die 5 snoepjes verdelen over 4 vrienden? Ja. Iedereen krijgt er 1. Je hebt dan 1 snoepje over (de "rest").

Uiteindelijk heeft elke vriend 30 + 1 = 31 snoepjes gekregen, en er blijft 1 snoepje over dat je niet kon verdelen.

## 3. Formele structuur
Een staartdeling volgt een vast algoritme: **Delen, Vermenigvuldigen, Aftrekken, Omlaag halen**.

- **Deeltal**: Het getal dat gedeeld wordt (bv. 125).
- **Deler**: Het getal waardoor je deelt (bv. 4).
- **Quotiënt**: De uitkomst (bv. 31).
- **Rest**: Wat overblijft (bv. 1).

**Voorbeeld: 125 / 4**

```
   31   (Quotiënt)
  ---
4/125   (Deler / Deeltal)
  12
  --
   05
    4
    -
    1   (Rest)
```

**Stappen:**
1.  **Delen**: Hoe vaak past 4 in 12? **3** keer. Schrijf 3 boven de 2.
2.  **Vermenigvuldigen**: 3 * 4 = **12**. Schrijf 12 onder de 12.
3.  **Aftrekken**: 12 - 12 = **0**.
4.  **Omlaag halen**: Haal het volgende cijfer (5) naar beneden. Je hebt nu 05, ofwel 5.
5.  **Herhaal**:
    - **Delen**: Hoe vaak past 4 in 5? **1** keer. Schrijf 1 naast de 3.
    - **Vermenigvuldigen**: 1 * 4 = **4**. Schrijf 4 onder de 5.
    - **Aftrekken**: 5 - 4 = **1**.
    - **Omlaag halen**: Er zijn geen cijfers meer om omlaag te halen.
6.  **Conclusie**: De deling is klaar. De uitkomst (quotiënt) is 31 met een rest van 1.

## 4. Toepassing
Een staartdeling is fundamenteel in de wiskunde en informatica.
- **Rekenen**: Voor handmatige delingen die te moeilijk zijn voor hoofdrekenen.
- **Algebra**: Hetzelfde principe wordt gebruikt voor het delen van veeltermen (polynoomdeling). Dit is een belangrijk concept in vakken als Problem Solving.
- **Programmeren**: De modulo-operator (`%`) die in veel programmeertalen de rest van een deling geeft, is gebaseerd op dit principe.

## 5. Examengerichte vertaling
- **Typische vraag:** "Deel 2548 door 12 zonder rekenmachine."
- **Vaak gemaakte fout:** Vergeten een '0' in het quotiënt te plaatsen als de deler niet in het nieuwe getal past. Bijvoorbeeld, bij 412 / 4, na 4-4=0 haal je de 1 omlaag. 4 past 0 keer in 1, dus je moet een 0 in het antwoord schrijven voor je de 2 omlaag haalt.
- **Link met andere concepten:** [[Veeltermen]], [[Modulo Rekenen]].

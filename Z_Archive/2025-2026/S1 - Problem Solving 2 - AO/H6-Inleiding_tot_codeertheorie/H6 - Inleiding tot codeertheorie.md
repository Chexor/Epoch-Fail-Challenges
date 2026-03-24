# H6 - Inleiding tot codeertheorie

[[Problem Solving 2 - Overzicht]]

## A. Wat is het kernprobleem?

Hoe kunnen we informatie (tekst, data) zo omzetten dat we het veilig kunnen versturen zonder dat onbevoegden het kunnen lezen (**encryptie**), en hoe kunnen we controleren of een ontvangen boodschap correct is en geen fouten bevat (**foutendetectie**)?

Dit hoofdstuk focust op de wiskundige principes hierachter, met name **getaltheorie** en **modulorekenen**.

## B. Intuïtieve uitleg

Stel je "klokrekenen" voor. Op een klok is 15 uur hetzelfde als 3 uur. We rekenen "modulo 12". Dit simpele idee is de basis van moderne cryptografie. Door te rekenen met de *rest na deling* door een (zeer groot) getal, creëren we een wiskundig systeem met unieke eigenschappen.

-   **Foutendetectie (bv. IBAN):** Je bankrekeningnummer bevat een controlegetal. Dat getal wordt berekend uit de andere cijfers met een modulo-operatie. Als je één cijfer verkeerd intypt, zal de berekening niet meer kloppen en weet het systeem dat het nummer ongeldig is.
-   **Encryptie (bv. RSA):** Dit is het geniale. Je gebruikt twee sleutels: een **publieke sleutel** die iedereen mag kennen om een bericht voor jou te versleutelen, en een **geheime privésleutel** die alleen jij hebt om het te ontcijferen. Het is alsof je een open hangslot (publieke sleutel) naar iemand stuurt. Iedereen kan het dichtklikken, maar alleen jij hebt de sleutel om het weer te openen. De veiligheid hangt af van het feit dat het extreem moeilijk is om uit het publieke hangslot de geheime sleutel af te leiden.

## C. Formele structuur

### 1. Getaltheorie: de bouwstenen

-   **Deelbaarheid:** `a | b` betekent "a is een deler van b".
-   **Priemgetal:** Een getal groter dan 1 dat enkel deelbaar is door 1 en zichzelf.
-   **Grootste Gemene Deler (ggd):** Het grootste getal dat twee andere getallen deelt.
-   **Algoritme van Euclides:** Een efficiënt stappenplan om de `ggd` van twee getallen te vinden, zonder ze in priemfactoren te moeten ontbinden. Dit is een fundamenteel algoritme.

### 2. Modulorekenen ("Klokrekenen")

-   **Congruentie:** `a ≡ b (mod n)` betekent "`a` en `b` hebben dezelfde rest na deling door `n`".
    -   Bv. `15 ≡ 3 (mod 12)`
-   **Rekenen:** Je kan met deze 'restklassen' optellen, aftrekken en vermenigvuldigen alsof het gewone getallen zijn.
-   **Inverse:** De 'inverse' van een getal `a` (mod `n`) is een getal `x` zodat `a*x ≡ 1 (mod n)`. Dit is de basis voor "delen" in modulorekenen.
    -   Een inverse bestaat **als en slechts als** `ggd(a, n) = 1` (a en n zijn "relatief priem").

### 3. De Stelling van Euler en de φ-functie

-   **φ-functie (phi):** `φ(n)` telt hoeveel getallen kleiner dan `n` relatief priem zijn met `n`.
-   **Stelling van Euler:** Als `ggd(a, n) = 1`, dan geldt: **`a^φ(n) ≡ 1 (mod n)`**.
-   **Gevolg:** Deze stelling geeft ons een directe manier om de inverse van `a` te vinden: `a^(φ(n)-1)`. Dit is cruciaal voor RSA.

### 4. RSA-encryptie: het stappenplan

1.  **Sleutelgeneratie (geheim):**
    -   Kies twee gigantisch grote priemgetallen, `p` en `q`.
    -   Bereken de **modulus** `n = p * q`.
    -   Bereken `φ(n) = (p-1)(q-1)`.
2.  **Sleutels bepalen:**
    -   Kies een **publieke exponent** `e` die relatief priem is met `φ(n)`.
    -   Bereken de **privé-exponent** `d` als de inverse van `e` modulo `φ(n)`.
    -   De **publieke sleutel** is `(n, e)`. Iedereen mag deze weten.
    -   De **privésleutel** is `d`. Deze houd je absoluut geheim. Gooi `p`, `q` en `φ(n)` weg.
3.  **Versleutelen (door zender):**
    -   Zet het bericht `B` om in een getal.
    -   Bereken het versleutelde bericht `C` met: **`C = B^e (mod n)`**.
4.  **Ontcijferen (door ontvanger):**
    -   Bereken het originele bericht `B` met: **`B = C^d (mod n)`**.

De veiligheid van RSA steunt op het feit dat het, zelfs met `n` en `e` bekend, praktisch onmogelijk is om `d` te berekenen zonder de originele priemfactoren `p` en `q` te kennen. En een groot getal `n` ontbinden in zijn priemfactoren is een extreem moeilijk wiskundig probleem.

## D. Toepassing: Codeertechniek van Hill

Dit is een (minder veilige) toepassing van matrices in de cryptografie, die in de syllabus wordt aangehaald.

-   **Idee:** Gebruik een inverteerbare vierkante matrix `S` (de 'sleutel') om een bericht te coderen.
-   **Coderen:** Zet het bericht om in getallen, verdeel het in blokken (vectoren), en vermenigvuldig elk blok met de sleutelmatrix `S`.
-   **Decoderen:** Vermenigvuldig de ontvangen blokken met de **inverse** van de sleutelmatrix, `S⁻¹`.

## E. Examengerichte vertaling

-   **Focus:** Je moet het **algoritme van Euclides** kunnen toepassen om een `ggd` te vinden en om de inverse in modulorekenen te bepalen. Het stappenplan van RSA is belangrijk om te begrijpen.
-   **Typische Vragen:**
    -   "Bereken `ggd(a, b)` met het algoritme van Euclides."
    -   "Schrijf `ggd(a, b)` als een lineaire combinatie van `a` en `b`." (Dit volgt uit de stappen van Euclides).
    -   "Bereken de inverse van `a` modulo `n`."
    -   Een RSA-vraagstuk met (zeer) kleine getallen, waarbij je de stappen moet doorlopen:
        -   Gegeven `p` en `q`, bereken `n` en `φ(n)`.
        -   Gegeven `e`, bereken `d`.
        -   Gegeven een bericht `B`, versleutel het naar `C`.
        -   Gegeven een versleuteld bericht `C`, ontcijfer het naar `B`.
-   **Software (`wxMaxima`):** `wxMaxima` heeft krachtige ingebouwde functies voor getaltheorie die het RSA-proces sterk vereenvoudigen.
    -   `gcd(a, b)`: Berekent de grootste gemene deler.
    -   `inv_mod(a, n)`: Berekent de inverse van `a` modulo `n`. Essentieel om de privé-exponent `d` te vinden uit `e` en `φ(n)`.
    -   `totient(n)`: Berekent de `φ(n)` (phi-functie van Euler).
    -   `power_mod(B, e, n)`: Berekent `B^e (mod n)` op een zeer efficiënte manier, zelfs voor grote getallen. Dit is de kern van het versleutelen en ontcijferen.
    -   `factor(n)`: Ontbindt een getal `n` in zijn priemfactoren. (De reden waarom RSA veilig is, is omdat dit voor zeer grote `n` ondoenbaar lang duurt).

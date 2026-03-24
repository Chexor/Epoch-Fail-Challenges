# Uitleg Oefening 7: Decoderingscomponent `d` berekenen

Deze notitie legt stap voor stap uit hoe je de decoderingscomponent (privésleutel) `d` van een RSA-code berekent, gebaseerd op de volgende opgave:

> **Opgave:** Bereken de decoderingscomponent `d` bij een RSA-code als je weet dat de publieke sleutel wordt gegeven door 14077 en 1931. Maak hiervoor gebruik van het algoritme van Euclides.

---

## Stap 1: Identificeer de publieke sleutel (n, e)

Een publieke RSA-sleutel bestaat uit twee getallen:
- **`n`**: de modulus. Dit is het product van twee (geheime) priemgetallen.
- **`e`**: de publieke exponent.

Per conventie is `n` het grootste van de twee getallen.
- `n = 14077`
- `e = 1931`

**wxMaxima commando's:**
```wxmx
n: 14077;
e: 1931;
```

## Stap 2: Ontbind de modulus `n` in priemfactoren

Om `d` te kunnen berekenen, hebben we de waarde `φ(n)` (de phi-functie van Euler) nodig. Hiervoor moeten we eerst `n` ontbinden in zijn twee priemfactoren, `p` en `q`.

We zoeken dus twee priemgetallen `p` en `q` zodat `p * q = 14077`.

**wxMaxima commando:**
In `wxMaxima` kunnen we de `factor()` functie gebruiken:
```wxmx
factor(n);
/* Output: 101*139 */
```

De priemfactoren zijn dus:
- `p = 101`
- `q = 139`

## Stap 3: Bereken φ(n)

Nu we `p` en `q` kennen, kunnen we `φ(n)` eenvoudig berekenen met de formule:
`φ(n) = (p - 1) * (q - 1)`

Invullen geeft:
`φ(n) = (101 - 1) * (139 - 1) = 100 * 138 = 13800`

**wxMaxima commando's:**
```wxmx
p: 101;
q: 139;
phi_n: (p - 1) * (q - 1);
/* Output: 13800 */

/* Alternatief met de ingebouwde functie: */
totient(n);
/* Output: 13800 */
```

## Stap 4: Bereken `d` met het uitgebreide algoritme van Euclides

De privésleutel `d` is de **modulaire inverse** van `e` modulo `φ(n)`. Dit betekent dat we op zoek zijn naar een getal `d` waarvoor geldt:
`e * d ≡ 1 (mod φ(n))`
`1931 * d ≡ 1 (mod 13800)`

### Manuele Methode (zoals gevraagd in de opgave)

**1. Algoritme van Euclides (staartdeling):**
```
13800 = 7 * 1931 + 283
1931  = 6 * 283  + 233
283   = 1 * 233  + 50
233   = 4 * 50   + 33
50    = 1 * 33   + 17
33    = 1 * 17   + 16
17    = 1 * 16   + 1 
16    = 16 * 1   + 0
```
De `ggd` is 1, dus de inverse bestaat.

**2. Terugwerken (substitutie):**
Nu herschrijven we elke stap om de rest te isoleren en werken we van onder naar boven om `1` uit te drukken als een combinatie van `13800` en `1931`.

- `1 = 17 - 1 * 16`
- `1 = 17 - 1 * (33 - 1 * 17) = 2 * 17 - 1 * 33`
- `1 = 2 * (50 - 1 * 33) - 1 * 33 = 2 * 50 - 3 * 33`
- `1 = 2 * 50 - 3 * (233 - 4 * 50) = 14 * 50 - 3 * 233`
- `1 = 14 * (283 - 1 * 233) - 3 * 233 = 14 * 283 - 17 * 233`
- `1 = 14 * 283 - 17 * (1931 - 6 * 283) = 116 * 283 - 17 * 1931`
- `1 = 116 * (13800 - 7 * 1931) - 17 * 1931 = 116 * 13800 - 812 * 1931 - 17 * 1931`
- `1 = 116 * 13800 - 829 * 1931`

We hebben nu de vergelijking: `116 * 13800 - 829 * 1931 = 1`.

Als we deze vergelijking `modulo 13800` bekijken, wordt de eerste term nul:
`-829 * 1931 ≡ 1 (mod 13800)`

We hebben dus een waarde voor `d` gevonden, namelijk `-829`. Omdat `d` een positief getal moet zijn, tellen we `13800` erbij op:
`d = -829 + 13800 = 12971`

### `wxMaxima` Methode

In `wxMaxima` is het berekenen van de modulaire inverse veel eenvoudiger met de functie `inv_mod(e, m)`.

```wxmx
/* Bereken de inverse van e=1931 modulo phi_n=13800 */
d: inv_mod(e, phi_n);
/* Output: 12971 */
```
Dit commando voert het uitgebreide algoritme van Euclides op de achtergrond uit en geeft direct het juiste resultaat.

Je kan de stappen van het algoritme ook deels volgen met `gcdex(a, b)` wat staat voor 'extended gcd':
```wxmx
/* Geeft een lijst [u, v, g] zodat u*a + v*b = g, waar g=ggd(a,b) */
[u, v, g] : gcdex(e, phi_n);
/* u = -829, v = 116, g = 1 */
/* Dit bevestigt: -829 * 1931 + 116 * 13800 = 1 */

/* Om de positieve inverse te vinden: */
mod(u, phi_n);
/* Output: 12971 */
```

## Conclusie

De decoderingscomponent `d` is **12971**.

**wxMaxima Controle:**
```wxmx
mod(e * d, phi_n);
/* Output: 1 */
```
Dit bevestigt dat `d` de correcte inverse is.

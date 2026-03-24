# Uitleg Oefening 5: De Theorie achter Matrixmachten

Deze notitie legt de theorie achter het berekenen van hoge matrixmachten (zoals `A^25`) op een eenvoudige manier uit. We gaan uit van weinig voorkennis.

---

### Deel 1: Het Probleem - Waarom is dit moeilijk?

De opgave vraagt ons om `A^25` te berekenen. Manueel betekent dit dat je de matrix `A` 24 keer met zichzelf moet vermenigvuldigen.
`A * A = A²`
`A² * A = A³`
`A³ * A = A⁴`
... en zo verder tot `A^25`.

Dit is extreem veel werk en de kans op rekenfouten is bijna 100%. Er moet een slimmere manier zijn. Die slimmere manier gebruikt een speciale eigenschap die *elke* vierkante matrix heeft.

---

### Deel 2: De "Magische Regel" - De Karakteristieke Veelterm

De truc is dat elke matrix een simpele "regel" of "formule" volgt. Voor de matrix `A` uit de oefening zullen we bijvoorbeeld ontdekken dat geldt:
`A² - 2A - 3I = 0`

Waar `I` de eenheidsmatrix `[[1,0],[0,1]]` is.

Als we deze regel kennen, kunnen we hem herschrijven als:
`A² = 2A + 3I`

Dit is onze **magische regel!** Het betekent dat we `A²` niet meer hoeven uit te rekenen, we kunnen het gewoon vervangen door `2A + 3I`. Dit stelt ons in staat om *elke* hoge macht van `A` te vereenvoudigen tot een simpele combinatie van `A` en `I`.

**Hoe vinden we die regel?**
De regel komt van de **karakteristieke veelterm**. Dit is een soort "DNA" van de matrix. Je vindt hem met de formule `det(A - λI)`.

Voor onze matrix `A = [[1, -2], [-2, 1]]`:

1.  **Vorm `A - λI`**: Trek `λ` af van de diagonaal.
    `[[1-λ, -2], [-2, 1-λ]]`

2.  **Bereken de determinant**: `(1-λ)(1-λ) - (-2)(-2)`
    `= λ² - 2λ + 1 - 4`
    `= λ² - 2λ - 3`

Dit is de veelterm! De **Stelling van Cayley-Hamilton** garandeert ons nu dat als we `λ` vervangen door `A`, de uitkomst de nulmatrix is:
`A² - 2A - 3I = 0`
En daar is onze magische regel!

---

### Deel 3: De "Sleutels" - De Eigenwaarden

De **eigenwaarden** van een matrix zijn de oplossingen (of wortels) van de karakteristieke vergelijking.

Onze vergelijking is `λ² - 2λ - 3 = 0`.
We kunnen deze ontbinden in `(λ - 3)(λ + 1) = 0`.

De oplossingen zijn dus:
- `λ₁ = 3`
- `λ₂ = -1`

Deze twee getallen, `3` en `-1`, zijn de "sleutels" die we nodig hebben voor de snelle methode. Ze zijn de enige getallen die zich op een speciale manier gedragen in combinatie met matrix `A`.

---

### Deel 4: De "Snelweg" - De Oplossingsmethode

We weten nu dat elke macht van `A` kan worden vereenvoudigd tot een vorm van `a*A + b*I`. Dus ook voor `A^25` moet dit gelden:

`A^25 = a*A + b*I`

Onze enige taak is om de getallen `a` en `b` te vinden. Hier gebruiken we de eigenwaarden voor. De bovenstaande relatie geldt niet alleen voor de matrix `A`, maar ook voor de eigenwaarden `λ`!

We vervangen `A` door `λ` en `I` door `1`:
`λ^25 = a*λ + b`

Dit is een simpele vergelijking met getallen. En we hebben twee `λ`-waarden die we kunnen invullen:

1.  **Vul `λ₁ = 3` in:**
    `3^25 = a * 3 + b`

2.  **Vul `λ₂ = -1` in:**
    `(-1)^25 = a * (-1) + b`
    `-1 = -a + b`

We hebben nu een stelsel van twee simpele vergelijkingen met twee onbekenden (`a` en `b`):
1.  `3a + b = 3^25`
2.  `-a + b = -1`

Dit stelsel kunnen we oplossen!
- Trek (2) van (1) af: `(3a - (-a)) + (b - b) = 3^25 - (-1)`
  `4a = 3^25 + 1` => `a = (3^25 + 1) / 4`
- Uit (2) volgt `b = a - 1`:
  `b = (3^25 + 1) / 4 - 1`
  `b = (3^25 + 1 - 4) / 4` => `b = (3^25 - 3) / 4`

We hebben `a` en `b` gevonden! We hoeven deze enorme getallen niet uit te rekenen.

---

### Deel 5: Het Eindantwoord (Stappenplan)

Nu we `a` en `b` kennen, is het eindantwoord simpelweg:

`A^25 = a*A + b*I`
`A^25 = ((3^25 + 1) / 4) * A + ((3^25 - 3) / 4) * I`

**Samengevat Stappenplan:**

1.  **Bereken de karakteristieke veelterm** `det(A - λI)`.
    *(Voorbeeld: `λ² - 2λ - 3`)*
2.  **Vind de eigenwaarden (λ₁, λ₂) ** door de veelterm gelijk te stellen aan nul en op te lossen.
    *(Voorbeeld: `λ₁ = 3`, `λ₂ = -1`)*
3.  **Stel de twee vergelijkingen op** met de vorm `λ^n = aλ + b`.
    *(Voorbeeld: `3^25 = 3a + b` en `-1 = -a + b`)*
4.  **Los het stelsel op** om `a` en `b` te vinden.
    *(Voorbeeld: `a = (3^25+1)/4`, `b = (3^25-3)/4`)*
5.  **Schrijf het eindantwoord** in de vorm `A^n = a*A + b*I`. Klaar!

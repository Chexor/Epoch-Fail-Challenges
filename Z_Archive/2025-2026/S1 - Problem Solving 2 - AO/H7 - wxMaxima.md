# H7 - wxMaxima Handleiding

[[H7 - Recurrente betrekkingen]]

Deze nota toont hoe je `wxMaxima` kan gebruiken om de stappen voor het oplossen van recurrente betrekkingen te ondersteunen. In tegenstelling tot andere hoofdstukken is er geen magisch commando dat alles voor je oplost; je gebruikt `wxMaxima` om de deelstappen (vierkantsvergelijking, stelsel) snel uit te rekenen.

## Stappenplan in `wxMaxima`

We lossen het voorbeeld `tn = tn-1 + 2*tn-2` met `t2=1` en `t7=65` op.

### Stap 1: Los de karakteristieke vergelijking op

De betrekking `tn = 1*t(n-1) + 2*t(n-2)` wordt de karakteristieke vergelijking `r^2 = 1*r + 2*1`, ofwel `r^2 - r - 2 = 0`.

```maxima
/* Los de vierkantsvergelijking op naar r */
solve(r^2 - r - 2 = 0, r);
/* Output: [r=2, r=-1] */
```
We hebben twee verschillende reële wortels: `r1 = 2` en `r2 = -1`.

### Stap 2: Stel de algemene oplossing op (manueel)

Omdat we twee verschillende wortels hebben, is de algemene vorm:
`t(n) := a1 * (r1)^n + a2 * (r2)^n`

In `wxMaxima` definiëren we dit als een functie:
```maxima
/* Definieer t(n) met de gevonden wortels.
   Gebruik a1 en a2 voor alpha1 en alpha2. */
t(n) := a1 * (2)^n + a2 * (-1)^n;
```

### Stap 3: Los het stelsel voor `a1` en `a2` op

Gebruik de gegeven beginvoorwaarden (`t(2)=1` en `t(7)=65`) om een stelsel op te stellen en op te lossen.

```maxima
/* Definieer de twee vergelijkingen gebaseerd op de beginvoorwaarden */
vgl1: t(2) = 1;
vgl2: t(7) = 65;

/* Los het stelsel op voor a1 en a2 */
constanten: solve([vgl1, vgl2], [a1, a2]);
/* Output: [[a1=1/2, a2= -1]] */
```

### Stap 4: Definieer de finale, expliciete functie

Nu we `a1` en `a2` kennen, kunnen we de finale functie definiëren.

```maxima
/* Gebruik de gevonden waarden voor a1 en a2 */
a1: 1/2;
a2: -1;

t_expl(n) := a1 * (2)^n + a2 * (-1)^n;

/* Of simpeler, gebruik subst() om de waarden in de algemene
   formule te substitueren: */
t_expl(n) := subst(constanten, t(n));
```

### Stap 5: Bereken de gevraagde termen

Nu je de expliciete functie hebt, kan je elke term direct berekenen.

```maxima
/* Bereken de 10de term */
t_expl(10);

/* Bereken de eerste 10 termen in een lijst */
makelist(t_expl(k), k, 1, 10);
```

Dit stappenplan, waarbij je `wxMaxima` gebruikt voor de `solve`-stappen, is de meest efficiënte manier om deze oefeningen op het examen op te lossen.

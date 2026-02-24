# H5: Toevalsveranderlijken en hun parameters

## ✅ SSOT
- Dit is de **authoritative** hoofdstuknote voor H5.
- Afgeleide samenvattingen moeten hiernaar linken.

## 1. Statistische vs. toevalsveranderlijke
- **Statistische veranderlijke:** gemeten uitkomst, beschreven met frequenties.
- **Toevalsveranderlijke:** toekomstige/onzekere uitkomst, beschreven met kansen.

### Parameters (parallel met H2)
- **Gemiddelde** -> **Verwachtingswaarde** $E(X)$.
- **Spreiding** -> **Variantie** $Var(X)$ en **standaardafwijking** $\sigma$.

## 2. Discrete toevalsveranderlijke
- **Kansfunctie:** $p(x)=P(X=x)$.
- **Grafiek:** staafdiagram.
- **Verdelingsfunctie:** $F(k)=P(X \le k)$.

## 3. Continue toevalsveranderlijke
- **Verdelingsfunctie:** $F(k)=P(X \le k)$ (wel zinvol).
- **Dichtheidsfunctie:** $f(x)$ met:
  - $f(x) \ge 0$.
  - Oppervlakte onder $f$ is 1.
  - $P(x_1 \le X \le x_2)=\int_{x_1}^{x_2} f(x)\,dx$.

## 4. Parameters van $X$
- **Verwachtingswaarde (discreet):** $E(X)=\sum x\,p(x)$.
- **Verwachtingswaarde (continu):** $E(X)=\int x f(x)\,dx$.
- **Variantie:** $Var(X)=E(X^2)-[E(X)]^2$.
- **Standaardafwijking:** $\sigma=\sqrt{Var(X)}$.

## 5. Tweedimensionale (discrete) toevalsveranderlijken
- **Gezamenlijke kansfunctie:** $p(x,y)=P(X=x, Y=y)$.
- **Onafhankelijkheid:** $p(x,y)=p_X(x)\,p_Y(y)$ voor alle $x,y$.

## 6. Som en verschil van toevalsveranderlijken
- Nieuwe variabelen: $X+Y$ en $X-Y$.
- **Verwachtingswaarde:** $E(X \pm Y)=E(X) \pm E(Y)$.
- **Variantie:**
  - Als $X$ en $Y$ onafhankelijk: $Var(X \pm Y)=Var(X)+Var(Y)$.
  - Anders moet covariantie worden meegenomen.

## 7. Examenvallen
- Verwachtingswaarde is het **kansgemiddelde**, niet het meest waarschijnlijke punt.
- Variantie van som = som van varianties **alleen bij onafhankelijkheid**.

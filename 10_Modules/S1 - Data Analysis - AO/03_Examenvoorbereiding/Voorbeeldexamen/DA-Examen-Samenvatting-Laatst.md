# Data Analysis - Laatste samenvatting (examen)

Dit is een compacte checklist van de leerstof die terugkomt in het voorbeeldexamen (oef. 1 t/m 10).

Rekenmachine:
- [[DA-Voorbeeldexamen-TI-36X-Pro-Cheat-Sheet]]
- [[DA-Voorbeeldexamen-TI-36X-Pro-Manual]]

## 1) Beschrijvende statistiek (tabel, grafiek, kengetallen)

### Gegroepeerde data (klassen)
- Intervalgrenzen bij afronding op 1: gebruik 0.5-correctie (bv. 1-6 -> 0.5-6.5).
- Klassenbreedte: $h = \text{bovengrens} - \text{ondergrens}$.
- Middelpunt klasse: $m_i = (L_i + U_i)/2$.
- Cumulatief: $cf_i = \sum_{k\le i} f_k$, en $ch_i(\%) = 100\,cf_i/n$.

### Grafieken
- Histogram: bij gelijke $h$ mag hoogte = $f_i$ (anders frequentiedichtheid = $f_i/h$).
- Ogief: plot (bovengrens, cumulatief) en verbind stijgend.
- Kwartielen grafisch: lees af bij 25%, 50%, 75% op de ogief.

### Interpolatie in een klasse (mediaan/kwartielen)
Voor een positie $p$ (bv. $p=n/2$ of $p=n/4$):
$$
\text{waarde} = L + \frac{p - cf_{\text{voor}}}{f_{\text{klasse}}}\,h
$$

### Gemiddelde en spreiding (gegroepeerd)
- Gemiddelde (schatting): $\bar{X}=\frac{\sum f_i m_i}{n}$.
- Variantie (noemer $n$): $s^2 = \frac{1}{n}\sum f_i m_i^2 - \bar{X}^2$.
- Standaardafwijking: $s=\sqrt{s^2}$.

### Modus (gegroepeerd)
Modale klasse = hoogste frequentie.
$$
Mo = L + \frac{\Delta_1}{\Delta_1+\Delta_2}\,h\quad\text{met}\quad \Delta_1=f_{mod}-f_{vorige},\ \Delta_2=f_{mod}-f_{volgende}
$$

### Scheefheid (Pearson)
$$
Sk_p = \frac{\bar{X}-Mo}{s}
$$
- $Sk_p>0$ rechtsscheef, $Sk_p<0$ linksscheef.

## 2) Kansrekening basics

- Complement: $P(\bar{A})=1-P(A)$.
- Onafhankelijk: $P(A\cap B)=P(A)P(B)$.
- Unie: $P(A\cup B)=P(A)+P(B)-P(A\cap B)$.
- “Minstens 1”: vaak sneller via complement: $1-P(\text{geen})$.

## 3) Voorwaardelijke kans en Bayes

- Definitie: $P(A\mid B)=\frac{P(A\cap B)}{P(B)}$.
- Totale kans: $P(B)=P(B\mid A)P(A)+P(B\mid \bar{A})P(\bar{A})$.
- Bayes:
$$
P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}
$$

## 4) Discrete toevalsvariabelen (tabel)

- Marginalen:
  - $P(X=x)=\sum_y P(X=x,Y=y)$
  - $P(Y=y)=\sum_x P(X=x,Y=y)$
- Onafhankelijk check: $P(X=x,Y=y)$ vergelijken met $P(X=x)P(Y=y)$.

### Som $S=X+Y$
- Maak de mogelijke sommen.
- Voor elke som: tel alle bijhorende cellen op.

### Verwachting en variantie
Voor een discrete $S$:
$$
E(S)=\sum s\,P(S=s)
$$
$$
Var(S)=\sum s^2\,P(S=s)-(E(S))^2
$$

## 5) Normale verdeling

- Notatie: $X\sim N(\mu,\sigma)$.
- Standaardiseren: $Z=\frac{X-\mu}{\sigma}$.
- Kansen: gebruik `normalcdf(lower, upper, mu, sigma)`.
- Percentielen: gebruik `invNorm(area, mu, sigma)`.

## 6) Steekproefgemiddelde

Als $X\sim N(\mu,\sigma)$ en je neemt een steekproef van grootte $n$:
$$
\bar{X}\sim N\left(\mu,\frac{\sigma}{\sqrt{n}}\right)
$$

## 7) Verschil van 2 normale variabelen

Bij onafhankelijkheid:
- $D=X-Y$ is normaal.
- $\mu_D=\mu_X-\mu_Y$
- $\sigma_D=\sqrt{\sigma_X^2+\sigma_Y^2}$

Gebruik daarna `normalcdf` op $D$.

## 8) Binomiale verdeling en normale benadering

- $X\sim B(n,p)$.
- Exact:
  - $P(X=x)$ met `binompdf(n,p,x)`
  - $P(X\le x)$ met `binomcdf(n,p,x)`

Normale benadering (als $n$ groot genoeg en $np$ en $n(1-p)$ niet te klein):
- $\mu=np$
- $\sigma=\sqrt{np(1-p)}$
- Continuiteitscorrectie:
  - $P(X\ge k)\approx P(N\ge k-0.5)$
  - $P(X\le k)\approx P(N\le k+0.5)$

## 9) Betrouwbaarheidsinterval voor het gemiddelde (n klein)

Als $\sigma$ onbekend en $n$ klein:
$$
\bar{X}\pm t_{\alpha/2,\,n-1}\,\frac{s}{\sqrt{n}}
$$
- $t$ komt uit t-tabel (of `invT` als je TI dat heeft).
- Let op consistentie: in oefeningen kan soms met $\sigma$-variant worden gewerkt; volg dan die conventie.

## 10) Toets: verschil tussen 2 gemiddelden (2 steekproeven)

Eenzijdig of tweezijdig:
- Zet $H_0$ en $H_1$ duidelijk.

Pooled t-toets (zoals in het voorbeeld):
$$
s_p^2=\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}
$$
$$
SE=\sqrt{s_p^2\left(\frac{1}{n_1}+\frac{1}{n_2}\right)}
$$
$$
t=\frac{\bar{x}_1-\bar{x}_2}{SE},\quad \nu=n_1+n_2-2
$$

Beslissing:
- Verwerp $H_0$ als $t$ in het kritieke gebied valt (bv. $t>t_{1-\alpha,\nu}$ bij eenzijdig rechts).

Schrijf in woorden:
- “significant” bij $\alpha=0.05$ en verwerpen.
- “sterk significant” bij $\alpha=0.01$ en verwerpen.

## Examenworkflow (snel)

- Schrijf altijd: definities van gebeurtenissen/variabelen, gegeven parameters, wat gevraagd is.
- Kies 1 formulepad en blijf consistent (noemer $n$ vs. $n-1$).
- Gebruik TI voor: `1-Var Stats`, `normalcdf`, `invNorm`, `binompdf`, `binomcdf`, en rekenwerk met haakjes.

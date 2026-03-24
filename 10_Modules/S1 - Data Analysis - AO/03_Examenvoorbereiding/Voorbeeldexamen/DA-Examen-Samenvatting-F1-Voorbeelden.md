# Data Analysis - Samenvatting per concept (F1-context, standalone)

Doel: leerstof herhalen in 1 document. Opbouw per concept (niet per oefening).
Bij elk concept:
- wat je berekent
- welke variabelen je gebruikt
- formules en rekenstappen (LaTeX)
- wat de uitkomst betekent
- een pragmatisch F1-voorbeeld met getallen

## 0) Notatie (altijd)

Steekproef / data:

$$
n = \text{aantal observaties},\qquad x_i = \text{i-de observatie}
$$

Gegroepeerde data:

$$
f_i = \text{frequentie van klasse } i,\quad cf_i = \sum_{k=1}^{i} f_k
$$

Gemiddelde:

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i\qquad (\text{steekproefgemiddelde})
$$

Spreiding:

$$
s = \text{standaardafwijking (steekproef)},\qquad \sigma = \text{standaardafwijking (populatie)}
$$

Kansen:

$$
P(\cdot) = \text{kans}
$$

Extra symbolen die vaak voorkomen:

$$
\min(x),\ \max(x) = \text{kleinste/grootste observatie}
$$

$$
Q_1,\ Me,\ Q_3 = \text{eerste kwartiel, mediaan, derde kwartiel}
$$

$$
\operatorname{Var}(X) = \text{variantie},\qquad \sigma(X)=\sqrt{\operatorname{Var}(X)}
$$

## 1) Datatypes (welke grafiek/formule is logisch?)

Wat je bepaalt:

- Kwalitatief (categorie):
  - nominaal (geen volgorde): team, motorleverancier
  - ordinaal (wel volgorde): bandenslijtage laag/medium/hoog

- Kwantitatief (getal):
  - discreet (tellen): aantal pitstops
  - continu (meten): pitstop-tijd (s), rondetijd (s)

Waarom dit telt:
- kwalitatief: staafdiagram/pie
- kwantitatief: histogram/boxplot/ogief, gemiddelden/spreiding

Pragmatisch voorbeeld:

- Data A: "team" = {Ferrari, McLaren, Mercedes} (kwalitatief, nominaal)
  - beste grafiek: staafdiagram met aantallen per team
- Data B: "aantal pitstops" = {1,2,3,...} (kwantitatief, discreet)
  - kan met staafdiagram of tabel
- Data C: "pitstop-tijd" in seconden (kwantitatief, continu)
  - beste grafiek: histogram of boxplot

## 2) Centrummaten (gemiddelde, mediaan, modus)

(Voorbeeldexamen: vooral oef. 1 en oef. 2.)

### 2.1 Gemiddelde

Wat bereken je?
- het “balanspunt” van de data; langetermijngemiddelde.

Formule:

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
$$

Variabelen:
- $x_i$ = meting i (bv. pitstop-tijd)
- $n$ = aantal metingen

Voorbeeld (F1, pitstop-tijden in seconden):

$$
x = (2.6, 2.7, 2.9, 3.1, 2.8, 2.7, 2.6, 3.4),\quad n=8
$$

$$
\sum x_i = 2.6+2.7+2.9+3.1+2.8+2.7+2.6+3.4 = 22.8
$$

$$
\bar{x} = \frac{22.8}{8} = 2.85
$$

Betekenis:
- gemiddeld duurt een pitstop in deze steekproef 2.85 s.

Pragmatische check:
- Als 1 pitstop extreem traag is (bv. 6.0 s), dan kan $\bar{x}$ sterk omhoog gaan.
- Daarom kijk je vaak ook naar de mediaan.

### 2.2 Mediaan

Wat bereken je?
- de middelste waarde; 50% zit eronder.

Stapplan:
1) sorteer
2) neem middelste (of gemiddelde van de 2 middelsten)

Voorbeeld (zelfde data, gesorteerd):

$$
(2.6, 2.6, 2.7, 2.7, 2.8, 2.9, 3.1, 3.4)
$$

Even $n$, dus:

$$
Me = \frac{x_{(4)} + x_{(5)}}{2} = \frac{2.7+2.8}{2} = 2.75
$$

Betekenis:
- 50% van de pitstops is sneller dan 2.75 s.
- minder gevoelig voor 1 extreme trage pitstop.

Pragmatisch voorbeeld (uitschieter):

Neem dezelfde set, maar vervang 3.4 door 6.0.

Nieuwe som:

$$
\sum x_i = 22.8 - 3.4 + 6.0 = 25.4
$$

Nieuw gemiddelde:

$$
\bar{x} = \frac{25.4}{8} = 3.175
$$

Mediaan blijft veel stabieler (nog steeds rond 2.75-2.80, afhankelijk van de exacte waarden).

Interpretatie:
- bij pitstops is mediaan vaak representatiever als er af en toe een probleemstop is.

### 2.3 Modus

Wat bereken je?
- meest voorkomende waarde.

Opmerking:
- bij continue data vaak weinig zinvol; bij gegroepeerde data wel (zie 4.6).

Pragmatisch voorbeeld (discreet):

Als $X$ = aantal pitstops per race in 10 races:

$$
X = (1,2,2,2,1,3,2,1,2,1)
$$

Dan is de modus:

$$
Mo = 2
$$

Interpretatie:
- "meestal" zijn het 2 pitstops.

## 3) Spreiding (range, variantie, standaardafwijking)

(Voorbeeldexamen: oef. 1(f), oef. 2.)

### 3.1 Range

$$
R = x_{\max} - x_{\min}
$$

Betekenis:
- totale spreiding tussen minimum en maximum.

Pragmatisch voorbeeld:

Voor de pitstop-tijden:

$$
R = 3.4 - 2.6 = 0.8\ \text{s}
$$

Interpretatie:
- in deze steekproef zitten alle pitstops binnen 0.8 s van elkaar.

### 3.2 Variantie en standaardafwijking

Wat bereken je?
- variantie: gemiddelde kwadratische afwijking
- standaardafwijking: typische afwijking (zelfde eenheid)

Steekproef (klassiek):

$$
s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2
$$

Populatie (noemer $n$):

$$
\sigma^2 = \frac{1}{n}\sum_{i=1}^{n}(x_i-\mu)^2
$$

En:

$$
s=\sqrt{s^2},\qquad \sigma=\sqrt{\sigma^2}
$$

Betekenis (F1):
- kleine $s$: rondetijden/pitstops zijn consistent
- grote $s$: veel variatie (problemen, verkeer, banden, ...)

Pragmatisch voorbeeld (waarom kwadrateren en wortel nemen?):

Voor steekproefdata gebruik je vaak:

$$
s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2
$$

De term $(x_i-\bar{x})$ is de afwijking van het gemiddelde.
Je kwadrateert zodat negatieve en positieve afwijkingen elkaar niet wegcancellen.
Je neemt daarna de wortel om terug te gaan naar seconden.

## 4) Gegroepeerde data (klassen, histogram, ogief)

(Voorbeeldexamen: oef. 1.)

We nemen dezelfde cijfers als het voorbeeldexamen, maar geven ze een F1-betekenis.

F1-context:
- $n=110$ races
- $X$ = aantal ronden per race dat een coureur binnen 1 seconde van de voorganger rijdt (afgerond op hele ronden)
- Klassen: 1-6, 7-12, 13-18, 19-24, 25-30
- Frequenties: $f=(22,39,28,15,6)$

### 4.1 Continue klassegrenzen en middenpunten

Omdat $X$ op hele ronden is afgerond, gebruik je 0.5-correctie:

$$
1\text{--}6 \rightarrow 0.5\text{--}6.5,\quad 7\text{--}12 \rightarrow 6.5\text{--}12.5,\ \ldots
$$

Klassenbreedte:

$$
h = U-L = 6
$$

Middenpunt:

$$
m_i = \frac{L_i+U_i}{2}
$$

Middenpunten:

$$
m=(3.5,9.5,15.5,21.5,27.5)
$$

Wat betekent dit?
- in rekenwerk vervang je elke klasse door zijn middenpunt (schatting).

Pragmatisch voorbeeld:

Als de data "afgerond op hele ronden" is, dan kan waarde 6 in werkelijkheid tussen 5.5 en 6.5 liggen.
Daarom wordt de klasse 1-6 continu als 0.5-6.5 genomen.

### 4.2 Cumulatieven en ogief

$$
cf_i = \sum_{k=1}^{i} f_k
$$

$$
cf=(22,61,89,104,110)
$$

Cumulatief relatief (in %):

$$
ch_i = 100\cdot\frac{cf_i}{n}
$$

Voorbeeld:

$$
ch_2 = 100\cdot\frac{61}{110}=55.45\%
$$

Ogiefpunten (bovengrens, cumulatief):

$$
(6.5,22),(12.5,61),(18.5,89),(24.5,104),(30.5,110)
$$

Betekenis:
- je kan aflezen welk aandeel races onder een bepaalde grens zit.

Pragmatisch voorbeeld:

Uit $cf_2=61$ volgt:

$$
\frac{61}{110}=0.5545
$$

Interpretatie:
- ongeveer 55.45% van de races heeft $X \le 12$ (want tweede klasse eindigt bij 12.5 in continue grenzen).

### 4.3 Gemiddelde (gegroepeerd)

Wat bereken je?
- schatting van het gemiddelde met middenpunten.

$$
\bar{x} \approx \frac{\sum f_i m_i}{n}
$$

$$
\sum f_i m_i = 22\cdot 3.5 + 39\cdot 9.5 + 28\cdot 15.5 + 15\cdot 21.5 + 6\cdot 27.5
$$

$$
= 77 + 370.5 + 434 + 322.5 + 165 = 1369
$$

$$
\bar{x} \approx \frac{1369}{110} = 12.45
$$

Betekenis:
- gemiddeld ongeveer 12.45 ronden binnen 1 seconde (per race).

Pragmatische check:
- Dit is een schatting, omdat je binnen elke klasse niet de exacte waarden kent.
- Als de echte waarden vaak aan de onderkant van de klasse zitten, overschat je met middenpunten.

### 4.4 Mediaan en kwartielen (interpolatie)

Wat bereken je?
- $Q_1$: 25% ligt eronder
- $Me$: 50% ligt eronder
- $Q_3$: 75% ligt eronder

Posities:

$$
p_{Q_1}=\frac{n}{4},\quad p_{Me}=\frac{n}{2},\quad p_{Q_3}=\frac{3n}{4}
$$

$$
p_{Me}=\frac{110}{2}=55
$$

Zoek de mediaanklasse via cumulatieven:

$$
cf_1=22 < 55 \le cf_2=61
$$

Interpolatieformule:

$$
\text{waarde} = L + \frac{p-cf_{\text{voor}}}{f_{\text{klasse}}}\cdot h
$$

Voor de mediaan:

$$
L=6.5,\ cf_{\text{voor}}=22,\ f_{\text{klasse}}=39,\ h=6
$$

$$
Me = 6.5 + \frac{55-22}{39}\cdot 6 = 11.58
$$

Betekenis:
- 50% van de races heeft $X$ kleiner dan ongeveer 11.6.

Pragmatisch voorbeeld (intuitioneel):

In de mediaanklasse (6.5-12.5) zitten 39 races.
Je hebt er nog $55-22=33$ nodig binnen die klasse om de mediaan te bereiken.
De fractie binnen de klasse is:

$$
\frac{33}{39}=0.8462
$$

Dus je zit ~84.6% door die klasse:

$$
6.5 + 0.8462\cdot 6 = 11.58
$$

### 4.5 Modus (gegroepeerde data)

Wat bereken je?
- meest typische waarde (binnen modale klasse).

Definities:

$$
\Delta_1=f_{mod}-f_{vorige},\qquad \Delta_2=f_{mod}-f_{volgende}
$$

$$
Mo = L + \frac{\Delta_1}{\Delta_1+\Delta_2}\cdot h
$$

Voorbeeld:

$$
f_{mod}=39,\ f_{vorige}=22,\ f_{volgende}=28
$$

$$
\Delta_1=39-22=17,\quad \Delta_2=39-28=11
$$

$$
Mo = 6.5 + \frac{17}{17+11}\cdot 6 = 10.14
$$

Betekenis:
- meest typische waarde ligt rond 10.

Pragmatisch voorbeeld:

Omdat de modale klasse de hoogste staaf heeft in het histogram, ligt de modus ergens in die klasse.
De formule schuift de modus richting de kant waar de daling naar de buurklasse steiler is.

### 4.6 Standaardafwijking (gegroepeerd)

Wat bereken je?
- spreiding rond het gemiddelde, met middenpunten als benadering.

Veelgebruikte examenvorm (noemer $n$):

$$
s^2 \approx \frac{1}{n}\sum f_i m_i^2 - \bar{x}^2
$$

$$
\sum f_i m_i^2 = 22\cdot 3.5^2 + 39\cdot 9.5^2 + 28\cdot 15.5^2 + 15\cdot 21.5^2 + 6\cdot 27.5^2
$$

$$
= 269.5 + 3522.75 + 6727 + 6933.75 + 4537.5 = 21990.5
$$

$$
s^2 \approx \frac{21990.5}{110} - 12.45^2 = 45.00
$$

$$
s \approx \sqrt{45.00} = 6.708
$$

Betekenis:
- typische afwijking rond 12.45 is ongeveer 6.7 ronden.

Pragmatische interpretatie:

Als $\bar{x}=12.45$ en $s\approx 6.7$, dan liggen veel waarden grofweg in de buurt van:

$$
12.45\pm 6.7
$$

Dus ruw tussen ongeveer 6 en 19 (niet als harde regel, maar als gevoel voor spreiding).

### 4.7 Scheefheid (Pearson)

Wat bereken je?
- richting en grootte van asymmetrie.

$$
Sk_p = \frac{\bar{x}-Mo}{s}
$$

$$
Sk_p = \frac{12.45-10.14}{6.708} = 0.34
$$

Betekenis:
- licht rechtsscheef: meestal rond centrum, soms hoge uitschieters.

Pragmatische check (orde van centrum-maten):

Bij rechtsscheef zie je vaak:

$$
Mo < Me < \bar{x}
$$

In het voorbeeld:

$$
10.14 < 11.58 < 12.45
$$

## 5) Kansregels (complement, onafhankelijk, unie)

(Voorbeeldexamen: oef. 3.)

Complement:

$$
P(\bar{A})=1-P(A)
$$

Onafhankelijkheid:

$$
P(A\cap B)=P(A)P(B)
$$

Unie:

$$
P(A\cup B)=P(A)+P(B)-P(A\cap B)
$$

Voorbeeld (F1-events met dezelfde cijfers):

$$
P(A)=0.20,\qquad P(B)=0.25
$$

$$
P(\bar{A}\cap\bar{B})=(1-0.20)(1-0.25)=0.60
$$

$$
P(A\cap B)=0.20\cdot 0.25=0.05
$$

$$
P(A\cup B)=0.20+0.25-0.05=0.40
$$

Betekenis:
- 40% kans dat minstens 1 event gebeurt (bij onafhankelijkheid).

Pragmatisch voorbeeld ("minstens 1" via complement):

Als "geen van beide" 0.60 is, dan:

$$
P(\text{minstens 1}) = 1-0.60 = 0.40
$$

## 6) Bayes en totale kans

(Voorbeeldexamen: oef. 4.)

Totale kans:

$$
P(E)=P(E\mid A)P(A)+P(E\mid\bar{A})P(\bar{A})
$$

Bayes:

$$
P(A\mid E)=\frac{P(E\mid A)P(A)}{P(E)}
$$

Voorbeeld (F1-inspectie, 10 echt op 12):

$$
P(A)=\frac{10}{12},\ P(\bar{A})=\frac{2}{12},\ P(E\mid A)=0.9,\ P(E\mid\bar{A})=0.1
$$

$$
P(E)=0.9\cdot\frac{10}{12}+0.1\cdot\frac{2}{12}=0.766\overline{6}
$$

$$
P(A\mid E)=\frac{0.9\cdot\frac{10}{12}}{0.766\overline{6}}=0.9783
$$

Betekenis:
- als de inspecteur “authentiek” zegt, is het bijna zeker echt.

Pragmatisch inzicht:

Bayes combineert:
- hoe vaak iets echt voorkomt (basis-kans $P(A)$)
- hoe betrouwbaar je test is ($P(E\mid A)$ en $P(E\mid\bar{A})$)
Totale kans $P(E)$ is de "normalisatie" zodat je weer op een echte kans uitkomt.

## 7) Gezamenlijke kansverdeling, somvariabele, verwachting, variantie

(Voorbeeldexamen: oef. 5.)

Gezamenlijke verdeling:
- tabel met $P(X=x, Y=y)$.

Marginalen:

$$
P(X=x)=\sum_y P(X=x,Y=y),\qquad P(Y=y)=\sum_x P(X=x,Y=y)
$$

Onafhankelijkheidstest:

$$
\text{onafhankelijk} \iff P(X=x,Y=y)=P(X=x)P(Y=y)\ \text{voor alle }x,y
$$

Somvariabele:

$$
S=X+Y
$$

Verdeling van $S$:

$$
P(S=s)=\sum_{x+y=s} P(X=x,Y=y)
$$

Verwachting en variantie (discreet):

$$
E(S)=\sum_s s\,P(S=s)
$$

$$
Var(S)=\sum_s s^2\,P(S=s) - (E(S))^2
$$

Betekenis:
- $E(S)$ is het langetermijngemiddelde van $S$.
- $Var(S)$ is de spreiding rond dat gemiddelde.

Pragmatisch voorbeeld (mini-tabel):

Neem $X\in\{1,2\}$ (aantal pitstops) en $Y\in\{0,1\}$ (wel/geen safety car) met:

$$
P(X=1,Y=0)=0.50,\quad P(1,1)=0.10,\quad P(2,0)=0.30,\quad P(2,1)=0.10
$$

Dan is $S=X+Y$ en:

$$
P(S=1)=P(1,0)=0.50
$$

$$
P(S=2)=P(1,1)+P(2,0)=0.10+0.30=0.40
$$

$$
P(S=3)=P(2,1)=0.10
$$

Nu:

$$
E(S)=1\cdot 0.50 + 2\cdot 0.40 + 3\cdot 0.10 = 1.60
$$

## 8) Binomiale verdeling (exact) en normale benadering

(Voorbeeldexamen: oef. 8.)

Binomiaal:

$$
X\sim B(n,p)
$$

$$
P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}
$$

Parameters:

$$
\mu=np,\qquad \sigma=\sqrt{np(1-p)}
$$

Voorbeeld (F1 quality control, p=0.10):

$$
X\sim B(50,0.10)
$$

$$
P(X=5)=\binom{50}{5}(0.10)^5(0.90)^{45}=0.1849
$$

Normale benadering met continuiteitscorrectie:

$$
X\approx N(\mu,\sigma)
$$

Voor $X\sim B(200,0.10)$:

$$
\mu=200\cdot 0.10=20,\qquad \sigma=\sqrt{200\cdot 0.10\cdot 0.90}=4.2426
$$

$$
P(X\ge 30)\approx P(N\ge 29.5)
$$

$$
z=\frac{29.5-20}{4.2426}=2.24
$$

$$
P(Z\ge 2.24)=0.0125
$$

Betekenis:
- 1.25% is “erg klein”: 30+ defecten is uitzonderlijk als p=0.10.

Pragmatische check (wanneer normale benadering ok is):

Vaak gebruik je de regel dat:

$$
np \ge 5\ \text{en}\ n(1-p)\ge 5
$$

In het voorbeeld $n=200,p=0.10$:

$$
np=20\ge 5,\qquad n(1-p)=180\ge 5
$$

## 9) Normale verdeling, z-score, Z-tabel

(Voorbeeldexamen: oef. 7 en oef. 9.)

$$
X\sim N(\mu,\sigma)
$$

Z-score:

$$
Z=\frac{X-\mu}{\sigma}\sim N(0,1)
$$

Voorbeeld (sigma uit percentiel):

$$
X\sim N(130,\sigma),\qquad P(X<125)=0.04
$$

$$
P\left(Z<\frac{125-130}{\sigma}\right)=0.04
$$

Uit Z-tabel: $z_{0.04}\approx -1.75$.

$$
\frac{-5}{\sigma}=-1.75\Rightarrow \sigma=\frac{5}{1.75}=2.8571
$$

Betekenis:
- sigma is de typische spreiding rond 130.

Pragmatisch voorbeeld (kans boven een grens):

Als $\sigma=2.8571$ en je wil $P(X>132)$:

$$
z=\frac{132-130}{2.8571}=0.70
$$

$$
P(X>132)=P(Z>0.70)=1-P(Z\le 0.70)
$$

## 10) Steekproefgemiddelde (sampling distribution)

(Voorbeeldexamen: oef. 7(a).)

Als $X$ normaal is (of n groot genoeg):

$$
\bar{X}\sim N\left(\mu,\frac{\sigma}{\sqrt{n}}\right)
$$

Variabelen:
- $\mu$ = gemiddelde van individuele meting
- $\sigma$ = standaardafwijking van individuele meting
- $n$ = steekproefgrootte

Betekenis:
- gemiddelden van steekproeven schommelen minder: factor $\sqrt{n}$.

Pragmatisch voorbeeld:

Als individuele rondetijden een spreiding $\sigma=9$ s hebben, dan heeft het gemiddelde van 6 ronden:

$$
\sigma_{\bar{X}}=\frac{9}{\sqrt{6}}=3.6742
$$

Interpretatie:
- gemiddelde over 6 ronden is veel stabieler dan 1 ronde.

## 11) Verschil van 2 normale variabelen

(Voorbeeldexamen: oef. 7(b).)

Bij onafhankelijkheid:

$$
D=X-Y\sim N\left(\mu_X-\mu_Y,\sqrt{\sigma_X^2+\sigma_Y^2}\right)
$$

Betekenis:
- je herleidt “wie is groter/smaller” naar 1 normale variabele $D$.

Pragmatisch voorbeeld:

Als je wil weten hoe vaak Team B trager is dan Team A, reken je:

$$
P(Y>X)=P(X-Y<0)=P(D<0)
$$

en standaardiseer je $D$ zoals bij een normale verdeling.

## 12) Betrouwbaarheidsinterval voor het gemiddelde (n klein -> t)

(Voorbeeldexamen: oef. 6.)

Vrijheidsgraden:

$$
\nu=n-1
$$

Standaardvorm:

$$
\bar{x}\pm t_{1-\alpha/2,\nu}\cdot\frac{s}{\sqrt{n}}
$$

Betekenis:
- interval met een gekozen betrouwbaarheid (bv. 95%) voor $\mu$.

Pragmatisch voorbeeld (95% tweezijdig):

$$
\bar{x}=2.28,\quad s=0.8756,\quad n=6,\quad \nu=5
$$

Neem $t_{0.975,5}\approx 2.57$.

$$
\text{marge}=2.57\cdot\frac{0.8756}{\sqrt{5}}\approx 1.01
$$

$$
\text{interval}=[2.28-1.01,\ 2.28+1.01]=[1.27,\ 3.29]
$$

## 13) Hypothesetoets (verschil tussen 2 gemiddelden)

(Voorbeeldexamen: oef. 10.)

Stramien:
1) formuleer $H_0$ en $H_1$
2) kies $\alpha$
3) bereken testgrootheid
4) kritieke waarde (t-tabel)
5) conclusie in woorden (significant/sterk significant)

Pooled t-toets (zoals in het voorbeeldexamen):

$$
\nu=n_1+n_2-2
$$

$$
s_p^2=\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}
$$

$$
SE=\sqrt{s_p^2\left(\frac{1}{n_1}+\frac{1}{n_2}\right)}
$$

$$
t=\frac{\bar{x}_1-\bar{x}_2}{SE}
$$

Betekenis:
- grote $t$ betekent: het verschil is groot t.o.v. de verwachte ruis.

Pragmatisch voorbeeld (beslissingsregel, eenzijdig rechts):

Als je $t=3.30$ berekent en je kritieke waarde bij $\alpha=0.01$ is $t_{0.99,\nu}=2.33$, dan:

$$
3.30 > 2.33\ \Rightarrow\ \text{verwerp }H_0\ \text{(sterk significant)}
$$

Interpretatie:
- zo'n groot verschil zie je zelden door toeval als de echte gemiddelden gelijk zijn.

# Symbolen & notatie (Data Analysis)

## ✅ SSOT
- Dit is de enige lijst met symbolen/notatie die we onderhouden.
- Aanpassingen gebeuren hier; andere notities embedden of linken hiernaartoe.

Dekking: alles uit `DA-Formularium.md` + wat je typisch nodig hebt bij de voorbeeldexamenvragen.

## Algemene notatie
- $X, Y$: (toevals)variabelen / grootheden.
- $x, y$: concrete waarden van $X$ of $Y$.
- $x_i, X_i$: i-de waarneming (index $i$).
- $i$: index (telvariabele).
- $\sum$: somteken.
- $\sqrt{\cdot}$: vierkantswortel.

## Operatoren (formules)
- $\cdot$: vermenigvuldigen.
- $\pm$: plus/min.
- $\approx$: ongeveer gelijk (benadering).
- $\sim$: "is verdeeld als" (bv. $X\sim \mathcal{N}(\mu,\sigma^2)$).
- $\mid$: "gegeven" (voorwaardelijke kans), bv. $P(B\mid A)$.
- $^2$: in het kwadraat (bv. $s^2$, $\sigma^2$, $X_i^2$).

## Beschrijvende statistiek

### Frequentietabellen (gegroepeerde data)
- $f_i$: absolute frequentie van klasse/waarde $i$.
- $f_m$: frequentie van de mediaanklasse.
- $f_{Q1}$, $f_{Q3}$: frequentie van de kwartielklasse.
- $cf$: cumulatieve frequentie.
  - In het formularium zie je o.a. $cf_{m-1}$ (cumulatieve frequentie tot en met de klasse v\'o\'or de mediaanklasse).
  - Ook $cf_{Q1-1}$ en $cf_{Q3-1}$ (analoog voor kwartielen).
- $l$: ondergrens van een klasse (mediaan/kwartiel/modus-klasse).
- $b$: klassenbreedte.
- $m_i$ of $X_i$: klassenmidden (bij gegroepeerde berekeningen met $\sum f_i X_i$).
- $\Delta_1, \Delta_2$: frequentieverschillen links/rechts van de modale klasse (modusformule).

### Centrummaten
- $\bar{X}$: (steekproef)gemiddelde.
- $\bar{X}_1, \bar{X}_2$: gemiddelden van steekproef 1 en 2.
- $Me$: mediaan.
- $Mo$: modus.
- $Q_1, Q_3$: eerste en derde kwartiel.

### Spreiding
- $s$: steekproefstandaardafwijking.
- $s^2$: steekproefvariantie.
- $s_1^2, s_2^2$: steekproefvarianties van groep 1 en 2.
- $\sigma$: populatiestandaardafwijking.
- $\sigma^2$: populatievariantie.
- $\overline{X^2}$: gemiddelde van de kwadraten (komt voor in $s = \sqrt{\overline{X^2} - \bar{X}^2}$).
- $Q$: interkwartielafstand: $Q = Q_3 - Q_1$.
- $V$: variatiecoefficient: $V = \frac{s}{\bar{X}}$.

### Vormparameters
- $Sk_p$: Pearson-scheefheid (in het formularium: $Sk_p = \frac{\bar{X} - Mo}{s}$).
- $Sk_B$: Bowley-scheefheid (op basis van kwartielen).

## Kansrekening

### Gebeurtenissen
- $P(A)$: kans op gebeurtenis $A$.
- $\overline{A}$ of $A^c$: complement van $A$ (A gebeurt niet).
- $A \cup B$: unie (A of B of beide).
- $A \cap B$: doorsnede (A en B).
- $P(B\mid A)$: voorwaardelijke kans.

### Wet van totale kans & Bayes
- $O_i$: gebeurtenis/oorzaak $i$ in een partitie (totale kans/Bayes).
- $O_k$: de specifieke oorzaak $k$ waarvan je $P(O_k\mid A)$ zoekt.

## Toevalsvariabelen
- $E(X)$: verwachtingswaarde van $X$.
- $E(X^2)$: verwachting van $X^2$.
- $E(XY)$: verwachting van het product $XY$ (komt voor in covariantie).
- $\operatorname{Var}(X)$: variantie van $X$.
- $\sigma(X)$: standaardafwijking van $X$ (in het formularium: $\sigma(X)=\sqrt{\operatorname{Var}(X)}$).
- $\operatorname{Cov}(X,Y)$: covariantie tussen $X$ en $Y$.

## Verdelingen

### Combinaties
- $\binom{n}{k}$ en $C_n^k$: combinatiegetal (binomiale coefficient).
- $n!$: faculteit (bij combinatiegetallen).

### Binomiaal
- $X \sim \mathcal{B}(n,p)$: $X$ is binomiaal verdeeld met parameters $n$ en $p$.
- $p$: kans op succes.
- $q$: kans op falen, $q = 1 - p$.
- $n$: aantal onafhankelijke proeven.
- $k$: aantal successen.

### Poisson
- $X \sim \mathrm{Poisson}(\lambda)$: $X$ is Poisson verdeeld met parameter $\lambda$.
- $\lambda$: Poisson-parameter (gemiddelde aantal gebeurtenissen per interval).
- $e$: het getal van Euler (basis van natuurlijke logaritmen), komt voor in $e^{-\lambda}$.

### Normaal + standaardisatie
- $X \sim \mathcal{N}(\mu, \sigma^2)$: $X$ is normaal verdeeld met gemiddelde $\mu$ en variantie $\sigma^2$.
- $Z$: gestandaardiseerde normale variabele: $Z = \frac{X-\mu}{\sigma}$.

## Steekproefverdelingen
- $\sigma_{\bar{X}}$: standaardfout van het gemiddelde ($\sigma/\sqrt{n}$).
- $t$: t-variabele / toetsingsgrootheid in t-context.

Let op: de noemer bij standaardfouten voor een gemiddelde is vrijwel altijd $\sqrt{n}$. Soms zie je per ongeluk $\sqrt{n-1}$ staan; dat is meestal verwarring met $df=n-1$.

## Betrouwbaarheidsintervallen
- $\alpha$: significantieniveau. (Bij BI: $1-\alpha$ is het betrouwbaarheidsniveau.)
- $a$: toegelaten foutenmarge (half-breedte van het interval) in de formule voor benodigde $n$.
- $z_{\alpha}$: kritieke z-waarde zoals genoteerd in het formularium.
  - In veel cursussen zie je ook $z_{\alpha/2}$ bij tweezijdige intervallen; volg hier de notatie van je tabel/vragen.
- $t_{\alpha}$: kritieke t-waarde zoals genoteerd in het formularium.
  - Vaak geschreven als $t_{\alpha/2, df}$ (met vrijheidsgraden).
- $df$: vrijheidsgraden (typisch $n-1$).

## Som en verschil
- $\mu_{X\pm Y}$: gemiddelde van $X\pm Y$.
- $\sigma_{X\pm Y}$: standaardafwijking van $X\pm Y$.
- $\sigma_{\bar{X}-\bar{Y}}$: standaardfout van het verschil van twee steekproefgemiddelden.

## Hypothesetoetsen
- $H_0$: nulhypothese.
- $H_1$: alternatieve hypothese.
- $\mu_0$: veronderstelde waarde onder $H_0$.
- $Z$: toetsingsgrootheid bij z-toets (let op: dit is een andere rol dan $Z$ bij standaardisatie, maar vaak dezelfde letter).
- $z$: toetsingsgrootheid bij z-toets (zelfde idee, andere schrijfwijze).
- $t$: toetsingsgrootheid bij t-toets.
- $\alpha$: kans op type I fout (vals alarm).
- $\beta$: kans op type II fout (gemiste kans).

## ⭐ Top 15 symbolen (snelle herhaling)
- $\bar{X}$: steekproefgemiddelde.
- $\mu$: populatiegemiddelde.
- $\sigma$: populatiestandaardafwijking.
- $s$: steekproefstandaardafwijking.
- $n$: steekproefgrootte.
- $P(A)$: kans op gebeurtenis $A$.
- $P(B\mid A)$: voorwaardelijke kans.
- $\binom{n}{k}$: combinatiegetal.
- $p, q$: succes- en faalkans.
- $\lambda$: Poisson-parameter.
- $Z$: standaardiseren / z-toets (context!).
- $E(X)$: verwachtingswaarde.
- $\sigma_{\bar{X}}$: standaardfout.
- $z_{\alpha}$: kritieke z-waarde.
- $H_0, H_1$: nul- en alternatieve hypothese.

## 🧪 Formule-voorbeelden (herken het symbool)
- Mediaan (gegroepeerd): $Me = l + \frac{\frac{n}{2} - cf_{m-1}}{f_m} \cdot b$
- Variantie rekenregel: $\operatorname{Var}(X)=E(X^2)-(E(X))^2$
- Standaardiseren: $Z = \frac{X-\mu}{\sigma}$
- Binomiaal: $P(X=k) = \binom{n}{k} p^k q^{n-k}$

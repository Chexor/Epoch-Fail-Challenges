# Symbolen en tekens - uitleg (Data Analysis)

## ✅ SSOT
- Dit is de **authoritative** lijst met symbolen en notatie.
- Aanpassingen gebeuren hier; andere notities linken hiernaartoe.

Deze lijst dekt de symbolen/tekens uit het formularium en de voorbeeldvragen.

## Algemene notatie
- $X, Y$: toevalsveranderlijken (random variables).
- $x, y$: concrete waarden van $X$ of $Y$.
- $x_i$: i-de waarneming.
- $\bar{X}$: steekproefgemiddelde.
- $\mu$: populatiegemiddelde.
- $\sigma$: populatiestandaardafwijking.
- $s$: steekproefstandaardafwijking.
- $s^2$: steekproefvariantie.
- $n$: steekproefgrootte.
- $n_1, n_2$: steekproefgrootten van groep 1 en 2.
- $i$: index (telvariabele).
- $\sum$: somteken (Sigma).
- $\sqrt{\cdot}$: vierkantswortel.

## Frequentietabellen
- $f_i$: absolute frequentie in klasse $i$.
- $cf_i$: cumulatieve absolute frequentie t/m klasse $i$.
- $h_i$: relatieve frequentie in klasse $i$.
- $ch_i$: cumulatieve relatieve frequentie t/m klasse $i$.
- $m_i$: intervalmidden van klasse $i$.
- $l$: ondergrens van (mediaan/kwartiel/modus) klasse.
- $b$: klassebreedte.
- $\Delta_1, \Delta_2$: hoogteverschillen links/rechts van de modusklasse.

## Centrummaten en kwartielen
- $Me$: mediaan.
- $Mo$: modus.
- $Q_1, Q_3$: eerste en derde kwartiel.
- $Q$: interkwartielafstand, $Q = Q_3 - Q_1$.
- $\bar{X}$: rekenkundig gemiddelde (soms aangeduid als $X$).

## Spreiding en vorm
- $\operatorname{Var}(X)$: variantie van $X$.
- $\operatorname{Cov}(X, Y)$: covariantie van $X$ en $Y$.
- $Sk_P$: Pearson-scheefheid.
- $Sk_B$: Bowley-scheefheid.
- $V$: variatiecoefficient, $V = \frac{s}{\bar{X}}$.

## Kansrekening
- $P(A)$: kans op gebeurtenis $A$.
- $\bar{A}$ (of $A'$): complement van $A$ (A gebeurt niet).
- $A \cup B$: unie (A of B of beide).
- $A \cap B$: doorsnede (A en B).
- $P(A \mid B)$: voorwaardelijke kans van A gegeven B.
- $O_i$: i-de mogelijke uitkomst/gebeurtenis in totale kans.

## Verwachtingswaarde
- $E(X)$: verwachtingswaarde van $X$.
- $E(X^2)$: verwachting van $X^2$.

## Verdelingen
- $\binom{n}{k}$: combinatiegetal (n boven k).
- Binomiaal: $X \sim \mathcal{B}(n, p)$.
- Poisson: $X \sim \mathrm{Poisson}(\lambda)$.
- Normaal: $X \sim \mathcal{N}(\mu, \sigma^2)$.
- $Z$: gestandaardiseerde normale variabele.
- $p$: succeskans.
- $q$: $1 - p$.
- $\lambda$: Poisson-parameter (gemiddelde).

## Steekproefgemiddelde en standaardfout
- $\bar{X}$: steekproefgemiddelde.
- $\sigma_{\bar{X}}$: standaardfout van $\bar{X}$, $\sigma / \sqrt{n}$.
- $s_{\bar{X}}$: schatting van standaardfout met $s$.

## Betrouwbaarheidsintervallen
- $\alpha$: significantieniveau (1 - betrouwbaarheidsniveau).
- $z_{\alpha/2}$: kritieke z-waarde voor interval.
- $t_{\alpha/2, df}$: kritieke t-waarde met $df$ vrijheidsgraden.
- $a$: maximale foutmarge (half-breedte van interval).
- $df$: vrijheidsgraden (meestal $n - 1$).

## Som en verschil van variabelen
- $\mu_{X+Y}$: gemiddelde van $X + Y$.
- $\mu_{X-Y}$: gemiddelde van $X - Y$.
- $\sigma_{X+Y}$: standaardafwijking van $X + Y$.
- $\sigma_{X-Y}$: standaardafwijking van $X - Y$.

## Hypothesetoetsen
- $H_0$: nulhypothese.
- $H_1$: alternatieve hypothese.
- $z$: toetsingsgrootheid bij z-toets.
- $t$: toetsingsgrootheid bij t-toets.
- $z_{\text{obs}}, t_{\text{obs}}$: geobserveerde toetsingsgrootheid.
- $\alpha$: significantieniveau.
- $\beta$: kans op type II fout.

## ⭐ Top 15 symbolen (snelle herhaling)
- $\bar{X}$: steekproefgemiddelde.
- $\mu$: populatiegemiddelde.
- $\sigma$: populatiestandaardafwijking.
- $s$: steekproefstandaardafwijking.
- $n$: steekproefgrootte.
- $P(A)$: kans op gebeurtenis $A$.
- $P(A \mid B)$: voorwaardelijke kans.
- $\binom{n}{k}$: combinatiegetal.
- $X \sim \mathcal{B}(n, p)$: binomiale verdeling.
- $X \sim \mathcal{N}(\mu, \sigma^2)$: normale verdeling.
- $Z$: gestandaardiseerde normale variabele.
- $E(X)$: verwachtingswaarde.
- $\sigma_{\bar{X}}$: standaardfout.
- $z_{\alpha/2}$: kritieke z-waarde.
- $H_0, H_1$: nul- en alternatieve hypothese.

## 🧪 Formule-voorbeelden per symbool
- $\bar{X} = \frac{1}{n}\sum_{i=1}^{n} x_i$
- $s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{X})^2$
- $\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}}$
- $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$
- $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- $\binom{n}{k} = \frac{n!}{k!(n-k)!}$
- $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$
- $Z = \frac{X-\mu}{\sigma}$
- $z = \frac{\bar{X} - \mu_0}{\sigma/\sqrt{n}}$
- $t = \frac{\bar{X} - \mu_0}{s/\sqrt{n}}$
- $\text{BI: } \bar{X} \pm z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$

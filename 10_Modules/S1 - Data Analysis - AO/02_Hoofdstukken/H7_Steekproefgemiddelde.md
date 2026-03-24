# H7: Steekproefverdeling van het gemiddelde

## ✅ SSOT
- Dit is de **authoritative** hoofdstuknote voor H7.
- Afgeleide samenvattingen moeten hiernaar linken.

## 1. Verdeling van het steekproefgemiddelde
- Neem alle mogelijke steekproeven van grootte $n$.
- Bereken telkens het steekproefgemiddelde $\bar{X}$.
- De verdeling van $\bar{X}$ heet de **steekproefverdeling**.

### Als de populatie normaal verdeeld is
- $X \sim N(\mu,\sigma)$.
- Dan: $\bar{X} \sim N\left(\mu, \frac{\sigma}{\sqrt{n}}\right)$.
- Grotere $n$ => kleinere spreiding van $\bar{X}$.

### Centrale limietstelling (CLT)
- Ook als $X$ **niet** normaal is:
  - $\bar{X}$ wordt ongeveer normaal bij voldoende grote $n$.
  - Gemiddelde $\mu$ en standaardfout $\sigma/\sqrt{n}$.

## 2. t-verdeling ($\sigma$ onbekend)
- In de praktijk is $\sigma$ vaak onbekend.
- Gebruik de steekproefstandaardafwijking $s$./
- Dan is:
  - $t=\frac{\bar{X}-\mu}{s/\sqrt{n}} \sim t_{\nu}$ met $\nu=n-1$ vrijheidsgraden.

### Eigenschappen
- Lijkt op standaardnormaal, maar met dikkere staarten.
- Hoe groter $n$, hoe dichter bij $N(0,1)$.

## 3. Tabellen
- t-tabellen geven kritieke waarden voor onder- of overschrijdingskansen.
- Let op het juiste aantal vrijheidsgraden ($n-1$).

## 4. Examenvallen
- Gebruik $t$ (niet $z$) wanneer $\sigma$ onbekend is.
- Standaardfout altijd $\sigma/\sqrt{n}$ of $s/\sqrt{n}$.

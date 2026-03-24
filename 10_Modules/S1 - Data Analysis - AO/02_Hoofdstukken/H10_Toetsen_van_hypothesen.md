# H10: Toetsen van hypothesen

## ✅ SSOT
- Dit is de **authoritative** hoofdstuknote voor H10.
- Afgeleide samenvattingen moeten hiernaar linken.

## 1. Doel en types toetsen
- **Doel**: beslissen of een verschil toevallig is of significant.
- **Eerste soort**: vergelijk populatieparameter met steekproefparameter.
- **Tweede soort**: verschil tussen twee steekproefparameters vergelijken.

## 2. Hypothesen en fouten
### Hypothesen
- **Nulhypothese** $H_0$: geen verschil of vaste waarde $\mu_0$.
- **Alternatieve hypothese** $H_1$: wel verschil.
- Tweezijdig: $H_1: \mu \neq \mu_0$.
- Eenzijdig: $H_1: \mu < \mu_0$ of $H_1: \mu > \mu_0$.

### Type I en Type II
- Type I-fout: $H_0$ onterecht verwerpen, kans $\alpha$.
- Type II-fout: $H_0$ onterecht aanvaarden, kans $\beta$.
- Als $\alpha$ daalt, stijgt $\beta$.
- **Onderscheidingsvermogen**: $1-\beta$.

## 3. Algemene toetsprocedure
- Formuleer $H_0$ en $H_1$.
- Kies significantieniveau $\alpha$.
- Bereken toetsingsgrootheid en beslis.

## 4. Z-toets van een gemiddelde ($\sigma$ bekend)
### Voorwaarden
- $X$ bij benadering normaal verdeeld.
- $\sigma$ bekend (of $n \ge 30$ en $\sigma$ vervangen door $s$).

### Toetsingsgrootheid
- $z=\frac{\bar{X}-\mu_0}{\sigma/\sqrt{n}}$.

### Beslissing
- Tweezijdig: verwerp als $|z|>z_{\alpha/2}$.
- Eenzijdig: verwerp als $z<-z_{\alpha}$ of $z>z_{\alpha}$.

## 5. t-toets van een gemiddelde ($\sigma$ onbekend)
### Voorwaarden
- $X$ bij benadering normaal verdeeld.

### Toetsingsgrootheid
- $t=\frac{\bar{X}-\mu_0}{s/\sqrt{n}} \sim t_{\nu}$ met $\nu=n-1$.

### Beslissing
- Tweezijdig: verwerp als $|t|>t_{\alpha/2,\nu}$.
- Eenzijdig: verwerp als $t<-t_{\alpha,\nu}$ of $t>t_{\alpha,\nu}$.

## 6. Z-toets voor twee gemiddelden ($\sigma$'s bekend)
### Voorwaarden
- $X_1, X_2$ bij benadering normaal.
- $\sigma_1, \sigma_2$ bekend.
- Steekproeven onafhankelijk.

### Toetsingsgrootheid
- $z=\frac{(\bar{X}-\bar{Y})-(\mu_1-\mu_2)}{\sqrt{\sigma_1^2/n_1+\sigma_2^2/n_2}}$.

## 7. t-toets voor twee gemiddelden ($\sigma$'s onbekend)
### Voorwaarden
- $X$ en $Y$ bij benadering normaal.
- $\sigma_1^2=\sigma_2^2$ verondersteld maar onbekend.
- Steekproeven onafhankelijk.

### Gepoolde variantie
- $s_p^2=\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}$.

### Toetsingsgrootheid
- $t=\frac{(\bar{X}-\bar{Y})-(\mu_1-\mu_2)}{s_p\sqrt{1/n_1+1/n_2}} \sim t_{\nu}$ met $\nu=n_1+n_2-2$.

## 8. P-waarde
- P-waarde = overschrijdingskans van de toetsingsgrootheid.
- Grootste $\alpha$ waarbij $H_0$ nog net aanvaard wordt (eenzijdig).
- Kleine P-waarde = meer bewijs tegen $H_0$.

## 9. Examenvallen
- Kies tweezijdig vs eenzijdig **voor** het rekenen.
- Tweezijdige test is strenger dan eenzijdig bij hetzelfde $\alpha$.
- Onafhankelijkheid expliciet checken bij twee steekproeven.

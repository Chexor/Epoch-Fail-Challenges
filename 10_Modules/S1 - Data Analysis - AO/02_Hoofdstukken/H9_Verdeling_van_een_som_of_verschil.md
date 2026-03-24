# H9: Verdeling van een som of verschil

## ✅ SSOT
- Dit is de **authoritative** hoofdstuknote voor H9.
- Afgeleide samenvattingen moeten hiernaar linken.

## 1. Doel
- Twee steekproeven uit dezelfde of verschillende populaties vergelijken.
- Verschil of som interpreteren via verdelingen.

## 2. Som of verschil van twee variabelen (algemeen)
### Onafhankelijke variabelen
- Als $X \sim N(\mu_X,\sigma_X)$ en $Y \sim N(\mu_Y,\sigma_Y)$, dan:
- $X+Y \sim N(\mu_X+\mu_Y,\sqrt{\sigma_X^2+\sigma_Y^2})$.
- $X-Y \sim N(\mu_X-\mu_Y,\sqrt{\sigma_X^2+\sigma_Y^2})$.

### Speciaal geval (zelfde populatie)
- Als $X,Y \sim N(\mu,\sigma)$, dan:
- $X-Y \sim N(0,\sqrt{2\sigma^2})$.

### Uitbreiding (som van meerdere variabelen)
- Als $X_i$ onafhankelijk, dan:
- $\sum X_i$ heeft gemiddelde $\sum \mu_i$ en variantie $\sum \sigma_i^2$.

## 3. Verschil van twee steekproefgemiddelden ($\sigma$ bekend)
### Algemeen
- $\bar{X} \sim N\left(\mu_1,\frac{\sigma_1}{\sqrt{n_1}}\right)$ en $\bar{Y} \sim N\left(\mu_2,\frac{\sigma_2}{\sqrt{n_2}}\right)$.
- $\bar{X}-\bar{Y} \sim N\left(\mu_1-\mu_2,\sqrt{\frac{\sigma_1^2}{n_1}+\frac{\sigma_2^2}{n_2}}\right)$.

### Speciaal geval (zelfde populatie, zelfde steekproeflengte)
- Als $\mu_1=\mu_2=\mu$ en $\sigma_1=\sigma_2=\sigma$ en $n_1=n_2=n$:
- $\bar{X}-\bar{Y} \sim N\left(0,\sqrt{\frac{2\sigma^2}{n}}\right)$.

## 4. Verschil van twee steekproefgemiddelden ($\sigma$ onbekend)
### Voorwaarde
- Veronderstel $\sigma_1^2=\sigma_2^2=\sigma^2$, maar onbekend.

### Gepoolde variantie
- $s_p^2=\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}$.

### t-statistiek
- $t=\frac{\bar{X}-\bar{Y}-(\mu_1-\mu_2)}{s_p\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}} \sim t_{\nu}$ met $\nu=n_1+n_2-2$.

### Opmerkingen
- Vrijheidsgraden: $\nu=n_1+n_2-2$ (zie t-tabel).
- Toepassing op kansberekening komt terug in H10.

## 5. Examenvallen
- Controleer altijd **onafhankelijkheid**.
- Gebruik $z$ als $\sigma$ bekend is, $t$ bij $\sigma$ onbekend.
- Bij gelijke populaties kan je de speciale formules gebruiken.

# 📘 Formularium Data Analysis

Een gestructureerd overzicht van de belangrijkste formules uit beschrijvende statistiek, kansrekening en statistische inferentie.

---

# 1️⃣ Beschrijvende statistiek

## 1.1 Centrummaten

### Rekenkundig gemiddelde

$$
\bar{X} = \frac{\sum X_i}{n}
$$

$$
\bar{X} = \frac{\sum f_i X_i}{n}
$$

$$
\sum X_i = n \cdot \bar{X}
$$

Gecombineerd gemiddelde:

$$
\bar{X} = \frac{n_1 \bar{X}_1 + n_2 \bar{X}_2}{n_1 + n_2}
$$

---

### Mediaan (gegroepeerde gegevens)

$$
Me = l + \frac{\frac{n}{2} - cf_{m-1}}{f_m} \cdot b
$$

---

### Kwartielen

$$
Q_1 = l + \frac{\frac{n}{4} - cf_{Q1-1}}{f_{Q1}} \cdot b
$$

$$
Q_3 = l + \frac{\frac{3n}{4} - cf_{Q3-1}}{f_{Q3}} \cdot b
$$

---

### Modus

$$
Mo = l + \frac{\Delta_1}{\Delta_1 + \Delta_2} \cdot b
$$

---

### Verband tussen gemiddelde, mediaan en modus

$$
\bar{X} - Mo = 3(\bar{X} - Me)
$$

---

## 1.2 Spreidingsmaten

### Standaardafwijking

$$
s = \sqrt{\frac{1}{n} \sum (X_i - \bar{X})^2}
$$

$$
s = \sqrt{\frac{1}{n} \sum f_i (X_i - \bar{X})^2}
$$

$$
s = \sqrt{\overline{X^2} - \bar{X}^2}
$$

---

### Alternatieve schrijfwijze

$$
\sum X_i^2 = n(s^2 + \bar{X}^2)
$$

---

### Gecombineerde variantie

$$
s^2 =
\frac{n_1 s_1^2 + n_2 s_2^2}{n_1 + n_2}
+
\frac{n_1(\bar{X}_1 - \bar{X})^2 + n_2(\bar{X}_2 - \bar{X})^2}{n_1 + n_2}
$$

---

### Interkwartielafstand

$$
Q = Q_3 - Q_1
$$

Benaderingen:

$$
Q \approx \frac{4}{3}s
$$

$$
s \approx 0{,}75Q
$$

---

### Variatiecoëfficiënt

$$
V = \frac{s}{\bar{X}}
$$

---

## 1.3 Vormparameters

### Scheefheid

$$
Sk_p = \frac{\bar{X} - Mo}{s}
$$

$$
Sk_B = \frac{(Q_3 - Me) - (Me - Q_1)}{Q_3 - Q_1}
$$

---

# 2️⃣ Kansrekening

$$
P(A) = \frac{\text{gunstige uitkomsten}}{\text{mogelijke uitkomsten}}
$$

$$
P(A) = 1 - P(\bar{A})
$$

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

Voor onafhankelijke gebeurtenissen:

$$
P(A \cap B) = P(A)P(B)
$$

Algemeen:

$$
P(A \cap B) = P(A)P(B|A)
$$

---

## Wet van totale kans

$$
P(A) = \sum P(O_i)P(A|O_i)
$$

## Regel van Bayes

$$
P(O_k|A) = \frac{P(O_k)P(A|O_k)}{\sum P(O_i)P(A|O_i)}
$$

---

# 3️⃣ Toevalsveranderlijken

## Verwachtingswaarde en variantie

$$
E(X) = \sum x_i P(X = x_i)
$$

$$
Var(X) = E(X^2) - (E(X))^2
$$

$$
\sigma(X) = \sqrt{Var(X)}
$$

Lineaire eigenschappen:

$$
E(X \pm Y) = E(X) \pm E(Y)
$$

Voor onafhankelijke variabelen:

$$
Var(X+Y) = Var(X) + Var(Y)
$$

$$
Cov(X,Y) = E(XY) - E(X)E(Y)
$$

---

# 4️⃣ Kansverdelingen

## Combinaties

$$
C_n^k = \frac{n!}{k!(n-k)!}
$$

---

## Binomiale verdeling

$$
P(X=k) = C_n^k p^k q^{n-k}
$$

$$
E(X) = np
$$

$$
\sigma(X) = \sqrt{npq}
$$

---

## Poissonverdeling

$$
P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}
$$

$$
E(X) = \lambda
$$

---

## Normale verdeling (standaardisatie)

$$
Z = \frac{X-\mu}{\sigma}
$$

---

# 5️⃣ Steekproefverdelingen

$$
\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}}
$$

$$
t = \frac{\bar{X}-\mu}{s/\sqrt{n-1}}
$$

---

# 6️⃣ Betrouwbaarheidsintervallen

## Z-interval

$$
\bar{X} \pm z_\alpha \frac{\sigma}{\sqrt{n}}
$$

Benodigde steekproefgrootte:

$$
n = \left(\frac{z_\alpha \sigma}{a}\right)^2
$$

---

## t-interval

$$
\bar{X} \pm t_\alpha \frac{s}{\sqrt{n-1}}
$$

---

# 7️⃣ Som en verschil van gemiddelden

$$
\mu_{X \pm Y} = \mu_X \pm \mu_Y
$$

$$
\sigma_{X \pm Y} = \sqrt{\sigma_X^2 + \sigma_Y^2}
$$

Voor steekproefgemiddelden:

$$
\sigma_{\bar{X} - \bar{Y}} = \sqrt{\frac{\sigma_X^2}{n_1} + \frac{\sigma_Y^2}{n_2}}
$$

---

# 8️⃣ Hypothesetoetsing

## Z-toets (één gemiddelde)

$$
Z = \frac{\bar{X}-\mu_0}{\sigma/\sqrt{n}}
$$

---

## t-toets (één gemiddelde)

$$
t = \frac{\bar{X}-\mu_0}{s/\sqrt{n-1}}
$$

---

## Z-toets voor verschil van gemiddelden

$$
Z = \frac{\bar{X}-\bar{Y}}{\sqrt{\frac{\sigma_X^2}{n_1} + \frac{\sigma_Y^2}{n_2}}}
$$

---

## t-toets voor verschil van gemiddelden

$$
t = \frac{\bar{X}-\bar{Y}}{\sqrt{\frac{n_1 s_1^2 + n_2 s_2^2}{n_1+n_2-2} \left( \frac{1}{n_1} + \frac{1}{n_2} \right)}}
$$

---

# 📖 Legenda van symbolen

> **Tip (Obsidian Canvas):** inline wiskunde wordt het meest consistent gerenderd met `\( … \)`.

## Algemene statistiek

- \(X\) : toevalsveranderlijke of observatie  
- \(X_i\) : i-de waarneming  
- \(\bar{X}\) : steekproefgemiddelde  
- \(\bar{X}_1,\,\bar{X}_2\) : gemiddelden van steekproef 1 en 2  
- \(\mu\) : populatiegemiddelde  
- \(\mu_0\) : veronderstelde waarde onder \(H_0\) (nulhypothese)  
- \(n\) : steekproefgrootte  
- \(n_1,\,n_2\) : steekproefgroottes van groep 1 en 2  
- \(f_i\) : (absolute) frequentie van klasse/waarde \(i\)  
- \(cf\) : cumulatieve frequentie  
- \(l\) : ondergrens van een klasse  
- \(b\) : klassenbreedte  
- \(Me\) : mediaan  
- \(Mo\) : modus  
- \(Q_1,\,Q_3\) : eerste en derde kwartiel  
- \(Q\) : interkwartielafstand  
- \(\Delta_1,\,\Delta_2\) : frequentieverschillen bij de modusformule  

---

## Spreiding

- \(s\) : steekproefstandaardafwijking  
- \(s^2\) : steekproefvariantie  
- \(\sigma\) : populatiestandaardafwijking  
- \(\sigma^2\) : populatievariantie  
- \(V\) : variatiecoëfficiënt  

---

## Kansrekening

- \(P(A)\) : kans op gebeurtenis \(A\)  
- \(A \cap B\) : doorsnede (A én B)  
- \(A \cup B\) : unie (A of B)  
- \(\overline{A}\) : complement van \(A\)  
- \(P(B\mid A)\) : voorwaardelijke kans  
- \(O_i\) : gebeurtenis/oorzaak \(i\) in een partitie (totale kans/Bayes)  

---

## Toevalsveranderlijken

- \(E(X)\) : verwachtingswaarde van \(X\)  
- \(\operatorname{Var}(X)\) : variantie van \(X\)  
- \(\operatorname{Cov}(X,Y)\) : covariantie tussen \(X\) en \(Y\)  

---

## Verdelingen

- \(C_n^k\) : combinatiegetal (binomiale coëfficiënt)  
- \(p\) : kans op succes  
- \(q\) : kans op falen, met \(q = 1 - p\)  
- \(\lambda\) : parameter van de Poissonverdeling  
- \(Z\) : gestandaardiseerde normale variabele  

---

## Steekproefverdelingen en toetsing

- \(\sigma_{\bar{X}}\) : standaardfout van het gemiddelde  
- \(z_{\alpha}\) : kritieke z-waarde bij significantieniveau \(\alpha\)  
- \(t_{\alpha}\) : kritieke t-waarde bij significantieniveau \(\alpha\)  
- \(a\) : toegelaten foutenmarge  
- \(H_0\) : nulhypothese  
- \(H_1\) : alternatieve hypothese  
- \(\alpha\) : significantieniveau  
- \(Z\) : toetsingsgrootheid bij z-toets (normale benadering)  
- \(t\) : toetsingsgrootheid bij t-toets  


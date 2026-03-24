# H8: Betrouwbaarheidsintervallen

## ✅ SSOT
- Dit is de **authoritative** hoofdstuknote voor H8.
- Afgeleide samenvattingen moeten hiernaar linken.

## 1. Doel en begrippen
- Doel: uitspraak over populatiegemiddelde $\mu$ op basis van steekproefgemiddelde $\bar{X}$.
- **Puntschatting**: vervang $\mu$ door $\bar{X}$.
- **Intervalschatting**: bepaal een interval waarin $\mu$ waarschijnlijk ligt.
- Betrouwbaarheidsniveau: $1-\alpha$ (bv. 90%, 95%, 99%).
- **Foutmarge** $E$: halve breedte van het interval.
- Kritieke waarde: $z_{\alpha/2}$ of $t_{\alpha/2,\nu}$.
- Link met hfst 7: [[H7_Steekproefgemiddelde]].

## 2. Gemiddelde met $\sigma$ bekend (Z-interval)
### Voorwaarden
- Populatie normaal verdeeld **of** $n > 30$ (CLT).
- Populatiestandaardafwijking $\sigma$ is bekend.

### Formule
- $\bar{X} \pm z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$

### Kritieke z-waarden
- 90%: $z_{0{,}95}=1{,}645$
- 95%: $z_{0{,}975}=1{,}96$
- 99%: $z_{0{,}995}=2{,}58$

### Foutmarge (relaties)
- $E$ neemt toe als $z$ groter wordt.
- $E$ neemt toe als $\sigma$ groter wordt.
- $E$ neemt af als $n$ groter wordt (via $\sqrt{n}$).

## 3. Gemiddelde met $\sigma$ onbekend (t-interval)
### Idee
- Gebruik steekproefstandaardafwijking $s$.
- Teststatistiek volgt een t-verdeling met $\nu=n-1$ vrijheidsgraden.

### Formule
- $\bar{X} \pm t_{\alpha/2,\nu} \cdot \frac{s}{\sqrt{n}}$

### Opmerkingen
- Interval is meestal **breder** dan bij $\sigma$ bekend.
- Voor $n>30$ is $t$-interval bijna gelijk aan $z$-interval.

## 4. Stappenplan
- Kies betrouwbaarheidsniveau $1-\alpha$.
- Bepaal of $\sigma$ bekend is (z) of onbekend (t).
- Bereken $\bar{X}$, $s$ (indien nodig) en standaardfout.
- Zoek kritieke waarde en bouw het interval.

## 5. Examenvallen
- Gebruik **t** wanneer $\sigma$ onbekend is.
- Hogere betrouwbaarheid => breder interval.
- Groter $n$ => smaller interval.
- Standaardfout is altijd $\sigma/\sqrt{n}$ of $s/\sqrt{n}$.

# H6: Enkele kansverdelingen

## ✅ SSOT
- Dit is de **authoritative** hoofdstuknote voor H6.
- Afgeleide samenvattingen moeten hiernaar linken.

## 1. Herhaling: combinatieleer
- **Combinaties:** $\binom{n}{k}$ manieren om $k$ elementen te kiezen uit $n$.
- **Driehoek van Pascal:** levert de combinatiefactoren.
- **Binomium van Newton:** $(a+b)^n=\sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}$.

## 2. Bernoulli-experiment en -proces
- **Bernoulli-experiment:** twee uitkomsten (succes/mislukking).
- **Kans op succes:** $P(S)=p$, mislukking $P(M)=q=1-p$.
- **Bernoulli-proces:** herhaling met vaste $p$.

## 3. Binomiale verdeling
- **Definitie:** $X$ = aantal successen in $n$ onafhankelijke Bernoulli-experimenten.
- **Notatie:** $X \sim B(n,p)$.
- **Kansfunctie:** $P(X=k)=\binom{n}{k} p^k q^{n-k}$.

### Eigenschappen
- **Verwachtingswaarde:** $E(X)=np$.
- **Variantie:** $Var(X)=npq$.
- **Symmetrie:** bij $p=0,5$ of bij grote $n$ (meer symmetrisch).

## 4. Poissonverdeling (zeldzame gebeurtenissen)
- **Limietgeval** van binomiaal bij groot $n$ en klein $p$.
- **Parameter:** $\lambda = E(X)=np$.
- **Notatie:** $X \sim P(\lambda)$.
- **Kansfunctie:** $P(X=k)=\frac{e^{-\lambda} \lambda^k}{k!}$.

### Eigenschappen
- $E(X)=\lambda$.
- $Var(X)=\lambda$.
- Symmetrischer als $\lambda$ groter wordt.

## 5. Normale verdeling
- **Notatie:** $X \sim N(\mu,\sigma)$.
- **Dichtheidsfunctie:** klokvorm van Gauss.
- **Betekenis:** $\mu=E(X)$, $\sigma$ is de spreiding.
- **Oppervlakte onder de curve:** 1.

### Kansberekening
- **Methode 1:** integraal.
- **Methode 2:** standaardiseren naar $Z$ en tabellen.

## 6. Normale benadering van binomiaal
- Gebruik bij **voldoende grote** $n$ en **niet te extreme** $p$.
- Controleer symmetrie en gebruik **continuiteitscorrectie**.

## 7. Examenvallen
- Poisson alleen bij **zeldzame** gebeurtenissen.
- Binomiaal vs. Poisson: check $n$ groot en $p$ klein.
- Normale benadering: altijd **continuiteitscorrectie** toepassen.

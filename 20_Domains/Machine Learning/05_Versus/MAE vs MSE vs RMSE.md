---
type: versus
domain: "machine-learning"
parent: "Model Evaluation"
related:
  - MAE (Mean Absolute Error)
  - MSE (Mean Squared Error)
  - RMSE (Root Mean Squared Error)
theme: "model-evaluation"
aliases:
  - MAE vs MSE vs RMSE
---

# MAE vs MSE vs RMSE
#concept #ml

MAE vs MSE vs RMSE kort uitgelegd: wat het is, waarom het telt en wanneer je het gebruikt.
## Wat wordt hier vergeleken?
- [[MAE (Mean Absolute Error)]]
- [[MSE (Mean Squared Error)]]
- [[RMSE (Root Mean Squared Error)]]

## Kernverschil
Alle drie meten voorspelfouten, maar ze leggen een ander accent. MAE is het meest rechtstreeks interpreteerbaar, MSE straft grote fouten het hardst, en RMSE houdt dat strafmechanisme maar brengt de uitkomst terug naar dezelfde eenheid als de target.

## Vergelijking

| Aspect | MAE | MSE | RMSE |
| --- | --- | --- | --- |
| Doel | gemiddelde absolute fout | gemiddelde gekwadrateerde fout | wortel van de gemiddelde gekwadrateerde fout |
| Gevoeligheid voor outliers | lager | hoog | hoog |
| Eenheid | zelfde als target | gekwadrateerde eenheid | zelfde als target |
| Interpretatie | zeer direct | minder intuïtief | directer dan MSE |
| Typische fout | absolute waarde vergeten | eenheid verkeerd interpreteren | verwarren met MAE |

## Wanneer gebruik je wat?
- **MAE:** als uitlegbaarheid en robuustheid tegenover uitschieters belangrijk zijn.
- **MSE:** als grote fouten extra zwaar moeten doorwegen, bijvoorbeeld tijdens optimalisatie.
- **RMSE:** als je de straf voor grote fouten wil behouden maar toch een interpreteerbare schaal wil.

## Waarom is dit onderscheid belangrijk?
Deze drie foutmaten lijken sterk op elkaar, maar leiden tot andere intuities over modelkwaliteit. Als je hun verschil begrijpt, kun je sneller inschatten waarom een model “goed” of “slecht” lijkt onder een bepaalde evaluatiemethode.

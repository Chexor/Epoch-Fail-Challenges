# TI-36X Pro - Cheat Sheet (Data Analysis)

Alleen de functies die je typisch nodig hebt voor het examen Data Analysis (zoals in het voorbeeldexamen).

Zie ook: [[DA-Voorbeeldexamen-TI-36X-Pro-Manual]].

## Altijd eerst

- `2nd` `MODE` = QUIT (terug naar normaal scherm)
- `MODE` = instellingen (vooral display)
- Haakjes: gebruik ze altijd bij /, sqrt, machten, sommen.
- `ANS` = vorige uitkomst hergebruiken

## Geheugen (tussentijdse resultaten)

- `STO>` letter = opslaan
- `RCL` letter = terughalen

## Lijsten invoeren (DATA)

- `DATA` = lijst-editor (L1, L2, ...)
- Tip: wis/overschrijf oude lijstwaarden voor je een nieuwe oefening start

## 1-Var Stats (gemiddelde, s, kwartielen)

Pad:
- `2nd` `DATA` -> `1-Var Stats`

Instellingen:
- `Xlist = L1`
- `FRQ = 1` (geen frequenties) of `FRQ = L2` (met frequenties)

Aflezen (naam kan licht verschillen):
- `xbar`
- `Sx` (steekproef, noemer n-1)
- `sigma x` (populatie, noemer n)
- `n`
- `minX`, `Med`, `maxX` (en soms ook `Q1`, `Q3`)

Examen-tip:
- Als je oplossing/formule met noemer $n$ werkt: gebruik `sigma x`.
- Als je oplossing/formule met noemer $n-1$ werkt: gebruik `Sx`.

## Kansverdelingen (DISTR/PROB)

Open het distributiemenu via:
- `2nd` `DATA` (STAT-REG/DISTR) en kies `DISTR`/`PROB` (naam verschilt)

Normaal:
- `normalcdf(lower, upper, mu, sigma)`
  - Handig: `-1E99` en `1E99` als benadering van min/plus oneindig
- `invNorm(area, mu, sigma)`

Binomiaal:
- `binompdf(n, p, x)`
- `binomcdf(n, p, x)`

Student t (niet elk modelmenu heeft dit):
- `tcdf(lower, upper, df)`
- `invT(area, df)`
Als je geen `invT` hebt: gebruik de t-tabel uit je cursus.

## Snelle templates (typ zoals dit)

- Percent -> kans: `waarde/110*100`
- Interpolatie (gegroepeerde data): `L + ((positie - cf_voor)/f)*h`
- Z-score: `(x - mu)/sigma`
- Normale kans: `normalcdf(a, b, mu, sigma)`
- Continuiteitscorrectie: vervang bv. `P(X>=30)` door `P(X>=29.5)` bij normale benadering

## Controlepunten

- Wetenschappelijke notatie? `5.79E2` betekent `5.79*10^2`. Wil je dit “normaal”: pas display aan in `MODE`.

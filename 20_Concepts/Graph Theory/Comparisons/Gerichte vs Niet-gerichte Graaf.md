---
type: concept-comparison
domain: "graph-theory"
parent: "Graaf"
related:
  - Verbindingsmatrix
  - Graad van een knoop
theme: "graph-representation"
aliases:
  - Gerichte vs Niet-gerichte Graaf
---

# Gerichte vs Niet-gerichte Graaf
#concept #grafen

## Wat wordt hier vergeleken?
- [[Graaf]]
- [[Verbindingsmatrix]]

## Kernverschil
In een niet-gerichte graaf werkt een verbinding in beide richtingen. In een gerichte graaf telt de richting wel degelijk mee. Dat verschil verandert zowel de interpretatie van paden als de vorm van de verbindingsmatrix.

## Vergelijking

| Aspect | Niet-gerichte graaf | Gerichte graaf |
| --- | --- | --- |
| Richting | beide richtingen | richting telt |
| Matrix | symmetrisch | meestal niet symmetrisch |
| Graad | 1 soort graad | vaak in-graad en uit-graad |
| Interpretatie | wederzijdse relatie | overgang of eenrichtingsrelatie |
| Typische fout | richting vergeten expliciteren | doen alsof omgekeerde verbinding automatisch bestaat |

## Wanneer gebruik je wat?
- **Niet-gerichte graaf:** als verbindingen wederkerig zijn, zoals een gewone weg tussen twee steden.
- **Gerichte graaf:** als de volgorde of richting essentieel is, zoals web-links, overgangen of eenrichtingsverkeer.

## Waarom is dit onderscheid belangrijk?
Veel fouten in grafentheorie ontstaan doordat studenten onbewust van het ene model naar het andere springen. Als je dit onderscheid scherp ziet, interpreteer je ook matrices en graden correct.

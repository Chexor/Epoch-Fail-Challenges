---
type: theory
domain: "machine-learning"
parent: "Feature Scaling en Normalization"
related:
  - Feature Scaling en Normalization
  - Scaling
  - Standardization
theme: "data-preparation"
aliases:
  - Normalization
  - Min-max scaling
---

# Normalization
#concept #ml

Normalization is een techniek waarbij featurewaarden meestal naar een vast bereik worden herschaald, vaak tussen `0` en `1`.

## Korte kern

- brengt waarden vaak naar een begrensd interval
- maakt features beter vergelijkbaar
- wordt vaak via min-max scaling uitgevoerd

## 1. Wat is het kernprobleem?
Hoe breng je features met verschillende grootten naar eenzelfde bereik zodat modellen er evenwichtiger mee werken?

## 2. Intuitieve uitleg
Als een feature tussen `10` en `20` ligt en een andere tussen `1000` en `5000`, dan zijn ze moeilijk direct te vergelijken. Normalization duwt beide naar een gelijkaardig bereik.

## 3. Formele structuur
- typische formule: `(x - min(x)) / (max(x) - min(x))`
- na min-max normalization liggen waarden vaak in `[0, 1]`
- normalization verandert de schaal, maar bewaart de relatieve volgorde van waarden

## 4. Snelle vergelijking
- [[Normalization]] = naar een vast bereik herschalen
- [[Standardization]] = centreren rond gemiddelde en delen door standaardafwijking
- [[Scaling]] = bredere verzamelterm waar beide onder kunnen vallen

## 5. Toepassing
Als `temperatuur` tussen `15` en `35` ligt, kan normalization die waarden omzetten naar iets tussen `0` en `1`, zodat de feature numeriek beter samenwerkt met andere features.

## 6. Begripsafbakening en verbanden
- **Kernonderscheid:** normalization zet waarden typisch in een vast bereik; standardization doet dat niet noodzakelijk.
- **Veelvoorkomende misvatting:** denken dat normalization en standardization exact hetzelfde zijn.
- **Link met andere concepten:** [[Scaling]], [[Standardization]], [[Feature Scaling en Normalization]], [[Gradient Descent]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

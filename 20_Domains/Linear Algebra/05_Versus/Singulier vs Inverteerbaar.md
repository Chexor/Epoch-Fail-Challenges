---
type: versus
domain: "linear-algebra"
parent: "Determinant - Betekenis en Berekening"
related:
  - Inverse matrix
  - Eenheidsmatrix
theme: "matrix-invertibility"
aliases:
  - Singulier vs Inverteerbaar
---

# Singulier vs Inverteerbaar
#concept #linal

## Wat wordt hier vergeleken?
- [[Determinant - Betekenis en Berekening]]
- [[Inverse matrix]]

## Kernverschil
Een singuliere matrix is niet omkeerbaar. Een inverteerbare matrix heeft wel een inverse. In de praktijk komt het onderscheid neer op de vraag of de determinant nul is of niet.

## Vergelijking

| Aspect | Singulier | Inverteerbaar |
| --- | --- | --- |
| Determinant | `det(A) = 0` | `det(A) != 0` |
| Inverse bestaat | nee | ja |
| Geometrische betekenis | transformatie drukt informatie plat | transformatie blijft omkeerbaar |
| Stelsels | vaak geen unieke oplossing | unieke oplossing mogelijk |
| Typische fout | determinant en inverse los van elkaar zien | denken dat elke vierkante matrix inverteerbaar is |

## Wanneer gebruik je wat?
- **Singulier:** wanneer je wil aantonen dat een matrix informatie verliest of niet omkeerbaar is.
- **Inverteerbaar:** wanneer je een inverse wil berekenen of een stelsel met unieke oplossing wil rechtvaardigen.

## Waarom is dit onderscheid belangrijk?
Veel opgaven in lineaire algebra draaien uiteindelijk om deze vraag. Als je meteen ziet of een matrix singulier of inverteerbaar is, begrijp je ook sneller wat mogelijk is met determinant, inverse en rijreductie.

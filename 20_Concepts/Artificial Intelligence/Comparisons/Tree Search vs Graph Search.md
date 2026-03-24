---
type: concept-comparison
domain: "artificial-intelligence"
parent: Search Algorithm
related:
  - Search Algorithm
  - Frontier
  - Explored Set
theme: "search-with-or-without-repeated-state-control"
aliases:
  - Tree Search vs Graph Search
---

# Tree Search vs Graph Search
#concept #ai

## Wat wordt hier vergeleken?
- [[Search Algorithm]]
- [[Frontier]]
- [[Explored Set]]

## Kernverschil
`Tree search` behandelt elke nieuw gevonden route alsof die volledig nieuw is. `Graph search` houdt expliciet bij welke toestanden al gezien of geëxpandeerd zijn, zodat herhaling en lussen beperkt worden.

## Vergelijking

| Aspect | Tree Search | Graph Search |
| --- | --- | --- |
| Basishouding | elk pad apart behandelen | toestanden herkennen als herhalingen |
| Explored set | meestal niet | wel |
| Kans op herhaling | hoog | lager |
| Lussen vermijden | moeilijker | beter beheersbaar |
| Geheugen | soms lager | vaak hoger |
| Correctheid in grafen | kwetsbaarder | robuuster |
| Typische fout | dezelfde toestand blijven herbezoeken | verkeerd omgaan met betere paden naar bestaande nodes |

## Wanneer gebruik je wat?
- **Tree Search:** als je het conceptueel eenvoudig wil houden of als het probleem zich echt als boom gedraagt.
- **Graph Search:** als toestanden via meerdere routes bereikbaar zijn en je dubbele expansie of lussen wil vermijden.

## Waarom is dit onderscheid belangrijk?
Veel problemen lijken op het eerste gezicht een boom, maar gedragen zich in werkelijkheid als een graaf met herhaalde toestanden. Het onderscheid verklaart waarom een [[Explored Set]] in veel zoekproblemen essentieel wordt.

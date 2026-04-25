---
type: lesnotitie
vak: Introduction to Linux
vakafkorting: Linux
les: "6"
thema: Filters, Pipelines & Scripting
datum: 2026-03-27
docent: Steven Moerman
tijdstip: Vrijdag 11:00-13:00
status: actief
parent: "[[10_Modules/S2 - Introduction to Linux/00_Overview|Introduction to Linux]]"
related: []
---

# Introduction to Linux  - Les 6
#linux #lesnotitie

## Lescontext
- **Thema**: Filters, Pipelines & Scripting
- **Docent:** Steven Moerman
- **Tijdstip:** Vrijdag 11:00-13:00
- **Presentaties:** 
- **Bronnen:** 
  - [[10_Modules/S2 - Introduction to Linux/Bronnen/IntroToLinux-Repo/07-Filters-Pipelines|Hoofdstuk 7: Filters & Pipelines]]
  - [[10_Modules/S2 - Introduction to Linux/Bronnen/IntroToLinux-Repo/08-Scripting|Hoofdstuk 8: Scripting]]
## Kernbegrippen
- **Filters & Pipelines**:
  - `grep`, `cut`, `tr`, `wc`, `sort`, `uniq`, `comm`, `sed`
- **Shell Scripting**:
  - `Shebang` (`#!/bin/bash`), Comments (`#`)
  - **Variables**: Toewijzing, gebruik, export
  - **User Input**: `read`, command-line arguments (`$1`, `$2`, `"$@"`)
  - **Conditional Statements**: `if`, `then`, `else`, `elif`, `fi`
  - **Loops**: `for`, `while`, `until`
  - **Case Statements**: `case`, `in`, `esac`

## Lesnotities

### 4.1 Hoofdstuk 7: Filters & Pipelines
- **Key Takeaways**:
  - Filters zijn de bouwstenen van tekstverwerking.
  - Pipes (`|`) maken complexe datatransformaties mogelijk door eenvoudige tools te combineren.
  - `grep` is essentieel voor patroonherkenning en zoeken.
  - Reguliere expressies vergroten de kracht van teksttools.
  - Oefen in het stap-voor-stap bouwen van pipelines.
  - Kies de juiste tool voor de taak.

### 4.2 Hoofdstuk 8: Scripting
- **Key Takeaways**:
  - Shell scripts automatiseren repetitieve taken en zorgen voor consistentie.
  - Goede scriptstructuur bevat: shebang, commentaar en error handling.
  - Variabelen en gebruikersinvoer maken scripts flexibel en interactief.
  - Condities (`if/else`) maken besluitvorming in scripts mogelijk.
  - Loops (`for`, `while`) maken efficiënte verwerking mogelijk.
  - Best practices: documentatie, foutcontrole en betekenisvolle namen.

### 4.3 Conceptvoorstellen (te creëren in 20_Wiki/)
- [[Shell Pipeline]] (Basisconcept voor datastroombeheer)
- [[Shell Scripting Basics]] (Structuur, Shebang, Uitvoerbaarheid)
- [[Shell Variables]] (Toewijzing, Export, Gebruik)
- [[Shell Control Flow]] (if, for, while, case)
- [[Regex in Linux]] (Patroonherkenning voor grep/sed)

## Exameninfo
-  `comm` zal zeker gevraagd worden op examen.
- Op examen moet **zeker** een script moeten gemaakt worden.
## Oefeningen
- [[12-practical-labs]]
- [[10-practical-labs]]

## Opdrachten
- Toledo - Labo 7
- Toledo - Labo 8

---

## Verwerking na de les
- [ ] Lesnotities opschonen en structureren
- [ ] Kernbegrippen linken aan bestaande conceptnotes
- [ ] Nieuwe conceptnotes aanmaken waar nodig
- [ ] Relevante info routeren naar module- of conceptniveau
- [ ] Oefeningen en opdrachten finaliseren met status
- [ ] Oefeningen: [[lesson-07-lab-solutions|Lab Oplossingen]]

## Links
- **Module:** [[10_Modules/S2 - Introduction to Linux/00_Overview|Introduction to Linux]]
- **Leslog:**
- **Samenvatting:**
- **Oefeningen:** [[lesson-07-lab-solutions|Lab Oplossingen]]
- **Concepten:**

h# _Dashboard_

#hub

> [!example] Start les
> - Commando: `/class @10_Modules/<module>/ "les x - thema"`
> - Les log opslaan op het einde: `/class log`
> - Actieve lesmap (nu): [[10_Modules/S2 - Machine Learning Fundamentals/Lessen/ML - Les 6 - Linear Classification en Support Vector Machines]]

---

## OpenCode

### Snelle Commando's
- Start lescontext: `/class @10_Modules/<module>/ "les x - thema"`
- Leslog opslaan: `/class log`

### Live Les Workflow
- Tijdens de les: enkel snelle capture en gerichte edits op jouw instructie.
- Na de les: opschonen, concepten valideren, links en metadata afwerken.
- Lesnaam-conventie:
  - Folder: `[vakafkorting] - Les [#] - [thema]`
  - Lesnotitie: `[vakafkorting]-Les[#]-[thema].md`

### Quality Check (na de les)
- [ ] Kernbegrippen gelinkt aan bestaande conceptnotes
- [ ] Nieuwe conceptnotes aangemaakt waar nodig
- [ ] Oefeningen en opdrachten bijgewerkt met status
- [ ] `/class log` opgeslagen in de actieve lesfolder

---

## Actieve Modules

### S2 Dagonderwijs
- [[10_Modules/S2 - Introduction to Linux/00_Overview|Introduction to Linux]]
- [[10_Modules/S2 - Machine Learning Fundamentals/00_Module_Overzicht|Machine Learning Fundamentals]]
- [[10_Modules/S2 - IoT1/00_Module_Overzicht|IoT1]]
- [[10_Modules/S2 - Design Patterns (Legacy)/00_Module_Overzicht|Design Patterns]]

### Afstandsonderwijs en Examens
- [[10_Modules/S1 - Introduction to AI - AO/00_Module_Overzicht|Introduction to AI - AO]]
- [[10_Modules/S1 - Data Analysis - AO/00_Module_Overzicht|Data Analysis - AO]]

---

## Centrale Bases

### Kernbases
- [[Base - Alle conceptnotes.base]]
- [[Base - Studiebasis AI en ML.base]]
- [[Base - Metadata Check.base]]
- [[Base - Python Codevoorbeelden.base]]
- [[Base - AI Examen Cockpit.base]]

### Alle beschikbare Bases
| Base | Locatie |
| --- | --- |
| [[Base - Alle conceptnotes.base]] | `20_Wiki/` |
| [[Base - Studiebasis AI en ML.base]] | `20_Wiki/` |
| [[Base - Metadata Check.base]] | `20_Wiki/` |
| [[Base - Python Codevoorbeelden.base]] | `20_Wiki/` |
| [[Base - AI Examen Cockpit.base]] | `10_Modules/S1 - Introduction to AI - AO/03_Examenvoorbereiding/` |

---

## Taken en Deadlines

### Dringend
```tasks
not done
(due today) OR (due before today)
sort by priority
sort by due
```

### Komende 7 dagen
```tasks
not done
due after today
due before in 7 days
sort by due
```

---

## Snelle Navigatie

- [[00_Inbox/Mobile-Capture|Nieuwe capture]]
- [[00_Overzicht Concepten|Concepten overzicht]]
- [[99_Meta/00_META_Index|Meta index]]

### Recent gewijzigd
```dataview
TABLE file.link as "Notitie", file.mtime as "Gewijzigd"
FROM "10_Modules"
SORT file.mtime DESC
LIMIT 8
```

---

## Retrieval Prompts
```dataview
LIST
FROM "10_Modules"
WHERE contains(file.name, "Retrieval") OR contains(file.name, "Herhaal")
SORT file.mtime DESC
LIMIT 7
```

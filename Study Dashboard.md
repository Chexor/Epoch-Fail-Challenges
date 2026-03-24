# 🚀 Studie Cockpit
#hub

> [!abstract] Focus van de Dag
> - [ ] **Hoofddoel:** 
> - [ ] **Quick Win:** (max 15 min)
> - [ ] **Retrieval:** 1 actieve oefening voor een S2 vak.

---

## 📚 Actieve Modules

### ⚡ Dagonderwijs (S2)
- [[10_Modules/S2 - Introduction to Linux/00_Module_Overzicht|🐧 Introduction to Linux]]
- [[10_Modules/S2 - Machine Learning Fundamentals/00_Module_Overzicht|🤖 Machine Learning Fundamentals]]
- [[10_Modules/S2 - IoT1/00_Module_Overzicht|🔌 IoT1]]
- [[10_Modules/Design Patterns/00_Module_Overzicht|🏗️ Design Patterns]]

### ⏳ Afstandsonderwijs & Examens
- [[10_Modules/S1 - Introduction to AI - AO/00_Module_Overzicht|🧠 Intro to AI]] (Examen: 27/03)
- [[10_Modules/S1 - Data Analysis - AO/00_Module_Overzicht|📊 Data Analysis]] (Wacht op resultaat)

---

## 📅 Agenda & Deadlines

### 🔥 Dringend (Vandaag of overtijd)
```tasks
not done
(due today) OR (due before today)
sort by priority
sort by due
```

### 🗓️ Komende Week
```tasks
not done
due after today
due before in 7 days
sort by due
```

---

## 🛠️ Snelkoppelingen & Onderhoud

| Actie | Link |
| --- | --- |
| 📥 **Nieuwe Capture** | [[00_Inbox/Mobile-Capture]] |
| 🧠 **Concepten Map** | [[20_Concepts/Maps/Concept_Index|Concept Index]] |
| ⚙️ **Vault Instellingen** | [[99_Meta/00_META_Index|Meta Index]] |
| 📝 **Recente Nota's** | `dataview TABLE file.mtime AS "Gewijzigd" FROM "10_Modules" SORT file.mtime DESC LIMIT 5` |

---

## 💡 Retrieval Drill
*Kies een willekeurige vraag uit je actieve modules:*
```dataview
LIST
FROM "10_Modules"
WHERE contains(file.name, "Retrieval") OR contains(file.name, "Herhaal")
SORT file.mtime DESC
LIMIT 5
```

---
type: module-overzicht
vak: "{{VAKNAAM}}"
docent: ""
status: "actief"
semester:
ects:
---

# {{VAKNAAM}}

- **Docent:**
- **Handboek:**
- **Semester:**
- **Examenfocus:**

> Gebruik deze template voor vakken met lesstructuur, typisch `S2 - ...`.
> Niet bedoeld voor AO-vakken.

---

## Structuur

- `01_Lessen/`
- Elke les krijgt een eigen lesmap binnen `01_Lessen/` met daarin altijd een lesnotitie als ankerbestand.
- `02_Samenvattingen/`
- `03_Oefeningen/`
- `04_Bronnen/`

Voorbeeld:

```text
01_Lessen/
  Les 1/
    Lesnotitie.md
```

Gebruik hiervoor `99_Meta/05_Templates/Lesnotitie Template.md`.

---

## Examenvereisten

- [ ] _Vul hier de concrete examenvereisten in_

---

## Taken

```tasks
not done
path includes "10_Modules/{{MODULEMAP}}"
sort by priority
sort by due
```

---

## Te kennen onderwerpen

- [ ] _Maak hier een checklist van de te kennen leerstof_

---

## Lessen

```dataview
LIST
FROM "10_Modules/{{MODULEMAP}}/01_Lessen"
SORT file.name ASC
```

---

## Samenvattingen

```dataview
LIST
FROM "10_Modules/{{MODULEMAP}}/02_Samenvattingen"
SORT file.name ASC
```

---

## Oefeningen

```dataview
LIST
FROM "10_Modules/{{MODULEMAP}}/03_Oefeningen"
SORT file.name ASC
```

---

## Bronnen & Documenten

```dataview
TABLE WITHOUT ID
file.link as "Bestand",
file.size as "Grootte"
FROM "10_Modules/{{MODULEMAP}}/04_Bronnen"
WHERE file.type = "file"
```

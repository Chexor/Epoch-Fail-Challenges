---
type: lesnotitie
vak: Introduction to Linux
vakafkorting: Linux
les: "3"
thema: Commando's en Help
datum:
docent: Steven Moerman
tijdstip: Vrijdag 11:00-13:00
status: afgerond
parent: "[[10_Modules/S2 - Introduction to Linux/00_Overview|Introduction to Linux]]"
related: []
---

# Linux-Les3-Commando's en Help
#linux #lesnotitie

> Naamgeving:
> - Lesfolder: `Linux - Les 3`
> - Lesnotitie: `Linux_Les3_Note.md`

## Lescontext
- **Thema**: Commando's, Help, Navigatie
- **Docent:** Steven Moerman
- **Tijdstip:** Vrijdag 11:00-13:00
- **Presentaties:**
- **Bronnen:** 
  - [[10_Modules/S2 - Introduction to Linux/Bronnen/IntroToLinux-Repo/02-Shell/|02-Shell]]

## Commando's in deze notitie

- `apropos`
- `man`
- `touch`
- `mkdir`
- `ls`
- `pwd`
- `mv`
- `cp`
- `head`
- `tail`
- `!!`

## Relevante topics in hoofdcursus

- **02-Shell**
  - [[09-getting-help-with-commands|Getting help with commands]] (`man`, `apropos`)
  - [[09-essential-navigation-commands|Essential navigation commands]] (`pwd`, absolute/relatieve paths)
  - [[10-essential-file-commands|Essential file commands]] (`ls`, `mkdir`, `touch`, `cp`, `mv`)
  - [[11-file-system-navigation-quiz|File system navigation quiz]] (examenvragen paths)

- **03-History-Variables**
  - [[01-review-shell-basics-lesson-12-recap|Review shell basics]]
  - [[02-environment-variables|Environment variables]] (`$PWD` context)
  - [[05-working-with-the-path-variable|Working with the PATH variable]]

## Kern

`apropos` = zoekmachine voor commando's.
`man` = handleiding van een commando.

## `apropos`

Zoekt in korte beschrijvingen van manpages op trefwoord.

```bash
apropos password
apropos network
```

## `man`

Toont de volledige manpage van een commando.

```bash
man ls
man 5 passwd   # manpage van het bestand /etc/passwd
man 1 passwd   # manpage van het passwd-commando
```

## Navigatie in `man`

- `/tekst` om te zoeken in de pagina
- `n` voor volgende match
- `q` om af te sluiten

## Workflow

```bash
apropos route
man route
```

## `touch`

Maakt een leeg bestand aan, of past de timestamp van een bestaand bestand aan.

```bash
touch note.txt
touch bestand1.txt bestand2.txt
```

## `mkdir`

Maakt een nieuwe map aan.

```bash
mkdir oefeningen
mkdir -p les3/opdracht1   # maakt ook tussenmappen aan
```

## `ls`

Toont de inhoud van een map.

```bash
ls
ls -l      # detailweergave
ls -a      # ook verborgen bestanden
```

## `pwd`

Toont in welke map je momenteel zit.

```bash
pwd
```

## `mv`

Verplaatst of hernoemt bestanden/mappen.

```bash
mv oud.txt nieuw.txt
mv bestand.txt map/
```

## `cp`

Kopieert bestanden of mappen.

```bash
cp bron.txt kopie.txt
cp bestand.txt map/
cp -r map1 map2   # map recursief kopieren
```

## `head`

Toont het begin van een bestand (standaard eerste 10 lijnen).

```bash
head bestand.txt
head -n 20 bestand.txt
```

## `tail`

Toont het einde van een bestand (standaard laatste 10 lijnen).

```bash
tail bestand.txt
tail -n 20 bestand.txt
tail -f logfile.txt   # live nieuwe lijnen volgen
```

## `!!`

Voert je **vorige commando** opnieuw uit.

```bash
ls -l
!!          # voert opnieuw 'ls -l' uit
```

Handig met `sudo`:

```bash
apt update
sudo !!     # wordt: sudo apt update
```

## Basic scripting (bash)

Een script is een reeks commando's in een `.sh`-bestand.

### 1) Maak een script

```bash
nano hello.sh
```

Inhoud:

```bash
#!/bin/bash
echo "Hallo"
```

### 2) Maak uitvoerbaar en run

```bash
chmod +x hello.sh
./hello.sh
```

### 3) Variabele en input (basis)

```bash
#!/bin/bash
naam="Tim"
echo "Hallo $naam"
read -p "Geef je stad: " stad
echo "Je woont in $stad"
```

## Mogelijke examenvragen: absolute en relatieve paths

- **Absolute path:** volledig pad vanaf `/`.
- **Relatieve path:** pad vanaf je huidige map.
- **Herkennen:** absolute paths starten met `/`, relatieve niet.

### Oefenvragen (zoals in de quiz)

1. Current: `/home/alice` -> Target: `/home/alice/documents/reports/2024`
   - Absolute: `cd __________________________`
   - Relatief: `cd __________________________`

2. Current: `/etc/config/network` -> Target: `/etc/config/apache`
   - Absolute: `cd __________________________`
   - Relatief: `cd __________________________`

3. Current: `/home/alice/documents/projects/scripts` -> Target: `/home/alice`
   - Absolute: `cd __________________________`
   - Relatief: `cd __________________________`

4. Current: `/home/alice/downloads/music/rock` -> Target: `/`
   - Absolute: `cd __________________________`
   - Relatief: `cd __________________________`

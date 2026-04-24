---
type: concept
domain: Linux
---
# 02 - De Shell en het Linux Bestandssysteem

Een overzicht van de command-line interface, de bestandsstructuur van Linux, permissies en de essentiële commando's voor bestandsbeheer en navigatie.

## Console, Terminal en Shell
- **TTY (TeleTYpe Writer):** De historische oorsprong van de command-line. Vroege terminals waren letterlijk typemachines verbonden aan computers.
- **Terminal (Emulator):** De software (interface) waarmee we interactie hebben (bv. GNOME Terminal, iTerm2, Windows Terminal).
- **Console:** Een speciaal type terminal zonder grafische omgeving, voor directe interactie op het systeem.
- **Shell:** Het programma (de interpreter) dat de commando's in de terminal leest en doorgeeft aan de kernel. Bekende shells zijn `bash` (de standaard op de meeste Linux-systemen), `zsh`, `sh` en `dash`.

## Gebruikerstypes en Login
- **Regular User (Ongeprivilegieerd):** Beperkte toegang. Kan alleen bestanden in de eigen home directory (`~`) aanpassen. De prompt eindigt doorgaans op een `$`.
- **Root Administrator (Geprivilegieerd):** Volledige systeemtoegang. De prompt eindigt op een `#`.
- **Switchen van gebruiker:**
  - `su -`: Schakel over naar de root-gebruiker (vereist het root-wachtwoord).
  - `sudo su` of `sudo -i`: Schakel over naar root met behulp van je eigen wachtwoord.
  - `sudo <commando>`: Voer één specifiek commando uit als administrator.
  - Check wie is ingelogd met commando's als `who`, `whoami` of `w`.

## Het Linux Bestandssysteem
In tegenstelling tot Windows (die stationsletters zoals `C:\` of `D:\` gebruikt), vertrekt Linux vanuit één enkele boomstructuur.

**Belangrijke directories:**
- `/` - De **Root** directory, waar de boomstructuur begint.
- `/bin` & `/sbin` - Essentiële commands en systeemprogramma's (binaries).
- `/etc` - Systeemconfiguratiebestanden.
- `/home` - Persoonlijke bestanden per gebruiker (bv. `/home/alice`). 
- `/root` - De home directory van de root-gebruiker.
- `/var` - Variabele data zoals logbestanden.
- `/tmp` - Tijdelijke bestanden (vaak geleegd bij een reboot).
- `/dev` - Hardware devices aangesloten op de pc.

**Paden (Paths):**
- **Absolute paden:** Beginnen altijd bij de root (`/`), bv. `/home/alice/document.txt`.
- **Relatieve paden:** Beginnen vanaf de huidige locatie, zonder de `/` vooraan, bv. `documents/report.txt`.

## Home Directory Concepten
Elke gewone gebruiker krijgt een eigen map in `/home`. Deze locatie heeft de snelle aanduiding `~` of de environment variabele `$HOME`. Het commando `cd` (zonder argumenten) brengt je altijd direct terug naar deze home directory.

## File System Permissies
Linux hanteert een sterke focus op security en user-isolation. Rechten worden toegewezen in drie groepen: aan de **Owner**, de **Group** en **Others**. 

Elke bestandsrechten-set is opgebouwd uit `rwx`:
- **Read (r):** Bestanden lezen / Directory inhoud oplijsten.
- **Write (w):** Bestanden bewerken en verwijderen / Bestanden in een directory aanmaken of verwijderen.
- **Execute (x):** Bestanden uitvoeren (scripts) / Een directory binnengaan (`cd`).

## Essentiële Commando's

**Navigatie:**
- `pwd`: (Print Working Directory) Toon de huidige map.
- `cd <pad>`: Verander van map (`cd ..` gaat één niveau omhoog, `cd -` gaat naar de vorige map).
- `ls`: Lijst bestanden en mappen op (`ls -l` voor details en rechten, `ls -la` voor alles inclusief verborgen bestanden, `ls -lh` voor menselijk leesbare bestandsgroottes).

**Bestandsbeheer:**
- `touch <bestand>`: Maak een leeg bestand aan.
- `mkdir <map>`: Maak een nieuwe map aan (`mkdir -p` voor geneste mappen).
- `cp <bron> <doel>`: Kopieer een bestand (`cp -r` voor volledige mappen).
- `mv <bron> <doel>`: Verplaats of hernoem een bestand of map.
- `rm <bestand>`: Verwijder een bestand (`rm -r` voor mappen, `rm -rf` voor geforceerd verwijderen zonder waarschuwing - gebruik met voorzichtigheid!).

**Inhoud bekijken en bewerken:**
- `cat`: Toon volledige bestandsinhoud in de terminal.
- `less` / `more`: Bekijk grotere bestanden pagina per pagina.
- `head` / `tail`: Toon de eerste (`head`) of laatste (`tail`) 10 regels van een bestand.
- `nano`: Simpele, toegankelijke command-line tekstverwerker.
- `wget <url>`: Download een bestand via het internet.

## Hulp Vragen
- `man <commando>`: Open de volledige manual page (bv. `man ls`). Gebruik `/` om hierin te zoeken en `q` om af te sluiten.
- `<commando> --help`: Korte samenvatting van het gebruik en de opties van een commando.
- `apropos <keyword>` of `man -k <keyword>`: Zoek commando's op basis van een beschrijving.
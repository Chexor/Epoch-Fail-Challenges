---
type: lesnotitie
vak: Introduction to Linux
vakafkorting: Linux
les: "7"
thema: Users & Groups
datum:
docent: Steven Moerman
tijdstip: Vrijdag 11:00-13:00
status: actief
parent: "[[10_Modules/S2 - Introduction to Linux/00_Overview|Introduction to Linux]]"
related: []
---

# Introduction to Linux - Les 7
#linux #lesnotitie

> Naamgeving:
> - Lesfolder: `Linux - Les 7`
> - Lesnotitie: `Linux_Les7_Note.md`

## Lescontext
- **Thema**: Users & Groups
- **Docent:** Steven Moerman
- **Tijdstip:** Vrijdag 11:00-13:00
- **Presentaties:**
- **Bronnen:**
  - [[10_Modules/S2 - Introduction to Linux/Bronnen/IntroToLinux-Repo/09-Users-Groups/|09-Users-Groups]]

## Kernbegrippen
- **Multi-user system**: Linux is gebouwd voor meerdere gebruikers met elk een eigen identiteit, rechten en werkomgeving.
- **Users**: onderscheid tussen `root`, system users en regular users op basis van hun rol en UID-bereik.
- **UID en GID**: numerieke identifiers voor gebruikers en groepen waarop permissies steunen.
- **Primary en secondary groups**: een gebruiker heeft een hoofdgroep en kan extra groepen hebben voor gedeelde toegang.
- **Accountbestanden**: `/etc/passwd`, `/etc/shadow` en `/etc/group` bevatten de basisinformatie over accounts en groepen.
- **sudo**: gecontroleerde privilege escalation zonder het root-wachtwoord te delen.
- **Security en auditing**: correct beheer van accounts, groepen en permissies is essentieel voor veiligheid.

## Lesnotities

### 4.1 Losse notities (ruwe capture)
- Eerste deel van de les behandelt [[10_Modules/S2 - Introduction to Linux/Bronnen/IntroToLinux-Repo/09-Users-Groups/|09-Users-Groups]].
- Hoofdstuk focust op hoe Linux gebruikers en groepen structureert in een multi-user systeem.
- Notatie tijdens de les:
  - `Patatje` => user `Patatje`
  - `%Patatjes` => group `Patatjes`
- Sudo list NOOIT met gewone editor aanpassen; gebruik `visudo`.

### 4.2 Concepts (te valideren)
-

## Exameninfo
- Examenvraag: toon alle users die een Bash shell mogen gebruiken.
- Praktisch spoor: filter in `/etc/passwd` op accounts met shell `/bin/bash`.
- Grote kans op examenvraag rond rechten aanpassen met octale cijfers.
- Rechten aanpassen kan op 2 manieren:
  - **Octaal**: elk cijfer stelt de rechten voor van `user`, `group` en `others`.
    - Voorbeeld: `chmod 647 file.txt`
  - **Symbolisch**: je wijzigt rechten met letters zoals `u`, `g`, `o`, `r`, `w`, `x`.
    - Voorbeeld: `chmod u=rw,g=r,o=x file.txt`

## Oefeningen (tijdens de les)
- [ ]

## Opdrachten (om thuis af te werken)
- [ ]

---

## Verwerking na de les
- [ ] Lesnotities opschonen en structureren
- [ ] Kernbegrippen linken aan bestaande conceptnotes
- [ ] Nieuwe conceptnotes aanmaken waar nodig
- [ ] Relevante info routeren naar module- of conceptniveau
- [ ] Oefeningen en opdrachten finaliseren met status

## Links
- **Module:** [[10_Modules/S2 - Introduction to Linux/00_Overview|Introduction to Linux]]
- **Leslog:**
- **Samenvatting:**
- **Oefeningen:**
- **Concepten:**

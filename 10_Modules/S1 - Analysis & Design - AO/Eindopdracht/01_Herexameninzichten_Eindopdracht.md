---
type: examennotitie
vak: Analysis & Design
thema: herexameninzichten eindopdracht
status: actief
parent: "[[10_Modules/S1 - Analysis & Design - AO/00_Module_Overzicht|Module Overzicht]]"
related:
  - "[[10_Modules/S1 - Analysis & Design - AO/Eindopdracht/EO_Fleetbooker_v1.pdf]]"
  - "[[10_Modules/S1 - Analysis & Design - AO/Eindopdracht/Feedback_eindopdracht.md]]"
---

# Herexameninzichten uit eindopdracht

## Kernpunt
- **Score**: `11/20`
- De docent vindt je **casus**, **usecasediagram**, **usecasebeschrijvingen**, **klassenselectie** en delen van de **vereistenanalyse** behoorlijk goed.
- Het grootste probleem zit in het **eventmodel**: dat is volgens de feedback **niet bruikbaar in de huidige vorm**.

## Wat al goed zat
- goede en duidelijke casus
- usecasediagram is goed
- usecasebeschrijvingen zijn goed ingedeeld
- er is aandacht voor uitzonderingen
- het systeemgedrag wordt meestal correct beschreven
- niet-functionele eisen zijn inhoudelijk zinvol
- domeinmodel bevat de nodige domeinconcepten
- klassen- en attribuutbeschrijvingen zijn goed
- lijst met events is in basis goed
- eventspecificaties zijn goed ingedeeld
- eventspecificaties houden rekening met bestaansafhankelijkheid
- toestandsdiagrammen zijn inhoudelijk correct

## Belangrijkste fouten volgens de feedback

### 1. Usecases waren niet scherp genoeg afgebakend
- `Melding afsluiten` is geen zinvolle usecase.
- `UC10 Overzicht raadplegen` was te breed en moest opgesplitst worden volgens doel.
- De usecaselijst was smaller dan de casus zelf: `voertuigtypes` en `onderhoudsparameters` ontbraken.
- `UC5 Schade/Defect melden` lijkt eerder onderdeel van `UC4 Rit afsluiten`.
- Er ontbreekt een usecase voor **aanmelden**.

### 2. Sommige usecases zijn nog te vaag gespecificeerd
- Formuleringen zoals `de opgegeven periode is ongeldig` moeten concreet gemaakt worden.
- Je moet expliciet bepalen **wanneer** iets ongeldig is.
- Het systeem mag de gebruiker soms meer werk uit handen nemen.
- Voorbeeld uit feedback: bij schade melden moet de gebruiker niet opnieuw het voertuig kiezen als het systeem dat al weet via de actieve rit.

### 3. Niet-functionele vereisten zijn te weinig meetbaar
- Inhoudelijk ok, maar te vaag geformuleerd.
- Voor herwerking moet je meer toetsbare criteria gebruiken.

## Domeinmodel: wat je opnieuw moet bewaken

### 1. UML-correctheid
- **Enumeraties hebben geen associaties.**
- De multipliciteiten bij `Reservering - Rit` stonden omgekeerd.
- `Id`-attributen zet je alleen in een domeinmodel als gebruikers die effectief zien en gebruiken.

### 2. Statusmodellering moet realistischer
- Twee statussen voor `Reservatie` zijn te beperkt.
- De feedback noemt expliciet het probleem van reservaties waarvan de rit al lopende of afgelopen is.
- Dus: statussen moeten de levenscyclus beter weerspiegelen.

### 3. Consistentie tussen modelonderdelen is cruciaal
- De feedback wijst op een inconsistente koppeling van `Melding`.
- Volgens de docent moest je je houden aan je domeinmodel; daar zou `Melding` afhangen van `Rit` en niet van `Voertuig`.
- Voor het herexamen moet je dus extra streng controleren of:
  - klassendiagram
  - klassenbeschrijvingen
  - event specs
  - toestandsdiagrammen
  allemaal exact hetzelfde model volgen.

## Eventanalyse: hier zat het echte probleem

### 1. Eventnamen en eventgrenzen
- Voor statusgedreven klassen werk je beter met **meerdere specifieke wijzigingsevents**.
- `MOD_Reservatie` bleek in jouw uitwerking eigenlijk twee verschillende events te zijn.
- Twee events met dezelfde naam mogen niet.
- Eventnamen moeten overal identiek gebruikt worden in:
  - OET
  - event specs
  - toestandsdiagrammen

### 2. OET was inhoudelijk fout
- De docent zegt expliciet dat de **propagatie in de Object Event Table niet goed** is.
- Een OET moet dus zuiver tonen **welk event welke klasse creëert, wijzigt of beëindigt**.
- Niet zomaar extra gevolglogica of afgeleide acties mengen alsof het nieuwe events zijn.

### 3. Postcondities vs. propagatie door elkaar gehaald
- In `MOD_Rit` horen de wijzigingen aan gelinkte objecten gewoon bij de **postcondities**.
- De tussentitel `Propagatie` is niet nodig en niet gewenst.
- `Conditionele propagatie` zoals jij die gebruikte is fout in deze context.
- Een **event triggert geen ander event**.
- Dus: beschrijf de gevolgen van een event rechtstreeks als postcondities, niet als nieuw event.

### 4. Bestaansafhankelijkheid strikter toepassen
- In `CRE_Melding` ontbrak volgens de feedback het juiste ouderobject.
- In `END_Rit` ontbrak een bijkomende eis rond afhankelijke `Melding`-objecten.
- De les hieruit: bij elk `CRE`, `MOD` en `END` moet je systematisch checken:
  - van welk ouderobject hangt dit object af?
  - welke afhankelijke objecten mogen dan wel of niet bestaan?

### 5. Overbodige of ongewenste postcondities vermijden
- In `CRE_Rit` waren de laatste twee regels van de postcondities niet nodig en niet gewenst.
- Dat wijst erop dat je enkel moet noteren wat echt semantisch nodig is voor dat event.

## Concrete herexamenlessen

### Voor usecases
- kies alleen échte gebruikersdoelen als usecase
- vermijd te brede overzicht-usecases
- zorg dat alle functionaliteit uit de casus afgedekt is
- voeg expliciet `aanmelden` toe als dat functioneel nodig is
- maak uitzonderingen toetsbaar en concreet

### Voor het domeinmodel
- hou associaties, multipliciteiten en bestaansafhankelijkheid 100% consistent
- gebruik geen associaties naar enumeraties
- voeg geen `id`-velden toe zonder goede reden
- modelleer voldoende rijke statussen waar de levenscyclus dat vereist

### Voor eventanalyse
- gebruik aparte, duidelijk benoemde events per betekenisvolle statuswijziging
- gebruik exact dezelfde eventnamen in alle diagrammen en specificaties
- laat events geen andere events triggeren
- schrijf gevolgwijzigingen als postcondities
- controleer bij elk event de bestaansafhankelijkheid en eindvoorwaarden

## Waarschijnlijk examengericht zwakke zone
- Als de docent zegt dat je eventmodel **niet bruikbaar** is, dan is **eventanalyse / OET / eventspecificaties** je grootste remediëringspunt.
- Daar moet je dus prioritair op oefenen voor het herexamen.

## Praktische aanpak voor een volgende versie
1. Eerst casus en scope scherp zetten.
2. Dan volledige, niet-overlappende usecaselijst maken.
3. Dan domeinmodel opbouwen en intern controleren op consistentie.
4. Pas daarna OET en event specs maken.
5. Op het einde systematisch checken of klassendiagram, events en toestandsdiagrammen elkaar nergens tegenspreken.

## Bronnen
- [[EO_Fleetbooker_v1.pdf|Ingeleverde eindopdracht]]
- [[Feedback_eindopdracht.md|Feedback van de docent]]

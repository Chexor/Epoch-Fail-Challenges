# Linux-Les 4 - Redirects en Pipes

#linux

## Commando's en operatoren in deze notitie

- `>`
- `>>`
- `2>`
- `2>>`
- `2>&1`
- `&>`
- `<`
- `<<`
- `<<<`
- `|`
- `tee`
- `head`
- `tail`
- `cat`
- `tac`
- `less`
- `more`
- `strings`

## Relevante topics in hoofdcursus

- [[01-understanding-standard-streams|Understanding Standard Streams]]
- [[02-output-redirection|Output Redirection]]
- [[03-input-redirection|Input Redirection]]
- [[04-pipes-chaining-commands|Pipes: Chaining Commands]]
- [[05-text-processing-commands|Text Processing Commands]]
- [[06-combining-redirection-and-pipes|Combining Redirection and Pipes]]
- [[10-troubleshooting|Troubleshooting]]
- [[10_Modules/S2 - Introduction to Linux/Bronnen/IntroToLinux-Repo/04-Redirects-Pipes/11-review-questions|Review Questions]]

## Grote plaatje

Deze les gaat over hoe data tussen het toetsenbord, bestanden, de terminal en andere commando's stroomt.

- **Vorige les:** history, variabelen en shell-omgeving
- **Deze les:** input en output sturen
- **Later nuttig voor:** scripting, logging, debugging, procesbeheer en serverbeheer

Het kernidee: in Linux hoeft output niet op het scherm te blijven. Je kan die opslaan, weggooien, filteren of doorgeven aan een ander commando.

## Wat is het kernprobleem?

Hoe laat je een commando werken met de juiste input en hoe stuur je de output naar de juiste plaats?

Zonder redirection en pipes ben je beperkt tot:

- input via toetsenbord
- output op het scherm
- weinig hergebruik tussen commando's

Met redirection en pipes kan je:

- resultaten bewaren in bestanden
- foutmeldingen apart houden
- commando's combineren tot workflows
- sneller analyseren en debuggen

## De 3 standaard streams

Elk Linux-proces heeft standaard 3 datastromen:

- `stdin` = standard input = file descriptor `0`
- `stdout` = standard output = file descriptor `1`
- `stderr` = standard error = file descriptor `2`

Standaard gedrag:

- `stdin` komt van het toetsenbord
- `stdout` gaat naar het scherm
- `stderr` gaat ook naar het scherm

```bash
echo "Hallo"
ls /bestaat-niet
cat
```

- `echo` schrijft naar `stdout`
- `ls /bestaat-niet` schrijft de fout naar `stderr`
- `cat` leest van `stdin`

## Output redirection

### Kern

Met output redirection stuur je uitvoer van een commando naar een bestand in plaats van naar het scherm.

### Belangrijkste operatoren

- `>` overschrijft bestand met `stdout`
- `>>` voegt toe aan bestand met `stdout`
- `2>` overschrijft bestand met `stderr`
- `2>>` voegt toe aan bestand met `stderr`
- `&>` stuurt `stdout` en `stderr` samen naar hetzelfde bestand
- `2>&1` maakt dat `stderr` dezelfde bestemming krijgt als `stdout`

```bash
ls > listing.txt
date >> log.txt
ls /bestaat-niet 2> errors.txt
find / -name "*.txt" > found.txt 2> errors.txt
command > output.txt 2>&1
command &> alles.txt
```

### Belangrijk verschil: `>` vs `>>`

- `>` maakt leeg of overschrijft
- `>>` bewaart bestaande inhoud en plakt onderaan bij

## Input redirection

### Kern

Met input redirection geef je een bestand of tekst aan een commando alsof die van het toetsenbord komt.

### Belangrijkste operatoren

- `<` leest input uit een bestand
- `<<` here document voor meerdere lijnen
- `<<<` here string voor 1 korte string

```bash
sort < namen.txt
wc -w < tekst.txt
cat << EOF > gedicht.txt
Rood is rood
Blauw is blauw
Linux is handig
En jij ook trouwens
EOF
grep "linux" <<< "ik leer linux vandaag"
```

### Wanneer handig?

- testdata snel doorgeven
- configuratie- of tekstblokken maken
- scripts voeden zonder interactief typen

## Pipes

### Kern

Een pipe (`|`) verbindt `stdout` van commando 1 met `stdin` van commando 2.

Dus: output van het ene commando wordt direct input van het volgende.

```bash
ls | wc -l
ps aux | grep firefox
history | tail -10
cat /etc/passwd | head -5
```

### Intuitie

Zie een pipe als een lopende band:

- commando 1 produceert data
- commando 2 filtert of verwerkt die data
- commando 3 toont of bewaart het resultaat

```bash
ls -la | grep "txt" | wc -l
```

Dit betekent:

1. toon alle bestanden
2. hou enkel regels met `txt`
3. tel hoeveel er overblijven

## Pipes vs redirection

- `>` of `<` gebruikt bestanden als tussenstap
- `|` stuurt data rechtstreeks tussen commando's

Gebruik redirection als je iets wil bewaren.
Gebruik pipes als je iets wil doorgeven aan een volgend commando.

## Tekstverwerking die vaak samen met pipes gebruikt wordt

### `head` en `tail`

```bash
head bestand.txt
head -n 5 bestand.txt
tail bestand.txt
tail -n 20 bestand.txt
tail -f /var/log/syslog
```

- `head` toont het begin
- `tail` toont het einde
- `tail -f` volgt live nieuwe regels, handig voor logs

### `cat` en `tac`

```bash
cat bestand.txt
cat -n bestand.txt
tac bestand.txt
```

- `cat` toont inhoud
- `cat -n` toont lijnnummers
- `tac` toont lijnen in omgekeerde volgorde

### `more` en `less`

```bash
less bestand.txt
ps aux | less
man ls | less
```

- `less` is meestal beter dan `more`
- handig bij lange output
- in `less`: `/` zoeken, `q` afsluiten

### `strings`

```bash
file onbekend_bestand
strings onbekend_bestand | head -10
```

Handig om leesbare tekst uit een binair of onbekend bestand te halen.

## Combineren van pipes en redirection

Dit is waar het echt krachtig wordt.

```bash
ps aux | sort -k4 -nr | head -10 > top_memory.txt
ls /bestaat-niet 2>&1 | grep "No such file"
command | tee output.txt
```

### `tee`

`tee` is belangrijk omdat het output tegelijk:

- op het scherm toont
- en in een bestand opslaat

```bash
ps aux | tee processen.txt | grep firefox
```

Dat is ook het antwoord op een typische vraag: _hoe bewaar je output en toon je die tegelijk?_ -> met `tee`.

## Praktische denkwijze bij pipelines

Werk van links naar rechts:

1. waar komt de input vandaan?
2. welk commando produceert de ruwe data?
3. welk commando filtert of sorteert?
4. wil ik het eindresultaat tonen, bewaren of beide?

Voorbeeld:

```bash
du -sh */ | sort -hr | head -5 > grootste_mappen.txt
```

- `du -sh */` meet mapgroottes
- `sort -hr` sorteert van groot naar klein
- `head -5` houdt de top 5 over
- `> grootste_mappen.txt` bewaart het resultaat

## Typische fouten en troubleshooting

### 1. Fout output komt niet mee

Als je enkel `>` gebruikt, stuur je alleen `stdout` door. Foutmeldingen blijven apart.

```bash
command > output.txt
command > output.txt 2>&1
```

### 2. Verkeerd bestand overschrijven

Gebruik `>>` als je wil toevoegen in plaats van vervangen.

### 3. Geen resultaat in een pipeline

Test elk stuk apart:

```bash
command1 > temp1.txt
command2 < temp1.txt > temp2.txt
command3 < temp2.txt
```

### 4. Permission denied bij redirection

Dit faalt vaak:

```bash
echo "test" > /etc/hosts
```

Werk dan via `tee` met `sudo`:

```bash
echo "test" | sudo tee -a /etc/hosts
```

### 5. `/dev/null` vergeten

`/dev/null` is de zwarte put van Linux: alles wat je daarheen stuurt, verdwijnt.

```bash
command > /dev/null
command 2> /dev/null
command &> /dev/null
```

Gebruik dit om ongewenste output of foutmeldingen te onderdrukken.

## Examengerichte vertaling

Wat je zeker moet kennen:

- verschil tussen `stdin`, `stdout`, `stderr`
- verschil tussen `>` en `>>`
- verschil tussen `>` en `|`
- betekenis van `2>` en `2>&1`
- functie van `/dev/null`
- waarom `tee` nuttig is

Typische examenvragen:

1. Wat zijn de drie standaard streams?
2. Hoe redirect je zowel gewone output als errors naar hetzelfde bestand?
3. Wat is het verschil tussen een pipe en output redirection?
4. Wanneer gebruik je `tee`?
5. Wat doet `tac` dat `cat` niet doet?

## Mini-oefeningen

### Oefening 1

Toon het aantal bestanden in de huidige map.

```bash
ls | wc -l
```

### Oefening 2

Bewaar de inhoud van `ls -l` in `files.txt`.

```bash
ls -l > files.txt
```

### Oefening 3

Voeg de huidige datum toe aan `log.txt` zonder bestaande inhoud te wissen.

```bash
date >> log.txt
```

### Oefening 4

Zoek foutmeldingen en stuur ze naar `errors.txt`.

```bash
ls /bestaat-niet 2> errors.txt
```

### Oefening 5

Sorteer een bestand `namen.txt` en bewaar het resultaat in `gesorteerd.txt`.

```bash
sort < namen.txt > gesorteerd.txt
```

## Kernsamenvatting

- Redirection stuurt input of output naar bestanden of andere bestemmingen.
- Pipes verbinden commando's rechtstreeks met elkaar.
- `stdout` en `stderr` zijn niet hetzelfde, ook al zie je ze vaak allebei op het scherm.
- `tee` toont en bewaart tegelijk.
- `/dev/null` gebruik je om output bewust weg te gooien.

## Snelle checklist

- [ ] Ik kan `stdin`, `stdout` en `stderr` uitleggen #linux
- [ ] Ik ken het verschil tussen `>` en `>>` #linux
- [ ] Ik kan uitleggen wat `2>&1` doet #linux
- [ ] Ik kan een eenvoudige pipeline lezen van links naar rechts #linux
- [ ] Ik kan beslissen wanneer ik `|` gebruik en wanneer `>` beter is #linux

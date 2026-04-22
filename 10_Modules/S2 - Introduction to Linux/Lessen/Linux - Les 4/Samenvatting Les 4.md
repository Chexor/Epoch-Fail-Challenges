# Samenvatting Les 4 - Redirects en Pipes

#linux

## Kernidee

Linux werkt met 3 standaard streams:

- `stdin` = input = `0`
- `stdout` = gewone output = `1`
- `stderr` = foutmeldingen = `2`

## Redirection

- `>` schrijf `stdout` naar bestand
- `>>` voeg `stdout` toe aan bestand
- `2>` schrijf `stderr` naar bestand
- `2>&1` stuur `stderr` mee met `stdout`
- `<` lees input uit bestand

```bash
ls > files.txt
date >> log.txt
ls /bestaat-niet 2> errors.txt
wc -l < fruits.txt
```

## Pipes

`|` stuurt output van het ene commando naar input van het volgende.

```bash
ls | wc -l
cat fruits.txt | sort
history | tail -10
```

## Belangrijke commando's

- `head` = eerste lijnen
- `tail` = laatste lijnen
- `cat` = toon inhoud
- `tac` = omgekeerde lijnvolgorde
- `tee` = toon en bewaar tegelijk

## Extra

- `>` bewaart output in een bestand
- `|` verwerkt output verder in een ander commando
- `/dev/null` gooit output weg

## Onthouden voor examen

- verschil tussen `stdin`, `stdout`, `stderr`
- verschil tussen `>` en `>>`
- verschil tussen `>` en `|`
- betekenis van `2>` en `2>&1`
- nut van `tee` en `/dev/null`

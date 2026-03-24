# Plugin Functionaliteitstest

Dit is een testbestand om te verifiëren dat de agent Dataview en Tasks queries correct kan aanmaken.

## Dataview Test

De onderstaande query zou alle notities in de `99_Meta` map moeten oplijsten.

```dataview
LIST
FROM "99_Meta"
```

## Tasks Test

De onderstaande query zou alle onvoltooide taken in de vault moeten tonen.

```tasks
not done
```

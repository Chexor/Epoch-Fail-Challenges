# Samenvatting les 5

Deze les gaat over 4 dingen:
- `structs`
- `pointers`
- `alternate functions`
- `USART/UART`

## 1. Structs

Een `struct` is een manier om meerdere variabelen samen te zetten in 1 geheel.

Voorbeeld:

```c
typedef struct
{
    char firstName[51];
    char lastName[51];
    float weight;
} Person;
```

Dit betekent:
- `firstName`, `lastName` en `weight` horen samen
- je kan die gegevens behandelen als 1 object: een `Person`

Waarom handig?
- je code wordt overzichtelijker
- gegevens die bij elkaar horen, zitten samen
- makkelijk herbruikbaar in andere bestanden via een header file

Voorbeeld van gebruik:

```c
Person bigGuy;
bigGuy.weight = 123.45f;
```

Dus:
- `bigGuy` is een variabele van het type `Person`
- met de punt `.` ga je naar een onderdeel van de struct

## 2. Pointers

Een pointer is een variabele die geen gewone waarde bewaart, maar een adres in het geheugen.

Heel simpel:
- een gewone variabele bevat data
- een pointer bevat de plaats waar die data staat

Voorbeeld:

```c
uint8_t getal = 138;
uint8_t* getalPointer;
getalPointer = &getal;
```

Betekenis:
- `getal` bevat `138`
- `getalPointer` bewaart het adres van `getal`

Belangrijke symbolen:
- `&getal` = "het adres van getal"
- `*getalPointer` = "de waarde op dat adres"

Voorbeeld:

```c
*getalPointer = 139;
```

Dit verandert de waarde van `getal` naar `139`.

Dus:
- `&` vraagt een adres op
- `*` gebruik je om via een pointer aan de echte waarde te raken

Let op:
het sterretje `*` heeft 2 betekenissen:
- bij declareren van een pointer:

```c
uint8_t* p;
```

- bij uitlezen of aanpassen van de waarde:

```c
*p = 10;
```

## Waarom zijn pointers belangrijk?

- veel gebruikt in embedded programming
- efficient bij functies
- je kan rechtstreeks met geheugen en registers werken

## Pointers naar structs

Je kan ook een pointer naar een struct hebben.

Voorbeeld:

```c
void PersoonToUsart(Person* person)
{
    sprintf(text, "%s %s (%.2f kg)", person->firstName, person->lastName, person->weight);
}
```

Hier gebruik je `->` in plaats van `.` omdat `person` een pointer is.

Dus:
- `.` gebruik je bij een gewone struct
- `->` gebruik je bij een pointer naar een struct

Waarom handig?
- je moet niet de hele struct kopieren
- je geeft alleen het adres door
- dat is sneller en zuiniger

## 3. Alternate Functions

Een pin van de microcontroller kan meerdere functies hebben.

Normaal kan een pin bijvoorbeeld zijn:
- digitale ingang
- digitale uitgang
- alternate function
- analoge pin

Een `alternate function` betekent:
- de pin wordt gebruikt door een ingebouwde module van de microcontroller
- bijvoorbeeld `USART`, `SPI`, `I2C`, timers, ...

Voorbeeld:
- pin `PA2` kan gebruikt worden als `USART2_TX`
- dan verstuurt die pin seriele data

Hoe kies je dat?
- zet de pin in alternate function mode via `GPIOx_MODER`
- kies daarna de juiste alternate function in `GPIOx_AFRL` of `GPIOx_AFRH`

Belangrijk:
- welke alternate functions mogelijk zijn, zoek je op in de datasheet van de microcontroller

## 4. USART / UART

USART is een manier om seriele data te versturen en ontvangen.

Eenvoudig gezegd:
- 1 toestel stuurt bits
- het andere toestel ontvangt bits
- dat gebeurt via `TX` en `RX`

Betekenis:
- `TX` = transmit = verzenden
- `RX` = receive = ontvangen

## UART-frame

- startbit
- 8 databits
- soms parity
- stopbit

Ook belangrijk:
- beide toestellen moeten dezelfde `baudrate` gebruiken
- baudrate = snelheid van de communicatie

## Op het Nucleo-bord

- `USART2` is verbonden met de USB via de ST-link
- daardoor krijg je op je pc een virtuele COM-poort
- gebruikte pinnen:
  - `PA2` = TX
  - `PA3` = RX

## USART instellen: stappen

1. klok inschakelen voor de GPIO-poort
2. pinnen op alternate function zetten
3. juiste alternate function kiezen
4. USART instellen:
   - baudrate
   - stopbits
   - zender/ontvanger aanzetten

## Data versturen en ontvangen

Er zijn 3 manieren:
- `polling`
- `interrupts`
- `DMA`

Heel simpel verschil:

- `polling`  
  De processor vraagt steeds: "is er al data?"
  - makkelijk te begrijpen
  - minder efficient

- `interrupts`  
  De hardware verwittigt de processor zodra er data is
  - beter voor reactiesnelheid
  - iets moeilijker

- `DMA`  
  Data wordt bijna automatisch verplaatst zonder veel werk van de CPU
  - heel efficient
  - het moeilijkst

## Belangrijkste kernideeen

- Een `struct` groepeert gegevens die samen horen.
- Een `pointer` bewaart een adres.
- Met `&` vraag je een adres op.
- Met `*` ga je naar de waarde op dat adres.
- Een pin kan via `alternate function` gekoppeld worden aan een interne module zoals USART.
- `USART/UART` gebruik je voor seriele communicatie via `TX` en `RX`.
- Op de Nucleo gebruik je vaak `USART2` via USB, met `PA2` en `PA3`.

## Kort onthouden

- `struct` = doos met meerdere variabelen
- `pointer` = verwijzing naar een plaats in geheugen
- `alternate function` = pin krijgt speciale taak
- `USART` = seriele communicatie

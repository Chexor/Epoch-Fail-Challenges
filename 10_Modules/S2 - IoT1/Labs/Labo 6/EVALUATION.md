# Evaluation ex02-05_to_ex02-08

## 1) Wanneer gebruik je polling en wanneer interrupts voor UART-ontvangst?

### Kort antwoord

Gebruik polling als je eenvoudige code wil en er weinig andere taken tegelijk lopen.
Gebruik interrupts als je sneller en efficiënter wil reageren op ontvangen data.

### Polling

Bij polling controleert je programma zelf voortdurend of er een nieuwe byte ontvangen is.

Dat gebruik je vooral wanneer:
- het programma eenvoudig is,
- er maar af en toe data binnenkomt,
- de microcontroller verder weinig andere taken heeft,
- je de code zo eenvoudig mogelijk wil houden.

Voordeel:
- makkelijk te begrijpen en te programmeren.

Nadeel:
- de processor verspilt tijd met constant controleren,
- je kan een byte missen als je te laat controleert,
- minder geschikt als je ook snel op andere gebeurtenissen moet reageren.

### Interrupts

Bij interrupts meldt de hardware zelf aan de CPU dat er een byte ontvangen is.
De microcontroller springt dan automatisch naar de interrupt handler.

Dat gebruik je vooral wanneer:
- je onmiddellijk wil reageren op ontvangen data,
- er nog andere taken tegelijk lopen,
- je efficiënter met CPU-tijd wil omgaan,
- polling te traag of te onbetrouwbaar wordt.

Voordeel:
- snelle reactie,
- efficiënter,
- beter voor gelijktijdige taken.

Nadeel:
- iets moeilijker om te programmeren en debuggen.

Kort samengevat:
- `polling` = eenvoudig, maar minder efficiënt
- `interrupts` = krachtiger en sneller, maar iets complexer

## 2) Wat betekent `RXNEIE` bij USART2?

### Kort antwoord

`RXNEIE` betekent dat er een interrupt gegenereerd wordt wanneer er een nieuwe byte ontvangen is.

`RXNEIE` staat voor:

```text
RXNE interrupt enable
```

Betekenis:
- `RXNE` = `Receive data register not empty`
- er is dus een byte ontvangen en die staat klaar in het receive data register
- `IE` = interrupt enable

Als je `RXNEIE` aanzet in `USART2->CR1`, dan:
- activeer je een interrupt zodra `RXNE` gezet wordt,
- dus zodra er een nieuwe byte ontvangen is.

Praktisch betekent dit:
- de USART2-interrupt wordt opgeroepen,
- in de interrupt handler lees je meestal `USART2->RDR` uit,
- daarmee haal je de ontvangen byte op en wis je tegelijk de ontvangststatus.

In de reference manual moet je hiervoor kijken bij:
- `USART_CR1`
- bit `RXNEIE`

Kort:
- `RXNEIE = 1` -> interrupt bij ontvangen byte
- `RXNEIE = 0` -> geen interrupt bij ontvangen byte

## 3) Wat is een `struct` in C?

### Kort antwoord

Een `struct` bundelt meerdere variabelen die logisch bij elkaar horen in 1 nieuw type.

Een `struct` is een manier om meerdere variabelen samen te bundelen in 1 nieuw gegevenstype.
Die variabelen horen logisch bij elkaar en krijgen samen 1 naam.

Een `struct` is handig wanneer je gegevens samen wil bewaren, bijvoorbeeld:
- instellingen,
- meetwaarden,
- toestand van een onderdeel,
- of de registers van een hardwareblok.

De variabelen in een `struct` noem je `velden` of `members`.

Eenvoudig voorbeeld:

```c
struct Meting
{
    uint16_t adValue;
    uint32_t milliVolt;
    bool geldig;
};
```

Hier bundel je:
- de ruwe ADC-waarde,
- de omgerekende spanning in millivolt,
- een vlag die zegt of de meting geldig is.

Waarom is dat nuttig?
- de gegevens blijven samen,
- de code wordt overzichtelijker,
- je kan makkelijker grotere programma's structureren.

Voorbeeld uit je microcontrollerprogramma's:

In je code gebruik je constant dingen zoals:

```c
USART2->CR1 |= USART_CR1_RE;
GPIOA->MODER |= GPIO_MODER_MODER2_1;
```

`USART2` en `GPIOA` zijn in feite pointers naar een `struct` die alle registers van die hardware groepeert.
j
Heel vereenvoudigd ziet dat idee er zo uit:

```c
struct VoorbeeldUsart
{
    uint32_t CR1;
    uint32_t CR2;
    uint32_t BRR;
    uint32_t RDR;
    uint32_t TDR;
};
```

Daarna kan je velden aanspreken met de `.` of `->` operator.

Bijvoorbeeld:
- `meting.adValue` gebruikt `.` omdat `meting` een gewone variabele is;
- `USART2->CR1` gebruikt `->` omdat `USART2` een pointer is.

Kort samengevat:
- een `struct` groepeert gegevens die bij elkaar horen;
- in embedded C wordt dat vaak gebruikt om hardwareregisters, sensorgegevens of toestanden netjes te organiseren.

## Aanvullingen per oefening

### ex02-05
- Voeg hier later extra evaluatievragen over UART-ontvangst via polling toe.

### ex02-06
- Voeg hier later extra evaluatievragen over UART-ontvangst via interrupt toe.

### ex02-07
- Voeg hier later extra evaluatievragen over looplichten en seriële commando's toe.

### ex02-08
- Voeg hier later extra evaluatievragen over start/stop via UART-commando's toe.

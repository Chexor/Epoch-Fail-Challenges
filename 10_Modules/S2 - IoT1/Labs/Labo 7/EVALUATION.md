# Evaluation ex03-01_to_ex03-03

## 1) Vraag 1
Waarvoor zorgt de `SPE`-bit in `SPI_CR1`?1.	Gebruik voor deze vraag gelijk welk STM32-project, waarbij de SPI-bus ingeschakeld wordt.
Zet daarbij een breakpoint op een weloverwogen locatie, waarbij je in de functie InitSpi1(), 
de SPE-bit uit het CR1-register mooi ziet omschakelen van 0 naar 1.
	
Waarvoor zorgt deze SPE-bit precies?
### Kort antwoord
`SPE` schakelt de SPI-peripheral effectief aan of uit.

### Uitleg
- `SPE` = **SPI enable** (`SPI_CR1` register).
- Met `SPE = 0` staat SPI uit: geen actieve transmissie/ontvangst.
- Met `SPE = 1` wordt SPI actief: de module kan data versturen/ontvangen volgens de ingestelde mode.

In de gebruikte `InitSpi1()` zie je dit op het einde:
```c
SPI1->CR1 |= SPI_CR1_SPE;
```

![[Pasted image 20260331103534.png]]
![[Pasted image 20260331103614.png]]

![[Pasted image 20260331110853.png]]
*Bron: De definitie van de `SPE`-bit is te vinden in de **Reference Manual (RM0091)**, in de sectie over de SPI peripheral registers (`SPI_CR1`).*

## 2) Vraag 2
Als we JP1 van het Nucleo Extension Shield willen gebruiken om SPI-communicatie op te zetten met SPI1, op welke pin zal er dan mogelijks data vanuit een sensor naar de microcontroller passeren? 
Bewijs aan de hand van het schema van het Nucleo Extension Shield.

### Kort antwoord
De data van sensor naar microcontroller komt binnen op **MISO/SDI**, dus op **PA6 (SPI1_MISO / SDI1)**.
### Uitleg
Bij SPI geldt:
- `MOSI` = data van master naar slave.
- `MISO` = data van slave naar master.

De Nucleo is hier master. Sensor-data terug naar de Nucleo loopt dus via de MISO-lijn.
In de code is dat ook zichtbaar:
```c
GPIOA->MODER ... MODER6_1;   // PA6 alternate function
GPIOA->AFR[0] ...            // PA6 = SDI1 (AF0)
```

Dus voor JP1/SPI1 is de relevante binnenkomende datapin `PA6`.

![[Pasted image 20260331111556.png]]
*Bron: De configuratie van de `MODER` en `AFR` registers is gedetailleerd in de **Reference Manual (RM0091)**, in het hoofdstuk over GPIO.*

## 3) Vraag 3
Op het Nucleo Extension Shield is er één opstelling gemaakt die we als analoge ingang kunnen verwerken in onze microcontroller. 
Wat weet je hierover? Gebruik zeker ook het schema van het Nucleo Extension Shield om je uitleg doen.
### Kort antwoord
De analoge opstelling is de **on-board trimmer (potentiometer)**, uitgelezen via **ADC kanaal 0 op PA0**.

### Uitleg
Een **potentiometer** is een regelbare weerstand, die je kan zien als een "dimmerknop". Door eraan te draaien, verandert de uitgangsspanning (tussen 0V en 3.3V). Omdat deze variabele spanning rechtstreeks op de microcontroller-pin wordt aangeboden, moet de pin in **analoge modus** staan om de exacte positie van de knop te kunnen meten. Een digitale meting zou enkel "hoog" of "laag" kunnen detecteren.

In de AD-initialisatie staat:
```c
GPIOA->MODER |= GPIO_MODER_MODER0;   // PA0 analoog
ADC1->CHSELR = ADC_CHSELR_CHSEL0;    // kanaal 0
```

Dat betekent:
- de trimmer levert een variabele analoge spanning,
- die spanning wordt op PA0 binnengebracht,
- ADC zet die om naar een digitale waarde (0..4095).

In oefening 3.3 wordt net die waarde gebruikt om de stripkleur te kiezen over het volledige bereik.

*Bron: De details van de `MODER` (voor de pin-configuratie) en `CHSELR` (voor de kanaalselectie) registers staan in de **Reference Manual (RM0091)**, in respectievelijk de GPIO en ADC hoofdstukken.*


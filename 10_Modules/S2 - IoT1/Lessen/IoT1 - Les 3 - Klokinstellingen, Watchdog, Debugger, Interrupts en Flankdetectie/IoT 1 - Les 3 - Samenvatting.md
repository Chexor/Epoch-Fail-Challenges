# IoT 1 - Les 3 - Samenvatting

Les 3 draait rond "controle over je microcontroller": timing (klok), betrouwbaarheid (watchdog), fouten zoeken (debugger) en snel reageren op events (interrupts/flanken).

## Klokinstellingen (STM32F091RC)

- Zonder klok geen instructies; instructies starten typisch op de stijgende flank van het kloksignaal.
- MCU kan tot 48 MHz; klok komt uit interne RC-oscillatoren of extern kristal.
- Config gebeurt in `SystemClock_Config()`; leer de "clock tree" lezen.
- Typisch pad: start van 8 MHz interne RC (HSI) en via PLL naar 48 MHz voor de CPU-core (let op delers/vermenigvuldigers).

## Watchdog timer (IWDG)

- Doel: bij "vastlopers" automatisch resetten zodat je systeem terug herstart.
- IWDG is onafhankelijk (eigen klokbron, typisch LSI ~40 kHz) zodat hij blijft lopen ook als je main code misloopt.
- Gebruik volgt een vaste procedure (keys + prescaler + reload + refresh).
- Demo-idee: LEDs knipperen na reset, watchdog "voeden" bij knopdruk, en reset zien als je te lang wacht.

## Debuggen met µVision

- Programmeren = fouten maken; debuggen is de snelste manier om die te vinden.
- Breakpoints: code pauzeren om variabelen en registers te bekijken op "mensen-tempo".
- Tools:
  - `Watch Window` voor variabelen.
  - `System Viewer` voor registers.
- De on-board ST-Link programmer is ook een debugger.

## Interrupts (NVIC)

- Interrupt = verzoek om het hoofdprogramma onmiddellijk te onderbreken, ISR/handler uitvoeren, daarna verdergaan.
- Waarom: supersnel reageren op externe events (bv. seriele bytes die onverwacht binnenkomen).
- NVIC:
  - schakel tussen interruptbron en CPU;
  - kan 32 interruptkanalen beheren;
  - 4 programmeerbare prioriteitsniveaus (0..3, 0 = hoogste);
  - elke interruptbron heeft ook een vaste (niet-programmeerbare) prioriteit als tie-breaker.
- Voorbeeld: EXTI1 en SPI1 tegelijk met dezelfde programmeerbare priority -> vaste priority bepaalt wie eerst; wil je omdraaien, pas programmeerbare priority aan.

## External interrupts + flankdetectie (incl. dender)

- EXTI basisstappen: pin/lijn koppelen, rising/falling edge kiezen, interrupt unmasken/enable, pending vlag afhandelen en wissen.
- Flankdetectie bij knoppen: detecteer de overgang (stijgend/dalend) i.p.v. de toestand "ingedrukt blijven".
- Dender (bounce): 1 druk kan meerdere snelle overgangen geven -> kan meerdere interrupts triggeren.
- Eenvoudige debounce: korte wachttijd/filtering na detectie (of softwarelogica die slechts 1 event per druk toelaat).

## Actieve recall (checkvragen)

1. Waarom is "clock tree" lezen essentieel om 48 MHz aan de core te krijgen?
2. Waarom gebruikt de IWDG een eigen (LSI) klokbron?
3. Wat is het verschil tussen programmeerbare en niet-programmeerbare interruptprioriteit?
4. Welke stappen heb je minimaal nodig om een EXTI-interrupt te laten afgaan?
5. Waarom kan dender meerdere interrupts veroorzaken en hoe demp je dat eenvoudig?

# IoT 1 - Les 4 - Samenvatting

Les 4 focust op de hardware timers van de STM32-microcontroller. We leren hoe we exacte tijdsintervallen kunnen creëren zonder de CPU te belasten met wachtlussen.

## 1. Hardware Timers (TIMx)

In plaats van `delay()`-achtige functies te gebruiken, gebruiken we de ingebouwde timers van de microcontroller.

### Kernbegrippen
- **CNT (Counter)**: De teller die omhoog of omlaag telt bij elke klokpuls.
- **PSC (Prescaler)**: Een deler die de klokfrequentie vertraagt. Als de klok 48 MHz is en de PSC is 48.000, telt de timer op 1 kHz (1000 pulsen per seconde).
- **ARR (Auto-reload Register)**: De waarde waarbij de teller reset. Als ARR op 1000 staat en de klok op 1 kHz, reset de timer elke seconde.

### Berekening van de Periode
De formule voor de timer-frequentie ($f_{timer}$) is:
$$f_{timer} = \frac{f_{clk}}{(PSC + 1) \cdot (ARR + 1)}$$
Waar $f_{clk}$ de klokfrequentie van de bus is (meestal 48 MHz).

## 2. Slinger-project

Het "Slinger-project" is een praktische toepassing van timers.

### Doel
Het creëren van een lichteffect met de 8 LED's op het NES-shield, waarbij de LED's heen en weer gaan (zoals een slinger of "Knight Rider"-effect).

### Werking
- Gebruik een hardware timer om periodieke interrupts te genereren.
- In de ISR (Interrupt Service Routine) pas je de status van de LED's aan.
- Dit zorgt voor een vloeiende beweging die onafhankelijk van de `main()`-loop draait.

## 3. Voordelen van Hardware Timers
- **Nauwkeurigheid**: Veel preciezer dan softwarematige wachtlussen.
- **Efficiëntie**: De CPU kan andere taken uitvoeren terwijl de timer op de achtergrond telt.
- **Interrupts**: Timers kunnen automatisch acties triggeren op exacte tijdstippen.

## Actieve recall (checkvragen)
1. Wat is de functie van de Prescaler (PSC)?
2. Hoe bereken je de ARR-waarde voor een timer die precies 1 seconde moet duren bij een klok van 48 MHz en een PSC van 48.000?
3. Waarom is een hardware timer beter dan een `for`-loop als "delay"?
4. Wat gebeurt er als de teller (CNT) de waarde in het ARR-register bereikt?

# Labo5 ex02-03

## Opgave
Meet de potentiometer en stuur de spanning in volt naar de pc.

## Oplossing
- Lees de ADC-waarde.
- Reken om naar millivolt met referentie `3,3 V`.
- Formatteer de waarde als `x.xxx V`.
- Verstuur de tekst om de `500 ms` via `USART2`.

## Codevoorbeeld
```c
uint16_t adcValue = GetAdValue();
uint32_t milliVolt = (adcValue * 3300U) / 4095U;

sprintf(buffer, "%lu.%03lu V\r\n", milliVolt / 1000, milliVolt % 1000);
StringToUsart2(buffer);
WaitForMs(500);
```

## Korte uitleg
De ADC geeft een ruwe waarde. Door die te schalen en als tekst te formatteren, krijg je een leesbare spanningsmeting in de terminal.

## Concepten uit Labo 5
- ADC naar spanning
- millivolt
- `sprintf(...)`
- meetdata versturen

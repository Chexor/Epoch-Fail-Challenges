# Labo6 ex02-06

## Opgave
Maak dezelfde ontvangst als ex02-05, maar werk nu met een USART-interrupt.

## Oplossing
- Activeer `RXNEIE`, de receiver en de NVIC.
- Laat de hoofdlus leeg.
- Lees de ontvangen byte in `USART2_IRQHandler()`.
- Zet de ontvangen byte op de leds.
- Toon ook `CHAR`, `ASCII` en `BIN` via USART2.

## Codevoorbeeld
```c
USART2->CR1 |= USART_CR1_RXNEIE;
NVIC_SetPriority(USART2_IRQn, 0);
NVIC_EnableIRQ(USART2_IRQn);
USART2->CR1 |= USART_CR1_RE;

struct RxData
{
    uint8_t ascii;
    char binair[9];
    char bericht[48];
};

void USART2_IRQHandler(void)
{
    static struct RxData rx = {0};
    uint8_t i = 0;

    if((USART2->ISR & USART_ISR_RXNE) == USART_ISR_RXNE)
    {
        rx.ascii = (uint8_t)USART2->RDR;
        ByteToLeds(rx.ascii);

        for(i = 0; i < 8; i++)
        {
            if((rx.ascii & (1U << (7 - i))) != 0)
            {
                rx.binair[i] = '1';
            }
            else
            {
                rx.binair[i] = '0';
            }
        }

        sprintf(rx.bericht, "CHAR: %c ASCII: %u BIN: %s\r\n", rx.ascii, rx.ascii, rx.binair);
        StringToUsart2(rx.bericht);
    }
}
```

## Uitleg per lijn code

`USART2->CR1 |= USART_CR1_RXNEIE;`
- Zet de receive-interrupt aan.
- Zodra een byte ontvangen is, mag USART2 een interrupt aanvragen.

`NVIC_SetPriority(USART2_IRQn, 0);`
- Geeft de USART2-interrupt een prioriteit.
- Hier wordt prioriteit `0` gekozen.

`NVIC_EnableIRQ(USART2_IRQn);`
- Zet de USART2-interrupt aan in de interrupt controller.
- Zonder deze lijn wordt de handler niet uitgevoerd.

`USART2->CR1 |= USART_CR1_RE;`
- Zet de receiver aan.
- Vanaf nu kan USART2 data ontvangen.

`struct RxData`
- Dit maakt een structuur aan.
- In die structuur worden de ontvangen ASCII-waarde, de binaire tekst en het bericht samengehouden.

`{`
- Begin van de structuur.

`uint8_t ascii;`
- Hier wordt de ontvangen byte bewaard als getal.

`char binair[9];`
- Hier komt de binaire voorstelling van de byte.
- Er is plaats voor 8 tekens.

`char bericht[48];`
- Hier komt de volledige tekst die via USART2 terug verstuurd wordt.

`};`
- Einde van de structuur.

`void USART2_IRQHandler(void)`
- Dit is de interrupt functie van USART2.
- Deze functie wordt automatisch uitgevoerd bij een USART2-interrupt.

`static struct RxData rx = {0};`
- Maakt een vaste variabele `rx` van de structuur aan.
- Alle velden starten op `0`.

`uint8_t i = 0;`
- Hulpvariabele voor de `for`-lus.
- Hiermee wordt door de 8 bits van de byte gelopen.

`{`
- Begin van de functie.

`if((USART2->ISR & USART_ISR_RXNE) == USART_ISR_RXNE)`
- Controleert of er echt een byte ontvangen is.
- `RXNE` betekent dat het receive register niet leeg is.

`{`
- Begin van het `if`-blok.

`rx.ascii = (uint8_t)USART2->RDR;`
- Leest de ontvangen byte uit `RDR`.
- Die byte wordt bewaard in `rx.ascii`.

`ByteToLeds(rx.ascii);`
- Zet de ontvangen byte op de 8 leds.
- Elke led toont 1 bit van die byte.

`for(i = 0; i < 8; i++)`
- Deze lus bekijkt de 8 bits van de ontvangen byte, van links naar rechts.

`if((rx.ascii & (1U << (7 - i))) != 0)`
- Controleert of de huidige bit gelijk is aan `1`.

`rx.binair[i] = '1';`
- Als de bit `1` is, zet de code het teken `'1'` in de tekst.

`else`
- Anders is de bit `0`.

`rx.binair[i] = '0';`
- Dan zet de code het teken `'0'` in de tekst.

`sprintf(rx.bericht, "CHAR: %c ASCII: %u BIN: %s\r\n", rx.ascii, rx.ascii, rx.binair);`
- Maakt een tekstbericht met het karakter, de ASCII-waarde en de binaire voorstelling.

`StringToUsart2(rx.bericht);`
- Verstuurt dat tekstbericht terug via USART2 naar de pc.

`}`
- Einde van het `if`-blok.

`}`
- Einde van de interrupt functie.

## Korte uitleg
Bij een ontvangen byte roept de hardware automatisch de handler op. Daardoor hoeft de hoofdlus niet voortdurend te controleren of er data is.

## Concepten uit Labo 6
- USART interrupt
- `RXNEIE`
- `USART2_IRQHandler()`
- event-driven ontvangst

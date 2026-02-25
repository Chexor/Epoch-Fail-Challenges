# Steekproefverdelingen

## Overzicht
Stel je voor dat je niet een, maar heel veel steekproeven uit dezelfde populatie neemt. Van elke steekproef bereken je bijvoorbeeld het gemiddelde. De verdeling van al die steekproefgemiddelden is de **steekproefverdeling**.

## Centrale Limietstelling
Zelfs als de populatie zelf niet normaal verdeeld is, zal de verdeling van de steekproefgemiddelden (bij een voldoende grote steekproef) een **normale verdeling** benaderen.

## Standaardfout
De **standaardfout** is de standaardafwijking van de steekproefverdeling. Ze meet hoe hard een puntschatting (zoals `x̄`) typisch varieert van steekproef tot steekproef.

Voor een gemiddelde is de standaardfout:
$$ SE = \frac{\sigma}{\sqrt{n}} $$

Als `\sigma` onbekend is, schatten we met de steekproefstandaardafwijking `s`:
$$ SE \approx \frac{s}{\sqrt{n}} $$

## t-verdeling (Student)
De **t-verdeling** lijkt op de normale verdeling, maar met dikkere staarten. We gebruiken deze vooral als:
- de steekproef klein is;
- en de populatiestandaardafwijking `σ` onbekend is (we gebruiken `s`).

## Waarom is dit belangrijk?
Dit is de brug tussen beschrijvende en verklarende statistiek. Het laat ons toe om op basis van een steekproef uitspraken te doen over de hele populatie.

# Oefening 3 - Handleiding (TI-36X Pro)

Doel: kansen met complementen en (veronderstelde) onafhankelijkheid. TI gebruik je enkel voor het rekenwerk.

## Opgave

![[DA-Voorbeeldexamen-Oef3.png]]

## Gegeven

Definieer:
- $A$ = “meer dan 1 werkongeval in afdeling A” met $P(A)=0.20$
- $B$ = “meer dan 1 werkongeval in afdeling B” met $P(B)=0.25$

Neem $A$ en $B$ onafhankelijk (zoals in de opgave/oplossing).

## (a) Op geen van beide afdelingen

Dit is $\bar{A}\cap \bar{B}$.

Manueel:
$$
P(\bar{A}\cap \bar{B})=P(\bar{A})P(\bar{B})=(1-0.20)(1-0.25)=0.80\cdot 0.75=0.60
$$

TI: `0.8*0.75`.

## (b) Op beide afdelingen

Manueel:
$$
P(A\cap B)=P(A)P(B)=0.20\cdot 0.25=0.05
$$

TI: `0.2*0.25`.

## (c) Op minstens 1 van de 2 afdelingen

Manueel (2 manieren):
$$
P(A\cup B)=P(A)+P(B)-P(A\cap B)
$$
of
$$
P(A\cup B)=1-P(\bar{A}\cap \bar{B})
$$

TI: reken uit met je gekozen formule.

## (d) Wel in A, niet in B

Manueel:
$$
P(A\setminus B)=P(A\cap \bar{B})=P(A)P(\bar{B})=0.20\cdot 0.75=0.15
$$

TI: `0.2*0.75`.

## Handige links

- [[DA-Voorbeeldexamen-TI-36X-Pro-Manual]]

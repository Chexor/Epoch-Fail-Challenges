---
type: theory
domain: "machine-learning"
parent: "Neural Network Models"
related:
  - Neural Network Models
  - Transformer
  - Self-Attention
  - Deep Learning
  - Machine Learning
  - Attention Python Worked Example
theme: "neural-network-models"
aliases:
  - Attention Mechanism
  - Attention
---

# Attention
#concept #ml

Attention is een mechanisme waarbij een model dynamisch bepaalt welke delen van de input op dat moment het belangrijkst zijn voor de huidige verwerking of voorspelling.

## Korte kern

- attention kent gewichten toe aan verschillende stukken context
- het laat een model focussen op relevante informatie in plaats van alles even sterk te behandelen
- `self-attention` is een specifieke vorm waarbij tokens naar andere tokens in dezelfde sequentie kijken

## 1. Wat is het kernprobleem?

Hoe kan een model uit veel mogelijke inputelementen snel bepalen welke informatie nu relevant is voor een bepaalde output of tussenstap?

## 2. Intuitieve uitleg

Denk aan lezen met een markeerstift: je kijkt niet naar elk woord even intensief, maar geeft meer gewicht aan woorden die nu belangrijk zijn.

In een neuraal netwerk doet attention iets gelijkaardigs:

- mogelijke contextstukken krijgen een score
- die scores worden omgezet naar gewichten
- relevante informatie krijgt meer invloed op het eindresultaat

Zo hoeft het model niet alle context op exact dezelfde manier te behandelen.

## 3. Formele structuur

In moderne modellen betekent attention meestal dat een model:

- een `query` vormt: waar zoekt dit deel van het model naar?
- `keys` gebruikt: welke stukken context zijn beschikbaar?
- `values` gebruikt: welke informatie moet uiteindelijk doorgegeven worden?

De aandachtgewichten bepalen dan hoeveel elke `value` bijdraagt aan de output.

Bij `scaled dot-product attention` is de kernvorm:

```text
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V
```

Belangrijke ideeën:

- `softmax` maakt van scores vergelijkbare gewichten
- hogere score betekent meer aandacht
- attention is dynamisch: de gewichten hangen af van de huidige input
- moderne varianten gebruiken vaak `multi-head attention`

## 4. Snelle vergelijking

- `Attention` = algemene techniek om context dynamisch te wegen
- [[Self-Attention]] = aandacht binnen dezelfde sequentie
- [[Transformer]] = architectuur die sterk op attention steunt
- [[Neural Network]] = breder begrip dat veel modellen omvat zonder noodzakelijk attention te gebruiken

## 5. Toepassing

Bij vertaling of tekstgeneratie kan attention helpen om voor een huidig woord vooral te kijken naar de relevante eerdere woorden, in plaats van alle context als een enkele vaste samenvatting te behandelen.

Dat maakt langere afhankelijkheden beter hanteerbaar.

Kort Python-voorbeeld:

```python
def normalize(scores):
    total = sum(scores)
    return [score / total for score in scores]


weights = normalize([2.0, 3.0, 5.0])
```

Voor een volledige Python-uitwerking, zie [[Attention Python Worked Example]].

## 6. Begripsafbakening en verbanden

- **Kernonderscheid:** attention is een mechanisme binnen een model, geen volledig modeltype op zich.
- **Veelvoorkomende misvatting:** denken dat attention hetzelfde is als `transformer`; transformers gebruiken attention intensief, maar het zijn niet dezelfde concepten.
- **Link met andere concepten:** [[Machine Learning]], [[Neural Network Models]], [[Neural Network]], [[Deep Learning]], [[Self-Attention]], [[Transformer]], [[Attention Python Worked Example]], [[Transformer Python Worked Example]]

## Probleem

Nog aan te vullen.

## Intuïtie

Nog aan te vullen.

## Toepassing

Nog aan te vullen.

## Formeel

Nog aan te vullen.

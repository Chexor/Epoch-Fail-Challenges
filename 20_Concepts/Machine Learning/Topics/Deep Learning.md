---
type: concept-topic
domain: "machine-learning"
parent: "Neural Network Models"
related:
  - Neural Network Models
  - Neural Network
  - Convolutional Neural Network (CNN)
  - Machine Learning vs Deep Learning
theme: "neural-network-models"
aliases:
  - Deep Learning
---

# Deep Learning
#concept #ml

## 1. Wat is het kernprobleem?
Hoe leer je zeer complexe patronen uit data wanneer eenvoudige modellen onvoldoende krachtig zijn?

## 2. Intuitieve uitleg
`Deep Learning` gebruikt neurale netwerken met meerdere lagen, zodat een model stap voor stap rijkere representaties kan opbouwen.

Bij beeldherkenning kan een diep netwerk bijvoorbeeld eerst eenvoudige patronen leren zoals randen, daarna vormen en texturen, en uiteindelijk volledige objecten zoals cijfers, gezichten of auto's.

De kernintuïtie is:

- vroege lagen leren **eenvoudige kenmerken**
- diepere lagen combineren die tot **complexe concepten**

## 3. Formele structuur
`Deep Learning` is een subdomein van [[Machine Learning]] dat steunt op [[Neural Network|neurale netwerken]] met meerdere `hidden layers`.

Belangrijke kenmerken:

- gebruikt een gelaagde netwerkstructuur
- leert representaties automatisch uit data
- heeft vaak veel data en rekenkracht nodig
- wordt meestal getraind met varianten van [[Gradient Descent]]
- gebruikt vaak frameworks zoals [[Keras]]

Typische modellen binnen deep learning zijn:

- gewone feedforward netwerken
- [[Sequential Neural Net]]
- [[Convolutional Neural Network (CNN)]]

Sterktes:

- zeer krachtig bij beeld, spraak en complexe patroonherkenning
- kan zelf nuttige features leren uit ruwe data

Zwaktes:

- data-hongerig
- rekenintensief
- vaak moeilijk interpreteerbaar als `black box`

## 4. Toepassing
Typische toepassingen zijn:

- handgeschreven cijfers herkennen
- objecten detecteren in beelden
- spraak herkennen
- tekst classificeren

In de cursus is het vooral belangrijk dat je begrijpt dat `Deep Learning` geen volledig aparte familie buiten machine learning is, maar een krachtig subdomein ervan.

## 5. Examengerichte vertaling
- **Typische vraag:** wat onderscheidt `Deep Learning` van klassieke `Machine Learning`?
- **Vaak gemaakte fout:** denken dat `deep` gewoon "moeilijk" betekent, terwijl het specifiek verwijst naar meerdere lagen in een neuraal netwerk.
- **Link met andere concepten:** [[Machine Learning]], [[Neural Network]], [[Sequential Neural Net]], [[Convolutional Neural Network (CNN)]], [[Gradient Descent]], [[Keras]], [[Scikit-learn]], [[Machine Learning vs Deep Learning]]

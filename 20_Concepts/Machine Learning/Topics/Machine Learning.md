---
type: concept-topic
domain: "machine-learning"
parent:
related:
  - Learning Paradigms
  - ML Problem Framing
  - Linear Modeling
  - Neural Network Models
theme: "data-driven-pattern-learning"
aliases:
  - Machine Learning
---

# Machine Learning
#concept #ml

## 1. Wat is het kernprobleem?
Hoe laat je een systeem patronen leren uit data, zodat het op nieuwe voorbeelden goede beslissingen of voorspellingen kan maken zonder dat elke regel expliciet geprogrammeerd is?

## 2. Intuitieve uitleg
Bij `Machine Learning` geef je een model geen volledige lijst met regels, maar wel data waaruit het zelf verbanden leert. In plaats van te zeggen *"als dit, dan dat"*, laat je het model ontdekken welke input typisch samenhangt met welke output of structuur.

Denk aan huizenprijzen voorspellen. Je geeft voorbeelden van woningen met kenmerken zoals oppervlakte, ligging en aantal kamers. Het model leert dan welke patronen meestal leiden tot een bepaalde prijs.

Het grote idee is dus:

- **klassiek programmeren**: regels schrijven op basis van menselijk inzicht
- **machine learning**: regels laten afleiden uit data

## 3. Formele structuur
`Machine Learning` is een deelgebied van [[Artificial Intelligence (AI)]] waarin een model leert uit data.

Belangrijke bouwstenen zijn:

- [[Data, Example, Feature, Target|data]]: de voorbeelden waarop het model leert
- `features`: de invoervariabelen
- `target`: de gewenste output, als die gekend is
- `model`: de wiskundige structuur die patronen probeert te leren
- `training`: het proces waarbij parameters aangepast worden
- `evaluation`: controleren hoe goed het model presteert op nieuwe data

De drie grote leerparadigma's zijn:

- [[Supervised Learning]]: leren met input-outputparen `(x, y)`
- [[Unsupervised Learning]]: leren zonder labels
- [[Reinforcement Learning]]: leren via interactie, beloning en straf

Typische probleemtypes zijn:

- [[Classification vs Regression|classificatie]]: een klasse voorspellen
- [[Classification vs Regression|regressie]]: een continue waarde voorspellen
- `clustering`: gelijkaardige datapunten groeperen

Voorbeelden van algoritmes:

- [[Linear Regression]]
- [[K-Nearest Neighbors (KNN)]]
- [[K-Means]]
- [[Neural Network]]

## 4. Toepassing
Enkele typische toepassingen zijn:

- spamdetectie in e-mails
- huisprijzen voorspellen
- klanten segmenteren in groepen
- handgeschreven cijfers herkennen
- aanbevelingen doen op basis van gebruikersgedrag

In een inleidend AI-vak is vooral belangrijk dat je begrijpt:

- welk type probleem je voor je hebt
- of er labels aanwezig zijn
- welk algoritme of model daarbij past

## 5. Examengerichte vertaling
- **Typische vraag:** wat is het verschil tussen `Machine Learning`, [[Deep Learning]], [[Supervised Learning]] en [[Unsupervised Learning]]?
- **Vaak gemaakte fout:** denken dat alle machine learning neerkomt op neurale netwerken.
- **Link met andere concepten:** [[Artificial Intelligence (AI)]], [[Supervised Learning]], [[Unsupervised Learning]], [[Reinforcement Learning]], [[Classification vs Regression]], [[Linear Regression]], [[K-Nearest Neighbors (KNN)]], [[K-Means]], [[Neural Network]], [[Deep Learning]], [[Sequential Neural Net]], [[Scikit-learn]], [[Keras]], [[Machine Learning vs Deep Learning]], [[Supervised vs Unsupervised vs Reinforcement Learning]]

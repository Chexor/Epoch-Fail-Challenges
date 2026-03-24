---
type: concept-map
domain: "machine-learning"
parent:
related:
  - Data, Example, Feature, Target
  - Linear Regression
  - Gradient Descent
theme: "supervised-learning-foundations"
aliases:
  - Overzicht Machine Learning Concepten
  - Machine Learning Concepten
---

# Overzicht Machine Learning Concepten
#concept #ml

## Doel van dit overzicht

Deze note groepeert de conceptnotes rond machine learning zodat je sneller verbanden ziet tussen basisbegrippen, regressie, optimalisatie, evaluatie en tools.

## Groot plaatje

Machine learning gaat niet alleen over modellen trainen, maar over een volledige keten:
- het probleemtype herkennen
- data en features begrijpen
- een model opbouwen
- fouten meten
- parameters optimaliseren
- het resultaat interpreteren of implementeren

Deze map-note is dus geen losse linklijst, maar een leerkaart van hoe de belangrijkste concepten samenhangen.

## Centrale vragen

- Welk type probleem wil je oplossen: `classification`, `regression` of `clustering`?
- Welke informatie is input en welke grootheid wil je voorspellen?
- Hoe meet je fout of modelkwaliteit?
- Hoe leert een model zijn parameters aanpassen?
- Wanneer volstaat een klassiek model en wanneer heb je een neuraal netwerk nodig?

---

## 1. Basisbegrippen

- [[Machine Learning]]
- [[Learning Paradigms]]
- [[ML Problem Framing]]
- [[Data, Example, Feature, Target]]
- [[Supervised Learning]]
- [[Unsupervised Learning]]
- [[Reinforcement Learning]]
- [[Classification vs Regression]]

Deze concepten helpen je bepalen:
- wat je input is
- wat je output is
- welk type ML-probleem je hebt

---

## 2. Linear Regression

- [[Linear Modeling]]
- [[Linear Regression]]
- [[Slope en Intercept]]
- [[Dot Product]]
- [[OLS (Ordinary Least Squares)]]

Deze groep gaat over:
- hoe een lineair model is opgebouwd
- hoe je een voorspelling berekent
- hoe de best passende lijn gevonden wordt

---

## 3. Andere basismodellen

- [[K-Nearest Neighbors (KNN)]]
- [[K-Means]]

Deze groep helpt je onderscheiden:
- voorbeelden met labels versus zonder labels
- classificatie/regressie versus clustering

---

## 4. Foutmaten en loss

- [[Model Evaluation]]
- [[Loss Function]]
- [[SSE (Sum of Squared Errors)]]
- [[MSE (Mean Squared Error)]]
- [[MAE (Mean Absolute Error)]]
- [[RMSE (Root Mean Squared Error)]]
- [[R2 en R]]
- [[MAE vs MSE vs RMSE]]

Deze concepten helpen je begrijpen:
- hoe je fouten meet
- hoe je modellen vergelijkt
- hoe je modelkwaliteit interpreteert

---

## 5. Wiskundige basis voor optimalisatie

- [[Derivative (Afgeleide)]]
- [[Gradient]]

Deze notities vormen de brug tussen wiskunde en machine learning:
- afgeleide = helling op 1 punt
- gradient = uitbreiding naar meerdere variabelen

---

## 6. Optimalisatie en training

- [[Optimization and Training]]
- [[Gradient Descent]]
- [[SGD (Stochastic Gradient Descent)]]
- [[Mini-batch Gradient Descent]]
- [[Learning Rate]]
- [[Epoch]]
- [[Parameters vs Hyperparameters]]
- [[Grid Search]]
- [[Gradient Descent Worked Example]]

Deze groep gaat over:
- hoe een model leert
- hoe parameters worden aangepast
- welke instellingen je zelf kiest en tunet

---

## 7. Preprocessing

- [[Data Preparation]]
- [[Feature Scaling en Normalization]]

Dit concept is belangrijk omdat preprocessing vaak mee bepaalt of training stabiel en snel verloopt.

---

## 8. Neural networks en implementatie

- [[Neural Network Models]]
- [[ML Tooling and Frameworks]]
- [[Neural Network]]
- [[Deep Learning]]
- [[Convolutional Neural Network (CNN)]]
- [[Scikit-learn]]
- [[Keras]]
- [[Sequential Neural Net]]

Deze notes tonen:
- met welke tools je de theorie in code omzet
- wanneer je klassieke ML gebruikt
- wanneer je met neurale netwerken werkt

---

## 8.5 Belangrijke vergelijkingen

- [[Machine Learning vs Deep Learning]]
- [[Supervised vs Unsupervised vs Reinforcement Learning]]

Deze vergelijkingsnotes helpen je snel zien:
- wanneer een begrip breder of specifieker is
- welk leerparadigma je precies voor je hebt
- welke verwarring je op examen moet vermijden

---

## 9. Hoe hangen deze groepen samen?

- [[Machine Learning]] geeft het overkoepelende kader.
- [[Data, Example, Feature, Target]], [[Supervised Learning]] en [[Unsupervised Learning]] bepalen het probleemtype.
- [[Reinforcement Learning]] toont een derde leerparadigma waarin interactie en beloning centraal staan.
- [[Linear Regression]], [[K-Nearest Neighbors (KNN)]] en [[K-Means]] zijn concrete modelfamilies.
- [[Loss Function]], [[MSE (Mean Squared Error)]] en [[R2 en R]] helpen prestaties interpreteren.
- [[Gradient]], [[Gradient Descent]] en [[Learning Rate]] verklaren hoe modellen leren.
- [[Neural Network]] en [[Deep Learning]] bouwen verder op dezelfde leerlogica, maar met rijkere modelstructuren.

---

## 10. Aanbevolen leerpad

Als je deze concepten opnieuw wil studeren, volg dan best deze volgorde:

1. [[Machine Learning]]
2. [[Data, Example, Feature, Target]]
3. [[Supervised Learning]], [[Unsupervised Learning]], [[Reinforcement Learning]]
4. [[Supervised vs Unsupervised vs Reinforcement Learning]]
5. [[Classification vs Regression]]
6. [[Linear Regression]]
7. [[K-Nearest Neighbors (KNN)]] en [[K-Means]]
8. [[Machine Learning vs Deep Learning]]
9. [[Slope en Intercept]]
10. [[Loss Function]]
11. [[MAE vs MSE vs RMSE]]
12. [[Derivative (Afgeleide)]]
13. [[Gradient]]
14. [[Gradient Descent]]
15. [[Gradient Descent Worked Example]]
16. [[Learning Rate]], [[Epoch]], [[SGD (Stochastic Gradient Descent)]], [[Mini-batch Gradient Descent]]
17. [[OLS (Ordinary Least Squares)]]
18. [[R2 en R]]
19. [[Feature Scaling en Normalization]]
20. [[Grid Search]]
21. [[Neural Network]], [[Deep Learning]], [[Convolutional Neural Network (CNN)]]
22. [[Scikit-learn]] en [[Keras]]

---

## 11. Verwante kennisdomeinen

- [[Artificial Intelligence (AI)]] als bredere context
- [[00_Overzicht Artificial Intelligence]] voor de symbolische en search-kant van AI

# Les 4 - Linear Regression

Doel van deze notitie: concepten kort, duidelijk en gelijkwaardig bijhouden.
Wanneer je een nieuw concept doorstuurt, voeg ik het toe in hetzelfde format.

---

## Concept 1: Grid Search

`Grid Search` test automatisch meerdere combinaties van hyperparameters en kiest de beste op basis van validatiescore.

Kort voorbeeld:
- `alpha = [0.1, 1, 10]`
- `degree = [1, 2]`
- combinaties: `3 x 2 = 6`

Het model test die 6 combinaties en houdt de best scorende combinatie over.

---

## Concept 2: Derivative (Afgeleide)

De **afgeleide** zegt hoe snel een functie verandert op een bepaald punt (de helling van de grafiek).

Kort voorbeeld:
- `f(x) = x^2`
- `f'(x) = 2x`
- bij `x = 3` is de helling `6`

In machine learning gebruik je afgeleiden in gradient descent om parameters stap voor stap te verbeteren.

---

## Concept 3: SSE (Sum of Squared Errors)

`SSE` is de som van alle gekwadrateerde voorspelfouten.

Formule:
- `SSE = sum((y_i - y_hat_i)^2)`

Kort voorbeeld:
- echte waarden: `[3, 5, 7]`
- voorspellingen: `[2, 5, 9]`
- fouten: `[1, 0, -2]`
- gekwadrateerde fouten: `[1, 0, 4]`
- `SSE = 5`

Lager is beter: een lagere SSE betekent dat voorspellingen dichter bij de echte waarden liggen.

---

## Concept 4: Gradient Descent

`Gradient Descent` is een methode om modelparameters stap voor stap aan te passen zodat de fout kleiner wordt.

Intuitie:
- je staat op een heuvel en wil naar het laagste punt
- je neemt telkens een kleine stap naar beneden
- in ML is die "heuvel" de foutfunctie

Kort voorbeeld:
- start met willekeurige parameterwaarden
- bereken de afgeleide (richting van grootste stijging)
- ga in de omgekeerde richting (naar daling)
- herhaal tot de fout bijna niet meer daalt

Belangrijk:
- `learning rate` bepaalt hoe groot elke stap is
- te groot: je springt over het minimum
- te klein: leren gaat traag

---

## Concept 5: Loss Function

Een `loss function` is een formule die meet hoe fout de voorspellingen van je model zijn.

Kort idee:
- per datapunt bereken je het verschil tussen echt en voorspeld
- die verschillen zet je om naar 1 getal: de loss
- tijdens training probeer je die loss zo laag mogelijk te maken

Kort voorbeeld (regressie):
- gebruik `SSE` of `MSE` als loss
- als voorspellingen dichter bij echte waarden liggen, daalt de loss

Link met gradient descent:
- gradient descent past parameters aan om de loss stap voor stap te verlagen

---

## Concept 6: Scikit-learn

`Scikit-learn` is een Python-bibliotheek om machine-learningmodellen te bouwen, trainen en evalueren.

Kort idee:
- je hoeft algoritmes niet zelf vanaf nul te programmeren
- je gebruikt kant-en-klare tools met een consistente structuur
- veelgebruikte stappen: `fit()` om te trainen en `predict()` om te voorspellen

Kort voorbeeld:
- je maakt een `LinearRegression()` model
- je traint met `model.fit(X_train, y_train)`
- je voorspelt met `model.predict(X_test)`

In deze les gebruik je scikit-learn vaak voor linear regression, metrics en tools zoals `GridSearchCV`.

---

## Concept 7: Keras Library

`Keras` is een Python-library om neurale netwerken snel op te bouwen en te trainen.

Kort idee:
- je bouwt een model in lagen (`layers`)
- je kiest een loss function en optimizer
- je traint met `model.fit(...)`

Kort voorbeeld:
- maak een `Sequential` model
- voeg `Dense` lagen toe
- compileer met bv. `loss="mse"` en optimizer `adam`
- train op je trainingsdata

Keras wordt vaak gebruikt bovenop TensorFlow en is handig voor deep learning taken.

---

## Concept 8: Sequential Neural Net

Een `sequential neural net` is een neuraal netwerk waarbij lagen netjes na elkaar staan: input -> hidden layers -> output.

Kort idee:
- data gaat van laag 1 naar laag 2 naar laag 3
- elke laag leert een stukje patroon
- de laatste laag geeft de voorspelling

Kort voorbeeld:
- inputlaag met je features
- 1 of 2 `Dense` hidden lagen met activatie (bv. `relu`)
- outputlaag met 1 neuron voor regressie

Dit type netwerk is de eenvoudigste startvorm in Keras (`Sequential`) en werkt goed voor basisproblemen.

---

## Concept 9: SGD (Stochastic Gradient Descent)

`SGD` is een variant van gradient descent waarbij je parameters update met kleine stukjes data (vaak 1 sample of mini-batch) in plaats van de volledige dataset.

Kort idee:
- sneller updates tijdens training
- minder geheugen nodig
- meer schommelingen, maar vaak sneller naar een goede oplossing

Kort voorbeeld:
- in plaats van 10.000 rijen ineens te gebruiken
- update je model bv. per mini-batch van 32 rijen
- na elke mini-batch worden gewichten aangepast

In Keras kies je dit vaak als optimizer met `SGD(...)`.

---

## Concept 10: MSE (Mean Squared Error)

`MSE` is het gemiddelde van de gekwadrateerde voorspelfouten.

Formule:
- `MSE = (1/n) * sum((y_i - y_hat_i)^2)`

Kort voorbeeld:
- als `SSE = 20` en je hebt `n = 5` datapunten
- dan is `MSE = 20/5 = 4`

Interpretatie:
- lagere `MSE` is beter
- grote fouten tellen extra zwaar door omdat ze gekwadrateerd worden
- `MSE` is eigenlijk `SSE` gedeeld door het aantal datapunten

---

## Concept 11: Learning Rate

De `learning rate` bepaalt hoe groot elke update-stap is tijdens training.

Kort idee:
- bij gradient descent pas je parameters telkens een beetje aan
- de learning rate zegt hoeveel je per stap verandert

Kort voorbeeld:
- `learning rate = 0.1`: grotere stappen, sneller maar risico op overshoot
- `learning rate = 0.001`: kleinere stappen, stabieler maar trager

Belangrijk:
- te groot -> model kan heen en weer springen en niet convergeren
- te klein -> training duurt lang en kan blijven hangen

---

## Concept 12: Dot Product

Het `dot product` (inwendig product) combineert twee vectoren tot 1 getal door component per component te vermenigvuldigen en op te tellen.

Formule:
- `a . b = a1*b1 + a2*b2 + ... + an*bn`

Kort voorbeeld:
- `a = [2, 3]`
- `b = [4, 5]`
- `a . b = 2*4 + 3*5 = 8 + 15 = 23`

In linear regression gebruik je dit om een voorspelling te maken:
- `y_hat = w . x + b`
- dus: gewichten en features worden via dot product gecombineerd.

---

## Concept 13: Data, Example, Feature, Target

Basiswoorden in ML:
- `data`: de volledige tabel
- `example` (sample): 1 rij in de tabel
- `feature`: invoervariabele (kolom)
- `target`: wat je wil voorspellen

Kort voorbeeld:
- feature: aantal kamers
- target: huisprijs

---

## Concept 14: Supervised vs Unsupervised vs Reinforcement Learning

`Supervised learning` gebruikt gelabelde data (met target).
`Unsupervised learning` gebruikt data zonder labels.
`Reinforcement learning` leert via beloningen of straffen tijdens interactie met een omgeving.

Kort voorbeeld:
- supervised: prijs voorspellen op basis van historische prijzen
- unsupervised: klanten groeperen zonder vooraf labels
- reinforcement: een agent leert betere acties kiezen via feedback

---

## Concept 15: Classification vs Regression

`Classification` voorspelt een categorie.
`Regression` voorspelt een numerieke waarde.

Kort voorbeeld:
- classification: spam of geen spam
- regression: salaris of huisprijs

---

## Concept 16: Linear Regression

Linear regression zoekt de best passende rechte (of vlak in meerdere dimensies).

Kernformule:
- `y_hat = a*x + b` (1 feature)
- met meerdere features: `y_hat = a0 + a1*x1 + a2*x2 + ...`

Doel: parameters kiezen zodat de voorspelfout zo klein mogelijk is.

---

## Concept 17: Slope en Intercept

In `y = a*x + b`:
- `a` = slope (helling)
- `b` = intercept (snijpunt met y-as)

Kort voorbeeld:
- `y = 100 + 50*x`
- bij `x = 4` krijg je `y = 300`

---

## Concept 18: MAE (Mean Absolute Error)

`MAE` is het gemiddelde van de absolute fouten.

Formule:
- `MAE = (1/n) * sum(|y_i - y_hat_i|)`

Eigenschap:
- makkelijk te interpreteren
- minder gevoelig voor uitschieters dan MSE

---

## Concept 19: OLS (Ordinary Least Squares)

`OLS` is de exacte methode die de som van gekwadrateerde fouten minimaliseert bij lineaire regressie.

Kort idee:
- geen iteratieve stappen nodig zoals bij gradient descent
- direct een analytische oplossing voor slope en intercept

In scikit-learn gebruikt `LinearRegression` standaard OLS.

---

## Concept 20: Epoch

Een `epoch` is 1 volledige doorgang door alle trainingsdata.

Kort voorbeeld:
- 1000 datapunten
- na 1 epoch heeft het model alle 1000 punten 1 keer gezien

Meer epochs kan helpen, maar te veel kan ook overfitting geven.

---

## Concept 21: Parameter vs Hyperparameter

`Parameters` worden geleerd door het model (bv. `a` en `b`).
`Hyperparameters` kies je zelf vooraf (bv. `learning rate`, `epochs`, `batch size`).

Kort voorbeeld:
- parameter: slope
- hyperparameter: `learning_rate = 0.01`

---

## Concept 22: Mini-batch Gradient Descent

Bij mini-batch gradient descent update je met een kleine groep datapunten per stap.

Vormen:
- SGD: batch size = 1
- mini-batch: batch size tussen 1 en volledige dataset
- batch gradient descent: volledige dataset per stap

Mini-batch is vaak een goed compromis tussen snelheid en stabiliteit.

---

## Concept 23: RMSE

`RMSE` is de wortel van MSE.

Formule:
- `RMSE = sqrt(MSE)`

Belangrijk:
- zelfde eenheid als de target
- daardoor vaak makkelijker leesbaar dan MSE

---

## Concept 24: R2 en R

`R2` (coefficient of determination) toont hoeveel variantie door het model verklaard wordt.

Kort idee:
- `R2` ligt meestal tussen 0 en 1
- dichter bij 1 betekent meestal betere fit

`R` is de correlatiecoefficient (tussen -1 en 1).
Let op: correlatie is niet hetzelfde als causaliteit.

---

## Concept 25: Feature Scaling en Normalization

Grote getallen kunnen gradient descent instabiel maken (bv. overflow).
Daarom schaal je features vaak vooraf.

Veelgebruikte technieken:
- min-max scaling: `(x - min(x)) / (max(x) - min(x))`
- standardization: `(x - mean(x)) / std(x)`

Praktisch effect:
- stabielere training
- vaak snellere convergentie

---

## Uitgebreide samenvatting van Les 4

## 1) Grote plaatje

In deze les leer je hoe je een **numerieke waarde** voorspelt met linear regression.
De kern is altijd dezelfde:
- je kiest een modelvorm (bv. rechte lijn)
- je bepaalt hoe fout voorspellingen zijn (loss)
- je zoekt parameters die die fout minimaliseren
- je evalueert met objectieve metrics

Linear regression is dus tegelijk:
- een wiskundig model (`y_hat = a*x + b`)
- een optimalisatieprobleem (loss minimaliseren)
- een praktische workflow in tools zoals scikit-learn en Keras

## 2) Data en probleemtype

Voor je begint, moet je weten wat elk onderdeel van je dataset betekent:
- `example` = 1 rij
- `feature` = inputkolom
- `target` = output die je wil voorspellen

Daarna kies je het juiste probleemtype:
- **classification**: categorie voorspellen
- **regression**: getal voorspellen

Deze les focust op **regression** met een (ongeveer) lineair verband.

## 3) Lineair model en interpretatie

Bij simple linear regression gebruik je:
- `y_hat = a*x + b`
- `a` = slope (helling)
- `b` = intercept (snijpunt met y-as)

Interpretatie:
- als `a` positief is, stijgt `y` als `x` stijgt
- als `a` negatief is, daalt `y` als `x` stijgt
- `b` is de voorspelde waarde van `y` wanneer `x = 0`

Met meerdere features wordt dat:
- `y_hat = a0 + a1*x1 + a2*x2 + ...`
- dit kan je zien als een dot product + bias: `y_hat = w . x + b`

## 4) Fout meten: loss function

Een model is goed als de afwijking tussen echt en voorspeld klein is.

Belangrijke losses/metrics:
- `SSE`: som van gekwadrateerde fouten
- `MSE`: gemiddelde gekwadrateerde fout (`SSE / n`)
- `MAE`: gemiddelde absolute fout
- `RMSE`: wortel van MSE (zelfde eenheid als target)

Waarom vaak kwadrateren?
- positieve en negatieve fouten heffen elkaar niet op
- grote fouten tellen extra zwaar mee
- afgeleiden zijn wiskundig handig voor optimalisatie

## 5) Afgeleide, gradient en optimalisatie

De afgeleide/gradient zegt:
- in welke richting de fout stijgt of daalt
- hoe sterk die verandering is

Bij een minimum van de loss is de gradient (ongeveer) nul.

In 1D/2D denk je aan helling van een lijn.
In meerdere dimensies is gradient de generalisatie daarvan (richting van sterkste stijging).

## 6) Twee manieren om parameters te vinden

### OLS (exact)
- Ordinary Least Squares geeft bij lineaire regressie een directe, exacte oplossing.
- `LinearRegression` in scikit-learn gebruikt standaard OLS.

### Gradient Descent (iteratief)
- start met random parameters
- bereken voorspelling en fout
- update parameters in de richting die loss verlaagt
- herhaal tot convergentie

Belangrijke hyperparameters:
- `learning rate` (stapgrootte)
- `epochs` (hoeveel volledige passes over data)
- `batch size` (hoeveel datapunten per update)

Te onthouden:
- te grote learning rate -> overshoot/divergentie
- te kleine learning rate -> traag leren

## 7) SGD en mini-batch

Varianten van gradient descent:
- **batch GD**: update met alle datapunten tegelijk
- **SGD**: update met 1 datapunt per stap
- **mini-batch GD**: update met kleine groep datapunten

Mini-batch is meestal een praktisch compromis:
- stabieler dan pure SGD
- sneller en lichter dan volledige batch op grote datasets

## 8) Evaluatie van regressiemodellen

Gebruik meerdere metrics samen:
- `MAE`: robuuster tegen outliers, makkelijk interpreteerbaar
- `MSE`: straft grote fouten extra
- `RMSE`: interpretatie in target-eenheid
- `R2`: verklaarde variantie (dichter bij 1 is doorgaans beter)
- `R`: correlatiecoefficient (tussen -1 en 1)

Belangrijke waarschuwing:
- **correlatie is geen causaliteit**

## 9) Schalen en normaliseren

Bij gradient descent kunnen grote feature-waarden numerieke problemen geven (bv. overflow).
Daarom pas je vaak preprocessing toe:
- min-max scaling
- standardization (z-score)

Effect:
- stabielere updates
- vaak snellere convergentie

## 10) Scikit-learn vs Keras in deze les

### Scikit-learn
- snel, compact, ideaal voor klassieke (shallow) ML
- standaardpatroon: `fit()` -> `predict()` -> metrics
- lineaire regressie via OLS

### Keras
- deep-learning API bovenop TensorFlow
- model in lagen opbouwen (`Sequential`, `Dense`)
- compileer met optimizer/loss (bv. `SGD` + `MSE`)
- train met `model.fit(...)`

Voor linear regression kan Keras dit ook leren, maar dan via iteratieve optimalisatie.

## 11) Grid Search in context

Na het kiezen van een model wil je goede hyperparameters vinden.
`Grid Search` test systematisch alle combinaties uit een opgegeven rooster en kiest de best scorende combinatie (meestal via validatie/CV).

Kort:
- handmatig gokken -> onbetrouwbaar
- grid search -> systematisch en reproduceerbaar

## 12) Les in 6 stappen (praktische workflow)

1. Definieer probleem: regression met numerieke target.
2. Kies features en target, check data.
3. Kies model (scikit-learn OLS of Keras + GD/SGD).
4. Kies loss/optimizer en hyperparameters.
5. Train model en evalueer met MAE/MSE/RMSE/R2.
6. Verbeter via scaling, hyperparameter tuning (bv. Grid Search).

## 13) Wat je zeker moet kennen voor het examen

- verschil tussen regression en classification
- betekenis van slope en intercept
- verschil tussen parameter en hyperparameter
- rol van loss function, afgeleide en gradient
- verschil tussen OLS en gradient descent
- invloed van learning rate, epochs en batch size
- betekenis van MAE, MSE, RMSE, R2 en R
- waarom feature scaling belangrijk is bij gradient descent
- waarom correlatie niet gelijk is aan causaliteit

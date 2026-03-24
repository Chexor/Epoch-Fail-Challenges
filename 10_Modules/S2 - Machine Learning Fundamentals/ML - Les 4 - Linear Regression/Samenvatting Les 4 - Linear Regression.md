# Samenvatting Les 4 - Linear Regression

## Gebruikte concepten (WikiLinks)

- [[Data, Example, Feature, Target]]
- [[Supervised vs Unsupervised vs Reinforcement Learning]]
- [[Classification vs Regression]]
- [[Linear Regression]]
- [[Slope en Intercept]]
- [[Dot Product]]
- [[Loss Function]]
- [[SSE (Sum of Squared Errors)]]
- [[MSE (Mean Squared Error)]]
- [[MAE (Mean Absolute Error)]]
- [[RMSE (Root Mean Squared Error)]]
- [[Derivative (Afgeleide)]]
- [[Gradient]]
- [[OLS (Ordinary Least Squares)]]
- [[Gradient Descent]]
- [[SGD (Stochastic Gradient Descent)]]
- [[Mini-batch Gradient Descent]]
- [[Learning Rate]]
- [[Epoch]]
- [[Parameters vs Hyperparameters]]
- [[R2 en R]]
- [[Feature Scaling en Normalization]]
- [[Scikit-learn]]
- [[Keras]]
- [[Sequential Neural Net]]
- [[Grid Search]]

## 1) Grote plaatje

In deze les leer je hoe je een numerieke waarde voorspelt met linear regression.
De kern is:
- model kiezen
- fout meten met een loss function
- parameters optimaliseren
- model evalueren met metrics

Linear regression is tegelijk een formule, een optimalisatieprobleem en een praktische workflow in Python.

## 2) Data en probleemtype

Belangrijke termen:
- `data`: volledige tabel
- `example` (sample): een rij
- `feature`: inputkolom
- `target`: output die je wil voorspellen

Probleemtypes:
- `classification`: categorie voorspellen
- `regression`: getal voorspellen

Deze les focust op regression.

## 3) Lineair model

Simple linear regression:
- `y_hat = a*x + b`
- `a` = slope (helling)
- `b` = intercept (snijpunt met y-as)

Meerdere features:
- `y_hat = a0 + a1*x1 + a2*x2 + ...`
- ook te schrijven als `y_hat = w . x + b` (dot product + bias)

## 4) Loss function en fouten

Doel: afwijking tussen echt (`y`) en voorspeld (`y_hat`) zo klein mogelijk maken.

Belangrijk:
- `SSE = sum((y_i - y_hat_i)^2)`
- `MSE = (1/n) * sum((y_i - y_hat_i)^2)`
- `MAE = (1/n) * sum(|y_i - y_hat_i|)`
- `RMSE = sqrt(MSE)`

Waarom kwadraten vaak gebruikt worden:
- plus/min fouten heffen elkaar niet op
- grote fouten worden zwaarder bestraft

## 5) Afgeleide en gradient

De afgeleide (derivative) geeft de lokale helling.
De gradient is de uitbreiding daarvan in meerdere dimensies.

Betekenis:
- richting: stijgt of daalt de fout?
- grootte: hoe sterk verandert de fout?

Bij een minimum is de gradient ongeveer 0.

## 6) Parameters optimaliseren

### OLS (Ordinary Least Squares)
- exacte, analytische oplossing voor lineaire regressie
- gebruikt in `scikit-learn` `LinearRegression`

### Gradient Descent (iteratief)
- start random
- update parameters om loss te verlagen
- herhaal tot convergentie

Belangrijke hyperparameters:
- `learning rate`
- `epochs`
- `batch size`

## 7) SGD en mini-batch

Varianten:
- batch GD: volledige dataset per update
- SGD: 1 datapunt per update
- mini-batch GD: kleine groep per update

Mini-batch is vaak het beste compromis tussen snelheid en stabiliteit.

## 8) Evaluatiemetrics

Gebruik meerdere metrics samen:
- `MAE`: goed interpreteerbaar, minder gevoelig voor outliers
- `MSE`: straft grote fouten extra
- `RMSE`: zelfde eenheid als target
- `R2`: verklaarde variantie (dichter bij 1 is meestal beter)
- `R`: correlatiecoefficient (-1 tot 1)

Let op: correlatie is geen causaliteit.

## 9) Feature scaling en normalization

Bij gradient descent kunnen grote waarden instabiliteit geven (bv. overflow).
Daarom schaal je features vaak vooraf.

Technieken:
- min-max scaling: `(x - min(x)) / (max(x) - min(x))`
- standardization: `(x - mean(x)) / std(x)`

Effect:
- stabielere training
- vaak snellere convergentie

## 10) Tools: scikit-learn en Keras

`Scikit-learn`:
- klassiek ML
- snel: `fit()` en `predict()`
- lineaire regressie via OLS

`Keras`:
- high-level API op TensorFlow
- model in lagen (`Sequential`, `Dense`)
- training via optimizer (bv. SGD) en loss (bv. MSE)

## 11) Grid Search in context

`Grid Search` test systematisch combinaties van hyperparameters en kiest de beste op basis van validatie/CV.

Voorbeeld:
- `alpha = [0.1, 1, 10]`
- `degree = [1, 2]`
- totaal `3 x 2 = 6` combinaties

## 12) Praktische workflow (6 stappen)

1. Definieer regressionprobleem en target.
2. Kies features en bereid data voor.
3. Kies model (OLS of GD/SGD).
4. Kies loss en hyperparameters.
5. Train en evalueer met MAE/MSE/RMSE/R2.
6. Verbeter met scaling en tuning (bv. Grid Search).

## 13) Examengerichte checklist

- verschil classification vs regression
- interpretatie van slope en intercept
- verschil parameter vs hyperparameter
- rol van loss, derivative en gradient
- OLS vs gradient descent
- impact van learning rate, epochs, batch size
- betekenis van MAE, MSE, RMSE, R2 en R
- belang van scaling bij gradient descent
- correlatie is niet causaliteit

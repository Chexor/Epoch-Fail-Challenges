---
type: lesnotitie
vak: Machine Learning Fundamentals
les: "6"
datum: 2026-03-25
docent: Andy Louwyck
status: actief
parent: "[[10_Modules/S2 - Machine Learning Fundamentals/00_Module_Overzicht|Machine Learning Fundamentals]]"
related: []
---

# Machine Learning Fundamentals - Les 6
#machine-learning-fundamentals #lesnotitie

## Lescontext
- **Thema:** Linear Classification en Support Vector Machines
- **Presentaties**:
	- [[Machine_Learning_Fundamentals_Linear_Classification.pdf]]
	- [[Machine_Learning_Support_Vector_Machines.pdf]]
- **Bronnen:**
	- [[Linear Classification en SVM|Map - Linear Classification en SVM]]
	- [[Binary Classification en Neural Basics|Map - Binary Classification en Neural Basics]]
	- [[Logistic Regression]]
	- [[Perceptron]]
	- [[Support Vector Machine]]
	- [[Kernel Trick]]

## Snelle capture

### Doelen van deze les
- [[Exploratory Data Analysis (EDA)|EDA]] op `thermostat.csv`

### Live notities
- Balanced dataset: ongeveer `50%` en `50%` per klasse.
- `C`-value (SVM):
	- Grote `C` = narrow street (smallere marge, strenger op fouten).
	- Kleine `C` = wide street (bredere marge, meer tolerantie).
- Examen:
	- Focus op SVM-classification.
	- Wiskundeformules worden niet gevraagd.
	- Algoritmes en concepten begrijpen is de kern.


### Kernbegrippen
- [[Linear Classification]]
- [[Exploratory Data Analysis (EDA)|EDA]]
- [[Scatter Plot]]
- [[Logistic Regression]]
- [[Perceptron]]
- [[Neural Network|Neural Net]]
- [[Activation Functions]]
	- [[Step Function]]
	- [[Sigmoid Function]]
- [[Loss Function]]
	- [[Binary Cross-entropy|Binary Crossentropy (minus logarithm)]]
	- [[Perceptron Loss]]
	- [[Hinge Loss]]
- [[SGD (Stochastic Gradient Descent)|Stochastic Gradient Descent]]
- Gauss curve (Bell curve)
- [[Multinomial Classification]]
	- [[One vs Rest]]

- [[Support Vector Machine|Support Vector Machines]]
	- [[Support Vectors]]
	- [[Hard Margin Classification]]
	- [[Soft Margin Classification]]
	- [[Polynomial Kernel]]
	- [[Kernel Trick]]
	- [[Gaussian RBF Kernel]]
	- C-Value 

- Terms:
	- Features
	- [[Sentiment]]
	- [[Threshold]]
	- Slope
	- Intercept
	- [[Regularization]] ("penalty")
	- [[Accuracy]]
	- [[Model Training]]
	- [[Model Fitting]] (overfitting & underfitting)
	- [[Grid Search]]
	- Hyperparameters
	- [[Validation]]
		- [[Cross-Validation]]
	- [[Computational Complexity]] (Big O)
		- Time complexity
		- Computational Complexity
	- Regression
### Voorbeelden en demo's
- 

### Vragen tijdens de les
- [ ]

### Acties / taken
- [ ]

---

## Uitwerking na de les

### 1. Groot plaatje
- Deze les gaat over **classificatie**: van data-analyse naar een model dat labels voorspelt.
- We bouwen de lijn op van eenvoudige lineaire beslissers (Logistic Regression, Perceptron) naar **Support Vector Machines (SVM)**.
- Kernvraag: hoe kiezen we een beslissingsgrens die goed generaliseert op nieuwe data?

### 2. Intuitie
- Start met [[Exploratory Data Analysis (EDA)|EDA]] en een [[Scatter Plot]] om te zien of klassen visueel scheidbaar zijn.
- Een classifier zoekt een **grens** (lijn/vlak) die punten in verschillende klassen splitst.
- Bij SVM willen we niet zomaar een grens, maar een grens met **maximale marge**: zoveel mogelijk ruimte tussen beide klassen.
- De moeilijkste punten dicht bij de grens zijn de [[Support Vectors]]; die bepalen het model het meest.
- `C` regelt de trade-off: **grote C** = strenger op fouten (smallere marge), **kleine C** = meer tolerantie (bredere marge).

### 3. Formele structuur
- [[Linear Classification]]: predictie van een discrete klasse op basis van features.
- [[Logistic Regression]]: lineair model + [[Sigmoid Function]] voor kans op klasse 1; beslissing via [[Threshold]].
- [[Perceptron]]: lineaire classifier met [[Step Function]] en update via foutgestuurde regel.
- Verliesfuncties:
  - [[Binary Crossentropy]] voor probabilistische binaire classificatie.
  - [[Perceptron Loss]] voor perceptron-leren.
  - [[Hinge Loss]] als standaard bij SVM.
- Optimalisatie: [[SGD (Stochastic Gradient Descent)|SGD]] tijdens [[Model Training]] en evaluatie via [[Validation]] / [[Cross-Validation]].
- SVM-varianten:
  - [[Hard Margin Classification]]: enkel bij perfect lineair scheidbare data.
  - [[Soft Margin Classification]]: laat enkele fouten toe via regularisatie (`C`).
- Niet-lineaire grenzen via [[Kernel Trick]], bv. [[Polynomial Kernel]] en [[Gaussian RBF Kernel]].
- Multi-class aanpak via [[Multinomial Classification]], vaak [[One vs Rest]].

### 4. Toepassing
- Demo op `thermostat.csv` met eerst EDA en vervolgens classificatiemodellen.
- Praktische workflow:
  1. Data verkennen (balans van klassen controleren).
  2. Model kiezen (Logistic Regression of SVM).
  3. Hyperparameters kiezen (`C`, kernel, threshold waar relevant).
  4. Trainen en valideren.
  5. Resultaat interpreteren met [[Accuracy]] en foutgedrag.
- Bij sentiment-achtige taken ([[Sentiment]]) is lineaire classificatie vaak een sterke baseline.

### 5. Examenfocus
- **Te kennen:**
- Verschil tussen Logistic Regression, Perceptron en SVM op conceptniveau.
- Betekenis van marge, support vectors, hard vs soft margin en impact van `C`.
- Waarom en wanneer je kernels gebruikt (Polynomial vs RBF intuïtief).
- Basisworkflow: training, validatie, modelkeuze en evaluatie.
- **Typische valkuilen:**
- `C` verkeerd interpreteren (grote C = smallere marge, niet omgekeerd).
- Denken dat hard margin altijd beter is.
- Formules uit het hoofd willen leren i.p.v. het algoritmisch gedrag te begrijpen.
- **Mogelijke examenvraag:**
- "Je hebt binaire data met lichte overlap. Kies tussen Logistic Regression en SVM, motiveer je keuze, en leg uit wat er verandert als je `C` verhoogt of verlaagt."

## Links
- **Module:** [[10_Modules/S2 - Machine Learning Fundamentals/00_Module_Overzicht|Machine Learning Fundamentals]]
- **Leslog:**
- **Samenvatting:** Les 6 bouwt classificatie op van EDA en lineaire grenzen (Logistic Regression, Perceptron) naar SVM met marge-optimalisatie, `C`-trade-off en kernels voor niet-lineaire scheidingen.
- **Oefeningen:**
- **Concepten:**
  - [[Exploratory Data Analysis (EDA)]]
  - [[Linear Classification]]
  - [[Scatter Plot]]
  - [[Linear Regression]]
  - [[Logistic Regression]]
  - [[Perceptron]]
  - [[Neural Network]]
  - [[Activation Functions]]
  - [[Step Function]]
  - [[Sigmoid Function]]
  - [[Loss Function]]
  - [[Binary Crossentropy]]
  - [[Perceptron Loss]]
  - [[SGD (Stochastic Gradient Descent)]]
  - [[Hinge Loss]]
  - [[Support Vector Machine]]
  - [[Support Vectors]]
  - [[Hard Margin Classification]]
  - [[Soft Margin Classification]]
  - [[Threshold]]
  - [[Model Training]]
  - [[Model Fitting]]
  - [[Sentiment]]
  - [[Regularization]]
  - [[Accuracy]]
  - [[Validation]]
  - [[Cross-Validation]]
  - [[Computational Complexity]]
  - [[Kernel Trick]]
  - [[Polynomial Kernel]]
  - [[Gaussian RBF Kernel]]
  - [[Multinomial Classification]]
  - [[One vs Rest]]
  - [[Slope]]
  - [[Intercept]]
  - [[Scaling]]

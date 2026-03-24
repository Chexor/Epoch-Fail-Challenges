# Samenvatting Topic 8: Intro to ML in Python (Geactualiseerd)

Dit topic behandelt de praktische implementatie van Machine Learning met behulp van het Python-ecosysteem. Het slaat de brug tussen theorie en code.

## 1. Het Kernprobleem (Big Picture)
Machine Learning in de praktijk vereist een robuuste "pipeline": van ruwe data naar een getraind model dat voorspellingen kan doen op nieuwe, ongeziene data. Het probleem is hoe we data efficiënt kunnen verwerken en standaard algoritmen kunnen toepassen zonder alles vanaf nul te hoeven programmeren.

## 2. De Intuïtie (De Python Stack)
Zie Python als een complete werkplaats:
- **NumPy**: De fundering (snelle berekeningen met getallenreeksen).
- **Pandas**: De administratie (data in tabellen/DataFrames laden en opschonen).
- **Matplotlib**: De visualisatie (grafieken en scatterplots maken).
- **Scikit-Learn**: De gereedschapskist (kant-en-klare ML algoritmen).
- **Keras/TensorFlow**: De zware machines (voor Deep Learning en neurale netwerken).

## 3. Formele Structuur: De Workflow

### A. Klassieke ML (Scikit-Learn)
De workflow voor algoritmen zoals Lineaire Regressie en K-Nearest Neighbors (KNN):
1.  **Data Laden**: Gebruik `pd.read_csv()` of `pd.read_excel()`.
2.  **Preprocessing**: Features ($X$) en Labels ($y$) scheiden. Strings omzetten naar getallen (bijv. 'm'/'v' naar 0/1).
3.  **Model Keuze**: `model = LinearRegression()` of `KNeighborsClassifier(n_neighbors=K)`.
4.  **Fit**: `model.fit(X, y)` - Het model leert van de data.
5.  **Predict**: `model.predict(X_new)` - Voorspel labels voor nieuwe data.
6.  **Score**: `model.score(X, y)` - Hoe goed presteert het model (R² of Accuracy).

### B. Deep Learning (Keras)
Voor complexere taken zoals beeldherkenning (MNIST dataset):
1.  **Netwerk Bouwen**: Een `Sequential` model met lagen (`Dense`, `Conv2D`).
2.  **Compileren**: Kies een loss-functie en optimizer.
3.  **Trainen**: `model.fit()` over meerdere *epochs*.
4.  **Evaluatie**: Testen op een aparte testset om overfitting te controleren.

## 4. Praktische Toepassingen uit de Notebooks
- **Lineaire Regressie**: Voorspellen van de leeftijd van een partner of de hoogte van verzekeringsclaims.
- **KNN (Classificatie)**: Voorspellen van geslacht op basis van lengte/gewicht of aankoopgedrag op basis van leeftijd/loon.
- **K-Means (Clustering)**: Automatisch groepen ontdekken in ongelabelde data.
- **Convnets (CNN)**: Herkennen van handgeschreven cijfers met extreem hoge nauwkeurigheid (>99%).

## 5. Examengerichte Focus
- **Supervised vs Unsupervised**: Begrijp waarom K-Means geen labels ($y$) nodig heeft bij `fit()`, maar KNN wel.
- **Feature Scaling**: Waarom we pixelwaarden herschalen naar 0-1 (normalisatie).
- **Overfitting**: Het verschil tussen prestaties op de trainingsset vs. de testset.
- **K-Hyperparameter**: Wat is de invloed van de waarde van $K$ in KNN en K-Means?

---
*Deze samenvatting is gebaseerd op de interactieve notebooks en slides van Topic 8.*

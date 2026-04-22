# Trashball Exercise - Notebook Outline

## 1) Title & Objective
- Korte challengebeschrijving
- Doelvariabele en succescriteria
- Wat we vergelijken: **Logistic Regression vs KNN**

## 2) Setup & Imports
- `pandas`, `numpy`, `matplotlib`, `seaborn`
- `sklearn` voor preprocessing, modellen, metrics en pipeline

## 3) Data Loading & First Look
- Dataset inladen
- Shape, `head()`, datatypes, missing values check
- Korte eerste observaties

## 4) EDA (Exploratory Data Analysis)
- Target class balance
- Univariate analyse (histogram/boxplot)
- Correlatie-overzicht (heatmap)
- Eventuele outliers of opvallende patronen noteren

## 5) Data Preparation
- Train/test split (stratified)
- Preprocessing pipeline opzetten
- Features schalen (belangrijk voor KNN en nuttig voor LR)

## 6) Baseline Model: Logistic Regression
- Logistic Regression pipeline trainen
- `predict()` en `predict_proba()` uitvoeren
- Eerste baseline scores rapporteren (bv. accuracy en F1)

## 7) Logistic Regression - Feature Importance
- Coefficients extraheren en op absolute waarde rangschikken
- Top features visualiseren
- Kort interpreteren welke features bijdragen aan de klassen

## 8) Evaluation Metrics (Logistic Regression)
- Confusion Matrix
- Classification Report (precision, recall, F1)
- ROC Curve + AUC
- Korte interpretatie van de trade-offs

## 9) KNN Model
- KNN pipeline trainen (met scaling)
- Starten met default `k`
- Kleine tuning van `k` (bv. 1-25)
- Beste `k` kiezen op een duidelijke metric (bv. F1 of ROC-AUC)

## 10) Evaluation Metrics (KNN)
- Confusion Matrix
- Classification Report
- ROC Curve + AUC
- Zelfde testset gebruiken als LR voor eerlijke vergelijking

## 11) Model Comparison & Final Choice
- Vergelijkingstabel: Accuracy, Precision, Recall, F1, AUC
- Final model kiezen met korte motivatie

## 12) Conclusion & Next Steps
- Samenvatting in 3-5 kernpunten
- Volgende verbeterstappen:
  - feature engineering
  - hyperparameter tuning
  - cross-validation
  - threshold tuning

---
type: lesnotitie
vak: Machine Learning Fundamentals
vakafkorting: ML
les: "7"
thema: KNN en Classification Evaluation Metrics
datum: 2026-04-01
docent: Andy Louwyck
status: actief
parent: "[[10_Modules/S2 - Machine Learning Fundamentals/00_Module_Overzicht|Machine Learning Fundamentals]]"
related: []
---

# ML-Les7-KNN en Classification Evaluation Metrics
#machine-learning-fundamentals #lesnotitie

> Naamgeving:
> - Lesfolder: `ML - Les 7 - KNN en Classification Evaluation Metrics`
> - Lesnotitie: `ML-Les7-KNN en Classification Evaluation Metrics.md`
> - Deze naamgeving volgt `99_Meta/03_Content/Vault Content Conventions.md`.

## Lescontext
- **Thema**: KNN en classification evaluation metrics
- **Presentaties:**
- **Bronnen:**
  - Pre-class teacher's announcement (Andy Louwyck)
  - Lokaal: H60.11
  - Startuur: 13:00
  - Lesactiviteit: trashball met gezamenlijk opgebouwde dataset
  - Verplichte individuele opdracht: toelichting in de les (15% van eindcijfer)

## Kernbegrippen
- Confusion Matrix
- Precision vs Recall
- F-scores (`F_1` en `F_\beta`)

## Lesnotities

### Classification evaluation metric: Accuracy

$$
\mathrm{accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
$$

- `TP` = True Positive
- `TN` = True Negative
- `FP` = False Positive
- `FN` = False Negative

### Wanneer Precision vs Recall?

- **Kies Precision** wanneer `False Positives (FP)` duur of schadelijk zijn.
  - Voorbeeld: spamfilter voor belangrijke mailboxen (je wil zo weinig mogelijk legitieme mails als spam markeren).
- **Kies Recall** wanneer `False Negatives (FN)` duur of risicovol zijn.
  - Voorbeeld: medische screening (je wil zo weinig mogelijk zieke patiënten missen).

### Threshold (beslissingsdrempel)

- **Threshold** is de grenswaarde waarop een modelscore/probability wordt omgezet naar een klasse.
  - Bijv. als `p(y=1|x) >= threshold`, dan voorspel je klasse `1`; anders klasse `0`.
- **Increasing threshold** (hoger zetten):
  - model wordt strenger om een positieve klasse te voorspellen
  - meestal minder `FP`, maar meer `FN`
  - vaak hogere Precision en lagere Recall
- **Decreasing threshold** (lager zetten):
  - model wordt sneller geneigd om positieve klasse te voorspellen
  - meestal meer `FP`, maar minder `FN`
  - vaak lagere Precision en hogere Recall

### Sensitivity en Specificity

- `Sensitivity` (ook `Recall` of `TPR`) meet hoeveel echte positieven je correct vindt.

$$
\mathrm{Sensitivity} = \frac{TP}{TP + FN}
$$

- `Specificity` (ook `TNR`) meet hoeveel echte negatieven je correct als negatief classificeert.

$$
\mathrm{Specificity} = \frac{TN}{TN + FP}
$$

- Intuitie:
  - hoge `Sensitivity` = weinig gemiste positieven (`FN` laag)
  - hoge `Specificity` = weinig valse alarmen (`FP` laag)

### FPR en TPR

- `TPR` (**True Positive Rate**) = aandeel echte positieven dat correct als positief wordt voorspeld.

$$
\mathrm{TPR} = \frac{TP}{TP + FN}
$$

- `FPR` (**False Positive Rate**) = aandeel echte negatieven dat fout als positief wordt voorspeld.

$$
\mathrm{FPR} = \frac{FP}{FP + TN}
$$

- Intuitie:
  - hoge `TPR` is goed (we vinden veel echte positieven)
  - lage `FPR` is goed (we maken weinig valse alarmen)

### AUC (Area Under the Curve)

- `AUC` is de **oppervlakte onder de ROC-curve**.
- De ROC-curve toont `TPR` (y-as) tegenover `FPR` (x-as) voor verschillende threshold-waarden.
- Interpretatie:
  - `AUC = 1.0`: perfecte classificatie
  - `AUC = 0.5`: niet beter dan random gokken
  - hoe hoger de `AUC`, hoe beter het model positieven en negatieven kan onderscheiden
- Praktisch: `AUC` is nuttig omdat ze modelprestatie samenvat over **alle thresholds**, niet enkel op 1 gekozen threshold.

### AUC classifier-types (intuitie)

- **Perfect Classifier**:
  - rangschikt alle positieven boven alle negatieven
  - ROC-curve gaat via linksboven (`TPR = 1`, `FPR = 0`)
  - `AUC = 1.0`
- **Random Classifier**:
  - geen onderscheidingskracht (zoals munt opgooien)
  - ROC-curve ligt rond de diagonaal `y = x`
  - `AUC = 0.5`
- **Inverse Classifier**:
  - model rangschikt systematisch verkeerd (negatieven boven positieven)
  - ROC-curve ligt onder de diagonaal
  - `AUC < 0.5` (in extreem geval `AUC = 0.0`)
  - praktisch: als je voorspellingen omdraait, kan je vaak een sterke classifier krijgen

### Scikit-Learn modules in deze context

- In deze lescontext gebruiken we verschillende onderdelen van `scikit-learn` voor classificatie en evaluatie.
- Typische opdeling:
  - `sklearn.neighbors` voor `KNN`
  - `sklearn.metrics` voor confusion matrix, precision/recall, F-scores, ROC, AUC en `classification_report`
  - `sklearn.model_selection` voor train/test split en evaluatieworkflow

### Lazy Learning vs Eager Learning

- **Lazy Learning**:
  - model leert geen expliciete globale functie tijdens training
  - in de praktijk is dit bijna "geen training": vooral data opslaan/indexeren
  - bewaart vooral trainingsdata en beslist pas bij predictie
  - voorbeeld: `KNN`
  - typisch: snelle "training", tragere predictie
- **Eager Learning**:
  - model leert wel een expliciet patroon/functie tijdens training
  - gebruikt dat getrainde model nadien voor predicties
  - voorbeelden: logistic regression, decision trees, neural networks
  - typisch: tragere training, snellere predictie

### K-value als hyperparameter in KNN

- De `K-value` is het aantal dichtste buren (`nearest neighbors`) dat KNN gebruikt om een voorspelling te maken.
- `K` is een **hyperparameter**: je kiest die vooraf, het model leert die niet zelf.
- Effect van de keuze:
  - kleine `K` -> gevoeliger aan ruis/outliers (hogere variantie)
  - grote `K` -> gladdere beslissing, maar risico op underfitting (hogere bias)

### Distance metrics in KNN

- KNN bepaalt "dichtste buren" via een afstandsmaat (`distance metric`).

- **Euclidean distance** (hemelsbrede afstand):

$$
d(\mathbf{x},\mathbf{y}) = \sqrt{\sum_{i=1}^{n}(x_i - y_i)^2}
$$

  - Intuitie: rechte lijn tussen twee punten.
  - Gebaseerd op de stelling van Pythagoras.
  - Vaak gebruikt wanneer features continu zijn en op vergelijkbare schaal staan.

- **Manhattan distance** (stadsblokafstand):

$$
d(\mathbf{x},\mathbf{y}) = \sum_{i=1}^{n}|x_i - y_i|
$$

  - Intuitie: je beweegt horizontaal/verticaal zoals straten in een raster.
  - Vaak robuuster voor outliers dan Euclidean en nuttig in hoge dimensies of sparse data.

### L1-norm en L2-norm (in deze context)

- Een **norm** meet de grootte van een vector (of het verschil tussen twee punten).
- In KNN gebruik je normen om afstanden te definiëren tussen datapoints.

- `L1`-norm:

$$
\|\mathbf{x} - \mathbf{y}\|_1 = \sum_{i=1}^{n}|x_i - y_i|
$$

  - Dit komt overeen met **Manhattan distance**.

- `L2`-norm:

$$
\|\mathbf{x} - \mathbf{y}\|_2 = \sqrt{\sum_{i=1}^{n}(x_i - y_i)^2}
$$

  - Dit komt overeen met **Euclidean distance**.

- Persoonlijke nota: hier nog verder in verdiepen tot het verschil en de intuitie volledig helder zijn.

### 4.1 Losse notities (ruwe capture)
- **Overgang:** start deel 2 van de les: `K Nearest Neighbor (KNN)`.

- Wat zijn de gevolgen van een **imbalanced dataset** vergelijking met een **balanced set**? -> vals hoge accuracy. 
  Voorbeeld: medical dataset in slides -> 10 infected vs. 990 not infected
  ```python
  def isInfected(patient)
	  return false # => 99% accuracy guaranteed
  ```

- Which type of errors do we allow/prefer (FP or FN)?
	- -> confusion matrix


### 4.2 Concepts (te valideren)
- False positive (FP) & False negatives (FN)
- Confusion Matrix
- Precision vs Recall
- Arithmetic mean vs Harmonic mean
- F_1 score
- F_beta score
- Sensitivity vs Specificity
- ROC curve

## Exameninfo
- 

## Oefeningen (tijdens de les)
- [ ]

## Opdrachten (om thuis af te werken)
- [ ]

---

## Verwerking na de les
- [ ] Lesnotities opschonen en structureren
- [ ] Kernbegrippen linken aan bestaande conceptnotes
- [ ] Nieuwe conceptnotes aanmaken waar nodig
- [ ] Relevante info routeren naar module- of conceptniveau
- [ ] Oefeningen en opdrachten finaliseren met status

## Links
- **Module:** [[10_Modules/S2 - Machine Learning Fundamentals/00_Module_Overzicht|Machine Learning Fundamentals]]
- **Leslog:**
- **Samenvatting:**
- **Oefeningen:**
- **Concepten:**

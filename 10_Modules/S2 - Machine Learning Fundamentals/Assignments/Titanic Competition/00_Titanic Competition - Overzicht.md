# Titanic Competition - Assignment Hub
#lesnotitie

This folder collects all files for the individual Kaggle assignment: Titanic - Machine Learning from Disaster.

## Required Assignment Constraints
- Clean the data and perform EDA.
- Use the full 6-step EDA workflow from class (mandatory).
- Use shallow learning models, with a focus on ensemble methods.
- Do not use deep learning models (no neural networks).
- Write all code in Python using Scikit-Learn and related packages.
- Clearly mention all sources and AI tools used.
- Keep all deliverables in English.

## EDA: 6-Step Structure (Mandatory)
1. Define objective and target variable.
2. Inspect data structure and quality (`shape`, `dtypes`, missing values, duplicates).
3. Clean data (imputation, type fixes, outlier handling where needed).
4. Univariate analysis (feature distributions and target balance).
5. Bivariate/multivariate analysis (feature-target relations, correlations, grouped comparisons).
6. Summarize key insights and translate them into modeling/preprocessing decisions.

## Preprocessing Requirements (Modeling)
- Quantitative variables: evaluate both `MinMaxScaler` and `StandardScaler`.
- Categorical variables: use encoding based on feature semantics:
  - `LabelEncoder` (target labels only, not input feature columns)
  - `OrdinalEncoder` (ordered categorical features)
  - `OneHotEncoder` (nominal categorical features)
- Combine preprocessing and model steps with `ColumnTransformer` + `Pipeline`.
- Keep train/test split and all transformations leakage-safe by fitting preprocessors on train data only (inside pipeline).

## Data Split Requirement
- The dataset must be split before modeling.
- Use a clear split strategy, e.g. `train_test_split(..., test_size=0.2, random_state=42, stratify=y)`.
- Fit preprocessing and models on the training set only.
- Use the validation/test split only for evaluation and model comparison.

## Submission Requirements
- Screenshot showing your competition score and proof of participation.
- Jupyter notebook submission (target reading time: about 15 minutes).
- A 10 to 15 minute video where you explain your solution method.
- Video and notebook links must remain permanently accessible to the course instructor.
- Deadline: Sunday, May 24 at 23:59 (midnight).

## Grading Weight
- This assignment counts for 15% of the total course points.

## Folder Structure
- `Data/` - Kaggle datasets (`train.csv`, `test.csv`) and optional processed exports.
- `Notebooks/` - experiments and final notebook(s).
- `Submissions/` - versioned `submission.csv` files.
- `Notes/` - findings, reflections, and references.

## Suggested Workflow
1. Put raw competition files in `Data/`.
2. Build EDA + preprocessing + model notebooks in `Notebooks/`.
3. Start with a baseline, then improve with ensemble models.
4. Save each Kaggle upload in `Submissions/` with a clear version name.
5. Document choices, sources, and AI assistance in `Notes/`.

## Recommended Model Candidates (Scikit-Learn)
- `RandomForestClassifier`
- `GradientBoostingClassifier`
- `AdaBoostClassifier`
- `ExtraTreesClassifier`

Optional (if installed and allowed):
- `XGBoost` / `LightGBM` as comparison models

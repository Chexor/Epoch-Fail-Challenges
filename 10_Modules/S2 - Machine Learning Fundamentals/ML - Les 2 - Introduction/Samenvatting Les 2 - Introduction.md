# Lesson 2 Summary - Introduction to Machine Learning

## Correct lesson order

1. Lesson 1: Supply-Demand Equilibrium Challenge
2. Lesson 2: Introduction
3. Lesson 3: EDA

## Core in 1 minute

- [[Artificial Intelligence]] is the broad field of systems showing intelligent behavior.
- [[Machine Learning]] is a part of AI where systems learn from data instead of fixed rules.
- [[Deep Learning]] is a part of ML that uses neural networks.
- [[Generative AI]] is a specific direction in ML focused on generating new content.
- Main goal of this lesson: understand the full ML flow from data to evaluation.

## Big picture

- AI -> ML -> DL (nested structure).
- This lesson is the foundation for the rest of the course.
- Next topics build on:
  - data understanding and preparation
  - model selection and training
  - performance evaluation

## Core concepts

### 1) Classical programming vs Machine Learning

- Classical programming: `rules + data -> output`
- Machine learning: `data + desired output -> model (rules)`
- Key idea: in ML, the rules are learned from examples.

### 2) Important terms

- `dataset`: full table of data
- `sample` / `instance`: one row (one observation)
- `feature`: input variable (column)
- `target` / `label`: output to predict

### 3) Supervised vs Unsupervised

- **Supervised learning**: with labels
  - tasks: classification, regression
- **Unsupervised learning**: without labels
  - tasks: clustering, dimensionality reduction, matrix factorization

### 4) Classification vs Regression

- **Classification**: categorical output (e.g. spam / not spam)
- **Regression**: numerical output (e.g. price, weight, temperature)

## Common algorithms (intro)

- [[K-Nearest Neighbors (KNN)]]
- [[Decision Trees]]
- [[Random Forest]]
- [[Linear Regression]]
- [[Logistic Regression]]
- [[Artificial Neural Networks]]

> There is no single best algorithm for every problem (no free lunch).

## Training and evaluation

### Training flow

1. Collect and prepare data
2. Train model on training set
3. Tune hyperparameters with validation set
4. Final check on test set
5. Deploy and monitor

### Critical distinction

- **Optimization**: fitting training data as well as possible
- **Generalization**: performing well on unseen data

### Common pitfalls

- **Underfitting**: model is too simple
- **Overfitting**: model is too specific to training data

## Loss vs Metric

- `loss`: what the algorithm minimizes during training
- `metric`: what we use to interpret model performance

Examples:
- Regression: MSE / MAE (loss), RMSE / R2 (metric)
- Classification: log loss (loss), accuracy (metric)

## Mini exam-style application

### Scenario

You want to predict whether an email is spam based on features such as:
- number of links
- number of uppercase words
- sender domain

### Question

Which learning type and task should you choose?

### Answer

- Learning type: **supervised learning** (labels are available: spam/not spam)
- Task: **classification** (output is categorical)

## Quick retrieval check

1. What is the difference between AI, ML, DL, and GenAI?
2. When do you choose classification instead of regression?
3. Why do you need a validation set in addition to a training set?
4. What is the difference between optimization and generalization?
5. How can you spot overfitting in training/validation results?

## 10-second exam checklist

- Is my target categorical or numerical?
- Do I have labels?
- Am I evaluating on unseen data?
- Is my model neither too simple nor too complex?
- Can I justify my algorithm choice?

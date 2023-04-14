# Project Name: Heart Disease Risk-Classification By Machine Learning

## Project Description:

### Heart Risk Classification By Machine Learning is a project that aims to develop a machine learning model to predict the likelihood of heart disease in individuals based on their personal characteristics. The project includes multiple Jupyter Notebook (.ipynb) files that demonstrate model testing, as well as an app that could potentially be built as an extracurricular phase to provide an interactive user platform for users to input their information or test information and watch the model predict their health. The model is designed to accurately predict true positives, which is the minority class among the dataset.

### View our findings at this link: https://gcweigenberg.github.io/Heart-Risk-Classification-/

## Installation Instructions:

### The following Python libraries are required for this project:

#### pandas
#### scikit-learn
#### imbalanced-learn
#### joblib

### You can install these libraries using the following commands in your Python environment:

#### '!pip install pandas scikit-learn imbalanced-learn joblib'

## Software:

### - VS Code (for running Jupyter Notebook files)
### - Tableau (for separate visualizations)

## Steps to get it up and running:

#### 1) Clone or download the project repository from the link provided in the project details.
#### 2) Open the Jupyter Notebook files (.ipynb) in VS Code or any other Jupyter Notebook-compatible environment.
#### 3) Click "Run All" on the Jupyter Notebook files to execute the full program and view the statistics outputs. The code contains full comments to clarify each process.
#### 4) To view project details and findings, including Tableau visualizations for the dataset and the model training information, visit the link provided in the project details. Users can click on various elements of the page to explore.

### There is no need for data input, as the project includes preprocessed data for model training and testing.

## Model Information:

### The final model used in this project is a Logistic Regression model that utilizes SMOTE (Synthetic Minority Over-sampling Technique) to deal with an imbalanced class set.

## Model Purpose:

### The purpose of the model is to predict the likelihood of heart disease in individuals based on their personal characteristics, using a machine learning approach.

## Model Training:

### The model was trained using a dataset that was preprocessed to select only relevant columns that significantly impact the chance of heart disease. Categorical features were converted to dummy indicators, and SMOTE was used to oversample the minority class. The model was evaluated using various metrics such as accuracy, precision, recall, F1-score, and confusion matrix. The best machine learning model was selected based on the evaluation results. The code for the model training process can be found in the Jupyter Notebook files provided in the project repository.
# Project Name: Heart Disease Risk-Classification By Machine Learning
Group Members: Jonathan Arp, Michael “Gabe” Cweigenberg, Jesse DeLaCruz, Dylan Kurbel, Nicolette Keplinger

## Project Description:
*Heart Risk Classification By Machine Learning* is a project that aims to develop a machine learning model to predict the likelihood of heart disease in individuals based on their personal characteristics. The project includes multiple Jupyter Notebook (.ipynb) files that demonstrate model testing, as well as the starting srchitecture of an app that could potentially be built as an extracurricular phase to provide an interactive user platform for users to input their information or test information and watch the model predict their health. Visualizations describing the dataset and results were generated through Tableau. Dashboards of these images can be found in the `images/ML_results` sub-directory, with additional individual graph images in the `images/ML_results/individual_photos` sub-directory. The model is designed to accurately predict true positives (TP) and true negatives (TN), while minimizing the number of false positives (FP) and false negatives (FN). Inherent bias of the selected dataset include uneven feature distribution as the majority of the dataset was comprised of Negative Heart Disease Diagnosis (0) individuals. Because of this, multiple models were evaluated to find and optimal ML model that had high accuracy, precision, and recall. 
### View our findings at this link: https://gcweigenberg.github.io/Heart-Risk-Classification-/

## Installation Instructions:

### The following Python libraries are required for this project:
* pandas
* scikit-learn
* imbalanced-learn
* joblib

### You can install these libraries using the following commands in your Python environment:

`!pip install pandas scikit-learn imbalanced-learn joblib`

## Software:
* VS Code (for running Jupyter Notebook files)
*Tableau (for separate visualizations)

## Steps to get it up and running:
1. Clone or download the project repository from the link provided in the project details.
2. Open the Jupyter Notebook files (.ipynb) in VS Code or any other Jupyter Notebook-compatible environment.
3. Click "Run All" on the Jupyter Notebook files to execute the full program and view the statistics outputs. The code contains full comments to clarify each process.
4. To view project details and findings, including Tableau visualizations for the dataset and the model training information, visit the link provided in the project details. Users can click on various elements of the page to explore.
### There is no need for data input, as the project includes preprocessed data for model training and testing.

## Model Information:
### We evaluated multiple ML models and hyper-parameters for the ability to predict positive and negative diagnosis of Heart Disease (links to jupyter notebooks exploring each of these can be found on the main paige): 
* Log Regression + Resampling
* Log Regression + Resampling + Hyper-parameter tuning
* Log Regression + Bootstrapping 
* Log Regression + Bootstrapping + Hyper-parameter tuning
* Log Regression + SMOTE
* Random Forests +  Hyper-parameter tuning
* Banalced Random Forests
* Banalced Random Forests + Resampling

#### The final model used in this project is a *Logistic Regression model that utilizes SMOTE* (Synthetic Minority Over-sampling Technique) to deal with an imbalanced class set. See results below for supporting information on why this was selected as our optimal model. 

## Model Purpose:

### The purpose of the model is to predict the likelihood of heart disease in individuals based on their personal characteristics, using a machine learning approach.

## Model Training:

### The model was trained using a dataset that was preprocessed to select only relevant columns that significantly impact the chance of heart disease. Categorical features were converted to dummy indicators, and SMOTE was used to oversample the minority class. The model was evaluated using various metrics such as accuracy, precision, recall, F1-score, and confusion matrix. The best machine learning model was selected based on the evaluation results. The code for the model training process can be found in the Jupyter Notebook files provided in the project repository.

## Results 
To identify the optimal final model, we compared a number of parameters includeing accuracy, precision, recall (aka sensitivity) and F1-Score:

### Accuracy
Accuracy across models predicting negative diagnosis (0) and positive diagnosis (1)
![](https://github.com/GCweigenberg/Heart-Risk-Classification-/blob/main/images/ML_resutls/individual_photos/Accuracy%20across%20Models.png)

### Precision across models predicting negative diagnosis (0) and positive diagnosis (1)

![](https://github.com/GCweigenberg/Heart-Risk-Classification-/blob/main/images/ML_resutls/individual_photos/Precision.png)

### Recall across models predicting negative diagnosis (0) and positive diagnosis (1)
![](https://github.com/GCweigenberg/Heart-Risk-Classification-/blob/main/images/ML_resutls/individual_photos/Recall.png)

### F1-Scores across models predicting negative diagnosis (0) and positive diagnosis (1)
![](https://github.com/GCweigenberg/Heart-Risk-Classification-/blob/main/images/ML_resutls/individual_photos/F1%20scores.png)

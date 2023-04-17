# Project Name: Heart Disease Risk-Classification By Machine Learning
Group Members: Jonathan Arp, Michael “Gabe” Cweigenberg, Jesse DeLaCruz, Dylan Kurbel, Nicolette Keplinger

## Project Description:
*Heart Risk Classification By Machine Learning* is a project that aims to develop a machine learning model to predict the likelihood of heart disease in individuals based on their personal characteristics. The project includes multiple Jupyter Notebook (.ipynb) files that demonstrate model testing, as well as the starting srchitecture of an app that could potentially be built as an extracurricular phase to provide an interactive user platform for users to input their information or test information and watch the model predict their health. Visualizations describing the dataset and results were generated through Tableau. Dashboards of these images can be found in the `images/ML_results` sub-directory, with additional individual graph images in the `images/ML_results/individual_photos` sub-directory. The model is designed to accurately predict true positives (TP) and true negatives (TN), while minimizing the number of false positives (FP) and false negatives (FN). Inherent bias of the selected dataset include uneven feature distribution as the majority of the dataset was comprised of true neagtive (1) disease states. Because of this, multiple models were evaluated to find and optimal ML model that had high accuracy, precision, and recall. 
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
We first looked at comparing the accuracy across all models that we evaluated. Most were ≥ 75% accurate and three even over 90%. However, even with high accuracy you can still have low precision (i.e., lots of false positives (FP)) and low sensitivity (lots of false negatives(FN)) which reduces practical utility of the ML model for many use cases. 
![](https://github.com/GCweigenberg/Heart-Risk-Classification-/blob/main/images/ML_resutls/individual_photos/Accuracy%20across%20Models.png)

### Precision
For precision, we were looking at each model’s ability for less false positive predictions (calculated by: TP/(TP+FP)). For the disease state 0 (positive for heart disease), precision was consistently high across all models meaning it didn’t have many FP predictions for heart disease. However, for disease state 1 (negative for heart disease), precision was less than 50% for almost all models. This means there were a high number of instances FP’s for most models (predicting that there was no heart disease when there was). Data suggests the best performer for both 0 and 1 disease states were the SMOTE model (third from the right).
![](https://github.com/GCweigenberg/Heart-Risk-Classification-/blob/main/images/ML_resutls/individual_photos/Precision.png)

### Recall
When assessing recall (aka sensitivity) we were looking for models with low amounts of FNs. Recall is calculated by FP/ (FP+FN). Since our data set has such a high skew of negative diagnoses, our main focus was on the reduction of False negatives (i.e., recall) to the extent that the dataset allows. You can see in this bar chart, there are only four models that had an increase of recall >75% for both disease states (0 and 1). 
![](https://github.com/GCweigenberg/Heart-Risk-Classification-/blob/main/images/ML_resutls/individual_photos/Recall.png)

### F1-Score
Due to some confounding results across metrics, we looked at F1 score to select the optimal model, which is the “harmonic means” of both precision and recall. F1 score ranges from 0 to 1, with 0 meaning both precision and recall are low and 1 meaning both precision and recall are 100%. The only clear model that sticks out for having high F1 scores (> 80%) for *BOTH* 0 and 1 disease states is the SMOTE model (Third from right). 
Given the limitations of our dataset (skewness and limited ability for feature engineering) Future directions can include trying to predict other categories/columns such as race and gender instead of the heart disease.  
![](https://github.com/GCweigenberg/Heart-Risk-Classification-/blob/main/images/ML_resutls/individual_photos/F1%20scores.png)

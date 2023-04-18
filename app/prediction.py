import joblib
import pandas as pd

# Load the model
model = joblib.load('/Users/dylan/Desktop/git/Heart-Risk-Classification-/app/logistic_regression_model.pkl')

# Load input data
input_data = {
    'question1': 10,
    'question2': 20
    # Add other input fields as needed
}

# Extract values from input_data
question1 = input_data.get('question1', '')
question2 = input_data.get('question2', '')
# Extract values from other input fields as needed

# Perform prediction using the loaded model
# Modify this part based on your actual model prediction logic
prediction = model.predict([[question1, question2]])
# Modify this part based on your actual model prediction logic

print(prediction.tolist())

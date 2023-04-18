import os
from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
app = Flask(__name__, template_folder='templates')

# Load the model
model = joblib.load('/Users/dylan/Desktop/git/Heart-Risk-Classification-/app/logistic_regression_model.pkl')

# Load the scaler
scaler = joblib.load('app/scaler.pkl')

@app.route('/') # if someone goes to webpage, i want you to run this function and i want you to give back this response
def root():
    return render_template('index.html')

#Run function below at webpage route above

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from frontend
    input_data = request.json

    # Extract values from input_data
    question1 = input_data.get('question1', '')
    question2 = input_data.get('question2', '')
    question3 = input_data.get('question3', '')
    question4 = input_data.get('question4', '')
    question5 = input_data.get('question5', '')
    question6 = input_data.get('question6', '')
    question7 = input_data.get('question7', '')
    question8 = input_data.get('question8', '')
    question9 = input_data.get('question9', '')
    question10 = input_data.get('question10', '')
    question11 = input_data.get('question11', '')
    question12 = input_data.get('question12', '')
    question13 = input_data.get('question13', '')
    question14 = input_data.get('question14', '')
    question15 = input_data.get('question15', '')

    # Extract values from other input fields as needed

    # Preprocess the input data
    input_df = pd.DataFrame({
        'question1': [question1],
        'question2': [question2],
        'question3': [question3],
        'question4': [question4],
        'question5': [question5],
        'question6': [question6],
        'question7': [question7],
        'question8': [question8],
        'question9': [question9],
        'question10': [question10],
        'question11': [question11],
        'question12': [question12],
        'question13': [question13],
        'question14': [question14],
        'question15': [question15],
        # Add columns for other input fields as needed
    })
    input_df = pd.get_dummies(input_df, drop_first=True)
    input_scaled = scaler.transform(input_df)

    # Perform prediction using the loaded model
    prediction = model.predict(input_scaled)

    # Prepare response
    response = {
        'prediction': prediction.tolist()
    }

    return response

#If name is main, run flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
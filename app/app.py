import os
from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
app = Flask(__name__, template_folder='templates')

# Load the model
model = joblib.load('/Users/dylan/Desktop/git/Heart-Risk-Classification-/app/logistic_regression_model.pkl')

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
    # Extract values from other input fields as needed

    # Perform prediction using the loaded model
    # Modify this part based on your actual model prediction logic
    prediction = model.predict([[question1, question2]])
    # Modify this part based on your actual model prediction logic

    # Prepare response
    response = {
        'prediction': prediction.tolist()
    }

    # Return JSON response
    return jsonify(response)



#If name is main, run flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
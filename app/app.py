import os
from flask import Flask, render_template, url_for, json, jsonify
import pandas as pd
app = Flask(__name__, template_folder='templates')


@app.route('/') # if someone goes to webpage, i want you to run this function and i want you to give back this response
def root():
    return render_template('index.html')

#Run function below at webpage route above
@app.route('/main')
def main():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the front-end
    input_data = request.json
    # Call your model prediction function to get predictions
    predictions = model_utils.predict(input_data)
    # Return predictions as JSON response
    return jsonify(predictions)

#If name is main, run flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
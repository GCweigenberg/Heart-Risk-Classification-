import os
from flask import Flask, render_template, url_for, json, jsonify, request
import pandas as pd
#from sklearn.externals import joblib
import joblib
import requests
import json
import urllib.parse

loaded_model = joblib.load('best_model.pkl')

app = Flask(__name__, template_folder='templates')

#preprocess function
def preprocess():
    user_data = np.array([ 0.15091147,  0.20454418, -0.49061052,  3.40998879, -0.8380497 ,
       -0.27075699, -0.19918862,  2.4975575 ,  0.95298154, -0.95298154,
       -0.2661606 , -0.23721138, -0.24941029, -0.26127751, -0.26544137,
       -0.27076586, -0.29383291, -0.32052326, -0.34322529, -0.34508172,
       -0.32886329, -0.26753216,  3.50803318, -0.1297837 , -0.1598657 ,
       -0.2780916 ,  3.27253957, -0.18751533, -1.81619011,  2.61062705,
        0.53908419, -0.5127498 ,  2.86715722, -0.6407626 , -0.19184433,
       -0.74479919, -0.39361474, -0.19541369, -0.32007225])
    ud = user_data.reshape(1,-1)
    predictions_user = loaded_model.predict(ud)

    return predictions_user

@app.route('/') # if someone goes to webpage, i want you to run this function and i want you to give back this response
def root():
    return render_template('index.html')

@app.route('/prediction') # if someone goes to webpage, i want you to run this function and i want you to give back this response
def predict():
    
    predictions = loaded_model.predict(ud)
    #call stagnant pre-processed data
    #Return prediction in json (call i.e.D3)
    return predictions

    #stagnant data
    #return predict on stagnant data

    #loaded model. predict 

    # user input 
#Run function below at webpage route above
@app.route('/main')
def mapMain():
    return render_template('mainpage.html')

#If name is main, run flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
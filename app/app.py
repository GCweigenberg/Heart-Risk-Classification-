import os
from flask import Flask, render_template, url_for, json, jsonify
import pandas as pd
app = Flask(__name__, template_folder='templates')


@app.route('/') # if someone goes to webpage, i want you to run this function and i want you to give back this response
def root():
    return render_template('index.html')

#Run function below at webpage route above
@app.route('/main')
def mapMain():
    return render_template('mainpage.html')

#If name is main, run flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
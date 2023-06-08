# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from flask import Flask
from flask import request, jsonify, render_template

from functions import review_to_tockens
import sklearn
from joblib import load
from models import models

model_path 	= "models/stack_overflow_tag_prediction.joblib"
target_path = "models/target_col.joblib"
vectors_path 	= "models/tfidf_vectorizer.joblib"
transformer_path = "models/normalize.joblib"
model = load(model_path)
target_col = load(target_path)
vectors = load(vectors_path)
transformer = load(transformer_path)



app = Flask(__name__)

# Home page
@app.route('/') 
def index():
    return render_template('index.html')


@app.route('/predictTag', methods=['POST'])
   
def predictTag():
   # return "Naima: Hello World!"
   #json_ = request.json
   #data = json_
	question 		= request.form['question']#data['question']  
	recommendation = ''
	if question is not None:
		question 		= str(question)
		#return jsonify({"prediction": question})
		question 		= review_to_tockens(question)
		question 		= vectors.transform(question)
		output 			= transformer.transform(question)
		result 			= models.prediction(model, 0.35, output, target_col)
		recommendation 	= result
	return render_template('recommendation.html', tags = recommendation)# jsonify({"prediction": question}))

if __name__ == "__main__":
    app.run(debug=True)
	#from waitress import serve
	#serve(app, host="0.0.0.0", port=8080)

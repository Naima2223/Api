import pandas as pd
import numpy as np
from flask import Flask
from flask import request, jsonify, render_template





app = Flask(__name__)

# Home page
@app.route('/') 
def index():
    return render_template('index.html')
	
	
@app.route('/predictTag', methods=['POST'])
   
def predictTag():
   return render_template('recommendation.html', tags = 'Retour test', questions='test')
	
if __name__ == "__main__":
    app.run(debug=True)	
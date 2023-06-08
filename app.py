# -*- coding: utf-8 -*-
from flask import Flask
from flask import request, jsonify, render_template
app = Flask(__name__)

# Home page
@app.route('/') 
def index():
    return render_template('index.html')


@app.route('/predictTag', methods=['POST'])
   
def predictTag():
   # return "Naima: Hello World!"
    json_ = request.json
    data = json_
    question = data['question']
    #return jsonify({"prediction": question})
	return render_template('recommendation.html', tags = jsonify({"prediction": question}))

if __name__ == "__main__":
    app.run(debug=True)

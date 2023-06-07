# -*- coding: utf-8 -*-
from flask import Flask
from flask import request, jsonify
app = Flask(__name__)

@app.route("/predict_tag")
def predict_tag():
   # return "Naima: Hello World!"
    json_ = request.json
    data = json_
    question = data['question']
    return jsonify({"prediction": question})
if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from flask import request, jsonify, render_template
app = Flask(__name__)

# Home page
@app.route('/') 
def index():
    return render_template('index.html')
	
if __name__ == "__main__":
    app.run(debug=True)	
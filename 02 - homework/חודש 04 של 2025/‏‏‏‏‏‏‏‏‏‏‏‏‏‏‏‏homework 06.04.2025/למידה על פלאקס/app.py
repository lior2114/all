from flask import Flask,jsonify
from datetime import datetime

app = Flask(__name__)
@app.route("/")
def home():
    return jsonify({"lori":"klfgd"})

@app.route("/name_of_kid")
def name_of_kid():
    return "kid"

@app.route("/api/time")
def get_time():
    return jsonify({"time": datetime.now().isoformat()})

if __name__ == '__main__': app.run(debug=True, host='0.0.0.0', port=5000)

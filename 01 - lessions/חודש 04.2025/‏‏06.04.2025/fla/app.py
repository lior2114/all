from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Flask!"})

@app.route("/details")
def get_details():
    return jsonify({"firstname":"ploni","lastname":"p"})
if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port = 5000)
    
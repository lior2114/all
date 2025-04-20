from flask import Flask, request, jsonify
import os
from city_model import CityModel
from city_controller import CityController


app = Flask(__name__)
CityController.init_db()

@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/cities', methods=['POST'])
def create_city():
    data = request.get_json()
    city = CityModel.from_dict(data)
    CityController.save(city)
    return jsonify(city.to_dict()), 201


# נתיבים נוספים: GET /cities, GET /cities/<id>, PUT, DELETE (ראה קוד בשיעור)

@app.route('/cities/country/<country_name>', methods=['GET'])
def get_cities_by_country(country_name):
    cities = CityController.get_by_country(country_name)
    return jsonify([city.to_dict() for city in cities]), 200

if __name__ == '__main__':
    app.run(debug=True)

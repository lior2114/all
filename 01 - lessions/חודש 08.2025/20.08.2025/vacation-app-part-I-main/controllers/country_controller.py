from flask import jsonify
from models.country_model import Country

class CountryController:

    @staticmethod
    def get_all_countries():
        try:
            countries = Country.get_all_countries()
            return jsonify(countries), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

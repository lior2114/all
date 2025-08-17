from flask import Blueprint
from controllers.country_controller import CountryController

country_bp = Blueprint('countries', __name__)

@country_bp.route('/countries', methods=['GET'])
def get_all_countries():
    return CountryController.get_all_countries()

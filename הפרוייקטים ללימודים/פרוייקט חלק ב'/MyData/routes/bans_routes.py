from flask import Blueprint
from controller.ban_controller import Bans_Controller as B

bans_bp = Blueprint('/bans', __name__)

@bans_bp.route('/bans/<int:user_id>', methods=['POST'])
def create_ban(user_id):
    return B.create_ban(user_id)

@bans_bp.route('/bans/<int:user_id>', methods=['GET'])
def check_ban(user_id):
    return B.check(user_id)

@bans_bp.route('/bans/<int:user_id>', methods=['DELETE'])
def unban(user_id):
    return B.unban(user_id)



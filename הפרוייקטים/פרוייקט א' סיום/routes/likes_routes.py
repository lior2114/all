from flask import Flask, Blueprint
from controller.likes_controller import Likes_Controller as L
likes_bp = Blueprint("/likes", __name__)

@likes_bp.route("/likes", methods = ["POST"])
def add_like_to_vacation():
    return L.add_like_to_vacation()

@likes_bp.route("/likes", methods = ["DELETE"])
def unlike_vacation():
    return L.unlike_vacation()

@likes_bp.route("/likes", methods = ["GET"])
def show_all_likes():
    return L.show_all_likes()
from flask import Flask, Blueprint, jsonify
from controller.worker_controller import WorkersControllers as WC

worker_bp = Blueprint("/worker", __name__)

@worker_bp.route("/worker", methods = ["POST"])
def create_worker():
  return WC.create_worker()

@worker_bp.route("/worker", methods = ["GET"])
def get_all_workers():
  return WC.get_all_workers()

@worker_bp.route("/worker/<int:worker_id>", methods = ["GET"])
def get_worker_by_id(worker_id):
  return WC.get_worker_by_id(worker_id)

@worker_bp.route("/worker/<int:worker_id>", methods = ["PUT"])
def update_worker(worker_id):
 return WC.update_worker(worker_id)

@worker_bp.route("/worker/<int:worker_id>", methods = ["DELETE"])
def delete_worker_by_id(worker_id):
  return WC.delete_worker(worker_id)


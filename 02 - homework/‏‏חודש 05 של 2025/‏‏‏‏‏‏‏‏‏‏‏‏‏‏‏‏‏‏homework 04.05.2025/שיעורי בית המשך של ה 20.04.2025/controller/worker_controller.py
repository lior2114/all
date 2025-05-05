from flask import jsonify,request
from models.workers_model import WorkersModel as W

class WorkersControllers:
    @staticmethod
    def create_worker():
        data = request.get_json()
        fields = ["first_name", "last_name", "salary","role_id"]
        if not data or not all(k in data for k in fields) : 
            return jsonify({"Error":"Data is empty/inccorect"}), 400
        result = W.create_worker(
            first_name=data["first_name"],
            last_name=data["last_name"],
            salary=data["salary"],
            role_id=data["role_id"]
        )
        return jsonify({"message":"worker created successfully", "worker_id":result["worker_id"]})
    
    @staticmethod
    def get_all_workers():
        result = W.get_all()
        return jsonify(result)
    
    @staticmethod
    def get_worker_by_id(worker_id):
        result = W.get_by_id(worker_id)
        return jsonify(result),201
    
    @staticmethod
    def update_worker(worker_id):
        data = request.get_json()
        if not data:
            return jsonify({"Error":"No Data provided"})
        result = W.update_worker_details(worker_id, data)
        if result is None:
            return jsonify({"Error": "worker not found"})
        return jsonify(result), 201
    
    @staticmethod
    def delete_worker(worker_id):
        result = W.delete_worker_by_id(worker_id)
        if not result:
            return jsonify({"Error":f"worker not found with id {worker_id}"}),400
        return jsonify({"message":f"worker: {worker_id} has been deleted"}),201
    
    @staticmethod
    def show_description_in_workers(worker_id):
        result = W.show_description_by_worker_id(worker_id)
        return jsonify(result),201
        

        
        
        
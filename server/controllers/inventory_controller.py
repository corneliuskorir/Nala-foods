from flask import Blueprint, jsonify, request
from services import InventoryService


def inventory_blueprint(service: InventoryService):

    inventory_bp = Blueprint("inventory", __name__, url_prefix="/inventory")

    @inventory_bp.route("", methods=["GET"])
    def get_items():
        products = service.get()
        return jsonify(products), 200

    @inventory_bp.route("", methods=["POST"])
    def add_item():
        data = request.get_json()
        item = service.add(data=data)
        if item:
            return jsonify(item), 201
        return jsonify({"message": "Something went wrong"}), 404

    @inventory_bp.route("/<int:id>", methods=["GET"])
    def get_item(id):
        item = service.get_item(id=id)
        if item:
            return jsonify(item), 200
        return jsonify({"message": f"Failed to get item id:{id}."}), 404

    @inventory_bp.route("/<int:id>", methods=["PATCH"])
    def update_item(id):
        data = request.get_json()
        if not data:
            return jsonify({"message": "Cannot update empty with value"}), 404
        item = service.update(id=id, data=data)
        return jsonify(item), 201

    @inventory_bp.route("/<int:id>", methods=["DELETE"])
    def delete_item(id):
        if service.delete(id):
            return jsonify({"message": "Delete item"}), 204
        else:
            return jsonify({"message": "Failed to delete item"}), 404

    return inventory_bp

from flask import Blueprint, jsonify, request


def inventory_blueprint():

    inventory_bp = Blueprint("inventory", __name__, url_prefix="/inventory")

    @inventory_bp.route("/", methods=["GET"])
    def get_items():
        return jsonify({"message": "Get inventory."}), 200

    @inventory_bp.route("/", methods=["POST"])
    def add_item():
        data = request.get_json()
        return jsonify({"message": "add inventory", "data": data}), 201

    @inventory_bp.route("/<int:id>", methods=["GET"])
    def get_item(id):
        return jsonify({"message": f"Get item {id}"}), 200

    @inventory_bp.route("/<int:id>", methods=["PATCH"])
    def update_item(id):
        data = request.get_json()
        return jsonify({"message": f"update item {id}", "data": data}), 201

    @inventory_bp.route("/<int:id>", methods=["DELETE"])
    def delete_item(id):
        return jsonify({"message": "Delete item"}), 204

    return inventory_bp

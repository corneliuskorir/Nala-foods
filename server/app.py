from flask import Flask, jsonify
from controllers import inventory_blueprint
from services import InventoryService
from repository import InventoryRepository
from data import inventory


def create_app():
    app = Flask(__name__)

    repo = InventoryRepository(inventory=inventory)
    service = InventoryService(repository=repo)

    app.register_blueprint(inventory_blueprint(service=service))

    @app.route("/", methods=["GET"])
    def entry():
        return (
            jsonify(
                {
                    "message": "Welcome to the Nala foods api",
                    "status": "Active",
                    "routes": [
                        {"endpoint": "/inventory", "methods": ["GET", "POST"]},
                        {
                            "endpoint": "/inventory/<id>",
                            "methods": ["GET", "PATCH", "DELETE"],
                        },
                    ],
                }
            ),
            200,
        )

    return app

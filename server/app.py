from flask import Flask, jsonify
from .controllers.inventory_controller import inventory_blueprint


def create_app():
    app = Flask(__name__)

    app.register_blueprint(inventory_blueprint())

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

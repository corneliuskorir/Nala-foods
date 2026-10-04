from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def entry():
        return (
            jsonify(
                {
                    "message": "Welcome to the Nala foods api",
                    "status": "Active",
                    "routes": [
                        {"endpoint": "/products", "methods": ["GET", "POST"]},
                        {
                            "endpoint": "/products/<id>",
                            "methods": ["GET", "PATCH", "DELETE"],
                        },
                    ],
                }
            ),
            200,
        )

    return app

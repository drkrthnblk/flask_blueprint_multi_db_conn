import os
from flask import Flask
from blueprints.main.show_main import main_bp
from blueprints.local.show_local import local_bp
from blueprints.main_local.show_main_local import main_local_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    app.register_blueprint(local_bp)
    app.register_blueprint(main_local_bp)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
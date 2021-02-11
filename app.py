import os
from flask import Flask
from blueprints.main.show_main import main_bp

app = Flask(__name__)

def create_app():
    app.register_blueprint(main_bp)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
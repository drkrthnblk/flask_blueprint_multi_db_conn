import os
from flask import Flask
from blueprints.main.show_main import main_bp
from blueprints.local.show_local import local_bp
from blueprints.main_local.show_main_local import main_local_bp
from blueprints.db_conn.db_routes import db_bp

import database

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    # initialize database tables
    database.init_app(app)

    # registering blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(local_bp)
    app.register_blueprint(main_local_bp)
    app.register_blueprint(db_bp)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
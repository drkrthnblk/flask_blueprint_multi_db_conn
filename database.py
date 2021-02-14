from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()

from models.model import Result, Acutal

def create_db(app):
    """Creates database"""
    with app.app_context():
        db.create_all()
        db.session.commit()

def drop_db():
    """Drop / Clean database - DANGER ACTION"""
    db.drop_all()

def init_app(app):
    db.init_app(app)
    create_db(app)


from flask import Blueprint, jsonify

from database import db, ma

db_bp = Blueprint('database_conn', __name__)

from models.model import Acutal, AcutalSchema
from models.model import Result, ResultSchema

@db_bp.route("/actual")
def list_of_clothes():
    actuals_schema = AcutalSchema(many=True)
    op_data = Acutal.query.all()
    op = actuals_schema.dump(op_data)
    return jsonify(op)
    


@db_bp.route("/result")
def list_of_shoes():
    actuals_schema = ResultSchema(many=True)
    op_data = Result.query.all()
    op = actuals_schema.dump(op_data)
    return jsonify(op)

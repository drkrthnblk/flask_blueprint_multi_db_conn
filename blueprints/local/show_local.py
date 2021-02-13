from flask import Blueprint, render_template, current_app, url_for 

local_bp = Blueprint('local', __name__, static_folder='static',static_url_path='/static/local',
               template_folder='templates')        

@local_bp.route('/show_local')
def show():
    return render_template("webfiles/show_local.html")
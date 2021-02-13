from flask import Blueprint, render_template, current_app 

main_local_bp = Blueprint('main_local', __name__, static_folder='static',static_url_path='/static/main_local',
               template_folder='templates')

@main_local_bp.route('/show_main_local')
def show():
    # using main css and local image
    css = os.path.join(os.path.join('static'), 'css/body_main.css')
    return render_template("webfiles/show_main_local.html", in_css=css)
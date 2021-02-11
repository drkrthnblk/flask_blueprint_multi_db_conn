from flask import Blueprint, render_template, current_app
import os    

main_bp = Blueprint('main', __name__, static_folder='static',static_url_path='/static',
               template_folder='templates')


@main_bp.route('/')
def show_all_links():
    return render_template("show_links.html")


@main_bp.route('/show_main')
def show():
    return render_template("show_main.html")

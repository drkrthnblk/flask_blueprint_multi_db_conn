from flask import Blueprint, render_template, current_app, url_for 

main_bp = Blueprint('main', __name__, static_folder='static',static_url_path='/static',
               template_folder='templates')

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    print("defaults, args: ", defaults, arguments)
    return len(defaults) >= len(arguments)


@main_bp.route('/')
def show_all_links():
    app = current_app._get_current_object()
    # print(app)
    links = []
    for rule in app.url_map.iter_rules():
        print("####", rule.methods)
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    return render_template("show_links.html" ,links=links)


@main_bp.route('/show_main')
def show():
    return render_template("show_main.html")

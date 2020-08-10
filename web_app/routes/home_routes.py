from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)


@home_routes.route("/")
def index():
    print("VISITING THE HOME PAGE")
    x = 100 / 20 
    return f"Hello World! {x}"

@home_routes.route("/about")
def about():
    print("VISITING THE ABOUT PAGE")
    return "About me"

@home_routes.route("/bio")
def bio():
    print("THIS IS ME...")
    return "Biography"


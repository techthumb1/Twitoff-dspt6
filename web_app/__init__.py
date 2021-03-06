# web_app/__init__.py

import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv() # loads env vars from the .env file (locally)

from web_app.models import db, migrate
from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes

# DATABASE_URL = os.getenv("DATABASE_URL"), connection to our database.
DATABASE_URI = "sqlite:///C:\\Users\\Aarons\\Desktop\\twitoff-dspt6\\web_app\\twitoff_development.db"
def create_app():
    # Our app instance.
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
    
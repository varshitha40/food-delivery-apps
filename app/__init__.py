import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# Create database object
db = SQLAlchemy()

# Create login manager
login_manager = LoginManager()
login_manager.login_view = "main.login"


def create_app():

    app = Flask(__name__)

    # --------------------------------------------------
    # Configuration
    # --------------------------------------------------

    app.config["SECRET_KEY"] = "food_delivery_secret_key_2026"

    BASE_DIR = os.path.abspath(
        os.path.dirname(os.path.dirname(__file__))
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "sqlite:///"
        + os.path.join(BASE_DIR, "database.db")
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # --------------------------------------------------
    # Initialize database
    # --------------------------------------------------

    db.init_app(app)

    # --------------------------------------------------
    # Initialize Flask Login
    # --------------------------------------------------

    login_manager.init_app(app)

    # --------------------------------------------------
    # User loader
    # --------------------------------------------------

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    # --------------------------------------------------
    # Import routes
    # --------------------------------------------------

    from app.routes import main

    app.register_blueprint(main)

    # --------------------------------------------------
    # Create database tables
    # --------------------------------------------------

    with app.app_context():
        db.create_all()

    return app
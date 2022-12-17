"""
Initializing the application
"""
import os

from cryptography.fernet import Fernet
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash

db = SQLAlchemy()
migrate = Migrate()
basic_auth = HTTPBasicAuth()
marshmallow = Marshmallow()
fernet = None


@basic_auth.verify_password
def verify_password(username, password):
    """
    Match the user provided credentials against database values.
    Returns username if credentials are verified.

    Args:
        username(string): Username value provided by user
        password(string): Password value provided by user

    Returns: string or None
    """
    from .models import User  # pylint: disable=import-outside-toplevel
    user = User.query.get(username)

    if user and check_password_hash(user.password, password):
        return username

    return None


def get_database_url():
    """
    Generate the database url.

    Args: None
    Returns: string
    """
    db_name = os.environ.get('DB_NAME')
    return f'sqlite:///{db_name}'


def init_app():
    """
    Initialize the core application.

    Args: None
    Returns: object
    """
    global fernet

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = get_database_url()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    encryption_key = Fernet.generate_key()
    fernet = Fernet(encryption_key)

    with app.app_context():
        # Include our Routes
        # pylint: disable=cyclic-import
        from . import models, routes  # pylint: disable=import-outside-toplevel, unused-import

        # Register Blueprints
        app.register_blueprint(routes.home_bp)

        return app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# from flask_login import LoginManager
from flask_cors import CORS
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__, instance_relative_config=False)
app.config.from_object("config.Config")

# init Modules
db = SQLAlchemy(app)
login = LoginManager(app)
migrate = Migrate(app, db)
cors = CORS(app)

from .models import User


with app.app_context():
    from . import auth

    # Register Blueprints
    app.register_blueprint(auth.auth_bp)

    # Create Database Models
    db.create_all()

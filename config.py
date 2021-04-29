"""Flask app configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    """Set Flask configuration from environment variables."""

    FLASK_APP = "start-backend.py"
    FLASK_ENV = environ.get("FLASK_ENV")
    SECRET_KEY = "123456789"  # !!!!!
    SESSION_TYPE = "filesystem"

    # CORS config
    CORS_HEADERS = "Content-Type"

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

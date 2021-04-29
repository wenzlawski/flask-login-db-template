"""Database models."""
from flask_login import UserMixin
from . import db, login
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    """User account model."""

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(
        db.String(200), primary_key=False, unique=False, nullable=False
    )

    def __init__(self, username, password):
        self.set_password(password)
        self.username = username

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method="sha256")

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<User {}>".format(self.username)

    # Properties required for Flask-Login
    def is_active(self):
        """Returns True, as all users are active"""
        return True

    # def get_email(self):
    #     """Returns the email address"""
    #     return self.email

    # def is_authenticated(self):
    #     """Returns True if the user is authenticated"""
    #     return self.authenticated

    # def is_anonymous(self):
    #     """Returns False, anonymous users aren't a thing"""
    #     return False


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

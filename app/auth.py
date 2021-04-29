from flask import Blueprint, request
from flask import json
from flask_login import login_required, logout_user, current_user, login_user
from flask.json import jsonify
from . import db
from .models import User

auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return jsonify("already authenticated"), 400
    user_info = json.loads(request.data)
    if not all([v in user_info.keys() for v in ["username", "password"]]):
        print("Bad request")
        return jsonify("Bad request"), 400
    # Logging in user
    user = User.query.filter_by(username=user_info["username"]).first()
    if user:
        if user.check_password(user_info["password"]):
            login_user(user, remember=True)
            return jsonify("success")
        else:
            print("Incorrect login details")
            return jsonify("Wrong password"), 400
    else:
        print("User not found")
        return jsonify("User does not exist"), 400


@auth_bp.route("/protected", methods=["GET"])
@login_required
def access():
    print("Accessing protected function")
    print(current_user)
    return jsonify("Successfully accessed protected function.")


@auth_bp.route("/logout", methods=["GET"])
@login_required
def logout():
    user = current_user
    logout_user()


@auth_bp.route("/register", methods=["POST"])
def register():
    data = json.loads(request.data)
    if not all([v in data.keys() for v in ["username", "password"]]):
        print("Bad request")
        return jsonify("Bad request"), 400
    if User.query.filter_by(username=data["username"]).first():
        print("User already exists")
        return jsonify("User already exists"), 400
    u = User(username=data["username"], password=data["password"])
    db.session.add(u)
    db.session.commit()
    print("Added user to database")
    return jsonify("Success")
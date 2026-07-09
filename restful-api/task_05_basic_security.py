#!/usr/bin/env python3
"""Simple Flask API"""

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)

# GET /basic-protected
# POST /login
# GET /jwt-protected
# GET /admin-only

app = Flask(__name__)
auth = HTTPBasicAuth()

# Secret key used to generate and validate JWT signatures
app.config["JWT_SECRET_KEY"] = "litoxamtoken"
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

@auth.verify_password
def verify_password(username, password):
    # Find the user in memory
    user = users.get(username)

    # Check user and password
    if user and check_password_hash(user["password"], password):
        return username

    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def get_basic():
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def post_login():
    # Get JSON data from the request
    data = request.get_json()

    # Get username and password
    username = data.get("username")
    password = data.get("password")

    # Find the user in memory
    user = users.get(username)

    # Check user and password
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Unauthorized"}), 401

    # Generate a JWT token
    access_token = create_access_token(identity=username)

    # Return the token
    return jsonify({
        "access_token": access_token
    })


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def get_jwt_protected():
    # Return a success message
    return jsonify({
        "message": "JWT Auth: Access Granted"
    }), 200


@jwt.unauthorized_loader
def handle_unauthorized_loader(_):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_loader(_):
    return jsonify({"error": "Invalid token"}), 401


@app.route("/admin-only", methods=["GET"])
# Require a valid JWT token
@jwt_required()
def get_admin_only():
    # Get the current user's identity from the token
    current_user = get_jwt_identity()

    # Get the dictionary of the current user
    user = users.get(current_user)

    if user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    # Return a success message
    return jsonify({
        "message": "Admin Access: Granted"
    })


if __name__ == "__main__":
    app.run(debug=True)
#!/usr/bin/env python3
"""Simple Flask API"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Users stored in memory
users = {}


@app.route("/")
def home():
    """Home endpoint"""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Return all usernames"""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return API status"""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Return a user"""

    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[username])


@app.post("/add_user")
def add_user():
    """Add a new user"""

    data = request.get_json()

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if username is None:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    user = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    users[username] = user

    return jsonify({
        "message": "User added",
        "user": user
    }), 201


if __name__ == "__main__":
    app.run()

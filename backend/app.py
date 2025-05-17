from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_session import Session

app = Flask(__name__)
app.secret_key = "super-secret-key"  # Change this for production!
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

CORS(app, supports_credentials=True)  # Allow cookies from frontend

# Fake user
USER = {"username": "tames", "password": "1234"}

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    if data["username"] == USER["username"] and data["password"] == USER["password"]:
        session["user"] = data["username"]
        return jsonify({"success": True, "message": "Logged in"})
    return jsonify({"success": False, "message": "Invalid credentials"}), 401

@app.route("/api/logout", methods=["POST"])
def logout():
    session.pop("user", None)
    return jsonify({"message": "Logged out"})


@app.route("/api/check", methods=["GET"])
def check_login():
    user = session.get("user")
    if user:
        return jsonify({"logged_in": True, "username": user})
    return jsonify({"logged_in": False})

if __name__ == "__main__":
    app.run(debug=True)
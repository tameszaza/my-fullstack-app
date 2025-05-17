import os
from flask import Flask, jsonify, session, request
from flask_cors import CORS
from flask_session import Session

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["https://my-fullstack-app-l1vs.onrender.com"])
app.secret_key = "super-secret-key"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from Flask!"})

@app.route("/api/check")
def check():
    user = session.get("user")
    return jsonify({"logged_in": bool(user), "username": user or ""})

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    if data["username"] == "tames" and data["password"] == "1234":
        session["user"] = "tames"
        return jsonify(success=True)
    return jsonify(success=False), 401

@app.route("/api/logout", methods=["POST"])
def logout():
    session.pop("user", None)
    return jsonify(success=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

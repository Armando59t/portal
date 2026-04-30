from flask import Flask, request, jsonify, render_template, session
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
app.secret_key = "secreto123"  # 🔐 necesario para sesiones
CORS(app)

MONGO_URI = "TU_URI_AQUI"
client = MongoClient(MONGO_URI)
db = client["portal_academico"]

usuarios = db["usuarios"]

@app.route("/")
def home():
    return render_template("index.html")

# REGISTRO
@app.route("/registro", methods=["POST"])
def registro():
    data = request.json

    if usuarios.find_one({"usuario": data["usuario"]}):
        return jsonify({"error": "Usuario ya existe"})

    usuarios.insert_one(data)
    return jsonify({"mensaje": "Registrado correctamente"})

# LOGIN
@app.route("/login", methods=["POST"])
def login():
    data = request.json

    user = usuarios.find_one({
        "usuario": data["usuario"],
        "password": data["password"]
    })

    if user:
        session["usuario"] = data["usuario"]
        return jsonify({"mensaje": "Login correcto"})
    else:
        return jsonify({"error": "Datos incorrectos"})

# SESIÓN ACTUAL
@app.route("/sesion")
def sesion():
    if "usuario" in session:
        return jsonify({"usuario": session["usuario"]})
    return jsonify({"usuario": None})

# LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    return jsonify({"mensaje": "Sesión cerrada"})

if __name__ == "__main__":
    app.run(debug=True)

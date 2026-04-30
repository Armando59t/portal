from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# 🔗 MEJOR usar variable de entorno (Render)
MONGO_URI = os.getenv("mongodb+srv://ricardopauljose92_db_user:sSondflxoc6PIFw6@cluster0.tmppfp7.mongodb.net/?retryWrites=true&w=majority"
)

# ⚠️ Si quieres probar localmente, usa esto (con comillas)
# MONGO_URI = "mongodb+srv://ricardopauljose92_db_user:sSondflxoc6PIFw6@cluster0.tmppfp7.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client["portal_academico"]

usuarios = db["usuarios"]
reinscripciones = db["reinscripciones"]

@app.route("/")
def home():
    return render_template("index.html")

# REGISTRO
@app.route("/registro", methods=["POST"])
def registro():
    data = request.json

    usuario = data.get("usuario")
    correo = data.get("correo")
    password = data.get("password")

    if not usuario or not correo or not password:
        return jsonify({"error": "Campos incompletos"}), 400

    if not correo.endswith("@cbtis.edu.mx"):
        return jsonify({"error": "Correo inválido"}), 400

    if usuarios.find_one({"usuario": usuario}):
        return jsonify({"error": "Usuario ya existe"}), 400

    usuarios.insert_one({
        "usuario": usuario,
        "correo": correo,
        "password": password
    })

    return jsonify({"mensaje": "Registrado correctamente"})

# LOGIN
@app.route("/login", methods=["POST"])
def login():
    data = request.json

    user = usuarios.find_one({
        "usuario": data.get("usuario"),
        "password": data.get("password")
    })

    if user:
        return jsonify({"mensaje": "Login correcto"})
    else:
        return jsonify({"error": "Datos incorrectos"}), 401

# REINSCRIPCIÓN
@app.route("/reinscripcion", methods=["POST"])
def reinscripcion():
    data = request.json
    reinscripciones.insert_one(data)
    return jsonify({"mensaje": "Guardado correctamente"})

if __name__ == "__main__":
    app.run(debug=True)

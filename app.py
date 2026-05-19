from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)

# =========================
# CONEXIÓN MONGODB ATLAS
# =========================

MONGO_URI = "mongodb+srv://Armando:Armando@cluster0.hmkf3ka.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

cliente = MongoClient(MONGO_URI)

db = cliente["tienda"]

clientes = db["clientes"]
productos = db["productos"]

# =========================
# INICIO
# =========================

@app.route("/")
def inicio():

    lista_clientes = clientes.find()
    lista_productos = productos.find()

    return render_template(
        "index.html",
        clientes=lista_clientes,
        productos=lista_productos
    )

# =========================
# CREAR CLIENTE
# =========================

@app.route("/agregar_cliente", methods=["POST"])
def agregar_cliente():

    nuevo_cliente = {

        "nombre": request.form["nombre"],
        "edad": request.form["edad"],
        "correo": request.form["correo"],
        "telefono": request.form["telefono"]

    }

    clientes.insert_one(nuevo_cliente)

    return redirect("/")

# =========================
# CREAR PRODUCTO
# =========================

@app.route("/agregar_producto", methods=["POST"])
def agregar_producto():

    nuevo_producto = {

        "nombre": request.form["nombre"],
        "precio": request.form["precio"],
        "stock": request.form["stock"],
        "categoria": request.form["categoria"]

    }

    productos.insert_one(nuevo_producto)

    return redirect("/")

# =========================
# BUSCAR CLIENTE
# =========================

@app.route("/buscar")
def buscar():

    nombre = request.args.get("nombre")

    resultado = clientes.find({
        "nombre": {"$regex": nombre, "$options": "i"}
    })

    return render_template(
        "buscar.html",
        clientes=resultado
    )

# =========================
# ELIMINAR CLIENTE
# =========================

@app.route("/eliminar_cliente/<id>")
def eliminar_cliente(id):

    clientes.delete_one({
        "_id": ObjectId(id)
    })

    return redirect("/")

# =========================
# ELIMINAR PRODUCTO
# =========================

@app.route("/eliminar_producto/<id>")
def eliminar_producto(id):

    productos.delete_one({
        "_id": ObjectId(id)
    })

    return redirect("/")

# =========================
# FORMULARIO EDITAR CLIENTE
# =========================

@app.route("/editar_cliente/<id>")
def editar_cliente(id):

    cliente_editar = clientes.find_one({
        "_id": ObjectId(id)
    })

    return render_template(
        "editar_cliente.html",
        cliente=cliente_editar
    )

# =========================
# ACTUALIZAR CLIENTE
# =========================

@app.route("/actualizar_cliente/<id>", methods=["POST"])
def actualizar_cliente(id):

    clientes.update_one(

        {"_id": ObjectId(id)},

        {
            "$set": {

                "nombre": request.form["nombre"],
                "edad": request.form["edad"],
                "correo": request.form["correo"],
                "telefono": request.form["telefono"]

            }
        }

    )

    return redirect("/")

# =========================
# FORMULARIO EDITAR PRODUCTO
# =========================

@app.route("/editar_producto/<id>")
def editar_producto(id):

    producto_editar = productos.find_one({
        "_id": ObjectId(id)
    })

    return render_template(
        "editar_producto.html",
        producto=producto_editar
    )

# =========================
# ACTUALIZAR PRODUCTO
# =========================

@app.route("/actualizar_producto/<id>", methods=["POST"])
def actualizar_producto(id):

    productos.update_one(

        {"_id": ObjectId(id)},

        {
            "$set": {

                "nombre": request.form["nombre"],
                "precio": request.form["precio"],
                "stock": request.form["stock"],
                "categoria": request.form["categoria"]

            }
        }

    )

    return redirect("/")

# =========================
# EJECUTAR
# =========================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )

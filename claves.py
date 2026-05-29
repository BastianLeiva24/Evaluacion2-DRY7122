from flask import Flask, request
import sqlite3

app = Flask(__name__)

DB = "usuarios.db"

def crear_tabla():

    conexion = sqlite3.connect(DB)
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT,
        password TEXT
    )
    """)

    conexion.commit()
    conexion.close()

crear_tabla()

@app.route("/")
def inicio():
    return "Servidor Flask operativo"

@app.route("/registro")
def registro():

    usuario = request.args.get("usuario")
    password = request.args.get("password")

    conexion = sqlite3.connect(DB)
    cursor = conexion.cursor()

    cursor.execute(
        "INSERT INTO usuarios(usuario,password) VALUES(?,?)",
        (usuario, password)
    )

    conexion.commit()
    conexion.close()

    return "Usuario registrado"

@app.route("/login")
def login():

    usuario = request.args.get("usuario")
    password = request.args.get("password")

    conexion = sqlite3.connect(DB)
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE usuario=? AND password=?",
        (usuario, password)
    )

    resultado = cursor.fetchone()

    conexion.close()

    if resultado:
        return "Acceso correcto"

    return "Acceso denegado"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

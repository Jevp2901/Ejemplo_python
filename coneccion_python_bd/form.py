from flask import Flask, request, render_template_string
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Página principal con el formulario
@app.route("/")
def index():
    return open("index.html", encoding="utf-8").read()

# Ruta que recibe el formulario y registra el jugador
@app.route("/registrar_jugador", methods=["POST"])
def registrar():
    name_jugador = request.form.get("name_jugador")
    password     = request.form.get("password")
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_juego"
        )
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO jugador(name_jugador, password) VALUES (%s, %s)",
            (name_jugador, password)
        )
        conexion.commit()
        return "<h2>✅ Jugador registrado exitosamente</h2><a href='/'>Volver</a>"
    except Error as error:
        return f"<h2>❌ Error: {error}</h2><a href='/'>Volver</a>"

if __name__ == "__main__":
    app.run(debug=True)
"""

Nota: para ejercutar colocar el siguiente comando en la terminal:
python form.

"""

import mysql.connector
from mysql.connector import Error

#Instrucciones para la coneccion a la base de datos

try: 
    conexion_bd = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "bd_juego"
    )

    #comprobar si la conexion es exitosa
    if conexion_bd.is_connected():
        print(f"Conexion exitosa con la base de datos")
except Error as e:
    print(f"Error al conectar a la base de datos: {e}")

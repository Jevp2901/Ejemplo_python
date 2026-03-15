import mysql.connector
from mysql.connector import Error 
import conexion_bd
#Se define la funcion para registrar un jugador
def registrar_jugador(name_jugador, password):
    try:
        conexion_bd = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "bd_juego"
        )
        
        cursor = conexion_bd.cursor()
        #Mediante cursor se da intrucciones agrgar un nuevo usuario con la base de datos
        cursor.execute("INSERT INTO jugador(name_jugador, password) VALUES (%s, %s)", (name_jugador, password))
        conexion_bd.commit()
        print("Jugador registrado exitosamente")
    except Error as e:
        print(f"Error al registrar el jugador: {e}")
    










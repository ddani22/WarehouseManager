
# Importa el conector de MySQL y la clase de error para manejar excepciones

# Importa el conector de MySQL y la clase de error para manejar excepciones
import mysql.connector
from mysql.connector import Error
# Importa dotenv para cargar variables de entorno
from dotenv import load_dotenv
import os

# Carga las variables de entorno desde el archivo .env
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../.env'))

# Parámetros de conexión a la base de datos obtenidos desde .env
host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_NAME')


# Clase para gestionar la conexión y operaciones con la base de datos MySQL
class db_manager:
    """
    Clase para gestionar la conexión y las operaciones con la base de datos MySQL.
    Implementa un patrón básico de gestión de conexión.
    """
    def __init__(self, host, user, password, database):
        # Inicializa los parámetros de conexión
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None


    def connect(self):
        """
        Intenta establecer una conexión a la base de datos.
        Si la conexión ya existe y está activa, la reutiliza.
        """
        if self.connection is None or not self.connection.is_connected():
            try:
                # Intenta conectar con los parámetros proporcionados
                self.connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    passwd=self.password,
                    database=self.database
                )
                if self.connection.is_connected():
                    print("Conexión exitosa a MySQL.")
            except Error as e:
                # Si ocurre un error, muestra el mensaje y asegura que la conexión sea None
                print(f"Error al conectar a MySQL: {e}")
                self.connection = None
        return self.connection


    def disconnect(self):
        """
        Cierra la conexión a la base de datos si está abierta.
        Es importante liberar recursos cuando ya no se necesita la conexión.
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()
            self.connection = None
            print("Conexión a MySQL cerrada.")


    def execute_query(self, sql_query, params=None, fetch_one=False, fetch_all=False):
        """
        Establece una conexión (si no existe), ejecuta una consulta SQL y maneja el cierre del cursor.
        Retorna los resultados si es una consulta SELECT.
        Parámetros:
            sql_query: Consulta SQL a ejecutar
            params: Parámetros para la consulta (tupla/lista/dict)
            fetch_one: Si es True, retorna solo un resultado
            fetch_all: Si es True, retorna todos los resultados
        """
        cursor = None
        result = None
        connection = None # Para asegurar que la conexión se maneje dentro de este método si es temporal

        try:
            # Reutiliza la conexión existente o crea una nueva si no está activa
            connection = self.connect() 
            if connection is None:
                print("No hay conexión a la base de datos.")
                return None

            # Crea el cursor para ejecutar la consulta
            cursor = connection.cursor()
            # Ejecuta la consulta con los parámetros dados
            cursor.execute(sql_query, params or ())

            # Realiza commit solo si la consulta modifica datos
            if sql_query.strip().upper().startswith(('INSERT', 'UPDATE', 'DELETE')):
                connection.commit()
            
            # Obtiene los resultados si es una consulta SELECT
            if fetch_one:
                result = cursor.fetchone()
            elif fetch_all:
                result = cursor.fetchall()
            
        except Error as e:
            # Muestra el error si la consulta falla
            print(f"Error al ejecutar consulta: {e}")
            # Revierte los cambios si hay un error
            if connection:
                connection.rollback()
        finally:
            # Cierra el cursor para liberar recursos
            if cursor:
                cursor.close()
            # No cerramos la conexión aquí si queremos reutilizarla para múltiples operaciones
            # La desconexión global debería ser manejada por la aplicación cuando finalice.
        return result
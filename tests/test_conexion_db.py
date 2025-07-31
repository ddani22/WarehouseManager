# Prueba simple de conexión a la base de datos
import unittest
from src.database.db_manager import db_manager, host, user, password, database

class TestConexionDB(unittest.TestCase):
    def test_conexion(self):
        db = db_manager(host, user, password, database)
        conn = db.connect()
        self.assertIsNotNone(conn)
        if conn is not None:
            self.assertTrue(conn.is_connected())
        else:
            self.fail("La conexión a la base de datos devolvió None.")

if __name__ == "__main__":
    unittest.main()

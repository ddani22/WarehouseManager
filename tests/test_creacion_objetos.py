# Pruebas de creación de objetos para DAOs y modelos
import unittest
from src.database.dao.productDAO import productDAO
from src.database.dao.clientDAO import clientDAO
from src.database.dao.movementDAO import movementDAO
from src.database.dao.supplierDAO import supplierDAO
from src.models.product import Product
from src.models.client import Client
from src.models.movement import Movement
from src.models.supplier import Supplier

class TestCreacionObjetos(unittest.TestCase):
    def test_creacion_objetos_bd(self):
        # Crear DAOs
        product_dao = productDAO()
        client_dao = clientDAO()
        movement_dao = movementDAO()
        supplier_dao = supplierDAO()
        # Crear modelos
        supplier = Supplier(1001, "ProveedorTest", 123456789, "proveedor@test.com", "Calle Falsa 123")
        client = Client(1001, "ClienteTest", "Calle Real 456", "987654321", "cliente@test.com")
        product = Product(1001, "ProductoTest", "Desc", "SKU9999", 10.0, 50, 5, "A1", 1001, "2025-07-20")
        movimiento_obj = Movement(1001, 1001, "entrada", 10, "2025-07-20", "ref1", 1, 1001)
        # Insertar en la base de datos
        supplier_dao.crear_proveedor(supplier)
        client_dao.crear_cliente(client)
        product_dao.crear_producto(product)
        movement_dao.crear_movimiento(movimiento_obj)
        # Comprobar que existen en la base de datos
        self.assertIsNotNone(supplier_dao.obtener_proveedor(1001))
        self.assertIsNotNone(client_dao.obtener_cliente(1001))
        self.assertIsNotNone(product_dao.obtener_producto(1001))
        self.assertIsNotNone(movement_dao.obtener_movimiento(1001))

if __name__ == "__main__":
    unittest.main()

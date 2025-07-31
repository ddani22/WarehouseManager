# Gestor de inventario
from src.database.dao.productDAO import productDAO
from src.database.dao.clientDAO import clientDAO
from src.database.dao.supplierDAO import supplierDAO
from src.database.dao.movementDAO import movementDAO
from src.models.product import Product
from src.models.client import Client
from src.models.supplier import Supplier
from src.models.movement import Movement

class InventoryManager:
    """
    Clase que coordina las operaciones principales del almacén: productos, clientes, proveedores y movimientos.
    """
    def __init__(self):
        # Inicializa los DAOs para cada entidad del sistema
        self.product_dao = productDAO()
        self.client_dao = clientDAO()
        self.supplier_dao = supplierDAO()
        self.movement_dao = movementDAO()

    # --- Productos ---
    def agregar_producto(self, *args, **kwargs):
        """
        Crea y agrega un nuevo producto al almacén.
        """
        producto = Product(*args, **kwargs)
        self.product_dao.crear_producto(producto)
        return producto

    def obtener_producto(self, id_producto):
        """
        Obtiene un producto por su ID.
        """
        return self.product_dao.obtener_producto(id_producto)

    def actualizar_producto(self, producto):
        """
        Actualiza los datos de un producto existente.
        """
        self.product_dao.actualizar_producto(producto)

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto por su ID.
        """
        self.product_dao.eliminar_producto(id_producto)

    def listar_productos(self):
        """
        Devuelve la lista de todos los productos.
        """
        return self.product_dao.listar_productos()

    # --- Clientes ---
    def agregar_cliente(self, *args, **kwargs):
        """
        Crea y agrega un nuevo cliente.
        """
        cliente = Client(*args, **kwargs)
        self.client_dao.crear_cliente(cliente)
        return cliente

    def obtener_cliente(self, id_cliente):
        """
        Obtiene un cliente por su ID.
        """
        return self.client_dao.obtener_cliente(id_cliente)

    def actualizar_cliente(self, cliente):
        """
        Actualiza los datos de un cliente existente.
        """
        self.client_dao.actualizar_cliente(cliente)

    def eliminar_cliente(self, id_cliente):
        """
        Elimina un cliente por su ID.
        """
        self.client_dao.eliminar_cliente(id_cliente)

    def listar_clientes(self):
        """
        Devuelve la lista de todos los clientes.
        """
        return self.client_dao.listar_clientes()

    # --- Proveedores ---
    def agregar_proveedor(self, *args, **kwargs):
        """
        Crea y agrega un nuevo proveedor.
        """
        proveedor = Supplier(*args, **kwargs)
        self.supplier_dao.crear_proveedor(proveedor)
        return proveedor

    def obtener_proveedor(self, id_proveedor):
        """
        Obtiene un proveedor por su ID.
        """
        return self.supplier_dao.obtener_proveedor(id_proveedor)

    def actualizar_proveedor(self, proveedor):
        """
        Actualiza los datos de un proveedor existente.
        """
        self.supplier_dao.actualizar_proveedor(proveedor)

    def eliminar_proveedor(self, id_proveedor):
        """
        Elimina un proveedor por su ID.
        """
        self.supplier_dao.eliminar_proveedor(id_proveedor)

    def listar_proveedores(self):
        """
        Devuelve la lista de todos los proveedores.
        """
        return self.supplier_dao.listar_proveedores()

    # --- Movimientos ---
    def registrar_movimiento(self, *args, **kwargs):
        """
        Registra un nuevo movimiento de inventario (entrada/salida).
        """
        movimiento = Movement(*args, **kwargs)
        self.movement_dao.crear_movimiento(movimiento)
        return movimiento

    def obtener_movimiento(self, id_movimiento):
        """
        Obtiene un movimiento por su ID.
        """
        return self.movement_dao.obtener_movimiento(id_movimiento)

    def actualizar_movimiento(self, movimiento):
        """
        Actualiza los datos de un movimiento existente.
        """
        self.movement_dao.actualizar_movimiento(movimiento)

    def eliminar_movimiento(self, id_movimiento):
        """
        Elimina un movimiento por su ID.
        """
        self.movement_dao.eliminar_movimiento(id_movimiento)

    def listar_movimientos(self):
        """
        Devuelve la lista de todos los movimientos registrados.
        """
        return self.movement_dao.listar_movimientos()

    

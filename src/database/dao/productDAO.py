# DAO para la entidad Producto
from src.database.db_manager import db_manager, host, user, password, database
from src.models.product import Product

class productDAO:
    """
    DAO para operaciones CRUD sobre la entidad Producto.
    """
    def __init__(self):
        self.db = db_manager(host, user, password, database)

    def crear_producto(self, producto):
        """
        Inserta un nuevo producto en la base de datos.
        :param producto: Product
        """
        try:
            query = ("INSERT INTO productos (id_producto, nombre_producto, descripcion, sku, precio_unitario, stock_actual, stock_minimo, ubicacion, id_proveedor, fecha_alta) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            values = (
                producto.id_producto,
                producto.nombre_producto,
                producto.descripcion,
                producto.sku,
                producto.precio_unitario,
                producto.stock_actual,
                producto.stock_minimo,
                producto.ubicacion,
                producto.id_proveedor,
                producto.fecha_alta
            )
            self.db.execute_query(query, values)
        except Exception as e:
            print(f"Error al crear producto: {e}")

    def obtener_producto(self, id_producto):
        """
        Obtiene un producto por su ID.
        :param id_producto: int
        :return: Product o None
        """
        try:
            query = "SELECT id_producto, nombre_producto, descripcion, sku, precio_unitario, stock_actual, stock_minimo, ubicacion, id_proveedor, fecha_alta FROM productos WHERE id_producto = %s"
            row = self.db.execute_query(query, (id_producto,), fetch_one=True)
            if row:
                return Product(*row)
            return None
        except Exception as e:
            print(f"Error al obtener producto: {e}")
            return None

    def actualizar_producto(self, producto):
        """
        Actualiza los datos de un producto existente.
        :param producto: Product
        """
        try:
            query = ("UPDATE productos SET nombre_producto=%s, descripcion=%s, sku=%s, precio_unitario=%s, stock_actual=%s, stock_minimo=%s, ubicacion=%s, id_proveedor=%s, fecha_alta=%s "
                    "WHERE id_producto=%s")
            values = (
                producto.nombre_producto,
                producto.descripcion,
                producto.sku,
                producto.precio_unitario,
                producto.stock_actual,
                producto.stock_minimo,
                producto.ubicacion,
                producto.id_proveedor,
                producto.fecha_alta,
                producto.id_producto
            )
            self.db.execute_query(query, values)
        except Exception as e:
            print(f"Error al actualizar producto: {e}")

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto por su ID.
        :param id_producto: int
        """
        try:
            query = "DELETE FROM productos WHERE id_producto = %s"
            self.db.execute_query(query, (id_producto,))
        except Exception as e:
            print(f"Error al eliminar producto: {e}")

    def listar_productos(self):
        """
        Devuelve una lista de todos los productos.
        :return: list[Product]
        """
        try:
            query = "SELECT id_producto, nombre_producto, descripcion, sku, precio_unitario, stock_actual, stock_minimo, ubicacion, id_proveedor, fecha_alta FROM productos"
            rows = self.db.execute_query(query, fetch_all=True)
            if rows is None:
                return []
            if isinstance(rows, list):
                return [Product(*row) for row in rows]
            try:
                return [Product(*rows)]
            except Exception:
                return []
        except Exception as e:
            print(f"Error al listar productos: {e}")
            return []

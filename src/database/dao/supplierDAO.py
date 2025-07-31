# DAO para la entidad Proveedor
from src.database.db_manager import db_manager, host, user, password, database
from src.models.supplier import Supplier

class supplierDAO:
    """
    DAO para operaciones CRUD sobre la entidad Proveedor.
    """
    def __init__(self):
        self.db = db_manager(host, user, password, database)

    def crear_proveedor(self, proveedor):
        """
        Inserta un nuevo proveedor en la base de datos.
        :param proveedor: Supplier
        """
        try:
            query = ("INSERT INTO proveedores (id_proveedor, nombre_proveedor, telefono, email, direccion) "
                    "VALUES (%s, %s, %s, %s, %s)")
            values = (
                proveedor.id_proveedor,
                proveedor.nombre_proveedor,
                proveedor.telefono,
                proveedor.email,
                proveedor.direccion
            )
            self.db.execute_query(query, values)
        except Exception as e:
            print(f"Error al crear proveedor: {e}")

    def obtener_proveedor(self, id_proveedor):
        """
        Obtiene un proveedor por su ID.
        :param id_proveedor: int
        :return: Supplier o None
        """
        try:
            query = "SELECT id_proveedor, nombre_proveedor, telefono, email, direccion FROM proveedores WHERE id_proveedor = %s"
            row = self.db.execute_query(query, (id_proveedor,), fetch_one=True)
            if row:
                return Supplier(*row)
            return None
        except Exception as e:
            print(f"Error al obtener proveedor: {e}")
            return None

    def actualizar_proveedor(self, proveedor):
        """
        Actualiza los datos de un proveedor existente.
        :param proveedor: Supplier
        """
        try:
            query = ("UPDATE proveedores SET nombre_proveedor=%s, telefono=%s, email=%s, direccion=%s "
                    "WHERE id_proveedor=%s")
            values = (
                proveedor.nombre_proveedor,
                proveedor.telefono,
                proveedor.email,
                proveedor.direccion,
                proveedor.id_proveedor
            )
            self.db.execute_query(query, values)
        except Exception as e:
            print(f"Error al actualizar proveedor: {e}")

    def eliminar_proveedor(self, id_proveedor):
        """
        Elimina un proveedor por su ID.
        :param id_proveedor: int
        """
        try:
            query = "DELETE FROM proveedores WHERE id_proveedor = %s"
            self.db.execute_query(query, (id_proveedor,))
        except Exception as e:
            print(f"Error al eliminar proveedor: {e}")

    def listar_proveedores(self):
        """
        Devuelve una lista de todos los proveedores.
        :return: list[Supplier]
        """
        try:
            query = "SELECT id_proveedor, nombre_proveedor, telefono, email, direccion FROM proveedores"
            rows = self.db.execute_query(query, fetch_all=True)
            if rows is None:
                return []
            if isinstance(rows, list):
                return [Supplier(*row) for row in rows]
            try:
                return [Supplier(*rows)]
            except Exception:
                return []
        except Exception as e:
            print(f"Error al listar proveedores: {e}")
            return []

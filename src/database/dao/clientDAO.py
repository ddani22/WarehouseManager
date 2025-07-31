# DAO para la entidad Cliente
from src.database.db_manager import db_manager, host, user, password, database
from src.models.client import Client


class clientDAO:
    """
    DAO para operaciones CRUD sobre la entidad Cliente.
    """
    def __init__(self):
        self.db = db_manager(host, user, password, database)

    def crear_cliente(self, cliente):
        """
        Inserta un nuevo cliente en la base de datos.
        :param cliente: Client
        """
        try:
            query = ("INSERT INTO clientes (id_cliente, nombre_cliente, direccion, telefono, email) "
                    "VALUES (%s, %s, %s, %s, %s)")
            values = (cliente.id_cliente, cliente.nombre_cliente, cliente.direccion, cliente.telefono, cliente.email)
            self.db.execute_query(query, values)
        except Exception as e:
            print(f"Error al crear cliente: {e}")

    def obtener_cliente(self, id_cliente):
        """
        Obtiene un cliente por su ID.
        :param id_cliente: int
        :return: Client o None
        """
        try:
            query = "SELECT * FROM clientes WHERE id_cliente = %s"
            row = self.db.execute_query(query, (id_cliente,), fetch_one=True)
            if row:
                return Client(*row)
            return None
        except Exception as e:
            print(f"Error al obtener cliente: {e}")
            return None

    def actualizar_cliente(self, cliente):
        """
        Actualiza los datos de un cliente existente.
        :param cliente: Client
        """
        try:
            query = ("UPDATE clientes SET nombre_cliente=%s, direccion=%s, telefono=%s, email=%s "
                    "WHERE id_cliente=%s")
            values = (cliente.nombre_cliente, cliente.direccion, cliente.telefono, cliente.email, cliente.id_cliente)
            self.db.execute_query(query, values)
        except Exception as e:
            print(f"Error al actualizar cliente: {e}")

    def eliminar_cliente(self, id_cliente):
        """
        Elimina un cliente por su ID.
        :param id_cliente: int
        """
        try:
            query = "DELETE FROM clientes WHERE id_cliente = %s"
            self.db.execute_query(query, (id_cliente,))
        except Exception as e:
            print(f"Error al eliminar cliente: {e}")

    def listar_clientes(self):
        """
        Devuelve una lista de todos los clientes.
        :return: list[Client]
        """
        try:
            query = "SELECT id_cliente, nombre_cliente, direccion, telefono, email FROM clientes"
            rows = self.db.execute_query(query, fetch_all=True)
            if rows is None:
                return []
            if isinstance(rows, list):
                return [Client(*row) for row in rows]
            # Si rows no es una lista, intenta convertirlo en lista si es posible
            try:
                return [Client(*rows)]
            except Exception:
                return []
        except Exception as e:
            print(f"Error al listar clientes: {e}")
            return []

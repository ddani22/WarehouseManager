from src.database.db_manager import db_manager, host, user, password, database
from src.models.movement import Movement


class movementDAO:
    """
    DAO para operaciones CRUD sobre la entidad Movimiento.
    """
    def __init__(self):
        self.db = db_manager(host, user, password, database)

    def crear_movimiento(self, movimiento):
        """
        Inserta un nuevo movimiento en la base de datos.
        :param movimiento: movement
        """
        try:
            query = ("INSERT INTO movimientos (id_movimiento, id_producto, tipo_movimiento, cantidad, fecha_movimiento, referencia_origen, id_usuario, id_cliente_proveedor) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
            values = (
                movimiento.id_movimiento,
                movimiento.id_producto,
                movimiento.tipo_movimiento,
                movimiento.cantidad,
                movimiento.fecha_movimiento,
                movimiento.referencia_origen,
                movimiento.id_usuario,
                movimiento.id_cliente_proveedor
            )
            self.db.execute_query(query, values)
        except Exception as e:
            print(f"Error al crear movimiento: {e}")

    def obtener_movimiento(self, id_movimiento):
        """
        Obtiene un movimiento por su ID.
        :param id_movimiento: int
        :return: movement o None
        """
        try:
            query = "SELECT id_movimiento, id_producto, tipo_movimiento, cantidad, fecha_movimiento, referencia_origen, id_usuario, id_cliente_proveedor FROM movimientos WHERE id_movimiento = %s"
            row = self.db.execute_query(query, (id_movimiento,), fetch_one=True)
            if row:
                return Movement(*row)
            return None
        except Exception as e:
            print(f"Error al obtener movimiento: {e}")
            return None

    def actualizar_movimiento(self, movimiento):
        """
        Actualiza los datos de un movimiento existente.
        :param movimiento: movement
        """
        try:
            query = ("UPDATE movimientos SET id_producto=%s, tipo_movimiento=%s, cantidad=%s, fecha_movimiento=%s, referencia_origen=%s, id_usuario=%s, id_cliente_proveedor=%s "
                    "WHERE id_movimiento=%s")
            values = (
                movimiento.id_producto,
                movimiento.tipo_movimiento,
                movimiento.cantidad,
                movimiento.fecha_movimiento,
                movimiento.referencia_origen,
                movimiento.id_usuario,
                movimiento.id_cliente_proveedor,
                movimiento.id_movimiento
            )
            self.db.execute_query(query, values)
        except Exception as e:
            print(f"Error al actualizar movimiento: {e}")

    def eliminar_movimiento(self, id_movimiento):
        """
        Elimina un movimiento por su ID.
        :param id_movimiento: int
        """
        try:
            query = "DELETE FROM movimientos WHERE id_movimiento = %s"
            self.db.execute_query(query, (id_movimiento,))
        except Exception as e:
            print(f"Error al eliminar movimiento: {e}")

    def listar_movimientos(self):
        """
        Devuelve una lista de todos los movimientos.
        :return: list[movement]
        """
        try:
            query = "SELECT id_movimiento, id_producto, tipo_movimiento, cantidad, fecha_movimiento, referencia_origen, id_usuario, id_cliente_proveedor FROM movimientos"
            rows = self.db.execute_query(query, fetch_all=True)
            if rows is None:
                return []
            if isinstance(rows, list):
                return [Movement(*row) for row in rows]
            try:
                return [Movement(*rows)]
            except Exception:
                return []
        except Exception as e:
            print(f"Error al listar movimientos: {e}")
            return []

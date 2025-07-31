# Modelo de movimiento
class Movement:
    """
    Modelo que representa un movimiento de inventario en el sistema de gestión de almacén.
    """
    def __init__(self, id_movimiento, id_producto, tipo_movimiento, cantidad, fecha_movimiento, referencia_origen, id_usuario, id_cliente_proveedor):
        """
        Inicializa un nuevo movimiento.
        :param id_movimiento: int, identificador único del movimiento
        :param id_producto: int, identificador del producto relacionado con el movimiento
        :param cantidad: int, cantidad de producto movido
        :param tipo_movimiento: str, tipo de movimiento (entrada o salida)
        :param fecha_movimiento: str, fecha del movimiento
        :param referencia_origen: str, referencia del origen del movimiento (por ejemplo, número de orden de compra)
        :param id_usuario: int, identificador del usuario que realiza el movimiento
        :param id_cliente_proveedor: int, identificador del cliente o proveedor relacionado con el movimiento
        """
        self.id_movimiento = id_movimiento
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.tipo_movimiento = tipo_movimiento
        self.fecha_movimiento = fecha_movimiento
        self.referencia_origen = referencia_origen
        self.id_usuario = id_usuario
        self.id_cliente_proveedor = id_cliente_proveedor

    def __str__(self):
        """
        Devuelve una representación en cadena del movimiento.
        """
        return f"Movimiento({self.id_movimiento}, {self.id_producto}, {self.cantidad}, {self.tipo_movimiento}, {self.fecha_movimiento}, {self.referencia_origen}, {self.id_usuario}, {self.id_cliente_proveedor})"
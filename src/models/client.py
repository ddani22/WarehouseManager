# Modelo de cliente

class Client:
    """
    Modelo que representa un cliente en el sistema de gestión de almacén.
    """
    def __init__(self, id_cliente, nombre_cliente, telefono, email, direccion):
        """
        Inicializa un nuevo cliente.
        :param id_cliente: int, identificador único del cliente
        :param nombre_cliente: str, nombre del cliente
        :param telefono: str, teléfono de contacto
        :param email: str, correo electrónico
        :param direccion: str, dirección del cliente
        """
        self.id_cliente = id_cliente
        self.nombre_cliente = nombre_cliente
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    def __str__(self):
        """
        Devuelve una representación en cadena del cliente.
        """
        return f"Cliente({self.id_cliente}, {self.nombre_cliente}, {self.telefono}, {self.email}, {self.direccion})"

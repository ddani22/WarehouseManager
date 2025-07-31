# Modelo de proveedor
class Supplier:
    """
    Modelo que representa un proveedor en el sistema de gestión de almacén.
    """
    def __init__(self, id_proveedor, nombre_proveedor, telefono, email, direccion):
        """
        Inicializa un nuevo proveedor.
        :param id_proveedor: int, identificador único del proveedor
        :param nombre_proveedor: str, nombre del proveedor
        :param telefono: str, teléfono de contacto
        :param email: str, correo electrónico
        :param direccion: str, dirección del proveedor
        """
        self.id_proveedor = id_proveedor
        self.nombre_proveedor = nombre_proveedor
        self.telefono = telefono
        self.email = email
        self.direccion = direccion

    def __str__(self):
        """
        Devuelve una representación en cadena del proveedor.
        """
        return f"Proveedor({self.id_proveedor}, {self.nombre_proveedor}, {self.telefono}, {self.email}, {self.direccion})"